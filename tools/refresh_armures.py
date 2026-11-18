#!/usr/bin/env python3
"""Enrichit pages/equipement-armures.html avec le leadership T5/T6.

Les donnees proviennent de discussions communautaires (Reddit, wiki fandom
"Beginner Guide", mmoexp) croisees avec les statistiques officielles des
artworks. Elles sont marquees comme communautaires la ou elles ne sont pas
issues de l'editeur.
"""
import pathlib, re

P = pathlib.Path('pages/equipement-armures.html')
s = P.read_text(encoding='utf-8')

ANCHOR = '''          <div class="callout callout-success"><h4>Compléter le set</h4>'''

NEW = '''          <h2 id="leadership">4. Le leadership T5 et T6, pièce par pièce</h2>
          <p>Une armure ne se juge pas sur son tier seul mais sur <strong>ce qu'elle protège</strong>, son
          <strong>poids</strong>, ses <strong>pénalités d'ergonomie</strong> et son <strong>prix</strong>. Voici les
          pièces que la communauté place en tête pour chaque palier, avec les statistiques officielles à
          l'appui. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Armures T5 et T6 — le podium par usage</caption>
              <thead><tr><th scope="col">Palier</th><th scope="col">Pièce</th><th scope="col">Ce qu'elle protège</th><th scope="col">À retenir</th></tr></thead>
              <tbody>
                <tr><td rowspan="3"><strong>T5</strong></td><td><strong>BT6 Heavy</strong></td><td>Poitrine + haut abdomen</td><td>Le choix T5 « tout compris » — mais <strong>2,5× le prix</strong> du M4 : c'est un achat de fin de progression</td></tr>
                <tr><td><strong>M4 Defender</strong></td><td>Poitrine</td><td><strong>Meilleur rapport T5</strong> selon la communauté : plus grand pool de PV, meilleure viabilité au réparation, excellent stockage</td></tr>
                <tr><td><strong>KN Field Commander</strong></td><td>Poitrine seule</td><td>Pénalités décrochantes, prix raisonnable, plus de durabilité que la 926 — le choix « mobilité »</td></tr>
                <tr><td rowspan="2"><strong>T6</strong></td><td><strong>KN Composite</strong></td><td>Poitrine + haut abdomen</td><td>Le standard T6 : protection complète, poids raisonnable, pénalités correctes</td></tr>
                <tr><td><strong>Spartan B</strong></td><td>Poitrine</td><td>Le « tank » — mais <strong>très lent</strong> : à réserver au raid où l'on accepte de trade la mobilité</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">Le piège du T6 « pour être tranquille »</h3>
            <p>Le raisonnement « je mets du T6 et je ne meurs plus » est faux, et il coûte cher. En
            <strong>Normal</strong>, le cap officiel est <strong>T4</strong> : un T6 n'y apporte aucun avantage
            mécanique face à un T4 bien joué, mais il coûte plusieurs fois plus cher à perdre. Et comme
            l'a dit un joueur du subreddit : <em>« la plupart de tes morts seront un tir dans le masque »</em> —
            ce qui tue, ce n'est pas le tier du torse, c'est le <strong>visage</strong>. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>La règle qui tient : <strong>le casque et le masque protègent plus que le gilet</strong>. Un T5
            avec masque T5 bat un T6 avec visage nu.</p>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Les deux builds qui résument l'état du jeu</h3>
            <ul>
              <li><strong>Budget</strong> — T3 sur le torse, casque T3 à visière, rig Canvas et sac Moyen, munitions
                T4. On survit aux tireurs de niveau moyen et on perfore les casques standard. C'est le kit de la
                phase 1 de l'économie. <span class="src-tag src-communautaire">Communautaire</span></li>
              <li><strong>Chad</strong> — H416 ou FAL entièrement moddées (barre long, suppresseur premium, chargeur
                60, optique holographique), M995 T5/6, armure T5-T6 pleine protection, casque T5 avec visière T5,
                grand rig pour porter les chargeurs et le médical. C'est le kit Armory et Lockdown haut.
                <span class="src-tag src-communautaire">Communautaire</span></li>
            </ul>
          </div>

'''

assert ANCHOR in s, 'point d insertion introuvable'
s = s.replace(ANCHOR, NEW + ANCHOR)

# Sommaire
m = re.search(r'<aside class="toc".*?</aside>', s, re.S)
if m:
    toc = m.group(0)
    new_toc = toc.replace('</aside>',
                          '<a href="#leadership" id="lnk-equipement-armures-097">4. Le leadership T5 / T6</a>\n        </aside>')
    s = s.replace(toc, new_toc)

P.write_text(s, encoding='utf-8')
print('equipement-armures.html : section leadership T5/T6 ajoutee')
