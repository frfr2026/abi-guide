#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige le bloc "conteneur-assurance" insere dans pages/guide-extraction.html.

Le bloc precedent decrivait une mecanique d'assurance comme si elle existait.
C'est faux : la section deja presente sur la meme page — sourcee sur le wiki
officiel — dit explicitement "il n'y a pas d'assurance dans ABI Infinite" et
cite le wiki : "insurance does not exist, what you lose is gone unless
recovered manually".

Le bloc est remplace par une note de verification qui :
  1. conserve la position officielle (pas d'assurance) ;
  2. signale explicitement le conflit avec plusieurs guides communautaires qui
     decrivent encore un remboursement conditionnel ;
  3. ajoute le seul element reellement nouveau : le verrou "Tactical Ops
     locked" sur le placement en conteneur.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/guide-extraction.html")

NOUVEAU = """          <h2 id="conteneur-assurance">Note de vérification : l'« assurance » n'existe pas, mais beaucoup de guides la décrivent encore</h2>
          <p>Plusieurs guides communautaires récents — guides de survie de Saison 7,
          guides d économie, tutos vidéo d'équipement — décrivent une « assurance » qui
          rembourserait l'équipement perdu à la mort, à condition qu'aucun autre
          joueur ne soit sorti avec un objet assuré. C'est un point de friction
          réel dans l'information disponible sur ce jeu, et il mérite d'être traité
          franchement plutôt que d'être silencieusement ignoré.</p>
          <div class="callout callout-warning">
            <p><strong>La position officielle ne laisse pas de place à
            l'ambiguïté.</strong> Le wiki officiel indique : <em>« insurance does not
            exist, what you lose is gone unless recovered manually »</em>. Il n'existe
            pas de police d'assurance, pas de prime à payer pour couvrir son kit, et
            donc aucun remboursement conditionnel. Tout ce que vous portez hors
            d'un emplacement protégé est perdu.</p>
          </div>
          <p><strong>Alors d'où vient cette description ?</strong> Deux
          hypothèses, et il faut les distinguer. La première : elle décrit le jeu
          d'origine, <em>Arena Breakout</em>, où le mécanisme existait réellement et
          où il a été supprimé ou redéfini dans la version Infinite. La seconde :
          elle décrit un mécanisme qui a existé dans une version antérieure de
          Infinite et qui a été retiré. Aucune des deux ne justifie de la traiter
          comme une mécanique actuelle. Les deux hypothèses convergent vers la
          même conclusion pratique : ne comptez pas sur un remboursement, et ne
          payez pas pour une couverture qui n'existe pas.</p>
          <div class="callout callout-info">
            <p><strong>Ce qui existe réellement, et qui joue le même rôle :</strong>
            le conteneur sécurisé, le coéquipier qui sort vivant et renvoie votre
            équipement par messagerie, le programme de compensation
            <strong>G.T.I. Security</strong> — qui ne concerne que les victimes de
            tricheurs bannis définitivement — et l'emplacement clé pour vos cartes
            d'accès. Ces quatre mécanismes sont décrits dans la section précédente
            et sont, eux, documentés.</p>
          </div>
          <p>Un dernier point de vocabulaire, qui explique une partie de la
          confusion : le terme « assurance » est employé en français dans deux
          sens différents. Il peut désigner le remboursement après une mort — ce
          qui n'existe pas. Il peut aussi désigner simplement l'<em>assurance-vie</em> d'un objet : une arme de secours, une clé qui ne se perd pas, un
          conteneur protégé. C'est ce second sens qui est valide, et c'est celui
          qu'il faut employer pour éviter de se comprendre de travers.</p>
          <div class="callout callout-success">
            <p><strong>Le verrou « Tactical Ops locked »</strong> est le seul
            élément réellement nouveau que les guides communautaires apporte à ce
            sujet. Un objet marqué « Tactical Ops locked » ne peut pas être placé
            dans un conteneur protégé avant votre <strong>première extraction
            réussie avec lui</strong> : le symbole de boîte n'apparaît sur l'objet
            qu'une fois cette condition remplie. En pratique, cela signifie qu'un
            objet tout juste acquis ne peut pas encore être mis à l'abri. Ce n'est
            pas anodin pour les objets les plus chers, et cela explique certains
            morts sur lesquels le joueur croyait avoir tout placé en sécurité.</p>
          </div>
"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    i = s.find('<h2 id="conteneur-assurance">')
    if i == -1:
        print("  bloc absent, rien a faire")
        return 0
    # trouver la fin du bloc : prochain <h2 ou fin du conteneur de contenu
    j = s.find('<h2', i + 10)
    if j == -1:
        j = s.find('<footer class="site-footer">')
    s = s[:i] + NOUVEAU.strip() + "\n\n" + s[j:]
    PAGE.write_text(s, encoding="utf-8")
    print("  guide-extraction.html : bloc d assurance corrige")
    return 0


if __name__ == "__main__":
    sys.exit(main())
