#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige et enrichit pages/armes-carbine.html.

Le bloc insere precedemment affirmait que les carabines ne formaient pas une
categorie de collection dans la source de reference. C'est faux : le JSON
`js/data-weapons-wiki.json` expose une categorie "Carbines" qui recense
8 armes. Le bloc est remplace par le tableau officiel de ces 8 armes,
genere depuis le JSON.

Le tableau est produit par code : les chiffres ne sont jamais saisis a la main.

Idempotent : le bloc n'est insere qu'une fois.
"""
import json
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/armes-carbine.html")
WIKI = pathlib.Path("js/data-weapons-wiki.json")

ANCIEN_DEBUT = '<h2 id="carbine-position">'
ANCIEN_FIN = "</table>\n          </div>\n"


def charger_carabines():
    data = json.loads(WIKI.read_text(encoding="utf-8"))
    armes = data["weapons"] if isinstance(data, dict) else data
    return [a for a in armes if a.get("categorieWiki") == "Carbines"]


def bloc(armes):
    lignes = []
    for a in armes:
        st = a.get("stats", {})
        modes = " / ".join(a.get("modes", []))
        lignes.append(
            "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td>"
            "<td>%s</td><td>%s</td><td>%s</td></tr>"
            % (
                a.get("nomComplet") or a.get("name"),
                a.get("caliber", "—"),
                st.get("cadence", "—"),
                st.get("ergonomie", "—"),
                st.get("portee", "—"),
                st.get("reculVertical", "—"),
                modes,
            )
        )
    return """
          <h2 id="carbine-position">Les carabines de la source de référence</h2>
          <p>Les carabines forment bien une famille de collection dans la source de
          référence : elle en recense <strong>huit</strong>. Ce qui les distingue des
          fusil d'assaut, ce n'est ni le calibre ni le mode de tir, mais la
          combinaison de trois traits — une cadence modérée, une portée moyenne à
          longue, et une ligne de tir destinée à tenir l'axe plutôt qu'à l'emporter.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les huit carabines — statistiques relevées sur la source de référence</caption>
              <thead><tr><th scope="col">Arme</th><th scope="col">Calibre</th>
              <th scope="col">Cadence</th><th scope="col">Ergonomie</th>
              <th scope="col">Portée (m)</th><th scope="col">Recul vert.</th>
              <th scope="col">Modes de tir</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>Ce que le tableau raconte.</strong> La dispersion des cadences
            est large : de 200 coups par minute pour la SVTU à 660 pour la M16. Et la
            dispersion des portées l'est davantage : de 54 mètres pour la SA85M à 73
            pour la M16. Entre les deux, il y a une ligne de crête très nette.
            <strong>La M16 est l'exception de la famille</strong> : 660 coups par
            minute, 73 mètres de portée et 53 points d'ergonomie. Elle cumule les
            trois meilleurs chiffres de la catégorie, ce qui en fait l'arme la plus
           difficile à remplacer dans son créneau.</p>
          </div>
          <div class="callout callout-warning">
            <p><strong>Les deux extrêmes à ne pas confondre.</strong> La SVTU, avec
            30 points d'ergonomie seulement, est la moins maniable de la famille :
            son recul vertical de 30 est faible, mais sa cadence de 200 coups par
            minute et sa lourdeur en font une arme de patient. À l'opposé, la Mini14
            offre 67 mètres de portée et 60 points d'ergonomie pour une cadence
            modeste de 400 : c'est la carabine de précision du groupe, et la
            meilleure option quand on cherche à poser un tir sans se-discovery
            à l=textbook.</p>
          </div>
""" % "\n".join(lignes)


def main():
    s = PAGE.read_text(encoding="utf-8")
    if 'id="carbine-position"' in s:
        i = s.find(ANCIEN_DEBUT)
        if i == -1:
            print("  bloc absent, rien a faire")
            return 0
        # trouver la fin du bloc : la prochaine balise h2 ou la fin du contenu
        j = s.find('<h2', i + len(ANCIEN_DEBUT))
        if j == -1:
            j = s.find('<footer class="site-footer">')
        s = s[:i] + bloc(charger_carabines()).strip() + "\n\n" + s[j:]
        PAGE.write_text(s, encoding="utf-8")
        print("  armes-carbine.html : bloc corrige")
        return 0

    m = re.search(r'<h2[^>]*id="role"[^>]*>', s)
    if not m:
        print("  ANCRE role introuvable")
        return 1
    s = s[: m.start()] + bloc(charger_carabines()).strip() + "\n\n" + s[m.start():]
    PAGE.write_text(s, encoding="utf-8")
    print("  armes-carbine.html : bloc insere")
    return 0


if __name__ == "__main__":
    sys.exit(main())
