import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Méta')
CRUMB = ('Meta', 'meta-tier-list-globale.html')

# ───────────────────────────────────────────── 1. TIER LIST GLOBALE
tier = """
          <figure class="page-figure">
            <img src="../img/meta/meta-tier-list.jpg" alt="Rack d'armes alignées par tier" loading="lazy">
            <figcaption>Tier list Saison 7 : cinq critères, pas un classement de Sinatra. Le tier d'une arme se décide par son coût, son tier de munitions et sa place sur la carte.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Critères</span><span class="fact-value">RPM · portée · tier de munitions · ergonomie · coût</span></div>
            <div class="fact"><span class="fact-label">Meta S7</span><span class="fact-value">A545, H416, U191, AK-12, M24, P90</span></div>
            <div class="fact"><span class="fact-label">Meta budget</span><span class="fact-value">AK-12 (~240 K) · SKS (~80 K) · MPX (~160 K)</span></div>
            <div class="fact"><span class="fact-label">Zone infectée</span><span class="fact-value">Shotgun + SMG (S12K, MP5)</span></div>
          </div>

          <h2 id="methode">1. Comment on construit un tier list honnête</h2>
          <p>Une tier list d'ABI se juge sur <strong>cinq axes</strong>, jamais sur le seul « feeling » :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Critère</th><th>Poids</th><th>Pourquoi</th></tr></thead>
              <tbody>
                <tr><td><strong>Tier de munitions</strong></td><td>Décisif</td><td>Avec le RNG T5/T6 supprimé, une arme designed autour d'un calibre sans munitions disponibles est un jouet coûteux</td></tr>
                <tr><td><strong>Coût réel du kit</strong></td><td>Décisif</td><td>Une arme à 500 K n'est pas « meilleure » : elle est <em>inaccessible</em> à la majorité</td></tr>
                <tr><td><strong>Portée effective</strong></td><td>Fort</td><td>Augmentée en S7 : la portée distingue une arme de raid d'une arme de parc à tir</td></tr>
                <tr><td><strong>RPM / contrôle du recul</strong></td><td>Fort</td><td>Le TTK est allongé en S7 : la cadence et la maîtrise du spray font la différence</td></tr>
                <tr><td><strong>Ergonomie</strong></td><td>Moyen</td><td>Détermine la vitesse de manipulation, la prise en main et le bruit</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Le biais à éviter</h4>
            <p>Le plus gros biais du joueur est le <strong>gear fear</strong> : croire qu'une arme rare est meilleure. La citation de la communauté est la plus juste du jeu : <em>« La meilleure arme dans n'importe quelle situation, c'est celle avec laquelle vous touchez vos tirs. Ignorez le meta jusqu'à pousser pour le Forbidden, et même là, utilisez ce qui marche pour vous. »</em> Une AK-74N bien maîtrisée bat un A545 mal maîtrisée.</p>
          </div>

          <h2 id="global">2. Le tier list global S7</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Tier</th><th>Armes</th><th>Rôle</th></tr></thead>
              <tbody>
                <tr><td><strong>S</strong></td><td>A545, H416, U191, AK-12, M24, P90</td><td>Fusils premium par défaut, « laser » AR à budget, menace de verrou, shredder CQB</td></tr>
                <tr><td><strong>A</strong></td><td>AK-15SC, PCC9 + Full-Auto Kit, AN-94 / A94, FAL + Recoil Kit, M110 + Dual-Stage Trigger, AR-57, AEK, F2000, Mk14, SJ16, RPK-16, Vector .45</td><td>Spécialistes de carte et de rôle, plateformes réveillées par les season kits</td></tr>
                <tr><td><strong>B</strong></td><td>MPX + Vulcan Barrel, MCX, M4A1, ACE31, AUG, VSS, USAS-12, T191 / T192</td><td>Jouables avec la bonne munition et la bonne carte</td></tr>
                <tr><td><strong>C</strong></td><td>MDR, FAMAS, Mini14, S12K, Banshee, Mosin, SKS, PCC9 (stock)</td><td>Remplisseurs à budget ou presses à niche</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Le résumé en une phrase</h4>
            <p>Pour la plupart des joueurs : <strong>H416 ou A545</strong>. Pour l'efficacité en Koen : <strong>AK-12</strong>. Pour le CQB pur : <strong>P90</strong> ou <strong>PCC9 + Full-Auto Kit</strong>.</p>
          </div>

          <h2 id="par-categorie">3. Tier list par catégorie</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Catégorie</th><th>S</th><th>A</th><th>B / C</th></tr></thead>
              <tbody>
                <tr><td><strong>Fusils d'assaut</strong></td><td>A545, H416, U191, AK-12</td><td>AK-15SC, AN-94, AEK, F2000, FAL + Recoil Kit</td><td>MCX, M4A1, ACE31, AUG, MDR, FAMAS, SKS</td></tr>
                <tr><td><strong>DMR</strong></td><td>—</td><td>M110 + Dual-Stage Trigger, Mk14, SJ16</td><td>VSS, MDR</td></tr>
                <tr><td><strong>Snipers</strong></td><td>M24</td><td>SJ16</td><td>Mosin, Mini14</td></tr>
                <tr><td><strong>SMG</strong></td><td>P90</td><td>Vector .45, AR-57, MPX + Vulcan</td><td>MPX (stock), MP5, Banshee, T191/T192</td></tr>
                <tr><td><strong>Shotguns</strong></td><td>—</td><td>—</td><td>USAS-12, S12K (T4 en 12ga) : le meta des zones infectées</td></tr>
                <tr><td><strong>LMG</strong></td><td>—</td><td>RPK-16, AEK</td><td>MG3 (squad uniquement, pénalité de mobilité lourde)</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="kits">4. L'impact réel des season kits</h2>
          <p>Les <strong>season kits</strong> sont le vrai moteur de reclassement de la Saison 7. Ce ne sont pas des accessoires : ils modifient la nature de l'arme.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Kit</th><th>Effet</th><th>Effet sur le tier</th></tr></thead>
              <tbody>
                <tr><td><strong>PCC9</strong></td><td>Full-Auto Kit</td><td>Ajoute le mode automatique complet</td><td><strong>D → A</strong> en test : recul quasi nul, tenue de porte</td></tr>
                <tr><td><strong>M110</strong></td><td>Dual-Stage Trigger</td><td>2 projectiles par gâchette</td><td><strong>A</strong> : devient un vrai mark de précision à l'overwatch</td></tr>
                <tr><td><strong>FAL</strong></td><td>Recoil Kit</td><td>Cadence de « moyennement-faible » à « élevée »</td><td><strong>A</strong> : dégâts stables à bas RPM, Lockdown/Forbidden</td></tr>
                <tr><td><strong>MPX</strong></td><td>Barrel Vulcan</td><td>Branche de munitions à chair</td><td><strong>B</strong> confirmé : nouveau profil de dégâts</td></tr>
                <tr><td><strong>UMP45</strong></td><td>Parties de modification</td><td>Nouvelles pièces, « pas Overpowered » selon l'éditeur</td><td>Reste en milieu de tableau</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Les kits expirent en fin de saison</h4>
            <p>MoreFun l'a confirmé : les season kits seront <strong>retirés à la fin de la saison</strong>, et un nouveau lot remplacera celui-ci pour d'autres armes. Un kit de saison est donc un <strong>investissement à court terme</strong> — n'achetez jamais un skin d'une arme que vous n'utilisez que grâce à un kit saisonnier.</p>
          </div>

          <h2 id="par-carte">5. Tier list par carte</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Carte</th><th>À privilégier</th><th>À éviter</th></tr></thead>
              <tbody>
                <tr><td><strong>TV Station</strong></td><td>P90, PCC9 + Full-Auto, AK-15SC</td><td>Snipers en primaire</td></tr>
                <tr><td><strong>Farm / Armory</strong></td><td>H416, A545, FAL + Recoil Kit</td><td>SMG pure comme seule arme</td></tr>
                <tr><td><strong>Valley / Northridge</strong></td><td>M24, M110 + Dual-Stage, U191, SJ16</td><td>SMG à canon court en primaire</td></tr>
                <tr><td><strong>Airport</strong></td><td>Fusil polyvalent + un plan CQB secondaire</td><td>Les kits « un seul coup à 130 m »</td></tr>
                <tr><td><strong>Zones infectées</strong></td><td>USAS-12, S12K, MP5, MPX + dum-dum</td><td>Les munitions T5/T6 contre des bots</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="zombies">6. Le meta spécifique des modes zombies</h2>
          <div class="callout callout-danger">
            <h4>Contre les IA, la pénétration est du gaspillage</h4>
            <p>Utiliser de la 5.45×39 ou de la 5.56×45 meta contre des zombies est un <strong>suicide financier</strong>. Les mutants ne portent pas d'armure T6 : ce qui compte, c'est le <strong>dégâts de groupe</strong>. Le combo gagnant est <strong>shotgun + munitions à chair</strong> : un USAS-12 ou un S12K, puis du dum-dum 9×19 pour les jambes.</p>
          </div>
          <ul>
            <li><strong>Infected Zone :</strong> le lootPvP compte autant que les zombies — un fusil d'assaut T4 est un bon compromis.</li>
            <li><strong>Zombie Endless :</strong> la classe est imposée et le loadout fourni : le shotgun est roi parce qu'il touche plusieurs ennemis d'un tir.</li>
            <li><strong>No Man's Land :</strong> entraînement, pas de loot : le coût est secondaire, seul compte l'apprentissage des mutations.</li>
          </ul>

          <h2 id="armures">7. Le tier list des armures</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Tier</th><th>Pièces de référence</th><th>Matériau</th><th>Usage</th></tr></thead>
              <tbody>
                <tr><td><strong>T6</strong></td><td>BT101, 926 Composite, BT6</td><td>Céramique / Composite / Acier</td><td>Forbidden uniquement. BT101 : 120 de durabilité, mais 9,8 kg</td></tr>
                <tr><td><strong>T5</strong></td><td>Hvk, 6B43, BT5</td><td>Céramique / Composite / Acier</td><td>Lockdown. Le meilleur compromis protection / mobilité</td></tr>
                <tr><td><strong>T4</strong></td><td>6B13, 6B23, 6B45</td><td>Composite / Kevlar</td><td>Le cœur du meta Normal. 6B13 : 46 d'ergonomie, 5,9 kg</td></tr>
                <tr><td><strong>T3</strong></td><td>6B62, KN, 6B12</td><td>Kevlar</td><td>Budget, mais 55–60 de durabilité seulement</td></tr>
                <tr><td><strong>T2</strong></td><td>6B2</td><td>Kevlar</td><td>Le kit du débutant : 30 000 K, 2,8 kg, 38 de durabilité</td></tr>
                <tr><td><strong>T1</strong></td><td>Gilet tactique</td><td>Nylon</td><td>10 000 K. Symbolique, mais ça évite le nudisme en début de raid</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Le réflexe anti-gear-fear</h4>
            <p>Un 6B13 T4 à 150 000 K avec 46 d'ergonomie est <strong>meilleur</strong> qu'un BT101 à 450 000 K avec 28 d'ergonomie pour 90 % des combats. Le sur-équipement est un choix, pas une obligation : c'est un pari sur votre propre taux de survie.</p>
          </div>

          <h2 id="armurerie">8. L'armurerie de référence (données du site)</h2>
          <p class="text-muted">Le catalogue complet des 24 armes de référence, trié par tier et par cadence de tir.</p>
          <div class="weapon-grid"></div>

          <h2 id="verdict">9. Le tier list par tier</h2>
          <div class="tier-list-output"></div>

          <h2 id="faq">10. FAQ tier list</h2>
          <h3>Quelle est la meilleure arme de la Saison 7 ?</h3>
          <p>H416 ou A545 pour la plupart. AK-12 pour l'efficacité en Koen. P90 ou PCC9 + Full-Auto Kit pour le CQB.</p>
          <h3>Les LMG valent-ils le coup ?</h3>
          <p>Sélectionnellement oui : le RPK-16 (600 RPM, chargeur 60) et l'AEK (800 RPM) offrent un vrai potentiel de suppression. Le MG3, lui, reste <strong>réservé au squad</strong> : sa pénalité de mobilité est un arrêt de mort en solo.</p>
          <h3>Quel est le meilleur kit budget ?</h3>
          <p>Le build MPX à ~160 000 K avec de l'AP 6.3 en PL 3 pour le CQB, ou le FAL à ~260 000 K pour le meilleur rapport qualité-prix en fusil. Voir <a href="meta-loadout-optimizer.html">l'optimiseur de loadout</a>.</p>
          <h3>Les bots faussent-ils la tier list ?</h3>
          <p>Oui, fortement. Les IA de Lockdown dotées d'armure T4 neuve et de munitions T4 — on en trouve même dans les missions — creusent l'écart entre le kit et le terrain. Une tier list « PvP pure » serait différente, mais elle ne correspondrait plus à votre expérience réelle.</p>
          <p>Pour les builds complets, voir <a href="meta-builds-roles.html">le guide des builds par rôle</a>. Pour la méthode, voir <a href="meta-stratégies-s7.html">le guide des stratégies S7</a>.</p>
"""

page('meta-tier-list-globale.html',
     "Tier List Globale S7",
     "Tier list complète d'Arena Breakout Infinite Saison 7 : A545, H416, U191, AK-12, M24, P90 en S, impact des season kits, tier list par carte et par catégorie, armures T1 à T6.",
     "../img/meta/meta-tier-list.jpg",
     "Meta — Tier List", "Tier List globale S7",
     "Cinq critères, quatre tiers, une seule question : quelle arme vaut votre Koen dans votre mode ?",
     tier,
     [("methode", "1. Méthodologie"), ("global", "2. Tier list global"), ("par-categorie", "3. Par catégorie"),
      ("kits", "4. Impact des kits"), ("par-carte", "5. Par carte"), ("zombies", "6. Meta zombies"),
      ("armures", "7. Tier list des armures"), ("armurerie", "8. Armurerie de référence"), ("verdict", "9. Tier list par tier"), ("faq", "10. FAQ")],
     extra_js=True, nav=NAV, crumb=CRUMB)

print("OK S11 batch A")
