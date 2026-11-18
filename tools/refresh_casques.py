#!/usr/bin/env python3
"""Enrichit pages/equipement-casques.html avec le leadership T4/T5/T6.

Sources : statistiques officielles des artworks (buffbuff, zilliongamer) et
classement communautaire (Reddit, wiki fandom "Beginner Guide").
Le site desactive le son est signale comme la contrepartie de la protection.
"""
import pathlib, re

P = pathlib.Path('pages/equipement-casques.html')
s = P.read_text(encoding='utf-8')

NEW = '''          <h2 id="leadership">4. Le leadership par palier, et le vrai coût du casque</h2>
          <p>Un casque ne se choisit pas sur son tier seul. Il y a trois variables : la <strong>protection du
          crâne</strong>, la <strong>couverture du visage</strong> (masque T3, T4, T5 ou T6 accepté ?) et le
          <strong>blocage sonore</strong> — parce qu'un casque qui vous rend sourd est un casque qui vous fait
          mourir. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les casques que la communauté place en tête</caption>
              <thead><tr><th scope="col">Palier</th><th scope="col">Casque</th><th scope="col">Points forts</th><th scope="col">Le compromis</th></tr></thead>
              <tbody>
                <tr><td rowspan="2"><strong>T4</strong></td><td><strong>KSS2 Tactical</strong></td><td>Protection crâne + oreilles, 45 de durabilité, masque T3</td><td>Le meilleur « tout compris » en T4 — le visage T3 reste la faille</td></tr>
                <tr><td><strong>KLSS</strong></td><td>Protection T4 complète, très couvrant</td><td>Couvre les oreilles : impossible d'y porter un casque audio</td></tr>
                <tr><td rowspan="2"><strong>T5</strong></td><td><strong>AN95 Heavy Blast</strong></td><td>Protection crâne + oreilles, 55 de durabilité, masque T4</td><td>Prix élevé (~100 000 K) mais le meilleur compromis T5</td></tr>
                <tr><td><strong>03 Heavy Tactical</strong></td><td>Masque jusqu'au T4, montage T7, 45 de durabilité</td><td>Atténuation sonore forte, et 51 000 K pour moins de protection que l'AN95</td></tr>
                <tr><td rowspan="2"><strong>T6</strong></td><td><strong>IND70 Tactical</strong></td><td>Protection visage + oreilles, compatible casque audio GS2</td><td>Le « tous azimuths » T6, et le meilleur rapport du palier</td></tr>
                <tr><td><strong>SH65 Military</strong></td><td>Protection crâne T6, option masque T5 ou T6, blocage sonore faible</td><td>Le choix « blindé » : se fier à l'ouïe plutôt qu'à l'épaisseur</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">La règle qui vaut plus que le tier</h3>
            <p>Un joueur du subreddit le formule ainsi : <em>« la plupart de tes morts seront le masque qui
            se prend la balle »</em>. Concrètement, <strong>un casque T5 avec masque T5 tue moins souvent qu'un
            casque T6 avec visage découvert</strong>. Le budget se met d'abord sur le <strong>masque</strong>, pas
            sur le crâne. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>Et l'arbitrage inverse existe aussi : si vous jouez en escouade avec un camarade qui porte le
            casque audio, le <strong>SH65</strong> devient cohérent, parce que son blocage sonore faible est
            compensé par l'oreille de l'autre.</p>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">La règle du masque selon le niveau adverse</h3>
            <p>Si vous vous battez contre des joueurs en T4, T5 et T6, ils ont de la T4 : un masque T3 ne
            survivra pas à un tir au visage. Deux solutions — soit <strong>un masque T5</strong> (IND70, SH65,
            6BNT), soit <strong>un casque bas de gamme à masque T4</strong> comme le FA Assault, moins cher et
            suffisant dans la majorité des duels. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>Et pour rappel, les <strong>casques audio</strong> ne protègent pas : ils vous font entendre.
            Toute la famille des Acoustic Earpads S7 (réduction du blocage sonore des casques) se trouve dans
            notre <a href="equipement-headsets.html" id="lnk-equipement-casques-093">guide des casques audio</a>.</p>
          </div>

'''

ANCHOR = '          <h2 id="galerie-masques">Les masques, article par article</h2>'
assert ANCHOR in s, 'point d insertion introuvable'
s = s.replace(ANCHOR, NEW + ANCHOR)

# Sommaire
m = re.search(r'<aside class="toc".*?</aside>', s, re.S)
if m:
    toc = m.group(0)
    s = s.replace(toc, toc.replace('</aside>',
              '<a href="#leadership" id="lnk-equipement-casques-095">4. Le leadership par palier</a>\n        </aside>'))

P.write_text(s, encoding='utf-8')
print('equipement-casques.html : section leadership ajoutee')
