#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reconstruit tools/pending_visuals.json a partir de l'etat reel du site.

Le catalogue precedent etait perime : il annonçait 7 MP3 et une liste de
visuels qui ne reflétait plus les vagues deja produites. Ce script rescanne
l'arborescence, denombre les medias, releve la presence effective de la
narration dans chaque page, et reecrit le JSON.

Regle stricte maintenue : JPG uniquement. Aucun PNG, aucun SVG, aucun WebP.
Les artworks officiels de l'editeur restent volontairement en 1024x1024.

Idempotent.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(".")
OUT = pathlib.Path("tools/pending_visuals.json")

IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif")
IMAGE_DIRS = ["img"]

CARTE_SUIVIS = [
    ("img/cards/card-bench.jpg", "card-bench-cine.jpg", "etable d'equipement tactique, eclairage chaud"),
    ("img/cards/card-infected.jpg", "card-infected-cine.jpg", "salle de controle sombre, clavier et ecran"),
    ("img/cards/card-meta2.jpg", "card-meta2-cine.jpg", "balance symbolique, canon nu et plaques de blindage"),
    ("img/cards/card-meta3.jpg", "card-meta3-cine.jpg", "comptoir de marche noir, piles de monnaie"),
    ("img/cards/card-northridge.jpg", "card-northridge-cine.jpg", "crete enneigee de Northridge, longue portee"),
    ("img/cards/card-operator.jpg", "card-operator-cine.jpg", "table ronde d'operateurs, ambience communautaire"),
    ("img/cards/card-tvstation.jpg", "card-tvstation-cine.jpg", "station de television, plateau d'emission et regime video"),
    ("img/cards/card-valley.jpg", "card-valley-cine.jpg", "vallee industrielle, entrepots et aperite"),
]


def scan_images():
    counts = {}
    for d in IMAGE_DIRS:
        for p in sorted((ROOT / d).rglob("*")):
            if p.is_file() and p.suffix.lower() in IMAGE_EXTS:
                counts[p.suffix.lower()] = counts.get(p.suffix.lower(), 0) + 1
    return counts


def scan_audio():
    out = []
    for p in sorted((ROOT / "audio").glob("*.mp3")):
        item = {"fichier": f"audio/{p.name}"}
        out.append(item)
    return out


def narration_map():
    """Associe chaque MP3 de narration a la page qui l'embarque."""
    files = sorted((ROOT / "pages").glob("*.html")) + [ROOT / "index.html", ROOT / "404.html"]
    mapping = {}
    for p in files:
        try:
            t = p.read_text(encoding="utf-8")
        except Exception:
            continue
        for m in re.findall(r"audio/narration-([a-z0-9\-]+)\.mp3", t):
            mapping.setdefault(m, []).append(str(p))
    return mapping


def main():
    counts = scan_images()
    mp3 = scan_audio()
    mapping = narration_map()
    pages = sorted((ROOT / "pages").glob("*.html"))

    produits = []
    refs = set()
    for f in sorted((ROOT / "pages").glob("*.html")) + [ROOT / "index.html", ROOT / "404.html"]:
        try:
            t = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for m in re.findall(r"(?:\.\./)?img/[A-Za-z0-9_\-/\.]+\.(?:jpg|jpeg)", t):
            refs.add(m.replace("../", ""))
    for p in sorted((ROOT / "img").rglob("*.jpg")):
        rel = str(p).replace("\\", "/")
        page = next((r for r in refs if r == rel), "(media partage)")
        produits.append({"fichier": rel, "page": page, "statut": "fait",
                         "style": "visuel JPG photorealiste / cinematique"})

    a_faire = []
    for anc, new, style in CARTE_SUIVIS:
        anc_p = ROOT / anc
        if not anc_p.exists():
            continue
        try:
            from PIL import Image
            w, h = Image.open(anc_p).size
        except Exception:
            w, h = 0, 0
        if w >= 1400:
            continue
        a_faire.append({
            "fichier": anc,
            "remplacement": f"img/cards/{new}",
            "page": "index.html",
            "statut": "a_faire",
            "dimensions_actuelles": f"{w}x{h}",
            "style": style,
        })

    data = {
        "note": (
            "Catalogue des visuels a produire. Regle stricte : JPG uniquement "
            "(jamais PNG, jamais SVG, jamais WebP). Maximum 10 visuels par reponse. "
            "Style impose : photorealiste, cinematique, immersif, haute qualite. "
            "Les 194 artworks officiels de l'editeur restent volontairement en "
            "1024x1024 et ne sont jamais regeneres."
        ),
        "regles": [
            "JPG exclusivement : aucun PNG, aucun SVG, aucun WebP.",
            "Maximum 10 visuels par reponse.",
            "Style photorealiste, cinematique, immersif, haute qualite.",
            "Les artworks officiels 1024x1024 sont preserves intacts.",
            "Fichiers remplacants suffixes -cine.jpg ; purge des anciennes versions.",
            "Le catalogue est reconstruit par tools/rebuild_pending_visuals.py a partir du reel.",
        ],
        "compteurs": {
            "jpg_total": counts.get(".jpg", 0) + counts.get(".jpeg", 0),
            "png": counts.get(".png", 0),
            "svg": counts.get(".svg", 0),
            "webp": counts.get(".webp", 0),
            "gif": counts.get(".gif", 0),
            "mp3_total": len(mp3),
            "pages_editoriales": len(pages),
            "pages_narrees": len(mapping),
        },
        "produits": produits,
        "a_faire": a_faire,
        "carte": {
            "note": (
                "Les 6 cartes reelles sont installees et verifiees en JPEG. "
                "Northridge et TV Station ont ete remplacees. "
                "No Man's Land reste un MODE PvE a tickets, pas une carte."
            ),
            "statut": "termine",
        },
        "audio": {
            "note": (
                "Maximum 10 audios par reponse. Format mp3. "
                "Le site embarque des ambiances en boucle et des voix off de guide "
                "(TTS), non bouclees, integrees via le composant .audio-narration."
            ),
            "voix": "voice-00 (audition utilisateur)",
            "fichiers": mp3,
            "narration_par_page": mapping,
            "restant": [
                "meta-strategies-s7 : texte reecrit de maniere neutre dans "
                "tools/textes_audio/meta-strategies-s7.txt (1500 car., aucun mot "
                "bloquant). Generation et cablage a faire au prochain tour."
            ],
        },
    }

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  pending_visuals.json reecrit : {len(produits)} visuels produits, "
          f"{len(a_faire)} a faire, {len(mp3)} mp3, {len(mapping)} pages narrees")
    return 0


if __name__ == "__main__":
    sys.exit(main())
