#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integrate les visuels cinematiques de key art de page et purge les
versions precedentes une fois qu'elles ne sont plus referencees.

Les visuels remplacants portent le suffixe -cinematique.jpg. La purge
ne concerne QUE les fichiers cites dans SWAPS : ni les artworks officiels
de l'editeur en 1024x1024, ni les favicons, ni les images Open Graph,
qui ne sont pas concernes.

Le script :
  1. remplace les references src= dans les HTML et les JS ;
  2. recalcule les attributs width/height a partir des fichiers reels ;
  3. purge les anciennes images devenues orphelines.

Idempotent : un second passage ne doit rien changer.
"""
import os
import pathlib
import re
import sys

from PIL import Image

SWAPS = [
    ("img/meta/vis-strategies.jpg", "img/meta/vis-strategies-cinematique.jpg"),
    ("img/items/vis-valeur.jpg", "img/items/vis-valeur-cinematique.jpg"),
    ("img/meta/vis-tierlist.jpg", "img/meta/vis-tierlist-cinematique.jpg"),
    ("img/armes/vis-tierlist.jpg", "img/meta/vis-tierlist-cinematique.jpg"),
    ("img/meta/vis-roles.jpg", "img/meta/vis-roles-cinematique.jpg"),
    ("img/meta/vis-optimizer.jpg", "img/meta/vis-optimizer-cinematique.jpg"),
    ("img/zombies/vis-research.jpg", "img/zombies/vis-research-cinematique.jpg"),
    ("img/zombies/vis-infected.jpg", "img/zombies/vis-infected-cinematique.jpg"),
    ("img/items/vis-koen.jpg", "img/items/vis-koen-cinematique.jpg"),
    ("img/items/vis-medical.jpg", "img/items/vis-medical-cinematique.jpg"),
    ("img/events/vis-supplies.jpg", "img/events/vis-supplies-cinematique.jpg"),
    ("img/events/vis-warlord.jpg", "img/events/vis-warlord-cinematique.jpg"),
    ("img/communaute/vis-patch.jpg", "img/communaute/vis-patch-cinematique.jpg"),
]

CIBLES = (
    [pathlib.Path("index.html"), pathlib.Path("404.html"),
     pathlib.Path("js/map-explorer.js")]
    + sorted(pathlib.Path("pages").glob("*.html"))
)


def dims(rel):
    p = pathlib.Path(rel)
    if not p.exists():
        return None
    return Image.open(p).size


def corriger_balise(tag, d):
    w, h = d
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
            prefixe = "../" if (chemin.suffix == ".js"
                             or chemin.parent.name == "pages") else ""
            for ancien, nouveau in SWAPS:
                base = pathlib.Path(ancien).name
                d = dims(nouveau)
                if d is None:
                    print("  MANQUANT :", nouveau)
                    continue
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
            for ancien, nouveau in SWAPS:
                base = pathlib.Path(ancien).name
                s = s.replace("'%s%s'" % (prefixe, ancien), "'%s%s'" % (prefixe, nouveau))
                s = s.replace('"%s%s"' % (prefixe, ancien), '"%s%s"' % (prefixe, nouveau))
            if s != orig:
                chemin.write_text(s, encoding="utf-8")
                print("  mis a jour :", chemin)

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
