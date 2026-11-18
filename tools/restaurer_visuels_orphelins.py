#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - reintegration des deux visuels cinematiques orphelins.

Les reconstructions de pages/saison7-battle-pass.html et
pages/saison7-zombie-endless.html depuis leurs generateurs ont retire les
visuels de tete de page, laissant deux fichiers JPG orphelins :

  img/events/vis-s7news-cinematique.jpg  -> pages/saison7-nouveautes.html
  img/zombies/vis-endless-cinematique.jpg -> pages/saison7-zombie-endless.html

Ce script ajoute un second <figure> dans chaque page, en plus du visuel
d'entree deja present : le visuel d'entree sert d'accroche, le visuel
cinematique sert d'illustration intermediaire.

Idempotent.
"""
import pathlib
import re
import sys

BLOCS = [
    (
        "pages/saison7-nouveautes.html",
        "../img/events/vis-s7news-cinematique.jpg",
        "Mur de newsroom couvert de documents epingles, eclaire par une lampe de bureau",
        "La newsroom de la Saison 7 : les annonces de l'editeur, les correctifs et les Notes de patch y affluent avant chaque mise a jour.",
    ),
    (
        "pages/saison7-zombie-endless.html",
        "../img/zombies/vis-endless-cinematique.jpg",
        "Hangar militaire vide la nuit, caisses sous housses et bureau eclaire",
        "L'Airport hors des vagues : l'entrepot qui sert de point de repli aux operateurs de l'Endless.",
    ),
]


def main():
    for page, src, alt, legende in BLOCS:
        p = pathlib.Path(page)
        s = p.read_text(encoding="utf-8")

        if src in s:
            print("  %s : deja present" % page)
            continue

        from PIL import Image
        dim = Image.open(pathlib.Path("img") / src.replace("../img/", "")).size
        balise = ('<img width="%d" height="%d" src="%s" alt="%s" loading="lazy" decoding="async">'
                  % (dim[0], dim[1], src, alt))

        figure = ('          <figure class="page-figure">\n'
                  '            %s\n'
                  '            <figcaption>%s</figcaption>\n'
                  '          </figure>\n' % (balise, legende))

        # insertion avant la premiere section h2 du contenu
        m = re.search(r'<h2 id=', s)
        if not m:
            print("  [!!] %s : aucune section h2 trouvee" % page)
            return 1
        s = s[:m.start()] + figure + "\n" + s[m.start():]
        p.write_text(s, encoding="utf-8")
        print("  %s : %s insere (%dx%d)" % (page, src.split('/')[-1], dim[0], dim[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
