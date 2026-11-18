import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Objets')
CRUMB = ('Objets', 'items-munitions.html')

# ───────────────────────────────────────────── 3. CLES
cles = """
          <figure class="page-figure">
            <img src="../img/items/keys.jpg" alt="Clés et cartes d'accès sur une table d'acier" loading="lazy">
            <figcaption>Les clés sont l'investissement le plus rentable d'ABI : elles se paient en 3 à 4 extractions et rapportent ensuite à chaque usage.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Usure</span><span class="fact-value">1 point en Normal · 2 en Lockdown · 3 en Forbidden</span></div>
            <div class="fact"><span class="fact-label">Clés universelles</span><span class="fact-value">Usage unique, toutes portes</span></div>
            <div class="fact"><span class="fact-label">Porte-clefs</span><span class="fact-value">Standard 5×3 (Privilèges Élite Premium)</span></div>
            <div class="fact"><span class="fact-label">Règle</span><span class="fact-value">1 clé = 1 conteneur + 1 salle</span></div>
          </div>

          <h2 id="fonctionnement">1. Comment fonctionne une clé</h2>
          <p>Chaque clé est liée à <strong>une porte précise</strong> d'une carte précise. À chaque ouverture, elle perd de la <strong>durabilité</strong> :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Coût en durabilité</th><th>Ouvertures possibles avec une clé à 30 points</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal</strong></td><td>1</td><td>30</td></tr>
                <tr><td><strong>Lockdown</strong></td><td>2</td><td>15</td></tr>
                <tr><td><strong>Forbidden</strong></td><td>3</td><td>10</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>L'arithmétique qui décide</h4>
            <p>La <strong>même clé ouvre trois fois plus de portes en Normal qu'en Forbidden</strong>. Si la pièce existe aux deux difficultés et que le loot vous intéresse, le Normal est la manière bon marché d'apprendre. Et l'<strong>Heavy Infected Zone</strong> de la S7 est l'autre bon plan : récompenses de Forbidden Zone au coût de clé de Lockdown.</p>
          </div>
          <div class="callout callout-danger">
            <h4>Le loot dans un coffre à clé ne vous appartient pas</h4>
            <p>Si vous mourez dans le raid, ce qui est dans un conteneur fermé est <strong>perdu pour vous</strong>. Une clé ne protège pas : elle ouvre. Le vrai réflexe, c'est de ne pas ouvrir une salle à 2 minutes de la fin de raid.</p>
          </div>

          <h2 id="par-carte">2. Les clés par carte</h2>
          <h3>Farm</h3>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Clé</th><th>Durabilité</th><th>Contenu</th></tr></thead>
              <tbody>
                <tr><td><strong>Motel Main Guest Room Key</strong></td><td>10</td><td>2 coffres (électronique + normal), manteau d'hiver, conteneur d'arme premium, spawn rare</td></tr>
                <tr><td>Motel 201 Key</td><td>15</td><td>Coffre, trousse de premiers secours Pro, objets rares sur la table</td></tr>
                <tr><td>Barn Office Key</td><td>15</td><td>Coffre, ordinateur, valise (au Grain Trade Center, 2ᵉ étage)</td></tr>
                <tr><td>Master Bedroom Key</td><td>15</td><td>Coffre, ordinateur, veste, spawn rare sur l'étagère (villa)</td></tr>
                <tr><td>Stables Warehouse Key</td><td>25</td><td>Boîte à documents, veste, boîte à outils</td></tr>
                <tr><td>Recycling Office Key</td><td>25</td><td>Trousse Pro, First-Aid Case</td></tr>
                <tr><td>Loading Area Key</td><td>25</td><td>First Aid Box, boîtes de munitions, coffres d'armes, pièces</td></tr>
                <tr><td>House Key</td><td>25</td><td>2 vestes, armoire de classement</td></tr>
                <tr><td>Graveyard Key</td><td>1</td><td>Coffre, veste, sac de sport (usage unique)</td></tr>
              </tbody>
            </table>
          </div>
          <h3>Valley</h3>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Clé</th><th>Durabilité</th><th>Contenu</th></tr></thead>
              <tbody>
                <tr><td><strong>Beach Villa Main Bedroom Key</strong></td><td>10</td><td>Coffre électronique, manteau d'hiver, conteneur d'arme premium</td></tr>
                <tr><td>Beach Villa Storage Key</td><td>10</td><td>Coffre, conteneur d'arme moyen, valise</td></tr>
                <tr><td>Factory Dressing Room Key</td><td>15</td><td>2 boîtes d'arme longue, 2 tenues de travail, sac de sport, coffre</td></tr>
                <tr><td>Factory File Room Key</td><td>15</td><td>Coffre, grand conteneur d'arme</td></tr>
                <tr><td>Radar Station Security Room Key</td><td>15</td><td>Conteneur d'arme longue, tenue de travail, boîte à outils Pro</td></tr>
                <tr><td>Staff Dormitory Key</td><td>15</td><td>Coffre, manteau d'hiver, sac de sport</td></tr>
                <tr><td>Valley Village Office Key</td><td>15</td><td>Ordinateur, First-Aid Case</td></tr>
                <tr><td>RV Camp Cabin Cafeteria Key</td><td>15</td><td>Coffre, boîte d'arme longue, classeur</td></tr>
                <tr><td>Courtyard Basement Key</td><td>10</td><td>Coffre, ordinateur, valise</td></tr>
                <tr><td>Abandoned Shack Key</td><td>5</td><td>Boîte à documents, boîte de munitions, Military Supply Case</td></tr>
              </tbody>
            </table>
          </div>
          <h3>Armory</h3>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Clé</th><th>Durabilité</th><th>Contenu</th></tr></thead>
              <tbody>
                <tr><td><strong>Command Room Entry Keycard</strong></td><td>30</td><td>Coffre électronique + instruments électroniques sur les tables</td></tr>
                <tr><td>Command Room Exit Keycard</td><td>30</td><td>Sacs et électronique (souvent 2 clés en circulation)</td></tr>
                <tr><td>Weapon Storage Keycard</td><td>30</td><td>Racks d'armes de l'armurerie</td></tr>
                <tr><td>Equipment Storage Key</td><td>25</td><td>Stockage d'équipement G3, 1ᵉʳ étage</td></tr>
                <tr><td>Private Lounge Key</td><td>15</td><td>Spawns premium</td></tr>
                <tr><td>Second Floor Lounge Key</td><td>15</td><td>Spawns premium</td></tr>
                <tr><td>Sluice No. 2 Key</td><td>3</td><td>Usage unique</td></tr>
              </tbody>
            </table>
          </div>
          <h3>TV Station</h3>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Clé</th><th>Durabilité</th><th>Contenu</th></tr></thead>
              <tbody>
                <tr><td><strong>2F General Office Card</strong></td><td>10</td><td>2 manteaux, PC, boîte à documents, valise, coffre, grand conteneur de matériaux</td></tr>
                <tr><td>Planning Room Key</td><td>10</td><td>Valise de business, PC militaire, Military Supply Case, coffre électronique, Tactical Accessory Case, boîte à documents</td></tr>
                <tr><td>Editing Room Key</td><td>10</td><td>Coffre électronique, boîte à documents, conteneur d'arme + 1 bureau</td></tr>
                <tr><td>Infirmary Key</td><td>15</td><td>Tactical Accessory Case, conteneur d'arme longue, 2 Military Supply Case, tenue de travail</td></tr>
                <tr><td>Darkroom Key</td><td>15</td><td>Tactical Accessory Case, PC, boîte à documents, coffre</td></tr>
                <tr><td>Post Production Room Key</td><td>10</td><td>Spawns premium</td></tr>
                <tr><td>2F Directors Office Card</td><td>10</td><td>Spawns premium</td></tr>
                <tr><td>Backstage Passage Area Key</td><td>10</td><td>Spawns premium</td></tr>
                <tr><td>Warehouse Storage Key</td><td>10</td><td>Conteneurs</td></tr>
                <tr><td>Backup Pump Room Key</td><td>25</td><td>Matériel technique</td></tr>
                <tr><td>Parking Lot Storage Room Key</td><td>25</td><td>Zone de parking</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Les durabilités varient selon les sources</h4>
            <p>Les valeurs ci-dessus proviennent des bases communautaires (wiki ABI et cartes interactives) et <strong>divergent parfois</strong> d'une version à l'autre — notamment sur TV Station. Traitez-les comme des ordres de grandeur et vérifiez la durée affichée sur la fiche de la clé dans votre client.</p>
          </div>

          <h2 id="universelles">3. Clés universelles et porte-clefs</h2>
          <ul>
            <li><strong>Clé universelle</strong> — ouvre n'importe quelle porte, n'importe quelle carte, mais <strong>une seule fois</strong>. La carte et la difficulté ne changent rien à ce comportement. Certaines sont des objets limités dans le temps (les <strong>Twitch Drops</strong> de la S7 par exemple).</li>
            <li><strong>Chaîne de carte d'accès universelle</strong> — trouvée en raid, elle est <strong>essayée en premier</strong> quand vous déverrouillez une porte. En pratique, c'est un « essayez-moi d'abord » qui augmente le taux de réussite.</li>
            <li><strong>Porte-clefs standard (5×3)</strong> — fourni avec les <strong>Privilèges Élite Premium</strong> depuis avril 2025 ; sorti du magasin en novembre 2024. On peut aussi obtenir un porte-clefs 2×3 en échangeant avec le contact <strong>Evita</strong> en le faisant monter de niveau.</li>
            <li>Les <strong>cartes d'identité de mission</strong> (Bodyguard Captain ID Card) sont un cas particulier : elles ne s'achètent pas, elles se récupèrent dans le monde (Motel de Farm, conteneurs ou corps de boss).</li>
          </ul>

          <h2 id="rentabilite">4. Calculer la rentabilité d'une clé</h2>
          <div class="callout callout-success">
            <h4>La formule</h4>
            <p><strong>Ouvertures restantes = durée ÷ coût par mode</strong>, puis <strong>ROI = (valeur moyenne du contenu × ouvertures restantes) − prix d'achat</strong>.</p>
            <p>Exemple : une clé à 30 points achetée 500 000 Koen, utilisée en Normal (30 ouvertures), contenu moyen estimé à 40 000 Koen → 1 200 000 Koen de loot brut pour 500 000 investis. C'est un retour de 140 %… à condition de <strong>survivre à chaque extraction</strong>. C'est là que le calcul se casse.</p>
          </div>
          <ul>
            <li>Les <strong>clés de zone à fort loot</strong> sont les plus rentables ; une clé d'un endroit vide est une perte sèche.</li>
            <li>Le coût <strong>opérationnel</strong> compte : munitions, médical et temps de raid. La clé n'est qu'une partie du ROI.</li>
            <li>Les clés de <strong>TV Station</strong> s'achètent cher (1 500 à 2 700 K) mais contiennent le loot le plus dense : le ratio est là.</li>
            <li>Les clés de <strong>Farm</strong> (Motel Main Guest Room à 5 000 K) sont chères mais ouvrent <strong>deux coffres</strong> — le meilleur rapport contenu/prix du jeu.</li>
          </ul>

          <h2 id="conseils">5. Conseils d'exploitation</h2>
          <ul>
            <li><strong>Emportez la clé, pas l'inventaire</strong> : une clé dans un conteneur fermé ne vous sert à rien si vous mourez.</li>
            <li><strong>Portez la clé loin de votre slot principal</strong> : en cas de mort, les objets « marqués » (clé, carte d'identité) sont plus souvent conservés.</li>
            <li><strong>Ouvrez tôt, extrayez tard</strong> : une clé ouverte en début de raid est un loot garanti ; une clé ouverte à T-2 minutes est un piège.</li>
            <li><strong>Le vault / case sécurisée</strong> : ne mettez pas votre clé la plus rentable dedans, vous ne pourrez pas l'utiliser.</li>
            <li>En <strong>Infected Zone</strong>, une clé ouvre une salle… mais la horde peut être dedans. Prévoyez le kit de fights.</li>
          </ul>
          <div class="callout callout-danger">
            <h4>Le plafond de valeur d'équipement</h4>
            <p>Les notes bêta de la S7 mentionnent un <strong>plafond de 900 000 Koen de valeur d'équipement en Lockdown</strong> (y compris l'Infected Zone) : seules les protections et pénétrations de niveau 5 et inférieur y sont autorisées. À vérifier dans le jeu, mais cela contraint directement le budget « clé + armure + munitions » d'un raid Lockdown.</p>
          </div>
          <p>Pour le loot contenu derrière ces portes, voir <a href="items-valeur.html">le guide de la valeur</a> et <a href="map-farm.html">le guide de la carte Farm</a>.</p>
"""

page('items-cles.html',
     "Clés & Accès",
     "Guide des clés ABI Saison 7 : toutes les clés de Farm, Valley, Armory et TV Station avec leur contenu, l'usure par mode, les clés universelles et le calcul de rentabilité.",
     "../img/items/keys.jpg",
     "Objets — Clés", "Clés & Accès",
     "Durabilité, ROI, clés universelles : le seul investissement d'ABI qui rapporte à chaque usage.",
     cles,
     [("fonctionnement", "1. Fonctionnement"), ("par-carte", "2. Clés par carte"), ("universelles", "3. Clés universelles"),
      ("rentabilite", "4. Rentabilité"), ("conseils", "5. Conseils")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ───────────────────────────────────────────── 4. VALEUR
valeur = """
          <figure class="page-figure">
            <img src="../img/items/red-drop.jpg" alt="Objet rare rouge dans un coffre ouvert" loading="lazy">
            <figcaption>La valeur se joue à deux endroits : ce que vous emportez, et ce que vous décidez de garder ou de vendre.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Règle n°1</span><span class="fact-value">5 000 Koen minimum par slot</span></div>
            <div class="fact"><span class="fact-label">Red S7</span><span class="fact-value">Elysium ≈ 4,5 M Koen</span></div>
            <div class="fact"><span class="fact-label">Red max</span><span class="fact-value">Document Secret ≈ 16–17 M realizables</span></div>
            <div class="fact"><span class="fact-label">Marchand</span><span class="fact-value">Cargaison mystère : 70 K → 550 K</span></div>
          </div>

          <h2 id="regles">1. Les règles de la valeur</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Règle</th><th>Formulation</th><th>Pourquoi</th></tr></thead>
              <tbody>
                <tr><td><strong>La règle du slot</strong></td><td>Viser <strong>5 000 Koen par case d'inventaire</strong></td><td>Un objet 1×1 à 10 000 K vaut plus qu'un 4×1 à 20 000 K : les slots sont la vraie monnaie</td></tr>
                <tr><td><strong>La règle du barter</strong></td><td>Ne take que le barter à <strong>8 000 K+ par slot</strong></td><td>Ruban adhésif (800), allumettes (400), vis (600) : remplissage de slots pour rien</td></tr>
                <tr><td><strong>La règle du kit</strong></td><td><strong>Max 20 %</strong> de votre stash dans une sortie</td><td>500 K de banque → 100 K max de kit ; sinon une mort ruine votre économie</td></tr>
                <tr><td><strong>La règle de vente</strong></td><td>Marché &gt; Contact</td><td>Le marché paie 20 à 30 % de plus sur les clés, l'électronique et le violet/or ; mais sous 4 000 K, vendez au contact</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="reds">2. Les red drops de la Saison 7</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Objet</th><th>Catégorie</th><th>Valeur (Koen)</th><th>Où l'obtenir</th></tr></thead>
              <tbody>
                <tr><td><strong>Elysium</strong></td><td>Objet de valeur</td><td>≈ 4 500 000</td><td><strong>Zones infectées</strong> — garanti en fin de série de missions zombies</td></tr>
                <tr><td>Carte graphique</td><td>Électronique</td><td>≈ 3 200 000</td><td>Red Tier électronique classique, toujours au sommet</td></tr>
                <tr><td><strong>Laptop MRID</strong></td><td>Électronique</td><td>≈ 2 800 000</td><td>Luxury Gift Box MRID, boîtes à mystery cargo, butin Kamona Investigation</td></tr>
                <tr><td>Northern Stars</td><td>Objet de valeur</td><td>≈ 2 200 000</td><td>Collectible rouge S7</td></tr>
                <tr><td>Luth à double manche</td><td>Objet de valeur</td><td>≈ 1 800 000</td><td>Joue une mélodie en raid</td></tr>
                <tr><td>Flûte de jade émeraude</td><td>Objet de valeur</td><td>≈ 1 600 000</td><td>Joue une mélodie en raid</td></tr>
                <tr><td>Circuit militaire</td><td>Électronique</td><td>≈ 1 500 000</td><td>Red Tier électronique</td></tr>
                <tr><td>Lingot d'or</td><td>Objet de valeur</td><td>≈ 1 200 000</td><td>Coffres très rares, boss</td></tr>
                <tr><td><strong>Chaotic Matter</strong></td><td>Red drop</td><td>—</td><td><strong>Sur toutes les cartes en S7</strong> (il était exclusif à Distorted Valley, carte retirée cette saison)</td></tr>
                <tr><td>Lunar Soil Sample</td><td>2×2</td><td>≈ 780 000</td><td>Coffres sur toutes les cartes, jusqu'au 9 novembre 2026 — aussi récompensé par l'événement Fame and Fortune</td></tr>
                <tr><td><strong>Document Secret</strong></td><td>1×2, 0,11 kg</td><td><strong>≈ 16 000 000 – 17 000 000</strong> réalisables</td><td>Affiché ≈ 23,9 M mais vendu ~16–17 M au contact</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Le piège du Document Secret</h4>
            <p>La valeur <strong>affichée</strong> (≈ 23,9 M) et la valeur <strong>encaissée</strong> (≈ 16–17 M) ne sont pas la même chose : les Contacts ne paient jamais le prix affiché. Et les rapports de la communauté sont rares : un joueur a trouvé son premier après 2 200 heures de jeu, un autre en a cinq après 1 700 heures et zéro. C'est le loot le plus rare du jeu.</p>
          </div>

          <h3 class="mt-lg">Catalogue interactif — tous les objets suivis</h3>
          <p class="text-muted">Tri automatique par rareté puis par valeur. Les « Nouveau » sont les ajouts de la Saison 7.</p>
          <div class="items-grid"></div>

          <h2 id="reds-limites">3. Les red drops à durée limitée</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Objet</th><th>Période</th><th>Comment</th></tr></thead>
              <tbody>
                <tr><td>Stallion Wave Chaser</td><td>27 août → 30 septembre 2026</td><td>Chance dans un coffre sur n'importe quelle carte</td></tr>
                <tr><td>Fading Dawn</td><td><strong>29 octobre → 25 novembre 2026</strong></td><td>Chance dans les coffres, n'importe quelle carte</td></tr>
                <tr><td>Corrupted Clock</td><td><strong>29 octobre → 25 novembre 2026</strong></td><td><strong>Craftable</strong> dans la Trophy Room à partir d'objets corrompus trouvés sur toutes les cartes</td></tr>
                <tr><td>Pegasus</td><td>Février 2026</td><td>Red drop évolutif : donnait de l'XP de kills et de butin en Lockdown/Forbidden</td></tr>
                <tr><td>Crown of Glory</td><td>Juillet 2026</td><td>Collaboration Resident Evil</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="marchand">4. Le marchand de terrain : la valeur pendant le raid</h2>
          <p>Le marchand de terrain (1 par raid, disponible 5 minutes après le début) est la nouveauté économique majeure de la S7. Il permet de <strong>convertir du loot en valeur sans extraire</strong>.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Offre</th><th>Prix (Koen)</th><th>Commentaire</th></tr></thead>
              <tbody>
                <tr><td>Mystery Cargo</td><td>70 000</td><td>Le ticket d'entrée : rendu moyen, risque faible</td></tr>
                <tr><td>Uncommon Mystery Cargo</td><td>250 000 – 350 000</td><td>Zone de risque</td></tr>
                <tr><td>Rare Collectibles</td><td>450 000</td><td>Le butin rare, à prix fort</td></tr>
                <tr><td>Rare Mystery Cargo</td><td>470 000 – 550 000</td><td>Le haut de gamme, potentiellement un red</td></tr>
                <tr><td>Rare Medical Supplies</td><td>480 000</td><td>Soins haut de gamme</td></tr>
                <tr><td>Uncommon Military Items</td><td>250 000</td><td>Matériel militaire</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Comment jouer le marchand</h4>
            <p><strong>Vendre</strong> d'abord : indulgez le loot encombrant et peu coûteux pour libérer des slots avant d'extraire — chaque slot libéré est un slot pour un red. <strong>Acheter</strong> ensuite : les cargaisons chères sont une loterie assumée, les cargaisons à 70 K sont un rendement quasi garanti. Le <strong>volume de transactions</strong> (ventes + achats) débloque de l'<strong>intel</strong> sur la carte et les objets : plus vous tradez, plus vous voyez venir les opportunités.</p>
          </div>

          <h2 id="smelter">5. Le smelter / Trash to Treasure</h2>
          <p>Le smelter est un appareil qui apparaît <strong>en raid</strong> : vous y déposez <strong>3 objets divers</strong> et il en ressort un objet de meilleure qualité. Vous dispose de <strong>3 tentatives par raid</strong>.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Valeur totale des 3 objets</th><th>Résultat possible</th></tr></thead>
              <tbody>
                <tr><td>Moins de 45 000</td><td>Objet violet bon marché — perte sèche</td></tr>
                <tr><td>45 000 et plus</td><td>Zone de profit : c'est le seuil minimum</td></tr>
                <tr><td>200 000 et plus</td><td>1 chance de sortie rouge</td></tr>
                <tr><td>300 000 et plus</td><td><strong>2 chances de sortie rouge</strong></td></tr>
                <tr><td>3 objets violets identiques</td><td>Chance d'obtenir le <strong>Luminous Rose</strong> (S6)</td></tr>
                <tr><td>3 objets or identiques</td><td>1 chance de sortie rouge, quelle qu'en soit la valeur</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>La règle qui casse tout : rien ne s'importe</h4>
            <p>Depuis la S7, on <strong>ne peut pas bring des matériaux de l'extérieur</strong> dans le raid. Un objet « supplied » n'est pas accepted par le smelter : il faut l'avoir trouvé pendant ce raid. Et les objets <strong>qualité or</strong> ne peuvent même pas être transportés dans un raid — il faut donc les trouver sur place pour les fondre.</p>
            <p>Formule en cours : <strong>29 octobre → 15 novembre 2026</strong>, PDA + Data Cable + Laptop → <strong>Prototype Calculation Module</strong>. Autres rotations : 15–28 octobre (module de localisation de cible), 16–27 septembre (Horloge de Phaethon), 13–26 août (caméra vidéo plaquée or).</p>
          </div>

          <h2 id="priorites">6. Priorité de loot sur le terrain</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Priorité</th><th>Quoi</th><th>Où</th></tr></thead>
              <tbody>
                <tr><td><strong>1</strong></td><td>Objets de valeur : lingot d'or (200 000 – 250 000)</td><td>Coffres très rares, boss</td></tr>
                <tr><td><strong>2</strong></td><td>Électronique : carte graphique, laptop MRID</td><td>Armory (Command Room), TV Station (Planning Room)</td></tr>
                <tr><td><strong>3</strong></td><td>Red drops / collectibles rouges</td><td>Coffres, boîte à mystery cargo, boss</td></tr>
                <tr><td><strong>4</strong></td><td>Barter à fort rendement : poudre rouge (45 000)</td><td>Armureries, caisses de matériel</td></tr>
                <tr><td><strong>5</strong></td><td>Clés et cartes d'accès</td><td>Corps, conteneurs, boss</td></tr>
                <tr><td>6</td><td>Munitions (si vous tirez ce calibre)</td><td>Caisses à munitions</td></tr>
                <tr><td>7</td><td>Fill : ruban adhésif, allumettes, vis</td><td>—</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Ne ramassez pas tout</h4>
            <p>Le réflexe « aspirateur » est l'erreur numéro un. Les objets sans usage dans votre sac occupent des slots, ralentissent votre course, augmentent le poids et transforment une extraction réussie en Extraction Impossible. Chaque slot laissé vide est un slot pour un red.</p>
          </div>

          <h2 id="marche">7. Vendre : Contact ou Marché ?</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Le Marché</h3>
              <p class="card-text">Pour tout ce qui vaut plus de 4 000 Koen : clés, électronique, objets violets et or, armes. Prix jusqu'à 20–30 % au-dessus du contact. 12 slots par dépôt, 500 objets par semaine.</p>
              <p class="card-text mt-sm">Astuce : vendez <strong>légèrement en dessous du prix le plus bas du marché</strong> pour écouler vite, et <strong>entre le plancher et le prix moyen</strong> pour maximiser.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Les Contacts</h3>
              <p class="card-text">Pour tout ce qui vaut moins de 4 000 Koen : les transactions sont immédiates, sans frais de liste, et alimentent la fidélité du contact qui améliore ses prix et ses stocks.</p>
              <p class="card-text mt-sm">Astuce : <strong>Deke Vinson</strong> réapprovisionne toutes les 2 à 3 heures. Ses articles de barter sont souvent sous-évalués : acheté 20 000 K, revendu 67 000 K au marché, c'est 47 000 K de profit.</p>
            </div></div>
          </div>
          <p>Pour la boucle complète de profit, voir <a href="items-koen-economy.html">le guide Koen &amp; économie</a>. Pour ranger vos red drops, voir <a href="items-collection-room.html">la Collection Room</a>.</p>
"""

page('items-valeur.html',
     "Valeur des objets",
     "Guide de la valeur ABI Saison 7 : red drops (Elysium 4,5M, MRID), Document Secret, marchands et cargaisons mystères, smelter Trash to Treasure et règles de slot.",
     "../img/items/red-drop.jpg",
     "Objets — Valeur", "Valeur des objets",
     "Le Document Secret, l'Elysium, le smelter et la règle des 5 000 Koen par slot : tout ce qui compte côté economie.",
     valeur,
     [("regles", "1. Règles de la valeur"), ("reds", "2. Red drops S7"), ("reds-limites", "3. Drops limités"),
      ("marchand", "4. Marchand de terrain"), ("smelter", "5. Smelter"), ("priorites", "6. Priorité de loot"),
      ("marche", "7. Vendre")],
     extra_js='items', nav=NAV, crumb=CRUMB)

print("OK S9 batch B")
