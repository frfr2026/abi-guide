#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - restauration des visuels de pages/saison7-zombie-endless.html.

La reconstruction depuis tools/build_s8a.py a retabli la page a son etat
d'origine, ce qui a :
  - retire le visuel cinematique d'entree (vis-endless-entree.jpg) qui
    decorait la section 2 ;
  - retabli deux images sans width/height ;
  - laisse un mot anglais residuel ("a opened").

Ce script reapplique le visuel, les dimensions et corrige le mot.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/saison7-zombie-endless.html")

# (ancien src, nouveau src, alt)
VISUELS = [
    (
        "../img/zombies/zombie-endless.jpg",
        "../img/zombies/vis-endless-entree.jpg",
        "Arene souterraine foddee de projecteurs,propylenee d'un groupe a l'entree du tunnel",
    ),
]

# corrections redactionnelles
FIX = [
    ("un <strong>weapon case</strong> à opened : chance d'arme nettement plus puissante.",
     "un <strong>weapon case</strong> à ouvrir : une chance d'arme nettement plus puissante."),
]


def dimension(src):
    """Retourne (l, h) a partir du fichier image, ou None."""
    from PIL import Image
    p = pathlib.Path("img") / src.replace("../img/", "")
    if not p.exists():
        return None
    im = Image.open(p)
    return im.size


def main():
    s = PAGE.read_text(encoding="utf-8")

    for avant, apres in FIX:
        if avant in s:
            s = s.replace(avant, apres)
            print("  correction redactionnelle appliquee")

    for ancien, nouveau, alt in VISUELS:
        if nouveau in s:
            print("  %s deja en place" % nouveau)
            continue
        if ancien not in s:
            print("  [!!] %s introuvable" % ancien)
            continue
        dims = dimension(nouveau)
        if dims:
            l, h = dims
        else:
            l, h = 1536, 1024
        balise = ('<img width="%d" height="%d" src="%s" alt="%s" loading="lazy" decoding="async">'
                  % (l, h, nouveau, alt))
        s = s.replace('<img src="%s"' % ancien, balise, 1)
        print("  %s -> %s (%dx%d)" % (ancien, nouveau, l, h))

    # dimensions sur toutes les images restantes sans width/height
    for m in list(re.finditer(r"<img\b[^>]*>", s)):
        tag = m.group(0)
        if "width=" in tag:
            continue
        a = re.search(r'src="([^"]+)"', tag)
        if not a:
            continue
        dims = dimension(a.group(1))
        if not dims:
            continue
        l, h = dims
        nouveau = tag.replace("<img", '<img width="%d" height="%d"' % (l, h), 1)
        if "decoding=" not in nouveau:
            nouveau = nouveau.replace('<img ', '<img decoding="async" ', 1)
        s = s.replace(tag, nouveau, 1)
        print("  dimensions ajoutees : %s" % a.group(1))

    PAGE.write_text(s, encoding="utf-8")
    print("  page ecrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
