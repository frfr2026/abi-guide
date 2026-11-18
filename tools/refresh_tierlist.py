#!/usr/bin/env python3
"""Enrichit pages/armes-tier-list.html avec les statistiques officielles.

Source : wiki officiel ABI (Template:WeaponData + fiches armes). Ce sont les
caracteristiques de l'arme telles que documentees, distinctes du classement
communautaire. Les tiers restent explicitement attribues a la communaute.
"""
import pathlib, re

P = pathlib.Path('pages/armes-tier-list.html')
s = P.read_text(encoding='utf-8')

if 'Statistiques officielles par arme' in s:
    print('deja enrichi')
    raise SystemExit(0)

# ── Tableau de stats officielles ────────────────────────────────────────
# colonnes : arme, calibre, mode, recul vertical, ergonomie, precision,
# portee effective, cadence, poids
OFFICIAL_ROWS = [
    ('M24', '7.62×51mm', 'Bolt-Action', '7', '39', '90', '120', '30', '4,40'),
    ('SJ16', '.338 Caliber', 'Bolt-Action', '11', '32', '90', '125', '26', '6,48'),
    ('SVDS', '7.62×54mm', 'Semi', '43', '44', '91', '83', '225', '7,36'),
    ('M110', '7.62×51mm', 'Semi', '58', '58', '91', '80', '300', '6,97'),
    ('MK14', '7.62×51mm', 'Semi, Full', '57', '59', '69', '55', '700', '8,14'),
    ('T192', '5.8×42mm', 'Semi, Full', '66', '84', '60', '41', '750', '2,50'),
    ('AN-94', '5.45×39mm', '2 Round Burst, Semi, Full', '60', '59', '72', '57', '630', '4,40'),
    ('M14', '7.62×51mm', 'Semi', '44', '45', '76', '66', '350', '5,34'),
    ('RPK-16', '5.45×39mm', 'Semi, Full', '73', '51', '57', '53', '750', '6,63'),
    ('MCX', '5.56×45mm', 'Semi, Full', '77', '80', '30', '30', '700', '2,61'),
    ('P90', '5.7×28mm', 'Semi, Full', '73', '72', '20', '36', '1000', '3,73'),
    ('Vector .45', '.45 Caliber', '2 Round Burst, Semi, Full', '62', '71', '21', '25', '1100', '3,28'),
    ('MPX', '9×19mm', 'Semi, Full', '68', '81', '25', '33', '850', '3,77'),
    ('MP5', '9×19mm', 'Semi, Full', '70', '74', '22', '28', '750', '3,89'),
    ('H416', '5.56×45mm', 'Semi, Full', '72', '73', '39', '32', '860', '4,42'),
    ('AUG', '5.56×45mm', 'Semi, Full', '77', '68', '59', '46', '750', '3,88'),
    ('FAMAS', '5.56×45mm', '3 Round Burst, Semi, Full', '73', '51', '45', '40', '900', '3,31'),
    ('AK-12', '5.45×39mm', '3 Round Burst, Semi, Full', '69', '60', '43', '55', '730', '3,89'),
    ('AKM', '7.62×39mm', 'Semi, Full', '50', '44', '38', '54', '600', '3,56'),
    ('FAL', '7.62×51mm', 'Semi, Full', '52', '43', '42', '51', '630', '6,93'),
    ('M4A1', '5.56×45mm', 'Semi, Full', '71', '57', '41', '49', '750', '5,57'),
    ('S12K', '12×70mm', 'Semi', '30', '66', '10', '14', '200', '4,85'),
    ('AKS-74U', '5.45×39mm', 'Semi, Full', '52', '44', '29', '33', '500', '4,93'),
    ('VSS', '9×39mm', 'Semi, Full', '65', '57', '44', '26', '850', '6,22'),
]

rows_html = '\n'.join(
    '                <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % r
    for r in OFFICIAL_ROWS)

BLOCK = '''
          <h2 id="stats-officielles">3. Statistiques officielles par arme</h2>
          <p>Le classement en tier est <strong>communautaire</strong>. Les chiffres ci-dessous ne le sont pas : ils sont repris du <strong>wiki officiel d'Arena Breakout Infinite</strong> (modèle de données <code>WeaponData</code> et fiches armes). Ce sont les caractéristiques brutes de l'arme — utile pour vérifier une intuition, inutile pour décider qui gagne un duel.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Calibre</th><th>Mode de tir</th><th>Recul vertical</th><th>Ergonomie</th><th>Précision</th><th>Portée effective</th><th>Cadence (RPM)</th><th>Poids</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : wiki officiel ABI, modèle de données <code>WeaponData</code>. L'échelle est identique pour toutes les armes : le recul se compte vers le haut (valeur haute = plus de recul), la précision et la portée effective sont exprimées sur l'échelle interne du jeu, la cadence en tours par minute. Ces valeurs bougent à chaque patch — l'armurerie en jeu reste la référence.</p>

          <div class="callout callout-info">
            <h3 class="h4">Comment lire ce tableau face à la tier list</h3>
            <ul>
              <li><strong>Le M24 et le SJ16</strong> cumulent précision 90 et portée effective 120-125, avec un recul vertical de 7 et 11 — les deux valeurs les plus faibles de la liste. Ils sont lents (26-30 RPM). C'est le profil « un tir, une décision ».</li>
              <li><strong>Le T192</strong> affiche l'ergonomie la plus élevée de tout l'échantillon (84) avec un poids de 2,50 — l'un des plus légers. Sur le papier, c'est l'arme la plus maniable ; en pratique, une précision de 60 et une portée de 41 la limitent au combat rapproigné et à la visée rapide.</li>
              <li><strong>Le Vector .45</strong> et le <strong>MPX</strong> combinent cadence (1100 et 850 RPM) et ergonomie (71 et 81) : ils encaissent la pression au corps à corps, mais leur précision (21 et 25) et leur portée (25 et 33) interdisent le duel à distance.</li>
              <li><strong>Le FAL</strong> est le plus lourd de l'échantillon (6,93) avec 43 d'ergonomie — le retour de manivelle se paie. Son canon long est en revanche son atout : 51 de portée effective pour un 7.62×51mm.</li>
              <li><strong>Le S12K</strong> n'a que 10 de précision et 14 de portée : c'est normal, ce n'est pas une arme de précision. Il compte sur le volume de pellets et sur l'agglomération.</li>
            </ul>
          </div>

          <div class="callout callout-warning">
            <h3 class="h4">Ce que le wiki ne documente pas encore</h3>
            <p>Le <strong>A545</strong> et l'<strong>AK-15SC</strong>, les deux fusil de la Saison 7 Utopia, ne figurent pas encore dans le modèle de données du wiki. Les valeurs de leurs fiches sur ce site proviennent donc d'autres sources, et restent à confirmer — nous les signalons comme telles plutôt que de les faire passer pour des données officielles. De même, le prix d'une arme et sa disponibilité en raid ne figurent dans aucune base publique : ce sont des données de terrain, pas des chiffres publiés.</p>
          </div>
''' % rows_html

# ── Insertion : avant la section tier-interactive ───────────────────────
anchor = '          <h2 id="tier-interactive">3. Tier list interactive</h2>'
if anchor in s:
    s = s.replace(anchor, BLOCK.strip() + '\n\n          <h2 id="tier-interactive">4. Tier list interactive</h2>', 1)
else:
    # l'ancre peut avoir un autre numero
    m = re.search(r'<h2 id="tier-interactive">(\d+)\. Tier list interactive</h2>', s)
    if not m:
        raise SystemExit('ancre tier-interactive introuvable')
    n = int(m.group(1))
    s = s[:m.start()] + BLOCK.strip() + '\n\n          <h2 id="tier-interactive">%d. Tier list interactive</h2>' % (n+1) + s[m.end():]
    # renumeroter les sections suivantes
    for old, new in [(4,5),(5,6),(6,7)]:
        s = s.replace('<h2 id="s7-notes">%d. Ce qui crée ce meta</h2>' % old,
                      '<h2 id="s7-notes">%d. Ce qui crée ce meta</h2>' % new)
        s = s.replace('<h2 id="par-carte">%d. Tier par carte (l\'onglet qui compte)</h2>' % old,
                      '<h2 id="par-carte">%d. Tier par carte (l\'onglet qui compte)</h2>' % new)
        s = s.replace('<h2 id="compare">%d. Comparateur d\'armes</h2>' % old,
                      '<h2 id="compare">%d. Comparateur d\'armes</h2>' % new)

P.write_text(s, encoding='utf-8')
print('pages/armes-tier-list.html enrichi')
