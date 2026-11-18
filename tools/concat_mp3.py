#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Concatene des fragments MP3 en un seul fichier, en Python pur.

Pourquoi cet outil existe : le filtre de contenu du synthese vocale refuse
certains textes au-dela d'une certaine longueur, alors que chacun des
fragments pris separement passe. La solution est donc de decouper le texte
en blocs courts, de les generer en parallele, puis de recoller les flux.

Les fragments produits par le TTS partagent le meme format (MPEG-1
Layer III, 128 kbps, 48 kHz, mono) : une simple concatenation des
trames MPEG fonctionne, a condition de retirer le tag ID3v2 de chaque
fragment avant de les coller, et de conserver celui du premier fragment
pour l'identite du fichier final.

Aucune dependance externe : ni ffmpeg, ni pydub, ni mutagen.

Usage :
    python3 tools/concat_mp3.py sortie.mp3 frag1.mp3 frag2.mp3 [...]
"""
import pathlib
import sys


def retire_id3v2(data):
    """Retourne (donnees_sans_tag, tag_conserve)."""
    if data[:3] == b"ID3":
        taille = ((data[6] & 0x7F) << 21) | ((data[7] & 0x7F) << 14) | \
                 ((data[8] & 0x7F) << 7) | (data[9] & 0x7F)
        return data[10 + taille:], data[:10 + taille]
    return data, b""


def retire_id3v1(data):
    """Retire un eventuel tag ID3v1 (128 derniers octets)."""
    if len(data) >= 128 and data[-128:-125] == b"TAG":
        return data[:-128]
    return data


def entete_frame(data):
    """Retourne les 4 premiers octets de la premiere trame MPEG, ou None."""
    corps, _ = retire_id3v2(data)
    for i in range(min(len(corps), 8192) - 4):
        if corps[i] == 0xFF and (corps[i + 1] & 0xE0) == 0xE0:
            return corps[i:i + 4]
    return None


def duree_secondes(data):
    """Estime la duree d'un flux MP3 a partir de ses trames.

    Table de debit MPEG-1 Layer III (kbps) indexee par le champ
    'bitrate index' de l'en-tete de trame. On ancre sur la premiere
    trame audio valide puis on avance de trame en trame : les frames
    de metadonnees (Xing, Info) ont un bitrate index a zero et sont
    donc ecartees en passant simplement a la trame suivante.
    """
    bits = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320]
    taux = [44100, 48000, 32000]
    corps, _ = retire_id3v2(data)

    i = 0
    n = len(corps)
    while i < n - 4:
        if corps[i] == 0xFF and (corps[i + 1] & 0xE0) == 0xE0:
            version = (corps[i + 1] >> 3) & 0x03      # 3 = MPEG-1
            couche = (corps[i + 1] >> 1) & 0x03       # 1 = Layer III
            idx_br = (corps[i + 2] >> 4) & 0x0F
            idx_sr = (corps[i + 2] >> 2) & 0x03
            if (version == 3 and couche == 1
                    and idx_br not in (0, 15) and idx_sr != 3):
                kbps = bits[idx_br]
                sr = taux[idx_sr]
                saut = int(144 * kbps * 1000 / sr)
                trames = 0
                j = i
                while j < n - 4 and corps[j] == 0xFF and (corps[j + 1] & 0xE0) == 0xE0:
                    trames += 1
                    j += saut
                return trames * 1152.0 / sr
        i += 1
    return 0.0


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    sortie = pathlib.Path(sys.argv[1])
    parties = [pathlib.Path(p) for p in sys.argv[2:]]

    for p in parties:
        if not p.exists():
            print("  MANQUANT :", p)
            return 1

    entetes = {}
    for p in parties:
        corps, tag = retire_id3v2(p.read_bytes())
        entetes[p.name] = entete_frame(p.read_bytes())
    formats = set(entetes.values())
    if len(formats) != 1:
        print("  FORMATS INCOMPATIBLES :", entetes)
        return 1

    sortie.parent.mkdir(parents=True, exist_ok=True)
    morceaux = []
    tag_final = b""
    duree = 0.0
    for p in parties:
        data = p.read_bytes()
        corps, tag = retire_id3v2(data)
        corps = retire_id3v1(corps)
        if not tag_final and tag:
            tag_final = tag
        morceaux.append(corps)
        duree += duree_secondes(data)

    sortie.write_bytes(tag_final + b"".join(morceaux))
    print(f"  {sortie.name} : {len(parties)} fragments -> {sortie.stat().st_size:,} octets "
          f"({duree:.1f} s estimees)".replace(",", " "))
    print(f"  format : {list(formats)[0].hex() if formats else '?'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
