# -*- coding: utf-8 -*-
"""S12 — Contenu de la page univers-dark-zone.html."""

CONTENT = r"""
          <div class="lore-legend">
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">annonces, notes de patch, archives et vidéos de MoreFun Studios</span>
            <span class="src-tag src-communautaire">Communautaire</span><span class="lg-txt">wikis, Reddit, guides tiers recoupés</span>
            <span class="src-tag src-theorie">Théorie</span><span class="lg-txt">cohérente mais jamais confirmée</span>
            <span class="src-tag src-rapporte">Rapporté</span><span class="lg-txt">source secondaire, recoupement partiel</span>
          </div>

          <figure class="page-figure">
            <img src="../img/univers/dark-zone.jpg" alt="Couloir industriel noir traversé par un faisceau de lampe frontale, poussière en suspension et brume" loading="lazy">
            <figcaption>« Seul ce que vous sortez de la Dark Zone vous appartient. » La règle du jeu est aussi la règle du lore.</figcaption>
          </figure>

          <h2 id="definition">1. Qu’est-ce que la Dark Zone ?</h2>
          <p>La Dark Zone est le <strong>territoire de l’après-armistice</strong> : l’espace de Kamona où la guerre Nord-Sud n’a jamais vraiment cessé, mais où elle s’est transformée en conflit larvaire. Elle naît de l’intervention du Comité Sumek, qui met fin publiquement aux hostilités sans en résoudre les causes. <span class="src-tag src-communautaire">Communautaire</span></p>
          <ul>
            <li><strong>Statut juridique</strong> : aucune autorité kamonaise n’y est présente de façon effective.</li>
            <li><strong>Acteurs</strong> : restes des armées du Nord et du Sud, PMC, organisations criminelles, et les entreprises militarisées privées.</li>
            <li><strong>Économie</strong> : contrats à risque, contrebande, marché noir, course aux ressources.</li>
            <li><strong>Règle</strong> : la seule loi qui y existe est économique — « seul ce que vous emportez hors de la Dark Zone vous appartient ». <span class="src-tag src-officiel">Officiel</span></li>
          </ul>
          <div class="lore-quote">
            « Bien que cet endroit soit rempli de trésors, seul ce que vous emportez hors de la Dark Zone vous appartient. Ceux qui y sont déjà venus vous diront que votre sécurité dépend de l’argent que vous avez. »
            <cite>Mission in-game « Abundant Profit » — texte officiel</cite>
          </div>
          <div class="lore-quote">
            « Ramener une brasée de butin dans la Dark Zone ne sert à rien si vous ne pouvez pas l’extraire. N’oubliez pas que les gourmets creusent leur propre tombe avec leurs dents. »
            <cite>Mission in-game « Smooth Extraction » — texte officiel</cite>
          </div>

          <h2 id="modes">2. Les trois modes de la Dark Zone</h2>
          <p>Le jeu traduit la Dark Zone par trois paliers de risque officiels. Ils ne sont pas des « zones » de la carte : ce sont des <strong>règles de raid</strong> appliquées aux mêmes cartes. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mode</th><th>Pression</th><th>Valeur du loot</th><th>Déblocage / frais</th><th>Pour qui ?</th></tr></thead>
              <tbody>
                <tr><td><strong>Normal</strong></td><td>Faible</td><td>Contenants majoritairement faibles, rares très improbables</td><td>Libre</td><td>Débutants, remise en fonds, apprentissage des rotations</td></tr>
                <tr><td><strong>Lockdown</strong></td><td>Élevée</td><td>Meilleure chance de trouver de la valeur, points premium</td><td>Niveau 12, ~100 000 K de valeur d’équipement, ~20 000 K de frais <span class="src-tag src-rapporte">Rapporte</span></td><td>Joueur au-dessus du mode Normal, prêt à risquer</td></tr>
                <tr><td><strong>Forbidden</strong></td><td>Maximale</td><td>Meilleur potentiel de récompense</td><td>Niveau 12, ~300 000 K de valeur d’équipement, ~50 000 K de frais <span class="src-tag src-rapporte">Rapporte</span></td><td>Joueur qui mise tout sur l’extraction, chasseur de loot rouge</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-muted small">Les seuils chiffrés ci-dessus proviennent de guides tiers et peuvent varier selon la carte et la version ; les limites de budget utilisées par notre <a href="meta-loadout-optimizer.html">Loadout Optimizer</a> (950 K en Lockdown, 2 M en Forbidden) sont des estimations prudentes de la communauté. <span class="src-tag src-rapporte">Rapporte</span></p>
          <div class="callout callout-warning">
            <h4>Normal, Lockdown, Forbidden : ce que vous achetez avec le risque</h4>
            <p>Le mode ne change pas votre loot, il change <strong>qui est dans la zone avec vous</strong>. En Normal, les PNJ et les joueurs sont faiblement équipés : un tir gratuit suffit. En Forbidden, chaque affrontement est un duel de budget. Le mode élevé est une <strong>taxe sur l’imprudent</strong>, pas sur le courage.</p>
          </div>

          <h2 id="origines">3. Les trois origines officielles du concept</h2>
          <p>Le concept de Dark Zone précède la version Infinite. La documentation officielle du premier jeu en donne la définition la plus nette. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="lore-grid">
            <div class="lore-card neutral">
              <h4>Tac Ops</h4>
              <p class="lore-sub">Vous jouez un Agent</p>
              <p>Vous entrez en raid en tant qu’<strong>Agent</strong>. Vous préparez vous-même vos armes, votre équipement et vos supplies dans l’entrepôt, puis vous entrez dans la Dark Zone. Vous cherchez des supplies sur le terrain, atteignez un point d’extraction dans le temps imparti, et <strong>conservez tout ce que vous avez trouvé</strong> si vous y parvenez.</p>
            </div>
            <div class="lore-card neutral">
              <h4>Covert Ops</h4>
              <p class="lore-sub">Vous jouez un Rogue</p>
              <p>Vous entrez en tant que <strong>Rogue</strong>, avec <strong>des armes, un équipement et des supplies attribués aléatoirement</strong>. Vous n’avez pas la maîtrise de votre build : la Dark Zone décide de votre dotation. C’est le mode le plus proche de la <strong>survie nue</strong> et le plus narrativement intéressant.</p>
            </div>
            <div class="lore-card gray">
              <h4>Les pionniers</h4>
              <p class="lore-sub">Dark Zone Pioneers</p>
              <p>Les « Dark Zone Pioneers » peuvent être <strong>déguisés en Rogues</strong>. Autrement dit, un joueur qui vous donne l’impression d’être une cible sans défense peut être un PMC de son côté, et l’inverse est vrai. C’est le premier niveau de « mise en abyme » du jeu.</p>
            </div>
          </div>
          <p class="text-muted small">Cette tripartition vient de la présentation officielle du jeu mobile de 2022 ; elle a été simplifiée en version PC/mobile Infinite, mais la logique « Agents / Rogues » reste la matrice de tous les modes. <span class="src-tag src-rapporte">Rapporte</span></p>

          <h2 id="cartes">4. Les nœuds de la Dark Zone</h2>
          <p>La Dark Zone n’est pas uniforme : chaque carte est un <strong>noeud</strong> dominé par une faction, avec ses propres règles de loot. Connaître le nœud, c’est déjà savoir à qui vous avez affaire. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Noeud</th><th>Carte</th><th>Faction dominante</th><th>Boss</th><th>Signature</th><th>Risque</th></tr></thead>
              <tbody>
                <tr><td><strong>Station de diffusion</strong></td><td><a href="map-tv-station.html">TV Station</a></td><td>Successions (White Wolves, puis Comité Sumek)</td><td>Kurt, Rolf, Bernard</td><td>Laboratoire secret, ascenseur du 2<sup>e</sup> étage, système d’inondation au gaz</td><td><span class="text-red">Très élevé</span></td></tr>
                <tr><td><strong>Dépôt de Marulos</strong></td><td><a href="map-armory.html">Armory</a></td><td>Kamona Liberation Army</td><td>Renoir</td><td>Arsenal de haut niveau, bunker sud, gardes nombreux</td><td><span class="text-red">Très élevé</span></td></tr>
                <tr><td><strong>Axe de ravitaillement</strong></td><td><a href="map-farm.html">Farm</a></td><td>Alternance Ajax / Hecate</td><td>Ajax, Hecate</td><td>Échanges de contrôle, grenades-leurre, colonne de Hecate</td><td><span class="text-orange">Élevé</span></td></tr>
                <tr><td><strong>Ligne de crête</strong></td><td><a href="map-northridge.html">Northridge</a></td><td>Indépendants / Abyss Squad</td><td>Fred Lee</td><td>Longue portée, escorte namesake, neige et météo</td><td><span class="text-orange">Élevé</span></td></tr>
                <tr><td><strong>Hub aérien de Guoyapos</strong></td><td><a href="map-airport.html">Airport</a></td><td>Base avancée de MNST</td><td>Ambush White Wolves / Blackgold</td><td>Meilleur budget d’entrée, coffres multiples, zone infectée en S7</td><td><span class="text-red">Très élevé</span></td></tr>
                <tr><td><strong>Vallée des Court's</strong></td><td><a href="map-valley.html">Valley</a></td><td>Famille Antonio / Mad Dogs</td><td>Doss Antonio</td><td>Or, coffres, marchands, escorte privée de Doss</td><td><span class="text-gold">Moyen</span></td></tr>
                <tr><td><strong>Terrasse minière</strong></td><td>Mine</td><td>Mad Dogs (Porrero)</td><td>Porrero Kazan</td><td>Prison, casque explosif, éclats d’Utopia</td><td><span class="text-red">Très élevé</span></td></tr>
                <tr><td><strong>Zone portuaire</strong></td><td>Port / events</td><td>Mutins du Polaris</td><td>Derwin Pan</td><td>Alerte sonore, marché noir, contrôle des routes</td><td><span class="text-gold">Moyen</span></td></tr>
                <tr><td><strong>Terres mortes</strong></td><td><a href="map-no-mans-land.html">No Man’s Land</a></td><td>Indéterminée</td><td>Aucun</td><td>Zone de reconnaissance, ni faction ni loot premium</td><td><span class="text-gold">Moyen</span></td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="commite">5. Le Comité Sumek sur le terrain</h2>
          <figure class="page-figure">
            <img src="../img/univers/sumek-committee.jpg" alt="Convoi de maintien de l’ordre en casque bleu clair devant un barrage de blocs de béton la nuit" loading="lazy">
            <figcaption>Le Comité Sumek : une force de maintien de l’ordre internationale, dont la neutralité a rapidement montré ses limites.</figcaption>
          </figure>
          <p>Le Comité Sumek intervient avec des unités de maintien de l’ordre, protectrices de convois d’aide humanitaire, et lance l’Operation Peacemaker pour couvrir ces vols face aux batteries antiaériennes. Mais l’Operation Blackout montre son angle mort : ses propres équipes mixtes se trahissent, et l’avion qu’il envoie ne transportait pas de l’aide mais des <strong>échantillons d’Utopia</strong>. <span class="src-tag src-communautaire">Communautaire</span></p>
          <ul>
            <li><strong>Alpha Team</strong> (Colom SAS) et <strong>Bravo Team</strong> (membres de l’Abyss Squad) agissent sous mandat conjoint.</li>
            <li>La Bravo Team redirige la dernière batterie antiaérienne vers l’avion du Comité.</li>
            <li>Conséquence politique : le Comité soupçonne le Sud, mais l’absence d’extraction d’Alpha empêche toute attribution — et <strong>Renoir Brady est accusé</strong>.</li>
          </ul>
          <p class="text-muted small">La question centrale de la Dark Zone tient en une phrase : <strong>qui contrôle les échantillons d’Utopia</strong> ? Ni le Nord, ni le Sud, ni le Comité n’ont d’intérêt à ce que la vérité remonte. <span class="src-tag src-theorie">Théorie</span></p>

          <h2 id="utopia">6. Utopia : la nouvelle couche de la Dark Zone</h2>
          <p>La Saison 7 ajoute une dimension physique à la Dark Zone : l’<strong>Infected Zone</strong>. L’officialisation de la fuite du réactif Utopia transforme des zones auparavant sûres en terrain contaminé. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Élément</th><th>Effet en jeu</th><th>Lecture lore</th></tr></thead>
              <tbody>
                <tr><td><strong>Farm</strong></td><td>Heavy Infected Zone</td><td>Contamination la plus dense : le site est proche des infrastructures</td></tr>
                <tr><td><strong>Valley</strong></td><td>Infected Zone standard</td><td>Anomalies et phénomènes étranges : la « Night Owl Detective Agency » y enquête</td></tr>
                <tr><td><strong>Airport</strong></td><td>Heavy Infected + Zombie Endless</td><td>Base avancée de MNST : le lieu où l’infrastructure s’est superposée à l’infection</td></tr>
                <tr><td><strong>Elysium</strong></td><td>Loot rouge de valeur égale à Utopia, en zone infectée</td><td>Utopia n’est pas un objet unique mais une classe de matériel bio-technologique</td></tr>
                <tr><td><strong>Zombie Research</strong></td><td>Progression dédiée</td><td>Le recherche sur le réactif se poursuit, y compris sous contrôle humain</td></tr>
              </tbody>
            </table>
          </div>
          <p>La liaison entre l’outbreak et les <strong>installations situées sous la TV Station</strong> est celle que le studio a lui-même mise en avant. C’est le fil qui relie le lore de la saison 7 à l’histoire de l’archipel — et c’est pourquoi la TV Station reste le point le plus important de la carte en S7. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="regles">7. Les lois non écrites de la Dark Zone</h2>
          <p>Au-delà des modes et des cartes, la Dark Zone impose un code de conduite que la communauté a stabilisé et que les meilleures équipes appliquent. <span class="src-tag src-communautaire">Communautaire</span></p>
          <ol>
            <li><strong>Le bruit est une signature.</strong> Chaque tir, chaque course, chaque porte forcée est un Coordinates. Dans la TV Station, le silence est votre meilleure arme.</li>
            <li><strong>La valeur transportée est un Permissions.</strong> Le bandit qui vous arrête ne veut pas vos armes : il veut votre butin. Plus vous transportez, plus vous valent une embuscade.</li>
            <li><strong>Le temps est une ressource.</strong> Les extractions ferment, les lignes d’IA se rechargent, et le chronomètre de raid se termine pour tout le monde. « Le timing d’extraction » est la compétence reine. <a href="meta-stratégies-s7.html">Voir les stratégies S7</a>.</li>
            <li><strong>Le rat run fonctionne encore.</strong> Entrer léger, lire les combats, récupérer l’équipement des morts, extraire : c’est le rapport rendement/risque le plus élevé du jeu. <a href="meta-stratégies-s7.html">Technique du rat</a>.</li>
            <li><strong>La faction adverse n’est pas votre ennemi.</strong> Dans la Dark Zone, un boss de PMC, un joueur et un PNJ sont trois types de danger différents. Le boss peut être votre allié de fait s’il est lui-même ciblé.</li>
          </ol>
          <div class="callout callout-danger">
            <h4>L’erreur la plus fréquente</h4>
            <p>Confondre la Dark Zone (le lieu du lore) avec le mode de jeu le plus difficile. La Dark Zone est <strong>partout</strong>. Un run en Normal sur la TV Station est déjà un run en Dark Zone. Le risque vient de vos adversaires, pas du nom de votre mode.</p>
          </div>

          <h2 id="implications">8. Implications pratiques</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Signal du lore</th><th>Ce qu’il faut faire</th><th>Équipement associé</th></tr></thead>
              <tbody>
                <tr><td>Un site est un <strong>nœud de faction</strong></td><td>Éviter l’axe du boss : il couvre l’accès au loot</td><td>Grenades, casque audio, deux charges</td></tr>
                <tr><td>Le site est un <strong>point de contrôle d’armistice</strong></td><td>Traiter chaque porte comme une embuscade possible ; ne jamais s’y arrêter</td><td>Énergie, sprint court, grenades</td></tr>
                <tr><td>Le site est un <strong>marché noir</strong></td><td>Prioriser coffres, clés et marchands ; fights inutiles</td><td>Budget moyen, pas de full kit</td></tr>
                <tr><td>La zone est <strong>infectée</strong></td><td>Masque, gestion des groupes, sortie rapide</td><td>Elysium en cible prioritaire</td></tr>
                <tr><td>Le boss est un <strong>chef de clan</strong></td><td>Son escorte porte un nom de famille : un seul kill peut en effondrer plusieurs</td><td>Munitions de pénétration, viseur</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-muted small">Les éléments en caractères non latins de ce tableau ont été corrigés ; la version published est entièrement en français. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="mysteres">9. Ce qui reste inexpliqué dans la Dark Zone</h2>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Qui possède les échantillons d’Utopia ?</h4>
              <p>Après l’Operation Blackout, Colom et Tevilla proposent des sommes considérables pour récupérer les échantillons de la Mine. Aucune faction ne les contrôle officiellement. <span class="src-tag src-communautaire">Communautaire</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Qui parle à la radio à Hecate ?</h4>
              <p>Une voix anonyme lui dit de ne pas partir et lui promet que « le camp de garde vous traitera bien ». L’identité n’a jamais été révélée, et Hecate reste sur la ferme malgré sa mission. <span class="src-tag src-rapporte">Rapporte</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Que se passe-t-il à la TV Station après Sumek ?</h4>
              <p>Le Comité réquisitionne la station « pour des raisons non déclarées ». Depuis, le complexe est le point le plus dense de la Dark Zone — et le point le plus silencieux en termes d’explications officielles. <span class="src-tag src-communautaire">Communautaire</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Où est le laboratoire de l’Ark ?</h4>
              <p>Si les installations sous la TV Station abritaient un programme de recherche, qui y travaille aujourd’hui ? Les hypothèses de la communauté tournent autour de la corporation Toland et d’une unité d’élimination, mais rien n’est confirmé. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Que vaut réellement le Secret Document ?</h4>
              <p>Un document confidentiel rouge circule en raid. Sa valeur marchande et sa fonction exacte ne sont pas documentées par l’éditeur : les prix de marché restent très dispersés. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>

          <h2 id="sources">10. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Textes de mission in-game</span> — « Abundant Profit », « Smooth Extraction », « Send Signal », « Sanctuary Recon », « Signal Interference », « Road to Riches » : les citations de la Dark Zone les plus directes. <a href="https://arenabreakout-infinite.com/missions/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></li>
            <li><span class="src-name">Description officielle Arena Breakout (2022)</span> — <em>Tac Ops</em>, <em>Covert Ops</em>, Agents et Rogues, Dark Zone Pioneers. <a href="https://arenabreakout.com/web202210/news/notice.html" target="_blank" rel="noopener">arenabreakout.com</a></li>
            <li><span class="src-name">Annonce de la Saison 7 : Utopia</span> — infection de Farm, Valley et Airport, origine et responsable du réactif non expliqués. <a href="https://idcgames.com/en/arena-breakout-infinite/news/arena-breakout-infinite-season-7-utopia-engulfs-kamona-in-a-new-crisis-on-september-16-2026-09-08-06-42-13766" target="_blank" rel="noopener">idcgames.com</a></li>
            <li><span class="src-name">Notes de mise à jour ABI (Steam)</span> — modes Normal / Lockdown / Forbidden, <em>Enter the Dark Zone</em>, conditions d’entrée par carte, S4 « Dusk to Dawn », S6 « White Nights ». <a href="https://steamcommunity.com/app/2073620/announcements/" target="_blank" rel="noopener">steamcommunity.com</a></li>
            <li><span class="src-name">S7 UTOPIA Arrives with Massive Rewards</span> — Elysium comme loot rouge de valeur égale à Utopia, en zone infectée. <a href="https://senseos.gg/guides/arena-breakout-infinite/red-items/" target="_blank" rel="noopener">senseos.gg</a></li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">Arena Breakout Wiki (Fandom)</span> — origine et limites de la Dark Zone, lien avec l’Operation Blackout. <a href="https://arena-breakout.fandom.com/wiki/Kamona" target="_blank" rel="noopener">arena-breakout.fandom.com</a></li>
            <li><span class="src-name">Grokipedia — Kamona</span> — Dark Zone et croissance des PMC. <a href="https://grokipedia.com/page/Kamona" target="_blank" rel="noopener">grokipedia.com</a></li>
            <li><span class="src-name">topuplist.com</span> — comparatif Normal / Lockdown / Forbidden, seuils de déblocage et frais d’entrée. <a href="https://topuplist.com/blogs/detail/what-is-lockdown-zone-arena-breakout" target="_blank" rel="noopener">topuplist.com</a></li>
            <li><span class="src-name">Reddit r/ArenaBreakoutInfinite</span> — fils sur la Dark Zone, les factions et les « archives » ; la terminologie « dark zone » est d’ailleurs souvent employée par la communauté pour désigner le jeu à haut risque en général, et pas uniquement un mode nommé.</li>
            <li><span class="src-name">senseos.gg</span> — boss et modes, dont l’Infected Zone et le Zombie Endless. <a href="https://senseos.gg/guides/arena-breakout-infinite/bosses-list/" target="_blank" rel="noopener">senseos.gg</a></li>
          </ul>
          <h3>Théories (non confirmées)</h3>
          <ul class="src-list">
            <li>Le réseau Toland, l’« Ark », les « Cleaners » et la figure d’« Arachne » : jamais mentionnés dans une communication officielle.</li>
            <li>La valeur exacte du Secret Document et sa fonction narrative : discussions communautaires uniquement.</li>
            <li>Les seuils chiffrés de déblocage Lockdown / Forbidden varient selon les guides : à traiter comme des ordres de grandeur, pas comme des valeurs officielles. <span class="src-tag src-rapporte">Rapporte</span></li>
          </ul>
          <p class="text-muted small"><a href="univers-lore.html">Lire l’histoire complète de Kamona</a> · <a href="univers-factions.html">Le dossier des factions et des personnages</a></p>
        """
