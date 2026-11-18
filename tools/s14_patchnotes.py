# -*- coding: utf-8 -*-
"""S14 — Contenu de la page communaute-patch-notes.html."""

CONTENT = r"""
          <div class="evt-legend">
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">note de patch ou annonce publiée par MoreFun</span>
            <span class="src-tag src-communautaire">Communauté</span><span class="lg-txt">miroir, agrégateur ou base de données</span>
            <span class="src-tag src-rapporte">Rapporte</span><span class="lg-txt">chiffre reconstitué, non publié tel quel</span>
            <span class="evt-badge evt-live">En cours</span><span class="lg-txt">actif au 17 novembre 2026</span>
          </div>

          <div class="facts">
            <div class="fact"><span class="fact-label">Source primaire</span><span class="fact-value">Steam News — appid 2073620</span></div>
            <div class="fact"><span class="fact-label">Patch suivi</span><span class="fact-value">1.0.0.142.19 — base de données au 4 nov. 2026</span></div>
            <div class="fact"><span class="fact-label">Dernière mise à jour</span><span class="fact-value">Live Update du 10 novembre 2026, 03:00 UTC+0</span></div>
            <div class="fact"><span class="fact-label">Cadence</span><span class="fact-value">Live Updates de 2 à 3 fois par mois</span></div>
          </div>

          <figure class="page-figure">
            <img src="../img/communaute/patch-notes.jpg" alt="Poste de developpement avec grand ecran affichant une longue liste de notes de mise a jour structuree" loading="lazy">
            <figcaption>Les notes de patch sont la seule source de vérité d’Arena Breakout: Infinite. Tout le reste — bases de données, guides, vidéos — n’est qu’une lecture de ces notes.</figcaption>
          </figure>

          <h2 id="ou">1. Où lire les notes officielles</h2>
          <p>Il existe un ordre de priorité strict, et il n’est pas celui du référencement. <span class="src-tag src-officiel">Officiel</span></p>
          <ul class="link-list">
            <li><span class="lk-name">Steam News — appid 2073620<span class="lk-desc">La source primaire. Chaque note de patch, chaque annonce de saison, chaque rappel de programme communautaire. C’est ici que MoreFun publie ses liens d’invite Discord — la seule porte d’entrée fiable.</span></span><span class="lk-kind">Officiel</span></li>
            <li><span class="lk-name">Site officiel idcgames.com<span class="lk-desc">Reprend les annonces majeures en version lisible, et parfois en avance sur Steam.</span></span><span class="lk-kind">Officiel</span></li>
            <li><span class="lk-name">Discord officiel<span class="lk-desc">Annonces et discussion de patch. Utile pour les questions de casas, mais ce n’est pas la source de vérité.</span></span><span class="lk-kind">Officiel</span></li>
            <li><span class="lk-name">X — @ArenaBreakoutPC<span class="lk-desc">Format court : les points saillants, les giveaways, les dates de début et de fin.</span></span><span class="lk-kind">Officiel</span></li>
            <li><span class="lk-name">YouTube officiel<span class="lk-desc">Trailers de patch et dev talks. Excellente illustration, mais sans les chiffres détaillés.</span></span><span class="lk-kind">Officiel</span></li>
          </ul>

          <div class="callout callout-warning">
            <h4>Une note de patch n’est pas un patch</h4>
            <p>Un <em>Live Update</em> est publié à 03:00 UTC+0 et s’applique sans arrêt de serveur : si vous étiez en raid au moment où il tombe, l’instruction de MoreFun est de quitter le jeu et de cliquer sur <strong>Update</strong> dans le lanceur. Un <em>Update Announcement</em>, lui, accompagne une mise à jour de saison ou de festival. La distinction compte, parce que les correctifs d’un Live Update s’appliquent immédiatement et ne sont pas réapplicables au patch suivant. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="trackers">2. Les miroirs : pratiques pour suivre sans traquer</h2>
          <p>Les notes officielles sont publiées sur un fil qui s’enfonce. Les miroirs et agrégateurs servent à remonter le flux. <span class="src-tag src-communautaire">Communauté</span></p>

          <div class="tool-grid">
            <div class="tool-card">
              <h4>PatchBot</h4>
              <span class="tool-tag">Miroir Steam + Discord</span>
              <p>Le miroir le plus structuré : chaque Live Update est rejouée avec ses titres, ses listes de correctifs numérotées et un lien vers la discussion Steam d’origine. PatchBot tient aussi un canal Discord à jour sur les notes.</p>
              <div class="tool-foot">C’est le miroir le plus pratique pour l’archive : chaque note y reste adresseable par date et par article. <a href="https://patchbot.io/games/arena-breakout-infinite" target="_blank" rel="noopener">patchbot.io</a></div>
            </div>
            <div class="tool-card">
              <h4>GameDropDaily</h4>
              <span class="tool-tag">Fil d’actualités daté</span>
              <p>Un flux chronologique qui affiche le nombre de mises à jour officielles sur 90 jours, avec le statut « Steam · Official » sur chaque entrée. Utile pour mesurer la cadence réelle de l’éditeur.</p>
              <div class="tool-foot">Sur la période observée en octobre 2026, 19 mises à jour officielles en anglais sur 90 jours. <a href="https://gamedropdaily.com/updates/arena-breakout-infinite/" target="_blank" rel="noopener">gamedropdaily.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Changelog.gg</h4>
              <span class="tool-tag">Archive des annonces</span>
              <p>Archive d’un format proche de celui de Steam, avec un lien de discussion associé à chaque annonce. Pratique pour retrouver l’annonce précise d’un correctif sécurité.</p>
              <div class="tool-foot">Les annonces de bannissement y sont archivées avec leur contenu intégral. <a href="https://changelog.gg/games/arena-breakout-infinite-2073620/updates" target="_blank" rel="noopener">changelog.gg</a></div>
            </div>
            <div class="tool-card">
              <h4>ABI Guide / abibuilder</h4>
              <span class="tool-tag">Fusionné — lire la mention</span>
              <p>Le Mirror le plus populaire de notes de patch a cessé d’être maintenu : ses données sont périmées et le site a fusionné avec abibuilder.com. La redirection est visible sur la page elle-même.</p>
              <div class="tool-foot">C’est aujourd’hui la source la plus fréquente de chiffres périmés circulant sur Reddit et YouTube. <a href="https://abi-guide.dev/en/patchnotes" target="_blank" rel="noopener">abi-guide.dev</a></div>
            </div>
            <div class="tool-card">
              <h4>ABI Database — patch notes</h4>
              <span class="tool-tag">Versionné par patch</span>
              <p>La seule source qui associe un journal de modifications <strong>à la base de données</strong> : chaque entrée indique le patch correspondant, et chaque enregistrement de la base est daté. C’est la meilleure façon de vérifier si un chiffre a changé.</p>
              <div class="tool-foot">Patch suivi : 1.0.0.142.19, données mises à jour le 4 novembre 2026, avec un journal de modifications dédié. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Ghosting Squad</h4>
              <span class="tool-tag">Threads de la communauté</span>
              <p>Un forum communautaire qui relaie les annonces officielles du studio, y compris le Mentor Program, avec un fil de discussion associé. Utile pour lire les réactions de la communauté sous le texte de l’annonce.</p>
              <div class="tool-foot">Les commentaires des membres ne sont pas des faits officiels : c’est un forum, pas une source. <a href="https://ghostingsquad.com/threads/6258/" target="_blank" rel="noopener">ghostingsquad.com</a></div>
            </div>
          </div>

          <figure class="page-figure">
            <img src="../img/communaute/opensource-code.jpg" alt="Code source deroulant sur un large ecran incurve dans un bureau sombre, lignes colores illuminees" loading="lazy">
            <figcaption>Une base de données versionnée par patch est ce qui distingue une source fiable d’une collection de captures d’écran.</figcaption>
          </figure>

          <h2 id="s7">3. Ce que la mise à jour de Saison 7 a réellement changé</h2>
          <p>La mise à jour du 15 septembre 2026 est la plus lourde de la saison et celle qui a redessiné le plus de choses. Voici le résumé complet, parce que beaucoup de ces règles sont encore mal comprises. <span class="src-tag src-officiel">Officiel</span></p>

          <h3>Continuous Mastery : la maîtrise continue</h3>
          <ul>
            <li>Ajout de la maîtrise de combat <strong>Last Stand</strong> : elle réduit fortement le recul horizontal et la dispersion du tir quand les HP de tête, de torse ou globaux passent sous un seuil.</li>
            <li>Retrait de la maîtrise de survie <strong>Parkour</strong>.</li>
            <li>Déplacement de la maîtrise de combat <strong>Quick Seal</strong> dans la catégorie Survie.</li>
            <li>L’objectif affiché : ajouter des maîtrises « centrales » qui créent des choix réellement différenciés selon le style de jeu.</li>
          </ul>

          <h3>Supplies Drops 2.0 : le mode refait</h3>
          <ul>
            <li>La <strong>Caisse d’équipe</strong> et la <strong>Caisse personnelle</strong> s’étendent continuellement avec le niveau de l’équipe, ce qui augmente le maximum extractible.</li>
            <li>Nouvelle mécanique de terminal en raid : les terminaux normaux accumulent de l’XP de façon continue, les <strong>terminaux covert</strong> exigent de tenir et défendre la position contre les autres escouades. Une capture réussie donne un fort boost d’XP, avec un risque assumé.</li>
            <li>Ajout du <strong>Crafter de qualité violette</strong> pour objets divers.</li>
            <li>Plus de conteneurs en raid et des rendements augmentés ; réapparitions plus rapides en début de partie, puis durées qui s’allongent au fil de la progression ; airdrops déployés en grand nombre en milieu et fin de partie ; unités IA à armure lourde ; annonces de kill et diffusions vocales en raid.</li>
          </ul>

          <h3>Optimisations des contrôles</h3>
          <ul>
            <li><strong>Input buffering</strong> : il est maintenant possible d’enchaîner un sprint pendant un saut, ou d’appuyer sur Sprint en étant couché pour se relever.</li>
            <li>Ajout de l’<strong>inspection et de l’interaction des plaques d’identité</strong> — l’interaction varie selon le nombre de plaques dans le sac.</li>
            <li>Animations de chargement de munitions ajoutées pour certains pistolets et fusils à pompe.</li>
            <li>Se mettre à plat interrompt désormais les animations d’inspection.</li>
            <li>Posture d’inclinaison optimisée, et correction d’un abus d’inclinaison inverse qui permettait de masquer la zone de touche à la tête.</li>
          </ul>

          <h3>Équilibrage : les changements les plus visibles</h3>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Changement</th><th>Détail</th><th>Impact pratique</th></tr></thead>
              <tbody>
                <tr><td>Portée effective augmentée</td><td>Sur la plupart des armes</td><td>Les duels à distance se resserrent : le 30 % de dégâts perdus hors de portée effective compte davantage</td></tr>
                <tr><td><strong>Ricochet supprimé</strong></td><td>Retiré de tous les casques et masques</td><td>Un tir à la tête compte enfin. C’est le changement le plus structurant de la saison</td></tr>
                <tr><td>Durabilité des casques et masques de classe V et VI</td><td>Taux de perte augmenté</td><td>Ces casques encaissent davantage avant de céder</td></tr>
                <tr><td>Pénétration à faible probabilité contre les armures de classe V et VI</td><td>Supprimée pour les gilets balistiques et rigs blindés</td><td>Il faut ramener la durabilité sous un seuil avant de percer de façon fiable</td></tr>
                <tr><td>Lampe tactique</td><td>Intensité d’éclairage réduite, ergonomie ajustée à −7</td><td>Se déplacer éclairé coûte en mobilité</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout">
            <h4>Comment lire le changement de ricochet</h4>
            <p>Avant la S7, une balle pouvait ricocher sur un casque, et vous découvriez que votre tir n’avait pas porté. Le retirer signifie qu’une balle à la tête inflige des dégâts de zone même si la partie touchée est un casque. Combiné à la suppression de la pénétration à faible probabilité, cela change la hiérarchie : <strong>la précision compte plus qu’avant, et l’usure de l’armure compte plus qu’avant</strong>. Ce sont deux règles qui vont dans le même sens, pas des règles opposées, mais elles se cumulent. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h3>Trophy Room et recherche</h3>
          <ul>
            <li>Les formules sont <strong>au niveau maximum dès leur déverrouillage</strong> : plus besoin de les faire monter comme le Workbench.</li>
            <li>Les matériaux requis pour de nombreuses formules ont été réajustés à un niveau plus raisonnable, et davantage d’objets divers ont trouvé de nouveaux usages.</li>
            <li>Nouvel objet tactique craftable : la <strong>grenade étourdissante M290</strong>.</li>
            <li>Limite de niveau de la <strong>Collection Room</strong> augmentée de 2, et limite de stockage des objets rouges portée à <strong>999</strong>.</li>
            <li>Le point rouge marquant les nouvelles plaques d’identité est restreint à l’étagère de plaques : il n’est plus transféré à l’écran principal de la Trophy Room ni à l’entrée du lobby.</li>
            <li>Le volume de la musique de fond baisse automatiquement en multijoueur, pour mieux entendre les voix de l’escouade.</li>
          </ul>

          <h2 id="live">4. Le format des Live Updates</h2>
          <p>En dehors des mises à jour de saison, MoreFun publie des correctifs à chaud de 2 à 3 fois par mois. Deux exemples de la saison 7 donnent le format. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="tool-grid">
            <div class="tool-card">
              <h4>Live Update du 27 octobre 2026</h4>
              <span class="tool-tag">6 événements + 22 correctifs</span>
              <p>L’annonce Halloween et Warlord III, plus une longue liste de correctifs. Les points qui touchent le gameplay : <strong>réduction du Merit total requis</strong> pour monter de niveau en Zombie Endless ; <strong>facilitation de plusieurs missions « Enter Infected Zone »</strong> ; et changement de ingrédient de fabrication des munitions 5.8×42 mm DVP88, dont la recette Trophy Room passe de l’<strong>Antenne</strong> au <strong>Luxury Tea Set</strong>.</p>
              <div class="tool-foot">Corrige aussi un résultat de recherche « Free Upgrade » de qualité rouge qui produisait une mauvaise quantité de 7.62×54 mm LPS, plusieurs anomalies d’affichage de modèles (Klukai, Leva, Emerald Web M14) et des points d’accès anormaux sur Airport, Farm et TV Station.</div>
            </div>
            <div class="tool-card">
              <h4>Live Update du 10 novembre 2026</h4>
              <span class="tool-tag">Collaboration + enquête + 12 correctifs</span>
              <p>Le Live Update le plus dense depuis le lancement : la collaboration <strong>Dim Dou Duk</strong>, le lancement de <strong>Kamona Investigation</strong>, et douze correctifs. Les plus notables : le Market ne pouvait plus ouvrir la fenêtre d’extension de stockage pendant une mise en vente ; les grenades ne pouvaient pas être lancées dans certaines situations ; et dans le Warlord Tournament, les armes tiraient accidentellement lorsqu’on consultait les informations d’équipement, avec un panneau de classement affiché sur la mauvaise couche.</p>
              <div class="tool-foot">Corrige également l’arme de mêlée Cause and Effect (détachement à l’inspection, saccade au sprint, retard de la main gauche, clipping accroupi ou couché), un mauvais nombre d’IA sur certaines zones de Farm, et les positions hors limites sur Farm, Northridge et Airport.</div>
            </div>
          </div>

          <h2 id="securite">5. Les rapports de sécurité : le suivi que personne ne lit</h2>
          <p>Chaque saison, MoreFun publie un rapport de sécurité du <strong>B.D.C.</strong> (son équipe anti-triche) et un avis de bannissement bimensuel. C’est la documentation la plus sous-consultée du jeu, et c’est pourtant la meilleure source chiffrée sur le comportement réel de la communauté. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="stat-strip">
            <div class="stat-box"><div class="sb-val">624 239</div><div class="sb-key">bannissements pour triche (cumul)</div></div>
            <div class="stat-box"><div class="sb-val">176 884</div><div class="sb-key">dont bannis 10 ans</div></div>
            <div class="stat-box"><div class="sb-val">76 466</div><div class="sb-key">bannissements appareil / IP</div></div>
            <div class="stat-box"><div class="sb-val">114</div><div class="sb-key">avis de bannissement publiés</div></div>
          </div>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Période</th><th>Avis</th><th>Bannissements triche</th><th>Dont 10 ans</th><th>Part</th></tr></thead>
              <tbody>
                <tr><td>2024 (depuis août)</td><td>20</td><td>214 264</td><td>83 552</td><td>39 %</td></tr>
                <tr><td>2025</td><td>52</td><td>186 639</td><td>58 645</td><td>31 %</td></tr>
                <tr><td>2026 (jusqu’au 27 oct.)</td><td>42</td><td>223 336</td><td>34 687</td><td>16 %</td></tr>
                <tr><td><strong>Cumul</strong></td><td><strong>114</strong></td><td><strong>624 239</strong></td><td><strong>176 884</strong></td><td><strong>28 %</strong></td></tr>
              </tbody>
            </table>
          </div>
          <p>La tendance est nette : la part de bannissements à dix ans passe de 39 % en 2024 à 16 % en 2026, alors que le volume total reste stable. Autrement dit, <strong>l’anti-triche détecte mieux et sanctionne plus vite</strong> : ce qui reste est la frange la plus déterministe. <span class="src-tag src-rapporte">Rapporte</span></p>

          <h3>Les outils de détection</h3>
          <ul>
            <li><strong>ACE (Anti-Cheat Expert)</strong> — anti-triche au niveau kernel, installé avec le jeu, complété par des vérifications serveur.</li>
            <li><strong>DMA Guard</strong> — protection contre le triche matériel, opérationnelle depuis août 2026.</li>
            <li><strong>Compensation des victimes de triche</strong> — le mécanisme de remboursement des pertes dues aux tricheurs, élargi à chaque saison. Sur les deux semaines précédant le 11 octobre 2026, <strong>89 618 joueurs ont été indemnisés à hauteur de 116,91 milliards de Koen</strong>.</li>
            <li><strong>Sanction des complices</strong> — les joueurs qui profitent d’un tricheur dans leur escouade sont sanctionnés : les bannissements peuvent aller jusqu’à <strong>3 650 jours</strong>, et le Season 3 a déjà enregistré plus de 14 000 joueurs pénalisés pour ce motif.</li>
          </ul>

          <h3>Les rapports par saison</h3>
          <ul class="link-list">
            <li><span class="lk-name">Rapport anti-triche B.D.C. — Saison 3<span class="lk-desc">Plus de 1 650 améliorations technologiques, plus de 5 700 types de plug-ins et cheats neutralisés, plus de 53 000 violations sanctionnées dont 14 000 comptes à dix ans. C’est ce rapport qui annonce la création de l’Inspector Community pour la Saison 4.</span></span><span class="lk-kind">Janv. 2026</span></li>
            <li><span class="lk-name">Rapport de sécurité — Saison 4<span class="lk-desc">Chiffres de remboursement. 8 avril 2026.</span></span><span class="lk-kind">Avr. 2026</span></li>
            <li><span class="lk-name">Rapport de sécurité — Saison 5<span class="lk-desc">Chiffres de remboursement. 3 juillet 2026.</span></span><span class="lk-kind">Juil. 2026</span></li>
            <li><span class="lk-name">Rapport de sécurité — Saison 6<span class="lk-desc">Plus de 772 améliorations de l’anti-triche, plus de 45 000 cas de triche sanctionnés dont plus de 8 000 bannissements à dix ans, plus de 14 000 joueurs pénalisés pour avoir fait équipe avec un tricheur. 28 septembre 2026.</span></span><span class="lk-kind">Sept. 2026</span></li>
            <li><span class="lk-name">Avis de bannissement du 14 octobre 2026<span class="lk-desc">Couvrant la période du 28 septembre au 11 octobre : 10 848 bannissements pour triche, 3 706 bannissements à dix ans, 1 744 bannissements d’appareil ou d’IP, 6 505 confiscations de Koen.</span></span><span class="lk-kind">Oct. 2026</span></li>
            <li><span class="lk-name">Avis de bannissement du 27 octobre 2026<span class="lk-desc">6 048 bannissements pour triche, dont 2 267 à dix ans.</span></span><span class="lk-kind">Oct. 2026</span></li>
          </ul>

          <div class="callout callout-danger">
            <h4>Ce que les chiffres impliquent pour vous</h4>
            <p>Avec 624 239 bannissements cumulés et 176 884 comptes à dix ans, l’anti-triche n’est pas un obstacle contournable : c’est un motif de bannissement permanent. Et l’Inspector Community a fait ses preuves : 24 765 participants en Saison 5 ont examiné 1 617 674 cas et permis le bannissement de 1 401 tricheurs, dont 618 en Saison 6 avec 13 058 participants. <strong>un signalement abusif répété contre des joueurs honnêtes a des conséquences</strong> : les rollsbacks de rapports sont traités au cas par cas. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="lire">6. Méthode : lire une note de patch en dix minutes</h2>
          <ol class="steps">
            <li><strong>Commencez par les « Events »</strong>, pas par les correctifs. Ce qui change en premier, c’est ce qui est en jeu en ce moment — et c’est ce qui expire en premier.</li>
            <li><strong>Repérez les sections « Balance Adjustments » et « Other Adjustments »</strong> : ce sont les seules qui modifient votre prise de décision en raid.</li>
            <li><strong>Ignorez la catégorie « Fixes »</strong>, sauf si elle touche à un élément d’événement en cours. Les correctifs d’affichage de modèles n’ont aucun intérêt tactique.</li>
            <li><strong>Notez la date et le patch.</strong> Sans cela, vous ne pourrez plus trancher un débat quatre mois plus tard.</li>
            <li><strong>Comparez avec la base de données versionnée</strong> pour savoir si un chiffre a bougé : c’est le seul moyen fiable de détecter une modification passée sous silence dans un guide.</li>
            <li><strong>Contrôlez la section « Trophy Room » et les crafts</strong> : un changement d’ingrédient (comme l’Antenne devenu Luxury Tea Set le 27 octobre) casse silencieusement les plans de la communauté.</li>
            <li><strong>Finissez par les rapports de sécurité</strong>, si un avis de bannissement est paru : ils vous disent si l’état du jeu s’est dégradé et si une mise à jour d’anti-triche a été déployée.</li>
          </ol>

          <div class="callout callout-warning">
            <h4>Le piège du contresens</h4>
            <p>Un Live Update fixe un bug ou change un paramètre — il ne l’« announced » pas. Un guide qui écrit « la note de patch du 27 octobre mentionne… » parle d’une note de patch ; un guide qui écrit « la note du 27 octobre dit que… » parle d’une règle. La différence est capitale quand la règle est un multiplicateur de points ou un seuil. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <h2 id="historique">7. Chronologie des mises à jour de la Saison 7</h2>
          <ul class="update-list">
            <li><span class="up-date">15 sept. 2026</span><span class="up-body"><strong>Season 7 Update Announcement — Utopia</strong><p>La mise à jour de saison : Continuous Mastery, Supplies Drops 2.0, optimisation des contrôles, rééquilibrage majeur, Trophy Room, Collection Room. Lancement de la saison le 16 septembre.</p></span></li>
            <li><span class="up-date">17 sept. 2026</span><span class="up-body"><strong>Live Update du 17 septembre</strong><p>Premier correctif à chaud de la saison 7.</p></span></li>
            <li><span class="up-date">24 sept. 2026</span><span class="up-body"><strong>Live Update Announcement — Biohazard &amp; Bountiful Autumn Festival</strong><p>Le festival d’automne : douze pistes de récompenses, Lunar Soil Sample, Supplies Drops 2.0, série Biohazard.</p></span></li>
            <li><span class="up-date">2 sept. 2026</span><span class="up-body"><strong>UPDATE — 2 septembre</strong><p>Correctif de septembre, publié en amont du lancement de la saison.</p></span></li>
            <li><span class="up-date">15 oct. 2026</span><span class="up-body"><strong>Live Update du 15 octobre — collaboration Girls’ Frontline 2</strong><p>Lancement de la collaboration et précisions sur les dates de fin des fournitures de la collaboration.</p></span></li>
            <li><span class="up-date">14 oct. 2026</span><span class="up-body"><strong>Live Update du 14 octobre</strong><p>Correctif à chaud de mi-saison.</p></span></li>
            <li><span class="up-date">20 oct. 2026</span><span class="up-body"><strong>Résultats de l’Inspector Community — Saison 6</strong><p>Publication des résultats de la saison précédente et annonce d’une récompense hebdomadaire pour la Saison 7.</p></span></li>
            <li><span class="up-date">27 oct. 2026</span><span class="up-body"><strong>Live Update du 27 octobre — Halloween et Warlord III</strong><p>Six événements Halloween, le Troisième Warlord Tournament, la formule Smelter Trash to Treasure, et 22 correctifs dont la réduction du Merit requis en Zombie Endless et le changement d’ingrédient du DVP88.</p></span></li>
            <li><span class="up-date">10 nov. 2026</span><span class="up-body"><strong>Live Update du 10 novembre — Dim Dou Duk et Kamona Investigation</strong><p>Collaboration Gourmet Market, phase Tea Break Delights de l’enquête, et 12 correctifs dont le Market, les grenades et le Warlord Tournament.</p></span></li>
          </ul>

          <figure class="page-figure">
            <img src="../img/communaute/market-tracking.jpg" alt="Ecran de terminal de marche affichant des graphiques en chandeliers et courbes de prix, reflet dans les lunettes d un analyste" loading="lazy">
            <figcaption>Chaque Live Update déplace le marché : le prix des objets cités dans les notes change le jour même. C’est pourquoi les bases versionnées par patch valent de l’or.</figcaption>
          </figure>

          <h2 id="sources">8. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Season 7 Update Announcement</span> — 15 septembre 2026 : Continuous Mastery, Supplies Drops 2.0, contrôles, équilibrage, Trophy Room, Collection Room. <a href="https://patchbot.io/games/arena-breakout-infinite/articles/1423-season-7-update-announcement" target="_blank" rel="noopener">patchbot.io</a></li>
            <li><span class="src-name">Live Update du 27 octobre 2026</span> — Halloween, Warlord III, formule Smelter et 22 correctifs. <a href="https://patchbot.io/games/arena-breakout-infinite/articles/1935-oct-27-utc0-live-update" target="_blank" rel="noopener">patchbot.io</a></li>
            <li><span class="src-name">Live Update du 10 novembre 2026</span> — Dim Dou Duk, Kamona Investigation, 12 correctifs. <a href="https://patchbot.io/games/arena-breakout-infinite/articles/2145-nov-10-utc0-live-update" target="_blank" rel="noopener">patchbot.io</a></li>
            <li><span class="src-name">Steam News — appid 2073620</span> — flux complet des notes, annonces de saison et avis de bannissement. <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">B.D.C. Season 3 Anti-Cheat Report</span> — 1 650 améliorations, 5 700 plug-ins neutralisés, 53 000 violations, 14 000 comptes à dix ans, création de l’Inspector Community. <a href="https://x.com/ArenaBreakoutPC/status/2010019140753662367" target="_blank" rel="noopener">x.com/ArenaBreakoutPC</a></li>
            <li><span class="src-name">Inspector Community est arrivé</span> — plateforme de relecture et mode d’accès. <a href="https://x.com/ArenaBreakoutPC/status/2011800620999881152" target="_blank" rel="noopener">x.com/ArenaBreakoutPC</a></li>
            <li><span class="src-name">Protectors of Peace</span> — chiffres de participation des Inspectors. <a href="https://steamcommunity.com/games/2073620/announcements/detail/536631984572597235" target="_blank" rel="noopener">steamcommunity.com</a></li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">GameDropDaily</span> — flux chronologique daté, volumétrie des mises à jour sur 90 jours. <a href="https://gamedropdaily.com/updates/arena-breakout-infinite/" target="_blank" rel="noopener">gamedropdaily.com</a></li>
            <li><span class="src-name">Changelog.gg</span> — archive datée des annonces officielles. <a href="https://changelog.gg/games/arena-breakout-infinite-2073620/updates" target="_blank" rel="noopener">changelog.gg</a></li>
            <li><span class="src-name">ABI Database — journal de modifications</span> — version 1.0.0.142.19, données au 4 novembre 2026, chaque chiffre marqué vérifié ou non. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></li>
            <li><span class="src-name">senseos.gg — anti-triche et bannissements</span> — cumul annuel par période, notifications d’historique, DMA Guard et VoT-d / IOMMU. <a href="https://senseos.gg/guides/arena-breakout-infinite/anti-cheat-and-bans/" target="_blank" rel="noopener">senseos.gg</a></li>
            <li><span class="src-name">Ghosting Squad</span> — relais des annonces officielles et reactions de la communauté. <a href="https://ghostingsquad.com/threads/6258/" target="_blank" rel="noopener">ghostingsquad.com</a></li>
          </ul>
          <h3>Non confirmé</h3>
          <ul class="src-list">
            <li>Le <strong>cumul de 624 239 bannissements</strong> et la répartition par période sont un <strong>agrégat reconstitué</strong> par un guide communautaire à partir de 114 avis ; MoreFun ne publie pas de cumul global.</li>
            <li>La <strong>date de sortie du jeu</strong> (15 septembre 2025) et le classement Steam (n°69, pic à 37 327 joueurs sur 24 h) proviennent d’un agrégateur tiers, et non d’une publication du studio.</li>
            <li>Le <strong>seuil de 19 mises à jour sur 90 jours</strong> a été mesuré à une date donnée et varie selon la période observée.</li>
          </ul>
        """
