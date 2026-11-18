#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restaure la structure HTML de equipement-tier-list.html.

Suite au remplacement des sections dupliquees, la page avait perdu :
  - la colonne <aside> de sommaire (sommaire interne de la page) ;
  - les fermetures </div> de la grille .page-layout et du conteneur ;
  - le bloc <h2 id="faq"> duplique, supprime a tort.

Ce script retablit une structure valide et coherente avec les autres pages
du site (voir pages/equipement-armures.html comme gabarit).

Idempotent : si le sommaire est deja present, le script ne fait rien.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/equipement-tier-list.html")

SOMMAIRE = """      <aside class="page-aside">
        <nav class="toc" aria-label="Sommaire de la page">
          <p class="toc-title">Sur cette page</p>
          <a href="#methodo" id="lnk-equipement-tier-list-095">1. Méthodologie</a>
          <a href="#tier-list" id="lnk-equipement-tier-list-096">2. Tier List Équipement S7</a>
          <a href="#notes" id="lnk-equipement-tier-list-097">3. Les découvertes S7</a>
          <a href="#par-mode" id="lnk-equipement-tier-list-098">4. Build type par mode</a>
          <a href="#classement-mode" id="lnk-equipement-tier-list-099">5. Lire le classement par mode</a>
          <a href="#pieces-cles" id="lnk-equipement-tier-list-100">6. Les pièces clés</a>
          <a href="#enveloppe-budget" id="lnk-equipement-tier-list-101">7. Trois enveloppes</a>
          <a href="#erreurs-classement" id="lnk-equipement-tier-list-102">8. Les erreurs de lecture</a>
          <a href="#faq-tier" id="lnk-equipement-tier-list-103">9. Questions fréquentes</a>
        </nav>
      </aside>
"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    if 'class="page-aside"' in s:
        print("  sommaire deja present")
    else:
        m = re.search(r'(<h2 id="methodo")', s)
        if not m:
            print("  ANCRE methodo introuvable")
            return 1
        s = s[: m.start()] + SOMMAIRE + "\n      <div class=\"page-content\">\n" + s[m.start():]
        print("  sommaire + ouverture page-content inseres")

    # fermeture de la grille et du <main>
    if "</aside>\n      </div>\n    </div>\n  </main>" not in s:
        j = s.find('<footer class="site-footer">')
        if j == -1:
            print("  footer introuvable")
            return 1
        ferme = "      </div>\n    </div>\n  </main>\n\n  "
        s = s[:j] + ferme + s[j:]
        print("  fermetures de grille et </main> restaurees")

    PAGE.write_text(s, encoding="utf-8")

    body = s[s.find("<body"): s.find("</body>")]
    o = len(re.findall(r"<div\b", body))
    c = len(re.findall(r"</div>", body))
    print("  div ouverts/fermes : %d / %d" % (o, c))
    return 0 if o == c else 1


if __name__ == "__main__":
    sys.exit(main())
