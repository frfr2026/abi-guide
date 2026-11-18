import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Saison 7')
CRUMB = ('Saison 7', 'saison7-utopia.html')

# ─────────────────────────────────────────────── 4. ZOMBIE RESEARCH
research = """
          <figure class="page-figure">
            <img src="../img/zombies/zombie-research.jpg" alt="Laboratoire de recherche biohazard" loading="lazy">
            <figcaption>Zombie Research — la progression permanente de la zone infectée, activée avec des échantillons extraits.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Type</span><span class="fact-value">Progression hors raid</span></div>
            <div class="fact"><span class="fact-label">Devise</span><span class="fact-value">Échantillons zombies extraits</span></div>
            <div class="fact"><span class="fact-label">Portée</span><span class="fact-value">Permanente en Infected Zone</span></div>
            <div class="fact"><span class="fact-label">Reset</span><span class="fact-value">Impossible — choix définitifs</span></div>
          </div>

          <h2 id="principe">1. Le principe</h2>
          <p><strong>Zombie Research</strong> est la progression <em>hors raid</em> dédiée à la contamination. Pendant une raid en Infected Zone, vous récupérez des <strong>échantillons zombies</strong>. Une fois <strong>extraits</strong> — un échantillon non extrait ne compte pas — vous les consommez pour <strong>activer</strong> et <strong>améliorer</strong> des <strong>points de recherche</strong>.</p>
          <p>Les capacités ainsi débloquées restent <strong>permanentes en Infected Zone</strong>, pour toute la durée de la saison. C'est ce qui donne à chaque raid infecté une vraie valeur : le loot est éphémère, la recherche est un actif durable.</p>
          <div class="callout callout-biohazard">
            <h4>La règle qui fait paniquer les pressés</h4>
            <p>Un point de recherche <strong>activé ne peut pas être remis à zéro</strong>. Les lignes qui relient les points indiquent leurs relations d'activation : si un point a plusieurs prérequis, <strong>un seul suffit</strong> pour le débloquer. Il n'y a donc pas de « mauvaise branche » — mais il y a un <strong>ordre</strong> qui compte, et il est définitif.</p>
          </div>

          <h2 id="sources">2. Où trouver les échantillons</h2>
          <ul>
            <li><strong>Uniquement en Infected Zone</strong> (Farm, Valley, Airport). Le Zombie Endless et No Man's Land servent à l'entraînement, la source de samples est la zone contaminée elle-même.</li>
            <li><strong>Sacs de zombies (body bags)</strong> : les corps infectés abattus ont une chance de laisser un sac et des objets zombies.</li>
            <li><strong>Conteneurs exclusifs zombies</strong> : conteneurs d'expédition, distributeurs abandonnés, caisses à indices huileuses — plus d'objets zombies que les conteneurs classiques.</li>
            <li><strong>Missions in-raid</strong> exclusives : les compléter rapporte des récompenses de caisses de loot, avec de quoi accélérer la recherche.</li>
          </ul>
          <div class="callout callout-warning">
            <h4>Ne gaspillez pas vos munitions sur du menu</h4>
            <p>Chaque tir inutile est une entrée dans un combat que vous n'aviez pas à livrer. La communauté le formule ainsi : <em>« le bruit est une ressource »</em>. Réservez les tirs aux Opérateurs, aux mutants dangereux, aux zombies qui bloquent votre route et à la protection de votre extraction. Contourner un groupe en silence est souvent meilleur que le nettoyer au prix de 30 balles.</p>
          </div>

          <h2 id="arbre">3. L'arbre de recherche</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Élément</th><th>Règle</th><th>Conséquence pratique</th></tr></thead>
              <tbody>
                <tr><td><strong>Point de recherche</strong></td><td>Consomme des échantillons pour être activé</td><td>Votre stock d'échantillons est votre vraie monnaie</td></tr>
                <tr><td><strong>Prérequis</strong></td><td>Plusieurs prérequis possibles, un seul suffit</td><td>Pas de verrou linearity : plusieurs chemins valides</td></tr>
                <tr><td><strong>Amélioration</strong></td><td>Un point activé peut être amélioré avec des échantillons supplémentaires</td><td>Les premiers points doivent être choisis avec soin</td></tr>
                <tr><td><strong>Capacité</strong></td><td>Effective en Infected Zone de façon permanente</td><td>Un point bien choisi vaut 3 raids</td></tr>
                <tr><td><strong>Reset</strong></td><td>Impossible</td><td>Ne «Bidules » rien au hasard pour « tester »</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="ordre">4. Ordre d'investissement recommandé</h2>
          <p>La hiérarchie d'investissement découle de la logique de survie : on sécurise d'abord la survie, ensuite l'économie.</p>
          <ol>
            <li><strong>Semaine 1 — la survie</strong> : échantillons de base, réanimation plus rapide, réduction du bruit. Tant que vous mourez en Infected Zone, la recherche avance très peu, car les échantillons non extraits sont perdus.</li>
            <li><strong>Semaine 2 — l'économie</strong> : une fois les upgrades de survie installés, poussez la <strong>recherche liée au loot</strong> (valeur des conteneurs, accès aux zones à fort rendement).</li>
            <li><strong>Semaine 3 — l'optimisation</strong> : dernier coup de pouce aux capacités situationnelles (détection, distance, contre-mesures).</li>
          </ol>
          <div class="callout callout-success">
            <h4>Le calcul qui décide de tout</h4>
            <p>Un échantillon non extrait vaut <strong>zéro</strong>. Avant de spécifier une capacité, vérifiez que votre kit d'extraction est complet : sac suffisant, clé d'extractions, niveau d'agent pour la zone visée. Un point de recherche activé le dernier jour de la saison ne vaut rien.</p>
          </div>

          <h2 id="missions">5. La ligne de missions zombies (40 missions)</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Étape</th><th>Nombre</th><th>Nature</th></tr></thead>
              <tbody>
                <tr><td><strong>Stage 1</strong></td><td>15 missions</td><td>Découverte : premiers échantillons, conteneurs, marqueurs d'objectif</td></tr>
                <tr><td><strong>Stage 2</strong></td><td>15 missions</td><td>Exigence : objectifs denses, récompenses de caisses de loot</td></tr>
                <tr><td><strong>Étape indépendante</strong></td><td>10 missions</td><td>Ligne <strong>exclusive Zombie Endless</strong> : survie, Merit, contre-mesures</td></tr>
              </tbody>
            </table>
          </div>
          <ul>
            <li>Les <strong>récompenses de caisses</strong> se débloquent en terminant les missions in-raid exclusives.</li>
            <li>Terminer la <strong>série complète de missions zombies</strong> garantit l'<strong>Elysium</strong>, le drop rouge de la zone infectée.</li>
            <li>Les <strong>événements d'extermination</strong> débouchent sur des <strong>Hazmat Suit Supply Passes</strong> —ratio de conversion en fin d'événement : 1 pass = 5 000 Koen si non utilisés.</li>
          </ul>

          <h2 id="erreurs">6. Les erreurs qui coûtent cher</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Erreur n°1 — activer au hasard</h3>
              <p class="card-text">Chaque point activé est définitif. Dépenser vos échantillons sur une branche qui ne sert pas votre style de jeu vous bloque pour le reste de la saison.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Erreur n°2 — mal extraire les échantillons</h3>
              <p class="card-text">Un échantillon dans un sac non extrait n'existe pas. Les morts en zone contaminée avec le sac plein coûtent la totalité des échantillons.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Erreur n°3 — tout tuer</h3>
              <p class="card-text">Nettoyer chaque groupe de zombies attire des hordes et vous signale aux squads. Contourner un groupe est souvent plus rentable que de le nettoyer.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Erreur n°4 — négliger les conteneurs</h3>
              <p class="card-text">Les conteneurs exclusifs zombies (shipping, distributeurs, caisses huileuses) sont souvent les meilleurs rendements en échantillons de la carte. Ignorer ce contenu est l'erreur la plus courante.</p>
            </div></div>
          </div>

          <h2 id="faq">7. FAQ</h2>
          <h3>Peut-on réinitialiser un point de recherche ?</h3>
          <p>Non. Les notes officielles sont claires : un point activé reste activé.</p>
          <h3>Faut-il plusieurs prérequis pour un même point ?</h3>
          <p>Non — un seul prérequis activé suffit à débloquer le point suivant, même si l'arbre en dessine plusieurs.</p>
          <h3>Les échantillons se perdent-ils à la fin de la saison ?</h3>
          <p>La recherche zombie est liée à la saison : vos capacités restent actives pendant la Saison 7. Le nouveau système de <strong>formules de recherche</strong> (Improvement Blueprint) est lui aussi explicitement <strong>réinitialisé à chaque saison</strong>.</p>
          <h3>Où sont les conteneurs zombies ?</h3>
          <p>Ils apparaissent en Infected Zone : conteneurs d'expédition, distributeurs de boissons abandonnés et caisses à indices huileuses. Ils remplacent une partie des conteneurs classiques sur ces cartes.</p>

          <div class="callout callout-success">
            <h4>Objectif de fin de semaine</h4>
            <p>Extrayez <strong>10 échantillons</strong> lors de votre prochaine raid Valley (zone standard, la plus simple pour débuter), et réservez-les pour le premier point de survie. Vous aurez déjà 3 fois plus d'échantillons que la moyenne des joueurs qui partent en Hunt-and-Kill.</p>
          </div>
"""

page('saison7-zombie-research.html',
     "Zombie Research — La progression infectée",
     "Zombie Research S7 d'Arena Breakout Infinite : échantillons zombies, points de recherche non réinitialisables, arbre de prérequis, ordre d'investissement et 40 missions zombies.",
     "../img/zombies/zombie-research.jpg",
     "Saison 7 — Zombie", "Zombie Research",
     "Échantillons extraits, points de recherche définitifs, et un arbre dont l'ordre d'activation décide de votre saison.",
     research,
     [("principe", "1. Principe"), ("sources", "2. Sources d'échantillons"), ("arbre", "3. L'arbre"),
      ("ordre", "4. Ordre d'investissement"), ("missions", "5. Les 40 missions"), ("erreurs", "6. Erreurs fréquentes"), ("faq", "7. FAQ")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ─────────────────────────────────────────────── 5. BALANCE CHANGES
balance = """
          <figure class="page-figure">
            <img src="../img/zombies/balance-pvp.jpg" alt="Impact de balle sur plaque d'armure" loading="lazy">
            <figcaption>Le rééquilibrage S7 : plus de portées, des headshots plus payants, et une pénétration devenue déterministe sur l'armure haute.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Version</span><span class="fact-value">Patch 1.0.0.142.19+ (16 sept. 2026)</span></div>
            <div class="fact"><span class="fact-label">Portée</span><span class="fact-value">Augmentée sur l'ensemble de l'armurerie</span></div>
            <div class="fact"><span class="fact-label">Headshots</span><span class="fact-value">Récompense plus régulière</span></div>
            <div class="fact"><span class="fact-label">RNG T5/T6</span><span class="fact-value">Supprimé</span></div>
          </div>

          <h2 id="resume">1. Les 6 changements qui touchent tout le monde</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Changement</th><th>Détail</th><th>Conséquence</th></tr></thead>
              <tbody>
                <tr><td><strong>Portée effective augmentée</strong></td><td>Sur la majorité de l'armurerie</td><td>Les fusils gardent leur létalité plus loin : Valley et Airport deviennent plus dangers à l'armement lourd</td></tr>
                <tr><td><strong>Headshots renforcés</strong></td><td>Les tirs à la tête paient davantage, de façon plus constante</td><td>Le TTK global est allongé mais les duels de précision sont plus rapides</td></tr>
                <tr><td><strong>Plafond d'équipement par mode</strong></td><td>Normal : T4 et moins · Lockdown : T5 et moins · Forbidden : T6</td><td>On ne peut plus écraser un squad déshérité en kit rouge</td></tr>
                <tr><td><strong>RNG de pénétration T5/T6 supprimé</strong></td><td>Pas de « petite chance » de percer une classe V ou VI</td><td>Il faut ramener la durability de la plaque sous un seuil pour percer de façon constante</td></tr>
                <tr><td><strong>Ricochets supprimés</strong></td><td>Plus de rebond sur casques et masques</td><td>Perte de durabilité plus rapide sur les casques et masques de classe V et VI</td></tr>
                <tr><td><strong>Flashlight nerfé</strong></td><td>Éclairage réduit, ergonomie ajustée à <strong>-7</strong></td><td>Fin de l'aveuglement garanti en zone sombre</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="modes">2. Les plafonds par mode</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Équipement et munitions</th><th>Déblocage</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal</strong></td><td>Tier 4 et inférieur (casques, masques, rigs, gilets, munitions)</td><td>Accessible dès le début</td></tr>
                <tr><td><strong>Lockdown</strong></td><td>Tier 5 et inférieur</td><td>Niveau 12</td></tr>
                <tr><td><strong>Forbidden</strong></td><td>Tier 6 autorisé</td><td>Niveau 30</td></tr>
                <tr><td><strong>Infected Zone / Heavy</strong></td><td>Farm et Airport : contamination lourde</td><td>Koen, entrées illimitées</td></tr>
                <tr><td><strong>Zombie Endless</strong></td><td>Loadout imposé par la classe</td><td>Niveau 8</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Ce que le plafond change vraiment</h4>
            <p>Avant, on pouvait « hot-drop » un kit complet dans un lobby de bas niveau pour écraser les déshérités. C'est terminé : en Normal, personne ne vient avec une classe V. Conséquence directe : la <strong>T4 devient le cœur du meta</strong> — les munitions T4 (M855A1, BP) sont le sweet spot de la communauté, et le stash de T6 que vous conservez n'a plus de valeur en Normal : c'est de la valeur immobilisée pour rien.</p>
          </div>

          <h2 id="armures">3. Armures et pénétration</h2>
          <ul>
            <li><strong>Pierce Level = plancher(Pénétration ÷ 10)</strong>, comparé au <strong>Niveau d'armure</strong> de la plaque visée (et non à un tableau externe).</li>
            <li>Avec le RNG supprimé sur la classe V et VI : <strong>sous le niveau, ça ne perce pas</strong>. On ne compte plus sur la chance.</li>
            <li>La percée « constante » exige de <strong>réduire la durability de la plaque sous un certain seuil</strong> : le TTK au torse est donc plus long, il faut poser plusieurs balles dans la même zone.</li>
            <li><strong>Ricochets supprimés</strong> sur tous les casques et masques : le tir à la tête ne « ricoche » plus sur un casque de classe V/VI, mais le casque perd plus vite en durabilité.</li>
          </ul>

          <h2 id="armes">4. Ajustements d'armes</h2>
          <p>Les notes de lancement S7 confirment l'<strong>augmentation de la portée effective</strong> et les <strong>season kits</strong>. Les valeurs chiffrées ci-dessous proviennent des <strong>notes bêta</strong> publiées par la communauté (serveur de test) : elles indiquent la direction des ajustements et servent de référence, mais seule la mise en production fait foi.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Ajustement (notes bêta)</th><th>Lecture tactique</th></tr></thead>
              <tbody>
                <tr><td><strong>188</strong></td><td>Puissance augmentée, portée effective 82 → 102, recul de tir réduit</td><td>Devient une option de sniper de précision plus crédible</td></tr>
                <tr><td><strong>H416</strong></td><td>Recul horizontal augmenté en fin de rafale</td><td>Contrôle plus exigeant sur les longues rafales</td></tr>
                <tr><td><strong>ACE31</strong></td><td>Contrôle vertical 52 → 48, horizontal 28 → 27 ; canon standard légèrement affaibli</td><td>Contrôle un peu meilleur, canon de base un peu moins fort</td></tr>
                <tr><td><strong>FAMAS</strong></td><td>Ergonomie 55 → 63</td><td>Maniement nettement plus confortable</td></tr>
                <tr><td><strong>MCX</strong></td><td>Portée effective 30 → 35</td><td>Plus de marge à distance moyenne</td></tr>
                <tr><td><strong>FAL</strong></td><td>Contrôle vertical 40 → 45, horizontal 22 → 27</td><td>Plus dur à contrôler — sauf avec le Recoil Kit saisonnier</td></tr>
                <tr><td><strong>T03</strong></td><td>Recul amélioré sur la première moitié de rafale</td><td>Spray initial plus maîtrisé</td></tr>
                <tr><td><strong>UMP45</strong></td><td>Cadence 600 → 650</td><td>Petit gain de DPS en CQB</td></tr>
                <tr><td><strong>M110</strong></td><td>Recul de tir réduit</td><td>Combine avec le Dual-Stage Trigger saisonnier</td></tr>
                <tr><td><strong>AK-74N</strong></td><td>Recul de tir amélioré</td><td>Arme budget plus agréable</td></tr>
                <tr><td><strong>AN-94</strong></td><td>Recul vers le haut réduit entre les deux premiers tirs</td><td>Première rafale plus propre</td></tr>
                <tr><td><strong>VSS</strong></td><td>Recul de tir réduit</td><td>Plus de confort en tir soutenu</td></tr>
                <tr><td><strong>5.7×28 SS190</strong></td><td>Pénétration 41 → 42, dégâts d'armure 18 → 19</td><td>Petit regain d'intérêt pour les calibres APDS</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Les 4 season kits, vrais game-changers</h4>
            <p>Ils modifient fondamentalement l'arme concernée : le <strong>M110 Dual-Stage</strong> tire <strong>2 projectiles par gâchette</strong> (dégâts considérables), le <strong>MPX Vulcan</strong> ouvre une branche de munitions à chair, le <strong>FAL Recoil Kit</strong> fait passer la cadence de l'arme de « moyennement-faible » à « élevée », le <strong>PCC-9 Full-Auto Kit</strong> transforme le PCC-9 en arme automatique.</p>
          </div>

          <h2 id="tactique">5. Objets tactiques et qualité de vie</h2>
          <ul>
            <li><strong>GLI-F4 (gaz lacrymogène)</strong> : durée 80 s → <strong>50 s</strong>.</li>
            <li><strong>Grenade de choc expérimentale</strong> : rayon d'explosion légèrement augmenté.</li>
            <li><strong>M84 Flashbang / Multi-Burst amélioré</strong> : rayon de l'effet d'aveuglement augmenté.</li>
            <li><strong>Lampe tactique</strong> : niveau d'éclairage réduit, ergonomie à -7, et l'aberration d'exposition en lumière proche a été corrigée.</li>
            <li><strong>Chargement de chargeur</strong> ajouté aux pistolet et fusils à pompe.</li>
            <li><strong>Inspection interruptible</strong> en s'accroupissant ; <strong>contrôles de fin de soin</strong> améliorés.</li>
            <li><strong>Perspectives 1ʳᵉ et 3ᵉ personne en inclinaison</strong> unifiées ; gestes d'arme au corps redesignés.</li>
            <li><strong>Inspects de plaques d'identité</strong> animés selon le nombre de plaques dans le sac, <strong>journal de dégâts détaillés sur les 30 dernières secondes</strong>, et <strong>partage des temps forts</strong> de la raid.</li>
            <li>Corrections : sprint qui bloquait, audio qui disparaissait, longueur d'arme qui influençait le recul.</li>
          </ul>

          <h2 id="impact">6. Impact sur le meta</h2>
          <ul>
            <li><strong>T4 devient la norme</strong> : en Normal, votre ensemble T4 est votre meta — et elle est parfaitement jouable contre des squads T4.</li>
            <li><strong>Les snipers de précision gagnent</strong> : la portée effective augmentée punit moins les distances de combat.</li>
            <li><strong>Les duels d'armure deviennent honnêtes</strong> : plus de chance, plus de roll de péné — le skill de visée et la gestion de la durability priment.</li>
            <li><strong>Le shotgun et la SMG en CQB restent intouchés</strong> : Armory et TV Station n'ont jamais été gagnés par le tir à distance.</li>
            <li><strong>A545 (700 RPM) vs H416 (800 RPM)</strong> : deux fusils de pointe, deux ways de tenir le milieu de terrain — l'A545 mise sur la maniabilité, le H416 sur le débit.</li>
          </ul>

          <h2 id="recherche">7. Le nouveau système de recherche</h2>
          <ul>
            <li><strong>Improvement Blueprint</strong> : nouveau matériau de recherche obtenu via les missions actives et les raids réguliers, <strong>plus fréquent dans les boîtes à documents, les vêtements et les tiroirs</strong>.</li>
            <li>On utilise un blueprint pour <strong>rechercher une formule</strong>, puis on équipe le résultat pour obtenir un <strong>buff unique</strong>.</li>
            <li>Les blueprints d'assistance peuvent être obtenus en apprenant et partageant des formules avec des amis — ils sont prioritaires dans la file de recherche.</li>
            <li><strong>Les résultats de recherche sont réinitialisés à chaque saison</strong> : ce que vous researches ne profite qu'à la saison en cours.</li>
            <li>Les <strong>formules</strong> de matériaux ont été réajustées et de nouveaux usages ont été ajoutés aux objets divers ; la <strong>M290</strong>, nouvelle grenade stun, est désormais craftable.</li>
          </ul>

          <div class="callout callout-danger">
            <h4>Ne vendez pas vos matériaux trop tôt</h4>
            <p>La Recherche S7 et le nouveau <strong>crafter violet</strong> changent la valeur de certains matériaux de craft. Avant de liquider vos composants au marchand, vérifiez s'ils ne sont pas réinvestissables en blueprints et en formules. L'erreur de market classique d'une saison de refonte.</p>
          </div>
"""

page('saison7-balance-changes.html',
     "Balance Changes S7 — Le rééquilibrage complet",
     "Rééquilibrage Saison 7 Utopia d'ABI : portées effectives, headshots, plafonds T4/T5/T6 par mode, suppression du RNG T5/T6, ricochets retirés, flashlights nerfed, ajustements d'armes et season kits.",
     "../img/zombies/balance-pvp.jpg",
     "Saison 7 — Balance", "Balance Changes S7",
     "Portées, headshots, plafonds d'équipement et pénétration déterministe : tout ce que le patch change dans votre prochain raid.",
     balance,
     [("resume", "1. Résumé"), ("modes", "2. Plafonds par mode"), ("armures", "3. Armures & pénétration"),
      ("armes", "4. Ajustements d'armes"), ("tactique", "5. Objets & QoL"), ("impact", "6. Impact sur le meta"),
      ("recherche", "7. Nouveau système de recherche")],
     extra_js=False, nav=NAV, crumb=CRUMB)

print("OK batch B1")
