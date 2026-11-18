import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Objets')
CRUMB = ('Objets', 'items-munitions.html')

# ───────────────────────────────────────────── 5. CRAFT / WORKBENCH
craft = """
          <figure class="page-figure">
            <img src="../img/items/ammo.jpg" alt="Cartouches militaires et boîte de munitions" loading="lazy">
            <figcaption>Le Workbench est la seconde source de munitions du jeu : la T6 et la T7 ne s'achètent plus, elles se fabriquent.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Lieu</span><span class="fact-value">Trophy Room → Living Area puis Workbench</span></div>
            <div class="fact"><span class="fact-label">Niveaux</span><span class="fact-value">0 → 4 (T6 au niveau 3, T7 au niveau 4)</span></div>
            <div class="fact"><span class="fact-label">S7</span><span class="fact-value">Formules au niveau max à l'obtention</span></div>
            <div class="fact"><span class="fact-label">Recherche</span><span class="fact-value">2 emplacements de bonus par formule</span></div>
          </div>

          <h2 id="principe">1. Le Workbench, comment ça marche</h2>
          <p>Le Workbench est l'établi de la <strong>Trophy Room</strong>. Il transforme des objets divers (et parfois des Koen) en <strong>munitions</strong>, <strong>médicaments</strong>, <strong>objets tactiques</strong> et <strong>équipement</strong>, sur plusieurs heures réelles de craft. Chaque formule affiche :</p>
          <ul>
            <li>un compteur de <strong>« Times Formula Crafted »</strong>,</li>
            <li>son <strong>statut de recherche</strong> et un bouton de partage,</li>
            <li>un <strong>prix de réapprovisionnement</strong> (coût des pièces manquantes),</li>
            <li>un <strong>prix de vente au contact</strong> (contact selling price).</li>
          </ul>
          <div class="callout callout-warning">
            <h4>L'ordre de construction qui compte</h4>
            <p>Construisez d'abord la <strong>Living Area</strong>, puis le Workbench niveau 0 → 4. Monter le Workbench avant la Living Area, c'est affamer votre sustain de raid pour un gain de craft : les deux se disputent les mêmes Koen de départ.</p>
          </div>

          <h2 id="s7">2. Ce qui change en Saison 7</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Changement</th><th>Avant</th><th>Saison 7</th></tr></thead>
              <tbody>
                <tr><td><strong>Niveau des formules</strong></td><td>Il fallait les faire monter</td><td><strong>Elles sont au niveau maximum dès l'obtention</strong></td></tr>
                <tr><td><strong>Exigences de matériaux</strong></td><td>Tables de coût de l'avant 16 septembre 2026</td><td><strong>Réajustées à un niveau plus raisonnable</strong></td></tr>
                <tr><td><strong>Usages des objets divers</strong></td><td>Limités</td><td>De nouveaux usages : <strong>montres de gousset, carnets d'ouvrier, analyseurs de gaz</strong> servent maintenant à craft des munitions</td></tr>
                <tr><td><strong>Nouvel objet tactique craftable</strong></td><td>—</td><td><strong>Grenade étourdissante M290</strong></td></tr>
                <tr><td><strong>Recherche d'amélioration</strong></td><td>—</td><td><strong>Nouveau système complet</strong> avec l'Improvement Blueprint</td></tr>
                <tr><td><strong>Partage de formules</strong></td><td>Impossible</td><td>On peut <strong>visiter les Trophy Rooms d'amis</strong> et apprendre leurs formules ; le propriétaire reçoit des blueprints d'assistance prioritaires</td></tr>
                <tr><td><strong>Fonction « Check Usage »</strong></td><td>—</td><td>Dans le Storage, les objets divers montrent quels contacts les échangent et quelles formules les utilisent</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="recherche">3. L'Improvement Research</h2>
          <p>Le cœur de la S7 côté craft. Vous trouvez des <strong>Improvement Blueprint</strong> en raid, vous les dépensez sur <strong>une</strong> formule, et vous choisissez <strong>2 résultats</strong> parmi les options tirées au sort. Les résultats <strong>non sélectionnés sont perdus</strong>.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Résultat</th><th>Effet type</th><th>Score (captures d'écran)</th></tr></thead>
              <tbody>
                <tr><td><strong>Research Expert</strong></td><td>Réduit de 10 % le nombre de blueprints requis</td><td>—</td></tr>
                <tr><td>Fast Track I</td><td>Réduit le temps de craft</td><td>30</td></tr>
                <tr><td>Steady Boost I</td><td>Amélioration de la production</td><td>—</td></tr>
                <tr><td>Tactical Synergy II</td><td>Bonus contextuel sur la recette (« 20× ×1 », « Commander ×1 » sur .338 AP)</td><td>40</td></tr>
                <tr><td>Scrap Recovery III</td><td>Chance de récupérer les matériaux</td><td>60</td></tr>
                <tr><td><strong>Unexpected Surplus IV</strong></td><td>Chance d'<strong>annuler tous les coûts</strong></td><td>94</td></tr>
                <tr><td><strong>First-Rate Provisions</strong></td><td>Chance de transformer un casque <strong>SH65 en IND70</strong></td><td>—</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Le score de recherche</h4>
            <p>Le <strong>Season Improvement Research Score</strong> d'une formule est la somme des scores de ses deux résultats. Il sert à <strong>comparer</strong> les combinaisons — il ne change pas mécaniquement les chances d'obtention d'un objet (point non confirmé par l'éditeur).</p>
            <p>Le datamining communautaire recense environ <strong>25 recettes researchables et 721 résultats possibles</strong> — d'où le caractère très aléatoire des tirages. <em>(Chiffres non officiels.)</em></p>
          </div>

          <h2 id="blueprints">4. Où trouver les blueprints</h2>
          <ul>
            <li><strong>En raid</strong>, avec une probabilité plus forte dans les <strong>boîtes à documents</strong>, les <strong>vêtements</strong> et les <strong>tiroirs</strong>.</li>
            <li>Via les <strong>missions actives</strong>.</li>
            <li>Via le <strong>Marché</strong> et les contacts.</li>
            <li>Via vos <strong>amis</strong> : vous appris leur formule, ils reçoivent des blueprints d'assistance, qui sont <strong>prioritaires</strong> dans votre file de recherche.</li>
          </ul>
          <div class="callout callout-warning">
            <h4>Le partage de formule, mode d'emploi</h4>
            <p>Icône d'amis → choisir un joueur → entrer dans sa Trophy Room → aller à son Workbench → sélectionner une formule disponible → l'étudier. Vous recevez une formule de test utilisable sur <strong>votre</strong> Workbench. Le propriétaire, lui, reçoit des blueprints d'assistance. On ne peut pas produire chez quelqu'un d'autre.</p>
          </div>

          <h2 id="couts">5. Les coûts et temps de craft</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Recette</th><th>Niveau Workbench</th><th>Temps</th><th>Quantité</th><th>Matériaux</th></tr></thead>
              <tbody>
                <tr><td>.45 AP</td><td>1</td><td>6 h</td><td>120</td><td>Câble de données, lecteur de disquette, poudre bleue</td></tr>
                <tr><td>5.7×28 L191</td><td>1</td><td>6 h</td><td>120</td><td>Couteau de chasse, multimètre, poudre bleue</td></tr>
                <tr><td>7.62×25 PS</td><td>1</td><td>6 h</td><td>120</td><td>Réveil de bureau, lecteur de disquette, poudre bleue</td></tr>
                <tr><td>7.62×39 BP</td><td>2</td><td>12 h</td><td>120</td><td>Antenne, cartouche de jeu, poudre verte</td></tr>
                <tr><td>7.62×54 LPS</td><td>2</td><td>12 h</td><td>60</td><td>Antenne, cartouche de jeu, poudre verte</td></tr>
                <tr><td>5.7×28 SS190</td><td>2</td><td>12 h</td><td>120</td><td>Plaque de titane, carte de circuit, poudre rouge</td></tr>
                <tr><td>7.62×51 M61</td><td>3</td><td>16 h</td><td>30</td><td>Bobine haute fréquence, carburant haute énergie, nitrocellulose</td></tr>
                <tr><td>7.62×54 SNB</td><td>3</td><td>20 h</td><td>20</td><td>Réservoir de carburant, plaque de titane, nitrocellulose</td></tr>
                <tr><td><strong>.338 AP</strong></td><td>3</td><td>24 h</td><td>10</td><td>Pack de batteries, antenne, nitrocellulose</td></tr>
                <tr><td><strong>7.62×54 7N37</strong> (T7)</td><td>4</td><td>28 h</td><td>20</td><td>Cube d'or, carburant haute énergie, nitrocellulose</td></tr>
                <tr><td>IND70 Tactical Helmet</td><td>5</td><td>40 h</td><td>1</td><td>2 Metal Hearts, 2 Sound-Muffling Cotton, 4 Space Boy comics, <strong>500 000 Koen</strong></td></tr>
                <tr><td>BT201 Full Body Armor</td><td>5</td><td>40 h</td><td>1</td><td>2 Porcelaine, 2 plaques de titane, 4 Space Boy comics, <strong>500 000 Koen</strong></td></tr>
                <tr><td>T7 Thermal Imager</td><td>3</td><td>48 h</td><td>1</td><td>Modèle satellite Sergey, niveau, module laser</td></tr>
                <tr><td>Traitement Ultra-Strength expérimental</td><td>4</td><td>20 h</td><td>1</td><td>Testeur portable, thermomètre, seringue</td></tr>
                <tr><td>Battlefield First Aid Kit Set</td><td>4</td><td>20 h</td><td>1</td><td>Pompe à insuline, injection de glucose, ciseaux médicaux</td></tr>
                <tr><td>Improved Multi-Burst Flashbang</td><td>—</td><td>6 h</td><td>5</td><td>Bouteille de propane, photomètre, lampe à kérosène</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Temps de craft : la vraie contrainte</h4>
            <p>Le craft est en <strong>temps réel</strong>. Une IND70 ou un BT201 demande <strong>40 heures</strong>. L'IND70 est craftable au <strong>niveau 5</strong> de Workbench et son <strong>prix de réapprovisionnement</strong> s'élève à <strong>1 784 194 Koen</strong> dans une capture de la communauté. Avec un bonus <strong>Unexpected Surplus IV à 30 %</strong>, vous économisez en moyenne <strong>535 000 Koen par craft</strong>. C'est le meilleur argument pour farmer des blueprints.</p>
          </div>

          <h2 id="rentabilite">6. Quelles formules researcher en premier</h2>
          <ol>
            <li><strong>Les munitions que vous tirez vraiment</strong> — un résultat « +20 à +60 cartouches » à 100 % se paie sur <em>chaque</em> craft. Un joueur a obtenu +30 % puis +40 % sur sa .45 APWC T4.</li>
            <li><strong>Les crafts d'équipement chers</strong> — IND70, BT201, SH65 : plus le craft est cher, plus un remboursement vaut.</li>
            <li><strong>Les médicaments et stimulants</strong> — la communauté rapporte <strong>20 % de remboursement</strong> sur le Traitement Ultra-Strength et <strong>100 %</strong> sur trois stimulants de régénération (12 h de soin en plus).</li>
          </ol>
          <div class="callout callout-success">
            <h4>Les règles d'or de la recherche</h4>
            <p>1) <strong>Ne dispersez pas vos blueprints</strong> sur toutes les formules : concentrez-les sur 2 ou 3 recettes que vous craftz souvent.<br>2) <strong>Visez les hautes raretés</strong> : Unexpected Surplus et First-Rate Provisions sont les plus rentables.<br>3) <strong>Ne négligez pas le retour de matériaux</strong> : pour une production coûteuse, un remboursement vaut mieux qu'un gain de vitesse.<br>4) <strong>Combinez</strong> : retour de matériaux + production supplémentaire.<br>5) <strong>Comparez le prix de revient</strong> : si les matériaux coûtent plus cher que le résultat ne vaut, ne craftz qu'avec un bonus de remboursement ou de surproduction.</p>
          </div>

          <h2 id="reset">7. Le reset de saison</h2>
          <p>Les <strong>résultats de recherche sont réinitialisés à chaque saison</strong>. Les recettes, elles, restent débloquées. Concrètement : ce que vous researches en S7 ne sert qu'en S7. Ne dispersez pas vos blueprints en fin de saison sur des bonuses « SURPLUS » — ils perdront toute valeur au reset.</p>

          <h2 id="checklist">8. Check-list Workbench</h2>
          <ul>
            <li><strong>Living Area d'abord</strong>, puis Workbench niveau par niveau.</li>
            <li>Choisir <strong>une</strong> formule de munitions que vous tirez, et la researched jusqu'à 2 bons résultats.</li>
            <li>Activer la fonction <strong>« Check Usage »</strong> dans le Storage avant de vendre un matériau : il peut entrer dans une formule.</li>
            <li>Installer les blueprints d'assistance de vos amis <strong>en premier</strong> : ils sont prioritaires.</li>
            <li>En fin de saison : <strong>ne plusammy</strong> de blueprints sur des bonus à durée limitée.</li>
          </ul>
          <p>Pour la valeur des matériaux finis, voir <a href="items-valeur.html">le guide de la valeur</a>. Pour les munitions elles-mêmes, voir <a href="items-munitions.html">le guide des munitions</a>.</p>
"""

page('items-craft-workbench.html',
     "Craft & Workbench",
     "Guide du Workbench ABI Saison 7 : Improvement Research, blueprints, coûts et temps de craft, formules de munitions et d'équipement, reset de saison et meilleures recettes à researcher.",
     "../img/items/ammo.jpg",
     "Objets — Craft", "Craft & Workbench",
     "Improvement Research, blueprints, 40 heures pour un casque IND70 : la manufacture de la saison.",
     craft,
     [("principe", "1. Principe"), ("s7", "2. Ce qui change en S7"), ("recherche", "3. Improvement Research"),
      ("blueprints", "4. Où trouver les blueprints"), ("couts", "5. Coûts de craft"), ("rentabilite", "6. Quoi researcher"),
      ("reset", "7. Reset de saison"), ("checklist", "8. Check-list")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ───────────────────────────────────────────── 6. COLLECTION ROOM
collection = """
          <figure class="page-figure">
            <img src="../img/items/collection-room.jpg" alt="Vitrine d'exposition de la Trophy Room" loading="lazy">
            <figcaption>Collection Room — votre musée personnel de red drops, et le coffre-fort définitif de vos objets les plus rares.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Accès</span><span class="fact-value">Gratuit depuis la Saison 4</span></div>
            <div class="fact"><span class="fact-label">Stockage</span><span class="fact-value">999 red drops (S7)</span></div>
            <div class="fact"><span class="fact-label">Niveau</span><span class="fact-value">Collection Room +2 en S7</span></div>
            <div class="fact"><span class="fact-label">Bonus</span><span class="fact-value">Titres de collectionneur</span></div>
          </div>

          <h2 id="principe">1. À quoi sert la Collection Room</h2>
          <p>Depuis la <strong>Saison 4</strong>, la Collection Room est <strong>gratuite</strong> dès que vous avez la Trophy Room. Elle sert à trois choses :</p>
          <ul>
            <li><strong>Stocker</strong> les objets <strong>Gold Bounty</strong> (les red drops) hors de votre Storage, et les récupérer librement — l'éditeur le formule comme « stocker et récupérer librement les Gold Bounty pour libérer de l'espace de stockage ».</li>
            <li><strong>Exposer</strong> votre collection dans une vitrine, avec des améliorations de présentation.</li>
            <li><strong>Obtenir des titres</strong> de collectionneur à des paliers de collection.</li>
          </ul>
          <div class="callout callout-success">
            <h4>Pourquoi c'est important en 2026</h4>
            <p>Depuis la S4, les red drops sont <strong>retirés du Marché</strong>. Votre seul usage « financier » est la vente à un contact — et un contact paie <strong>moins</strong> que la valeur affichée. Avec un stockage porté à <strong>999</strong>, un Document Secret devient un coffre-fort quasi gratuit : il ne coûte plus de place et il ne se périme pas.</p>
          </div>

          <h2 id="s7">2. Les améliorations de la Saison 7</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Amélioration</th><th>Détail</th></tr></thead>
              <tbody>
                <tr><td><strong>Limite de stockage des red drops</strong></td><td>Passée à <strong>999</strong> (800 depuis la S5)</td></tr>
                <tr><td><strong>Niveau de la Collection Room</strong></td><td>Limite de niveau augmentée de <strong>+2</strong></td></tr>
                <tr><td><strong>Marquage rouge</strong></td><td>Le marquage des nouvelles plaques d'identité est restreint à l' <strong>étagère dédiée</strong> ; il n'apparaît plus sur l'écran principal de la Trophy Room ni à l'entrée du lobby</td></tr>
                <tr><td><strong>Personnalisation</strong></td><td>Frame Infected Area, Central Sculpture: Destruction and Rebirth, Central Piece: Revolution (missions en zone infectée)</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="reds">3. La collection rouge de la Saison 7</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Objet</th><th>Rareté</th><th>Valeur (Koen)</th><th>Note</th></tr></thead>
              <tbody>
                <tr><td><strong>Elysium</strong></td><td>Red</td><td>4 500 000</td><td>Drop des zones infectées ; garanti par la série de missions zombies</td></tr>
                <tr><td>Carte graphique</td><td>Red</td><td>3 200 000</td><td>Le classique électronique</td></tr>
                <tr><td>Laptop MRID</td><td>Red</td><td>2 800 000</td><td>Luxury Gift Box MRID ; jouable en tant qu'objet de raid ? non — pièce de collection</td></tr>
                <tr><td>Northern Stars</td><td>Red</td><td>2 200 000</td><td>Collectible S7</td></tr>
                <tr><td>Luth à double manche</td><td>Red</td><td>1 800 000</td><td>Joue une mélodie en raid</td></tr>
                <tr><td>Flûte de jade émeraude</td><td>Red</td><td>1 600 000</td><td>Joue une mélodie en raid</td></tr>
                <tr><td>Circuit militaire</td><td>Red</td><td>1 500 000</td><td>Électronique</td></tr>
                <tr><td>Lingot d'or</td><td>Red</td><td>1 200 000</td><td>Coffres rares et boss</td></tr>
                <tr><td>Lunar Soil Sample</td><td>2×2</td><td>780 000</td><td>Jusqu'au 9 novembre 2026</td></tr>
                <tr><td>Chaotic Matter</td><td>Red</td><td>—</td><td>Sur toutes les cartes en S7</td></tr>
                <tr><td>Fading Dawn</td><td>Red</td><td>—</td><td>29 octobre → 25 novembre 2026</td></tr>
                <tr><td>Corrupted Clock</td><td>Red</td><td>—</td><td>29 octobre → 25 novembre 2026, craftable en Trophy Room</td></tr>
                <tr><td>Stallion Wave Chaser</td><td>Red</td><td>—</td><td>27 août → 30 septembre 2026</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="garder">4. Garder ou vendre ?</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Gardez si…</h3>
              <p class="card-text">— vous voulez complet<strong>er votre vitrine</strong> et obtenir les titres de collectionneur ;</p>
              <p class="card-text">— l'objet est <strong>hors marché</strong> (tous les red drops depuis la S4) ;</p>
              <p class="card-text">— la vente au contact vous <strong>paierait 30 % sous la valeur affichée</strong> ;</p>
              <p class="card-text">— vous avez de la place (<strong>999</strong> désormais).</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Vendez si…</h3>
              <p class="card-text">— vous avez besoin de <strong>Koen immédiat</strong> pour un round ;</p>
              <p class="card-text">— l'objet a une <strong>valeur liquidative réelle</strong> (ex. Lingot d'or vendu 1,2 M) ;</p>
              <p class="card-text">— vous êtes en <strong>fin de saison</strong> et le pass saisonnier vous coûte cher ;</p>
              <p class="card-text">— le drop est <strong>limité dans le temps</strong> (Fading Dawn, Corrupted Clock) et vous n'avez pas la place.</p>
            </div></div>
          </div>

          <h2 id="titres">5. Les titres de collectionneur</h2>
          <p>La Collection Room récompense la complétude par des <strong>titres</strong> obtenus à des paliers de collection. C'est le seul avantage non cosmétique et non financier de la salle : <strong>un titre se montre dans votre profil et sur les tables de jeu</strong>.</p>
          <ul>
            <li>Les <strong>rubans de collection</strong> et titres d'<strong>extermination</strong> : affichage de progression.</li>
            <li>Le <strong>titre S7 Wealthy Winner</strong> est la récompense directe de l'opération Zombie No Man's Land : accumulez la valeur de loot extrait pour l'obtenir.</li>
            <li>Les <strong>décos de Trophy Room</strong> (sculpture centrale, pièce centrale, fond Infected Area) sont des récompenses de missions, pas de la Collection Room — mais ils l'accompagnent visuellement.</li>
          </ul>

          <h2 id="trophy">6. La Trophy Room en 2026</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Section</th><th>Rôle</th><th>Conseil S7</th></tr></thead>
              <tbody>
                <tr><td><strong>Storage</strong></td><td>Tous vos objets</td><td>Utilisez « Check Usage » avant de vendre un matériau</td></tr>
                <tr><td><strong>Living Area</strong></td><td>Amélioration du base de vie</td><td>À construire avant le Workbench</td></tr>
                <tr><td><strong>Workbench</strong></td><td>Craft de munitions, médical, tactique, équipement</td><td>Formules au niveau max dès l'obtention en S7</td></tr>
                <tr><td><strong>Collection Room</strong></td><td>Vitrine des red drops + titres</td><td>999 emplacements de stockage en S7</td></tr>
                <tr><td><strong>Contacts / marché</strong></td><td>Vente et achats</td><td>Deke Vinson réapprovisionne toutes les 2–3 h</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="checklist">7. Check-list de fin de saison</h2>
          <ul>
            <li>Tout red drop qui expire bientôt : <strong>vendu ou stocké en priorité</strong>.</li>
            <li>Comptez vos red drops : le <strong>stockage à 999</strong> n'a de sens que si vous savez ce que vous avez.</li>
            <li>Ne vendez pas un red pour financer un pass : le pass ne se rentabilise qu'en début de saison.</li>
            <li>Faites un passage en <strong>Collection Room</strong> avant le reset de saison : vos bonus de recherche seront perdus, pas vos objets.</li>
          </ul>
          <p>Pour la valeur liquidative de chaque objet, voir <a href="items-valeur.html">le guide de la valeur</a>. Pour le craft, voir <a href="items-craft-workbench.html">le guide Workbench</a>.</p>
"""

page('items-collection-room.html',
     "Collection Room & Trophy Room",
     "Collection Room d'ABI : stockage 999 red drops S7, titres de collectionneur, nouveau auvent zombie, conservation ou vente des red drops et guide Trophy Room complet.",
     "../img/items/collection-room.jpg",
     "Objets — Collection", "Collection Room",
     "999 emplacements, des titres, et le coffre-fort des objets que le marché ne vend plus.",
     collection,
     [("principe", "1. Principe"), ("s7", "2. Améliorations S7"), ("reds", "3. Collection rouge S7"),
      ("garder", "4. Garder ou vendre"), ("titres", "5. Titres"), ("trophy", "6. La Trophy Room"), ("checklist", "7. Check-list")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ───────────────────────────────────────────── 7. KOEN / ECONOMIE
koen = """
          <figure class="page-figure">
            <img src="../img/items/koen-economy.jpg" alt="Poste de marché noir clandestin" loading="lazy">
            <figcaption>Le Koen ne se gagne pas en tirant : il se gagne en.Extrait, en vendant au bon moment, et en ne transportant jamais plus que ce que vous pouvez perdre.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Règle d'or</span><span class="fact-value">5 000 Koen par slot</span></div>
            <div class="fact"><span class="fact-label">Budget max</span><span class="fact-value">20 % du stash par sortie</span></div>
            <div class="fact"><span class="fact-label">Revenu passif</span><span class="fact-value">Deke Vinson : marge ×3</span></div>
            <div class="fact"><span class="fact-label">Covert Ops</span><span class="fact-value">150 000 – 500 000 K par run</span></div>
          </div>

          <h2 id="regles">1. Les 4 règles qui regulator votre économie</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Règle</th><th>Chiffre</th><th>Pourquoi</th></tr></thead>
              <tbody>
                <tr><td><strong>Valeur par slot</strong></td><td>≥ 5 000 Koen</td><td>Un 1×1 à 10 000 K bat un 4×1 à 20 000 K</td></tr>
                <tr><td><strong>Budget de kit</strong></td><td>≤ 20 % du stash</td><td>500 K de banque → 100 K max ; une mort ne doit pas vous arrêter</td></tr>
                <tr><td><strong>Barter inutile</strong></td><td>≥ 8 000 K par slot</td><td>Ruban 800, allumettes 400, vis 600 : du bruit de slot</td></tr>
                <tr><td><strong>Seuil de vente</strong></td><td>4 000 K</td><td>Sous ce seuil, vendez au contact (immédiat, sans frais) ; au-dessus, passez par le marché</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>L'erreur qui coûte le plus cher</h4>
            <p>Monter un kit à 600 000 Koen « parce que c'est la saison Forbidden ». Si vous mourez, vous avez perdu <strong>quatre mois</strong> d'économie en une raid. La bonne question n'est jamais « qu'est-ce que j'ai ? » mais « qu'est-ce que je peux me permettre de perdre aujourd'hui ? ».</p>
          </div>

          <h2 id="revenus">2. Les revenus passifs — l'argent sans risque</h2>
          <h3>Le flip Deke Vinson</h3>
          <p>Deke Vinson réapprovisionne <strong>toutes les 2 à 3 heures</strong> (avec un gros reset à 22 h PST). Ses articles sont souvent sous-évalués par rapport au marché. Exemples de marges observées :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Article</th><th>Prix Deke</th><th>Prix marché</th><th>Marge</th></tr></thead>
              <tbody>
                <tr><td>Armure Tier 4</td><td>≈ 34 000</td><td>≈ 56 000</td><td><strong>+22 000</strong></td></tr>
                <tr><td>Bundle M855 (120 cartouches)</td><td>≈ 21 000</td><td>≈ 57 000</td><td><strong>+36 000</strong></td></tr>
                <tr><td><strong>Lunette thermique</strong></td><td>≈ 50 000</td><td>≈ 150 000</td><td><strong>+100 000</strong></td></tr>
                <tr><td>Sac à dos</td><td>20 000</td><td>67 000</td><td><strong>+47 000</strong></td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>La technique du refresh</h4>
            <p>Quand vous achetez des pièces pour gunsmithing, <strong>rafraîchissez plusieurs fois les prix</strong> : les nouveaux articles moins chers apparaissent. Sur un build d'arme, c'est des milliers de Koen économisés. Et pour vendre : ne posez jamais au prix plancher. Si le marché suggère 5 475 K pour un sac et que le prix moyen est 6 750 K, <strong>positionnez-vous entre les deux</strong>.</p>
          </div>

          <h2 id="covert">3. Les runs gratuits (Covert Ops / scav)</h2>
          <ul>
            <li>Vous entrez avec un <strong>équipement généré aléatoirement</strong> : <strong>zéro risque financier</strong>.</li>
            <li>Le mode se recharge : les estimations de la communauté situent le cooldown autour de <strong>15 minutes</strong>.</li>
            <li>Rendement typique : <strong>150 000 à 500 000 Koen par extraction</strong> en ciblant les zones à fort conflit (Motel de Farm, Hôtel de Northridge) <em>après</em> que les gros combats se sont calmés.</li>
            <li>Bonus : en éliminant des boss comme <strong>Fred</strong> à Northridge, on peut récupérer le jeton <strong>Wedding Ring</strong> et de l'armure T4.</li>
            <li>Enchaîner les <strong>missions Covert Ops hebdomadaires</strong> rapporte environ <strong>3 millions de Koen</strong> au total.</li>
          </ul>
          <div class="callout callout-warning">
            <h4>Où aller en scav</h4>
            <p>Les zones de conflit <strong>après</strong> le combat : les conteneurs restent, les joueurs sont partis. À noter : la règle des 5 000 Koen par slot s'applique encore plus en scav — votre sac ne vaut rien si vous ne le remplissez pas.</p>
          </div>

          <h2 id="marche">4. Le marché : la mécanique</h2>
          <ul>
            <li><strong>12 slots</strong> par dépôt, <strong>500 objets</strong> maximum par semaine.</li>
            <li>Des <strong>frais de gestion</strong> sont prélevés sur le prix de vente, variables selon la valeur de l'objet et la durée de mise en ligne.</li>
            <li>Le marché propose le <strong>prix plancher</strong> et le <strong>prix moyen</strong> de chaque objet : c'est votre reference de négociation.</li>
            <li>Le <strong>prix moyen</strong> est calculé à partir des ventes réelles et est plus représentatif que le prix affiché.</li>
            <li>Les objets <strong>« Check Usage »</strong> (fonction S7 du Storage) permettent de comparer instantanément le prix de marché, le prix contact et le prix de craft d'un même objet.</li>
          </ul>
          <div class="callout callout-success">
            <h4>La règle de placement</h4>
            <p>Pour vendre <strong>vite</strong>, posez légèrement sous le prix le plus bas du marché. Pour <strong>maximiser</strong>, posez entre le plancher et le prix moyen. Et surtout : vendez en <strong>lots</strong> les objets de faible valeur (poudre, munitions bon marché) — un stack par slot au lieu d'un par pile.</p>
          </div>

          <h2 id="evenements">5. L'argent gratuit des événements</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Source</th><th>Gain</th><th>Fréquence</th></tr></thead>
              <tbody>
                <tr><td><strong>Bonus de connexion</strong></td><td>Millions de Koen annoncés à l'ouverture de la saison</td><td>Journée</td></tr>
                <tr><td><strong>Défi de Merit</strong></td><td>3× Koen sur votre meilleur Merit hebdomadaire, jusqu'à <strong>3 000 000 K/semaine</strong></td><td>Hebdomadaire (lun. 5 h UTC)</td></tr>
                <tr><td><strong>Pass de saison</strong></td><td>Des Koen sur la piste gratuite et en récompense de paliers</td><td>Continue</td></tr>
                <tr><td><strong>Festival Biohazard &amp; Automne</strong></td><td>Check-in, boutique, Défi de Vinson, Lunar Soil Sample</td><td>Depuis le 24 sept. 2026</td></tr>
                <tr><td><strong>Zombie No Man's Land</strong></td><td>Pass de check-in, paliers à 4 / 8 / 16 tâches quotidiennes</td><td>Hebdomadaire</td></tr>
                <tr><td><strong>Premium Koen Random Bundles</strong></td><td>Koen contre un bundle aléatoire</td><td>Événement limité</td></tr>
              </tbody>
            </table>
          </div>

          <figure class="page-figure">
            <img src="../img/items/loot-value.jpg" alt="Valise de butin ouverte sur une caisse" loading="lazy">
            <figcaption>Un bon raid, c'est une valise dont chaque slot vaut au moins 5 000 Koen — et une extraction réussie.</figcaption>
          </figure>

          <h2 id="cartes">6. Les meilleures cartes pour l'argent</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Carte</th><th>Pourquoi</th></tr></thead>
              <tbody>
                <tr><td><strong>Valley</strong></td><td>Considérée comme la meilleure carte pour l'argent : beaucoup de loot de valeur, armes et accessoires. La route Beach Villa → Radar Station cumule des caisses d'armes et des clés valorisées jusqu'à <strong>1,85 M Koen</strong></td></tr>
                <tr><td><strong>Farm</strong></td><td>Route Motel → Stables : 3–4 caisses moyennes de 20 000 à 50 000 K. En <strong>Heavy Infected Zone</strong>, le loot est sensiblement plus élevé</td></tr>
                <tr><td><strong>Northridge</strong></td><td>En Hostile Sector PvE : pas de PvP, mais il faut 5–6 stacks de munitions et 2× le médical — le coût monte vite</td></tr>
                <tr><td><strong>Hostile Sector</strong></td><td>Le loot est plus élevé qu'en Lockdown et <strong>amplifié par le smelter</strong> : les runs solo atteignent régulièrement 5 à 7 millions de Koen</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="budget">7. Le kit budget rentable</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Poste</th><th>Option</th><th>Coût</th></tr></thead>
              <tbody>
                <tr><td>Fusil CQB</td><td><strong>MPX</strong> (~88 000 K) avec AP6.3 T3</td><td>88 000</td></tr>
                <tr><td>Fusil longue distance</td><td>BM59 ou SKS de base</td><td>&lt; 30 000</td></tr>
                <tr><td>Gilet</td><td>6B23</td><td>50 000</td></tr>
                <tr><td>Casque</td><td>SH12</td><td>16 000</td></tr>
                <tr><td>Rig</td><td>926 chest rig</td><td>12 000</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>La logique du kit budget</h4>
            <p>Un kit à <strong>80 000 – 100 000 Koen</strong> est le cœur de l'économie saine : une seule extraction de 270 000 K (un coupe de'or) couvre plusieurs morts. Un budget serré n'est pas une insulte tactique : c'est ce qui permet de jouer 50 raids par semaine au lieu de 3.</p>
          </div>

          <h2 id="inventaire">8. La gestion du sac</h2>
          <ul>
            <li><strong>Un slot, c'est de l'argent.</strong> Un thermique à 50 000 K sur 1 slot vaut mieux qu'une armure à 100 000 K sur 4 slots.</li>
            <li><strong>Case sécurisée</strong> : ce qu'elle contient est sauvé même si vous mourez — mais elle ne peut pas contenir de munitions rouges depuis la S6, et elle ne sert pas en raid.</li>
            <li><strong>Poids</strong> : au-delà d'un certain seuil, vous courez plus lentement et votre endurance s'effondre. Le <strong>Strength Booster</strong> ou le <strong>Regen Injection</strong> sont des solutions temporaires au sac trop lourd.</li>
            <li><strong>Ne ramassez pas ce que vous ne vendrez pas</strong> : chaque slot superflu est une extraction ratée qui s'annonce.</li>
          </ul>

          <h2 id="plan">9. Le plan économique en 4 semaines</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Semaine</th><th>Objectif</th><th>Priorité</th></tr></thead>
              <tbody>
                <tr><td><strong>1</strong></td><td>Remplir le stash de munitions T4 et de médical, vendre le surplus au contact</td><td>Survivre et s'approvisionner</td></tr>
                <tr><td><strong>2</strong></td><td>Première clé de Farm (Motel 201) et de Valley (Beach Villa) — l'amortissement le plus rapide</td><td>Investissement</td></tr>
                <tr><td><strong>3</strong></td><td>Exploiter le smelter : 3 objets identiques violets/or à chaque run, 3 tentatives par raid</td><td>Amplifier le loot</td></tr>
                <tr><td><strong>4</strong></td><td>Passer au Forbidden avec un kit T5 propre, une fois le stock de T6 solide</td><td>Consolider</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>La règle du 20 %, gravée dans le marbre</h4>
            <p>« Ne dépensez jamais plus de 20 % de votre stash total dans une sortie. Si vous avez 500 000 Koen, votre arme, votre armure, vos munitions et votre médical ne doivent pas dépasser 100 000 Koen. » — <em>Guide Survivant S7, r/ArenaBreakoutInfinite</em>. Tout le reste de l'économie en découle.</p>
          </div>
          <p>Pour la valeur au spot, voir <a href="items-valeur.html">le guide de la valeur</a>. Pour les clés comme investissement, voir <a href="items-cles.html">le guide des clés</a>.</p>
"""

page('items-koen-economy.html',
     "Koen & Économie",
     "Guide économique ABI : règle des 5 000 Koen par slot, budget 20 %, flip Deke Vinson, marché, Covert Ops, smelter et plan économique en 4 semaines.",
     "../img/items/koen-economy.jpg",
     "Objets — Économie", "Koen & Économie",
     "Flip, marché, smelter, scav : comment remplir un stash sans jamais casser votre dynamique.",
     koen,
     [("regles", "1. Les 4 règles"), ("revenus", "2. Revenus passifs"), ("covert", "3. Covert Ops"),
      ("marche", "4. Le marché"), ("evenements", "5. Argent des événements"), ("cartes", "6. Cartes rentables"),
      ("budget", "7. Kit budget"), ("inventaire", "8. Gestion du sac"), ("plan", "9. Plan en 4 semaines")],
     extra_js=False, nav=NAV, crumb=CRUMB)

print("OK S9 batch C")
