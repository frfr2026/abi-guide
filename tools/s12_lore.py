# -*- coding: utf-8 -*-
"""S12 — Contenu de la page univers-lore.html."""

CONTENT = r"""
          <div class="lore-legend">
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">annonces, notes de patch, archives et vidéos de MoreFun Studios</span>
            <span class="src-tag src-communautaire">Communautaire</span><span class="lg-txt">wikis, Reddit, guides tiers recoupes</span>
            <span class="src-tag src-theorie">Théorie</span><span class="lg-txt">cohérente mais jamais confirmée</span>
            <span class="src-tag src-rapporte">Rapporte</span><span class="lg-txt">source secondaire, recoupement partiel</span>
          </div>

          <figure class="page-figure">
            <img src="../img/univers/kamona-island.jpg" alt="Vue aerienne cinematique d'une ile ravagee par la guerre, fumee et brume au lever du jour" loading="lazy">
            <figcaption>Kamona : un archipel autosuffisant, ravage par une guerre civile de plusieurs années, puis par une guerre ouverte qui ne s’est jamais vraiment arrêtée.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Nation</span><span class="fact-value">Archipel autosuffisant, une île principale</span></div>
            <div class="fact"><span class="fact-label">Langue</span><span class="fact-value">Espagnol (d’après les PNJ)</span></div>
            <div class="fact"><span class="fact-label">Conflit</span><span class="fact-value">Guerre Nord-Sud, puis guerre larvée</span></div>
            <div class="fact"><span class="fact-label">Zone de jeu</span><span class="fact-value">La Dark Zone</span></div>
          </div>

          <h2 id="resume">1. Kamona en bref</h2>
          <p>Kamona est l’état principal de la franchise <em>Arena Breakout</em> : un petit archipel autosuffisant, forme de nombreuses îles, dont l’immense majorité de la population vit sur la plus grande, qui donne son nom au pays. <span class="src-tag src-communautaire">Communauté</span></p>
          <p>Le territoire est géographiquement simple et stratégiquement riche : des collines roulantes dans le centre et l’ouest, des régions montagneuses et stériles à l’intérieur (la <strong>Mine</strong>, les <strong>Onotos Mines</strong>), des plaines agricoles dans la région de <strong>Marulos</strong>, des ports sur la côte, et une frontière montagneuse au nord où la neige bloque les dépôts. Le terrain n’est pas le sujet : ce qui compte, c’est que quelques sites concentrent à la fois la production, l’information et les routes logistiques. <span class="src-tag src-rapporte">Rapporte</span></p>
          <p>La langue officielle de Kamona semble être l’espagnol, d’après les dialogues de plusieurs PNJ, notamment des personnels militaires. <span class="src-tag src-rapporte">Rapporte</span></p>

          <div class="callout callout-warning">
            <h4>Une chronologie datée, mais des dates flouées</h4>
            <p>Le jeu ne donne presque jamais de dates absolues. Les événements sont ordonnés de façon fiable (avant la guerre, pendant, après l’armistice), mais leur datation reste approchée. Toute chronologie de Kamona est donc une <strong>reconstruction</strong> : elle indique l’ordre, pas la date. Les saisons du jeu donnent des repères fiables : la Saison 1 <em>IGNITION</em>, la Saison 4 <em>Airport Hunt</em>, la Saison 5 <em>Dusk to Dawn</em>, la Saison 6 <em>White Nights</em> et la Saison 7 <em>Utopia</em>.</p>
          </div>

          <h2 id="geographie">2. La géographie de l’archipel</h2>
          <p>Chaque lieu du lore correspond à une zone de jeu où à un site secondaire. C’est la règle la plus utile du lore : quand vous lisiez une histoire de Kamona, elle se passe presque toujours <em>où vous êtes en train de looter</em>.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Lieu</th><th>Région</th><th>Rôle dans le lore</th><th>Zone de jeu</th></tr></thead>
              <tbody>
                <tr><td><strong>TV Station</strong></td><td>Centre / hauteur</td><td>Complexe de diffusion fortifié, base des White Wolves, laboratoire secret à l’ascenseur du 2e étage, système d’inondation au gaz pour dénier l’accès au centre. Plus tard réquisitionne par le Comité Sumek.</td><td><a href="map-tv-station.html">TV Station</a></td></tr>
                <tr><td><strong>Marulos Armory</strong></td><td>Nord</td><td>Dépôt militaire majeur du Nord, prise de guerre décisive. Arsenal de haut niveau au pouvoir de la Kamona Liberation Army.</td><td><a href="map-armory.html">Armory</a></td></tr>
                <tr><td><strong>Marulos Farms</strong></td><td>Nord / plaines</td><td>Zone agricole disputée : Ajax Jones y défend l’Axe de ravitaillement contre les sous-traitants de Blackgold, puis contre l’Abyss Squad.</td><td><a href="map-farm.html">Farm</a></td></tr>
                <tr><td><strong>The Mine</strong></td><td>Intérieur montagneux</td><td>Ancienne prison construite dans le complexe minier, bandits des Mad Dogs, puis lieu de l’écrasement de l’avion du Comité Sumek transportant des échantillons d’Utopia.</td><td>Mine / events</td></tr>
                <tr><td><strong>Kamona Port</strong></td><td>Côte</td><td>Hub du marché noir et des réseaux d’échanges illicites ; port tenu par les mutins de Derwin Pan et Rodriquez.</td><td>Port / events</td></tr>
                <tr><td><strong>Guoyapos International Airport</strong></td><td>Sud</td><td>Hub aviation modernisé en base de commandement provisoire des deux camps, puis militarisé. Base avancée de MNST après l’incident de la TV Station.</td><td><a href="map-airport.html">Airport</a></td></tr>
                <tr><td><strong>Northridge</strong></td><td>Nord / altitude</td><td>Station de téléphérique, hôtel, station d’épuration. Position dominante,enneigée, terrain de l’affrontement Fred contre Obol et Viper.</td><td><a href="map-northridge.html">Northridge</a></td></tr>
                <tr><td><strong>Valley / Norteno Court</strong></td><td>Centre</td><td>Vallée rénovée en fort par la famille Antonio ; résidence de Doss Antonio et de son escorte.</td><td><a href="map-valley.html">Valley</a></td></tr>
                <tr><td><strong>Floranpino Valley</strong></td><td>Centre</td><td>Zone de résidence de Doss Antonio, blanchiment d’armes sous la Villa.</td><td><a href="map-valley.html">Valley</a></td></tr>
                <tr><td><strong>Onotos Mines</strong></td><td>Intérieur</td><td>Zone minière de réunions clandestines et de tentatives d’embuscade.</td><td>Events</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="avant-guerre">3. Avant la guerre : la fracture</h2>
          <p>Kamona n’a pas explosé d’un coup. La guerre Nord-Sud commence par une <strong>déclaration d’indépendance du Second Clan</strong>, un acte politique local. L’armée kamonaise se scinde : des officiers choisissent de partir avec leurs hommes plutôt que d’accepter la nouvelle ligne de commandement. <span class="src-tag src-rapporte">Rapporte</span></p>
          <ul>
            <li><strong>Benjamin Renoir Brady</strong> commande alors la <strong>4e brigade d’infanterie blindée</strong> de l’armée kamonaise. Il part avec Ajax Jones et d’autres lorsque le Second Clan déclare son indépendance. <span class="src-tag src-rapporte">Rapporte</span></li>
            <li>La <strong>Marine de la République du Nord de Kamona</strong> disposait de deux cuirassés. Après une série d’événements, l’armée du Nord, trop exposée, est désorientée : le commandement ordonne de couler un navire. <span class="src-tag src-rapporte">Rapporte</span></li>
            <li>Le <strong>Polaris</strong> a refusé de couler. Son officier, <strong>Derwin Pan</strong>, tue ses supérieurs avec son pistolet F57, provoque une mutinerie, puis construit un réseau de marché noir avec un contact nommé <strong>Rodriquez</strong>. <span class="src-tag src-rapporte">Rapporte</span></li>
          </ul>
          <p>Le résultat de ces mutineries se lit dans le jeu : Derwin Pan est un boss de la zone portuaire, et son récit (RPK-16 à tambour de 95 rounds, F57 en arme secondaire) est celui d’un homme qui a gardé sa dignité d’officier. <span class="src-tag src-rapporte">Rapporte</span></p>

          <h2 id="guerre">4. La guerre Nord-Sud</h2>
          <p>Le conflit oppose un Nord industriel et un Sud riche en ressources. Il ne s’agit pas d’une guerre idéologique : c’est une <strong>guerre par procuration</strong>, où deux puissances étrangères se combattent sur le territoire kamonais en utilisant les forces locales comme des mandataires. <span class="src-tag src-communautaire">Communauté</span></p>

          <figure class="page-figure">
            <img src="../img/univers/civil-war.jpg" alt="Colonne de vehicules blindes franchissant un pont detruit en zone rurale grise, poussiere et fumee" loading="lazy">
            <figcaption>Une guerre par procuration : les grandes puissances emploient les opérateurs locaux, le pays paie le prix.</figcaption>
          </figure>

          <div class="table-wrap">
            <table class="data-table rel-matrix">
              <thead><tr><th>Camp</th><th>Force locale</th><th>Parrain étranger</th><th>Unité d’élite</th><th>Positions clés</th></tr></thead>
              <tbody>
                <tr><td>Nord</td><td>Front du Nord / MNST</td><td class="yes">Tevilla</td><td class="yes">White Wolves Squad</td><td>TV Station, Marulos Armory, ports</td></tr>
                <tr><td>Sud</td><td>Armée du Sud / CDIS</td><td class="yes">Colom</td><td class="yes">Alpha Team (Colom SAS)</td><td>TV Station, Marulos Farms, ports</td></tr>
                <tr><td>Tiers</td><td>Kamona Liberation Army</td><td class="mid">Tevilla + White Wolves</td><td class="mid">Renoir Brady, Ajax Jones</td><td>Marulos Armory, Marulos Farms</td></tr>
                <tr><td>Neutre</td><td>Comité Sumek</td><td class="no">International</td><td class="mid">Alpha + Bravo</td><td>TV Station (après l’armistice)</td></tr>
              </tbody>
            </table>
          </div>

          <h3>4.1 Les batailles qui comptent</h3>
          <figure class="page-figure">
            <img src="../img/univers/tv-station.jpg" alt="Station de télévision brutaliste abandonnée de nuit, mât d'antenne dans la brume, éclairage rouge d'urgence" loading="lazy">
            <figcaption>La TV Station : le point le plus disputé de l'archipel, fortifié par les White Wolves, puis réquisitionné par le Comité Sumek.</figcaption>
          </figure>
          <ul>
            <li><strong>La prise de la TV Station.</strong> Les forces du Nord, avec les White Wolves, s’emparent de la station et la transforment en base fortifiée : système d’inondation au gaz pour dénier l’accès à la zone centrale, et <strong>laboratoire secret</strong> accessible par un ascenseur spécial au deuxième étage. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>Les ports et les disques.</strong> Aux ports, White Wolves et opérateurs Blackgold se disputent le contrôle d’informations sensibles, notamment des <strong>disquettes</strong> contenant des données capitales. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>Marulos Armory.</strong> La prise du dépôt par la Kamona Liberation Army crée un <strong>troisième pôle</strong> que ni le Nord ni le Sud ne peut neutraliser facilement. Ajax Jones défend ensuite Marulos Farms contre les contre-attaques méridionales. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>La percée d’Hecate.</strong> L’Abyss Squad franchit la ligne d’armistice à Marulos Farms, force Ajax Jones à se replier et obtient un contrôle temporaire avant que la Libération Army ne reprenne la position. <span class="src-tag src-communautaire">Communauté</span></li>
          </ul>

          <h3>4.2 Les trois rebellions internes</h3>
          <p>La guerre Nord-Sud est le décor. Le vrai sujet, ce sont les <strong>cinq ou six conflits locaux</strong> qui se superposent et que le jeu met en jeu sous forme de boss. <span class="src-tag src-communautaire">Communauté</span></p>
          <div class="lore-grid">
            <div class="lore-card north">
              <h4>Kamona Liberation Army</h4>
              <p class="lore-sub">Renoir Brady &amp; Ajax Jones</p>
              <p>Former officiers de l’armée kamonaise, ils fondent l’Arme de la Libération de Kamona après la déclaration d’indépendance du Second Clan. Leur coup d’éclat est la prise de l’Armory de Marulos.</p>
              <ul>
                <li>Base : Marulos Armory et Marulos Farms</li>
                <li>Position : alliés du Nord, mais <strong>indépendant</strong></li>
                <li>Conflit interne : Ajax sur le terrain, Renoir au bunker</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>Les mutins du Polaris</h4>
              <p class="lore-sub">Derwin Pan &amp; Rodriquez</p>
              <p>Refus de couler le <em>Polaris</em>, mutinerie, liquidation de la chaîne de commandement, puis constitution d’un réseau de marché noir dans un port. Pan reste un officier de marine : son équipement de boss conserve un grade militaire.</p>
              <ul>
                <li>Base : la zone portuaire</li>
                <li>Méthode : corruption plutôt que violence de front</li>
                <li>Token de boss : la ceinture tranchée</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>Les Mad Dogs</h4>
              <p class="lore-sub">Stephen &amp; Porrero Kazan</p>
              <p>Banditisme organisé dans les prisons de la Mine. Pendant la guerre, le gang de Stephen organisé une émeute réussie contre le gardien et les gardes, avec l’aide de Porrero Kazan. Interne, la bande se retourne : Porrero tente d’assassiner Stephen pour insubordination, est déposé et abandonné dans la mine, puis <strong>récupéré par les White Wolves</strong>.</p>
              <ul>
                <li>Base : la Mine et le Valley</li>
                <li>Porrero devient sbire de Doss Antonio</li>
                <li>Token de boss : la clé de la prison de la Mine</li>
              </ul>
            </div>
            <div class="lore-card gold">
              <h4>La famille Antonio</h4>
              <p class="lore-sub">Doss Antonio &amp; Porrero</p>
              <p>Organisation criminelle qui prospère dans l’anarchie de l’après-guerre. Doss Antonio transforme sa richesse en pouvoir : il embauche des sbires (dont Porrero Kazan), fait appel aux White Wolves pour du soutien et finance la construction du <strong>Norteno Court</strong> et la rénovation de bâtiments de la vallée.</p>
              <ul>
                <li>Base : la Villa, Floranpino Valley</li>
                <li>Code visuel : or, lunettes de soleil, costume</li>
                <li>Token de boss : la pièce d’or faite main</li>
              </ul>
            </div>
          </div>

          <h2 id="sumek">5. Sumek : la fin officielle de la guerre</h2>
          <p>Le <strong>Comité Sumek</strong> est une organisation internationale neutre. Il intervient dans la guerre Nord-Sud et <strong>médiatise publiquement la fin des hostilités ouvertes</strong> entre le Nord et le Sud. L’armistice est réel sur le papier : les deux camps acceptent de cesser les combats de front. <span class="src-tag src-communautaire">Communauté</span></p>
          <p>Mais la guerre ne s’arrête pas. Elle change simplement de forme : elle devient une <strong>guerre larvée</strong> dans la zone qui sera appelée la <strong>Dark Zone</strong>, une immense région sans loi où subsistent escarmouches, trahisons et courses aux ressources. C’est précisément cette persistance qui attire les <strong>PMC</strong> et les acteurs économiques : c’est là que se joue votre vie, et vos Koen. <span class="src-tag src-communautaire">Communauté</span></p>
          <div class="callout callout-success">
            <h4>Pourquoi c’est important pour vous</h4>
            <p>Toute la boucle de jeu d’ABI est une paraphrase du lore : une zone de conflit déclarée mais non résolue, des acteurs multiples aux intentions incompatibles, et un prix pour ceux qui restent. La Dark Zone n’est pas une métaphore du PvP, c’est le lieu où la métaphore a été réalisée.</p>
          </div>
          <p>Le Comité ne se limite pas à la médiation : après l’incident de l’avion, il <strong>réquisitionne la TV Station</strong> pour des raisons non déclarées. C’est le dernier geste documenté du Comité dans le lore public. <span class="src-tag src-communautaire">Communauté</span></p>

          <h2 id="blackout">6. Operation Peacemaker et Operation Blackout</h2>
          <p>Pour protéger ses vols d’aide humanitaire des batteries antiaériennes restantes, le Comité Sumek lance l’opération <strong>Peacemaker</strong>. Son volet le plus documenté est l’opération <strong>Blackout</strong>. <span class="src-tag src-communautaire">Communauté</span></p>
          <ol>
            <li>Deux équipes mixtes sont déployées sur l’<strong>Armory de Marulos Nord</strong> : l’<strong>Alpha Team</strong> (spécialistes aéronautiques de Colom) et la <strong>Bravo Team</strong> (membres de l’Abyss Squad de Blackgold Universal).</li>
            <li>La mission : neutraliser les batteries antiaériennes et enquêter sur des systèmes supplémentaires.</li>
            <li>Juste avant l’extraction, la Bravo Team <strong>trahit l’Alpha Team</strong> et redirige la dernière batterie vers l’avion d’aide humanitaire du Comité qui survole le site.</li>
            <li>L’avion <strong>ne transportait pas de l’aide</strong> : il transportait des <strong>échantillons d’Utopia</strong>. Il s’écrase dans la zone de la <strong>Mine</strong>, dispersant un matériel de valeur devenu l’objectif de toutes les parties.</li>
            <li>Colom et Tevilla offrent ensuite des sommes considérables pour récupérer ces échantillons. Alpha n’ayant pas réussi à s’extraire, la suspicion du Comité ne peut pas se fixer sur le Sud : <strong>Renoir Brady est accusé</strong>, et sa réputation est abîmée.</li>
          </ol>
          <figure class="page-figure">
            <img src="../img/univers/mine.jpg" alt="Mine noyée avec arches de bois, rails disparaissant dans le noir et lampe de travail ambrée" loading="lazy">
            <figcaption>La Mine : une ancienne prison, puis le lieu de l’écrasement de l’avion du Comité Sumek et de la dispersion des échantillons d’Utopia.</figcaption>
          </figure>
          <div class="lore-quote">
            « La trahison de la Bravo Team, le secret de l’avion, et la disparition des échantillons : c’est le point de bascule du lore de Kamona. »
          <div class="lore-quote">
            « La trahison de la Bravo Team, le secret de l’avion, et la disparition des échantillons : c’est le point de bascule du lore de Kamona. »
            <cite>Recoupement Grokipedia / wiki communautaire</cite>
          </div>
          <p>C’est le seul événement où une action collective documentée explique à la fois <strong>Utopia</strong>, <strong>la Mine</strong>, <strong>la réputation de Renoir</strong> et <strong>la suspicion internationale</strong>. Si vous ne deviez retenir qu’un épisode du lore, c’est celui-là. <span class="src-tag src-communautaire">Communauté</span></p>

          <h2 id="darkzone">7. Naissance de la Dark Zone</h2>
          <p>La Dark Zone est le nom donné au territoire où le conflit se poursuit après l’armistice. Ses caractéristiques, confirmées par la communauté :</p>
          <ul>
            <li><strong>Zone sans loi.</strong> Aucune autorité Kamonaise n’y est présente de façon effective.</li>
            <li><strong>Conflit de basse intensité permanent.</strong> Escarmouches, trahisons, récupérations de ressources, cellules de réseau.</li>
            <li><strong>Arena des PMC.</strong> Les entreprises militarisées privées y font leurs affaires, à travers des contrats à risque et à forte récompense.</li>
            <li><strong>Zone d’enjeu.</strong> Les sites historiques (TV Station, Armory, Mine, Port, Northridge, Guoyapos) y sont là où se concentrent les régressions.</li>
          </ul>
          <p>Le jeu traduit cela par une règle simple, répétée dans les textes de mission in-game : <em>« seul ce que vous sortez de la Dark Zone vous appartient »</em>. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="lore-quote">
            « Bien que cet endroit soit rempli de trésors, seul ce que vous emportez hors de la Dark Zone vous appartient. Ceux qui y sont déjà venus vous diront que votre sécurité dépend de l’argent que vous avez. »
            <cite>Mission in-game « Abundant Profit » — texte officiel</cite>
          </div>
          <p>Le détail est lu pour un joueur : la sécurité est proportionnelle au capital transporté. Un pauvre en loot est un joueur que personne ne tuerait pour rien. <span class="src-tag src-officiel">Officiel</span></p>
          <p>Voir la page dédiée : <a href="univers-dark-zone.html">La Dark Zone — modes, sites et implications pratiques</a>.</p>

          <h2 id="utopia">8. Utopia : l’origine du mystère de la Saison 7</h2>
          <p>La Saison 7 <strong>Utopia</strong> est le premier moment où le jeu relie explicitement la Saison 7 à l’histoire de Kamona. L’annonce officielle est claire sur un point et volontairement muet sur tout le reste. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="facts">
            <div class="fact"><span class="fact-label">Événement</span><span class="fact-value">Fuite du réactif Utopia</span></div>
            <div class="fact"><span class="fact-label">Conséquence</span><span class="fact-value">Crise à l’échelle de Kamona</span></div>
            <div class="fact"><span class="fact-label">Origine</span><span class="fact-value">Non communiquée</span></div>
            <div class="fact"><span class="fact-label">Responsable</span><span class="fact-value">Non désigné</span></div>
          </div>
          <p>Le studio a explicitement indiqué que ni l’origine du réactif, ni sa fonction, ni le responsable de la perte de contrôle n’étaient expliqués. <span class="src-tag src-officiel">Officiel</span> Les zones infectées apparaissent sur <strong>Farm, Valley et Airport</strong>, et le matériel de développement relie l’épisode aux installations situés <strong>sous la TV Station</strong>. <span class="src-tag src-officiel">Officiel</span></p>

          <figure class="page-figure">
            <img src="../img/univers/utopia-reactor.jpg" alt="Chambre de reacteur souterraine scellee, viroles de refroidissement cyan et passerelles grillees" loading="lazy">
            <figcaption>Les développements de MoreFun ont relie l’outbreak d’Utopia aux installations situées sous la TV Station. L’installation elle-même n’a jamais été montrée.</figcaption>
          </figure>

          <p>Un second loot rouge fait de poids égal à Utopia, <strong>Elysium</strong>, est disponible en S7 dans les zones infectées, avec une garantie via la ligne de mission zombie. <span class="src-tag src-officiel">Officiel</span> Cela suggère que le réactif d’Utopia n’est pas un objet unique, mais une <strong>classe de matériel bio-technologique</strong> déjà largement diffusée avant la fuite. <span class="src-tag src-theorie">Théorie</span></p>

          <h2 id="chronologie">9. Chronologie de Kamona</h2>
          <div class="timeline">
            <div class="tl-item">
              <p class="tl-year">Avant la guerre</p>
              <h4>Déclaration d’indépendance du Second Clan</h4>
              <p>Renoir Brady quitte l’armée avec Ajax Jones. Derwin Pan a refusé de couler le Polaris et mute. Les Mad Dogs s’organisent dans les prisons de la Mine. <span class="src-tag src-rapporte">Rapporte</span></p>
            </div>
            <div class="tl-item">
              <p class="tl-year">Pendant la guerre</p>
              <h4>Prise de la TV Station et de l’Armory de Marulos</h4>
              <p>Les White Wolves fortifient la TV Station (inondation au gaz, laboratoire secret). La Kamona Liberation Army s’empare de l’Armory, crée un troisième pôle. Les ports deviennent le théâtre d’affrontements pour des disquettes de données. <span class="src-tag src-communautaire">Communauté</span></p>
            </div>
            <div class="tl-item ev">
              <p class="tl-year">Operation Peacemaker / Blackout</p>
              <h4>La trahison de la Bravo Team</h4>
              <p>La batterie antiaérienne est redirigée sur l’avion du Comité Sumek, qui transportait des échantillons d’Utopia. Crash dans la Mine. Renoir Brady est accusé ; sa réputation est abîmée. <span class="src-tag src-communautaire">Communauté</span></p>
            </div>
            <div class="tl-item">
              <p class="tl-year">Armistice</p>
              <h4>Le Comité Sumek médie la fin des hostilités</h4>
              <p>Fin publique de la guerre Nord-Sud. Le Comité réquisitionne ensuite la TV Station pour des raisons non déclarées. <span class="src-tag src-communautaire">Communauté</span></p>
            </div>
            <div class="tl-item">
              <p class="tl-year">Après l’armistice</p>
              <h4>La guerre larvée</h4>
              <p>Apparition de la Dark Zone. Les PMC s’installent. Doss Antonio bâtit le Norteno Court, la famille Antonio et les Mad Dogs se structurent, Derwin Pan contrôle un port. <span class="src-tag src-communautaire">Communauté</span></p>
            </div>
            <div class="tl-item">
              <p class="tl-year">Incident de la TV Station</p>
              <h4>EDELWEISS rappelée</h4>
              <p>EDELWEISS est rappelée pour reprendre le commandement de la TV Station et gérer les conséquences. MNST lui ordonne ensuite de sécuriser l’aéroport de Guoyapos comme base avancée : au cours du repérage, l’escouade des White Wolves est embusquée par la Blackgold Squad. <span class="src-tag src-officiel">Officiel</span></p>
            </div>
            <div class="tl-item mys">
              <p class="tl-year">Saison 7 — 16 septembre 2026</p>
              <h4>La fuite d’Utopia</h4>
              <p>Le réactif Utopia s’échappe et provoque une crise à l’échelle de Kamona. Apparition des infectés sur Farm, Valley et Airport, du mode Zombie Endless et du loot rouge Elysium. <span class="src-tag src-officiel">Officiel</span></p>
            </div>
          </div>

          <h2 id="mysteres">10. Les mystères non résolus</h2>
          <p>Le lore de Kamona est délibérément fragmentaire. Les trous ne sont pas des oublis de la communauté : ce sont des <strong>véritables zones d’ombre</strong>, que le studio remplit progressivement. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Qui a fabrique Utopia, et pour quoi ?</h4>
              <p>Ni l’origine, ni la fonction, ni le responsable ne sont donnés par MoreFun. L’hypothèse dominante est qu’Utopia était un programme de recherche militaire ou industriel, déjà conduit avant la guerre. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Qu’était le projet Gungnir ?</h4>
              <p>Un programme de type « armée stratégique » est cité par la communauté qui aurait incubé sous la TV Station. Aucun document officiel du Comité Sumek ne le mentionne pas dans les sources recoupées. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Qu’est-ce que l’Apostle ?</h4>
              <p>Les <strong>Archives du Kamona Investigation Bureau</strong> publient un dossier intitulé « Apostle », qui révèle un contexte historique et des dynamiques clandestines. Le contenu exact du dossier n’est pas documenté par une source tierce. <span class="src-tag src-rapporte">Rapporte</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Le réseau Toland</h4>
              <p>Une corporation transnationale pharma-défense, présent dans les théories communautaires comme le commanditaire possible du laboratoire sous la TV Station. Aucune mention officielle confirmée dans les notes de patch. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Le Secret Document</h4>
              <p>Un document confidentiel rouge, dont la circulation en raid alimente les théories. Sa nature exacte et sa valeur de monétisation restent non confirmées par l’éditeur. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>La voix inconnue de la radio</h4>
              <p>Pendant l’affrontement de Hecate à Marulos Farms, une voix anonyme la contacte par radio et lui dit de ne pas partir — « le camp de garde vous traitera bien ». L’identité de l’interlocuteur n’a jamais été révélée. <span class="src-tag src-rapporte">Rapporte</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Le sort de Doctor Mihalio</h4>
              <p>Le scientifique qui intéressait toutes les factions a été évacué par Blackgold sous escorte, ambuscade par les White Wolves, puis déplacé aux Marulos Farms, avant de tomber sous contrôle de sous-traitants. Sa localité de recherche exacte et sa destination finale restent inconnues. <span class="src-tag src-communautaire">Communauté</span></p>
            </div>
          </div>

          <h2 id="implications">11. Ce que le lore change en jeu</h2>
          <p>Le lore n’est pas décoratif : il prédit la densité de danger et la densité de loot. Voici la traduction opérationnelle. <span class="src-tag src-communautaire">Communauté</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Signal du lore</th><th>Lecture en jeu</th><th>Action concrète</th></tr></thead>
              <tbody>
                <tr><td>Un site est un <strong>nœud stratégique</strong> (TV Station, Armory, Mine, Airport)</td><td>Compensation élevée, contesté, boss</td><td>Équipe complète, munitions de pénétration, budget élevé</td></tr>
                <tr><td>Un site est un <strong>lieu de marché noir</strong> (Port, Valley, Norteno Court)</td><td>Objets de valeur, coffres, mais peu de munitions</td><td>Budget moyen, prioriser l’extracteur et les coffres</td></tr>
                <tr><td>Un <strong>boss de faction</strong> apparaît</td><td>Sa faction contrôle la zone ce jour-là</td><td>Éviter l’axe du boss ; opportunité de farm de tokens</td></tr>
                <tr><td>Les <strong>renseignements</strong> (disquettes, archives)</td><td>valeur narrative et officielle</td><td>Ne pas sacrifier une extraction pour un objet de récit</td></tr>
                <tr><td>Une <strong>zone infectée</strong> (S7)</td><td>Bonus de risque + bonus de loot rouge</td><td>Combiner masque, sprint court, Elysium en priorité</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>La règle qui résume tout</h4>
            <p>Un site à fort enjeu narratif est presque toujours un site à fort enjeu financier, et un site à fort enjeu financier est presque toujours un site ou l’on meurt. Le lore vous donne la carte ; l’équipement décide de l’issue.</p>
          </div>

          <h2 id="sources">12. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Annonce de la Saison 7 : Utopia</span> — MoreFun Studios / idcgames. Lancement le 16 septembre 2026, fuite du réactif Utopia, origine et responsable non expliqués. <a href="https://idcgames.com/en/arena-breakout-infinite/news/arena-breakout-infinite-season-7-utopia-engulfs-kamona-in-a-new-crisis-on-september-16-2026-09-08-06-42-13766" target="_blank" rel="noopener">idcgames.com</a></li>
            <li><span class="src-name">Notes de mise à jour S1 à S7</span> — Steam / site officiel. Textes de mission « Dusk to Dawn », « A Debt Unpaid », « Abundant Profit », « Smooth Extraction », « Sanctuary Recon », « Signal Interference », « Send Signal ». <a href="https://steamcommunity.com/app/2073620/announcements/" target="_blank" rel="noopener">steamcommunity.com</a></li>
            <li><span class="src-name">S7 UTOPIA Arrives with Massive Rewards</span> — MoreFun Studios, 15 septembre 2026 : Elysium comme loot rouge de valeur égale à Utopia, limite de la Collection Room. <a href="https://senseos.gg/guides/arena-breakout-infinite/red-items/" target="_blank" rel="noopener">senseos.gg</a></li>
            <li><span class="src-name">Story of Kamona</span> — série officielle YouTube : <em>First Season Documentary</em>, <em>EP.03 Red Smoke</em>, <em>EP.04 The Key</em>, <em>EP.05 RAT</em>, <em>EP.06 Dogtag</em>, plus <em>No Man’s Land</em> et <em>A Golden Opportunity</em>. <a href="https://www.youtube.com/@ArenaBreakoutInfinite" target="_blank" rel="noopener">youtube.com/@ArenaBreakoutInfinite</a></li>
            <li><span class="src-name">Kamona Investigation Bureau Archives ① et ②</span> — publications officielles (X, Facebook, Instagram) : origines de la Dark Zone, causes de la guerre, dossier « Apostle ».</li>
            <li><span class="src-name">Official Kamona Investigation Mission Overview</span> — trailer officiel de mission narrative : le joueur est un enquêteur qui récupère des documents confidentiels dans des sites abandonnés.</li>
            <li><span class="src-name">Description officielle Arena Breakout (2022)</span> — définitions de <em>Tac Ops</em> (Agents) et <em>Covert Ops</em> (Rogues) et des « Dark Zone Pioneers ». <a href="https://arenabreakout.com/web202210/news/notice.html" target="_blank" rel="noopener">arenabreakout.com</a></li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">Arena Breakout Wiki (Fandom)</span> — page Kamona : chronologie de la guerre, alliances, sites, personnages. <a href="https://arena-breakout.fandom.com/wiki/Kamona" target="_blank" rel="noopener">arena-breakout.fandom.com</a></li>
            <li><span class="src-name">Grokipedia — Kamona</span> — synthèse secondaire recoupant factions, chronologie et rôle des PMC ; source la plus dense pour l’Operation Blackout. <a href="https://grokipedia.com/page/Kamona" target="_blank" rel="noopener">grokipedia.com</a></li>
            <li><span class="src-name">NamuWiki — Arena Breakout / Boss</span> — fiches de boss, affiliations, armes et tokens. <a href="https://en.namu.wiki/w/Arena%20Breakout/%EB%B3%B4%EC%8A%A4" target="_blank" rel="noopener">en.namu.wiki</a></li>
            <li><span class="src-name">Reddit r/ArenaBreakoutInfinite et r/ArenaBreakoutGlobal</span> — fils « Does anyone know who all the factions are », « ABI / White Nights lore », archives du Bureau, analyses du Secret Document.</li>
            <li><span class="src-name">senseos.gg</span> — registre des boss, guide des loot rouges et de l’event S7. <a href="https://senseos.gg/guides/arena-breakout-infinite/bosses-list/" target="_blank" rel="noopener">senseos.gg</a></li>
          </ul>
          <h3>Théories (non confirmées)</h3>
          <ul class="src-list">
            <li>Corporation Toland, « l’Ark » sous la TV Station, projet Gungnir, projet Apostle, agents d’élimination « Cleaners » et la figure « Arachne » : recoupées par des posts Reddit et un site générateur automatique, <strong>sans confirmation officielle</strong>.</li>
            <li>Les archives du Bureau no 2 selon un post Reddit : CDIS aurait possédé la Valley et Northridge avant que MNST ne les reprenne. Information issue d’un post communautaire, à confirmer auprès de la source primaire.</li>
            <li>Confusion courante entre les <strong>White Wolves</strong> (faction lore, parrainée par Tevilla) et la <strong>Saison 6 White Nights</strong> (nom de saison officiel). Deux entités sans rapport.</li>
          </ul>
        """
