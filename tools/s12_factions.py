# -*- coding: utf-8 -*-
"""S12 — Contenu de la page univers-factions.html."""

CONTENT = r"""
          <div class="lore-legend">
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">annonces, notes de patch, archives et vidéos de MoreFun Studios</span>
            <span class="src-tag src-communautaire">Communautaire</span><span class="lg-txt">wikis, Reddit, guides tiers recoupés</span>
            <span class="src-tag src-theorie">Théorie</span><span class="lg-txt">cohérente mais jamais confirmée</span>
            <span class="src-tag src-rapporte">Rapporté</span><span class="lg-txt">source secondaire, recoupement partiel</span>
          </div>

          <figure class="page-figure">
            <img src="../img/univers/blackgold-pmc.jpg" alt="Escouade de mercenaires en uniforme bleu nuit avec insignes dorés, devant un véhicule blindé devant une station-service en ruine" loading="lazy">
            <figcaption>Blackgold Universal : une entreprise militaire privée de Colom, bien équipée, disciplinée, et toujours du mauvais côté de l’armistice.</figcaption>
          </figure>

          <h2 id="vue">1. Vue d’ensemble</h2>
          <p>Le lore de Kamona repose sur une structure simple : <strong>deux puissances étrangères parient deux armées locales, un tiers groupe refuse de choisir, et une constellation d’organisations criminelles exploite le chaos</strong>. Les PMC que vous incarnez constituent la quatrième couche, celle qui arrive une fois que tout le monde est déjà installé. <span class="src-tag src-communautaire">Communautaire</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Faction</th><th>Nature</th><th>Camp</th><th>Territoire</th><th>Chef / figure</th></tr></thead>
              <tbody>
                <tr><td><strong>Tevilla</strong></td><td>Puissance étrangère</td><td><span class="text-blue">Nord</span></td><td>Sponsor du Nord</td><td>État non nommé</td></tr>
                <tr><td><strong>White Wolves Squad</strong></td><td>Unité d’élite (forces spéciales)</td><td><span class="text-blue">Nord</span></td><td>TV Station, Guoyapos</td><td>Chef non identifié</td></tr>
                <tr><td><strong>Colom</strong></td><td>Puissance étrangère</td><td><span class="text-orange">Sud</span></td><td>Sponsor du Sud</td><td>État non nommé</td></tr>
                <tr><td><strong>Alpha Team</strong></td><td>Special Air Service de Colom</td><td><span class="text-orange">Sud</span></td><td>Opérations conjointes</td><td>Chef non identifié</td></tr>
                <tr><td><strong>Blackgold Universal</strong></td><td>PMC internationale</td><td><span class="text-orange">Sud</span></td><td>TV Station, Marulos Farms, Mine</td><td>Direction militaire</td></tr>
                <tr><td><strong>Abyss Squad</strong></td><td>Élite de Blackgold</td><td><span class="text-orange">Sud</span></td><td>Marulos Farms, Northridge</td><td>Hecate</td></tr>
                <tr><td><strong>MNST / Front du Nord</strong></td><td>Armée régulière du Nord</td><td><span class="text-blue">Nord</span></td><td>Armory, TV Station</td><td>Renoir Brady (4<sup>e</sup> brigade)</td></tr>
                <tr><td><strong>CDIS / Armée du Sud</strong></td><td>Armée régulière du Sud</td><td><span class="text-orange">Sud</span></td><td>TV Station, ports</td><td>Commandement non nommé</td></tr>
                <tr><td><strong>Kamona Liberation Army</strong></td><td>Force dissidente locale</td><td><span class="text-gold">Tiers</span></td><td>Marulos Armory, Marulos Farms</td><td>Renoir Brady &amp; Ajax Jones</td></tr>
                <tr><td><strong>Comité Sumek</strong></td><td>Organisation internationale</td><td><span class="text-muted">Neutre</span></td><td>TV Station (après l’armistice)</td><td>Non désigné</td></tr>
                <tr><td><strong>Kamona Investigation Bureau</strong></td><td>Service d’enquête</td><td><span class="text-muted">Neutre</span></td><td>Dossier / archives</td><td>Non désigné</td></tr>
                <tr><td><strong>EDELWEISS</strong></td><td>Commandement militaire</td><td><span class="text-blue">Nord</span></td><td>TV Station, Guoyapos</td><td>EDELWEISS</td></tr>
                <tr><td><strong>Famille Antonio</strong></td><td>Organisation criminelle</td><td><span class="text-gold">Neutre</span></td><td>Floranpino Valley, Norteno Court</td><td>Doss Antonio</td></tr>
                <tr><td><strong>Mad Dogs</strong></td><td>Gang de prisonniers</td><td><span class="text-gold">Neutre</span></td><td>La Mine, le Valley</td><td>Stephen</td></tr>
                <tr><td><strong>Mutins du Polaris</strong></td><td>Réseau de marché noir</td><td><span class="text-gold">Neutre</span></td><td>Zone portuaire</td><td>Derwin Pan &amp; Rodriquez</td></tr>
                <tr><td><strong>PMC indépendants</strong></td><td>Sociétés de mercenaires</td><td><span class="text-muted">Sans camp</span></td><td>Partout</td><td>Vous</td></tr>
                <tr><td><strong>Corporation Toland</strong></td><td>Groupe pharmo-militaire</td><td><span class="text-muted">Inconnu</span></td><td>Laboratoire sous la TV Station</td><td>Aucune source officielle</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="puissances">2. Les deux puissances étrangères</h2>
          <div class="lore-grid">
            <div class="lore-card north">
              <h4>Tevilla</h4>
              <p class="lore-sub">Puissance du Nord — rôle de parrain</p>
              <p>Tevilla est une <strong>puissance militaire étrangère située au nord de Kamona</strong>. Elle n’est pas une faction « jouable » : elle n’apparaît jamais comme une entité en jeu. Son rôle est de <strong>fournir un appui militaire et logistique au Front du Nord</strong>, principalement via son unité d’élite, la White Wolves Squad. C’est ce qui permet au Nord de tenir dans la durée face au Sud. <span class="src-tag src-communautaire">Communautaire</span></p>
              <ul>
                <li>Position : Nord de l’archipel, frontière montagneuse</li>
                <li>Instrument : la White Wolves Squad</li>
                <li>Objectif apparent : consolider le contrôle du Nord sur les sites stratégiques</li>
                <li>Après l’armistice : soutien maintenu en clandestinité <span class="src-tag src-rapporte">Rapporte</span></li>
              </ul>
              <p class="text-muted small">La terminologie exacte de l’État n’est pas documentée : la communauté emploie indifféremment « Tevilla », « Tevila » ou « Fédération de Tevila ». <span class="src-tag src-theorie">Théorie</span></p>
            </div>
            <div class="lore-card south">
              <h4>Colom</h4>
              <p class="lore-sub">Puissance du Sud — rôle de parrain</p>
              <p>Colom est une <strong>puissance étrangère située au sud de Kamona</strong>, qui soutient l’Armée du Sud (CDIS). Sa signature opérationnelle est l’<strong>Alpha Team</strong>, une unité de spécialistes aéronautiques (Colom Special Air Servicemen) déployée en opérations conjointes avec le Comité Sumek. Colom fait également appel à une PMC privée, Blackgold Universal, pour l’action de terrain. <span class="src-tag src-communautaire">Communautaire</span></p>
              <ul>
                <li>Position : Sud de l’archipel</li>
                <li>Instruments : Alpha Team (militaire), Blackgold Universal (privé)</li>
                <li>Point noir : la réputation de Colom dans l’Operation Blackout — son Alpha Team n’a pas extrait <span class="src-tag src-rapporte">Rapporte</span></li>
              </ul>
              <p class="text-muted small">Comme Tevilla, le nom officiel complet de l’État n’est pas documenté par une source primaire. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>

          <h2 id="locales">3. Les forces locales</h2>
          <div class="lore-grid">
            <div class="lore-card north">
              <h4>MNST — Front du Nord</h4>
              <p class="lore-sub">Armée régulière du Nord</p>
              <p>Le MNST (sigle retenu par la communauté) est la <strong>force militaire régulière du Nord</strong>, secondée par Tevilla. Le jeu la mentionne explicitement dans les textes de mission : c’est MNST qui ordonne à EDELWEISS de sécuriser l’aéroport de Guoyapos comme base avancée après l’incident de la TV Station. <span class="src-tag src-officiel">Officiel</span></p>
              <ul>
                <li>Postes : TV Station, Marulos Armory, aéroport de Guoyapos</li>
                <li>Figures : Renoir Brady, EDELWEISS, les White Wolves</li>
                <li>Après-guerre : présence militaire réduite, mais influence intacte</li>
              </ul>
            </div>
            <div class="lore-card south">
              <h4>CDIS — Armée du Sud</h4>
              <p class="lore-sub">Armée régulière du Sud</p>
              <p>Le CDIS est la <strong>force militaire régulière du Sud</strong>, soutenue par Colom. Le sigle apparaît dans les archives du Kamona Investigation Bureau, qui suggèrent que le CDIS aurait antérieurement contrôlé la Valley et Northridge avant que le MNST ne récupère ces territoires. <span class="src-tag src-rapporte">Rapporte</span></p>
              <ul>
                <li>Postes : TV Station, ports, Marulos Farms</li>
                <li>Figures : Randall Fisher (contact CDIS devenu boss Blackgold)</li>
                <li>Relation avec Blackgold : le CDIS emploie des éléments de la PMC, pas l’inverse</li>
              </ul>
            </div>
            <div class="lore-card gold">
              <h4>Kamona Liberation Army</h4>
              <p class="lore-sub">Renoir Brady &amp; Ajax Jones</p>
              <p>La troisième force. Née de la déclaration d’indépendance du Second Clan, elle est dirigée par <strong>Renoir Brady</strong>, ancien commandant de la 4<sup>e</sup> brigade d’infanterie blindée, avec <strong>Ajax Jones</strong> comme subordonné de terrain. Leur prise de l’Armory de Marulos crée un <strong>pôle neutre de fait</strong> que ni le Nord ni le Sud ne peut easily neutraliser. <span class="src-tag src-communautaire">Communautaire</span></p>
              <ul>
                <li>Postes : Marulos Armory (bunker sud), Marulos Farms</li>
                <li>Ambiguïté : alliés du Nord, mais structure de commandement locale</li>
                <li>Faiblesse : Hecate franchit la ligne d’armistice et les chasse des Farms</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>EDELWEISS</h4>
              <p class="lore-sub">Commandement militaire réactivé</p>
              <p>EDELWEISS est un <strong>commandement militaire rappelé</strong> après l’incident de la TV Station, avec mission de reprendre le commandement de la station et d’en gérer les conséquences. Le texte officiel de la Saison 4 précise ensuite que MNST l’envoie sécuriser l’aéroport de Guoyapos. <span class="src-tag src-officiel">Officiel</span></p>
              <ul>
                <li>Trajectoire : TV Station → aéroport de Guoyapos</li>
                <li>Contexte : la tension dans la Dark Zone s’intensifie</li>
                <li>Point de rupture : l’escouade White Wolves est embusquée par la Blackgold Squad</li>
              </ul>
            </div>
          </div>

          <h2 id="pmc">4. Les entreprises militaires privées</h2>
          <figure class="page-figure">
            <img src="../img/univers/white-wolves.jpg" alt="Campement militaire enneigé sous filet de camouflage blanc en forêt de sapins, neige au sol" loading="lazy">
            <figcaption>La White Wolves Squad, unité d’élite de Tevilla, au camouflage blanc. C’est la seule formation documentée qui porte une identité visuelle de faction.</figcaption>
          </figure>

          <div class="lore-card gold" style="margin-bottom: var(--space-lg);">
            <h4>Blackgold Universal</h4>
            <p class="lore-sub">PMC internationale — bras armé de Colom</p>
            <p>Blackgold Universal est une <strong>entreprise militaire privée internationale</strong>, principale exécuteur des intérêts méridionaux. Elle déploie des opérateurs sur la TV Station et les Marulos Farms, et son unité d’élite, l’<strong>Abyss Squad</strong>, est celle qui commet la trahison de l’Operation Blackout. Blackgold dispose aussi de tout un appareil de contacts : le <strong>contact book</strong> (Randall Fisher) fait office de recruteur de PMC, avec ses propres contrats de missions. <span class="src-tag src-communautaire">Communautaire</span></p>
            <ul>
              <li>Rôle :PMC de soutien du Sud, mais avec agenda propre</li>
              <li>Signature : l’<strong>Abyss Squad</strong> et sa cheffe Hecate</li>
              <li>Méthode : embuscades nocturnes, intervention surgicale, rupture de la ligne d’armistice</li>
              <li>Enjeu interne : la trahison du Comité Sumek pour des raisons non élucidées</li>
            </ul>
          </div>

          <figure class="page-figure">
            <img src="../img/univers/hecate-abyss.jpg" alt="Opératrice encapuchonnée dans une caverne rituelle, lumière violette et cyan, encens" loading="lazy">
            <figcaption>Hecate et l’Abyss Squad : l’unité d’élite de Blackgold, celle qui a franchi la ligne d’armistice et trahi le Comité Sumek.</figcaption>
          </figure>
          <div class="lore-card south" style="margin-bottom: var(--space-lg);">
            <h4>Abyss Squad — les « abysses » de Blackgold</h4>
            <p class="lore-sub">Élite de Blackgold — commandée par Hecate</p>
            <p>L’Abyss Squad est l’unité de company-level de Blackgold Universal, et <strong>Hecate</strong> en est la cheffe de terrain. <span class="src-tag src-rapporte">Rapporte</span> Ses opérations sont documentées : la percée de la ligne d’armistice à Marulos Farms qui force Ajax Jones à se replier, puis la trahison de l’Operation Blackout. <strong>Obol</strong> et <strong>Viper</strong> appartiennent à la même unité. <span class="src-tag src-rapporte">Rapporte</span></p>
            <ul>
              <li>Responsable d’opérations : le terrain, pas la stratégie</li>
              <li>Signature : discrétion, timing, usage de la nuit</li>
              <li>Point faible : le radio-message mystérieux qui l’immobilise sur la ferme</li>
            </ul>
            <p class="text-muted small">Un nom de guerre ou un pseudonyme de quartier pour « Hecate » apparaît dans le lore, mais son nom civil n’est jamais révélé. <span class="src-tag src-theorie">Théorie</span></p>
          </div>

          <h2 id="neutres">5. Les acteurs non belligérants</h2>
          <div class="lore-grid">
            <div class="lore-card neutral">
              <h4>Comité Sumek</h4>
              <p class="lore-sub">Organisation internationale — médiateur</p>
              <p>Le Comité Sumek est l’<strong>organisation internationale neutre</strong> qui médiatise la fin des hostilités. Il finance et protège des vols d’aide humanitaire, lance l’Operation Peacemaker et ses deux équipes conjointes (Alpha et Bravo), puis réquisitionne la TV Station après l’Operation Blackout. Sa neutralité est <strong>officielle mais discontinue</strong> : lhotmail chargement d’échantillons d’Utopia plutôt que de l’aide montre que le Comité transporte autre chose. <span class="src-tag src-communautaire">Communautaire</span></p>
              <ul>
                <li>Objectif déclaré : faire cesser la guerre</li>
                <li>Objectif réel (déduit) : controlling les échantillons d’Utopia</li>
                <li>Après l’armistice : contrôle de la TV Station</li>
              </ul>
            </div>
            <div class="lore-card neutral">
              <h4>Kamona Investigation Bureau</h4>
              <p class="lore-sub">Service d’enquête — narrateur du lore</p>
              <p>Le Bureau d’enquête de Kamona est l’<strong>organisme qui publie le lore</strong>. Ses « Archives » sont diffusées par les canaux officiels (X, Facebook, Instagram) et compilent les résultats d’enquête sur les <strong>origines de la Dark Zone</strong>, les <strong>causes de la guerre Nord-Sud</strong> et les <strong>personnages influents</strong>. L’un des dossiers publiés porte le titre « Apostle ». <span class="src-tag src-rapporte">Rapporte</span></p>
              <ul>
                <li>Archive n° 1 : origines et causes de la guerre</li>
                <li>Archive n° 2 : contrôle territorial du CDIS et du MNST</li>
                <li>Dossier « Apostle » : contexte historique et dynamiques clandestines</li>
              </ul>
            </div>
          </div>

          <h2 id="criminelles">6. Les organisations criminelles</h2>
          <div class="lore-grid">
            <div class="lore-card gray">
              <h4>Famille Antonio</h4>
              <p class="lore-sub">Doss Antonio</p>
              <p>Organisation criminelle qui prospère dans l’anarchie de l’après-guerre. <strong>Doss Antonio</strong> (aussi appelé Doss Anthony) transforme sa richesse en pouvoir territorial : il embauche des sbires dont <strong>Porrero Kazan</strong>, passe des contrats auprès des White Wolves pour obtenir du soutien, et finance la construction du <strong>Norteno Court</strong> comme la rénovation de bâtiments d’une vallée. Il opère depuis la <strong>Villa</strong>, avec une escorte armée et la capacité de rappeler des renforts. <span class="src-tag src-communautaire">Communautaire</span></p>
              <ul>
                <li>Base : Floranpino Valley, Norteno Court</li>
                <li>Code visuel : or, lunettes de soleil, costume d’affaires</li>
                <li>Token de boss : l’or travaillé artisanal</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>Mad Dogs</h4>
              <p class="lore-sub">Stephen</p>
              <p>Banditisme organisé dans les prisons de la <strong>Mine</strong>. Pendant la guerre, le gang de <strong>Stephen</strong> organise une émeute réussie contre le gardien et les gardes, avec l’aide de Porrero Kazan. La fracture interne suit : Porrero tente d’assassiner Stephen pour insubordination, est déposé, abandonné dans la mine, puis récupéré par les White Wolves. Le gang reste actif dans le Valley. <span class="src-tag src-communautaire">Communautaire</span></p>
              <ul>
                <li>Base : la Mine et le Valley</li>
                <li>Recrutement : le système pénitentiaire</li>
                <li>Sort de Porrero : White Wolves → famille Antonio</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>Mutins du Polaris</h4>
              <p class="lore-sub">Derwin Pan &amp; Rodriquez</p>
              <p>Le navire <em>Polaris</em> devait être coulé pour que la Marine du Nord ne soit pas démantelée. Son officier, <strong>Derwin Pan</strong>, refuse, tue ses supérieurs avec son F57 et provoque une mutinerie. Il construit ensuite avec <strong>Rodriquez</strong> un réseau de marché noir dans un port : le commerce illicite comme instrument de pouvoir. <span class="src-tag src-rapporte">Rapporte</span></p>
              <ul>
                <li>Base : la zone portuaire</li>
                <li>Spécialité : contrôle des routes et des prix</li>
                <li>Token de boss : la ceinture tranchée</li>
              </ul>
            </div>
            <div class="lore-card gray">
              <h4>PMC indépendants</h4>
              <p class="lore-sub">Vous</p>
              <p>Les entreprises militarisées privées convergent vers la Dark Zone <strong>après</strong> les autres : elles n’ont ni alliance, ni patrie, ni maison. Elles viennent pour le contrat. C’est exactement ce que dit la documentation officielle du premier jeu : en <em>Tac Ops</em> le joueur entre en tant qu’<strong>Agent</strong>, en <em>Covert Ops</em> en tant que <strong>Rogue</strong>, et les « Dark Zone Pioneers » peuvent être déguisés en Rogues. <span class="src-tag src-officiel">Officiel</span></p>
              <ul>
                <li>Motivation : le contrat, le loot, la réputation</li>
                <li>Acteurs centraux : le <strong>contact book</strong> (recruteur) et les marchands</li>
                <li>Statut : neutres sur le papier, mais la cible de tous</li>
              </ul>
            </div>
          </div>

          <h2 id="inconnues">7. Les factions que personne ne confirme</h2>
          <p>Elles reviennent dans les théories de la communauté et dans les documents non sourcés, mais aucune note de patch ni annonce officielle ne les mentionne. <span class="src-tag src-theorie">Théorie</span></p>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>La corporation Toland</h4>
              <p>Un groupe pharmo-militaire transnational qui aurait exploité le vide juridique de Kamona pour construire un laboratoire clandestin sous la TV Station, surnommé « l’Ark ». Source : discussions Reddit et sites générés automatiquement, sans confirmation. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Les « Cleaners » et la figure « Arachne »</h4>
              <p>Une unité d’élimination envoyée pour effacer les témoins et les traces après la perte de contrôle d’Utopia, avec un élément désigné sous le nom d’« Arachne, the Emerald Web » traquant les zones de contamination. Non documenté par l’éditeur. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>
          <div class="mystery">
            <span class="m-ico">?</span>
            <div>
              <h4>Les projets Gungnir et Apostle</h4>
              <p>Un programme d’armes stratégiques (Gungnir) et un programme de type « Apostle » sont cités comme ayant incubé sous la TV Station. Le dossier « Apostle » figure dans les archives officielles du Bureau, mais le contenu exact du programme reste non documenté par une source tierce. <span class="src-tag src-theorie">Théorie</span></p>
            </div>
          </div>

          <h2 id="personnages">8. Les personnages</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Personnage</th><th>Faction</th><th>Statut</th><th>Terrain</th><th>Signature</th></tr></thead>
              <tbody>
                <tr><td><strong>Benjamin Renoir Brady</strong></td><td>Kamona Liberation Army</td><td>Boss</td><td><a href="map-armory.html">Armory</a></td><td>RPK, MK14, AK-74N, Saiga-12 ; token « Insignia of Reversal »</td></tr>
                <tr><td><strong>Ajax Jones</strong></td><td>Kamona Liberation Army</td><td>Boss</td><td><a href="map-farm.html">Farm</a></td><td>MP5, AKS-74U, AKM, Bizon ; escorte « Jackson »</td></tr>
                <tr><td><strong>Hecate</strong></td><td>Abyss Squad (Blackgold)</td><td>Boss</td><td><a href="map-farm.html">Farm</a></td><td>MCX, MP5, MPX ; vision thermique ; token « Clean Climbing Hook »</td></tr>
                <tr><td><strong>Obol</strong></td><td>Abyss Squad</td><td>Boss d’event</td><td>Events S7</td><td>M14, BPZ ; armure de niveau 3</td></tr>
                <tr><td><strong>Viper</strong></td><td>Abyss Squad</td><td>Boss d’event</td><td>Events S7–S8</td><td>M24 + M80, SVDS + LPS ; jet de 120 cartouches</td></tr>
                <tr><td><strong>Fred Lee</strong></td><td>Indépendant / boss de zone</td><td>Boss</td><td><a href="map-northridge.html">Northridge</a></td><td>SVDS, M14, FAL, AR-30 ; escorte « Juve » ; token « Fred’s Wedding Ring »</td></tr>
                <tr><td><strong>Antonio Doss</strong></td><td>Famille Antonio</td><td>Boss</td><td><a href="map-valley.html">Valley</a></td><td>AKS-74U, MP5, F2000, Glock 18c ; or et costume</td></tr>
                <tr><td><strong>Porrero Kazan</strong></td><td>Mad Dogs puis Antonio</td><td>Boss</td><td>Mine / events</td><td>RPK, casque explosif ; token « clé de la prison de la Mine »</td></tr>
                <tr><td><strong>Derwin Pan</strong></td><td>Mutins du Polaris</td><td>Boss</td><td>Zone portuaire</td><td>RPK-16 à tambour 95 rounds, AEK, F57 ; token « ceinture tranchée »</td></tr>
                <tr><td><strong>Randall Fisher</strong></td><td>CDIS / Blackgold</td><td>Boss d’event</td><td>Events S4</td><td>Ancien forces spéciales de l’Union Océanique ; contact book de PMC</td></tr>
                <tr><td><strong>Kurt Williams, Rolf Schneider, Bernard Martin</strong></td><td>TV Station</td><td>Bosss</td><td><a href="map-tv-station.html">TV Station</a></td><td>Trio de la station ; retirés du récit après la S10 chinoise</td></tr>
                <tr><td><strong>Doctor Mihalio</strong></td><td>Aucune — objet de convoitise</td><td>Scientifique</td><td>Non fixé</td><td>Évadé par Blackgold, ambuscade des White Wolves, déplacé aux Farms</td></tr>
                <tr><td><strong>Evita</strong></td><td>Contact / medic</td><td>PNJ</td><td>Non fixé</td><td>Se dit fille de Mihalio, puis corrige ; coupe les liens avec les contractors</td></tr>
                <tr><td><strong>Stephen, Rodriquez</strong></td><td>Mad Dogs / marché noir</td><td>Secondaires</td><td>Mine / Port</td><td>Chef de gang et contact de contrebande</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-muted small">Les armes, les armures et les tokens de boss listés ci-dessus proviennent des fiches communautaires et namuwiki ; leur présence en jeu est vérifiable, leur lecture purement narrative reste déductive. <span class="src-tag src-rapporte">Rapporte</span></p>

          <h2 id="relations">9. Qui soutient qui</h2>
          <div class="table-wrap">
            <table class="data-table rel-matrix">
              <thead><tr><th>Faction</th><th>Tevilla</th><th>Colom</th><th>Comité Sumek</th><th>MNST</th><th>CDIS</th><th>KLA</th><th>Blackgold</th></tr></thead>
              <tbody>
                <tr><td>Tevilla</td><td class="yes">Soi</td><td class="no">Hostile</td><td class="mid">Neutre</td><td class="yes">Soutient</td><td class="no">Hostile</td><td class="mid">Soutient</td><td class="no">Hostile</td></tr>
                <tr><td>Colom</td><td class="no">Hostile</td><td class="yes">Soi</td><td class="mid">Neutre</td><td class="no">Hostile</td><td class="yes">Soutient</td><td class="no">Hostile</td><td class="yes">Emploie</td></tr>
                <tr><td>White Wolves</td><td class="yes">Émanation</td><td class="no">Hostile</td><td class="mid">Ambigu</td><td class="yes">Avec</td><td class="no">Hostile</td><td class="mid">Avec</td><td class="no">Hostile</td></tr>
                <tr><td>Alpha Team</td><td class="no">Hostile</td><td class="yes">Émanation</td><td class="yes">Conjoint</td><td class="no">Hostile</td><td class="yes">Avec</td><td class="no">Hostile</td><td class="mid">Trahit</td></tr>
                <tr><td>Abyss Squad</td><td class="no">Hostile</td><td class="yes">Sous Blackgold</td><td class="no">Trahi</td><td class="no">Hostile</td><td class="yes">Avec</td><td class="no">Hostile</td><td class="yes">Appartient</td></tr>
                <tr><td>Kamona Liberation Army</td><td class="mid">Sponsor</td><td class="no">Hostile</td><td class="mid">Accusé</td><td class="mid">Allié</td><td class="no">Hostile</td><td class="yes">Soi</td><td class="no">Hostile</td></tr>
                <tr><td>Famille Antonio</td><td class="mid">Client</td><td class="no">Hostile</td><td class="no">Indifférent</td><td class="mid">Client</td><td class="no">Hostile</td><td class="mid">Allié</td><td class="no">Hostile</td></tr>
                <tr><td>PMC indépendants</td><td class="no">Aucun</td><td class="no">Aucun</td><td class="mid">Contrats</td><td class="no">Aucun</td><td class="no">Aucun</td><td class="no">Aucun</td><td class="no">Concurrent</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-muted small">Lecture : <span class="text-green">vert</span> = lien établi et documenté, <span class="text-orange">orange</span> = lien ambigu ou daté, <span class="text-muted">gris</span> = aucun lien. <span class="src-tag src-communautaire">Communautaire</span></p>

          <h2 id="boss">10. Ce que les boss révèlent de leur faction</h2>
          <p>Chaque boss est l’<strong>avatar visible</strong> d’une faction. Son équipement, ses escortes et son token en disent plus long sur le camp que sur lui-même. <span class="src-tag src-rapporte">Rapporte</span></p>
          <ul>
            <li><strong>Les escortes ont un nom de famille commun.</strong> Les hommes d’Ajax Jones s’appellent tous « Jackson », ceux de Fred Lee tous « Juve ». C’est la signature d’une organisation, pas d’une bande : le clan est structuré.</li>
            <li><strong>Les niveaux de protection trahissent le budget.</strong> Un boss d’elite de PMC porte du T3–T4 et des opticiennes thermiques ; un chef de guerre civile porte du L4 et des classes 4.</li>
            <li><strong>Les tokens racontent une relation.</strong> La « clé de la prison de la Mine » de Porrero raconte son passé ; l’« Insignia of Reversal » de Renoir raconte son statut de dissident ; le « Clean Climbing Hook » de Hecate raconte une opération d’infiltration.</li>
            <li><strong>Les signatures d’arme.</strong> Hecate, Obol et Viper partagent le même ADN d’équipement : ce sont des fratries d’arme, pas des Individus.</li>
          </ul>

          <h2 id="implications">11. Implications pratiques</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Faction dominante</th><th>Zone</th><th>Boss associé</th><th>Ce que ça change pour vous</th></tr></thead>
              <tbody>
                <tr><td>Kamona Liberation Army</td><td><a href="map-armory.html">Armory</a>, <a href="map-farm.html">Farm</a></td><td>Renoir, Ajax</td><td>Densité de PNJ élevée : imaginez des grenades, ne tirez pas en rafale dans les couloirs</td></tr>
                <tr><td>Abyss Squad (Blackgold)</td><td><a href="map-farm.html">Farm</a>, <a href="map-northridge.html">Northridge</a></td><td>Hecate, Obol, Viper</td><td>Adversaires disciplinés : surveillez les angles hauts, la lunette thermique change les règles</td></tr>
                <tr><td>Famille Antonio</td><td><a href="map-valley.html">Valley</a></td><td>Doss Antonio</td><td>Zone de valeur plutôt que de bullets : coffres, clés, marchands, corps gardés</td></tr>
                <tr><td>Mad Dogs</td><td>Mine / events</td><td>Porrero Kazan</td><td>Hostilité de proximité : casque explosif, charges, attention aux recoins Aveugles</td></tr>
                <tr><td>Mutins du Polaris</td><td>Zone portuaire</td><td>Derwin Pan</td><td>Alerte sonore : il diffuse sur les haut-parleurs, couper l’alarme est prioritaire</td></tr>
                <tr><td>TV Station</td><td><a href="map-tv-station.html">TV Station</a></td><td>Kurt, Rolf, Bernard</td><td>Trio redoutable : soit vous les séparez, soit vous les affrontez ensemble</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>La règle de lecture d’un boss</h4>
            <p>Avant d Engaging un boss, demandez-vous à quelle faction il appartient et qui le paie. Un boss de PMC est un <strong>problème tactique</strong> (équipement, escortes, discipline). Un boss de guerre civile est un <strong>problème politique</strong> (nombreux, imprévisibles, hostiles à tout le monde). Vos tactiques ne sont pas les mêmes.</p>
          </div>

          <h2 id="sources">12. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Notes de mise à jour ABI (Steam / site officiel)</span> — missions de saison : « Dusk to Dawn » (EDELWEISS, MNST, aéroport de Guoyapos, embuscade White Wolves / Blackgold), « A Debt Unpaid » (faction inconnue, traces de Lab 76, force spéciale échappée de la TV Station, opération en cours de la Dark Zone), « Abundant Profit », « Send Signal ». <a href="https://steamcommunity.com/app/2073620/announcements/" target="_blank" rel="noopener">steamcommunity.com</a></li>
            <li><span class="src-name">Annonce de la Saison 7 : Utopia</span> — MoreFun Studios, origine et responsable du réactif non expliqués. <a href="https://idcgames.com/en/arena-breakout-infinite/news/arena-breakout-infinite-season-7-utopia-engulfs-kamona-in-a-new-crisis-on-september-16-2026-09-08-06-42-13766" target="_blank" rel="noopener">idcgames.com</a></li>
            <li><span class="src-name">Description officielle Arena Breakout (2022)</span> — <em>Tac Ops</em> / <em>Covert Ops</em>, Agents et Rogues, Dark Zone Pioneers. <a href="https://arenabreakout.com/web202210/news/notice.html" target="_blank" rel="noopener">arenabreakout.com</a></li>
            <li><span class="src-name">Kamona Investigation Bureau Archives ① et ②</span> — publications officielles : origines de la Dark Zone, causes de la guerre, dossier « Apostle », attributions territoriales CDIS / MNST.</li>
            <li><span class="src-name">Story of Kamona</span> — série officielle : <em>First Season Documentary</em>, <em>EP.03 Red Smoke</em>, <em>EP.04 The Key</em>, <em>EP.05 RAT</em>, <em>EP.06 Dogtag</em>, <em>No Man’s Land</em>, <em>A Golden Opportunity</em>.</li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">Arena Breakout Wiki (Fandom)</span> — <a href="https://arena-breakout.fandom.com/wiki/Kamona" target="_blank" rel="noopener">arena-breakout.fandom.com</a></li>
            <li><span class="src-name">Grokipedia — Kamona</span> — alliances, commanders, structure des PMC et de l’Operation Blackout. <a href="https://grokipedia.com/page/Kamona" target="_blank" rel="noopener">grokipedia.com</a></li>
            <li><span class="src-name">NamuWiki — Arena Breakout / Boss</span> — fiches de boss : armes, armures, escortes, tokens, affiliation. <a href="https://en.namu.wiki/w/Arena%20Breakout/%EB%B3%B4%EC%8A%A4" target="_blank" rel="noopener">en.namu.wiki</a></li>
            <li><span class="src-name">Reddit r/ArenaBreakoutGlobal</span> — fil « Any good YouTube channels covering the Lore of Kamona ? » et son récapitulatif de factions (CDIS = Armée du Sud, MNST = Front du Nord, Blackgold = PMC de Colom implantée dans la Mine) : synthèse de joueur, non officielle.</li>
            <li><span class="src-name">senseos.gg</span> — registre des boss et de leurs apparitions. <a href="https://senseos.gg/guides/arena-breakout-infinite/bosses-list/" target="_blank" rel="noopener">senseos.gg</a></li>
          </ul>
          <h3>Théories (non confirmées)</h3>
          <ul class="src-list">
            <li>Corporation Toland, « l’Ark », projet Gungnir, projet Apostle, « Cleaners », figure « Arachne » : non confirmées par l’éditeur.</li>
            <li>La ventilation exacte des rôles entre MNST et CDIS sur la Valley et Northridge : issue d’un post Reddit sur les Archives n° 2, à recouper avec la source primaire.</li>
            <li>Le rattachement exact d’EDELWEISS (unité, corps ou personne) n’est pas explicité par les textes : traité ici comme un commandement militaire réactivé. <span class="src-tag src-theorie">Théorie</span></li>
          </ul>
        """
