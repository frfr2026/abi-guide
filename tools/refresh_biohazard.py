#!/usr/bin/env python3
"""Ajoute les emplacements des Biohazard Bags a la page Infected Zone.

Source : guide communautaire Season 7 "UTOPIA Complete Survivor & Beginner
Guide" (Reddit, 24 septembre 2026). Localisations decodees par la
perk Zombie Footprint Tracking, qui affiche des empreintes luminescentes.
Statut : donnee COMMUNAUTAIRE, les emplacements ne sont pas publies par
l'editeur et peuvent varier selon la seed.
"""
import pathlib, re

P = pathlib.Path('pages/saison7-zombie-infected-zone.html')
s = P.read_text(encoding='utf-8')

NEW = '''          <h2 id="biohazard">5. Les Biohazard Bags — où les trouver</h2>
          <p>Les <strong>Biohazard Bags</strong> sont des conteneurs cachés qui rapportent un loot de
          haut niveau. Ils ne sont pas visibles : il faut <strong>équiper la perk de suivi d'empreintes
          zombies</strong>, qui affiche des <strong>traces lumineuses</strong> au sol à partir des zones
          connues. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Emplacements des Biohazard Bags (données communautaires)</caption>
              <thead><tr><th scope="col">Zone</th><th scope="col">Où précisément</th><th scope="col">Nombre</th></tr></thead>
              <tbody>
                <tr><td><strong>Tar Area</strong></td><td>Suivez les empreintes dans la boue jusqu'au cœur de la zone de tranchées</td><td>1</td></tr>
                <tr><td><strong>Port</strong></td><td>Juste derrière le conteneur d'expédition bleu, à gauche de la porte d'entrée principale</td><td>1</td></tr>
                <tr><td><strong>Burnt Forest</strong></td><td>Au centre du cratère d'impact, juste à côté de l'épave calcinée</td><td>1</td></tr>
                <tr><td><strong>Factory Compound</strong></td><td><strong>Deux</strong> sacs : l'un à côté de la loge de garde de l'entrée principale, l'autre dans le parking souterrain à droite de la tour</td><td>2</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">Ces emplacements peuvent varier</h3>
            <p>Ces positions viennent de la communauté, pas de l'éditeur. Le point important n'est pas la
            coordonnée exacte : c'est la <strong>méthode</strong>. Un Biohazard Bag se localise en
            traçant, pas en devinant. Procédure :</p>
            <ol>
              <li><strong>Équipez la perk de suivi d'empreintes</strong> avant d'entrer en zone infectée.</li>
              <li><strong>Marchez sur les traces</strong> — elles glowent et mènent à la zone concernée.</li>
              <li><strong>Vérifiez les points de repère physiques</strong> : le conteneur bleu du Port, le
                cratère du Burnt Forest, la loge de garde et le parking souterrain du Factory Compound.</li>
              <li><strong>Ne perdez pas de temps si le sac n'y est pas</strong> : la position peut varier
                selon la partie. Un sac raté coûte deux minutes, pas un raid.</li>
            </ol>
          </div>

'''

# Insertion avant la section "6. Le marchand de terrain"
ANCHOR = None
for m in re.finditer(r'<h2 id="([a-z-]+)">(\d+\. [^<]+)</h2>', s):
    if 'marchand' in m.group(1):
        ANCHOR = m.start()
        break
assert ANCHOR is not None, 'point d insertion introuvable'
s = s[:ANCHOR] + NEW + s[ANCHOR:]

# Renumerotation des H2 qui suivent
suffixes = [
    ('<h2 id="marchand">6. Le marchand de terrain</h2>', '<h2 id="marchand">6. Le marchand de terrain</h2>'),
    ('<h2 id="recherche">7. La progression Zombie Research</h2>', '<h2 id="recherche">7. La progression Zombie Research</h2>'),
    ('<h2 id="checklist">8. Check-list avant d\'entrer</h2>', '<h2 id="checklist">8. Check-list avant d\'entrer</h2>'),
    ('<h2 id="sources">9. Sources</h2>', '<h2 id="sources">9. Sources</h2>'),
]
for a, b in suffixes:
    s = s.replace(a, b)

# Sommaire : ajouter l'entree
m = re.search(r'<aside class="toc".*?</aside>', s, re.S)
if m:
    toc = m.group(0)
    s = s.replace(toc, toc.replace('</aside>',
              '<a href="#biohazard" id="lnk-saison7-zombie-infected-zone-093">5. Les Biohazard Bags</a>\n        </aside>'))

P.write_text(s, encoding='utf-8')
print('saison7-zombie-infected-zone.html : section Biohazard Bags ajoutee')
