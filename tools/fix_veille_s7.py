#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrections post-integration des blocs de veille du 18/11/2026 :

1. Les callouts inseres doivent vivre DANS une section h2, jamais avant le
   premier h2 (sinon saut de niveau h1 -> h3, casse par qa_final.py).
   On les deplace apres le premier h2 de la page.

2. Purge des mots anglais laisses dans la prose francaise ("Known",
   "regularly", "counting", "ICV").

Idempotent.
"""
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")

# page -> marqueur unique du bloc a deplacer
DEPLACER = [
    ("equipement-casques.html", "En S7, la tête n'est plus une seule zone"),
    ("saison7-utopia.html", "Trois sections de mission qu'il vaut mieux contourner"),
    ("equipement-headsets.html", "Le reverse lean ne masque plus la tête"),
    ("items-medical.html", "Un membre noirci ne se répare pas"),
]

# substitutions de mots anglais restants dans la prose
MOTS = [
    ("est contre-intuitive et Known de la plupart des joueurs du\n            top",
     "est contre-intuitive et connue de la plupart des meilleurs\n            joueurs"),
    ("qu'assez regularly", "qu'assez régulièrement"),
    ("un joueur qui counting sur cette posture",
     "un joueur qui comptait sur cette posture"),
    ("Alignment presentationnent", "présentent"),
    ("trophées(ICV)", "trophées"),
]


def extraire_bloc(s, marqueur):
    """Retourne (bloc, debut, fin) du div.callout contenant marqueur."""
    for m in re.finditer(r'<div class="callout[^"]*">.*?</div>', s, re.S):
        if marqueur in m.group(0):
            return m.group(0), m.start(), m.end()
    return None, -1, -1


def main():
    total = 0
    for page, marqueur in DEPLACER:
        f = PAGES / page
        s = f.read_text(encoding="utf-8")
        bloc, deb, fin = extraire_bloc(s, marqueur)
        if bloc is None:
            print("  absent :", page)
            continue
        # le bloc est-il deja apres un h2 ?
        avant = s[:deb]
        dernier_h2 = None
        for m in re.finditer(r'<h2[^>]*>.*?</h2>', avant, re.S):
            dernier_h2 = m
        if dernier_h2 is not None and dernier_h2.end() < deb:
            print("  deja bien place :", page)
            continue
        # deplacer : retirer puis reinserer juste apres le premier h2
        s2 = s[:deb] + s[fin:]
        m2 = re.search(r'<h2[^>]*>.*?</h2>', s2, re.S)
        assert m2, page
        insert = m2.end()
        s2 = s2[:insert] + "\n" + bloc + s2[insert:]
        f.write_text(s2, encoding="utf-8")
        total += 1
        print("  deplace :", page)

    # purge des mots anglais
    for f in list(PAGES.glob("*.html")):
        s = f.read_text(encoding="utf-8")
        orig = s
        for a, b in MOTS:
            s = s.replace(a, b)
        if s != orig:
            f.write_text(s, encoding="utf-8")
            total += 1
            print("  mots   :", f.name)

    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
