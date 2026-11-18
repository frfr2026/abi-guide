#!/usr/bin/env python3
"""Enrichit pages/equipement-headsets.html avec les arbitrages audio concrets.

Sources : discussions communautaires (Reddit, wiki fandom "How to play") et
les notes officielles S7 (Acoustic Earpads, Last Stand).
"""
import pathlib, re

P = pathlib.Path('pages/equipement-headsets.html')
s = P.read_text(encoding='utf-8')

NEW = '''          <h2 id="arbitrages">5. Les arbitrages audio que personne n'explique</h2>
          <p>Un casque audio ne change aucune statistique. Il change <strong>le moment où vous apprenez qu'un
          ennemi existe</strong> — et en extraction shooter, une information arrivée deux secondes trop tard
          vaut zéro. Encore faut-il savoir ce que vous perdez exactement. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Ce que vous entendez, ce que vous perdez</caption>
              <thead><tr><th scope="col">Information</th><th scope="col">Ce que l'ouïe donne</th><th scope="col">La contrepartie</th></tr></thead>
              <tbody>
                <tr><td><strong>Rechargement</strong></td><td>Un rechargement est un bruit métallique net : on sait qu'un ennemi recharge, donc qu'il est vulnérable</td><td>Aucun — c'est la Dividend info la plus rentable du jeu</td></tr>
                <tr><td><strong>Painkillers</strong></td><td>Le bruit caractéristique d'un soin consommé signale un ennemi blessé, donc probablement proche</td><td>Vous l'entendez, mais le bruit de vos propres soins vous trahit aussi</td></tr>
                <tr><td><strong>Pas et collisions</strong></td><td>Un déplacement sur du métal ou du gravier s'entend de loin</td><td>Sur terrain meuble, le silence est total : le casque n'a rien à vous donner</td></tr>
                <tr><td><strong>Blocage sonore du casque</strong></td><td>—</td><td><strong>C'est le vrai coût.</strong> Un casque lourd covering les oreilles coupe une partie du spectre : c'est pourquoi les Acoustic Earpads existent</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">Le vrai arbitrage n'est pas « passif ou électronique »</h3>
            <p>La question utile n'est pas « quel casque audio choisir » mais <strong>« mon casque de tête
            me laisse-t-il entendre ? »</strong> Trois cas concrets :</p>
            <ul>
              <li><strong>Casque T5/T6 couvrant les oreilles</strong> (03 Heavy, RSP, SH Maska) : même un casque
                audio excellent ne servira presque à rien. Les <strong>Acoustic Earpads</strong>, qui réduisent
                l'effet de blocage des casques, sont précisément la réponse officielle à ce problème.
                <span class="src-tag src-officiel">Officiel</span></li>
              <li><strong>Casque audio en révision d'un : il faut à la fois les oreilles et la information</strong> :
                l'IND70 est cité comme la seule option T6 compatible avec un casque audio de type GS2.
                <span class="src-tag src-communautaire">Communautaire</span></li>
              <li><strong>En escouade</strong> : un camarade qui porte le casque audio peut porter le casque
                lourd qui bloque le son, et vous restituer l'information. Le travail d'équipe remplace
                l'équipement. <span class="src-tag src-communautaire">Communautaire</span></li>
            </ul>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Le protocole audio en quatre temps</h3>
            <ol>
              <li><strong>Avant de pousser</strong> : arrêtez-vous, coupez le son du jeu, listenez 5 secondes.
                C'est la décision la plus rentable du jeu et presque personne ne la prend.</li>
              <li><strong>En rotation</strong> : déplacez-vous par à-coups, jamais en ligne droite. Le bruit que
                vous faites est une information que vous offrez.</li>
              <li><strong>Après un tir</strong> : changez de position immédiatement. Votre position est connue.</li>
              <li><strong>Avant l'extraction</strong> : le silence est un atout — un couloir sans bruit est un
                couloir que personne ne surveille.</li>
            </ol>
          </div>

'''

ANCHOR = '          <h2 id="galerie-officielle">Galerie officielle</h2>'
assert ANCHOR in s, 'point d insertion introuvable'
s = s.replace(ANCHOR, NEW + ANCHOR)

m = re.search(r'<aside class="toc".*?</aside>', s, re.S)
if m:
    toc = m.group(0)
    s = s.replace(toc, toc.replace('</aside>',
              '<a href="#arbitrages" id="lnk-equipement-headsets-094">5. Les arbitrages audio</a>\n        </aside>'))

P.write_text(s, encoding='utf-8')
print('equipement-headsets.html : section arbitrages ajoutee')
