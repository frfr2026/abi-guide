#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - restauration definitive de pages/saison7-zombie-endless.html.

La purge regex de la vague E a coupe le bloc au premier </div> et l'a laisse
orphelin ; des fragments duplique se sont accumules. Cette page est
reconstruisible depuis tools/build_s8a.py, qui en est le generateur.

On reprend le corps d'origine, on reapplique les transformations
posterieures (hierarchie des titres, identifiants de liens) et on insere le
bloc de veille IA proprement.

Idempotent.
"""
import pathlib
import re
import subprocess
import sys

PAGE = pathlib.Path("pages/saison7-zombie-endless.html")
BUILD = pathlib.Path("tools/build_s8a.py")
BACKUP = pathlib.Path("/tmp/ze_body_source.txt")

# transformations posterieures a build_s8a.py
TITRES = [
    ("<h4>", '<h3 class="h4">'),
    ("</h4>", "</h3>"),
]

LIENS = [
    ("<a href=\"saison7-zombie-infected-zone.html\">", "<a href=\"saison7-zombie-infected-zone.html\" id=\"lnk-saison7-zombie-endless-105\">"),
]


def extraire_source():
    """Relit build_s8a.py et en extrait le corps de la page endless."""
    src = BUILD.read_text(encoding="utf-8")
    m = re.search(r'endless = """(.*?)"""', src, re.S)
    if not m:
        print("  [!!] corps 'endless' introuvable dans build_s8a.py")
        return None
    BACKUP.write_text(m.group(1), encoding="utf-8")
    return m.group(1)


def bloc_ia():
    src = pathlib.Path("tools/refresh_veille_nov2026e.py").read_text(encoding="utf-8")
    m = re.search(r'IA = """(.*?)"""', src, re.S)
    if not m:
        print("  [!!] bloc IA introuvable")
        return None
    return m.group(1).rstrip()


def main():
    body = extraire_source()
    if body is None:
        return 1
    print("  corps source : %d caracteres" % len(body))

    # transformations de hierarchie
    for avant, apres in TITRES:
        body = body.replace(avant, apres)
    for avant, apres in LIENS:
        body = body.replace(avant, apres)

    # bloc de veille IA : insertion avant la section 4
    bloc = bloc_ia()
    if bloc is None:
        return 1
    anc = '<h2 id="astuces">'
    if anc not in body:
        anc = re.search(r'<h2 id="[^"]*">\s*4\.\s*Astuces de terrain', body)
        if not anc:
            print("  [!!] ancre section 4 introuvable")
            return 1
        anc = anc.group(0)
    o = "<!--VEILLE-E:IA:OPEN-->"
    f = "<!--VEILLE-E:IA:CLOSE-->"
    body = body.replace(anc, o + "\n" + bloc + "\n" + f + "\n" + anc, 1)

    # on remplace le contenu de l'article dans la page actuelle
    courant = PAGE.read_text(encoding="utf-8")
    d = courant.find('<article class="content-col">')
    fin = courant.find("</article>", d)
    if d == -1 or fin == -1:
        print("  [!!] article introuvable")
        return 1
    page = courant[:d] + '<article class="content-col">\n' + body + courant[fin:]

    PAGE.write_text(page, encoding="utf-8")
    print("  page restauree (%d caracteres)" % len(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
