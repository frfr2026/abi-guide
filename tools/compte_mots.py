#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compteur de mots canonique du site ABI NEXUS.

Methode de reference : on retire les <script> et les <style>, on retire
les balises, et on compte les mots du texte rendu. Les entites HTML
(&nbsp;, &amp;, ...) sont COMPTEES comme des mots : c'est la methode qui
a produit le volume de reference du projet, et elle est stable dans le
temps.

Elle inclut la navigation et les pieds de page (qui sont du texte
reellement affiche au lecteur) mais exclut le code.

Recalibrage du 18 novembre 2026 : l'ancienne valeur de reference de
137 385 mots, plus les enrichissements de la journee (items-cles puis
les quatre pages de veille), redonne exactement 140 105 mots.

Usage :
    python3 tools/compte_mots.py            # resume
    python3 tools/compte_mots.py --pages    # detail par page
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(".")


def texte_compte(f):
    s = f.read_text(encoding="utf-8")
    s = re.sub(r"<script\b.*?</script>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<style\b.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    pages = sorted((ROOT / "pages").glob("*.html"))
    detail = "--pages" in sys.argv

    lignes = []
    total = 0
    for f in pages:
        n = len(texte_compte(f).split())
        total += n
        lignes.append((f.name, n))

    if detail:
        for nom, n in sorted(lignes, key=lambda x: x[1]):
            print(f"  {n:6d}  {nom}")
        print()

    moy = total // len(lignes) if lignes else 0
    sous = [(n, c) for n, c in lignes if c < 1300]
    print(f"  Pages editoriales : {len(lignes)}")
    print(f"  Volume de texte   : {total:,} mots".replace(",", " "))
    print(f"  Moyenne           : {moy:,} mots/page".replace(",", " "))
    print(f"  Sous 1 300 mots   : {len(sous)}" + (f" -> {sous}" if sous else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
