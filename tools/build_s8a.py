import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Saison 7')
CRUMB = ('Saison 7', 'saison7-utopia.html')

# ─────────────────────────────────────────────── 1. HUB
hub = """
          <figure class="page-figure">
            <img src="../img/events/s7-utopia-keyart.jpg" alt="Key art Saison 7 Utopia - Kamona contaminée" loading="lazy">
            <figcaption>Utopia — le réactif Utopia s'est répandu dans les zones clés de Kamona. Saison lancée le 16 septembre 2026 (patch 1.0.0.142.19+).</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Lancement</span><span class="fact-value">16 septembre 2026</span></div>
            <div class="fact"><span class="fact-label">Patch</span><span class="fact-value">1.0.0.142.19+</span></div>
            <div class="fact"><span class="fact-label">Thème</span><span class="fact-value">Biohazard — l'Utopia reagent contamine Kamona</span></div>
            <div class="fact"><span class="fact-label">Reset</span><span class="fact-value">Rang de saison + missions uniquement</span></div>
          </div>

          <h2 id="bref">1. La saison en bref</h2>
          <p><strong>Utopia</strong> est la saison la plus structurante de l'histoire d'ABI. Elle introduit pour la première fois un <strong>vrai mode zombie</strong> — deux modes distincts — tout en réécrivant le cœur du combat PvP : portées effectives augmentées, headshots renforcés, plafonds d'équipement par mode et suppression du <strong>RNG de pénétration</strong> sur les armures de classe V et VI.</p>
          <p>Le compte n'est pas wipe. Votre stash, vos Koen, votre niveau de personnage et vos Bonds sont <strong>conservés</strong>. Seuls le rang de saison et la progression des missions / Battle Pass repartent de zéro — l'échelle que vous gravissez <em>pendant</em> la saison, pas votre compte.</p>

          <h2 id="nouveautes">2. Les 10 nouveautés majeures</h2>
          <div class="grid grid--2">
            <article class="card reveal">
              <div class="card-media"><img src="../img/zombies/infected-zone.jpg" alt="Infected Zone" loading="lazy"></div>
              <div class="card-body">
                <h3 class="card-title">Zone infectée <span class="badge badge-s7">PvPvE</span></h3>
                <p class="card-text">Extraction classique augmentée de 6 types de mutants sur Farm, Valley et Airport. Progression par échantillons via Zombie Research.</p>
                <div class="card-meta"><a class="btn btn-biohazard btn-sm" href="saison7-zombie-infected-zone.html">Guide complet</a></div>
              </div>
            </article>
            <article class="card reveal">
              <div class="card-media"><img src="../img/zombies/zombie-endless.jpg" alt="Zombie Endless" loading="lazy"></div>
              <div class="card-body">
                <h3 class="card-title">Zombie Endless <span class="badge badge-s7">PvE</span></h3>
                <p class="card-text">Survie en équipe de 1 à 4 sur l'Airport dès le niveau 8. Loadout imposé, mort définitive, progression par Merit.</p>
                <div class="card-meta"><a class="btn btn-biohazard btn-sm" href="saison7-zombie-endless.html">Guide complet</a></div>
              </div>
            </article>
            <article class="card reveal">
              <div class="card-media"><img src="../img/events/s7-nouveautes.jpg" alt="A545 et AK-15SC" loading="lazy"></div>
              <div class="card-body">
                <h3 class="card-title">2 armes + 4 season kits</h3>
                <p class="card-text">L'A545 rejoint le sommet du meta aux côtés du U191 et du H416. L'AK-15SC écrase le close-to-mid. Quatre kits saisonniersenian inaugurent le concept.</p>
                <div class="card-meta"><a class="btn btn-primary btn-sm" href="armes-nouveautes-s7.html">Les builds S7</a></div>
              </div>
            </article>
            <article class="card reveal">
              <div class="card-media"><img src="../img/zombies/balance-pvp.jpg" alt="Balance changes" loading="lazy"></div>
              <div class="card-body">
                <h3 class="card-title">Le rééquilibrage majeur</h3>
                <p class="card-text">Plafonds d'équipement par mode, RNG T5/T6 supprimé, headshots plus payants, flashlights nerfed, TTK global allongé.</p>
                <div class="card-meta"><a class="btn btn-primary btn-sm" href="saison7-balance-changes.html">Détail des patchs</a></div>
              </div>
            </article>
          </div>

          <h2 id="balance">3. Ce qui change dans CHAQUE raid</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Changement</th><th>Effet concret</th><th>Impact</th></tr></thead>
              <tbody>
                <tr><td><strong>Portée effective augmentée</strong></td><td>Les armes conservent leurs dégâts plus loin</td><td>Fusils redeviennent pertinents en zone ouverte</td></tr>
                <tr><td><strong>Headshots renforcés</strong></td><td>Récompense plus régulière pour les tirs à la tête</td><td>La précision vaut plus que le volume</td></tr>
                <tr><td><strong>Plafond par mode</strong></td><td>Normal : T4 et moins · Lockdown : T5 et moins</td><td>Fini le hot-drop en kit rouge contre des déshérités</td></tr>
                <tr><td><strong>RNG T5/T6 supprimé</strong></td><td>Pas de « chance » de percer le haut de gamme</td><td>Duels d'armure déterministes, TTK au torse plus long</td></tr>
                <tr><td><strong>Ricochets supprimés</strong></td><td>Plus de rebond sur casques et masques</td><td>Durabilité T5/T6 perdue plus vite</td></tr>
                <tr><td><strong>Flashlight nerfé</strong></td><td>Éclairage réduit, ergonomie à -7</td><td>Fin de l'aveuglement garanti</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>La règle d'or de la saison</h4>
            <p>Le <strong>Pierce Level</strong> d'une munition vaut <code>plancher(Pénétration ÷ 10)</code> et se compare au <strong>Niveau d'armure</strong> de la plaque visée. Sous le RNG supprimé : pas de niveau de pénétration, pas de percée. Vérifiez vos calibres avant chaque sortie.</p>
          </div>

          <h2 id="modes">4. Les trois modes à distinguer</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Type</th><th>Cartes</th><th>Progression</th></tr></thead>
              <tbody>
                <tr><td><strong>Infected Zone</strong></td><td>PvPvE extraction</td><td>Farm (Heavy), Valley (standard), Airport (Heavy)</td><td>Zombie Research</td></tr>
                <tr><td><strong>Zombie Endless</strong></td><td>PvE survie</td><td>Airport (débloqué niveau 8)</td><td>Merit → capacités</td></tr>
                <tr><td><strong>No Man's Land</strong></td><td>PvE entraînement</td><td>Zone d'entraînement (billets)</td><td>Échantillons zombies</td></tr>
                <tr><td><strong>Tactical Ops</strong></td><td>PvP extraction</td><td>Toutes les cartes, hors zones contaminées</td><td>Rang de saison, Koen</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="economie">5. L'économie change de visage</h2>
          <ul>
            <li><strong>Marchand de terrain in-raid</strong> — présent en jeu principal <em>et</em> en zone infectée : 1 marchand par raid, disponible 5 minutes après le début. Vous vendez du loot pour libérer du sac, vous achetez des cargaisons mystères, et le volume de transactions débloque de l'<strong>intel</strong> sur la carte.</li>
            <li><strong>Cargaison mystère</strong> — prix bas = rendement stable ; prix élevé = jackpot ou perte sèche. C'est un pari, pas un achat.</li>
            <li><strong>Elysium</strong> — nouveau drop rouge de l'Infected Zone, d'une valeur équivalente à l'Utopia. La série de missions zombies le garantit à son terme.</li>
            <li><strong>Amélioration Blueprint</strong> — nouveau matériau de recherche obtenu en raid (plus fréquent dans les boîtes à documents, vêtements, tiroirs). Les recettes apprises offrent un buff unique, <strong>valable uniquement la saison en cours</strong>.</li>
            <li><strong>Trash to Treasure</strong> — l'événement de fonte revient : votre loot bas-grade se transforme en stuff.</li>
          </ul>

          <h2 id="agenda">6. Agenda de la saison</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Date</th><th>Événement</th><th>Détail</th></tr></thead>
              <tbody>
                <tr><td>16 sept. 2026</td><td><strong>Lancement Utopia</strong></td><td>Patch 1.0.0.142.19+, deux modes zombies, pass saisonnier</td></tr>
                <tr><td>24 sept. 2026</td><td>Festival Biohazard & Automne</td><td>Check-inAutomne, boutique, Défi de Vinson, Lunar Soil Sample</td></tr>
                <tr><td>28 sept. 2026</td><td>Boutique & Défi d'Automne</td><td>Patrouille de zone sombre, Vinson's Challenge, décompte des points</td></tr>
                <tr><td>29 oct. → 7 déc. 2026</td><td><strong>Warlord Tournament 3</strong></td><td>Classement sur la valeur du loot, 400 K minimum de gear + 50 K de ticket</td></tr>
                <tr><td>Hebdo (lun. 5 h UTC)</td><td>Missions & Défi de Merit</td><td>Meilleur Merit de la semaine = 3× Koen, jusqu'à 3 000 000 K/semaine</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="faq">7. FAQ — ce que la communauté demande</h2>
          <h3>Est-ce que la saison wipe mon compte ?</h3>
          <p>Non. Stash, Koen, niveau de personnage et Bonds sont intacts. Seuls le rang de saison et les missions / Battle Pass sont remis à zéro.</p>
          <h3>Quel niveau pour le Zombie Endless ?</h3>
          <p>Niveau 8. L'entrée coûte des Koen, sans limite de nombre de parties. L'équipe compte 1 à 4 joueurs ; si un opérateur tombe, il reste <strong>downed définitivement</strong> pour le reste de la raid.</p>
          <h3>Peut-on reset la Zombie Research ?</h3>
          <p>Non. Un point de recherche activé ne peut pas être remis à zéro. Les liens entre points indiquent les prérequis : s'il y en a plusieurs, un seul suffit. Choisissez dans l'ordre.</p>
          <h3>Quel est le meilleur mode pour débuter ?</h3>
          <p>No Man's Land pour apprendre sans risque, puis Endless pour l'action, puis l'Infected Zone pour l'expérience complète loot → combat → extraction avec le jeu mental biochimique.</p>
          <h3>Les boss sont-ils toujours là ?</h3>
          <p>Oui, et ils se cumulent aux mutants. Hecate (Farm), Fred (Northridge), Renoir (Armory), Kurt / Rolf / Bernard (TV Station) — plus <strong>Phobos</strong>, le boss mutant des zones infectées.</p>

          <div class="callout callout-success">
            <h4>Le plan d'action de la saison</h4>
            <p>Semaine 1 : No Man's Land pour roder les mutants, puis votre premier Infected Zone en Valley pour Constitution Research. Semaine 2 : Farm et Airport en Heavy Infected avec un squad. Semaine 3 : Zombie Endless pour le Merit et le marchand en jetons. Semaine 4 : Warlord Tournament et pass de saison.</p>
          </div>
"""

page('saison7-utopia.html',
     "Saison 7 : Utopia",
     "Saison 7 Utopia d'Arena Breakout Infinite (16 septembre 2026) : Zone infectée, Zombie Endless, A545 et AK-15SC, Zombie Research, marchand de terrain et rééquilibrage complet du PvP.",
     "../img/events/s7-utopia-keyart.jpg",
     "Saison 7 — Utopia", "Saison 7 : Utopia",
     "La contamination d'Utopia a métamorphosé Kamona. Deux modes zombies, deux armes vedettes, et un rééquilibrage qui change chaque raid.",
     hub,
     [("bref", "1. En bref"), ("nouveautes", "2. Les nouveautés"), ("balance", "3. Le rééquilibrage"),
      ("modes", "4. Les modes"), ("economie", "5. L'économie"), ("agenda", "6. Agenda"), ("faq", "7. FAQ")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ─────────────────────────────────────────────── 2. INFECTED ZONE
infected = """
          <figure class="page-figure">
            <img src="../img/zombies/infected-zone.jpg" alt="Zone infectée de Kamona sous bio-hazard" loading="lazy">
            <figcaption>Infected Zone — PvPvE : les mutants arpentent les zones contaminées de Kamona en même temps que les autres squads.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Type</span><span class="fact-value">PvPvE extraction</span></div>
            <div class="fact"><span class="fact-label">Cartes</span><span class="fact-value">Farm · Valley · Airport</span></div>
            <div class="fact"><span class="fact-label">Difficulté</span><span class="fact-value">Heavy sur Farm et Airport, standard sur Valley</span></div>
            <div class="fact"><span class="fact-label">Progression</span><span class="fact-value">Zombie Research (échantillons extraits)</span></div>
          </div>

          <h2 id="principe">1. Le principe</h2>
          <p>L'<strong>Infected Zone</strong> prend le raid d'extraction classique et y ajoute des <strong>mutants</strong> — IA infectée qui chasse, occupe des positions et contamine le terrain. Le loot, les extractions, le marchand : tout le reste fonctionne comme en Tactical Ops. Seuls les modes et les boss changent.</p>
          <div class="callout callout-biohazard">
            <h4>Répartition de la contamination</h4>
            <p><strong>Farm</strong> et <strong>Airport</strong> basculent en <em>Heavy Infected Zone</em> (remplaçant respectivement Forbidden Zone et Forbidden Zone). <strong>Valley</strong> passe en <em>Infected Zone</em> standard (à la place de Lockdown Zone) et gagne de nouvelles conditions météo : nuit pluvieuse, nuit, brouillard, soleil, pluie.</p>
          </div>

          <h2 id="mutants">2. Les 6 mutants — fiche par fiche</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mutant</th><th>Comportement</th><th>Effet</th><th>Priorité</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal Mutant</strong></td><td>Saute et sprinte vers les_OPERATORs</td><td>Aucun effet de zone</td><td>Évitable — coupez la route, ne tirez pas</td></tr>
                <tr><td><strong>Reaper</strong></td><td>Crache son tissu mutant à distance, depuis un point haut</td><td>Vert : flaque d'acide · Jaune : marais ralentissant · Gris : fumée qui bloque la vue</td><td><strong>1</strong> — tuez-le en premier</td></tr>
                <tr><td><strong>Ambusher</strong></td><td>Bondit sur sa cible, la cloue au sol et ne lâche plus</td><td>Suppression continue</td><td><strong>2</strong> — jamais à portée de mêlée</td></tr>
                <tr><td><strong>Bloater</strong></td><td>Lent, il gonfle puis explose</td><td>Vert : poison · Jaune : ralentissement · Gris : flash aveuglant</td><td><strong>3</strong> — tuez avant le contact</td></tr>
                <tr><td><strong>Breacher</strong></td><td>Charge à vitesse folle, envoie les obstacles en l'air d'un coup de membre</td><td>Marteau lourd, coups brutaux en série</td><td><strong>4</strong> — terrain àugaliser</td></tr>
                <tr><td><strong>Phobos</strong></td><td>Boss. Un Breacher en armure tactique lourde, corps extrêmement résistant</td><td>Abandonne son armure quand il est mal touché et revient plus furieux</td><td><strong>Boss</strong> — engagement d'objectif</td></tr>
              </tbody>
            </table>
          </div>

          <figure class="page-figure">
            <img src="../img/zombies/mutant-reaper.jpg" alt="Reaper crachant son slime corrosif" loading="lazy">
            <figcaption>Reaper — il tire son acide à distance et depuis les hauteurs. La bave au sol persiste : ne combattez jamais dans la zone qu'il crée.</figcaption>
          </figure>

          <h2 id="ordres">3. Ordre d'élimination</h2>
          <p>La communauté a très vite identifié une hiérarchie de priorité, qui diffère selon que vous jouez solo ou en groupe :</p>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">En squad</h3>
              <p class="card-text"><strong>Reaper &gt; Ambusher &gt; Bloater &gt; Normal &gt; Breacher</strong></p>
              <p class="card-text mt-sm">En équipe, le Reaper est le plus dangereux : son acide transforme la carte en champ de mines. Le Breacher passe en dernier car il est prévisible et se laisse canaliser.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">En solo</h3>
              <p class="card-text"><strong>Ambusher &gt; Reaper &gt; Bloater &gt; Normal &gt; Breacher</strong></p>
              <p class="card-text mt-sm">Seul, l'Ambusher passe devant : il ne lâche jamais sa cible et vous transforme en statue pendant qu'il vous vide. Le Reaper passe deuxième car il vous one-shot au-delà du niveau 4 si la bave vous prend.</p>
            </div></div>
          </div>
          <div class="callout callout-warning">
            <h4>Ne tirez pas sur tout ce qui bouge</h4>
            <p>« Le bruit est une ressource. » Chaque détonation attire des horde de mutants et révèle votre position aux autres squads. Si un zombie ne bloque pas votre route et ne vous menace pas : <strong>contournez-le</strong>. Réservez vos munitions aux Opérateurs, aux mutants dangereux, aux zombies qui bloquent un passage et à la protection de votre extraction.</p>
          </div>

          <figure class="page-figure">
            <img src="../img/zombies/mutant-bloater.jpg" alt="Bloater mutant gonflé diffusant un nuage toxique" loading="lazy">
            <figcaption>Bloater — lent, il gonfle puis explose. Vert : poison · Jaune : ralentissement · Gris : flash aveuglant. Tuez-le avant le contact, ou quittez la zone immediatement.</figcaption>
          </figure>

          <figure class="page-figure">
            <img src="../img/zombies/mutant-phobos.jpg" alt="Phobos, boss mutant lourdement blindé" loading="lazy">
            <figcaption>Phobos — le boss des zones infectées. Armure tactique lourde, il l'abandonne quand il est mal touché et revient plus enragé.</figcaption>
          </figure>

          <h2 id="items">4. Les nouveaux objets de la zone</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Objet</th><th>Effet</th><th>Usage tactique</th></tr></thead>
              <tbody>
                <tr><td><strong>Grenade phéromone</strong></td><td>Attire les mutants vers un point choisi</td><td>Ouvrir un passage, détourner un Breacher d'un couloir</td></tr>
                <tr><td><strong>Fumigène de soin</strong></td><td>Restaure progressivement la santé dans la zone</td><td>Regroupement après un combat de horde</td></tr>
                <tr><td><strong>Lance-roquettes</strong></td><td>Provoque la chute de cargaison</td><td>Faire tomber du loot lourd — et alerter tout le monde</td></tr>
                <tr><td><strong>Réactif « Pathfinder »</strong></td><td>+PV de torse temporaires</td><td>Mais + dégâts subis des mutants et détection facilitée</td></tr>
                <tr><td><strong>Réactif « Messenger »</strong></td><td>+vitesse de déplacement temporaire</td><td>Même contrepartie : plus de dégâts subis, plus visible</td></tr>
                <tr><td><strong>Réactif de résistance</strong></td><td>Résistance aux blessures critiques</td><td>Trade le même risque : détection et dégâts augmentés</td></tr>
                <tr><td><strong>Conteneurs zombies</strong></td><td>Conteneurs shipping, distributeurs abandonnés, caisses de Indices</td><td>Exclusifs à la zone : corps de zombies, sacs, loot spécifique</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="events">5. Événements de horde et contamination</h2>
          <ul>
            <li><strong>Tirer sur les voitures de police</strong> déclenche un <strong>événement de horde</strong> : une vague de mutants arrive. Ne le faites jamais en zone de loot.</li>
            <li><strong>Certaines actions d'Operator</strong> peuvent déclencher une horde de mutants.</li>
            <li><strong>Missions in-raid exclusives</strong> : les terminer débloque des récompenses de caisses de loot.</li>
            <li>Les <strong>terminaux</strong> sont désormais plus polyvinylents : un terminal normal par squad pour un peu de XP de caisse, un terminal <strong>clandestin</strong> qui exige de tenir la position pendant que les autres squads peuvent contester — pour un gros lot de XP de caisse d'un coup.</li>
            <li><strong>Retours plus rapides</strong> en début de raid, durées qui s'allongent au fil de la partie ; <strong>larges quantités d'air-drops</strong> en milieu et fin de raid ; nouvelles <strong>unités IA en armure lourde</strong> sur les cartes.</li>
            <li>Le <strong>crafter violet</strong> (qualité Miscellaneous) est illimité mais n'accepte que les objets de qualité violette ou inférieure.</li>
          </ul>

          <figure class="page-figure">
            <img src="../img/zombies/merchant-field.jpg" alt="Marchand de terrain en mission" loading="lazy">
            <figcaption>Le marchand de terrain — 1 par raid, ouvert 5 minutes après le début. Vente de loot, cargaisons mystères, et de l'intel débloqué par le volume de transactions.</figcaption>
          </figure>

          <h2 id="marchand">6. Le marchand de terrain</h2>
          <ul>
            <li><strong>1 marchand par raid</strong>, disponible à l'interaction <strong>5 minutes après le début</strong> du raid.</li>
            <li><strong>Vendre</strong> : déposez du loot contre de la valeur — pratique pour libérer du sac avant l'extraction.</li>
            <li><strong>Acheter</strong> : cargaisons mystères. Prix bas = rendement stable, prix élevé = résultat extrême — une vraie décision de risque.</li>
            <li><strong>Intel</strong> : achats <em>et</em> ventes cumulent un volume de transactions ; atteindre un seuil débloque des renseignements sur la carte et les objets.</li>
            <li>En <strong>Infected Zone</strong>, le marchand fonctionne comme en jeu principal (valeur de loot, Koen). En <strong>Zombie Endless</strong>, il fonctionne en <strong>jetons zombies</strong>.</li>
          </ul>

          <h2 id="recherche">7. La progression Zombie Research</h2>
          <p>Les <strong>échantillons zombies</strong> récupérés en raid puis <strong>extraits</strong> sont consommés pour activer et améliorer les <strong>points de recherche</strong>. Les capacités débloquées sont <strong>permanentes en Infected Zone</strong> — mais un point activé <strong>ne peut pas être remis à zéro</strong>. Les liens entre points tracent les prérequis ; si un point a plusieurs prérequis, un seul suffit.</p>
          <p>Détail complet de l'arbre et ordres d'investissement dans <a href="saison7-zombie-research.html">le guide Zombie Research</a>.</p>

          <h2 id="checklist">8. Check-list avant d'entrer</h2>
          <ul>
            <li>Grenades phéromone et fumigène de soin dans le sac — ce sont vos outils de contrôle de horde.</li>
            <li>Molotov pour les concentrations : plusieurs mutants dans une pièce = un lancer suffit.</li>
            <li>Un slot de mêlée : les mutants normaux se tuent gratuitement à la mêlée, sans consommer de munitions.</li>
            <li>Emplacement : un seul slot pour une radio ou un casque qui coupe le bruit des pas.</li>
            <li>Un chemin de repli mental : chaque combat contre un mutant est un combat qui <em>révèle</em> votre position aux Operateurs.</li>
          </ul>
"""

page('saison7-zombie-infected-zone.html',
     "Infected Zone — La zone contaminée",
     "Infected Zone S7 d'Arena Breakout Infinite : les 6 mutants (Reaper, Ambusher, Bloater, Breacher, Phobos), ordre d'élimination, nouveaux objets, hordes et marchand de terrain.",
     "../img/zombies/infected-zone.jpg",
     "Saison 7 — Zombie", "Infected Zone",
     "Six mutants, deux niveaux de contamination, un marchand de terrain et une progression par échantillons.",
     infected,
     [("principe", "1. Principe"), ("mutants", "2. Les 6 mutants"), ("ordres", "3. Ordre d'élimination"),
      ("items", "4. Nouveaux objets"), ("events", "5. Hordes & contamination"), ("marchand", "6. Marchand de terrain"),
      ("recherche", "7. Zombie Research"), ("checklist", "8. Check-list")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ─────────────────────────────────────────────── 3. ENDLESS
endless = """
          <figure class="page-figure">
            <img src="../img/zombies/zombie-endless.jpg" alt="Aéroport infesté par la horde en mode Endless" loading="lazy">
            <figcaption>Zombie Endless — l'Airport infesté, un niveau de menace qui monte, une seule équipe de 1 à 4 opérateurs.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Type</span><span class="fact-value">PvE survie</span></div>
            <div class="fact"><span class="fact-label">Carte</span><span class="fact-value">Airport</span></div>
            <div class="fact"><span class="fact-label">Déblocage</span><span class="fact-value">Niveau 8</span></div>
            <div class="fact"><span class="fact-label">Équipe</span><span class="fact-value">1 à 4 joueurs</span></div>
            <div class="fact"><span class="fact-label">Progression</span><span class="fact-value">Merit → niveau de croissance</span></div>
            <div class="fact"><span class="fact-label">Élimination</span><span class="fact-value">Downed définitif (pas de réapparition)</span></div>
          </div>

          <h2 id="principe">1. Principe : survivre, pas extraire</h2>
          <p>Zombie Endless est le mode <strong>PvE</strong> de la saison. Vous ne risquez <em>pas</em> votre stash : le jeu vous attribue une <strong>classe</strong> au départ et un <strong>loadout initial</strong> correspondant. L'entrée coûte des Koen, <strong>sans limite</strong> de nombre de parties.</p>
          <p>Le <strong>niveau de menace</strong> monte continûment au fil de la raid : plus de mutants, plus forts. Quand tout l'effectif est mort — ou quand l'équipe choisit d'extraire activement — la raid se termine. Chaque seconde survécue = plus de <strong>Merit</strong>.</p>
          <div class="callout callout-danger">
            <h4>La règle la plus dure du jeu</h4>
            <p>Si un opérateur tombe, il passe en état <strong>downed permanent</strong> pour le reste de la raid. Pas de réapparition, pas de reprise. En solo, un mistake de Broken = la run est terminée. C'est ce qui transforme l'Airport en champ de bataille profondément asymétrique.</p>
          </div>

          <h2 id="boucle">2. La boucle de survie</h2>
          <ol>
            <li><strong>Mission d'arme</strong> — chaque niveau de menace propose un choix d'arme. Prenez-le, improvez votre équipement <em>avant</em> que les ennemis ne deviennent des éponges à balles.</li>
            <li><strong>Amélioration</strong> — achetez des améliorations de personnage et de statistiques au marchand.</li>
            <li><strong>Missions d'extermination</strong> — en les remplissant, vous obtenez des <strong>clés</strong> pour les salles verrouillées.</li>
            <li><strong>Salles verrouillées</strong> — un <strong>weapon case</strong> àopened : chance d'arme nettement plus puissante.</li>
            <li><strong>Jetons zombies</strong> — monétisés en <strong>supplies</strong> et <strong>contre-mesures</strong> tirées au sort (exclusives à la raid).</li>
          </ol>

          <figure class="page-figure">
            <img src="../img/zombies/mutant-ambusher.jpg" alt="Ambusher bondissant sur sa cible" loading="lazy">
            <figcaption>Ambusher — il bondit, verrouille sa cible et ne lâche plus. En solo, c'est la première cible à abattre.</figcaption>
          </figure>

          <h2 id="priorites">3. Priorité d'élimination</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Solo</h3>
              <p class="card-text"><strong>Ambusher &gt; Reaper &gt; Bloater &gt; Normal &gt; Breacher</strong></p>
              <p class="card-text mt-sm">L'Ambusher vous maintient en suppression jusqu'à la mort. Le Reaper vert vous one-shot au-delà du niveau 4. Les Normals se tuent au corps à corps, le Breacher se laisse canaliser.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">En squad</h3>
              <p class="card-text"><strong>Reaper &gt; Ambusher &gt; Bloater &gt; Normal &gt; Breacher</strong></p>
              <p class="card-text mt-sm">En groupe, le Reaper est prioritaire car son acide rend la carte impraticable. Attention au combo le plus dangereux : le Breacher vous charge pendant que le Reaper vous crache dans le dos.</p>
            </div></div>
          </div>
          <div class="callout callout-warning">
            <h4>Les Reapers verts tuent en un tir</h4>
            <p>Au-delà du <strong>niveau 4</strong>, un Reaper acide peut vous mettre en un coup. Arrêtez-vous de bouger, tuez-les en premier, et ne tenez jamais une position à l'intérieur d'une flaque.</p>
          </div>

          <h2 id="astuces">4. Astuces de terrain</h2>
          <ul>
            <li><strong>Conteneurs et sous l'avion</strong> : les Breachers sont trop grands pour y entrer ni pour charger. Bonus : leur tête est hors de portée — vous ne pouvez pas les tuer à la tête, donc prévoyez de la munitions.</li>
            <li><strong>Le puits de ventilation</strong> au centre de la carte (gaine d'ascenseur, salle avec un chariot élévateur) est inaccessible aux zombies, sauf à l'Ambusher qui peut sauter dedans — et perd de la taille en le faisant.</li>
            <li><strong>Ne restez pas à l'entrée</strong> : les Reapers et Ambushers vous atteignent quand même.</li>
            <li><strong>Le corps bloque la horde</strong> : un opérateur mort à un choke point suffit à ralentir les zombies qui ne franchissent pas.</li>
            <li><strong>Voitures de police</strong> : leurs sirènes s'activent à proximité et attirent des hordes. Restez à distance sauf si c'est une mission.</li>
            <li><strong>Mission « défendre la transmission »</strong> : les zombies n'attaquent pas l'équipement et priorisent les joueurs. Activez, puis occupy une position plus avantageuse.</li>
            <li><strong>Automatique de l'Airport en extérieur</strong> : il peut piéger une horde entière si le combat est perdu.</li>
            <li><strong>Shotguns = rois</strong> : dégâts de base élevés sur les zombies normaux, et ils touchent <em>plusieurs</em> ennemis d'un seul tir, là où un fusil automatique ne touche qu'un corps à la fois.</li>
            <li><strong>Niveaux 3 de grenades</strong> : phéromones et molotovs sont efficaces pour un contrôle de horde instantané. Gardez vos variantes de haut niveau pour les boss et les Reapers qui crachent.</li>
          </ul>

          <h2 id="marchand">5. Le marchand en Endless</h2>
          <ul>
            <li>Le marchand existe en Endless avec <strong>8 emplacements fixes</strong>, <strong>2 marchands par emplacement</strong>, disponibles <strong>dès le début du match</strong>.</li>
            <li>La monnaie n'est pas le Koen mais le <strong>jeton zombie</strong>.</li>
            <li>On y achète des <strong>supplies</strong> normales et des <strong>contre-mesures zombies</strong> — chaque achat de contre-mesure <strong>tire une contre-mesure exclusive à la raid</strong> au hasard.</li>
            <li>En mode Tactique Ops, on peut acheter des <strong>Mystery Supplies</strong> jusqu'à <strong>2 fois par raid</strong> ; en Endless, l'offre est élargie (supplies + contre-mesures zombies).</li>
          </ul>

          <h2 id="merit">6. Le Merit et les capacités permanentes</h2>
          <p>Chaque mission remplie, chaque mutant abattu rapporte du <strong>Merit</strong>. Le cumul fait monter votre <strong>niveau de croissance Endless</strong>, et chaque niveau débloque <strong>une capacité inédite</strong> — effective <strong>uniquement en mode Endless</strong>.</p>
          <ul>
            <li><strong>Coup de pied (Kick)</strong> — capacité exclusive du mode, sur la touche <code>~</code> par défaut : elle consomme de l'<strong>endurance</strong> pour repousser les mutants devant vous. C'est la meilleure protection contre l'Ambusher et le Breacher.</li>
            <li>Les capacités suivantes s'achètent avec le Merit hors raid et s'appliquent définitivement à vos runs Endless.</li>
            <li><strong>Défi de Merit</strong> (hebdomadaire, reset lundi 5 h UTC) : votre meilleur Merit hebdomadaire en Endless est converti en <strong>3× Koen</strong>, plafonné à <strong>3 000 000 Koen par semaine</strong>.</li>
          </ul>

          <h2 id="missions">7. La ligne de missions zombies</h2>
          <p>La saison 7 ajoute <strong>40 missions zombies</strong> sur un onglet dédié, avec des récompenses par palier :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Étape</th><th>Missions</th><th>Contenu</th></tr></thead>
              <tbody>
                <tr><td><strong>Stage 1</strong></td><td>15</td><td>Base de la progression zombie : échantillons, conteneurs, premiers marqueurs</td></tr>
                <tr><td><strong>Stage 2</strong></td><td>15</td><td>Objectifs plus exigeants, récompenses de caisses de loot</td></tr>
                <tr><td><strong>Étape indépendante</strong></td><td>10</td><td>Ligne <strong>exclusive Zombie Endless</strong> : survie,-Merit, contre-mesures</td></tr>
              </tbody>
            </table>
          </div>
          <p>Terminer la série de missions zombies <strong>garantit l'Elysium</strong>, le nouveau drop rouge de la zone infectée.</p>

          <h2 id="conseils">8. Conseils de survie</h2>
          <ul>
            <li><strong>Ne sur-engagez pas</strong> : chaque balle tirée signale votre position exacte aux autres squads… et dans un raid PvP, aux humains.</li>
            <li><strong>Gardez des munitions économiques</strong> et des <strong>Koen</strong> pour les vagues à haute menace.</li>
            <li><strong>Améliorez vos PV de base</strong> : un Ambusher + un Reaper qui s'enchaînent, c'est un one-shot sans marge.</li>
            <li><strong>Jouez en équipe</strong> — officiellement recommandé : les القدرة se combinent et le downed permanent d'un joueur ne vous élimine pas.</li>
            <li><strong>Fixez-vous un objectif de temps</strong> (« je tiens jusqu'au niveau de menace 12 ») plutôt que « je veux le plus de loot ».</li>
          </ul>

          <div class="callout callout-success">
            <h4>L'ordre recommandé par la communauté</h4>
            <p>No Man's Land pour apprendre les comportements des mutants → Endless pour l'action et le Merit → Infected Zone pour l'expérience complète loot / combat / extraction. Et l'erreur classique :→ le Reaper en premier, toujours.</p>
          </div>
"""

page('saison7-zombie-endless.html',
     "Zombie Endless — Survie PvE",
     "Zombie Endless S7 d'Arena Breakout Infinite : mode PvE sur l'Airport, niveau 8, squad de 1 à 4, Merit, marchand à jetons zombies, ordres d'élimination et astuces de terrain.",
     "../img/zombies/zombie-endless.jpg",
     "Saison 7 — Zombie", "Zombie Endless",
     "Pas de loot à récupérer, pas de second essai : juste la question de combien de temps vous tiendrez.",
     endless,
     [("principe", "1. Principe"), ("boucle", "2. Boucle de survie"), ("priorites", "3. Priorités"),
      ("astuces", "4. Astuces de terrain"), ("marchand", "5. Marchand Endless"), ("merit", "6. Merit & capacités"),
      ("missions", "7. Missions zombies"), ("conseils", "8. Conseils")],
     extra_js=False, nav=NAV, crumb=CRUMB)

print("OK batch A")
