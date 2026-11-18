import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Méta')
CRUMB = ('Meta', 'meta-tier-list-globale.html')

# ───────────────────────────────────────────── 2. BUILDS PAR ROLE
builds = """
          <figure class="page-figure">
            <img src="../img/meta/meta-builds.jpg" alt="Équipement d'opérateur organisé au sol" loading="lazy">
            <figcaption>Cinq rôles, cinq façons de gagner sa vie dans Kamona. Le mauvais rôle pour votre style, c'est une mort par raid pendant des semaines.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Rôles</span><span class="fact-value">Assaut S · Sniper A · Lointier A · Team Player A · Pistol Runner B</span></div>
            <div class="fact"><span class="fact-label">Variantes</span><span class="fact-value">Normal T4 · Lockdown T5 · Forbidden T6</span></div>
            <div class="fact"><span class="fact-label">Règle</span><span class="fact-value">Le build est une fonction, pas une liste d'objets</span></div>
            <div class="fact"><span class="fact-label">Outil</span><span class="fact-value">Loadout Optimizer intégré</span></div>
          </div>

          <h2 id="principe">1. Un build est une fonction</h2>
          <p>Un « build » n'est pas une liste d'objets : c'est une <strong>fonction</strong> — ce que vous faites pendant les 12 minutes du raid. Chaque objet doit servir cette fonction. Si un slot ne sert pas le rôle, il est de l'argent dans un sac qui ralentit votre course.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Rôle</th><th>Tier</th><th>Fonction</th><th>Équipement cœur</th></tr></thead>
              <tbody>
                <tr><td><strong>Assaut</strong></td><td>S</td><td>Pousser agressivement les zones de loot contestées, combattre à moyenne distance, extraire avec du loot lourd</td><td>Fusil d'assaut modifié, gilet T4, casque T3, trousse IFAK</td></tr>
                <tr><td><strong>Sniper</strong></td><td>A</td><td>Tenir une position d'overwatch en hauteur, engager à 200 m et +, se relocaliser après chaque tir</td><td>SVD / M24, 4×, sidearm, armure T3 (légère), attelles</td></tr>
                <tr><td><strong>Lointier</strong></td><td>A</td><td>Sprinter vers les spawns de valeur, remplir les conteneurs, extraire par le point le plus proche</td><td>MP5, grand sac, rig multi-slots, clés de salles fermées</td></tr>
                <tr><td><strong>Team Player</strong></td><td>A</td><td>Rester avec le squad, soutenir médicalement, partager munitions et soins</td><td>M4A1 standard, IFAK supplémentaires, kit chirurgical, attelles, armure T4</td></tr>
                <tr><td><strong>Pistol Runner</strong></td><td>B</td><td>Éviter le PvP, piocher le loot dans les zones calmes, extraire vite avec un conteneur plein</td><td>Glock 17 à chargeur étendu, pansements de base, rig à grandes poches</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="assaut">2. Build Assaut — tier S</h2>
          <figure class="page-figure">
            <img src="../img/meta/role-assault.jpg" alt="Opérateur en attaque dans une usine" loading="lazy">
            <figcaption>Assaut : entrer vite, sortir vite. L'objectif n'est pas de tout voir, c'est de prendre la pièce avant les autres.</figcaption>
          </figure>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Slot</th><th>Choix</th><th>Pourquoi</th></tr></thead>
              <tbody>
                <tr><td>Primaire</td><td><strong>H416</strong> ou <strong>A545</strong></td><td>Le recul contrôlable et la portée S7 : ils couvrent le CQB et la moyenne distance</td></tr>
                <tr><td>Munitions</td><td>M855A1 PL 4 (Normal) / M995 PL 5 (Lockdown)</td><td>Le PL 4 est le sweet spot ; le PL 5 seulement si votre cible est équipée de classe 5</td></tr>
                <tr><td>Gilet</td><td>6B13 T4 (Normal) / 6B43 T5 (Lockdown)</td><td>46 d'ergonomie au T4 : la mobilité vaut plus que 20 points de durabilité</td></tr>
                <tr><td>Casque</td><td>T4 avec <strong>visière T4</strong></td><td>En Lockdown, la DK6 (T3) laisse passer toute munition T3 et moins</td></tr>
                <tr><td>Médical</td><td>100D Battlefield Medkit + 1 kit chirurgical + OPM bandage ×2</td><td>Le saignement et le membre cassé sont les deux causes de mort en push</td></tr>
                <tr><td>Budget</td><td>~950 000 K en Lockdown</td><td>Le kit d'assaut typique de la communauté</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="sniper">3. Build Sniper — tier A</h2>
          <figure class="page-figure">
            <img src="../img/armes/m24.jpg" alt="Fusil de précision M24" loading="lazy">
            <figcaption>M24 — le sniper S7. Chaque tir doit compter : après la détonation, on se relocalise.</figcaption>
          </figure>
          <ul>
            <li><strong>Arme :</strong> M24 (tier S) pour la portée, M110 + Dual-Stage Trigger (tier A) pour le two-shot-per-pull en overwatch, SJ16 (tier A) pour le budget Forbidden.</li>
            <li><strong>Munitions :</strong> 7.62×51 M62 (PL 5) en Lockdown, 7.62×54 SNB (PL 6) en Forbidden. Le 7N37 (PL 7) perce la classe 6 de façon constante, mais il est <strong>au-dessus du plafond standard</strong> : vérifiez son admissibilité en jeu.</li>
            <li><strong>Protection :</strong> armure <strong>T3</strong> maximum. Le sniper n'a pas besoin d'une classe 5 : il a besoin de vitesse et de silence.</li>
            <li><strong>Technique :</strong> choisissez un <strong>monument</strong> et restez à côté, en bougeant le moins possible tout en gardant une ligne de vue. Ne vous installez <em>pas</em> dessus.</li>
            <li><strong>Ne lootez jamais un kill</strong> tant que la zone n'est pas sûre. La tentation est forte, la discipline paie.</li>
            <li><strong>Après le tir :</strong> déplacez-vous. Les snipers adverses guettent les positions statiques, et en S7 la portée effective augmentée rend le contre-tir plus probable.</li>
          </ul>

          <h2 id="cqb">4. Build CQB — tier A</h2>
          <figure class="page-figure">
            <img src="../img/meta/role-cqb.jpg" alt="Opérateur en CQB dans un couloir" loading="lazy">
            <figcaption>CQB : trois mètres, une porte, zéro marge. Le bruit est votre pire ennemi — et votre meilleur informant.</figcaption>
          </figure>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Slot</th><th>Choix</th><th>Pourquoi</th></tr></thead>
              <tbody>
                <tr><td>Primaire</td><td><strong>P90</strong> (S) ou <strong>PCC9 + Full-Auto Kit</strong> (A)</td><td>Cadence, maniabilité, vitesse de mise en joue</td></tr>
                <tr><td>Secondaire</td><td>Pistolet 9×19 + dum-dum</td><td>Pour les jambes : la « leg meta » est l'option la plus économique du jeu</td></tr>
                <tr><td>Audio</td><td><strong>GS2</strong> (coupe ouverte)</td><td>Le son est une information : c'est la principale source de données en CQB</td></tr>
                <tr><td>Équipement</td><td>Stun grenade + smoke</td><td>Le stun ouvre, la smoke couvre la traversée</td></tr>
                <tr><td>Règle</td><td>Jamais un sniper en primaire</td><td>En TV Station, les lignes de vue sont courtes et les duels se jouent en 2 secondes</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="loot">5. Build Lointier — tier A</h2>
          <figure class="page-figure">
            <img src="../img/meta/role-looter.jpg" alt="Opérateur en course avec un sac plein" loading="lazy">
            <figcaption>Lointier : la vitesse est une stat de combat. Chaque slot non chargé est un slot perdu.</figcaption>
          </figure>
          <ul>
            <li><strong>Priorité absolue :</strong> la <strong>valeur par slot</strong>. Visez 5 000 Koen par case en Normal, 10 000 en Lockdown, davantage en Forbidden.</li>
            <li><strong>Arme légère :</strong> MP5, UMP45 ou USAS-12. Le but n'est pas de tuer, c'est de sortir vite.</li>
            <li><strong>Équipement :</strong> grand sac, rig multi-slots, <strong>une clé de salle fermée</strong> — un coffre ouvre bien plus de valeur qu'un conteneur au sol.</li>
            <li><strong>Sur les bodies :</strong> un joueur tué porte souvent un kit T4 ou T5. Vider un corpse vaut mieux que fouiller une armoire.</li>
            <li><strong>Méthode « rat » :</strong> entrer quasi nu, seauthentication dans un coin, laisser les autres fights se faire, puis opportunément voler l'équipement des morts. C'est le build le plus rentable en Forbidden pour les joueurs qui n'ont pas le niveau de PvP.</li>
          </ul>

          <h2 id="support">6. Build Team Player / Soutien — tier A</h2>
          <figure class="page-figure">
            <img src="../img/meta/role-support.jpg" alt="Opérateur portant secours à un coéquipier" loading="lazy">
            <figcaption>Soutien : en squad, votre valeur se mesure au nombre de coéquipiers que vous remettez en combat.</figcaption>
          </figure>
          <ul>
            <li><strong>Arme :</strong> RPK-16 (600 RPM, chargeur 60) ou AEK (800 RPM) — la suppressioncontinue est votre métier.</li>
            <li><strong>Médical en double :</strong> une trousse supplémentaire pour les coéquipiers. Un STO First Aid Set supplémentaire vaut plus qu'une lunette thermique pour le business du squad.</li>
            <li><strong>Munitions :</strong> 180 cartouches minimum, et un second type de calibre dans un slot libre : vous ramassez les balles de vos morts.</li>
            <li><strong>Communication :</strong> le volume de la musique baisse automatiquement en multijoueur en S7 : c'est fait pour que vous entendiez vos coéquipiers.</li>
            <li><strong>Réactivité :</strong> le kit de soutien n'a pas besoin d'être agressif. Il couvre, il porte, il ramène.</li>
          </ul>

          <h2 id="prets">7. Les 5 builds prêts à l'emploi</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Build</th><th>Arme</th><th>Munition</th><th>Usage</th></tr></thead>
              <tbody>
                <tr><td><strong>Polyvalent</strong></td><td>AK-12</td><td>5.45×39 BS (PL 5)</td><td>Le fusil à tout faire, rentable en Koen</td></tr>
                <tr><td><strong>Assaut</strong></td><td>Vector .45</td><td>.45 AP (PL 3)</td><td>Assaut lourd : 1 200 RPM et des dégâts de chair à la hauteur</td></tr>
                <tr><td><strong>Longue distance</strong></td><td>M24</td><td>7.62×51 M80 (PL 4)</td><td>Overwatch et headshots : 63 dégâts de chair, classe 4 percée</td></tr>
                <tr><td><strong>Léger</strong></td><td>P90</td><td>5.7×28mm SS198</td><td>CQB rapide et mobile</td></tr>
                <tr><td><strong>Anti-armure lourde</strong></td><td>Mosin</td><td>7.62×54 SNB (PL 6)</td><td>Le setup qui perce la classe 6 de façon fiable</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Chaque build a deux variantes</h4>
            <p>En S7, le <strong>class d'armure est plafonné par la difficulté</strong> : chaque build existe donc en version <strong>Normal (T4 max)</strong> et <strong>Lockdown (T5 max)</strong>. Le build est le même, seul l'équipement change — et c'est exactement ce que calcule <a href="meta-loadout-optimizer.html">l'optimiseur de loadout</a>.</p>
          </div>

          <h2 id="variantes">8. Adapter son build au mode</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Plafond</th><th>Déblocage</th><th>Ce que vous devez changer</th></tr></thead>
              <tbody>
                <tr><td>Normal</td><td>T4</td><td>Immédiat</td><td>Tout le kit doit tenir sous T4 : le stock T5/T6 est de la valeur immobilisée</td></tr>
                <tr><td>Lockdown</td><td>T5</td><td>Niveau 12</td><td>Montez d'un cran en armure et en munitions ; c'est là que se fait l'économie</td></tr>
                <tr><td>Forbidden</td><td>T6</td><td>Niveau 30</td><td>Vérifiez la valeur du kit : 2 000 K+ de gear = une mort à 2 millions</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>La règle de la « juiced kit »</h4>
            <p>Placer un sac à dos et des accessoires <strong>dans le rig</strong> au lieu du sac réduit la valeur d'entrée du kit et permet d'entrer avec un équipement qui dépasserait la limite — le contournement classique de la limite de valeur. Attention : depuis la mise à jour, on ne peut plus placer de sac à dos dans le rig.</p>
          </div>
          <p>Pour l'outil de construction, voir <a href="meta-loadout-optimizer.html">le Loadout Optimizer</a>. Pour le classement des armes, voir <a href="meta-tier-list-globale.html">la tier list globale</a>.</p>
"""

page('meta-builds-roles.html',
     "Builds par rôle S7",
     "Builds ABI Saison 7 par rôle : Assaut, Sniper, CQB, Lointier, Soutien. Slots détaillés, variantes Normal/Lockdown/Forbidden et 5 builds prêts à l'emploi.",
     "../img/meta/meta-builds.jpg",
     "Meta — Builds", "Builds par rôle",
     "Assaut, Sniper, CQB, Lointier, Soutien : cinq rôles, et un seul qui correspond à votre façon de jouer.",
     builds,
     [("principe", "1. Un build est une fonction"), ("assaut", "2. Build Assaut"), ("sniper", "3. Build Sniper"),
      ("cqb", "4. Build CQB"), ("loot", "5. Build Lointier"), ("support", "6. Build Soutien"),
      ("prets", "7. Builds prêts à l'emploi"), ("variantes", "8. Adapter au mode")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ───────────────────────────────────────────── 3. STRATEGIES S7
strategies = """
          <figure class="page-figure">
            <img src="../img/meta/meta-strategies.jpg" alt="Table de planification tactique dans un avant-poste" loading="lazy">
            <figcaption>Le meta de la Saison 7, c'est la patience. L'arme la plus deadly du jeu ne vaut rien si vous tirez le premier.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Principe</span><span class="fact-value">Patience armee — tirer en dernier</span></div>
            <div class="fact"><span class="fact-label">Rat run</span><span class="fact-value">Entrer léger, voler l'équipement</span></div>
            <div class="fact"><span class="fact-label">Seuil de loot</span><span class="fact-value">5 000 K/slot en Normal, 10 000 en Lockdown</span></div>
            <div class="fact"><span class="fact-label">Fenêtre d'extraction</span><span class="fact-value">Dernières 3 minutes = zone de tier 3</span></div>
          </div>

          <h2 id="patience">1. La patience armée — le principe directeur</h2>
          <p>Le meilleur joueur de la communauté l'a formulé ainsi : <em>« Si tu n'es pas sûr de ton tir, tu es mort. La survie de la raid est tout l'intérêt. »</em> Avec le <strong>TTK allongé</strong> et les <strong>headshots renforcés</strong> de la S7, tirer en premier est devenu plus risqué que de tirer en dernier.</p>
          <ul>
            <li><strong>Ne tirez jamais le premier</strong> si vous pouvez le éviter. Vous n'avez qu'à gagner un échange de plus.</li>
            <li><strong>Surveillez le son avant l'image</strong> : un casque audio GS2 (coupe ouverte) est l'information la plus rentable du jeu.</li>
            <li><strong>Relocalisez après chaque engagement</strong> : rester en place après un tir, c'est offering une seconde chance à l'adversaire.</li>
            <li><strong>Ne lootez un kill qu'en sécurité</strong> : c'est la tentation numéro un et la mort numéro un.</li>
          </ul>
          <div class="callout callout-success">
            <h4>« Weaponized patience »</h4>
            <p>La formule est apparue dans la communauté : la patience est une <strong>arme</strong>. Attendre que l'adversaire commette l'erreur coûte zéro Koen et élimine le risque. Les joueurs qui « se battent comme ils l'arrivent » gagnent moins de loot mais survivent plus longtemps — et leur économie tient.</p>
          </div>

          <h2 id="rat">2. La technique du « rat »</h2>
          <p>C'est la méthode la plus rentable du jeu pour un joueur qui n'est pas au top du PvP, et elle s'apprend en une phrase : <strong>entrez sans armure, faites le mort, et ramassez ce que les autres ont payé.</strong></p>
          <ol>
            <li><strong>Entrez avec le strict minimum</strong> : une arme, un casque audio, un sac, un rig. Vous êtes « juste au-dessus » du seuil d'entrée.</li>
            <li><strong>Ne vous déplacez qu'en silence</strong> et restez à couvert.</li>
            <li><strong>Lisez les combats</strong> : quand deux squads s'affrontent, attendez la fin.</li>
            <li><strong>Récupérez l'équipement</strong> des morts et des bots.</li>
            <li><strong>Extrayez</strong> avec le butin récupéré.</li>
          </ol>
          <div class="callout callout-warning">
            <h4>L bank's de la communauté</h4>
            <p>« J'ai fait 1 000 heures et je joue surtout en Forbidden. En mode Rat, je lis un livre jusqu'aux 15 dernières minutes, puis je farm les munitions T4 des bots et je loot ce qui reste. » Sur un run réussi, la technique rapporte plusieurs millions de Koen — et le coût de mort est minimal.</p>
          </div>

          <h2 id="par-mode">3. La stratégie économique par mode</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Stratégie dominante</th><th>Seuil de loot</th><th>Conseil</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal</strong></td><td>Économie lente mais sûre, farm de loot, clés bon marché</td><td>5 000 K/slot</td><td>« Un run Normal bien joué fait 20 à 30 K de butin — c'est déjà un flux d'airain positif. »</td></tr>
                <tr><td><strong>Lockdown</strong></td><td><strong>Le mode qui finance le Forbidden</strong>. Kit à 300–400 K, T5, PvP actif</td><td>10 000 K/slot</td><td>« Mes raids Lockdown financent mes sorties Forbidden. »</td></tr>
                <tr><td><strong>Forbidden</strong></td><td>Top 5 % du jeu. Rat run ou mort rapide</td><td>15 000 K+/slot</td><td>« Le Forbidden est où le top 5 % gagne de l'argent ; les autres grattent. »</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>Le seuil de bascule</h4>
            <p>Un consensus Reddit : <strong>au-delà de 5 millions de liquidité, passez en Lockdown à T5</strong> et restez-y. En dessous, accumulation en Normal. Le moment où l'on bascule est l'un des seuls vrais jalons de progression économique du jeu — et il est purement lié au capital, pas au talent.</p>
          </div>

          <h2 id="extraction">4. Le timing d'extraction</h2>
          <ul>
            <li><strong>Les extractions conditionnelles s'ouvrent vers T+10 minutes</strong> (Southern Blockade, Hunter's Path). Le Blockade Ouest coûte 2 000 K en Normal, 6 000 K en Lockdown.</li>
            <li><strong>Les 3 dernières minutes = zone de tier 3</strong> : le jeu place des joueurs de haut niveau autour des points d'extraction. Le dernier quart du raid est le plus dangereux, pas le plus rentable.</li>
            <li><strong>Valley Helipad</strong> exige 2 plaques d'identité : une préparation en plus.</li>
            <li><strong>Ne sortez pas du raid par l'extraction la plus proche</strong> si elle traverse une zone à fort trafic. L'extraction « gratuite » en durée vaut parfois plus que 30 secondes de trajet supplémentaire.</li>
          </ul>

          <h2 id="bruit">5. Le bruit comme ressource</h2>
          <p>C'est le concept le plus important de l'extraction shooter : <strong>chaque détonation est une information que vous offrez</strong> — aux joueurs et aux mutations.</p>
          <ul>
            <li><strong>Le silence est un multiplicateur de loot</strong> : les zombies que vous contournez ne coûtent pas de munitions.</li>
            <li><strong>Tirer sur les voitures de police</strong> déclenche un <strong>événement de horde</strong> en zone infectée. Ne le faites jamais près d'un loot.</li>
            <li><strong>Le suppresseur</strong> réduit le rayon d'information — mais pas la distance de l'information : vos balles traversent quand même.</li>
            <li><strong>Le son de pas</strong> : réservez l'endurance (sprint) pour les moments où vous ne voulez pas être entendu.</li>
          </ul>

          <h2 id="survie">6. Les 5 règles de survie</h2>
          <ol>
            <li><strong>Chaque slot compte.</strong> Visez 5 000 K par case en Normal, 10 000 en Lockdown, plus en Forbidden. Un slot vide vaut un slot de red drop.</li>
            <li><strong>Le poids est un ennemi.</strong> Un BT101 à 9,8 kg et un sac de 45 L transforment vos 12 minutes en sprint de 4 minutes.</li>
            <li><strong>Le médical n'est pas optionnel.</strong> Un membre cassé non soigné = mort. Portez au moins un kit chirurgical.</li>
            <li><strong>Ne restez jamais au spawn.</strong> Les zones de spawn sont balayées par les joueurs qui.rotate rapidement.</li>
            <li><strong>Évaluez chaque combat.</strong> Un duel contre un kit T6 avec votre fusil T4 n'est pas un duel : c'est un don.</li>
          </ol>

          <h2 id="squad">7. Solo ou squad ?</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Solo</h3>
              <p class="card-text">— <strong>Avantage :</strong> aucun partage de loot, pas de traître, rotation libre.</p>
              <p class="card-text">— <strong>Inconvénient :</strong> en Lockdown et Forbidden, vous affrontez des squads de 4. Aucun joueur sérieux ne recommande le Forbidden en solo sans un groupe stable.</p>
              <p class="card-text">— <strong>Stratégie :</strong> le rat run, les zones à faible densité de joueurs, l'extraction dès qu'elle est ouverte.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Squad</h3>
              <p class="card-text">— <strong>Avantage :</strong> couverture, reviving, partage de munitions, seuil de valeur plus élevé supporté.</p>
              <p class="card-text">— <strong>Inconvénient :</strong> un mort coûte le loot du groupe, et le butin se partage.</p>
              <p class="card-text">— <strong>Stratégie :</strong> le build Soutien devient le plus rentable du jeu : un STO First Aid Set de plus vaut mieux qu'une lunette thermique.</p>
            </div></div>
          </div>

          <h2 id="routine">8. La routine d'entraînement</h2>
          <p>La communauté est claire : <strong>le skill avant le gear</strong>. « Le mouvement, le loot, la gestion des munitions, la connaissance des cartes et l'IQ d'extraction shooter comptent plus que n'importe quel kit. »</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Semaine</th><th>Objectif</th><th>Exercice</th></tr></thead>
              <tbody>
                <tr><td>1</td><td>Maîtrise du déplacement</td><td>Alterner Normal et Lockdown, sprint court / marche / accroupi, rotation silencieuse</td></tr>
                <tr><td>2</td><td>Gestion de l'inventaire</td><td>Objectif : 5 000 K par slot à la fin de chaque raid. Jeter ce qui ne sert pas.</td></tr>
                <tr><td>3</td><td>Maîtrise balistique</td><td>Chaque arme que vous possédez : apprendre son pattern de recul au Workbench ou en No Man's Land</td></tr>
                <tr><td>4</td><td>Connaissance des cartes</td><td>Une carte par jour, ses spawns de valeur, ses extractions, ses lignes de vue</td></tr>
                <tr><td>5</td><td>Discipline de tir</td><td>Toujours tirer en second, toujours se relocaliser, toujours loot en sécurité</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>La routine « 15 minutes » du hit-parade de la maîtrise</h4>
            <p>Chaque jour : <strong>15 minutes en No Man's Land</strong> (zombies, Pattern de recul, aucun risque) puis <strong>1 run Normal</strong> avec un kit à 100 K. Cette routine, ludique et économique, fait plus progresser qu'un pass saisonnier.</p>
          </div>

          <h2 id="erreurs">9. Les erreurs récurrentes</h2>
          <ul>
            <li><strong>Le gear fear</strong> : « je ne suis pas prêt pour le Lockdown ». Vous ne serez jamais prêt ; vous le deviendrez en mourant 10 fois à 100 K au lieu d'une fois à 2 millions.</li>
            <li><strong>Over-équipement</strong> : au-delà de 20 % de votre stash dans une sortie, chaque mort est une crise économique.</li>
            <li><strong>Le spawn camping</strong> : rester près de son point d'apparition est la cause de mort la plus stupide et la plus fréquente.</li>
            <li><strong>Suivre le bruit</strong> : aller vers un combat est rarement le bon choix, sauf si votre kit est supérieur.</li>
            <li><strong>Négliger le médical</strong> : un membre cassé est une death sentence à retardement.</li>
            <li><strong>Survivre passivement</strong> : « les survivants finissent toujours par mourir sur le point d'extraction ». Survivre, c'est bouger, accepter une occasion.</li>
          </ul>
          <p>Pour les builds, voir <a href="meta-builds-roles.html">le guide des builds par rôle</a>. Pour le classement des armes, voir <a href="meta-tier-list-globale.html">la tier list globale</a>. Pour l'outil, voir <a href="meta-loadout-optimizer.html">le Loadout Optimizer</a>.</p>
"""

page('meta-stratégies-s7.html',
     "Stratégies S7",
     "Stratégies ABI Saison 7 : patience armée, technique du rat, économie par mode Normal/Lockdown/Forbidden, timing d'extraction, gestion du bruit, routine d'entraînement et erreurs à éviter.",
     "../img/meta/meta-strategies.jpg",
     "Meta — Stratégies", "Stratégies S7",
     "Le meta n'est pas une arme : c'est une discipline. Patience, discipline, économie — dans cet ordre.",
     strategies,
     [("patience", "1. La patience armée"), ("rat", "2. La technique du rat"), ("par-mode", "3. Économie par mode"),
      ("extraction", "4. Timing d'extraction"), ("bruit", "5. Le bruit comme ressource"), ("survie", "6. 5 règles de survie"),
      ("squad", "7. Solo ou squad"), ("routine", "8. Routine d'entraînement"), ("erreurs", "9. Erreurs récurrentes")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ───────────────────────────────────────────── 4. LOADOUT OPTIMIZER
optimizer = """
          <figure class="page-figure">
            <img src="../img/meta/meta-optimizer.jpg" alt="Poste de travail d'optimisation d'équipement" loading="lazy">
            <figcaption>Loadout Optimizer — choisissez votre mode, votre rôle et votre budget : l'outil calcule le kit, son coût et ses points de vigilance.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Entrées</span><span class="fact-value">Mode · Rôle · Budget</span></div>
            <div class="fact"><span class="fact-label">Sources</span><span class="fact-value">24 armes · 14 gilets · 17 munitions</span></div>
            <div class="fact"><span class="fact-label">Contraintes</span><span class="fact-value">Plafond de tier par mode</span></div>
            <div class="fact"><span class="fact-label">Sortie</span><span class="fact-value">8 lignes de kit + verdict + export</span></div>
          </div>

          <h2 id="outil">1. L'outil</h2>
          <p>Choisissez un <strong>mode</strong> (il fixe le plafond de tier et donc l'équipement possible), un <strong>rôle</strong> (il pondère cadence, portée et catégorie d'arme) et un <strong>budget</strong>. L'optimizer sélectionne l'arme, la munition, le gilet et l'équipement annexe, calcule le coût total et signale les incohérences.</p>

          <div class="optimizer">
            <div class="opt-controls">
              <div class="opt-field">
                <label for="opt-mode">Mode de jeu</label>
                <select id="opt-mode"></select>
              </div>
              <div class="opt-field">
                <label for="opt-role">Rôle de jeu</label>
                <select id="opt-role"></select>
              </div>
              <div class="opt-field">
                <label for="opt-budget">Budget (Koen)</label>
                <div class="opt-budget-head"><span>Budget total du kit</span><b id="opt-budget-val">450 000 K</b></div>
                <input type="range" id="opt-budget" min="120000" max="3500000" step="10000" value="450000">
              </div>
            </div>
            <div class="opt-result">
              <div class="callout"><p>Chargement des données…</p></div>
            </div>
            <div class="opt-actions">
              <button type="button" class="btn btn-primary" id="opt-copy">Copier le build</button>
              <pre class="opt-summary"></pre>
            </div>
          </div>

          <h2 id="lecture">2. Comment lire le résultat</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Indicateur</th><th>Signification</th></tr></thead>
              <tbody>
                <tr><td><strong>Coût total du kit</strong></td><td>Somme de l'arme, des munitions (120 cartouches, 180 pour le rôle Soutien, au prix unitaire du calibre), du gilet, du casque, du rig, du sac, de l'audio et du médical</td></tr>
                <tr><td><strong>% du budget</strong></td><td>Barre verte sous 95 %, ambre à 95 %, rouge au-dessus de 100 %. Chaque mode charge sa propre enveloppe : 450 000 K en Normal, 950 000 K en Lockdown, 2 000 000 K en Forbidden</td></tr>
                <tr><td><strong>Verdict</strong></td><td>Jugement de cohérence économique du kit par rapport au budget déclaré</td></tr>
                <tr><td><strong>Points de vigilance</strong></td><td>Incohérences détectées automatiquement : arme de tier S en mode Normal, munition en dessous du plafond, gilet sous-équipé, sniper en Normal, CQB en Forbidden…</td></tr>
                <tr><td><strong>Conseil du rôle</strong></td><td>La ligne de jeu spécifique au rôle sélectionné</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="methode">3. La méthode de calcul</h2>
          <figure class="page-figure">
            <img src="../img/meta/ammo-tiers.jpg" alt="Cartouches de munitions classées par niveau de pénétration" loading="lazy">
            <figcaption>Les niveaux de pénétration décident du choix : chaque cartouche porte un Pierce Level, comparé au niveau de la plaque visée.</figcaption>
          </figure>
          <ol>
            <li><strong>Filtrage par mode</strong> : le tier de plafond (T4 / T5 / T6) élimine tout ce qui n'est pas autorisé.</li>
            <li><strong>Filtrage par rôle</strong> : seules les catégories d'armes du rôle sont considérées (fusils pour l'assaut, SMG et shotgun pour le CQB, sniper et DMR pour la longue distance…).</li>
            <li><strong>Score d'arme</strong> : tier (×14), cadence (pondérée par le rôle), portée effective (pondérée par le rôle), ergonomie, dégâts de base, moins une pénalité de coût.</li>
            <li><strong>Choix final</strong> : l'enveloppe disponible est répartie entre l'arme (60 %), le gilet (25 %) et les munitions (le reste). L'arme retenue est la mieux notée du rôle dont le prix entre dans sa part ; le gilet vise le tier maximal du mode puis se dégrade d'un cran tant qu'il dépasse l'enveloppe.</li>
            <li><strong>Munition</strong> : la plus haute pénétration du calibre de l'arme, plafonnée par le mode et par le prix unitaire restant.</li>
            <li><strong>Gilet</strong> : le tier maximal autorisé par le mode, dégradé d'un cran si son prix dépasse l'enveloppe.</li>
            <li><strong>Équipement annexe</strong> : casques, rigs, sacs, audio et médical issus du template du mode, complétés par les parts restantes du budget.</li>
          </ol>
          <div class="callout callout-warning">
            <h4>Ce que l'outil ne fait pas</h4>
            <p>Il ne calcule <strong>pas</strong> le coût de vos clés, de votre case sécurisée, de vos quick kits ni de vos consommables de raid. Et il ne remplace pas votre style : il part du principe qu'un build doit être <strong>une fonction</strong> avant d'être un optimum statistique.</p>
          </div>

          <h2 id="presets">4. Les presets à copier immédiatement</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Preset</th><th>Mode</th><th>Rôle</th><th>Budget</th><th>Résultat attendu</th></tr></thead>
              <tbody>
                <tr><td>Apprentissage sûr</td><td>Normal</td><td>Lointier</td><td>250 000</td><td>MP5 ou UMP + dum-dum, gilet T3, sac léger : on apprend sans mourir riche</td></tr>
                <tr><td>Lockdown standard</td><td>Lockdown</td><td>Polyvalent</td><td>950 000</td><td>AK-12 ou H416 en T5, gilet T5, le kit de la majorité</td></tr>
                <tr><td>Push agressif</td><td>Lockdown</td><td>Assaut</td><td>1 200 000</td><td>H416 / A545, 6B43, casque T5, médical complet</td></tr>
                <tr><td>Overwatch</td><td>Lockdown</td><td>Longue distance</td><td>1 000 000</td><td>M110 + Dual-Stage, M62 en T5, armure T4 pour la mobilité</td></tr>
                <tr><td>Zombies</td><td>Normal</td><td>CQB</td><td>500 000</td><td>USAS-12 + dum-dum, le meta anti-horde</td></tr>
                <tr><td>Forbidden anti-armure</td><td>Forbidden</td><td>Longue distance</td><td>2 000 000</td><td>M61 en 7.62×51 ou 7N37, gilet T6, casque T6 : le seul qui perce la classe 6</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="apropos">5. À propos des données</h2>
          <p>Les données proviennent des bases de référence du site (<code>data-weapons.json</code>, <code>data-armors.json</code>, <code>data-ammo.json</code>) et des <code>data-builds.json</code> de l'étape Meta. Les prix sont <strong>indicatifs</strong> et fluctuent avec le marché joueur : la valeur de référence d'une arme ou d'un gilet change chaque semaine.</p>
          <div class="callout callout-success">
            <h4>Le bon réflexe</h4>
            <p>Utilisez l'optimizer pour <strong>structurer</strong> votre kit, jamais pour valider un achat. La décision d'investissement doit suivre le marché : achetez le <strong>calibre</strong> que vous utilisez (5.56×45 couvre 13 armes, 9×19 en couvre 12), pas l'arme exacte.</p>
          </div>
          <p>Pour comprendre le classement des armes, voir <a href="meta-tier-list-globale.html">la tier list globale</a>. Pour la méthode de jeu, voir <a href="meta-stratégies-s7.html">les stratégies S7</a>.</p>
"""

page('meta-loadout-optimizer.html',
     "Loadout Optimizer",
     "Outil interactif ABI Saison 7 : choisissez votre mode, votre rôle et votre budget, l'optimiseur calcule le kit complet — arme, munitions, gilet, casque, rig, sac, audio et médical — avec verdict et export.",
     "../img/meta/meta-optimizer.jpg",
     "Meta — Outil", "Loadout Optimizer",
     "Mode, rôle, budget : l'outil calcule votre kit complet et signale les incohérences avant la raid.",
     optimizer,
     [("outil", "1. L'outil"), ("lecture", "2. Lire le résultat"), ("methode", "3. Méthode de calcul"),
      ("presets", "4. Presets"), ("apropos", "5. À propos des données")],
     extra_js='optimizer', nav=NAV, crumb=CRUMB)

print("OK S11 batch B")
