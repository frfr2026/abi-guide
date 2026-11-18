#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichit pages/items-cles.html avec quatre elements issus de la veille
communautaire qui ne figuraient pas sur la page :

  1. le seuil de rentabilite PAR OUVERTURE, qui complete la formule globale
     deja presente ;
  2. le moment ou acheter : le marche des cles est un marche horaire ;
  3. la propriete "voir avant d'ouvrir", propre a certaines cartes a
     keycard, qui change la nature du pari ;
  4. la hiérarchie des coffres : les coffres minutés et les grands coffres
     rapportent plus que les petits.

Statut : retour communautaire dans tous les cas. Les fourchettes de prix
changent tous les jours et sont donc presentees comme des ordres de
grandeur, jamais comme des valeurs de reference.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/items-cles.html")

BLOC = """
          <h3 id="seuil-ouverture">Le seuil par ouverture : le calcul qui tranche</h3>
          <p>La formule de retour sur investissement présentée plus haut donne le
          résultat global d'une clé. Mais pour décider d'en acheter une, il faut un
          chiffre plus simple : <strong>combien vaut une ouverture, et combien
          coûte-t-elle</strong>.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Le seuil de rentabilité par ouverture</caption>
              <thead><tr><th scope="col">Étape</th><th scope="col">Calcul</th>
              <th scope="col">Exemple</th></tr></thead>
              <tbody>
                <tr><td><strong>1. Coût par ouverture</strong></td>
                <td>Prix d'achat ÷ nombre d'utilisations restantes</td>
                <td>Clé à 600 000 K sur 30 usages = <strong>20 000 K par ouverture</strong></td></tr>
                <tr><td><strong>2. Valeur espérée par ouverture</strong></td>
                <td>Valeur moyenne du contenu de la pièce</td>
                <td>Un coffre de la pièce rend en moyenne 45 000 K</td></tr>
                <tr><td><strong>3. Verdict</strong></td>
                <td>Valeur espérée − coût par ouverture</td>
                <td>45 000 − 20 000 = <strong>+25 000 K par ouverture</strong></td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>Pourquoi ce calcul change les décisions.</strong> Une clé à
            trois millions de Koen qui ouvre une pièce ne se juge pas sur son prix
            mais sur son coût par ouverture : à trente usages, c'est cent mille
            Koen la porte. Si le contenu moyen de la pièce vaut soixante mille,
            la clé est une perte sèche à chaque usage — même si vous en sortez
            parfois un objet à sept cent mille. Cette asymétrie est exactement ce
            qui trompe les joueurs qui comptent leurs gains au lieu de compter
            leurs portes.</p>
          </div>
          <div class="callout callout-warning">
            <p><strong>Le cas particulier des clés très chères.</strong> Pour les
            clés au-dessus de deux millions, la réponse de la communauté est
            cohérente : une clé à ce niveau de prix ne se rentabilise pas en
            Lockdown, elle se rentabilise en Forbidden, où le butin des pièces
            est d'un tout autre ordre de grandeur. Et les clés de la zone la plus
            disputée — le motel de Farm, notamment — se remplissent de
            synthétisés, mais le risque de mort y est le plus élevé. Le prix de la
            clé n'est qu'une partie de l'équation ; le taux de survie sur la pièce
            est l'autre.</p>
          </div>

          <h3 id="timing-marche">Le marché des clés a une horaire</h3>
          <p>Les prix des clés varient tous les jours, et cette variation n'est
          pas du bruit : elle est corrélée à l'affluence. Un consensus emerges des
          retours de joueurs : <strong>les clés se paient moins cher en semaine,
          en journée, et le week-end les prix montent</strong>. Le motif est
          mécanique — le nombre de raid augmente, donc la demande de clés monte
          plus vite que l'offre.</p>
          <ul>
            <li><strong>Acheter tôt dans la semaine, en journée</strong> : c'est le
            moment où l'écart entre le prix affiché et le prix de revient réel est
            le plus favorable.</li>
            <li><strong>Regarder les baisses ponctuelles</strong> : un contact
            peut brader une clé pour vider son stock. La règle de terrain qui
            revient le plus souvent est simple : n'achetez auprès d'un contact que
            lorsqu'il est en promotion.</li>
            <li><strong>Comparer avec le prix du marché</strong> avant d'acheter :
            le marché est la référence, le contact est l'opportunité.</li>
          </ul>
          <div class="callout callout-info">
            <p><strong>Statut de cette information :</strong> retour communautaire.
            La corrélation horaire est observée de façon récurrente par les joueurs
            qui achètent en volume, mais elle n'est publiée par aucun canal
            officiel. Traitez-la comme une heuristique de terrain fiable, pas comme
            une donnée.</p>
          </div>

          <h3 id="voir-avant-ouvrir">Voir avant d'ouvrir : le cas particulier des keycards</h3>
          <p>Certaines pièces s'ouvrent avec une <strong>carte d'accès</strong> plutôt
          qu'avec une clé, et c'est précisément ce qui les rend différentes. Dans
          certaines configurations — le centre de commandement de l'Armory est
          l'exemple le plus cité — la vitre de la pièce donne sur son contenu.
          Vous voyez donc la pièce <em>avant</em> de payer l'ouverture.</p>
          <div class="callout callout-success">
            <p><strong>Pourquoi c'est la meilleure clé du jeu.</strong> Une clé
            classique est un pari aveugle : vous payez avant de savoir. Une
            keycard dont la vitre montre le contenu transforme le pari en
            vérification. Si la pièce contient un objet de forte valeur, vous
            ouvrez et vous gagnez. Si elle ne contient que de la commonplace, vous
            passez votre chemin et vous gardez votre clé. La valeur par ouverture
            devient predictable, et c'est exactement ce qui sépare une clé
            rentable d'une clé qu'on achète par habitude.</p>
          </div>

          <h3 id="coffres">Tous les coffres ne se valent pas</h3>
          <p>À l'intérieur d'une même pièce, deux coffres peuvent ne rien avoir en
          commun. Deux observations reviennent régulièrement chez les joueurs qui
          achètent en volume.</p>
          <ul>
            <li><strong>Les coffres à minuterie</strong> — ceux qui affichent un
            compte à rebours — sont les plus rentables de l'Armory, en particulier
            celui de la station de réparation. Le minuterie est un signal de valeur
            par le jeu lui-même.</li>
            <li><strong>Les grands coffres, en hauteur, valent mieux que les
            petits.</strong> Le rapport semble s'inverser : les petits coffres de type
            bureau ordinaire sont généralement les moins généreux de la pièce. C'est
            une théorie de terrain, mais elle est cohérente d'un joueur à l'autre.</li>
            <li><strong>Les coffres électroniques</strong> sortent des objets
            électroniques de valeur supérieure à celle des coffres standards, et
            c'est ce qui rend certaines pièces Chill.</li>
          </ul>
          <div class="callout callout-warning">
            <p><strong>Deux nuances.</strong> D'abord, la hiérarchie des coffres
            est une observation, pas une règle : un petit coffre peut sortir un
            objet rare, et c'est précisément ce qui arrive de temps en temps. Ensuite,
            les prix indiqués dans les guides de marché sont des fourchettes de la
            période où ils ont été relevés — ils changent de jour en jour et
            servent d'ordre de grandeur, pas de valeur de référence.</p>
          </div>
"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    if 'id="seuil-ouverture"' in s:
        print("  deja present")
        return 0
    m = re.search(r'<h2[^>]*id="conseils"[^>]*>', s)
    if not m:
        print("  ANCRE conseils introuvable")
        return 1
    s = s[: m.start()] + BLOC.strip() + "\n\n" + s[m.start():]
    PAGE.write_text(s, encoding="utf-8")
    print("  items-cles.html : 4 blocs ROI inseres")
    return 0


if __name__ == "__main__":
    sys.exit(main())
