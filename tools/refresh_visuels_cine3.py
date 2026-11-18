#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integre la 3e vague de visuels cinematiques haute qualite.

Dix visuels photorealistes remplacent des images editoriales de faible
definition :
  - les 6 miniatures de cartes de l'explorateur de cartes (720x480), qui
    etaient des captures de rendu du jeu ;
  - les 4 cartes d'accueil concernees (800x450).

Les visuels officiels de l'editeur (artworks d'armes, d'armures, de
munitions et de gear en 1024x1024) ne sont PAS concernes : ils sont
volontairement conserves en 1024x1024.

Le script :
  1. remplace les references src= dans index.html et js/map-explorer.js ;
  2. recalcule les attributs width/height de chaque balise img concernee,
    a partir des fichiers reels ;
  3. purge les anciennes images si elles ne sont plus referencees.

Idempotent : un second passage ne doit rien changer.
"""
import os
import pathlib
import re
import sys

from PIL import Image

SWAPS = [
    ("img/cards/card-arms.jpg", "img/cards/card-arms-cine.jpg"),
    ("img/cards/card-utopia.jpg", "img/cards/card-utopia-cine.jpg"),
    ("img/cards/card-airport.jpg", "img/cards/card-airport-cine.jpg"),
    ("img/cards/card-armor.jpg", "img/cards/card-armor-cine.jpg"),
    ("img/cards/card-armory.jpg", "img/cards/card-armory-cine.jpg"),
    ("img/cards/card-build.jpg", "img/cards/card-build-cine.jpg"),
    ("img/cards/card-compare.jpg", "img/cards/card-compare-cine.jpg"),
    ("img/cards/card-elysium.jpg", "img/cards/card-elysium-cine.jpg"),
    ("img/cards/card-farmzone.jpg", "img/cards/card-farmzone-cine.jpg"),
    ("img/cards/card-meta.jpg", "img/cards/card-meta-cine.jpg"),
    ("img/cards/card-a545.jpg", "img/cards/card-a545-cine.jpg"),
    ("img/cards/card-farm.jpg", "img/cards/card-farm-cine.jpg"),
    ("img/maps/var-farm.jpg", "img/maps/var-farm-cine.jpg"),
    ("img/maps/var-valley.jpg", "img/maps/var-valley-cine.jpg"),
    ("img/maps/var-airport.jpg", "img/maps/var-airport-cine.jpg"),
    ("img/maps/var-northridge.jpg", "img/maps/var-northridge-cine.jpg"),
    ("img/maps/var-armory.jpg", "img/maps/var-armory-cine.jpg"),
    ("img/maps/var-tvstation.jpg", "img/maps/var-tvstation-cine.jpg"),
    ("img/cards/card-bench.jpg", "img/cards/card-bench-cine.jpg"),
    ("img/cards/card-infected.jpg", "img/cards/card-infected-cine.jpg"),
    ("img/cards/card-meta2.jpg", "img/cards/card-meta2-cine.jpg"),
    ("img/cards/card-meta3.jpg", "img/cards/card-meta3-cine.jpg"),
    ("img/cards/card-northridge.jpg", "img/cards/card-northridge-cine.jpg"),
    ("img/cards/card-operator.jpg", "img/cards/card-operator-cine.jpg"),
    ("img/cards/card-tvstation.jpg", "img/cards/card-tvstation-cine.jpg"),
    ("img/cards/card-valley.jpg", "img/cards/card-valley-cine.jpg"),
]

CIBLES = [
    pathlib.Path("index.html"),
    pathlib.Path("js/map-explorer.js"),
]


def dims(rel):
    p = pathlib.Path(rel)
    if not p.exists():
        return None
    return Image.open(p).size


def corriger_balise(tag, dims_reelles):
    """Recalcule width/height dans une balise img, quel que soit l'ordre."""
    w, h = dims_reelles
    if re.search(r'\bwidth="\d+"', tag):
        tag = re.sub(r'\bwidth="\d+"', 'width="%d"' % w, tag)
    else:
        tag = tag.replace("<img", '<img width="%d"' % w)
    if re.search(r'\bheight="\d+"', tag):
        tag = re.sub(r'\bheight="\d+"', 'height="%d"' % h, tag)
    else:
        tag = tag.replace("<img", '<img height="%d"' % h)
    return tag


def main():
    racine = pathlib.Path(__file__).resolve().parent.parent
    cwd = os.getcwd()
    os.chdir(racine)
    try:
        swaps = 0
        for chemin in CIBLES:
            if not chemin.exists():
                continue
            s = chemin.read_text(encoding="utf-8")
            orig = s
            prefixe = "../" if chemin.suffix == ".js" else ""
            for ancien, nouveau in SWAPS:
                base = pathlib.Path(ancien).name
                d = dims(nouveau)
                if d is None:
                    print("  MANQUANT :", nouveau)
                    continue
                # remplacer le src dans les balises img
                pat = re.compile(r'<img\b[^>]*?src="[^"]*' + re.escape(base) + r'"[^>]*?>')
                nouvelles = []
                for m in pat.finditer(s):
                    tag = m.group(0)
                    tag = re.sub(r'src="[^"]*' + re.escape(base) + r'"',
                                 'src="%s%s"' % (prefixe, nouveau), tag)
                    tag = corriger_balise(tag, d)
                    nouvelles.append(tag)
                if nouvelles:
                    s = pat.sub(lambda _m, it=iter(nouvelles): next(it), s)
                    swaps += 1
            # references hors balise img (js : simple chaine)
            for ancien, nouveau in SWAPS:
                base = pathlib.Path(ancien).name
                s = s.replace("'%s%s'" % (prefixe, ancien), "'%s%s'" % (prefixe, nouveau))
                s = s.replace('"%s%s"' % (prefixe, ancien), '"%s%s"' % (prefixe, nouveau))
            if s != orig:
                chemin.write_text(s, encoding="utf-8")
                print("  mis a jour :", chemin)
            else:
                print("  inchange   :", chemin)

        # purge des anciennes images orphelines
        corpus = ""
        for pat in ("*.html", "pages/*.html", "css/*.css", "js/*.js", "js/*.json"):
            for p in pathlib.Path(".").glob(pat):
                corpus += p.read_text(encoding="utf-8", errors="ignore")
        for ancien, nouveau in SWAPS:
            if pathlib.Path(ancien).name in corpus:
                print("  conserve   : %s (reference subsistante)" % ancien)
                continue
            p = pathlib.Path(ancien)
            if p.exists():
                p.unlink()
                print("  purge      :", ancien)

        print("\ntotal swaps :", swaps)
    finally:
        os.chdir(cwd)
    return 0


if __name__ == "__main__":
    sys.exit(main())
