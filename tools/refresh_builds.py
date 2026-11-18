#!/usr/bin/env python3
"""Enrichit pages/armes-builds.html avec les statistiques officielles.

Source : wiki officiel ABI (Template:WeaponData). Pour chaque arme de build,
on ajoute une ligne de caracteristiques officielles. Cela permet de verifier
si la description du build (recul, cadence, ergonomie) resiste a l'examen.

Les couts annonces restent des estimations communautaires : ils sont signales
comme tels.
"""
import pathlib, re

P = pathlib.Path('pages/armes-builds.html')
s = P.read_text(encoding='utf-8')

if 'build-officiel' in s:
    print('deja enrichi')
    raise SystemExit(0)

# stats officielles : arme -> (nom officiel, calibre, mode, recul_v, ergo, precision, portee, cadence, poids)
STATS = {
 'A545': ('A545 (non encore documentée au wiki)', '5.45×39mm', '—', '—', '—', '—', '—', '—', '—'),
 'AK-12': ('AK12 Assault Rifle', '5.45×39mm', '3 Round Burst, Semi, Full', '69', '60', '43', '55', '730', '3,89'),
 'Vector .45': ('Vector 45 Micro SMG', '.45 Caliber', '2 Round Burst, Semi, Full', '62', '71', '21', '25', '1100', '3,28'),
 'M24': ('M24 Bolt-Action Rifle', '7.62×51mm', 'Bolt-Action', '7', '39', '90', '120', '30', '4,40'),
 'FAL': ('FAL Assault Rifle', '7.62×51mm', 'Semi, Full', '52', '43', '42', '51', '630', '6,93'),
}

BLOCK = '''
          <h2 id="build-officiel">6. Chaque build face aux chiffres officiels</h2>
          <p>Les caractéristiques ci-dessous sont reprises du <strong>wiki officiel</strong> (modèle de données <code>WeaponData</code>). Elles permettent de vérifier si ce que les builds promettent tient la route — en particulier sur le recul, l'ergonomie et la cadence. Les <strong>coûts</strong> annoncés dans les sections précédentes restent, eux, des estimations communautaires : le wiki ne publie aucun prix.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Build</th><th>Arme (nom officiel)</th><th>Calibre</th><th>Mode de tir</th><th>Recul vertical</th><th>Ergonomie</th><th>Précision</th><th>Portée effective</th><th>Cadence (RPM)</th><th>Poids</th></tr></thead>
              <tbody>
                <tr><td>A545 « Utopia »</td><td><strong>Non documentée au wiki</strong></td><td>5.45×39mm</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
                <tr><td>AK-12 « Laser Budget »</td><td>AK12 Assault Rifle</td><td>5.45×39mm</td><td>3 Round Burst, Semi, Full</td><td>69</td><td>60</td><td>43</td><td>55</td><td>730</td><td>3,89</td></tr>
                <tr><td>Vector .45 « Infected Clear »</td><td>Vector 45 Micro SMG</td><td>.45 Caliber</td><td>2 Round Burst, Semi, Full</td><td>62</td><td>71</td><td>21</td><td>25</td><td>1100</td><td>3,28</td></tr>
                <tr><td>M24 « Tribunal »</td><td>M24 Bolt-Action Rifle</td><td>7.62×51mm</td><td>Bolt-Action</td><td>7</td><td>39</td><td>90</td><td>120</td><td>30</td><td>4,40</td></tr>
                <tr><td>FAL « Forbidden Tribunal »</td><td>FAL Assault Rifle</td><td>7.62×51mm</td><td>Semi, Full</td><td>52</td><td>43</td><td>42</td><td>51</td><td>630</td><td>6,93</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : wiki officiel ABI. L'échelle est celle du jeu : recul vers le haut (valeur haute = plus de recul), précision et portée effective sur l'échelle interne, cadence en tours par minute.</p>

          <div class="callout callout-info">
            <h3 class="h4">Ce que les chiffres confirment — et ce qu'ils nuancent</h3>
            <ul>
              <li><strong>Le M24 est le plus propre de la série</strong> : recul vertical de 7, le plus faible de tout l'échantillon, et 120 de portée effective. Un « oneshot » comme le décrit le build, c'est exactement ce que les chiffres racontent. Mais sa cadence de 30 RPM et son ergonomie de 39 rappellent le prix : chaque tir est une décision, et la manipulation est lente.</li>
              <li><strong>Le Vector .45 tient sa promesse de volume</strong> : 1100 RPM et 71 d'ergonomie. En revanche, 21 de précision et 25 de portée effective : le build « Infected Clear » ne vaut que face à des cibles de proximité et à l'armure légère. Contre un boss en armure T5, c'est un jouet.</li>
              <li><strong>Le FAL est le plus lourd et le moins maniable</strong> des cinq : 6,93 kg et 43 d'ergonomie, pour 630 RPM. Son atout reste la portée effective de 51 en 7.62×51mm — mais « Forbidden Tribunal » ne compense pas une manivelle lente que par la munition.</li>
              <li><strong>L'AK-12 est l'équilibre du lot</strong> : 730 RPM, 60 d'ergonomie, 55 de portée effective. Rien n'est spectaculaire, mais rien n'est critiquable — ce qui est précisément ce qu'on attend d'un build « laser budget » destiné à monter en Lockdown sans vider le stash.</li>
              <li><strong>L'A545 reste non vérifiable</strong> : le wiki ne l'a pas encore integrated. Tant qu'il n'y est pas, ses caractéristiques sur ce site reposent sur des retours de terrain et non sur une source documentée. Nous le signalons plutôt que de le présenter comme un fait.</li>
            </ul>
          </div>

          <div class="callout callout-warning">
            <h3 class="h4">Le coût annoncé ne vient d'aucune source</h3>
            <p>Les budgets cités dans chaque build (450 000–600 000 K pour l'A545, ~250 000 K pour l'AK-12) sont des <strong>estimations communautaires</strong> reconstruites à partir des prix observés en marché. Le wiki officiel ne publie pas les prix des armes ni des pièces. Ces montants sont indicatifs : ils varient selon la flambée du marché, la durée de la saison et l'offre. Utilisez-les comme un ordre de grandeur pour arbitrer, jamais comme un prix d'achat.</p>
          </div>
'''

# inserer apres la derniere section de build (FAL), avant le bloc de fin
m = re.search(r'<h2 id="build-fal">.*?</h2>(.*?)(?=<div class="callout callout-biohazard">)', s, re.S)
if not m:
    raise SystemExit('bloc FAL introuvable')
s = s[:m.end(1)] + BLOCK.strip() + '\n\n' + s[m.end(1):]

P.write_text(s, encoding='utf-8')
print('pages/armes-builds.html enrichi')
