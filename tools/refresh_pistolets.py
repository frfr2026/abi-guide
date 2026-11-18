#!/usr/bin/env python3
"""Enrichit pages/armes-pistolets.html avec les statistiques officielles.

Source : wiki officiel ABI (Template:WeaponData, fiches M1911 / M45A1 / G17 /
G18C / F57 / Desert Eagle / T05 et pages de munitions). Chaque valeur est
reprise telle quelle, avec mention explicite de la source. Les roles et
strategies restent attribues a la communaute.
"""
import pathlib, re

P = pathlib.Path('pages/armes-pistolets.html')
s = P.read_text(encoding='utf-8')

if 'data-table-officiel' in s:
    print('deja enrichi')
    raise SystemExit(0)

# ── Bloc 1 : tableau des statistiques officielles ────────────────────────
OFFICIAL = '''
          <h2 id="stats-officielles">2. Les pistolets en chiffres (statistiques officielles)</h2>
          <p>Les valeurs ci-dessous sont reprises telles quelles du <strong>wiki officiel d'Arena Breakout Infinite</strong> (fiches armes et modèle de données <code>WeaponData</code>). Ce sont des caractéristiques de l'arme, pas des avis : elles décrivent la matière première, pas la qualité d'un build. L'échelle est la même pour toutes les armes du jeu, donc les valeurs sont comparables entre elles, mais elle ne dit rien du prix, de la disponibilité ni de la rentabilité en raid.</p>
          <div class="table-wrap">
            <table class="data-table data-table-officiel">
              <thead>
                <tr><th>Pistolet</th><th>Calibre</th><th>Mode de tir</th><th>Puissance</th><th>Recul vertical</th><th>Recul horizontal</th><th>Ergonomie</th><th>Précision</th><th>Portée efficace</th><th>Cadence (RPM)</th><th>Poids</th></tr>
              </thead>
              <tbody>
                <tr><td><strong>M45A1</strong></td><td>.45</td><td>Semi</td><td>Mid-High</td><td>58</td><td>28</td><td>84</td><td>15</td><td>12</td><td>250</td><td>2,25</td></tr>
                <tr><td><strong>F57</strong></td><td>5.7×28mm</td><td>Semi</td><td>Mid-High</td><td>60</td><td>25</td><td>83</td><td>22</td><td>20</td><td>400</td><td>2,49</td></tr>
                <tr><td><strong>M1911</strong></td><td>.45</td><td>Semi</td><td>Mid-High</td><td>54</td><td>26</td><td>77</td><td>14</td><td>16</td><td>350</td><td>2,50</td></tr>
                <tr><td><strong>G18C</strong></td><td>9×19mm</td><td>Semi, Full</td><td>Low</td><td>57</td><td>24</td><td>73</td><td>16</td><td>12</td><td>1000</td><td>1,31</td></tr>
                <tr><td><strong>G17</strong></td><td>9×19mm</td><td>Semi</td><td>Low</td><td>56</td><td>23</td><td>73</td><td>15</td><td>14</td><td>400</td><td>1,16</td></tr>
                <tr><td><strong>T05</strong></td><td>9×19mm</td><td>Semi</td><td>Low</td><td>41</td><td>22</td><td>77</td><td>11</td><td>14</td><td>300</td><td>1,62</td></tr>
                <tr><td><strong>Desert Eagle</strong></td><td>.44</td><td>Semi</td><td>Medium</td><td>40</td><td>24</td><td>65</td><td>30</td><td>31</td><td>300</td><td>1,81</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Lecture : <em>recul</em> se compte vers le haut (valeur haute = plus de recul), <em>précision</em> et <em>portée efficace</em> sont exprimées sur l'échelle interne du jeu, <em>cadence</em> en tours par minute. Source : wiki officiel ABI, modèle de données <code>WeaponData</code>. Ces chiffres sont ceux du wiki et peuvent evolved à chaque patch : l'armurerie en jeu reste la reference.</p>

          <div class="callout callout-info">
            <h3 class="h4">Ce que le tableau dit — et ce qu'il ne dit pas</h3>
            <ul>
              <li><strong>Il dit</strong> que le M45A1 offre la meilleure ergonomie de la catégorie (84) et le Desert Eagle la meilleure précision (30) et la meilleure portée effective (31) — mais aussi le moins bon recul vertical (40).</li>
              <li><strong>Il ne dit pas</strong> le prix en GPA, la disponibilité en raid, le poids de l'ensemble de l'armure, ni la facilité à trouver les munitions correspondantes. Un pistolet à 8 000 GPA et introuvable ne vaut pas mieux qu'un G17 à 2 000 GPA présent dans chaque raid.</li>
              <li><strong>Il ne dit pas</strong> qu'une arme est « bonne » : l'arme la mieux notée du tableau est celle qui correspond à votre budget et à votre niveau de munitions.</li>
            </ul>
          </div>

          <h3 class="h4">Trois profils qui se dégagent des chiffres</h3>
          <ul>
            <li><strong>Le poids lourd de poche</strong> — M45A1 ou F57 : ergonomie de pointe (84 et 83), puissance Mid-High et recul vertical contenu (58 et 60). Ce sont les pistolets les plus agréables à manier sur un long raid, quand on a le budget pour les munitions de haut niveau.</li>
            <li><strong>Le polyvalent à prix bas</strong> — G17 ou T05 : 9×19mm, l'une des munitions les plus répandues du jeu. Le G17 est le plus léger de la liste (1,16) et le T05 a le plus faible recul vertical (41). Comptez sur une précision faible (15 et 11) : c'est acceptable à courte distance, pas au frontal.</li>
            <li><strong>La enclume</strong> — Desert Eagle : précision 30 et portée effective 31, ce que rien d'autre n'offre dans la catégorie. En contrepartie, l'ergonomie (65) et le recul vertical (40, le plus bas de la liste : le moins contrôleable) en font une arme de duel, pas une arme de poche.</li>
            <li><strong>L'exception de rafale</strong> — G18C : le seul de la liste à accepter le tir automatique (Semi, Full) avec 1000 RPM. C'est l'arme de la fuite à l'arrachée quand la Haggler de zone vous tombe dessus — et un piège, car sa puissance est classée Low.</li>
          </ul>
'''

# insertion apres la section modeles (avant "3. Conseils de jeu")
anchor = '          <h2 id="conseils">3. Conseils de jeu</h2>'
assert anchor in s
s = s.replace(anchor, OFFICIAL.strip() + '\n\n' + anchor, 1)

# renumerotation : conseils devient 4
s = s.replace('<h2 id="conseils">3. Conseils de jeu</h2>', '<h2 id="conseils">4. Conseils de jeu</h2>', 1)

# ── Bloc 2 : munitions officielles ───────────────────────────────────────
AMMO = '''
          <h2 id="munitions">3. Les munitions par calibre (données officielles)</h2>
          <p>Le choix du pistolet se fait autant sur la munition que sur l'arme. Le wiki officiel tient à jour, pour chaque arme, la liste complète des munitions compatibles et leur <strong>niveau</strong>. Un niveau élevé signifie une munition plus Performante, plus rare, et plus chère — le verrou principal de l'escalade d'arme.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Pistolet</th><th>Calibre</th><th>Munitions disponibles (niveau)</th></tr></thead>
              <tbody>
                <tr><td>M45A1</td><td>.45</td><td><strong>.45 HS</strong> (1) · <strong>.45 FMJ</strong> (1) · <strong>.45 AP</strong> (3)</td></tr>
                <tr><td>M1911</td><td>.45</td><td><strong>.45 HS</strong> (1) · <strong>.45 FMJ</strong> (1) · <strong>.45 AP</strong> (3)</td></tr>
                <tr><td>G18C</td><td>9×19mm</td><td>9x19mm DumDum (0) · <strong>9x19mm PSO</strong> (1) · <strong>9x19mm Pst</strong> (2) · <strong>9x19mm AP6.3</strong> (3) · <strong>9x19mm 7N31</strong> (4)</td></tr>
                <tr><td>G17 / T05</td><td>9×19mm</td><td>Mêmes 9×19mm que le G18C, de DumDum (0) à 7N31 (4)</td></tr>
                <tr><td>Desert Eagle</td><td>.44</td><td><strong>.44 LFNP</strong> (2) · <strong>.44 SJHP</strong> (3) · <strong>.44 JSP</strong> (4)</td></tr>
                <tr><td>F57</td><td>5.7×28mm</td><td>5.7x28mm R37.F (0) · R37.X (1) · <strong>SS197SR</strong> (2) · <strong>L191</strong> (3) · <strong>SS190</strong> (4) · <strong>SS198</strong> (5)</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : wiki officiel ABI, sections « Ammo » des fiches armes. L'échelle de niveau va de 0 à 5 : le niveau 0 est la munition de base, disponible partout.</p>

          <div class="callout callout-warning">
            <h3 class="h4">La règle des 9×19mm</h3>
            <p>Cinq niveaux de munition pour le 9×19mm, contre trois pour le .45 et deux points d'entrée seulement pour le .44 (à partir du niveau 2). Concrètement : <strong>le 9×19mm est le calibre le plus flexible du jeu pour un pistolet</strong>. Vous pouvez monter un G17 avec une 7N31 de niveau 4, ou redescendre à une DumDum de niveau 0 selon ce que vous trouvez. Le .44 du Desert Eagle vous oblige à passer au niveau 2 minimum, ce qui verrouille l'accès à une munition de base — un vrai handicap pour un petit arme censé être accessible à tous les stashes.</p>
          </div>

          <h3 class="h4">Les attachements dédiés aux pistolets</h3>
          <p>Le wiki officiel recense les pièces compatibles arme par arme. Pour le M1911, quatre pièces lui sont propres :</p>
          <ul>
            <li><strong>Dedicated M1911 Grip</strong> — la poignée dédiée.</li>
            <li><strong>M1911 Standard Barrel</strong> et <strong>M1911 Threaded Barrel</strong> — canon standard ou canon fileté (support de modérateur).</li>
            <li><strong>M1911 Standard Upper Receiver</strong> — boîtier supérieur.</li>
          </ul>
          <p>Pour le G17, le wiki recense également <strong>G17 Carbon Fiber Receiver</strong>, <strong>G17 Desert Carbon Fiber Receiver</strong>, <strong>G17 Metal Machined Receiver</strong> et <strong>G17 Threaded Barrel</strong>. Ce sont les récepteurs en fibre de carbone et en métal usiné, plus un canon fileté pour le modérateur.</p>
          <p class="small text-muted">Source : wiki officiel ABI, section « Weapon Mods ». La compatibilité est un fait du jeu ; l'intérêt d'une pièce donnée reste, lui, une question de build.</p>
'''

# inserer munitions avant la section conseils (qui est renumerotee 4)
s = s.replace('          <h2 id="conseils">4. Conseils de jeu</h2>', AMMO.strip() + '\n\n          <h2 id="conseils">4. Conseils de jeu</h2>', 1)

# ── Bloc 3 : mettre a jour le sommaire ───────────────────────────────────
old_toc = '''          <h4>Sommaire</h4>
<a href="#role" id="lnk-armes-pistolets-096">1. Rôle réel</a>
<a href="#modeles" id="lnk-armes-pistolets-097">2. Modèles</a>
<a href="#conseils" id="lnk-armes-pistolets-098">3. Conseils</a>'''
new_toc = '''          <h4>Sommaire</h4>
<a href="#role" id="lnk-armes-pistolets-096">1. Rôle réel</a>
<a href="#modeles" id="lnk-armes-pistolets-097">2. Modèles</a>
<a href="#stats-officielles" id="lnk-armes-pistolets-096b">3. Statistiques officielles</a>
<a href="#munitions" id="lnk-armes-pistolets-097b">4. Munitions par calibre</a>
<a href="#conseils" id="lnk-armes-pistolets-098">5. Conseils</a>'''
assert old_toc in s
s = s.replace(old_toc, new_toc, 1)

P.write_text(s, encoding='utf-8')
print('pages/armes-pistolets.html enrichi')
