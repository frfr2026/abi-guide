import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Objets')
CRUMB = ('Objets', 'items-munitions.html')

# ───────────────────────────────────────────── 1. MUNITIONS
ammo = """
          <figure class="page-figure">
            <img src="../img/items/ammo.jpg" alt="Boîte de munitions militaires et cartouches" loading="lazy">
            <figcaption>Saison 7 — le RNG de pénétration a disparu sur les armures T5/T6 : votre munition décide de vos duels.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Formule</span><span class="fact-value">Pierce Level = plancher(Pénétration ÷ 10)</span></div>
            <div class="fact"><span class="fact-label">Comparaison</span><span class="fact-value">Pierce Level vs Niveau d'armure</span></div>
            <div class="fact"><span class="fact-label">Plafonds</span><span class="fact-value">Normal T4 · Lockdown T5 · Forbidden T6</span></div>
            <div class="fact"><span class="fact-label">Échelle</span><span class="fact-value">Pierce Level 0 → 7</span></div>
          </div>

          <h2 id="comprendre">1. Comment fonctionne la pénétration</h2>
          <p>En ABI, la munition ne « perce » pas : elle est <strong>classée</strong>. Chaque munition affiche une valeur de <strong>Pénétration</strong> ; on en déduit son <strong>Pierce Level</strong> — le niveau de pénétration — par la formule communautaire issue du tableau officiel :</p>
          <div class="callout callout-success">
            <h4>La formule à retenir</h4>
            <p><code>Pierce Level = plancher(Pénétration ÷ 10)</code></p>
            <p>Une cartouche à 47 de pénétration est donc un Pierce Level 4. Le jeu compare ce niveau au <strong>Niveau d'armure</strong> de la plaque visée. En dessous, la balle rebondit (ou se déforme) sans percer.</p>
          </div>
          <p><strong>Le changement de la Saison 7</strong> : jusqu'à la S6, une munition sous le niveau de la plaque T5 ou T6 avait une petite chance de passer. Cette « loterie » a été <strong>supprimée</strong>. Résultat : le combat à haut niveau est devenu <strong>déterministe</strong>, et le TTK au torse plus long — il faut ramener la durabilité de la plaque sous un seuil pour percer de façon constante.</p>

          <h2 id="niveaux">2. L'échelle des Pierce Level</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Pierce Level</th><th>Pénétration</th><th>Contre</th><th>Exemples</th><th>Usage</th></tr></thead>
              <tbody>
                <tr><td><strong>0–1</strong></td><td>~0–19</td><td>Classe 1</td><td>9×19 de base, 7.62×25 Pst, .45 FMJ</td><td>Pistolet, jambes non protégées</td></tr>
                <tr><td><strong>2</strong></td><td>~20–29</td><td>Classe 2</td><td>5.45 PS, 9×19 Pst, 7.62×39 US</td><td>Début de raid, armure légère</td></tr>
                <tr><td><strong>3</strong></td><td>~30–39</td><td>Classe 3</td><td>5.56 M855, 7.62×39 T45M / PS</td><td>Confortable contre la classe 3</td></tr>
                <tr><td><strong>4</strong></td><td>~40–49</td><td>Classe 4</td><td><strong>5.56 M855A1</strong>, <strong>7.62×39 BP</strong>, 5.45 BP</td><td><strong>Le standard du rapport qualité/prix</strong></td></tr>
                <tr><td><strong>5</strong></td><td>~50–59</td><td>Classe 5</td><td>5.45 BS, 5.56 M995, 7.62×51 M62</td><td>Lockdown, anti-armure haute</td></tr>
                <tr><td><strong>6</strong></td><td>~60–71</td><td>Classe 6</td><td><strong>7.62×54 7N37</strong> (PL 7), .338 AP (PL 6)</td><td>Forbidden, uniquement</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Attention aux calibres qui se ressemblent</h4>
            <p>5.56×45, 5.45×39 et 5.8×42 sont <strong>trois munitions différentes</strong>. Idem pour les quatre 7.62 (×25, ×39, ×51, ×54), et pour 9×19 (pistolet) contre 9×39 (fusil). Rien ne se mélange : l'erreur de munition dans un sac se paie cher.</p>
          </div>

          <h2 id="modes">3. Quelle munition pour quel mode</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Plafond</th><th>Munitions recommandées</th><th>Budget</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal</strong></td><td>T4 et moins</td><td>M855A1 (5.56), BP (7.62×39), 7N31 (9×19)</td><td>Le sweet spot de la communauté</td></tr>
                <tr><td><strong>Lockdown</strong></td><td>T5 et moins</td><td>M855A1, M995, 5.45 BS, 7.62×51 M62</td><td>Une classe au-dessus du T4</td></tr>
                <tr><td><strong>Forbidden</strong></td><td>T6 autorisé</td><td><strong>.338 AP</strong> (PL 6), 7.62×54 SNB (PL 6), PPBS (PL 6), 7N37 (PL 7)</td><td>Cher, et à réserver aux raids Forbidden</td></tr>
                <tr><td><strong>Infected Zone</strong></td><td>Selon la zone</td><td>Idem Normal/Lockdown + munitions à chair contre les horde</td><td>Heavy sur Farm et Airport</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>Le piège de la valeur immobilisée</h4>
            <p>En Normal, votre stock de munitions T6 est de la valeur <strong>bloquée</strong> : vous ne pouvez pas l'emporter. Emportez des cartouches <strong>T4</strong> — le M855A1 et le BP sont cités par la communauté comme le meilleur compromis pénétration/prix.</p>
          </div>

          <h2 id="calibres">4. Les calibres et les armes qui les partagent</h2>
          <p>Avec <strong>81 armes</strong> et <strong>14 calibres</strong>, choisir un calibre, c'est choisir une famille d'armes. Les deux plus gros groupes :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Calibre</th><th>Armes</th><th>Nombre</th><th>Armeshed</th></tr></thead>
              <tbody>
                <tr><td><strong>5.56×45mm</strong></td><td>H416, M4A1, MCX, SCAR-L, AUG, MDR, AK-102, M16, FAMAS, SG550, Mini14, M96, F2000</td><td><strong>13</strong></td><td>Le plus polyvalent du jeu</td></tr>
                <tr><td><strong>9×19mm</strong></td><td>PP19, MP5, MPX, Vector 9, Uzi, PCC-9, MP9, MP40, G18C, G17, M9A3, T05</td><td><strong>12</strong></td><td>SMG et pistolet : imbattable en CQB et contre les zombies</td></tr>
                <tr><td><strong>7.62×51mm</strong></td><td>M24, Mk14, M110, M14, FAL, BM59, G3</td><td>7</td><td>Puissance longue distance</td></tr>
                <tr><td><strong>7.62×39mm</strong></td><td>AEK, CZ807, ACE31, <strong>AK-15SC</strong>, AKM, SKS, SA85M</td><td>7</td><td>La famille AK, dont la nouvelle AK-15SC</td></tr>
                <tr><td><strong>.45</strong></td><td>UMP45, Vector 45, MAC-10, MPF45, M3A1, M1911, M45A1</td><td>7</td><td>Alternative US en CQB</td></tr>
                <tr><td><strong>5.45×39mm</strong></td><td>AK12, <strong>A545</strong>, RPK-16, AK-74N, AN-94, AKS-74U</td><td>6</td><td>La famille de l'A545</td></tr>
                <tr><td><strong>5.8×42mm</strong></td><td>T192, T951, U191, T88, T03 (+ autres)</td><td>6</td><td>Le calibre du U191</td></tr>
                <tr><td><strong>7.62×25mm</strong></td><td>T85, T79, QC61, CZ52, T54</td><td>5</td><td>Pistolets-mitraillettes</td></tr>
                <tr><td><strong>5.7×28mm</strong></td><td>AR-57, Banshee, P90, F57</td><td>4</td><td>Le bloc P90 / AR-57</td></tr>
                <tr><td><strong>7.62×54mm</strong></td><td>SVDS, Mosin, SVTU</td><td>3</td><td>Les snipers russes, dont le 7N37 (PL 7)</td></tr>
                <tr><td><strong>9×39mm</strong></td><td>VSS, AMB-17</td><td>2</td><td>Subsonique : VSS et AMB-17 uniquement</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>La règle du stock intelligent</h4>
            <p>Ne stockez pas « une arme », stockez <strong>un calibre</strong>. 5.56×45 couvre 13 armes, 9×19 en couvre 12 : un stock de l'un ou l'autre s'adaptera presque toujours à l'arme que vous sortez. Le <strong>5.45×39</strong> est confirmé par les notes S7 pour l'A545 ; l'AK-15SC est rattachée au <strong>7.62×39</strong> par les notes officielles, mais certains guides communautaires la rattachent au 7.62×51 : les quatre 7.62 ne se mélangent pas, vérifiez la fiche de l'arme avant de faire le plein.</p>
          </div>

          <h2 id="speciales">5. Les munitions spéciales qui méritent un slot</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Munition</th><th>Calibre</th><th>Spécialité</th><th>Usage</th></tr></thead>
              <tbody>
                <tr><td><strong>Dum-Dum</strong></td><td>9×19</td><td>Dégâts à la chair, Pierce Level très bas</td><td>Meta jambes et <strong>horde de zombies</strong> : ça scie des rangs entiers</td></tr>
                <tr><td><strong>AP6.3</strong></td><td>9×19</td><td>Pierce Level 3 en 9×19</td><td>La solution low-cost en CQB avec le MPX</td></tr>
                <tr><td><strong>M855A1</strong></td><td>5.56×45</td><td>Pierce Level 4, 47 dégâts chair</td><td>Le standard du budget sérieux</td></tr>
                <tr><td><strong>BP</strong></td><td>7.62×39</td><td>Pierce Level 4, 55 dégâts chair, 23 dégâts d'armure</td><td>Idem, pour les calibres AK ; le BP 5.45 fait 45 dégâts et 17 dégâts d'armure</td></tr>
                <tr><td><strong>5.7×28 SS190</strong></td><td>5.7×28</td><td>Pierce Level 4, 47 dégâts chair, 18 dégâts d'armure</td><td>Le bloc P90 / AR-57 : laMunition T4 de référence du calibre</td></tr>
                <tr><td><strong>7N37</strong></td><td>7.62×54</td><td><strong>Pierce Level 7</strong> — le sommet du tableau</td><td>Le seul qui perce la classe 6 en_regular</td></tr>
                <tr><td><strong>.338 AP</strong></td><td>.338</td><td>Pierce Level 6 (pénétration 64), 90 dégâts chair, 55 dégâts d'armure</td><td>Réservé au Forbidden (interdit en Normal/Lockdown)</td></tr>
                <tr><td><strong>PPBS</strong></td><td>5.45×39</td><td>T6, pénétration 62</td><td>La pointe de lance 5.45 pour l'A545 et l'AK-12</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="rouges">6. Les munitions rouges : craft, pas achat</h2>
          <ul>
            <li>Les munitions <strong>T6 et T7</strong> (les « red ammo ») se <strong>craftent</strong> : <strong>niveau 3 de Workbench pour la T6, niveau 4 pour la T7</strong>.</li>
            <li>Depuis la Saison 6, le <strong>Marché et les Contacts les ont délistés</strong> : on ne les achète plus, on les fabrique.</li>
            <li>Depuis la S6, les munitions rouges <strong>ne peuvent pas être placées en case sécurisée</strong> : magazines ou sac, jamais la case.</li>
            <li>Les recettes T6 apparaissent une fois le Workbench niveau 3 atteint ; la T7 exige le niveau 4.</li>
          </ul>
          <div class="callout callout-warning">
            <h4>Ne transportez que ce dont vous avez besoin</h4>
            <p>Emportez un <strong>petit compte</strong> de red ammo, uniquement quand l'extraction est probable (Farm / Northridge Hostile Sector). Les munitions rouges se transportent mal, ne rentrent pas dans les cases sécurisées, et une mort en raid les détruit.</p>
          </div>

          <h2 id="lire">7. Comment lire le tableau dans le jeu</h2>
          <ol>
            <li>Ouvrez la fiche d'une munition et relevez sa <strong>valeur de Pénétration</strong>.</li>
            <li>Divisez par 10 et arrondissez à l'entier inférieur : vous avez son <strong>Pierce Level</strong>.</li>
            <li>Comparez avec le <strong>Niveau d'armure</strong> de la cible (classe 1 à 6).</li>
            <li>Ajustez le mode : Normal → plafond T4, Lockdown → plafond T5, Forbidden → T6.</li>
            <li>Vérifiez dans le même onglet le <strong>type de munition disponible</strong> pour votre arme (chargeur, boîte, vrac).</li>
          </ol>
          <div class="callout callout-danger">
            <h4>Avertissement sur les tableaux non officiels</h4>
            <p>Morefun ne publie pas de tableau de pénétration round-by-round. Les valeurs exactes de chaque cartouche sont donc des <strong>données communautaires</strong>, utiles comme point de départ mais à confirmer sur la fiche de l'objet dans votre client. Vérifiez toujours avant une sortie coûteuse.</p>
          </div>

          <h2 id="reco">8. Récapitulatif — le kit munitions parfait</h2>
          <ul>
            <li><strong>Normal :</strong> M855A1 ou BP, 3 chargeurs de 30 + 2 chargeurs de secours. Comptez ~150 cartouches.</li>
            <li><strong>Lockdown :</strong> idem en T5 (M995 / 5.45 BS / 7.62×51 M62) si votre cible est équipée.</li>
            <li><strong>Forbidden :</strong> 7N37 ou .338 AP, en petit volume, jamais en case.</li>
            <li><strong>Zombies (Infected Zone / Endless) :</strong> dum-dum 9×19 + shotgun : le meta Literal des horde, ce n'est pas la pénétration qui compte mais les dégâts de groupe.</li>
            <li><strong>Toujours</strong> un lot de munitions de chaque calibre du squad : un mort avec vos munitions, c'est un squad privé de munitions.</li>
          </ul>
          <p>Pour le détail de la Fabrication de ces munitions, voir <a href="items-craft-workbench.html">le guide Workbench</a>. Pour l'armure qui va avec, voir <a href="equipement-armures.html">le guide des armures</a>.</p>
"""

page('items-munitions.html',
     "Munitions & Pénétration",
     "Guide des munitions ABI Saison 7 : Pierce Level, Armor Level, tableau par calibre (5.56/9mm/7.62/5.45), plafonds par mode, munitions rouges T6-T7 et munitions anti-zombie.",
     "../img/items/ammo.jpg",
     "Objets — Munitions", "Munitions & Pénétration",
     "Pierce Level, Armor Level, T4/T5/T6 : la munition décide de vos duels, plus l'arme.",
     ammo,
     [("comprendre", "1. Fonctionnement"), ("niveaux", "2. Échelle des niveaux"), ("modes", "3. Par mode"),
      ("calibres", "4. Calibres & armes"), ("speciales", "5. Munitions spéciales"), ("rouges", "6. Munitions rouges"),
      ("lire", "7. Lire le tableau"), ("reco", "8. Kit parfait")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ───────────────────────────────────────────── 2. MEDICAL
medical = """
          <figure class="page-figure">
            <img src="../img/items/medical.jpg" alt="Trousse médicale de terrain ouverte" loading="lazy">
            <figcaption>Le médical en ABI est un système à quatre états. Mal le comprendre, c'est mourir à 5 mètres d'une extraction.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Ordre</span><span class="fact-value">Douleur → Hémorragie → Membre cassé → PV</span></div>
            <div class="fact"><span class="fact-label">Touche</span><span class="fact-value">V — roue de soins (appui long = auto)</span></div>
            <div class="fact"><span class="fact-label">Règle</span><span class="fact-value">Max 20 % de votre stash dans un kit</span></div>
            <div class="fact"><span class="fact-label">Meilleur ratio</span><span class="fact-value">TMK Military Surgical Kit</span></div>
          </div>

          <h2 id="etats">1. Les 4 états de blessure</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>État</th><th>Symptôme</th><th>Ce qui le guérit</th><th>Ce qui ne marche PAS</th></tr></thead>
              <tbody>
                <tr><td><strong>Douleur</strong></td><td>Visée et course dégradées</td><td>Antalgiques (painkillers)</td><td>—</td></tr>
                <tr><td><strong>Hémorragie</strong></td><td>Perte de PV continue, indicateur « wounded »</td><td><strong>Pansements</strong> — et les medkits haut de gamme traitent aussi le saignement</td><td>Un simple medkit ne referme pas la plaie</td></tr>
                <tr><td><strong>Membre cassé (noir)</strong></td><td>PV du membre à 0,Propagation aux vitaux</td><td><strong>Kit chirurgical</strong></td><td>Bandages et medkits ne réparent pas un membre cassé</td></tr>
                <tr><td><strong>Blessure légère</strong></td><td>PV du membre diminués, pas de saignement</td><td><strong>Medkit</strong></td><td>—</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>La cascade qui tue</h4>
            <p>Un membre qui tombe à 0 PV devient <strong>noir</strong>. Tant qu'il est noir, les dégâts se propagent aux <strong>vitals</strong> et tuent. Et un kit chirurgical ne remet le membre qu'à <strong>1 PV</strong> : il faut <strong>ensuite</strong> un medkit pour le restaurer. D'où l'ordre obligatoire.</p>
          </div>

          <h2 id="ordre">2. L'ordre de soin qui sauve des raids</h2>
          <ol>
            <li><strong>Antalgique d'abord</strong> — il vous permet de <em>fuir</em> sans que la douleur gêne. Idéalement avant le combat, pour vous concentrer sur le gunfight.</li>
            <li><strong>Pansement</strong> — on stoppe le saignement. Un membre qui saigne en continu peut re-casser ce que vous venez de réparer.</li>
            <li><strong>Kit chirurgical</strong> — on répare le membre cassé.</li>
            <li><strong>Medkit</strong> — on restaure les PV.</li>
            <li><strong>Boisson</strong> — on répare l'hydratation.</li>
          </ol>
          <p>La touche <strong>V</strong> ouvre la roue de soins ; un appui long déclenche l'usage automatique des objets que vous avez. Pratique, mais <strong>dangereux</strong> : l'auto-usage peut utiliser un antalgique alors que vous vouliez un pansement. Utilisez la roue manuellement en situation tendue.</p>

          <h2 id="trousses">3. Les trousses de secours</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Trousse</th><th>PV rendus</th><th>Temps</th><th>Traite l'hémorragie</th><th>Hydratation</th><th>Taille</th></tr></thead>
              <tbody>
                <tr><td>Simple First Aid Pack</td><td>80</td><td>2 s</td><td>Non</td><td>−8</td><td>1×1</td></tr>
                <tr><td>Standard First Aid Kit</td><td>120</td><td>2,1 s</td><td>Non</td><td>−6</td><td>1×1</td></tr>
                <tr><td>926 Rapid First Aid Kit</td><td>220–270</td><td>3,5 s</td><td>Non</td><td>−22</td><td>2×1</td></tr>
                <tr><td>E3 Military Medkit</td><td>300</td><td>4,1 s</td><td>Non</td><td>−15</td><td>2×1</td></tr>
                <tr><td><strong>100D Battlefield Medkit</strong></td><td>400</td><td>4,1 s</td><td><strong>Oui</strong></td><td>0</td><td>2×1</td></tr>
                <tr><td>TMK Field Medkit</td><td>960</td><td>4,1 s</td><td>Oui</td><td>−48</td><td>2×2</td></tr>
                <tr><td><strong>STO First Aid Set</strong></td><td>1200</td><td>3,3 s</td><td>Oui</td><td>0</td><td>2×2</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Le classement de la communauté</h4>
            <p><strong>100D Battlefield Medkit</strong> en tête : aucune perte d'hydratation, 2 slots seulement, ~35 PV/s. <strong>STO First Aid Set</strong> juste derrière (4 slots, mais 4× la couverture et 10 PV/s de plus, pour le même prix). Budget serré : <strong>E3 Military Kit</strong>. Pour les longs raids : le <strong>STO</strong>.</p>
          </div>

          <h2 id="chirurgie">4. Les kits chirurgicaux</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Kit</th><th>Usages</th><th>Temps</th><th>Pénalité PV max</th><th>Taille</th></tr></thead>
              <tbody>
                <tr><td>Simple Surgical Pack</td><td>1</td><td>18 s</td><td><strong>−60 %</strong></td><td>1×1</td></tr>
                <tr><td>Standard Military Surgical Kit</td><td>4</td><td>13 s</td><td>−40 %</td><td>2×1</td></tr>
                <tr><td><strong>TMK Military Surgical Kit</strong></td><td>8</td><td>15 s</td><td>−20 %</td><td>3×1</td></tr>
                <tr><td><strong>STO Battlefield Surgical Set</strong></td><td>12</td><td>16 s</td><td><strong>Aucune pénalité</strong></td><td>2×2</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Le TMK, meilleur rapport de la communauté</h4>
            <p>8 usages, seulement <strong>−20 %</strong> de PV maximum par membre et 3 slots. Le Standard Military Surgical Kit très répandu offre les mêmes 8 usages mais en 4 slots et avec −40 % de PV mangés — pour 3 000 Koen de plus seulement. Le STO reste le meilleur objet du jeu, mais il coûte <strong>4 slots</strong>.</p>
          </div>

          <h2 id="antalgiques">5. Les antalgiques</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Antalgique</th><th>Usages</th><th>Temps d'activation</th><th>Durée d'insensibilisation</th><th>Hydratation</th></tr></thead>
              <tbody>
                <tr><td>Fast-Acting Painkiller</td><td>3</td><td>3,5 s</td><td>180 s</td><td>−10</td></tr>
                <tr><td>AP Painkiller</td><td>6</td><td>5,5 s</td><td>210 s</td><td>−10</td></tr>
                <tr><td><strong>EX Painkiller</strong></td><td>8</td><td>5,5 s</td><td><strong>300 s</strong></td><td>−10</td></tr>
                <tr><td>Anti-Inflam Painkiller</td><td>3</td><td>3,5 s</td><td>60 s</td><td>−6</td></tr>
                <tr><td>Liquid Painkiller</td><td>1</td><td>6 s</td><td>270 s</td><td>0</td></tr>
                <tr><td>Energy Drink</td><td>1</td><td>6 s</td><td>240 s</td><td>0</td></tr>
              </tbody>
            </table>
          </div>
          <p>L'<strong>EX Painkiller</strong> est le plus durable (5 minutes) et supporte 8 usages : le meilleur de la liste. L'<strong>Anti-Inflam</strong> est souvent déconseillé — 60 secondes ne suffisent pas à se désengager. Le <strong>Liquid Painkiller</strong> et l'<strong>Energy Drink</strong> sont monoprix, sans coût d'hydratation, parfaits en economy.</p>

          <h2 id="pansements">6. Les pansements</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Pansement</th><th>Usages</th><th>Temps</th><th>Poids</th></tr></thead>
              <tbody>
                <tr><td>Quick Bandage</td><td>1</td><td>6,8 s</td><td>0,04 kg</td></tr>
                <tr><td>Field Bandage</td><td>2</td><td>6,8 s</td><td>0,06 kg</td></tr>
                <tr><td><strong>OPM Bandage</strong></td><td><strong>4</strong></td><td>6,8 s</td><td>0,08 kg</td></tr>
              </tbody>
            </table>
          </div>
          <p>Les pansements sont peu chers : l'OPM en 4 usages est le standard. À noter : certains medkits haut de gamme (100D, TMK, STO) <strong>traient aussi l'hémorragie</strong> — c'est ce qui les rend supérieurs à un duo bandage + petit medkit.</p>

          <h2 id="stimulants">7. Les stimulants</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Stimulant</th><th>Effet</th><th>Durée</th></tr></thead>
              <tbody>
                <tr><td>Regen Booster</td><td>Restauration continue des PV sur tous les membres</td><td>300 s</td></tr>
                <tr><td>Regen Injection</td><td>Idem + capacité de port augmentée</td><td>180 s</td></tr>
                <tr><td>Endurance Booster</td><td>Endurance max augmentée, coût réduit, régénération accélérée</td><td>300 s</td></tr>
                <tr><td>Strength Booster</td><td>Capacité de port augmentée</td><td>300 s</td></tr>
                <tr><td>Sensory Enhancer F</td><td>Amélioration de l'audition</td><td>180 s</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Les stimulants ont un coût</h4>
            <p>Tous les stimulants coûtent de l'<strong>énergie</strong> (−3 à −5) et de l'hydratation (−3 à −5). La <strong>Regen</strong> est un luxe de raid long : entre deux combats, un medkit instantané est presque toujours plus rentable. Portez-la pour les raids à sac lourd, où l'endurance est votre ennemie.</p>
          </div>

          <h2 id="s7">8. Le médical en Saison 7</h2>
          <ul>
            <li><strong>Traitement Y40 (Experimental Ultra-Strength Treatment)</strong> — un stimulant experimentally classé, craftable, qui donne une régénération accélérée et peut même réparer des membres cassés. Reddit le décrit comme « de la Wolverine » : il guérit plus vite et répare les membres. <strong>Durée courte mais très fort.</strong></li>
            <li><strong>Battlefield First Aid Kit Set F</strong> — soin d'un coéquipier <strong>downed</strong> : indispensable en squad, inutile en solo.</li>
            <li><strong>G-96 Nebulizer</strong> — protection pulmonaire et traitement des lésions pulmonaires pendant 30 s. Sans usage réel tant que les grenades à gaz ne sont pas dans le meta.</li>
            <li><strong>Réactifs expérimentaux (zone infectée)</strong> — Pathfinder (+PV de torse), Messenger (+vitesse), résistance aux blessures critiques : ils augmentent aussi les dégâts subis des mutants et votre probabilité d'être détecté.</li>
            <li>La <strong>fumigène de soin</strong> de la S7 restaure progressivement la santé dans une zone : l'outil de soutien du squad en zone contaminée.</li>
          </ul>
          <div class="callout callout-success">
            <h4>Le kit médical rentable — l'avis Reddit</h4>
            <p>« 100D Battlefield Medkit (400 PV, 2 slots, traite le saignement) + un kit chirurgical. » En budget : le kit chirurgical noir 4 usages. Et une règle d'or de la communauté : <strong>ne jamais dépasser 20 % de votre stash dans un seul kit</strong>. Avec 500 000 Koen en banque, votre kit total (arme + armure + munitions + médical) ne devrait pas dépasser 100 000 Koen. Mourir avec un kit surdimensionné casse votre dynamique économique.</p>
          </div>

          <h2 id="checklist">9. Check-list médical avant extraction</h2>
          <ul>
            <li>Au moins <strong>un kit chirurgical</strong> — sans lui, un membre cassé est une mort retardée.</li>
            <li><strong>2 à 4 pansements</strong> — l'hémorragie tue plus vite que la blessure.</li>
            <li><strong>1 antalgique EX</strong> — pour fuir.</li>
            <li><strong>1 medkit 100D</strong> — pour tenir la différence après le soin.</li>
            <li>Et de l'espace : un sac Medical Case vaut de l'or dans une zone à horde.</li>
          </ul>
          <p>Pour le budget global, voir <a href="items-koen-economy.html">le guide Koen &amp; économie</a>. Pour les zombies, l'<a href="saison7-zombie-endless.html">antalgique est vital</a> : en Endless, rester debout 3 secondes de plus vaut un tank.</p>
"""

page('items-medical.html',
     "Médical & Soins",
     "Guide du médical ABI Saison 7 : hémorragie, membre cassé, trousses de secours, kits chirurgicaux, antalgiques, stimulants et budget médical en squad.",
     "../img/items/medical.jpg",
     "Objets — Médical", "Médical & Soins",
     "Hémorragie, membre cassé, antalgiques : l'ordre des soins vaut plus que n'importe quel kit.",
     medical,
     [("etats", "1. États de blessure"), ("ordre", "2. Ordre de soin"), ("trousses", "3. Trousses de secours"),
      ("chirurgie", "4. Kits chirurgicaux"), ("antalgiques", "5. Antalgiques"), ("pansements", "6. Pansements"),
      ("stimulants", "7. Stimulants"), ("s7", "8. Médical S7"), ("checklist", "9. Check-list")],
     extra_js=False, nav=NAV, crumb=CRUMB)

print("OK S9 batch A")
