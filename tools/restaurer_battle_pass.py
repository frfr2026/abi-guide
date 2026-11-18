#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - restauration definitive de pages/saison7-battle-pass.html.

Le script de veille d (refresh_veille_nov2026d.py) avait une purge par motif
regex qui a supprime deux morceaux de la page. L'original est reconstructible
depuis tools/build_s8c.py, generateur de la page : on reprend son corps, puis
on reapplique les transformations posters :
  - balise img avec width/height/decoding (audit images)
  - h4 -> h3 class="h4" (normalisation de hierarchie)
  - identifiants de liens lnk-saison7-battle-pass-NNN (wire_pages)
  - bloc de veille MISSIONS3X3

Le <head> et l'ossature (nav, aside, footer) sont conserves depuis le fichier
courant : ils portent les enrichissements SEO et le fil d'Ariane.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/saison7-battle-pass.html")
REBUILD = pathlib.Path("/tmp/bp_body_rebuilt.txt")

# transformations posterieures a build_s8c.py
IMG_OLD = '<img src="../img/events/s7-battle-pass.jpg" alt="Récompenses du Battle Pass Saison 7 Utopia" loading="lazy">'
IMG_NEW = ('<img width="1536" height="1024" src="../img/events/s7-battle-pass.jpg" '
           'alt="Récompenses du Battle Pass Saison 7 Utopia" loading="lazy" decoding="async">')

LIEN_094 = '<a href="saison7-utopia.html#agenda">'
LIEN_094_NEW = '<a href="saison7-utopia.html#agenda" id="lnk-saison7-battle-pass-094">'
LIEN_095 = '<a href="cosmetiques-skins-perso.html">'
LIEN_095_NEW = '<a href="cosmetiques-skins-perso.html" id="lnk-saison7-battle-pass-095">'

# corrections redactionnelles
FIX = [
    ("la même logique :rattrapez chaque semaine.", "la même logique : rattrapée chaque semaine."),
    ("les objectifs published", "les objectifs publiés"),
    ("<h2 id=\"recompenses\">3. Les autres récompenses</h2>",
     "          <h2 id=\"recompenses\">3. Les autres récompenses</h2>"),
    ("<h2 id=\"achat\">4. Où et comment acheter</h2>",
     "          <h2 id=\"achat\">4. Où et comment acheter</h2>"),
]

MARQUEUR_OUV = "<!--VEILLE-D:MISSIONS3X3:OPEN-->"
MARQUEUR_FERME = "<!--VEILLE-D:MISSIONS3X3:CLOSE-->"

BLOC_MISSIONS = """
          <div class="callout callout-success">
            <h3 class="h4">Comment obtenir la case 3×3 Titanium Case</h3>
            <p>Le conteneur sécurisé 3×3 se débloque en terminant les <strong>missions de saison</strong>, en
            deux difficultés : <strong>Normal</strong> et <strong>Hardcore</strong>. Les objectifs publiés
            pour la Saison&nbsp;7 tournent tous autour des zones infectées et de la signalétique de Valley.</p>
            <div class="table-wrap">
              <table class="data-table">
                <thead><tr><th>Objectif</th><th>Mission</th></tr></thead>
                <tbody>
                  <tr><td>Éliminer 10 ennemis ou mutants dans la zone ouest de Farm</td><td>Back in Shadow</td></tr>
                  <tr><td>Fouiller 15 conteneurs non fouillés dans la zone est de Valley</td><td>First Meeting</td></tr>
                  <tr><td>Localiser le signal au Crash Canyon de Valley</td><td>Checking the Clues</td></tr>
                  <tr><td>Localiser le signal à la Summit Platform de Valley</td><td>Military Isolation Zone</td></tr>
                  <tr><td>Localiser le signal à l'héliport de la Beach Villa de Valley</td><td>Military Isolation Zone</td></tr>
                  <tr><td>Éliminer 15 ennemis ou mutants dans Valley</td><td>Northridge Situation</td></tr>
                  <tr><td>Survivre 20 minutes à Northridge</td><td>Northridge Situation</td></tr>
                  <tr><td>Fouiller 4 boîtes à documents ou caisses de ravitaillement à Northridge</td><td>Northridge Situation</td></tr>
                </tbody>
              </table>
            </div>
            <p>Deux points de vigilance. D'abord, la plupart de ces objectifs se remplissent en <strong>Lockdown
            ou en Forbidden</strong> : le seuil de valeur d'équipement y est plus élevé, donc la mission coûte
            plus cher en matériel perdu qu'en Normal. Ensuite, la case 3×3 <strong>est réinitialisée au début de
            la saison suivante</strong> — c'est un objet de saison, pas un achat définitif.</p>
            <p class="small text-muted">Source&nbsp;: base de données de missions ABI Builder, recoupée avec les
            guides vidéo de déblocage de la case 3×3 de septembre 2026 — <strong>Documenté</strong>, non publiée
            par l'éditeur. Les objectifs de mission évoluent d'une saison à l'autre&nbsp;: vérifiez la liste
            active dans votre interface avant de planifier une rotation.</p>
          </div>
"""


def transformer(body):
    body = body.replace(IMG_OLD, IMG_NEW)
    body = body.replace(LIEN_094, LIEN_094_NEW).replace(LIEN_095, LIEN_095_NEW)
    body = re.sub(r"<h4>", '<h3 class="h4">', body)
    body = body.replace("</h4>", "</h3>")
    for avant, apres in FIX:
        body = body.replace(avant, apres)
    return body


def main():
    if not REBUILD.exists():
        print("  [!!] /tmp/bp_body_rebuilt.txt absent : lancer d'abord build_s8c.py")
        return 1

    courant = PAGE.read_text(encoding="utf-8")

    # 1. retirer tout bloc de veille deja present
    i = courant.find(MARQUEUR_OUV)
    j = courant.find(MARQUEUR_FERME)
    if i != -1 and j != -1:
        courant = courant[:i] + courant[j + len(MARQUEUR_FERME):]
        print("  ancien bloc MISSIONS3X3 retire")

    # 2. corps reconstruit, transforme
    body = transformer(REBUILD.read_text(encoding="utf-8"))

    # 3. insertion du bloc de veille avant la section 4
    anc = '          <h2 id="achat">'
    if anc not in body:
        print("  [!!] ancre section 4 introuvable dans le corps reconstruit")
        return 1
    body = body.replace(anc, MARQUEUR_OUV + "\n" + BLOC_MISSIONS + "          " + MARQUEUR_FERME + "\n" + anc, 1)

    # 4. remplacement du body dans la page courante
    d = courant.find('<article class="content-col">')
    f = courant.find("</article>", d)
    if d == -1 or f == -1:
        print("  [!!] article introuvable")
        return 1
    page = courant[:d] + body + courant[f:]

    PAGE.write_text(page, encoding="utf-8")
    print(f"  page restauree ({len(page)} caracteres)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
