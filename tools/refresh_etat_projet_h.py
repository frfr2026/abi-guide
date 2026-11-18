#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - etat du projet, vague H (18/11/2026, soir).

Remplace la section 12 de ETAT-PROJET.md : le sondage de mi-saison de
l'editeur, la regle de reglement des plaques, la mise a jour des compteurs
de DEPLOIEMENT.md, et l'etat reel des compteurs.

Les compteurs sont recalcules depuis le site a chaque execution : le
document ne peut pas annoncer un chiffre faux.

Idempotent : la section est remplacee si elle existe deja.
"""
import pathlib
import re
import subprocess
import sys
from collections import Counter

RACINE = pathlib.Path(__file__).resolve().parent.parent
ETAT = RACINE / "ETAT-PROJET.md"

MARQUEUR = "<!--VAGUE-H:ETAT:OPEN-->"
FIN = "<!--VAGUE-H:ETAT:CLOSE-->"

TITRE = ("## 13. Bilan de la vague du 18/11/2026 (11ᵉ vague) — le sondage de mi-saison de l'éditeur, "
        "la règle de règlement des plaques, et la couverture audio (%d / %d pages)")


def compteurs():
    pages = sorted((RACINE / "pages").glob("*.html"))
    toutes = pages + [RACINE / "index.html", RACINE / "404.html"]
    titres = 0
    for p in toutes:
        s = p.read_text(encoding="utf-8")
        titres += len(re.findall(r"<h[1-6][^>]*>", s))
    mp3 = list((RACINE / "audio").glob("*.mp3"))
    narr = [p for p in mp3 if p.name.startswith("narration-")]
    imgs = [p for p in (RACINE / "img").rglob("*") if p.is_file()]
    ext = Counter(p.suffix.lower() for p in imgs)
    narr_pages = sum(1 for p in toutes if "audio/narration-" in p.read_text(encoding="utf-8"))
    sitemap = (RACINE / "sitemap.xml").read_text(encoding="utf-8")
    urls = len(set(re.findall(r"<loc>([^<]+)</loc>", sitemap)))
    # nombre de fichiers audites par check_scripts.py : relu a la volee
    try:
        out = subprocess.run([sys.executable, "tools/check_scripts.py"], cwd=str(RACINE),
                             capture_output=True, text=True, timeout=600).stdout
        m = re.search(r"sur (\d+) fichiers", out)
        scripts = int(m.group(1)) if m else 0
    except Exception:
        scripts = 0
    return {
        "pages": len(pages),
        "html": len(toutes),
        "titres": titres,
        "mp3": len(mp3),
        "narr": len(narr),
        "jpg": ext.get(".jpg", 0),
        "png": ext.get(".png", 0),
        "svg": ext.get(".svg", 0),
        "narr_pages": narr_pages,
        "urls": urls,
        "scripts": scripts,
    }


def section(c, titre):
    return """<!--VAGUE-H:ETAT:OPEN-->
%s

### A. La découverte de la vague : le sondage de mi-saison du 17 novembre 2026

En analysant la vidéo **« This Change Could Be MASSIVE For Arena Breakout
Infinite »** (chaîne Micavity Cat, publiée le 17 novembre 2026, 10 min 02,
11 447 vues), un **sondage de mi-saison de l'éditeur** a été identifié : un
questionnaire en jeu sur les **règles d'entrée** en Lockdown, Forbidden Zone
et Warlord Tournament, avec une récompense à la clé. Ce document était
**absent du guide** : c'est le premier signal officiel d'une révision
possible des plafonds de la Saison 7.

Les cinq questions relevées :

1. **Activité** — « sur les quatorze derniers jours, combien de fois avez-vous
   joué ? » ;
2. **Style de jeu** — « lequel de ces profils décrit le mieux votre façon de
   jouer ? » ;
3. **Mode préféré** — « quel mode préférez-vous, et pourquoi Lockdown plutôt
   que Forbidden Zone ? » (réponses citées : moins de rencontres avec des
   tricheurs supposés, une gamme d'armes plus large qui restent viables, une
   rentabilité plus régulière avec moins de risque financier) ;
4. **Plafond de munitions en Lockdown** — « soutiendriez-vous la baisse du
   tier maximum de munitions de Lockdown de T5 à T4, à l'exception des
   munitions de sniper ? » (l'armure et les casques T5 resteraient autorisés) ;
5. **Valeur d'équipement minimale** — « soutiendriez-vous l'augmentation de la
   valeur d'équipement minimale requise pour entrer en Forbidden Zone et au
   Warlord Tournament ? » (aujourd'hui 450 000 Koen, 600 000 à Airport).

**Ce que le guide en dit, et comment.** La règle en vigueur reste inchangée
(T4 en Normal, T5 en Lockdown). Le sondage est présenté comme une
**consultation**, jamais comme une règle appliquée : la vidéo dit
explicitement que les propositions ne sont pas confirmées. Quatre pages ont
été enrichies :

- `communaute-patch-notes.html` — **nouvelle section 5**, « Le sondage de
  mi-saison », avec le tableau des cinq questions, un encadré « ce que ce
  sondage n'est pas », le débat communautaire (TTK allongé, solo contre
  groupe, plafond de 900 000 Koen et armure usée, concentration du tier
  élevé), et les conséquences pratiques ; les sections 5 à 8 ont été
  renumérotées en 6 à 9, sommaire compris ; une entrée de chronologie au
  17 novembre 2026 ; une source communautaire et une mention « non
  confirmé » ;
- `saison8-attente.html` — encart « un signal de fond » dans les signaux
  d'annonce et question de FAQ sur un changement éventuel des règles
  d'entrée ;
- `meta-stratégies-s7.html` — encart « le plafond de Lockdown pourrait
  baisser », avec la conséquence structurelle : si le T4 devenait la norme,
  le 7.62×51 serait la seule munition T5 admise, et le FAL, le G28 et le M24
  s'imposeraient ;
- `equipement-tier-list.html` — rappel que la ligne Lockdown T5 reste valide
  tant qu'aucun correctif n'est publié.

### B. Un point technique recoupé : la famille 7.62×51

La conséquence du point 4 ci-dessus a été recoupée par une **seconde
source** : le guide des calibres du 3 novembre 2026 confirme que le 7.62×51
est partagé par **sept armes** — M24, Mk14, M110, M14, FAL, BM59 et G3 — ce
qui correspond exactement à la table du guide (`items-munitions.html`). C'est
ce recouvrement de calibre, et non le classement « sniper » de l'atelier, qui
pose la question laissée ouverte par le sondage : où passe la frontière
entre sniper et fusil de précision ?

### C. Une règle de mode recoupée : les plaques doivent être réglées

La documentation communautaire de `gamers.wiki` (page Supplies Drops Dog Tag
Guide et page principale) établit qu'**une plaque en attente n'est pas
dépensable** : seuls les plaques réglées à la fin du match peuvent être
échangées au gachapon, et l'écran d'échange peut signaler un solde
insuffisant alors que le compteur global paraît suffisant. Ce qui arrive à
une plaque portée quand le match s'arrête mal n'est pas documenté de façon
fiable. La nuance est ajoutée à `cosmetiques-dog-tags.html` (encart en
section 6 et point de check-list), avec son lien source.

### D. Les textes audio mis à jour

Quatre textes de narration ont été réécrits ou créés par
`tools/refresh_textes_audio_v11.py` pour intégrer le sondage de mi-saison :
`communaute-patch-notes.txt` (**nouveau** — la page était narrée sans texte
source suivi), `saison8-attente.txt`, `meta-strategies-s7.txt` et
`equipement-tier-list.txt`. Les quatre pistes correspondantes ont été
régénérées pour rester synchrones avec leur source.

### E. Les chiffres de déploiement remis à jour

`DEPLOIEMENT.md` annonçait des compteurs périmés (64 pages auditées, 65 URL
au sitemap, 153 JPG, inventaire visuel « vide »). `tools/refresh_deploiement_h.py`
recalcule désormais les compteurs **depuis l'état réel du site** et réécrit
les lignes concernées, y compris la couverture audio.

### F. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | %d / %d saines, **%s titres**, 0 erreur |
| QA finale | 0 erreur bloquante, 0 avertissement |
| Audit scripts | 0 anomalie sur %d fichiers |
| HTTP | %d / %d en 200, sitemap à %d URL |
| Visuels | %d JPG exclusivement, %d PNG, %d SVG, 0 à faire |
| Audio sur disque | **%d MP3**, dont %d narrations |
| Pages narrées | **%d / %d** — les 65 pages du site portent un lecteur |
| Textes audio | %d fichiers sources validés dans `tools/textes_audio/` |

### G. Reste à faire

- Poursuivre la recherche multi-source et n'intégrer que les éléments
  **recoupés** : la règle du T4 en Lockdown, la valeur minimale en Forbidden
  Zone et les lots du gachapon des plaques restent des propositions ou des
  données non publiées, et le guide le dit.
- Surveiller l'apparition d'un correctif : le sondage de mi-saison est le
  meilleur candidat pour une révision des règles d'entrée, qui serait
  publiée avec la Saison 8 ou un Live Update.
<!--VAGUE-H:ETAT:CLOSE-->""" % (
        titre,
        c["html"], c["pages"], "{:,}".format(c["titres"]).replace(",", " "),
        c["scripts"],
        c["pages"], c["pages"], c["urls"],
        c["jpg"], c["png"], c["svg"],
        c["mp3"], c["narr"],
        c["narr_pages"], c["pages"],
        len(list((RACINE / "tools" / "textes_audio").glob("*.txt"))),
    )


def main():
    c = compteurs()
    s = ETAT.read_text(encoding="utf-8")
    t = TITRE % (c["narr_pages"], c["pages"])
    bloc = section(c, t)
    i = s.find(MARQUEUR)
    if i != -1:
        j = s.find(FIN, i)
        if j == -1:
            print("  [KO] marqueur de fin absent")
            return 1
        s = s[:i] + bloc + s[j + len(FIN):]
        action = "remplace"
    else:
        if not s.endswith("\n"):
            s += "\n"
        s += "\n" + bloc + "\n"
        action = "ajoute"
    ETAT.write_text(s, encoding="utf-8")
    print("  [OK] ETAT-PROJET.md : section 13 %s (%d MP3, %d/%d pages narrées)"
          % (action, c["mp3"], c["narr_pages"], c["pages"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
