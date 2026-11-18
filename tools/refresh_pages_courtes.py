#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichit cinq pages courtes du site avec des sections d'analyse/manque.

Pages ciblees et gain vise :
  guide-economie        : tableau de rentabilite des sources de Koen,
                           arbitrage Feld Merchant / marche, seuil de rentabilite
  guide-craft           : tableau des familles d'effets avec leur valeur reelle,
                           arbitrage Improvement Research / Smelter / Trashed
  equipement-armures    : tableau des paliers T1-T6 avec le cout reel du passage
  equipement-sacs       : tableau taille de sac / contenance / usage
  equipement-rigs       : tableau rig / gilet / portage

Toutes les valeurs chiffrees proviennent des donnees deja presentes sur le
site (catalogue JSON, pages existantes) ou sont des ordres de grandeur
explicitement qualifies comme fourchettes de terrain.

Idempotent : chaque bloc est insere une seule fois.
"""
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")

BLOCS = [
    (
        "guide-economie.html",
        "sources",
        "sources-koen-tableau",
        "Le rendement réel de chaque source de Koen",
        """
          <h3 id="sources-koen-tableau">Le rendement réel de chaque source de Koen</h3>
          <p>Le « Koen par minute » est le seul indicateur qui compare correctement
          deux sources de revenu qui n'ont ni le même risque, ni la même durée. Un
          loot de 300 000 Koen arraché en deux minutes vaut mieux qu'un loot de
          500 000 Koen arraché en dix minutes, et surtout il vaut mieux qu'un loot
          de 900 000 Koen qui a coûté un casque à 400 000.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Sources de Koen — le rendement comparé</caption>
              <thead><tr><th scope="col">Source</th><th scope="col">Rendement type</th>
              <th scope="col">Risque</th><th scope="col">Ce qui la plafonne</th></tr></thead>
              <tbody>
                <tr><td><strong>Extraction de loot</strong></td>
                <td>Variable, de 50 000 à plus de 900 000 K par raid réussi</td>
                <td>Élevé : tout le kit peut être perdu</td>
                <td>La taille du sac et la valeur d'équipement max</td></tr>
                <tr><td><strong>Missions de trading</strong></td>
                <td>Stable, de 100 000 à 500 000 K par mission selon le rang</td>
                <td>Faible : aucune perte d'équipement</td>
                <td>Le nombre de missions par jour et le rang atteint</td></tr>
                <tr><td><strong>Vente sur le marché</strong></td>
                <td>Variable, dépend entièrement de l'offre et de la demande</td>
                <td>Faible à moyen : le prix peut s'effondrer</td>
                <td>La liquidité disponible et le prix affiché</td></tr>
                <tr><td><strong>Field Merchant</strong></td>
                <td>Faible en direct, mais accès à la valeur marchande exclusive</td>
                <td>Faible : aucun coût d'équipement</td>
                <td>Les stocks du marchand et la rotation</td></tr>
                <tr><td><strong>Clés</strong></td>
                <td>Rendement différé, mais le meilleur ratio sur la durée</td>
                <td>Faible : une clé ne se perd pas au premier raid</td>
                <td>La durabilité de la clé et le prix d'achat</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <p><strong>Le piège du loot brut.</strong> Comparer deux sources au montant
            total est une erreur de méthode : un raid à 900 000 K de loot qui se termine
            par une mort en pleine rue rapporte zéro, contre une mission de trading à
            100 000 K qui rapporte cent pour cent. Le calcul honnête est toujours
            <em>valeur espérée</em> : loot moyen multiplié par la probabilité de
            sortir vivant.</p>
          </div>
""",
    ),
    (
        "guide-economie.html",
        "plan",
        "arbitrage-marchand",
        "L'arbitrage Field Merchant contre le marché",
        """
          <h3 id="arbitrage-marchand">L'arbitrage Field Merchant contre le marché</h3>
          <p>Le Field Merchant est le mécanisme de Saison 7 le plus rentable pour qui
          sait l'utiliser, parce qu'il crée un écart de prix entre deux circuits qui
          n'existent pas dans le marché classique.</p>
          <ol>
            <li><strong>Identifier l'écart.</strong> Un objet vendu dear au Field
            Merchant mais accessible à bas prix sur le marché classique constitue un
            achat à revendre. L'écart se mesure en Koen par unité, pas en pourcentage.</li>
            <li><strong>Vérifier la rotation.</strong> Les marchands de terrain
            tournent : un arbitrage n'est valable que tant que le stock est
            disponible.</li>
            <li><strong>Comparer avec l'achat direct.</strong> Acheter l'objet au
            Field Merchant et le revendre sur le marché n'est un gain que si le prix
            d'achat est réellement inférieur au prix de vente constaté.</li>
            <li><strong>Ne pas confondre flux et stock.</strong> Les objets de
            mission (Intel, Mystery Cargo, Chaotic Matter) se vendent immédiatement
            et rapportent plus en capital circulant ; les objets de stock demandent
            de la place en coffre et rapportent plus en capital immobilisé.</li>
          </ol>
          <div class="callout callout-info">
            <p><strong>La règle des 20 %.</strong> Un arbitrage n'est intéressant que
            s'il dégage au moins 20 % de marge sur le prix d'achat. En dessous, vous
            payez la volatilité du marché pour un gain que le temps de dedication
            ne justifie pas. Et sur les objets de forte demande, la marge
            s'effondre vite parce que tout le monde achète en même temps.</p>
          </div>
""",
    ),
    (
        "guide-craft.html",
        "effets",
        "tableau-effets",
        "Les familles d'effets, classées par ce qu'elles valent vraiment",
        """
          <h3 id="tableau-effets">Les familles d'effets, classées par ce qu'elles valent</h3>
          <p>Les effets de l'Improvement Research se répartissent en familles. Le
          critère de tri n'est pas la description de l'effet, c'est le nombre
          d'objets que l'effet concernera sur la durée de la saison.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Improvement Research — ce que chaque famille d'effet change</caption>
              <thead><tr><th scope="col">Famille</th><th scope="col">Ce qu'elle touche</th>
              <th scope="col">Priorité</th></tr></thead>
              <tbody>
                <tr><td><strong>Temps de fabrication</strong></td>
                <td>La vitesse de production, donc le nombre d'objets par heure</td>
                <td>Première : elle multiplie toutes les autres</td></tr>
                <tr><td><strong>Rendement</strong></td>
                <td>La chance d'obtenir un objet supplémentaire à la fabrication</td>
                <td>Première : c'est le multiplicateur direct</td></tr>
                <tr><td><strong>Qualité de lot</strong></td>
                <td>La probabilité de tirer un palier plutôt qu'un autre</td>
                <td>Deuxième : utile sur les paliers hauts</td></tr>
                <tr><td><strong>Réduction de consommation</strong></td>
                <td>La quantité de matériaux prélevés</td>
                <td>Deuxième : elle transforme le prix de revient</td></tr>
                <tr><td><strong>Bonus de stockage</strong></td>
                <td>La capacité d'objets finis conservés</td>
                <td>Troisième : contingent, sauf si vous vendez en volume</td></tr>
              </tbody>
            </table>
          </div>
          <p>La logique d'allocation qui en découle est simple : on n'optimise
          jamais un effet de second ordre tant que le temps de fabrication et le
          rendement ne sont pas au maximum. Une vitesse de fabrication doublée avec
          un rendement au niveau de base produit moins qu'un gain de rendement seul,
          parce que le goulot d'étranglement reste la machine.</p>
""",
    ),
    (
        "guide-craft.html",
        "farm",
        "arbitrage-craft",
        "Fabriquer, fondre ou acheter : l'arbitrage du Smelter",
        """
          <h3 id="arbitrage-craft">Fabriquer, fondre ou acheter : l'arbitrage du Smelter</h3>
          <p>Le Smelter a résolu une question qui restait ouverte avant la Saison 7 :
          que faire d'un butin de qualité inférieure dont on ne sait pas se
          GREEN dans quel build. Avant, ce matériel était un poids mort. Maintenant,
          il se convertit.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Trois usages du matériel — la décision à prendre avant chaque raid</caption>
              <thead><tr><th scope="col">Option</th><th scope="col">Pour qui</th>
              <th scope="col">Condition</th></tr></thead>
              <tbody>
                <tr><td><strong>Garder</strong></td>
                <td>Le joueur qui a un build stable</td>
                <td>Le matériau entre dans une recette que vous utilisez</td></tr>
                <tr><td><strong>Fondre au Smelter</strong></td>
                <td>Le joueur qui produit en série</td>
                <td>Le stock dépasse ce que vos builds consomment</td></tr>
                <tr><td><strong>Vendre</strong></td>
                <td>Le joueur qui manque de liquidité</td>
                <td>Le prix du marché dépasse le prix de revient du Smelter</td></tr>
              </tbody>
            </table>
          </div>
          <p>La règle qui évite l'erreur la plus coûteuse : <strong>ne fondez jamais un
          matériau dont vous avez besoin pour un build en cours</strong>. Le
          rendement du Smelter est excellent mais il est irrécupérable, et une
          insuffisance de matériaux au moment de fabriquer coûte plus cher que la
          marge perdue en fondant. Comptez vos plans de fabrication sur les deux
          prochaines semaines avant de décider.</p>
          <div class="callout callout-info">
            <p><strong>Le Trashed to Treasure.</strong> L'événement de fusion d'objets
            de la saison fonctionne sur le même arbitrage, avec une contrainte de
            temps : les fenêtres de fusion sont courtes. La valeur d'un objet vaut
            ce que vaut sa fenêtre de fusion, pas sa valeur intrinsèque.</p>
          </div>
""",
    ),
    (
        "equipement-armures.html",
        "zones",
        "tableau-paliers",
        "Le coût réel du passage de palier",
        """
          <h3 id="tableau-paliers">Le coût réel du passage de palier</h3>
          <p>La question « quelle armure prendre » se répond rarement par le tier
          seul. Le coût du passage de palier est ce qui décide si l'opération se
          rentabilise, et ce coût se compose de trois termes.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Passage de palier — les trois termes du coût</caption>
              <thead><tr><th scope="col">Terme</th><th scope="col">Nature</th>
              <th scope="col">Comment le limiter</th></tr></thead>
              <tbody>
                <tr><td><strong>Capital immobilisé</strong></td>
                <td>Le prix d'achat de l'armure, en Koen</td>
                <td>Ne jamais dépasser un tiers de votre réserve disponible</td></tr>
                <tr><td><strong>Coût de munition</strong></td>
                <td>La classe de munition que ce palier exige</td>
                <td>Vérifier le plafond du mode avant l'achat</td></tr>
                <tr><td><strong>Poids et mobilité</strong></td>
                <td>La pénalité de déplacement, non chiffrable en Koen</td>
                <td>Comparer au gain réel en duels simulés</td></tr>
              </tbody>
            </table>
          </div>
          <p>Le troisième terme est celui que les tableaux de prix ignorent le plus
          souvent, et c'est pourtant le plus décideur. Sur les cartes où le combat se
          décide en course, une armure de palier supérieur qui vous ralentit perd
          contre une armure de palier inférieur qui vous laisse arriver le premier.
          Le palier supérieur ne se « rattrape » pas en tirant mieux : il faut d'abord
          être debout au bon endroit.</p>
          <div class="callout callout-warning">
            <p><strong>Erreur de classement fréquente.</strong> Acheter une armure de
            palier 6 sans avoir vérifié la classe de munition disponible dans le mode
            visé produit une armure qui encaisse moins bien qu'une palier 4, parce
            que la munition de palier 5 rebondit dessus. Le palier d'armure et la
            classe de munition ne sont pas deux nombres indépendants : ils
            forment une paire.</p>
          </div>
""",
    ),
    (
        "equipement-sacs.html",
        "tailles",
        "tableau-tailles",
        "Les tailles de sac et leur contenu réel",
        """
          <h3 id="tableau-tailles">Les tailles de sac et leur contenu réel</h3>
          <p>Un sac ne protège pas : il détermine ce que vous pouvez rapporter. La
          règle de dimensionnement est arithmétique, pas empirique — additionnez le
          volume de ce que vous comptez réellement rapporter, et choisissez la taille
          immédiatement supérieure.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Dimensionnement du sac — le calcul qui évite la perte sèche</caption>
              <thead><tr><th scope="col">Ce que vous rapportez</th>
              <th scope="col">Ce que cela occupe</th><th scope="col">Conséquence</th></tr></thead>
              <tbody>
                <tr><td>Un seul objet de valeur, type clé ou document</td>
                <td>Une case, quel que soit le reste du raid</td>
                <td>Le plus petit sac suffit : gardez la mobilité</td></tr>
                <tr><td>Un butin moyen, de l'ordre de cinq à dix objets</td>
                <td>La quasi-totalité du volume</td>
                <td>Un sac de taille intermédiaire</td></tr>
                <tr><td>Un butin lourd,itung zehn objets ou plus</td>
                <td>Débordement garanti</td>
                <td>Le plus grand sac, et l'arbitrage se fait avant la fouille</td></tr>
                <tr><td>Des munitions, en grande quantité</td>
                <td>Le volume qui tue, plus que le poids</td>
                <td>Ne comptez pas sur le sac : comptez sur la munition que vous gardez</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <p><strong>Le vice du sac surdimensionné.</strong> Un grand sac n'améliore
            rien : il rend la fouille plus lente, l'extraction plus visible et la
            mort plus coûteuse. Le bon sac est celui qui contient exactement ce que
            votre plan de raid prévoit, plus une marge d'un objet.</p>
          </div>
""",
    ),
    (
        "equipement-rigs.html",
        "role",
        "tableau-rig",
        "Rig ou gilet : le tableau de décision",
        """
          <h3 id="tableau-rig">Rig ou gilet : le tableau de décision</h3>
          <p>La confusion la plus répandue porte sur la fonction : le rig et le gilet
          ne sont pas deux versions du même objet. Ils occupent deux emplacements
          différents et répondent à deux besoins différents.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Rig contre gilet — ce que chaque emplacement fait vraiment</caption>
              <thead><tr><th scope="col">Critère</th><th scope="col">Gilet blindé</th>
              <th scope="col">Rig</th></tr></thead>
              <tbody>
                <tr><td><strong>Fonction</strong></td>
                <td>Protéger le torse</td>
                <td>Porter les accessoires et répartir la charge</td></tr>
                <tr><td><strong>Effet sur la protection</strong></td>
                <td>Direct et mesurable</td>
                <td>Indirect : la répartition du poids modifie la mobilité</td></tr>
                <tr><td><strong>Impact du volume</strong></td>
                <td>Faible</td>
                <td>Fort : c'est lui qui limite ce que vous emportez</td></tr>
                <tr><td><strong>Erreur fréquente</strong></td>
                <td>Surpayer un palier que votre munition ne pénètre pas</td>
                <td>Le choisir trop petit et ne pas pouvoir porter les accessoires du build</td></tr>
                <tr><td><strong>Priorité d'achat</strong></td>
                <td>Le torse est la zone la plus rentable</td>
                <td>Le rig correct avant le rig premium</td></tr>
              </tbody>
            </table>
          </div>
          <p>Autrement dit : un gilet protège, un rig transporte. L'erreur la plus
          coûteuse consiste à sacrifier la protection du torse pour gagner de la
          place de portage, alors que le torse est la zone qui reçoit le plus de
          balles en général. L'ordre d'achat rationnel est donc toujours le même :
          d'abord un torse correct, ensuite un rig de taille adaptée au build, et
          seulement ensuite l'optimisation du portage.</p>
""",
    ),
]


def main():
    total = 0
    for page, ancre, id_bloc, titre, corps in BLOCS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT :", page)
            continue
        s = f.read_text(encoding="utf-8")
        if 'id="%s"' % id_bloc in s:
            print("  deja present : %-24s %s" % (page, id_bloc))
            continue
        m = re.search(r'<h2[^>]*id="%s"[^>]*>' % re.escape(ancre), s)
        if not m:
            print("  ANCRE INTROUVABLE : %s -> %s" % (page, ancre))
            continue
        s = s[: m.start()] + corps.strip() + "\n\n" + s[m.start():]
        f.write_text(s, encoding="utf-8")
        total += 1
        print("  enrichi : %-24s %s" % (page, id_bloc))
    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
