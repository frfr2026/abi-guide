#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - reparation de pages/saison7-battle-pass.html.

Une purge de script a supprime deux morceaux de la page ; le contenu d'origine
est reconstructible depuis tools/build_s8c.py, qui est le generateur de cette
page. Ce script retablit :

  1. l'encadré "Les recompenses d'activite ne se rattrapent pas" ;
  2. le titre "2. Les skins exclusifs de la saison" et son introduction ;
  3. l'entete du tableau des skins (Skin | Arme | Obtention) ;
  4. le paragraphe "Le Streamlined ..." et l'encadré "La progression de tirage
     est conservee" ;
  5. le deplacement du bloc MISSIONS3X3 juste apres la section 3.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/saison7-battle-pass.html")

# --- fragments d'origine (tools/build_s8c.py) --------------------------------
SKINS_TETE = """          <div class="callout callout-warning">
            <h3 class="h4">Les récompenses d'activité ne se rattrapent pas</h3>
            <p>Les récompenses d'étoile (star rewards) sont <strong>réinitialisées chaque lundi à 05:00 UTC</strong>, et les récompenses non réclamées <strong>ne sont pas rééditées</strong>. La ligne de missions zombies de 40 missions suit la même logique : rattrapée chaque semaine.</p>
          </div>

          <h2 id="skins">2. Les skins exclusifs de la saison</h2>
          <p>Les skins d'armes exclusifs de la saison s'obtiennent via le <strong>Battle Pass Store</strong> et les <strong>vouchers</strong> gagnés en missions ou en événements. Liste annoncée officiellement :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Skin</th><th>Arme</th><th>Obtention</th></tr></thead>
"""

STREAMLINED = """          <p>Le <strong>« Streamlined »</strong> se décline sur cinq armes de la même famille visuelle — c'est le set le plus rentable en effort. Le <strong>Pixel Soldier / Pixelated Battlefield</strong> est le set « rétro pixel » de la saison, obtenu gratuitement via le check-in et le Défi de Merit.</p>
          <div class="callout callout-success">
            <h3 class="h4">La progression de tirage est conservée</h3>
            <p>La progression de tirage de la <strong>Saison 6 est intégralement reportée</strong> : si vous étiez à mi-parcours sur un banner de la saison précédente, vous reprenez exactement où vous vous étiez arrêté. Aucun tirage perdu au changement de saison.</p>
          </div>
"""

MARK_OUVERT = "<!--VEILLE-D:MISSIONS3X3:OPEN-->"
MARK_FERME = "<!--VEILLE-D:MISSIONS3X3:CLOSE-->"


def main():
    s = PAGE.read_text(encoding="utf-8")

    # ---- 1. bloc MISSIONS3X3 : le detacher et le memoriser ------------------
    i = s.find(MARK_OUVERT)
    j = s.find(MARK_FERME)
    bloc_missions = ""
    if i != -1 and j != -1:
        bloc_missions = s[i:j + len(MARK_FERME)]
        s = s[:i] + s[j + len(MARK_FERME):]
        print("  bloc MISSIONS3X3 detache")

    # ---- 2. purger les residus du bloc (texte orphelin) ---------------------
    s = re.sub(r"[ \t]*\n?[ \t]*de saison, pas un achat définitif\.</p>\n", "\n", s)
    s = re.sub(r"[ \t]*\n?[ \t]*<p class=\"small text-muted\">Source&nbsp;: base de données de missions ABI Builder.*?</p>\n", "", s, flags=re.S)
    s = re.sub(r"[ \t]*\n?[ \t]*</div>\n[ \t]*</div>\n[ \t]*\n", "\n", s)

    # ---- 3. retablir l'entete du tableau des skins --------------------------
    if "<h2 id=\"skins\">" not in s:
        anc = "              <tbody>\n                <tr><td><strong>Shooting Star Panorama</strong></td>"
        if anc not in s:
            print("  [!!] ancre tbody introuvable")
            return 1
        s = s.replace(anc, SKINS_TETE + anc, 1)
        print("  en-tete du tableau des skins retablie")

    # ---- 4. retablir le paragraphe Streamlined et l'encadre tirage ---------
    if "La progression de tirage est conservée" not in s:
        debut = s.find('          <p>Le <strong>« Streamlined »</strong>')
        if debut == -1:
            print("  [!!] paragraphe Streamlined introuvable")
            return 1
        m = re.search(r'<h2 id="recompenses">', s[debut:])
        if not m:
            print("  [!!] ancre section 3 introuvable")
            return 1
        fin = debut + m.start()
        s = s[:debut] + STREAMLINED + s[fin:]
        print("  paragraphe Streamlined et encadre tirage retablis")

    # ---- 5. inserer le bloc missions apres la section 3 ---------------------
    if bloc_missions and MARK_OUVERT not in s:
        m = re.search(r'<h2 id="achat">', s)
        if m:
            anc = m.group(0)
            s = s[:m.start()] + bloc_missions + "\n" + s[m.start():]
            print("  bloc MISSIONS3X3 replace apres la section 3")
        else:
            print("  [!!] ancre section 4 introuvable")
            return 1

    PAGE.write_text(s, encoding="utf-8")
    print("  page ecrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
