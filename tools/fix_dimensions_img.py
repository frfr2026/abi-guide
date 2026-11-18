#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige les attributs width/height des <img> pour qu'ils correspondent aux
dimensions REELLES du fichier servi.

Les generateurs d'images renvoient des images plus grandes que la version
optimisee publiee sur le site (le pipeline redimensionne avant livraison).
Declarer les dimensions de la source au lieu de celles du fichier induit un
ratio faux : le navigateur reserve un espace incorrect et l'image se decale
au chargement.

Idempotent.
"""
import pathlib
import re
import sys

from PIL import Image

PAGES = pathlib.Path("pages")
IMG_DIR = pathlib.Path("img")


def main():
    total = 0
    cibles = sorted(PAGES.glob("*.html"))
    racine = pathlib.Path(__file__).resolve().parent.parent
    for extra in ("index.html", "404.html"):
        p = racine / extra
        if p.exists():
            cibles.append(p)
    for f in cibles:
        s = f.read_text(encoding="utf-8")
        orig = s

        def repl(m):
            dw, dh, src = int(m.group(1)), int(m.group(2)), m.group(3)
            if src.startswith("data:"):
                return m.group(0)
            p = (f.parent / src).resolve()
            if not p.exists() or p.suffix.lower() not in (".jpg", ".jpeg", ".png"):
                return m.group(0)
            try:
                with Image.open(p) as im:
                    rw, rh = im.size
            except Exception:
                return m.group(0)
            if (dw, dh) == (rw, rh):
                return m.group(0)
            globals()["total"] = globals().get("total", 0) + 1
            print("  fix %-34s %s -> %s" % (src.split("/")[-1], "%dx%d" % (dw, dh), "%dx%d" % (rw, rh)))
            return '<img width="%d" height="%d" src="%s"' % (rw, rh, src)

        s = re.sub(r'<img width="(\d+)" height="(\d+)" src="([^"]+)"', repl, s)
        if s != orig:
            f.write_text(s, encoding="utf-8")
    print("\ntotal :", globals().get("total", 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
