#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repare equipement-tier-list.html.

La page contenait cinq sections recopiees depuis equipement-armures.html
("Les regles qui dictent le armure", "Les munitions a connaitre", "Quel kit
pour quel budget", "Les erreurs qui coutent cher", "FAQ"), avec une
numerotation dupliquee (deux sections 3., deux sections 4., deux sections 5.,
deux sections 6.) et des ancres reutilisees. Le contenu parle d'armure
(classe de protection, penetration, plafond de mode) alors que la page est
une tier list d'equipement.

Ce script remplace ce bloc par cinq sections propres a la tier list
d'equipement, numerotees 5 a 9, avec des ancres propres.

Idempotent : si les ancres nouvelles sont deja presentes, le script ne fait rien.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/equipement-tier-list.html")

NOUVEAU = """
          <h2 id="classement-mode">5. Comment lire le classement selon le mode</h2>
          <p>Un tier list d'équipement se lit mal si on l'applique à tous les modes
          à la fois. Le classement ci-dessus vaut pour le mode <strong>Lockdown</strong>,
          qui est le mode de référence de la Saison 7. Dans les deux autres modes, les
          écarts se resserrent et plusieurs paliers fusionnent.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Ce que change le mode — la même pièce n'a pas la même valeur</caption>
              <thead><tr><th scope="col">Mode</th><th scope="col">Ce que le classement privilégie</th>
              <th scope="col">Ce qu'il faut déprioriser</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal</strong></td><td>Les pièces au meilleur rapport
                poids / protection : le critère est la mobilité, pas la tenue</td>
                <td>Le haut de gamme, trop lourd et trop cher pour l'enjeu réel</td></tr>
                <tr><td><strong>Lockdown</strong></td><td>La cohérence de la protection :
                torse, casque et sac au même niveau de qualité</td>
                <td>Le mélange de niveaux, qui crée une zone de faiblesse</td></tr>
                <tr><td><strong>Forbidden</strong></td><td>La couverture de zone : chaque
                centimètre de torse et de tête compte</td>
                <td>Les pièces qui ne couvrent que le torse</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <p><strong>Le piège de la tier list :</strong> un classement d'équipement
            est un classement <em>relatif à une rencontre</em>. La même pièce est de
            premier choix face à un joueur en T3, et de dernier choix face à un
            joueur en T6 sur la même carte. La seule tier list stable est celle qui
            est liée à un mode et à une carte.</p>
          </div>

          <h2 id="pieces-cles">6. Les pièces qui font la différence</h2>
          <p>Sur l'ensemble de l'équipement, quatre familles de pièces concentrent
          l'essentiel de l'écart de performance. Elles sont classées ici par influence
          décroissante sur le résultat d'un raid.</p>
          <ul>
            <li><strong>Le casque.</strong> En Saison 7, casque et masque sont deux
            zones de dégât séparées : chaque point perdu sur l'une n'affecte pas
            l'autre. C'est la pièce qui change le plus la nature d'un duel, parce
            qu'elle détermine si le second tir adverse fait encore des dégâts.</li>
            <li><strong>Le gilet.</strong> Il porte l'essentiel de la protection, mais
            son utilité réelle dépend de ce qu'il couvre. Un gilet qui ne protège que
            le torse laisse la tête et les jambes nus : la question à poser n'est
            jamais « quel tier ? » mais « quelles zones ? ».</li>
            <li><strong>Le sac et le rig.</strong> Ils ne protègent presque rien, mais
            ils décident de ce que vous pouvez rapporter. Un sac sous-dimensionné
            transforme une fouille réussie en perte sèche, et c'est la perte la plus
            fréquente du jeu.</li>
            <li><strong>Les pièces de réduction du bruit.</strong> Moins
            douillères, mais elles changent la nature d'un engagement : un joueur peu
            bruyant obtient le premier tir, et le premier tir decide de la majority
            des engagements.</li>
          </ul>
          <div class="callout callout-info">
            <p><strong>Méthode de vérification.</strong> Pour chaque pièce que vous
           consider, posez trois questions : quelles zones elle protège-t-elle,
            quel est son niveau exact, et que se passe-t-il si vous la perdez en
            raid. Une pièce dont vous ne pouvez pas répondre à la troisième question
            n'est pas une pièce que vous pouvez ajuster en raid.</p>
          </div>

          <h2 id="enveloppe-budget">7. Trois enveloppes, trois usages</h2>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Enveloppes d'équipement — ce que vous achetez selon votre profil</caption>
              <thead><tr><th scope="col">Profil</th><th scope="col">Budget</th>
              <th scope="col">Priorité d'achat</th><th scope="col">Usage</th></tr></thead>
              <tbody>
                <tr><td><strong>Économique</strong></td><td>80 000 – 180 000 K</td>
                <td>Gilet et casque de palier moyen, sac correct</td>
                <td>Le ratio rendement / sécurité maximal, pour l'apprentissage</td></tr>
                <tr><td><strong>Standard</strong></td><td>200 000 – 400 000 K</td>
                <td>Protection cohérente sur torse et tête, sac de taille réelle</td>
                <td>Le kit de la majorité des joueurs en Lockdown</td></tr>
                <tr><td><strong>Complet</strong></td><td>450 000 – 900 000 K</td>
                <td>Tout au même palier, plus les pièces de réduction du bruit</td>
                <td>Réservé aux raids à très fort enjeu</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="erreurs-classement">8. Les erreurs de lecture du classement</h2>
          <ul>
            <li><strong>Suivre le tier au lieu de lire la zone couverte.</strong> Deux
            pièces de même tier peuvent couvrir des zones totalement différentes.
            C'est la première cause de mort en duel rapproché.</li>
            <li><strong>Considérer que le niveau du sac est un niveau de protection.
            </strong> Le sac ne protège pas : il conditionne le butin. Un sac de niveau
            élevé n'arrête pas une balle, il évite de perdre ce que vous avez trouvé.</li>
            <li><strong>Ignorer le mode.</strong> Le classement n'a de sens qu'à
            l'intérieur d'un mode, parce que les plafonds de niveau et de valeur
            changent d'un mode à l'autre.</li>
            <li><strong>Acheter une pièce isolée très haut de gamme.</strong> Une seule
            pièce de niveau élevé au milieu d'un ensemble moyen crée exactement le
            point faible qu'elle devait couvrir.</li>
            <li><strong>Dépasser le plafond de valeur d'équipement.</strong> Le raid
            refuse de démarrer tant qu'un objet n'est pas retiré de l'inventaire.</li>
          </ul>

          <h2 id="faq-tier">9. Questions fréquentes</h2>
          <h3>Quelle est la meilleure pièce d'équipement de la Saison 7 ?</h3>
          <p>Il n'y en a pas une, il y en a une <em>par mode et par rencontre</em>. En
          Lockdown, la priorité est la cohérence entre torse et casque. En Normal, la
          priorité est la mobilité. Ce qui reste vrai partout : une pièce de niveau
          moyen bien choisie bat presque toujours une pièce de haut niveau mal
          accordée au reste de l'ensemble.</p>
          <h3>Dois-je viser le plus haut niveau possible ?</h3>
          <p>Non. Le haut de gamme a un coût double : son prix et son poids. Un
          équipement lourd ralentit vos déplacements, ce qui compte plus qu'on ne le
          croit sur les cartes où les déplacements se jouent en course. Les niveaux
          intermédiaires sont les plus efficients.</p>
          <h3>Comment savoir si mon équipement est cohérent ?</h3>
          <p>Additionnez la valeur de chaque pièce et vérifiez que vous êtes sous le
          plafond du mode, puis comparez les niveaux zone par zone. La cohérence se
          vérifie sur le torse et la tête : ce sont les deux zones qui décident d'un
          duel.</p>
          <h3>Et si je suis vaulté contre un joueur mieux équipé ?</h3>
          <p>C'est là que la mobilité compte plus que la protection : se déplacer,
          casser l'angle, tirer depuis une position inattendue. L'écart de niveau se
          compense par le terrain, pas par l'usure de la plaque adverse.</p>
"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    if 'id="classement-mode"' in s:
        print("  deja repare")
        return 0
    # bloc fautif : de id="regles" jusqu'au premier <h2 id="faq"
    i = s.find('id="regles"')
    j = s.find('<h2 id="faq"')
    if i == -1 or j == -1 or j < i:
        print("  BORNES INTROUVABLES")
        return 1
    # conserver le <h2 id="faq" ... et remplacer tout ce qui precede
    s = s[:i] + NOUVEAU.strip() + "\n\n          " + s[j:]
    PAGE.write_text(s, encoding="utf-8")
    print("  equipement-tier-list.html : 5 sections remplacees")
    return 0


if __name__ == "__main__":
    sys.exit(main())
