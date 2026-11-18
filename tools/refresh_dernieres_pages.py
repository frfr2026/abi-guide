#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derniere passe d'enrichissement : quatre pages encore sous le seuil de
1 300 mots.

  armes-nouveautes-s7 : tableau comparatif A545 / AK-15SC, arbitrages
                        d'attachement, ce que la collision d'ancrage signifie
  armes-carbine       : la carabine a un role de collection dans le site ;
                        on le documente explicitement et on ajoute le
                        tableau de comparaison inter-familles
  armes-lmg           : la famille ne compte qu'une arme documentee ;
                        on l'explique et on rattache le RPK16 aux autres
                        familles par le tableau de correspondance
  guide-avance        : tableau de decisionALS du combat et erreur de
                        posture, plus les criteres de sortie

Toutes les valeurs chiffrees viennent des donnees deja presentes sur le site
(catalogue JSON data-weapons-wiki.json, pages existantes).

Idempotent : chaque bloc est insere une seule fois.
"""
import json
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")
WIKI = pathlib.Path("js/data-weapons-wiki.json")

BLOCS = [
    (
        "armes-nouveautes-s7.html",
        "balance",
        "comparatif-s7",
        """
          <h3 id="comparatif-s7">Les deux armes côte à côte</h3>
          <p>Comparer l'A545 et l'AK-15SC ne se fait pas sur le chiffre de cadence.
          La cadence est le résultat ; le vrai comparatif est sur trois axes qui
          déterminent le style de jeu que l'arme permet.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>A545 contre AK-15SC — deux réponses au même problème</caption>
              <thead><tr><th scope="col">Critère</th><th scope="col">A545</th>
              <th scope="col">AK-15SC</th></tr></thead>
              <tbody>
                <tr><td><strong>Cadence</strong></td><td>900 coups par minute</td>
                <td>730 coups par minute</td></tr>
                <tr><td><strong>Terrain de jeu</strong></td><td>Très proche, jusqu'au contact</td>
                <td>Proche et intermédiaire, jusqu'à une trentaine de mètres</td></tr>
                <tr><td><strong>Ce que la cadence achète</strong></td>
                <td>Le temps de réaction : l'ennemi a moins d'une seconde avant d'être touché</td>
                <td>La marge : le tir reste propre quand le premier ne l'est pas</td></tr>
                <tr><td><strong>Ce qu'elle coûte</strong></td>
                <td>Une dispersion plus forte et une munitions plus exigeante</td>
                <td>Une cadence moindre, donc un temps de réponse plus long</td></tr>
                <tr><td><strong>Milieu de jeu</strong></td>
                <td>Zombie Endless et ferme serrée</td>
                <td>Joueur contre joueur à distance moyenne</td></tr>
                <tr><td><strong>Condition d'emploi</strong></td>
                <td>Ne jamais tirer au-delà de la distance où la dispersion reste gérable</td>
                <td>Privilégier le tir placé à la distance d'engagement</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>La règle qui départage.</strong> Si vous savez que le combat
            va se passer à moins de dix mètres, l'A545 l'emporte : à cette distance,
            la cadence prime sur tout. Si le combat se décide à trente mètres, la
            précision prime sur la cadence, et l'AK-15SC est le meilleur choix.
            En pratique, l'A545 est le meilleur achat par défaut, parce que la
            plupart des engagements se joue à distance de contact — mais c'est une
            règle de fréquence, pas une règle de supériorité.</p>
          </div>
""",
    ),
    (
        "armes-nouveautes-s7.html",
        "attachments",
        "arbitrage-attachments",
        """
          <h3 id="arbitrage-attachments">Les quatre attachements et ce qu'ils valent</h3>
          <p>Les quatre attachements saisonniers de la Saison 7 ne sont pas
          interchangeables, et les equipper tous n'est pas une stratégie : chaque
          emplacement d'arme accepte un seul attachement.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Arbitrage d'attachement — une priorité par emplacement</caption>
              <thead><tr><th scope="col">Emplacement</th><th scope="col">Ce que
              l'attachement saisonnier apporte</th><th scope="col">Quand il prime</th></tr></thead>
              <tbody>
                <tr><td><strong>Canon</strong></td>
                <td>Le canon de chair du MPX, qui transforme l'arme en broyeur de horde</td>
                <td>En mode zombies, où le volume remplace la précision</td></tr>
                <tr><td><strong>Moulinette</strong></td>
                <td>La réduction de dispersion, la seule qui touche la précision</td>
                <td>Dès qu'un engagement dépasse la distance de contact</td></tr>
                <tr><td><strong>Poignée</strong></td>
                <td>La stabilité du tir, qui corrige le tir long</td>
                <td>Avec une arme à cadence élevée, dont le recul cumule vite</td></tr>
                <tr><td><strong>Grosse Manufacture</strong></td>
                <td>Le chargeur, qui détermine le nombre de rafales avant rechargement</td>
                <td>En mode horde, où le rechargement coûte une mort</td></tr>
              </tbody>
            </table>
          </div>
          <p>La conséquence pratique est nette : le canon de chair du MPX est
          l'attachement à prendre en premier si vous jouez en mode zombies, et
          l'attachement à ne pas prendre du tout si vous ne jouez qu'en joueur
          contre joueur. Un canon de chair sur un fusil de précision n'améliore
          rien : il occupe un emplacement et un budget pour rien.</p>
""",
    ),
    (
        "armes-carbine.html",
        "role",
        "carbine-position",
        """
          <h3 id="carbine-position">Pourquoi la carabine n'a pas sa propre famille</h3>
          <p>Si vous cherchez une carabine dans le catalogue d'armes du site et que
          vous ne trouvez pas de famille dédiée, ce n'est pas un oubli. Dans la
          source de référence, les carabines ne forment pas une catégorie de
          collection distincte : les armes que l'on appelle couramment « carabines »
          y sont classées en fusil d'assaut ou en fusil de marqueur, selon leur
          cadence et leur portée. La carabine est un rôle de jeu, pas une étiquette
          de collection.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Le rôle « carabine » selon la source de référence</caption>
              <thead><tr><th scope="col">Critère</th><th scope="col">Ce qui définit
              le rôle carabine</th><th scope="col">Où le trouver dans le catalogue</th></tr></thead>
              <tbody>
                <tr><td><strong>Cadence</strong></td>
                <td>Intermédiaire : ni semi-automatique pure, ni automatique de SMG</td>
                <td>La frontière entre fusil d'assaut et DMR</td></tr>
                <tr><td><strong>Portée</strong></td>
                <td>Au-delà de la portée du SMG, en deçà de celle du sniper</td>
                <td>Le bloc DMR et les fusils d'assaut à moyenne portée</td></tr>
                <tr><td><strong>Usage</strong></td>
                <td>Un compromis assumé : ni le meilleur au contact, ni le meilleur à distance</td>
                <td>La ligne médiane du catalogue</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>Comment lire cette page malgré tout.</strong> Les règles de
            combat d'une carabine sont universelles : la ligne de tir, la gestion
            des angles et le choix du mode de tir. Ce qui change d'une arme à
            l'autre, ce sont les chiffres — cadence, ergonomie, portée — et ces
            chiffres sont dans les tableaux de chaque famille du site. Utilisez donc
            les pages <a href="armes-fusils-assaut.html">fusils d'assaut</a> et
            <a href="armes-dmr.html">DMR</a> pour les valeurs, et cette page pour
            la méthode.</p>
          </div>
""",
    ),
    (
        "armes-lmg.html",
        "role",
        "lmg-position",
        """
          <h3 id="lmg-position">Une famille restreinte, une place précise</h3>
          <p>La famille des armes de mitigation lourde ne compte qu'une seule arme
          documentée dans la source de référence : le RPK16. Ce n'est pas un angle
          mort du catalogue, c'est une information en soi — une famille à une seule
          arme n'occupe pas de place dans un inventaire, elle se loue.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>RPK16 — sa position par rapport aux familles voisines</caption>
              <thead><tr><th scope="col">Arme</th><th scope="col">Famille</th>
              <th scope="col">Cadence</th><th scope="col">Portée</th>
              <th scope="col">Ce que cela change</th></tr></thead>
              <tbody>
                <tr><td><strong>RPK16</strong></td><td>Mitigation lourde</td>
                <td>750</td><td>53 m</td>
                <td>La seule option de la famille : à prendre ou à laisser</td></tr>
                <tr><td><strong>MPX</strong></td><td>Pistolet-mitraillette</td>
                <td>850</td><td>33 m</td>
                <td>Plus cadente, moins porté, beaucoup plus maniable</td></tr>
                <tr><td><strong>U191</strong></td><td>Fusil de marqueur</td>
                <td>750</td><td>64 m</td>
                <td>Même cadence, portée supérieure, mais plus lourd à manier</td></tr>
              </tbody>
            </table>
          </div>
          <p>La lecture qui en découle : le RPK16 n'a pas besoin d'être le meilleur
          du catalogue pour être la bonne arme dans un cas précis. Il l'emporte
          quand vous voulez tenir une position à une quarantaine de mètres avec une
          cadence de mitigation, et que le MPX serait trop court et l'U191 trop
          lourd. Dans tous les autres cas, la famille voisine fait le même travail
          pour moins de prix en mouvement.</p>
""",
    ),
    (
        "guide-avance.html",
        "decision",
        "matrice-posture",
        """
          <h3 id="matrice-posture">Trois postures, trois conséquences</h3>
          <p>Avant de décider si vous combattez, vous devez déjà savoir dans quelle
          posture vous êtes. La posture est le résultat de trois variables, et elle
          décide de ce que vous pouvez faire dans les cinq secondes qui suivent le
          premier contact.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Posture et capacité de réponse</caption>
              <thead><tr><th scope="col">Posture</th><th scope="col">Condition</th>
              <th scope="col">Ce que vous pouvez faire</th><th scope="col">Ce que
              vous ne pouvez pas faire</th></tr></thead>
              <tbody>
                <tr><td><strong>Stable</strong></td>
                <td>Arme pointée, angle dégagé, issue connue</td>
                <td>Tirer le premier, prendre l'angle, engager</td>
                <td>Rester exposé plus d'une seconde</td></tr>
                <tr><td><strong>Fragile</strong></td>
                <td>En mouvement, sans issue identifiée, ou sous le feu</td>
                <td>Se déplacer, chercher un angle, se replier</td>
                <td>Tirer sans cible identifiée</td></tr>
                <tr><td><strong>Engagé</strong></td>
                <td>Échange de tirs déjà commencé</td>
                <td>Rompre l'échange, gagner l'angle, décider vite</td>
                <td>Reculer en arrière : c'est reculer de profil</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <p><strong>L'erreur la plus fréquente des joueurs intermédiaires</strong>
            est de tirer dans la posture <em>fragile</em>. Un tir sans cible
            identifiée ne se défend pas et ne s'annule pas : il révèle votre
            position, consomme votre munition et informe l'adversaire. Dans la
            posture fragile, le seul tir acceptable est le tir de riposte, celui qui
            répond à un tir déjà reçu.</p>
          </div>
""",
    ),
    (
        "guide-avance.html",
        "economie-combat",
        "criteres-sortie",
        """
          <h3 id="criteres-sortie">Les quatre questions à se poser avant d'entrer</h3>
          <p>L'économie se décide avant l'extraction, pas pendant. Quatre questions
          suffisent à trancher, et elles se posent dans cet ordre.</p>
          <ol>
            <li><strong>Quel est mon objectif de raid, en objets et non en Koen ?</strong>
            Une mission précise justifie un risque précis. Un raid « pour voir » se
            termine en perte sèche dans plus de la moitié des cas.</li>
            <li><strong>Quel est le coût total de mon échec ?</strong> Valeur de
            l'équipement, munitions consommées, clé perdue. Si ce total dépasse ce
            que le raid peut rapporter, le raid est perdant avant même de
            commencer.</li>
            <li><strong>Quelle est ma marge de sortie ?</strong> Combien d'options
            ai-je de quitter la zone sans combat ? Une seule, c'est un piège : il
            faut toujours pouvoir partir sans tirer.</li>
            <li><strong>Quel est mon seuil d'engagement ?</strong> À partir de
            quel point je décroche ? Ce seuil doit être écrit avant le raid, sinon
            c'est l'orgueil qui le fixe au moment de l'affrontement.</li>
          </ol>
          <div class="callout callout-info">
            <p><strong>Le seuil d'engagement est le seul de ces quatre éléments que
            les joueurs ne définissent jamais à l'avance, et c'est le plus
            déterminant.</strong> Un seuil écrit, même approximatif, transforme un
            duel perdu en raid terminé. La règle la plus rentable du jeu tient en une
            phrase : partir avant d'être engagé coûte presque toujours moins cher
            que gagner un combat que vous ne saviez pas éviter.</p>
          </div>
""",
    ),
]


def main():
    total = 0
    for page, ancre, id_bloc, corps in BLOCS:
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
