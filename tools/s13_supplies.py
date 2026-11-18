# -*- coding: utf-8 -*-
"""S13 — Contenu de la page events-supplies-drops.html."""

CONTENT = r"""
          <div class="evt-legend">
            <span class="evt-badge evt-live">En cours</span><span class="lg-txt">mécanique active au 17 novembre 2026</span>
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">notes de patch et annonces MoreFun</span>
            <span class="src-tag src-communautaire">Communauté</span><span class="lg-txt">tests de joueurs, guides recoupés</span>
            <span class="src-tag src-rapporte">Rapporte</span><span class="lg-txt">recoupement partiel, non confirmé</span>
          </div>

          <div class="facts">
            <div class="fact"><span class="fact-label">Mode</span><span class="fact-value">Co-op PvPvE, 4 équipes, carte Airport</span></div>
            <div class="fact"><span class="fact-label">Risque</span><span class="fact-value">Aucun — loadout fourni, réapparitions illimitées</span></div>
            <div class="fact"><span class="fact-label">Progression</span><span class="fact-value">Caisse de récompense de niveau 1 à 5</span></div>
            <div class="fact"><span class="fact-label">Débloqué au niveau 3</span><span class="fact-value">Le Smelter, sans limite d’usage</span></div>
          </div>

          <figure class="page-figure">
            <img src="../img/events/supply-drops-airdrop.jpg" alt="Caisse de ravitaillement militaire descendue sous parachute sur un terrain d aeroport nocturne, lueur orange de fusée de signalisation" loading="lazy">
            <figcaption>Supplies Drops 2.0 : ce n’est pas une extraction, c’est une gestion de caisse. Ce qui compte, c’est le niveau de la crate à la fin du raid, pas ce que vous avez dans le sac.</figcaption>
          </figure>

          <h2 id="mode">1. Supply Drops 2.0 en bref</h2>
          <p><strong>Supplies Drops 2.0</strong> est le rework saisonnier du mode Supplies Drops, arrivé avec le festival <em>Biohazard &amp; Bountiful Autumn Festival</em> annoncé le 24 septembre 2026. C’est le mode le plus rentable du jeu pour qui sait le jouer, parce qu’il inverse entièrement l’économie du risque. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Caractéristique</th><th>Valeur</th><th>Conséquence pratique</th></tr></thead>
              <tbody>
                <tr><td>Type</td><td>Co-op décontracté, PvPvE</td><td>On joue pour les objectifs, pas pour survivre</td></tr>
                <tr><td>Équipement</td><td>Entièrement fourni par le système</td><td>Votre stuff et votre stash ne sont pas en jeu</td></tr>
                <tr><td>Réapparitions</td><td>Illimitées</td><td>Un mort est un délai, pas une perte</td></tr>
                <tr><td>Récompense</td><td>Caisse d’équipe + caisse personnelle</td><td>Seul le contenu de la caisse est réglé</td></tr>
                <tr><td>Progression</td><td>Caisse de niveau 1 → 5</td><td>Chaque niveau ajoute des rangées de stockage</td></tr>
                <tr><td>Objectifs</td><td>Terminaux standard + un terminal confidentiel</td><td>La densité d’XP est entièrement dans les terminaux</td></tr>
                <tr><td>Débloqué</td><td>Smelter au niveau 3</td><td>Conversion d %}</td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout callout-danger">
            <h4>La règle qui décide de tout : ne quittez pas avant la fin</h4>
            <p>Les récompenses sont payées <strong>quand le raid se termine</strong>. Quitter le mode en cours de route vide votre progression et transforme vos dépôts en rien. Les respawns illimités ne sont pas une permission de cash out au milieu du match. Comptez environ 10 à 12 minutes de raid et gardez l’onglet du timer sous les yeux. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="crate">2. La caisse de récompense : cinq niveaux</h2>
          <p>En Supplies Drops 2.0, on ne « sort » pas un sac à dos de loot. On remplit deux caisses : une <strong>Caisse de récompense d’équipe</strong> partagée et une <strong>Caisse de récompense personnelle</strong>. Le nombre de <strong>rangées</strong> de chaque caisse est la limite stricte de ce que vous conservez, et la seule façon d’ajouter des rangées pendant le raid est de monter le niveau de la caisse. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Niveau</th><th>Ce que vous gagnez</th><th>Effet concret</th><th>Priorité</th></tr></thead>
              <tbody>
                <tr><td><strong>Niveau 1</strong></td><td>4 rangées de départ</td><td>État initial de la caisse d’équipe</td><td>Base</td></tr>
                <tr><td><strong>Niveau 2</strong></td><td>+1 rangée à la caisse d’équipe</td><td>Plus de volume collectif</td><td>Haute</td></tr>
                <tr><td><strong>Niveau 3</strong></td><td><strong>Débloque le Smelter</strong></td><td>Conversion illimitée des objets violets et inférieurs</td><td>Haute — c’est le meilleur palier</td></tr>
                <tr><td><strong>Niveau 4</strong></td><td>+1 rangée à la caisse d’équipe</td><td>Deuxième extension collective</td><td>Moyenne</td></tr>
                <tr><td><strong>Niveau 5</strong></td><td>+1 rangée à la caisse d’équipe <em>et</em> à la caisse personnelle</td><td>Seul niveau qui fait grandir votre part individuelle</td><td>Maximale</td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout callout-success">
            <h4>Traitez le niveau 5 comme l’objectif du raid</h4>
            <p>Trois des cinq niveaux étendent directement votre capacité, et le dernier est le seul à agrandir votre part personnelle. Une équipe qui plafonne au niveau 3 laisse deux rangées d’équipe et une rangée personnelle sur la table — c’est une part considérable de la valeur réglée qui disparaît. L’XP de caisse vient de trois sources : <strong>fouiller des conteneurs</strong>, <strong>éliminer des joueurs</strong>, et <strong>interagir avec les terminaux</strong>. Les terminaux sont de loin les plus denses en XP. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <figure class="page-figure">
            <img src="../img/events/reward-crate-terminal.jpg" alt="Console de terminal militaire avec interface holographique cyan dans un entrepot industriel" loading="lazy">
            <figcaption>Le terminal est l’objet le plus rentable de la carte : c’est là que se concentre l’XP de caisse.</figcaption>
          </figure>

          <h2 id="terminals">3. Les deux types de terminaux</h2>
          <p>Ce sont eux qui définissent le rythme du raid, et ils se traitent de façon opposée. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="lore-grid">
            <div class="lore-card north">
              <h4>Terminal standard</h4>
              <div class="lore-sub">Plusieurs sur la carte · XP faible</div>
              <p>Chaque équipe peut interagir avec <strong>chaque terminal une seule fois</strong>, et chaque interaction rapporte une petite quantité d’XP de caisse. Le montant est fixe, le plafond est par équipe : c’est une course.</p>
              <ul>
                <li><strong>Faites-les tôt.</strong> Le total est plafonné, donc le dernier arrivé n’y gagne rien.</li>
                <li><strong>Divisez l’équipe en deux.</strong> Deux binômes sur des côtés opposés de la carte doublent votre ingestion d’XP et vous révèlent les positions ennemies plus tôt.</li>
                <li><strong>Ne les traitez pas comme un objectif à défendre.</strong> Vous les activez et vous repartez.</li>
              </ul>
            </div>
            <div class="lore-card south">
              <h4>Terminal confidentiel</h4>
              <div class="lore-sub">Un seul sur toute la carte · XP élevé</div>
              <p>Il n’existe <strong>qu’un seul terminal confidentiel</strong> sur la carte entière. Après interaction, l’équipe doit <strong>rester et le défendre</strong> pendant la durée du chronomètre, et les autres équipes peuvent contester. La sécurisation rapporte une grosse quantité d’XP de caisse, assez à sauter un niveau à elle seule.</p>
              <ul>
                <li><strong>Ne l’activez pas en arrivant.</strong> Déployez-vous, nettoyez les angles de tir, puis déclenchez : l’activation est ce qui annonce votre position à toute la carte.</li>
                <li><strong>Tenez les angles, pas le terminal.</strong> Avec des réapparitions illimitées, sacrifier des corps pour protéger le point est un échange gagnant.</li>
                <li><strong>Attendez-vous à de la compagnie en fin de raid.</strong> C’est la plus grosse source d’XP de la carte : les meilleures équipes y convergent en milieu et fin de raid, au moment où la fréquence des airdrops monte aussi.</li>
              </ul>
            </div>
          </div>

          <h2 id="smelter">4. Le Smelter : votre multiplicateur de loot au niveau 3</h2>
          <p>Lorsque la caisse atteint le <strong>niveau 3</strong>, le Smelter se débloque. La note officielle est explicite : <em>« les joueurs peuvent l’utiliser pour fondre des objets de qualité Violette ou inférieure en nouveaux objets, sans limite d’usage »</em>. <span class="src-tag src-officiel">Officiel</span></p>

          <figure class="page-figure">
            <img src="../img/events/smelter-forge.jpg" alt="Four de fusion industriel dans une installation souterraine, coulée de metal en fusion et etincelles" loading="lazy">
            <figcaption>Le Smelter transforme le fond de votre sac — verts, bleus, violets — en tirages. Sans limite d’usage, il n’y a aucune raison de le laisser inactif.</figcaption>
          </figure>

          <p>La clause <strong>sans limite d’usage</strong> est celle que la plupart des équipes ignorent. Elle a deux conséquences : elle transforme le bruit de fond de vos butins (verts, bleus, violets) en tickets de tirage, et comme il n’y a pas de limite, il n’y a aucune raison de laisser le four inactif une fois ouvert.</p>
          <ul>
            <li><strong>La boucle pratique</strong> : dès le niveau 3, fais passer au Smelter chaque objet violet ou inférieur dont tu n’as pas besoin, au lieu de le déposer tel quel dans la caisse.</li>
            <li><strong>C’est la même mécanique que le festival</strong> : <em>Trash to Treasure</em> est le pendant événementiel du Smelter du mode. L’habitude paie sur les deux.</li>
            <li><strong>Priorité.</strong> Le Smelter est un excellent motif pour viser le niveau 3 vite : une caisse qui ne fait que remplir des verts bruts gaspille le meilleur outil de conversion du mode.</li>
          </ul>

          <div class="callout callout-warning">
            <h4>Ce qu’on sait des seuils — et ce qu’on ne sait pas</h4>
            <p>Des seuils de rendement du Smelter circulent sur Reddit, avec des tables de quantités et de probabilités observées par les joueurs. <strong>Ce ne sont pas des données publiées par l’éditeur</strong> et les résultats sont explicitement aléatoires : la note officielle parle d’une <em>« chance »</em> d’obtenir le Prototype Calculation Module, pas d’une garantie. Considérez ces chiffres comme des observations de terrain, jamais comme des garanties de rendement. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <h2 id="airdrop">5. Airdrops, IA blindée et rythme du raid</h2>
          <p>Le rework 2.0 a modifié plusieurs paramètres du mode. Ce sont des leviers concrets si on sait qu’ils existent. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Modification</th><th>Effet</th><th>Comment l’exploiter</th></tr></thead>
              <tbody>
                <tr><td><strong>Valeur du pass et du loot augmentée</strong></td><td>Chaque raid vaut plus qu’en Supplies Drops S6</td><td>Jouez le raid complet, ne sortez pas au premier tour</td></tr>
                <tr><td><strong>Temps de réapparition croissant</strong></td><td>Les morts du début sont presque gratuits, ceux de la fin coûtent cher</td><td>jouez large en ouverture, resserrez une fois le terminal confidentiel lancé</td></tr>
                <tr><td><strong>Fréquence des airdrops en hausse</strong></td><td>Les drops se concentrent en milieu et fin de raid</td><td>Gardez votre vigilance de carte pour la seconde moitié</td></tr>
                <tr><td><strong>Unités IA lourdement blindées</strong></td><td>Ce ne sont pas des kills gratuits ; il faut de la pénétration</td><td>Adaptez votre niveau Pierce à leur blindage</td></tr>
                <tr><td><strong>Annonces de kill et d’XP</strong></td><td>Informations audio sur les événements</td><td>Utilisez-les pour suivre la phase du raid</td></tr>
                <tr><td><strong>Numéros d’équipe et annonces vocales</strong></td><td>Repérage instantané des coéquipiers</td><td>Communiquez moins au micro, l’information est déjà là</td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout callout-danger">
            <h4>L’erreur classique : videz votre magazine sur une IA blindée</h4>
            <p>Ces unités apparaissent à un moment où la contest du terminal va commencer. Gaspiller tout votre chargeur sur une IA blindée à la mauvaise entrée du terminal, c’est perdre le point et le temps de réapparition d’un coup. Emportez assez de pénétration, mais tenez-vous en réserve pour le contest. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="strategie">6. Stratégie d’équipe</h2>
          <p>Comme le loadout est fourni et les réapparitions illimitées, Supplies Drops 2.0 inverse la logique d’extraction : vous ne risquez rien, donc il n’y a aucune raison de jouer prudent. <span class="src-tag src-officiel">Officiel</span></p>

          <ol class="steps">
            <li><strong>Répartissez les rôles au lancement.</strong> Deux joueurs balaient les terminaux standard et ouvrent les conteneurs ; deux autres se positionnent vers le terminal confidentiel. Vous convergez pour la contest.</li>
            <li><strong>Butez sur les objectifs, pas sur la survie.</strong> Votre stash n’est pas en jeu. Échangez agressivement pour taguer les terminaux et tenir le point confidentiel.</li>
            <li><strong>Portez de la pénétration pour les IA blindées.</strong> Le match se joue sur le Pierce Level de vos munitions contre leur blindage.</li>
            <li><strong>Poussez le niveau 5 avant de relâcher.</strong> Le dernier niveau est le seul qui ouvre une ligne à votre caisse personnelle ; tant que l’équipe tient et que le raid est jeune, continuez à alimenter la caisse.</li>
            <li><strong>Traquez les airdrops en fin de raid.</strong> Leur fréquence monte dans la seconde moitié : c’est là que se trouve le volume de loot brut, une fois la caisse agrandie.</li>
            <li><strong>Restez jusqu’au chronomètre zéro.</strong> Le règlement se fait à la fin. Sortir tôt vide tout.</li>
          </ol>

          <h2 id="erreurs">7. Les erreurs qui coûtent le plus cher</h2>
          <div class="dodont">
            <div class="dd-card dd-do">
              <h4>Ce qu’il faut faire</h4>
              <ul>
                <li>Balayer les terminaux standard <strong>dès l’ouverture</strong>, en parallèle sur deux axes de la carte.</li>
                <li>Traiter le terminal confidentiel comme un <strong>objectif à tenir</strong>, pas comme un conteneur.</li>
                <li>Atteindre le niveau 3 pour ouvrir le Smelter, puis ne jamais le laisser inactif.</li>
                <li>Utiliser la caisse <strong>personnelle</strong> pour les objets uniques et irremplaçables, la caisse <strong>d’équipe</strong> pour le surplus commun.</li>
                <li>Rester jusqu’à la fin du raid, même si votre part est déjà pleine.</li>
              </ul>
            </div>
            <div class="dd-card dd-dont">
              <h4>Ce qu’il ne faut surtout pas faire</h4>
              <ul>
                <li><strong>Quitter le raid avant la fin</strong> : la progression est perdue, pas mise en attente.</li>
                <li>Porter en backpack ce qui doit être déposé : seul le contenu de la caisse est réglé.</li>
                <li>Jouer passivement en pensant à « survivre » : votre stuff n’est pas en jeu, le mode n’enregistre pas ce réflexe.</li>
                <li>Traiter le terminal confidentiel trop tôt et sans couverture.</li>
                <li>Changer d’itinéraire au milieu du raid sans prévenir : le mode est fait pour converger.</li>
              </ul>
            </div>
          </div>

          <h2 id="trash">8. Trash to Treasure : le pendant événementiel du Smelter</h2>
          <p><strong>Trash to Treasure</strong> est l’événement de fusion d’items d’Arena Breakout: Infinite. Au lancement, MoreFun a expliqué que <em>« des fours apparaissent sur diverses cartes dans les zones Lockdown et Forbidden. Soumettez des objets divers en raid pour avoir une chance de recycler des déchets en trésor ! »</em> Le flux en jeu tient en trois étapes : trouver le four, soumettre <strong>3 objets divers</strong>, puis réclamer le résultat une fois la fusion terminée. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Formule</th><th>Ingrédients</th><th>Résultat possible</th><th>Disponible (UTC+0)</th></tr></thead>
              <tbody>
                <tr><td><strong>Trash to Treasure</strong></td><td>Personal Digital Assistant + Data Cable + Laptop</td><td>Prototype Calculation Module (collectible de valeur)</td><td>29 oct. – 15 nov. 2026</td></tr>
              </tbody>
            </table>
          </div>

          <div class="evt-alert">
            <h4>La formule Halloween est close depuis le 15 novembre 2026</h4>
            <p>Au 17 novembre, cette formule n’est plus disponible. Ce qui reste accessible, c’est le <strong>Smelter du mode Supplies Drops 2.0</strong>, débloqué au niveau 3 de caisse, sans limite d’usage et fonctionnant sur les objets violets ou inférieurs. C’est le relais naturel pour ceux qui exploitaient la formule d’octobre. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h3>Peut-on acheter les ingrédients pour courir au four ?</h3>
          <p>C’est exactement la question posée sur Reddit cette semaine. Les réponses des joueurs indiquent que les <strong>objets fournis par l’opérateur ne peuvent pas être fondus</strong> : on peut acheter des objets violets ou inférieurs, mais il faut qu’ils sortent d’un raid pour perdre leur marque « fourni ». MoreFun n’a pas confirmé ce point : traitez-le comme un test communautaire. <span class="src-tag src-communautaire">Communauté</span></p>
          <p>En revanche, une limite est explicitement documentée : dans la mise à jour en direct du 15 juillet 2026, MoreFun a interdit un objet supplémentaire <em>« conformément aux autres objets divers de qualité Or »</em>, confirmant que les objets divers de qualité Or ne peuvent pas être emportés en raid. Tout ingrédient de qualité Or doit donc être trouvé <strong>dans le raid même</strong> où vous voulez l’utiliser. <span class="src-tag src-officiel">Officiel</span></p>
          <ul>
            <li>Faites sortir une fois les ingrédients de moindre qualité d’un raid, pour qu’ils perdent la marque « fourni ».</li>
            <li>Emportez-les ensuite dans chaque raid Lockdown ou Forbidden.</li>
            <li>Récupérez la pièce de qualité Or pendant le raid, puis filez droit vers un four.</li>
            <li>Les notes 2026 ne précisent pas la qualité de chaque ingrédient : vérifiez la couleur de l’objet dans le client avant de planifier.</li>
          </ul>

          <h2 id="biohazard-modes">9. Les modes infectés de la Saison 7</h2>
          <p>Supplies Drops 2.0 n’est pas le seul mode événementiel de la saison. La série Biohazard a introduit deux modes qui partagent les mêmes objets d’événement. <span class="src-tag src-officiel">Officiel</span></p>

          <figure class="page-figure">
            <img src="../img/events/extermination-hazmat.jpg" alt="Operateurs en combinaison hazmat jaune avec respirateurs avances dans un couloir industriel contamine, lueur ambre et brume toxique" loading="lazy">
            <figcaption>Les zones infectées de la Saison 7 ajoutent un bonus de risque et un loot rouge plus généreux. Masque, sprint court et Elysium en priorité.</figcaption>
          </figure>


          <div class="event-grid">
            <div class="event-card live">
              <h4>Infected Area <span class="evt-badge evt-live">En cours</span></h4>
              <span class="evt-dates">Depuis le 16 sept. 2026</span>
              <p>Un raid Tactique classique dans une zone occupée par des zombies mutants et des boss de classe Élite affaiblis. Le loot rouge de zone y est plus généreux, et les tickets <strong>Zombie No Man’s Land</strong> y droppent.</p>
              <div class="evt-meta">À faire avec un masque, un sprint court et Elysium en priorité. La S7 a ajouté des variantes plus faibles des quatre classes d’élite, plus des boss mutants.</div>
            </div>
            <div class="event-card live">
              <h4>Zombie Endless <span class="evt-badge evt-live">En cours</span></h4>
              <span class="evt-dates">Depuis le 16 sept. 2026</span>
              <p>Un mode à score cumulé où l’objectif est votre <strong>Merit</strong>. C’est le mode qui alimente le <strong>Merit Challenge</strong>, la piste la plus rentable de la saison : conversion en Koen ×3, jusqu’à 3 000 000 Koen par semaine.</p>
              <div class="evt-meta">Le patch du 27 octobre 2026 a abaissé le Merit total requis pour monter de niveau et facilité plusieurs missions « Enter Infected Zone ».</div>
            </div>
            <div class="event-card live">
              <h4>Extermination Mission <span class="evt-badge evt-live">Hebdomadaire</span></h4>
              <span class="evt-dates">Remise chaque lundi à 05:00 UTC+0</span>
              <p>Une piste hebdomadaire d’élimination d’infectés qui débouche sur la <strong>tenue Hazmat complète</strong> via les Supply Passes. Un équipement d’événement entier obtenu gratuitement n’est pas rare.</p>
              <div class="evt-meta">Attention : pas de report. Ce qui n’est pas remis le lundi repart à zéro.</div>
            </div>
            <div class="event-card closed">
              <h4>Trash to Treasure <span class="evt-badge evt-closed">Terminé</span></h4>
              <span class="evt-dates">29 oct. – 15 nov. 2026</span>
              <p>La formule événementielle du four : PDA + câble + portable, avec une chance d’obtenir le Prototype Calculation Module.</p>
              <div class="evt-meta">Fermée le 15 novembre. La version 2.0 du Smelter, elle, reste ouverte dans Supplies Drops 2.0.</div>
            </div>
          </div>

          <h2 id="merit">10. Ce que le mode rapporte vraiment</h2>
          <p>Il faut distinguer deux choses : ce que le mode donne <em>directement</em>, et ce qu’il alimente <em>ailleurs</em>. <span class="src-tag src-officiel">Officiel</span></p>
          <ul>
            <li><strong>Directement</strong> : la caisse d’équipe et la caisse personnelle, réglées au changement de phase du raid, plus les objets convertis au Smelter à partir du niveau 3.</li>
            <li><strong>En plus</strong> : le <strong>Merit Challenge</strong> est hebdomadaire et se joue en <strong>Zombie Endless</strong>, pas en Supplies Drops. C’est le plus gros chiffre de la saison, mais il vient d’un autre mode.</li>
            <li><strong>Par ailleurs</strong> : les objets de la <strong>série Biohazard</strong> et les <strong>Zombies No Man’s Land Passes</strong> tombent en Infected Area, pas en Supplies Drops.</li>
            <li><strong>En pratique</strong> : Supplies Drops 2.0 est le mode où votre équipement ne risque rien. C’est le moment idéal pour “tester” un kit ou apprendre une carte, et le mode le plus stable en Koen brut.</li>
          </ul>

          <div class="callout callout-danger">
            <h4>Ce que le mode n’est pas</h4>
            <p>Supplies Drops 2.0 n’est pas le mode Hostile Sector, pas l’arbre de maîtrise, et pas un système de Secure Case. C’est un mode événementiel à durée limitée, qui a déjà tourné une fois en S6 et tourne en S7 : il n’est pas garanti qu’il sera présent à la prochaine saison. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="sources">11. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Biohazard &amp; Bountiful Autumn Festival</span> — annonce du 24 septembre 2026 : progression de la caisse à 5 niveaux, types de terminaux,déblocage du Smelter, airdrops, IA blindée, annonces de kill et d’XP. <a href="https://x.com/ArenaBreakoutPC/status/2103092246711275780" target="_blank" rel="noopener">x.com/ArenaBreakoutPC</a></li>
            <li><span class="src-name">Live Update du 27 octobre 2026</span> — formule Trash to Treasure, emplacement des fours en Lockdown et Forbidden Zone, interdiction des objets divers de qualité Or (patch du 15 juillet 2026). <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">Notes de la Saison 7 — Utopia</span> — 15 septembre 2026 : modes Infected Area et Zombie Endless, règles d’arme et changements d’équilibre. <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">timesaver.gg — Supplies Drops 2.0 Guide</span> — ordre de priorité des objectifs, répartition des rôles, hiérarchie de la caisse, pièges du mode. <a href="https://timesaver.gg/blog/arena-breakout-infinite-supplies-drops-2-strategy" target="_blank" rel="noopener">timesaver.gg</a></li>
            <li><span class="src-name">overgear.com — Supply Drops</span> — règles d’origine du mode : pass d’entrée ou Koen, caisses personnelles et d’équipe, airdrops, dog tags. <a href="https://overgear.com/guides/arena-breakout/supply-drops/" target="_blank" rel="noopener">overgear.com</a></li>
            <li><span class="src-name">gamers.wiki — Arena Breakout: Infinite</span> — règles du mode d’origine (niveau 6 requis, 300 000 Koen d’entrée) et usage des caisses. <a href="https://gamers.wiki/en/games/arena-breakout-infinite/wiki" target="_blank" rel="noopener">gamers.wiki</a></li>
            <li><span class="src-name">r/ArenaBreakoutInfinite</span> — fil « Smelter PSA » (seuils observés), fil sur les objets fournis non fondables, discussions sur la répartition des gains entre caisses personnelle et d’équipe. <a href="https://www.reddit.com/r/ArenaBreakoutInfinite/comments/1v3m0i0/smelter_psa/" target="_blank" rel="noopener">reddit.com</a></li>
          </ul>
          <h3>Non confirmé</h3>
          <ul class="src-list">
            <li>Les <strong>seuils et probabilités du Smelter</strong> rapportés sur Reddit sont des observations de joueurs, jamais publiées par l’éditeur ; les résultats sont aléatoires par conception.</li>
            <li>Le fait que les <strong>objets fournis par l’opérateur ne puissent pas être fondus</strong> repose sur des tests communautaires. Seule l’interdiction des objets divers de qualité Or est explicitement documentée dans les correctifs.</li>
            <li>Le tableau de points par placement (<strong>+3 / +1 / 0 / −1 / −1</strong> en Warlord) est une reconstruction communautaire à partir de l’édition précédente, pas une grille publiée par MoreFun.</li>
          </ul>
        """
