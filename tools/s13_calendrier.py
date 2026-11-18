# -*- coding: utf-8 -*-
"""S13 — Contenu de la page events-calendrier.html."""

CONTENT = r"""
          <div class="evt-legend">
            <span class="evt-badge evt-live">En cours</span><span class="lg-txt">événement actif au 17 novembre 2026</span>
            <span class="evt-badge evt-soon">Bientôt</span><span class="lg-txt">annoncé, pas encore ouvert</span>
            <span class="evt-badge evt-closed">Terminé</span><span class="lg-txt">date de fin dépassée</span>
            <span class="evt-badge evt-unconfirmed">Non confirmé</span><span class="lg-txt">ni annonce officielle ni date stable</span>
          </div>

          <div class="facts">
            <div class="fact"><span class="fact-label">Saison en cours</span><span class="fact-value">Saison 7 — Utopia (depuis le 16 septembre 2026)</span></div>
            <div class="fact"><span class="fact-label">État au</span><span class="fact-value">17 novembre 2026, 08:00 UTC+0</span></div>
            <div class="fact"><span class="fact-label">Événements actifs</span><span class="fact-value">4 pages de règles simultanées</span></div>
            <div class="fact"><span class="fact-label">Prochaine échéance</span><span class="fact-value">Tea Break Delights — 22 novembre</span></div>
          </div>

          <figure class="page-figure">
            <img src="../img/events/loot-fest-arena.jpg" alt="Scene de competition e-sport sur une grande scene avec ecrans geants et jury en silhouette" loading="lazy">
            <figcaption>Les événements d’Arena Breakout: Infinite tournent en couches : un festival saisonnier, un mode, un concours et des pistes hebdomadaires partagent le même calendrier.</figcaption>
          </figure>

          <h2 id="statut">1. Où en est la Saison 7 au 17 novembre 2026</h2>
          <p>La Saison 7 <em>Utopia</em> a démarré le <strong>16 septembre 2026</strong> et n’a pas de date de fin officielle : elle s’arrête quand la Saison 8 commence, et cette date n’a pas été annoncée. En revanche, tous les événements à durée limitée de la saison ont des dates finies, et la plupart tombent entre le 15 novembre et le 7 décembre. <span class="src-tag src-officiel">Officiel</span></p>
          <p>Concrètement, au 17 novembre 2026, la situation est la suivante :</p>
          <ul>
            <li><strong>Quatre événements sont encore ouverts</strong> : Mysterious Pumpkin Night (jusqu’au 25/26 novembre), Dim Dou Duk Gourmet Market (6 décembre), le Troisième Warlord Tournament (7 décembre) et la série Biohazard avec ses pistes hebdomadaires.</li>
            <li><strong>Deux événements viennent de fermer</strong> : la formule Smelter <em>Trash to Treasure</em> (15 novembre) et l’échantillon de sol lunaire (9 novembre).</li>
            <li><strong>Un seul événement est encore en investigation</strong> : Kamona Investigation — Tea Break Delights (22 novembre), et c’est le plus urgent.</li>
            <li><strong>La Saison 8 n’a aucune date officielle.</strong> Les sources communautaires convergent sur une fenêtre de lancement entre le 3 et le 14 décembre 2026, mais ce n’est qu’une estimation fondée sur la durée des trois dernières saisons. <span class="src-tag src-theorie">Théorie</span></li>
          </ul>

          <div class="evt-alert">
            <h4>Le point de vigilance du 17 novembre</h4>
            <p>La <strong>Kamona Investigation — Tea Break Delights</strong> ferme le <strong>22 novembre 2026</strong> : il reste <span class="d-count">5 jours</span>. C’est la seule piste encore active qui demande de <em>rendre</em> quatre objets (lait, miel, pellicule et raviolis Dim Dou Duk). Les événements de collecte pure, eux, ne disparaissent pas quand on arrête de les farm — mais une investigation non rendue, elle, disparaît avec son stock. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="principes">2. Comment fonctionnent les événements chez MoreFun</h2>
          <p>Le jeu n’a pas une seule catégorie d’ « événement ». Il y en a six, et elles se combinent. Confondre deux catégories est la première cause de mauvaise programmation : on passe une heure à farmer un objet qui n’a aucun intérêt pour la piste qu’on vise. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="lore-grid">
            <div class="lore-card gold">
              <h4>Le festival saisonnier</h4>
              <div class="lore-sub">Rotation — 4 à 8 semaines</div>
              <p>Le plus gros dispositif : un thème (Halloween, Biohazard, Été) qui ajoute une dizaine de pistes de récompenses sur plusieurs semaines. Chaque festival a sa date d’ouverture et sa date de fin, souvent échelonnées piste par piste.</p>
              <ul>
                <li><strong>Biohazard &amp; Bountiful Autumn Festival</strong> — 24 septembre au 28 octobre 2026.</li>
                <li><strong>Mysterious Pumpkin Night</strong> — 29 octobre au 25/26 novembre 2026.</li>
                <li><strong>Dim Dou Duk Collaboration</strong> — 9 novembre au 6 décembre 2026.</li>
              </ul>
            </div>
            <div class="lore-card north">
              <h4>Le mode événementiel</h4>
              <div class="lore-sub">Rotation — 2 à 6 semaines</div>
              <p>Un mode de jeu à part entière, avec ses propres règles de score et son propre écran de récompense. On y entre avec un pass ou des Koen, et on en sort avec une crate à régler.</p>
              <ul>
                <li><strong>Supplies Drops 2.0</strong> — co-op, réapparitions illimitées, crate à niveaux.</li>
                <li><strong>Zombie Endless</strong> et <strong>Infected Area</strong> — modes infectés de la S7.</li>
                <li><strong>Secure Ops</strong> — on garde son équipement même en mourant.</li>
                <li><strong>Hostile Sector</strong> — secteurs reinforced, rotations de haut niveau.</li>
              </ul>
            </div>
            <div class="lore-card south">
              <h4>Le concours</h4>
              <div class="lore-sub">Classement — 3 à 6 semaines</div>
              <p>Un classement séparé du rang de saison, où l’on monte par étoiles. Les règles ont changé à chaque édition, ce qui rend obsolètes les guides des tours précédents.</p>
              <ul>
                <li><strong>Troisième Warlord Tournament</strong> — 29 octobre au 7 décembre 2026.</li>
                <li>Une piste de missions parallèle distribue des jetons échangeables.</li>
              </ul>
            </div>
            <div class="lore-card neutral">
              <h4>La piste d’enquête</h4>
              <div class="lore-sub">Collecte et remise — 2 semaines</div>
              <p>Le joueur collecte une liste d’objets imposés et les rend à l’écran d’événement. La fenêtre est courte et le stock nécessaire peut être volumineux.</p>
              <ul>
                <li><strong>Kamona Investigation</strong> — phase <em>Tea Break Delights</em>, 9 au 22 novembre 2026.</li>
                <li>Une seconde couche, <em>Investigate Drawers</em>, overlaps la première.</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>La piste hebdomadaire</h4>
              <div class="lore-sub">Remise le lundi à 05:00 UTC+0</div>
              <p>Ces pistes se réinitialisent chaque semaine. Ce qui n’est pas rendu le lundi disparaît : il n’y a pas de report.</p>
              <ul>
                <li><strong>Extermination Mission</strong> — tenue Hazmat complète.</li>
                <li><strong>Merit Challenge</strong> — jusqu’à 3 000 000 Koen par semaine.</li>
                <li><strong>Zombies No Man’s Land</strong> — passes de connexion et de jalons.</li>
              </ul>
            </div>
            <div class="lore-card">
              <h4>La collecte d’objets d’événement</h4>
              <div class="lore-sub">Court — 1 à 4 semaines</div>
              <p>Des objets rares dropés en raid dans des contenants précis, avec une date d’expiration. On les dépense ou on les échange hors raid.</p>
              <ul>
                <li><strong>Dim Sum Vouchers</strong> — sacs de sport et valises, toutes cartes.</li>
                <li><strong>Lunar Soil Sample</strong> — 780 000 Koen, coffres, jusqu’au 9 novembre.</li>
                <li><strong>Festive Pumpkin</strong> — achetable, évolutif, non protégeable.</li>
              </ul>
            </div>
          </div>

          <h2 id="echeances">3. Toutes les échéances de la Saison 7</h2>
          <p>Le tableau ci-dessous est l’outil de travail principal. Les dates sont celles des notes officielles et des annonces du compte officiel ; la colonne « reste » est calculée au 17 novembre 2026.</p>

          <ul class="evt-deadlines">
            <li>
              <span class="d-date">9 nov. 2026</span>
              <span class="d-name">Lunar Soil Sample <em>Échantillon de sol lunaire — 780 000 Koen, dans les coffres, toutes cartes</em></span>
              <span class="d-left done">Terminé — il y a 8 j</span>
            </li>
            <li>
              <span class="d-date">15 nov. 2026</span>
              <span class="d-name">Trash to Treasure <em>Formule Smelter Halloween : PDA + Câble de données + Ordinateur portable</em></span>
              <span class="d-left done">Terminé — il y a 2 j</span>
            </li>
            <li>
              <span class="d-date">22 nov. 2026</span>
              <span class="d-name">Kamona Investigation — Tea Break Delights <em>Lait, miel, pellicule, raviolis Dim Dou Duk à rendre</em></span>
              <span class="d-left hot">5 jours</span>
            </li>
            <li>
              <span class="d-date">25 nov. 2026</span>
              <span class="d-name">Mysterious Pumpkin Night <em>Fin officielle : 26 nov. à 05:00 UTC — 6 sous-événements</em></span>
              <span class="d-left hot">8 jours</span>
            </li>
            <li>
              <span class="d-date">6 déc. 2026</span>
              <span class="d-name">Dim Dou Duk Collaboration — Gourmet Market <em>Dim Sum Vouchers, sacs de sport et valises</em></span>
              <span class="d-left warm">19 jours</span>
            </li>
            <li>
              <span class="d-date">7 déc. 2026</span>
              <span class="d-name">Troisième Warlord Tournament <em>Classement séparé, 5 paliers, 30 étoiles au sommet</em></span>
              <span class="d-left warm">20 jours</span>
            </li>
            <li>
              <span class="d-date">Hebdomadaire</span>
              <span class="d-name">Extermination Mission, Merit Challenge, Zombies No Man’s Land <em>Remise chaque lundi à 05:00 UTC+0</em></span>
              <span class="d-left warm">En cours</span>
            </li>
            <li>
              <span class="d-date">Non annoncé</span>
              <span class="d-name">Saison 8 — Utopia II <em>Aucune date officielle au 17 novembre 2026</em></span>
              <span class="d-left">Estimation : 3–14 déc.</span>
            </li>
          </ul>

          <div class="callout callout-warning">
            <h4>Fin d’Halloween : 25 ou 26 novembre ?</h4>
            <p>L’annonce officielle précise que la série Halloween est disponible <em>« du 29 octobre à 05:00 UTC jusqu’au 26 novembre »</em>. L’ensemble des guides affiche « 25 novembre » parce qu’il raisonne en journées UTC+0 pleines. Les deux lectures désignent le même instant : la coupure est fixée au <strong>26 novembre 2026 à 05:00 UTC</strong>, soit la fin de la journée du 25 novembre en UTC+0. Si vous planifiez une extraction de citrouille, visez le 25 au soir, pas le 26 au matin. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="festival">4. Le festival d’automne : Biohazard &amp; Bountiful Autumn Festival</h2>
          <p>Le festival d’automne a été annoncé le <strong>24 septembre 2026</strong>, neuf jours après le lancement de la Saison 7, et a superposé ses pistes à la série Biohazard déjà en cours. Il a produit l’essentiel des récompenses de la saison : 4 800 Bonds gratuits, 14 tickets Zombie No Man’s Land, un skin gratuit de niveau S de classe Tac-Master, et des pistes à plusieurs millions de Koen. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Piste</th><th>Ouverture</th><th>Ce que vous faites</th><th>Récompense</th><th>Statut</th></tr></thead>
              <tbody>
                <tr><td><strong>Autumn Gift</strong></td><td>24 sept.</td><td>Connexion et petites tâches</td><td>Skins d’arme gratuits</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Bountiful Autumn Store</strong></td><td>28 sept.</td><td>Échanger des points</td><td>Skins, dont un Tac-Master au choix (T191 ou M24)</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Bountiful Autumn Challenge</strong></td><td>28 sept.</td><td>Défis d’automne</td><td>Random Featured Weapon Bundle</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Lunar Soil Sample</strong></td><td>24 sept.</td><td>Chercher dans les coffres</td><td>Collectible 2×2 à 780 000 Koen</td><td><span class="evt-badge evt-closed">Terminé le 9 nov.</span></td></tr>
                <tr><td><strong>Extermination Mission</strong></td><td>Hebdo</td><td>Éliminer des infectés</td><td>Tenue Hazmat complète via Supply Passes</td><td><span class="evt-badge evt-live">En cours</span></td></tr>
                <tr><td><strong>Merit Challenge</strong></td><td>Hebdo</td><td>Meilleur Merit hebdo en Biohazard Endless</td><td>Conversion en Koen ×3, jusqu’à 3 000 000 Koen/sem.</td><td><span class="evt-badge evt-live">En cours</span></td></tr>
                <tr><td><strong>Zombies No Man’s Land</strong></td><td>Hebdo</td><td>Connexion + jalons 4/8/16 tâches</td><td>Passes de connexion ; passes en Infected Area</td><td><span class="evt-badge evt-live">En cours</span></td></tr>
                <tr><td><strong>Dark Zone Patrol</strong></td><td>28 sept.</td><td>Envoyer Paul patrouiller</td><td>Objets de valeur trouvés par le compagnon</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Vinson’s Challenge</strong></td><td>28 sept. – 28 oct.</td><td>Dépenser des Koen sur la page</td><td>Récompenses de défi (Koen non remboursable)</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Trash to Treasure</strong></td><td>24 sept. → 15 nov.</td><td>Smelter en raid</td><td>Module de calcul prototype</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Upgrade Battle Pass</strong></td><td>24 sept. → 28 oct.</td><td>500 Bonds instantanés</td><td>Skins, tenue, Koen</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
                <tr><td><strong>Bundles limités</strong></td><td>24 sept. → 28 oct.</td><td>6 bundles à 4,50 $</td><td>450 Bonds + carte Élite 7 j + skin exclusif</td><td><span class="evt-badge evt-closed">Terminé</span></td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout callout-success">
            <h4>La piste la plus rentable de la saison n’est pas une collecte</h4>
            <p>Le <strong>Merit Challenge</strong> convertit votre meilleur score de Merit hebdomadaire en Biohazard Endless en Koen, avec un multiplicateur de 3, jusqu’à <strong>3 000 000 Koen par semaine</strong>. Aucun autre dispositif de la saison n’approche ce montant, et il ne demande ni objet rare ni risque supplémentaire. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="halloween">5. Mysterious Pumpkin Night — le détail des six sous-événements</h2>
          <p>La saison Halloween 2026 est nommée <strong>Mysterious Pumpkin Night</strong> dans les notes, et le volet citrouille s’appelle <strong>Pumpkin Evolution II</strong>. Ce n’est pas la première fois : la version 2025 s’était tenue du 24 octobre au 13 novembre 2025, soit 21 jours. La version 2026 dure 28 jours. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Sous-événement</th><th>Dates</th><th>Objectif</th><th>Récompense clé</th></tr></thead>
              <tbody>
                <tr><td><strong>Pumpkin Evolution II</strong></td><td>29 oct. – 25 nov.</td><td>Entrer une Festive Pumpkin en raid et en extraire</td><td>Citrouilles évoluées, jusqu’à 880 000 Koen</td></tr>
                <tr><td><strong>Mysterious Night Adventure</strong></td><td>29 oct. – 25 nov.</td><td>Missions d’événement → Mysterious Points</td><td>Miraculous Festive Pumpkin, skins Night of Fear</td></tr>
                <tr><td><strong>Mysterious Night: Check In</strong></td><td>29 oct. – 25 nov.</td><td>Connexion sur 7 jours</td><td>Sleepless Night AK-12, Stormy Night SG550</td></tr>
                <tr><td><strong>Pumpkin Messenger Sighted</strong></td><td>29 oct. – 25 nov.</td><td>Tuer les Pumpkin Messengers</td><td>Autumn Pumpkin Helmet, citrouilles de tout stade</td></tr>
                <tr><td><strong>Corrupted Treasures</strong></td><td>29 oct. – 25 nov.</td><td>Coffres / fabrication en Trophy Room</td><td>Fading Dawn, Corrupted Clock</td></tr>
                <tr><td><strong>Warlord Tournament III</strong></td><td>29 oct. – 7 déc.</td><td>Monter dans le classement</td><td>Badge, cadre et fond Warlord III</td></tr>
              </tbody>
            </table>
          </div>

          <p>La campagne de connexion est la partie à risque zéro : sept jours de connexion sur une fenêtre de 28 jours, c’est largement rattrapable. Elle délivre des citrouilles non mûres (le point de départ de l’évolution), le skin Sleepless Night de l’AK-12, le skin Stormy Night du SG550, le charme Jack-o’-Lantern et le charme Pumpkin Monster. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="novembre">6. Les événements de novembre en détail</h2>
          <p>Le <strong>10 novembre 2026</strong> a été la mise à jour la plus dense de la saison après celle du lancement : une collaboration de marque, une phase d’enquête, et douze correctifs. Elle est entrée en vigueur à 03:00 UTC+0. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="event-grid">
            <div class="event-card live">
              <h4>Dim Dou Duk Collaboration <span class="evt-badge evt-live">En cours</span></h4>
              <span class="evt-dates">9 nov. – 6 déc. 2026 · 28 jours</span>
              <p>Une collaboration avec une vraie enseigne de dim sum cantonaise. Deux objets entrent dans le loot pool de toutes les cartes : la <strong>Dim Sum Voucher</strong>, qui est la monnaie de l’événement, et les <strong>Dim Dou Duk Shrimp Dumplings</strong>, qui est un objet de RAID distinct.</p>
              <div class="evt-meta">Récompenses : skin d’équipement, skin de grenade fumée, badge, spray Char Siu, vouchers de charme et coupons de tirages S7. <strong>Uniquement cosmétique.</strong></div>
            </div>
            <div class="event-card hot">
              <h4>Kamona Investigation — Tea Break Delights <span class="evt-badge evt-hot" style="color:var(--color-accent-red);border-color:rgba(255,59,59,.45);background:rgba(255,59,59,.10)">Urgent</span></h4>
              <span class="evt-dates">9 nov. – 22 nov. 2026 · 14 jours</span>
              <p>L’enquête demande de rendre quatre objets : <strong>lait, miel, pellicule, et raviolis Dim Dou Duk Shrimp Dumplings</strong>. Les trois premiers sont du loot de nourriture et de valeur moyenne ; les raviolis sortent des mêmes conteneurs que les vouchers.</p>
              <div class="evt-meta">Récompenses : boîtes-cadeaux Rain of Gold et Shining Gold, Stroke of Luck I, Lucky Break I, vouchers de charme, coupons de skins S7. La piste <em>Investigate Drawers</em> ajoute des missions en Koen.</div>
            </div>
            <div class="event-card closed">
              <h4>Trash to Treasure <span class="evt-badge evt-closed">Terminé</span></h4>
              <span class="evt-dates">29 oct. – 15 nov. 2026</span>
              <p>La formule Halloween du Smelter : <strong>Personal Digital Assistant + Data Cable + Laptop</strong> pour une chance d’obtenir le <strong>Prototype Calculation Module</strong>. Les fours apparaissent dans les zones Lockdown et Forbidden.</p>
              <div class="evt-meta">A Closed le 15 novembre. La formule d’octobre est tombée ; surveillez la mise à jour de novembre pour la formule suivante.</div>
            </div>
            <div class="event-card live">
              <h4>Série Biohazard <span class="evt-badge evt-live">En cours</span></h4>
              <span class="evt-dates">Depuis le lancement de la S7 · hebdomadaire</span>
              <p>La série de zombies de la saison : mode <strong>Infected Area</strong> dans les raids, <strong>Zombie Endless</strong> en mode compétitif, et trois pistes hebdomadaires (Extermination, Merit Challenge, Zombies No Man’s Land).</p>
              <div class="evt-meta">La tenue Hazmat complète se gagne gratuitement par l’Extermination Mission. Le patch du 27 octobre a facilité la montée de niveau en Zombie Endless.</div>
            </div>
          </div>

          <h2 id="modes">7. Les modes événementiels de la Saison 7</h2>
          <p>Un événement n’est pas toujours une page de quêtes. Les modes événementiels ont leurs propres règles, et c’est souvent là que se trouve la valeur la plus sûre du jeu. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Format</th><th>Règle clé</th><th>Ce qu’on en tire</th></tr></thead>
              <tbody>
                <tr><td><strong>Supplies Drops 2.0</strong></td><td>Co-op PvPvE, 4 équipes, Airport</td><td>Loadout fourni, réapparitions illimitées,crate à 5 niveaux</td><td>Loot sans risque, plus le Smelter dès le niveau 3</td></tr>
                <tr><td><strong>Zombie Endless</strong></td><td>Classement infini, infectés</td><td>Score de Merit, montée de niveau</td><td>Jusqu’à 3 000 000 Koen/semaine via le Merit Challenge</td></tr>
                <tr><td><strong>Infected Area</strong></td><td>Raid Tactique en zone infectée</td><td>Zombies mutants, boss de classe Élite affaiblis</td><td>Tickets Zombie No Man’s Land et loot rouge de zone</td></tr>
                <tr><td><strong>Secure Ops</strong></td><td>Raid Tactique modifié</td><td>On garde son équipement même en mourant</td><td>Apprentissage sans perte, koen à l’extraction</td></tr>
                <tr><td><strong>Hostile Sector</strong></td><td>Secteurs renforcés</td><td>Ennemis d’élite lourdement équipés, rotation</td><td>Le loot haut de gamme de la saison</td></tr>
                <tr><td><strong>Warlord Tournament</strong></td><td>Classement par valeur de loot</td><td>Loadouts visibles, fichier chiffré multiplicateur</td><td>Badges, cadre, fond, skins de classe S</td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout">
            <h4>Le point commun des modes événementiels</h4>
            <p>Presque tous partagent la même logique économique : <strong>le risque de votre stuff n’est pas en jeu</strong>, donc la bonne décision est de jouer agressivement sur les objectifs et de laisser le loot dans la caisse plutôt que dans le sac. Un guide de Saison 6 qui vous apprend à « ne jamais mourir » vous fait perdre de l’argent en Supplies Drops 2.0. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="biohazard">8. La série Biohazard en pratique</h2>
          <p>La S7 a introduit la notion de zone infectée, avec deux modes qui s’articulent : <strong>Infected Area</strong>, où l’on fait un raid Tactique classique mais avec des zombies mutants et des boss d’élite, et <strong>Zombie Endless</strong>, un mode à score cumulé. Les événements d-Non se greffent dessus. <span class="src-tag src-officiel">Officiel</span></p>

          <ol class="steps">
            <li><strong>Extermination Mission</strong> — hebdomadaire, remise le lundi à 05:00 UTC+0. Récompense : la <strong>tenue Hazmat complète</strong>, obtenue via les Supply Passes. C’est un équipement d’événement gratuit, ce qui est rare.</li>
            <li><strong>Merit Challenge</strong> — hebdomadaire. Votre meilleur score de Merit en Zombie Endless dans la semaine est converti en Koen, avec un multiplicateur de 3, dans la limite de 3 000 000 Koen par semaine. À faire en priorité.</li>
            <li><strong>Zombies No Man’s Land</strong> — hebdomadaire. Connexion quotidienne et passes de jalons aux seuils 4, 8 et 16 tâches quotidiennes. Des tickets droppent aussi en Infected Area.</li>
            <li><strong>Infected Area</strong> — en raid. Les zones infectées ajoutent un bonus de risque et un loot rouge plus généreux ; masquez-vous, courez en sprinteur, et gardez Elysium en priorité.</li>
            <li><strong>Zombie Endless</strong> — le mode. Le patch du 27 octobre 2026 a abaissé le Merit total requis pour monter de niveau et facilité plusieurs missions « Enter Infected Zone ».</li>
          </ol>

          <h2 id="saison8">9. Et la Saison 8 ?</h2>
          <p>Aucune date n’est annoncée. Le compte officiel n’a rien publié sur Steam, sur le site officiel ni dans les notes du patch en direct du 10 novembre, qui ne parle que de la collaboration Dim Dou Duk et de l’enquête Kamona. <span class="src-tag src-officiel">Officiel</span></p>
          <p>Ce qui est observable : la Saison 7 a démarré le 16 septembre 2026, et les trois dernières saisons ont duré entre 78 et 89 jours. Une extrapolation placerait la Saison 8 entre le 3 et le 14 décembre 2026, et les événements S7 courant jusqu’au 7 décembre, l’estimation la plus citée est la semaine du 8 au 14 décembre. Deux contre-exemples existent : la Saison 3 a débordé sur Noël et la Saison 4 n’a lancé qu’en janvier. <span class="src-tag src-theorie">Théorie</span></p>

          <div class="callout callout-warning">
            <h4>Ce qui se passe au changement de saison</h4>
            <p>Arena Breakout: Infinite <strong>ne vide pas le stash</strong> entre les saisons — ni même à la fin d’un festival. Ce qui expire, ce sont les objets marqués « fournitures de saison », les coupons de tirages de la saison précédente et les monnaies d’événement dont l’écran a été fermé. Les cosmétiques et les objets de collection se conservent. En pratique, vos seuls vrais coupsables sont les coupons de tirages S7, à dépenser avant la fin de la saison. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="planification">10. Plan d’action recommandé au 17 novembre 2026</h2>
          <p>Voici l’ordre qui maximise le rendement sur les cinq semaines restantes, en tenant compte du fait que les événements se terminent dans un ordre précis et que les pistes hebdomadaires se remettent chaque lundi.</p>

          <ol class="evt-plan">
            <li><strong>Ce soir et demain : l’enquête Tea Break Delights.</strong> Il reste cinq jours. Faites une sortie dédiée avec un kit léger pour remplacer tout ce qui manque dans les quatre objets à rendre. C’est la seule piste qui disparaît sans préavis de votre stock.</li>
            <li><strong>En parallèle, le Smelter est inaccessible depuis le 15 novembre pour la formule Halloween</strong> — mais le Smelter du mode Supplies Drops 2.0 (niveau 3 de crate) reste actif et sans limite d’usage. C’est le relais naturel.</li>
            <li><strong>Cette semaine : viser le niveau 5 de crate en Supplies Drops 2.0.</strong> Le mode ne coûte que des Koen ou un pass, il n’a aucun risque sur votre équipement, et le niveau 5 est le seul qui ouvre une ligne au crate personnel. Faites-le avant que le mode ne tourne.</li>
            <li><strong>Le lundi 23 novembre : reset hebdomadaire.</strong> Remettez l’Extermination Mission et le Merit Challenge avant la remise de 05:00 UTC+0. Le Merit Challenge à 3 000 000 Koen se joue sur un mode Endless précis.</li>
            <li><strong>Avant le 25/26 novembre : toutes les missions Halloween.</strong> Mysterious Night Adventure, Pumpkin Messenger Sighted et Corrupted Treasures. La fenêtre de connexion pour le check-in de 7 jours est la plus facile, mais la campagne de missions à points est celle qui rapporte le plus.</li>
            <li><strong>Du 26 novembre au 6 décembre : la fenêtre Gourmet Market.</strong> C’est le plus long événement restant, donc pas le plus urgent. Ramassez les Dim Sum Vouchers au fur et à mesure des sorties de routine, sur un kit bon marché.</li>
            <li><strong>Jusqu’au 7 décembre : le Warlord Tournament.</strong> Le classement se règle à la fin de chaque raid, pas à l’extraction : ne quittez pas la carte sur un petit avantage. Et attrapez le fichier chiffré, puis faites sortir son porteur.</li>
          </ol>

          <div class="callout callout-danger">
            <h4>Un avertissement qui vaut de l’argent</h4>
            <p>Chaque événement attire des sites qui vendent des Koen ou des citrouilles déjà évoluées. <strong>Ne les utilisez pas.</strong> MoreFun a supprimé l’achat de Koen contre de l’argent réel à la version 1.0 et applique une politique de tolérance zéro qui sanctionne les acheteurs autant que les vendeurs : confiscation, baisse du score de Merit, bannissements. Le rapport de sécurité de la saison 6 a listé à lui seul 2 133 confiscations de Koen et 1 217 bannissements de dix ans entre le 13 et le 26 juillet 2026. Tout se gagne en jouant. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="sources">11. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Live Update du 27 octobre 2026 (UTC+0)</span> — annonce de l’événement Halloween, du Troisième Warlord Tournament et de la formule Smelter. <a href="https://x.com/ArenaBreakoutPC/status/2115421734728044892" target="_blank" rel="noopener">x.com/ArenaBreakoutPC</a></li>
            <li><span class="src-name">Live Update du 10 novembre 2026 (UTC+0)</span> — collaboration Dim Dou Duk, lancement de Kamona Investigation, 12 correctifs. <a href="https://patchbot.io/games/arena-breakout-infinite/articles/2145-nov-10-utc0-live-update" target="_blank" rel="noopener">patchbot.io</a></li>
            <li><span class="src-name">Biohazard &amp; Bountiful Autumn Festival</span> — annonce officielle du 24 septembre 2026 : les douze pistes du festival, le Lunar Soil Sample et Supplies Drops 2.0. <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">Notes de mise à jour de la Saison 7 — Utopia</span> — 15 septembre 2026 : Red Drops, Elysium, Collection Room, fichier chiffré du Warlord. <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">Annonces de festivals précédents</span> — Kamona Summer Festival (13 août – 13 sept. 2026) et Resident Evil / Girls’ Frontline 2 collaborations, pour la structure des pistes. <a href="https://idcgames.com/en/arena-breakout-infinite/news/" target="_blank" rel="noopener">idcgames.com</a></li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">timesaver.gg</span> — calendriers événementiels, tableaux de récompenses et analyses de règles pour la S7, y compris la confirmation de l’absence de date pour la Saison 8. <a href="https://timesaver.gg/blog/arena-breakout-infinite-season-8" target="_blank" rel="noopener">timesaver.gg</a></li>
            <li><span class="src-name">senseos.gg</span> — registre des objets rouges de la saison : dates d’expiration du Lunar Soil Sample, liste des Red Drops S7. <a href="https://senseos.gg/guides/arena-breakout-infinite/red-items/" target="_blank" rel="noopener">senseos.gg</a></li>
            <li><span class="src-name">abibuilder.com</span> — calendrier événementiel agrégé, utile pour recouper les dates de rotation. <a href="https://abibuilder.com/events" target="_blank" rel="noopener">abibuilder.com</a></li>
            <li><span class="src-name">r/ArenaBreakoutInfinite</span> — fils « 5 raids havent found a single one » (vouchers Dim Sum), discussions sur l’expiration des citrouilles et les seuils du Smelter. <a href="https://www.reddit.com/r/ArenaBreakoutInfinite/" target="_blank" rel="noopener">reddit.com</a></li>
            <li><span class="src-name">gamers.wiki et overgear.com</span> — règles du mode Supplies Drops d’origine (niveau 6, pass ou 300 000 Koen) et usage des crates personnel / équipe. <a href="https://gamers.wiki/en/games/arena-breakout-infinite/wiki" target="_blank" rel="noopener">gamers.wiki</a></li>
          </ul>
          <h3>Non confirmé</h3>
          <ul class="src-list">
            <li>La fenêtre de lancement de la Saison 8 (3–14 décembre 2026) est une <strong>extrapolation</strong> fondée sur la durée des trois dernières saisons ; elle n’a jamais été annoncée par MoreFun.</li>
            <li>Les seuils de rendement du Smelter rapportés sur Reddit (quantités et probabilités) sont des <strong>observations de joueurs</strong>, jamais publiés par l’éditeur.</li>
            <li>Le fait que les objets fournis par l’opérateur ne puissent pas être smeltés, et que les objets de qualité Or ne puissent pas entrer en raid, repose sur des <strong>tests communautaires</strong> et des notes de correctif partielles ; seule l’interdiction des misc-items de qualité Or est explicitement documentée.</li>
            <li>Les points d’apparition, la vie et les horaires des Pumpkin Messengers ne sont <strong>pas publiés</strong> par l’éditeur.</li>
          </ul>
        """
