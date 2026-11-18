#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veille du 18 novembre 2026 (3e serie) : quatre pages comblees sur des
lacunes confirmees par sondage du corpus existant.

  1. pages/items-cles.html
     - la fin de vie d'une cle : elle disparait a zero de durabilite ;
     - le seuil d'achat : 50 % de durabilite, et pourquoi la remise sous
       30 % ne se rentabilise pas ;
     - la rotation de cles : un set par niveau de risque, pour ne pas
       surcharger le conteneur securise.

  2. pages/guide-extraction.html
     - les boites de recuperation : ce qu'elles rendent reellement, et la
       regle de securite qui les accompagne.

  3. pages/equipement-sacs.html
     - le "backpack inception" : un sac dans un sac ;
     - les sacs a slots positifs, qui rendent plus de cases qu'ils n'en
       occupent.

  4. pages/equipement-rigs.html
     - le meme phenomene applique aux rigs : un rig qui garde plus de
       slots qu'il n'en consomme.

  5. pages/guide-traders.html
     - Deke, le contact des offres a duree limitee : le flux de revenu
       risque nul que presque personne n'exploite.

Statuts :
  - Communautaire pour les retours de joueurs et les mesures en jeu ;
  - Documentee pour les regles de jeu verifiees par recoupement.

Idempotent : chaque bloc porte un marqueur, un second passage ne change rien.
"""
import pathlib
import re
import sys

CIBLE = pathlib.Path("pages")


BLOC_CLES = """          <h3 id="fin-de-vie">Quand une clé s'éteint</h3>
          <p>Une clé ne se use pas, elle se <strong>consomme</strong>. Sa
          durabilité descend à chaque ouverture, et elle disparaît de votre
          inventaire le jour où elle atteint zéro. Ce n'est pas une nuance
          cosmétique : c'est ce qui transforme une clé en actif qui se dévalue
          tout seul si vous ne l'utilisez pas. Une clé achetée et inutilisée
          reste entière ; une clé utilisée dans le mauvais mode perd deux ou
          trois fois plus vite que prévu.</p>
          <div class="callout callout-warning">
            <p><strong>Le seuil d'achat : 50 % de durabilité, pas 30 %.</strong>
            Une clé vendue avec 30 % de durabilité affiche une remise, mais il
            ne vous reste que dix ouvertures en Normal, cinq en Lockdown et
            trois en Forbidden. La remise est immédiatement mangée par le
            nombre d'utilisations perdues. Les joueurs qui achètent en volume
            achètent à <strong>50 % ou plus</strong> de durabilité : c'est le
            point où le prix au marché reste rentable une fois le nombre
            d'ouvertures réel intégré. À l'inverse, une clé neuve à 100 % se
            négocie presque toujours plus cher, et l'écart de prix ne se
            rattrape pas si vous l'utilisez en Lockdown.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
          <div class="callout callout-info">
            <p><strong>La rotation : un jeu de clés par niveau de risque.</strong>
            L'erreur la plus coûteuse n'est pas d'acheter une mauvaise clé, c'est
            d'en acheter trop. Un conteneur sécurisé ne contient que six à neuf
            cases, et chaque clé en occupe une. Emporter en raid le jeu
            complet de clés d'Armory et de Northridge sur une carte où vous ne
           Collecterez que du loot de Farm revient à remplir votre Case de
            Ticket de bus. La pratique qui tient : <strong>un jeu de clés par
            niveau de risque</strong> — un set bas risque pour Farm, un set
            haut risque pour Armory et Northridge — et l'on ne prend en raid
            que celui de la carte que l'on joue. Le gain de Koen vient de
            l'espace libéré dans le conteneur, pas de la clé supplémentaire.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

BLOC_RETRIEVAL = """          <h3 class="h4">Les boîtes de récupération : l'espace que vous ne payez pas</h3>
          <p>Quand vous récupérez l'équipement d'un adversaire, vous n model's
          récupérez pas que ses objets : vous récupérez aussi la
          <strong>boîte de récupération</strong> qui l'accompagne. Elle
          fonctionne comme une case supplémentaire de conteneur sécurisé, et
          elle est gratuite. Concrètement, l'un des avis de joueurs les plus
          utiles est que ce mécanisme offre l'équivalent de <strong>six cases
          de Case en plus</strong>, ce qui n'est pas négligeable quand la Case
          elle-même n'en offre que six.</p>
          <div class="callout callout-info">
            <p><strong>La règle de sécurité qui accompagne le loot.</strong> Ne
            foncez jamais sur un corps : l'équipe adverse observe très
            souvent, et la boîte de récupération est précisément ce qui
            déclenche l'embuscade. La séquence qui se répète dans les retours
            de joueurs : <strong>un angle sûr, un balayage de la zone, puis
            seulement le loot.</strong> L'angle se prend avant le sac, jamais
            l'inverse.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

BLOC_SACS = """          <h2 id="inception">Le sac dans le sac : l'inception de l'espace</h2>
          <p>La plupart des sacs et des rigs occupent dans votre inventaire
          autant de cases que ce qu'ils contiennent à l'intérieur. Certains
          font l'inverse : ils en rendent <strong>plus</strong> qu'ils n'en
          prennent. C'est ce que les joueurs appellent l'<em>inception</em> de
          l'espace, et c'est le premier réflexe de quiconque optimise son
          inventaire depuis six mois.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les contenants à slots positifs, du plus utile au plus niche</caption>
              <thead><tr><th scope="col">Contenant</th><th scope="col">Ce qu'il rend</th>
              <th scope="col">Comment l'utiliser</th></tr></thead>
              <tbody>
                <tr><td><strong>Rush Tac</strong></td>
                <td>Plus de cases à l'intérieur que la place qu'il occupe</td>
                <td>Le sac de base de l'inception : il se glisse dans un autre
                sac sans coût de place</td></tr>
                <tr><td><strong>Cowhide</strong></td>
                <td>Le plus grand gain de la catégorie</td>
                <td>Le contenant extérieur de référence pour un run
                d'optimisation</td></tr>
                <tr><td><strong>Retro Camping</strong></td>
                <td>Gain net positif, plus compact que le Cowhide</td>
                <td>Le compromis quand le poids et la place deviennent le
                facteur limitant</td></tr>
                <tr><td><strong>926</strong></td>
                <td>Deux cases rendues, net</td>
                <td>Le choix rationnel si vous ne visez pas
                l'optimisation maximale</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <p><strong>La règle de décision, en une phrase.</strong> Avant
            d'acheter un sac, demandez-vous s'il vous rend plus de cases
            qu'il n'en occupe. Si oui, c'est un achat qui se rembourse en
            espace. Si non, c'est un sac comme un autre, et il faut le juger
            sur sa capacité brute et son prix. Le même raisonnement s'applique
            aux rigs : <strong>un rig qui garde 14 slots pour 9 cases occupées
            vaut plus qu'un rig de 12 slots pour 10 cases occupées</strong>, et
            le gain se mesure en places de loot, pas en Millimètres de
            tissu.<span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
          <div class="callout callout-warning">
            <p><strong>L'angle mort de l'optimisation.</strong> Tout ce
            raisonnement porte sur l'espace, pas sur le poids. Un empilement de
            sacs optimise vos cases mais alourdit votre équipement : dans une
            zone à forte affluence, un raid lent est un raid qui finit en
            récupération de corps adverse. Optimisez l'espace en priorité
            quand vous avez le poids pour le porter — c'est-à-dire dans les
            zones où vous savez que vous ne swifterez pas.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

BLOC_RIGS = """          <h2 id="rig-positif">Le rig à slots positifs</h2>
          <p>La même logique que pour les sacs s'applique aux rigs, et elle est
          même plus rentable : un rig est porté sur le corps, il n'occupe donc
          pas de case de sac. Un rig qui rend plus de slots qu'il n'en consomme
          vous offre de la capacité de loot <strong>sans aucun coût
          d'espace dans le sac</strong>.</p>
          <div class="callout callout-success">
            <p><strong>La règle du rig positif.</strong> Comptez les slots
            qu'un rig offre, puis les cases qu'il occupe. Le rapport est
            positif dans un sens très simple : <strong>un rig qui garde 14
            slots pour 9 cases occupées est un rig qui vous donne cinq cases
            de loot gratis</strong> — l'équivalent d'un sac entier, sans le
            poids. C'est pourquoi les vieux rigs de la communauté reviennent
            dans tous les guides d'optimisation : ils sont plus volumineux que
            les modèles récents, mais ils stockent mieux. Un rig dense qui
            n'offre que dix slots pour dix cases occupées est, lui, un objet
            de Slot Park, pas un rig.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
          <div class="callout callout-info">
            <p><strong>Le réflexe de rangement.</strong> Un rig bien choisi se
            remplit de ce qui a le meilleur rapport valeur par case :
            attachements, munitions, médicaux, et casque quand le format le
            permet. Le reste du contenu se répartit entre le sac et les
            conteneurs à slots positifs. Deux boutons de l'interface font le
            travail à votre place — <em>Kit</em> et <em>Quick Organize</em> —
            et ils trouvent les objets même enfouis dans un rig ou au fond
            d'une pile de sacs.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

BLOC_DEKE = """          <h2 id="deke">Deke : le contact des offres à durée limitée</h2>
          <p>Le marché de l'onglet 1 parle de réputation et de volume ; il
          passe à côté d'un contact qui fonctionne sur un tout autre principe.
          <strong>Deke</strong> ne vend pas une gamme stable : il propose des
          <strong>offres à durée limitée</strong>, qui changent au fil de ses
          rafraîchissements. Casques, armures, rigs, sacs, clés, et
          occasionnellement des munitions à prix très bas. Chaque
          consultation de son offre est une occasion de comparer.</p>
          <div class="callout callout-success">
            <p><strong>La règle de consultation.</strong> Ce qui change la
            donne, ce n'est pas l'offre elle-même, c'est la <strong>fréquence
            de consultation</strong> : le catalogue bouge, les prix changent, et
            un contact consulté trois fois par jour offre trois fois plus
            d'occasions qu'un contact consulté une fois par semaine. C'est un
            flux de revenu à risque nul : aucune de ces ventes ne demande de
            sortir en raid, et même du matériel dont vous ne voulez pas
            ­ peut être revendu au marché pour une petite marge.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
          <div class="callout callout-info">
            <p><strong>La discipline du barter.</strong> Deux réflexes
            complètent le tableau. D'abord, comparer systématiquement le
            <strong>prix du barter</strong> et le <strong>prix du Market</em>
            : certains contacts cassent le prix sur des armes et des pièces,
            d'autres facturent au-dessus. Ensuite, ne rien acheter au prix
            fort quand le jeu vous le donne : les bundles d'événements, les
            missions de saison et les récompenses de barre offrent
            régulièrement le même objet pour rien.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

BLOC_CORRECTION_DEKE = [("à prix très bas", "à prix très bas"),
                         ("souvent", "souvent")]


def insere(texte, ancre, bloc, marqueur):
    """Insere le bloc juste avant l'ancre. Idempotent via le marqueur."""
    if marqueur in texte:
        return texte, False
    i = texte.find(ancre)
    if i < 0:
        raise SystemExit("  ANCRE INTROUVABLE : " + ancre[:70])
    return texte[:i] + bloc + texte[i:], True


def maj_date(t, date="2026-11-18"):
    t = re.sub(r'("dateModified": ")\d{4}-\d{2}-\d{2}(")', rf"\g<1>{date}\g<2>", t)
    t = re.sub(r'("datePublished": ")\d{4}-\d{2}-\d{2}(")', rf"\g<1>{date}\g<2>", t)
    return t


def main():
    echecs = []

    travaux = [
        ("items-cles.html",
         '<h2 id="conseils">5. Conseils d\'exploitation</h2>',
         BLOC_CLES, "Quand une clé s'éteint", None),
        ("guide-extraction.html",
         '          <h3 class="h4">La récupération par les coéquipiers',
         BLOC_RETRIEVAL, "Les boîtes de récupération", None),
        ("equipement-sacs.html",
         '          <h2 id="conseils">2. Conseils d\'emport</h2>',
         BLOC_SACS, "Le sac dans le sac", None),
        ("equipement-rigs.html",
         '          <h2 id="conseils">2. Conseils d\'opérateur</h2>',
         BLOC_RIGS, "Le rig à slots positifs", None),
        ("guide-traders.html",
         '<h2 id="erreurs">5. Les erreurs de marchand',
         BLOC_DEKE, "Deke : le contact des offres", None),
    ]

    for page, ancre, bloc, marqueur, _ in travaux:
        f = CIBLE / page
        s = f.read_text(encoding="utf-8")
        try:
            s, ok = insere(s, ancre, bloc, marqueur)
        except SystemExit as e:
            echecs.append(f"{page} : {e}")
            continue
        if ok:
            s = maj_date(s)
            f.write_text(s, encoding="utf-8")
            print(f"  {page:26s} bloc insere")
        else:
            print(f"  {page:26s} deja present")

    if echecs:
        for e in echecs:
            print("  ERREUR :", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
