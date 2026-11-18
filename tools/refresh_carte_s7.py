#!/usr/bin/env python3
"""Ajoute les changements de carte de la Saison 7 et les astuces de tir.

1. pages/map-farm.html : la Saison 7 a modifie la carte de Farm. Les notes de
   patch officielles de la beta mentionnent explicitement des ajustements
   autour du petit etang du Wheatfield (suppression de murs invisibles,
   meilleure traversabilite) et l'ajout d'un nouveau conteneur, le
   "collection cabinet". C'est une information operationnelle : un mur
   invisible qui disparait change une route entiere.

2. pages/armes-fusils-assaut.html : trois techniques de tir concrete
   rapportees par la communaute en S7, dont une est une mecanique reelle du
   jeu et non une preference :
     - l'AN-94 en mode automatique, declenche en tapes rapides : les deux
       premieres balles de chaque tape se regroupent presque parfaitement ;
     - l'A545 a la tete contre du 5.45 : on vise les hanches, les cuisses et
       les genoux, pas le torse, et on tire de hip ou en ADS leger ;
     - le M290 comme outil d'ouverture au corps a corps.

Source : notes de patch officielles de la beta S7 (recopiees sur Reddit) et
retours de joueurs et createurs de contenu. Les techniques sont attribuees a
la communaute, les modifications de carte a l'editeur.

Idempotent.
"""
import pathlib

FARM = '''          <h3 class="h4">Ce que la Saison 7 a change à Farm</h3>
          <p>La carte n'est pas restée la même en S7, et ce n'est pas anecdotique : une modification de
          traversabilité change une route entière, donc change le prix d'une extraction.</p>
          <ul>
            <li><strong>Autour du petit étang du Wheatfield</strong> — des ajustements ont été apportés, avec notamment la <strong>suppression de murs invisibles</strong> et une <strong>meilleure traversabilité</strong>. Ce qui était un détour baffuant peut désormais être une ligne droite — et inversement.</li>
            <li><strong>Un nouveau conteneur : le collection cabinet</strong> — ajouté en S7, avec des ajustements apportés à certains autres conteneurs de la carte.</li>
          </ul>
          <p class="small text-muted">Source : notes de patch officielles de la beta de la Saison 7 (MoreFun
          Studios), recopiées et publiées par la communauté. Annonce éditeur.</p>
'''

TIR = '''          <h3 class="h4">Trois techniques de tir qui changent tout en S7</h3>
          <div class="grid grid--2">
            <article class="card">
              <div class="card-body">
                <h3 class="h4">L'AN-94 : la manuelle en mode automatique</h3>
                <p>C'est une mécanique du jeu, pas une préférence :
                <strong>ne passez pas le sélecteur en mode rafale à 3 balles</strong>. Laissez l'arme en
                <strong>automatique</strong> et travaillez votre <strong>déclenchement semi-automatique manuel
                — le tap rapide</strong>. Le mécanisme regroupe alors <strong>les deux premières balles de
                chaque tape presque parfaitement au même point</strong>.</p>
                <p>Concrètement : avec la même ammunition 5,45 que l'A545 et l'AK-12, un AN-94 joué en taps
                peut <strong>fendre une plaque de niveau 5</strong> avant que l'adversaire ne réagisse au bruit.
                C'est l'arme la moins chère du lot à rendre un résultat de niveau 5.</p>
                <p class="small text-muted">Source : conseil communautaire, S7. Donnée communautaire.</p>
              </div>
            </article>
            <article class="card">
              <div class="card-body">
                <h3 class="h4">L'A545 : viser les jambes, pas le torse</h3>
                <p>L'A545 tire très vite, et c'est sa puissance de feu qui fait le travail. Mais en 5,45,
                <strong>les munitions à chair ne percent pas une plaque de torse de niveau 5</strong> : inutile
                d'essayer.</p>
                <p>La méthode qui fonctionne : <strong>viser les hanches, les cuisses et les genoux</strong>, en
                <strong>hipfire ou en visée légère</strong>, et comboser le combat en intérieur. Vous touchez une
                zone que l'armure ne couvre pas, et vous cassez la mobilité de l'adversaire plutôt que sa
                vie.</p>
                <p>Un point de vigilance inverse : le <strong>M290 est l'outil d'ouverture au corps à corps</strong>
                de la saison. Quand une porte doit céder, c'est lui, pas la rafale.</p>
                <p class="small text-muted">Source : conseils communautaires, S7. Donnée communautaire.</p>
              </div>
            </article>
          </div>
'''

JOBS = [
    ('pages/map-farm.html', 'zones', FARM),
    ('pages/armes-fusils-assaut.html', 'munitions', TIR),
]

for path, anchor, block in JOBS:
    p = pathlib.Path(path)
    s = p.read_text(encoding='utf-8')
    if 'Ce que la Saison 7 a chang' in s or 'Trois techniques de tir' in s:
        print('  deja enrichi :', path)
        continue
    i = s.find('id="%s"' % anchor)
    if i < 0:
        print('  ancre introuvable, skip :', path, anchor)
        continue
    j = s.rfind('<h2 ', 0, i)
    if j < 0:
        j = s.rfind('<h3 ', 0, i)
    assert j > 0, path
    s = s[:j] + block.strip() + '\n\n' + s[j:]
    p.write_text(s, encoding='utf-8')
    print('  %-38s enrichi' % path)
