# -*- coding: utf-8 -*-
"""S13 — Contenu de la page events-warlord-tournament.html."""

CONTENT = r"""
          <div class="evt-legend">
            <span class="evt-badge evt-live">En cours</span><span class="lg-txt">événement actif au 17 novembre 2026</span>
            <span class="evt-badge evt-closed">Terminé</span><span class="lg-txt">date de fin dépassée</span>
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">notes de patch et annonces MoreFun</span>
            <span class="src-tag src-communautaire">Communauté</span><span class="lg-txt">tests de joueurs, guides recoupés</span>
            <span class="src-tag src-rapporte">Rapporte</span><span class="lg-txt">recoupement partiel, non confirmé</span>
          </div>

          <div class="facts">
            <div class="fact"><span class="fact-label">Tournoi</span><span class="fact-value">Troisième Warlord Tournament — 3e édition</span></div>
            <div class="fact"><span class="fact-label">Dates</span><span class="fact-value">29 octobre – 7 décembre 2026 (UTC+0)</span></div>
            <div class="fact"><span class="fact-label">Classement</span><span class="fact-value">Par valeur de loot, hors rang de saison</span></div>
            <div class="fact"><span class="fact-label">Nouveauté S7</span><span class="fact-value">Fichier chiffré multiplicateur, dog tags, Kill Leader</span></div>
          </div>

          <figure class="page-figure">
            <img src="../img/events/warlord-tournament.jpg" alt="Arene de tournoi tactique dans un hangar en beton, escouades en tenue sombre face a face sous eclairage de projecteurs" loading="lazy">
            <figcaption>Le Warlord Tournament est le mode le plus competitive d’Arena Breakout: Infinite : les loadouts de tous les joueurs sont visibles, et le score se fait sur la valeur du loot extrait — pas sur les kills.</figcaption>
          </figure>

          <h2 id="warlord">1. Le Troisième Warlord Tournament en bref</h2>
          <p>Le Warlord Tournament est ce qui ressemble le plus à une échelle compétitive dans Arena Breakout: Infinite. Chaque raid se déroule dans un petit salon à forte valeur, où personne ne peut cacher son équipement. La troisième édition s’est ouverte le <strong>29 octobre 2026</strong> et ferme le <strong>7 décembre 2026</strong>, soit environ 40 jours pour grimper — presque deux semaines de plus que les événements d’Halloween lancés le même jour. <span class="src-tag src-officiel">Officiel</span></p>
          <p>La formule de MoreFun tient en une ligne : <em>« Avec les loadouts révélés et chaque geste à découvert, le Troisième Warlord Tournament est de retour ! »</em> Les règles changent à chaque édition, ce qui rend obsolètes les guides des tours précédents. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Édition</th><th>Dates</th><th>Saison</th><th>Ce qui a changé</th></tr></thead>
              <tbody>
                <tr><td><strong>Premier Warlord</strong></td><td>17 avr. – 14 mai 2026</td><td>S5 — Distortion</td><td>Début : TV Station, salons de 5 équipes, classement par valeur de loot, loadouts visibles</td></tr>
                <tr><td><strong>Deuxième Warlord</strong></td><td>13 août – 13 sept. 2026</td><td>S6 — White Nights</td><td>Étoiles du rang d’équipe et du rang d’éliminations personnelles, plafond de 3 par raid, limite d’écart de rang</td></tr>
                <tr><td><strong>Troisième Warlord</strong></td><td><strong>29 oct. – 7 déc. 2026</strong></td><td><strong>S7 — Utopia</strong></td><td><strong>Multiplicateur du fichier chiffré, intel par dog tags, marque Kill Leader</strong></td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="ranks">2. Rangs et récompenses</h2>
          <p>Le tournoi a son propre classement, <strong>séparé du rang de saison</strong>. Un compte neuf démarre au rang <strong>Recruit IV</strong>. Chaque palier est subdivisé en sous-rangs numérotés, et on monte en gagnant des étoiles. Une fois le rang <strong>Warlord</strong> atteint, les étoiles continuent de compter : les deux dernières récompenses se trouvent à 15 et 30 étoiles. <span class="src-tag src-officiel">Officiel</span></p>

          <ul class="rank-track">
            <li><span class="rk-name">Rookie</span><span class="rk-reward">Tacti-Girl Charm Voucher ×5</span></li>
            <li><span class="rk-name">Ranger</span><span class="rk-reward">Skin Supply Coupon S7 ×10</span></li>
            <li><span class="rk-name">Commander</span><span class="rk-reward">Velocity Protocol Racing Suit</span></li>
            <li><span class="rk-name">Warlord</span><span class="rk-reward">Warlord III Badge</span></li>
            <li class="top"><span class="rk-name">Warlord 15★</span><span class="rk-reward">Warlord III Frame</span></li>
            <li class="top"><span class="rk-name">Warlord 30★</span><span class="rk-reward">Warlord III Background</span></li>
          </ul>

          <div class="callout callout-warning">
            <h4>Rookie ou Vanguard ?</h4>
            <p>Les notes de patch nomment le premier palier <strong>« Rookie »</strong>, mais le suivi client de la deuxième édition affichait <strong>« Reach Vanguard Rating »</strong> pour la même marche. Traitez-les comme la même première étape au-dessus de Recruit, et fiez-vous à votre client. La structure de la S6 était identique : Demon Hunter Charm Voucher ×5, S6 Skin Supply Coupon ×10, Tournament Combat Suit, titre S2 Warlord, cadre et fond Warlord II. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h3>La piste parallèle : Warlord Trial et Challenge Tokens</h3>
          <p>À côté du classement, il existe une seconde voie de récompenses. Les <strong>missions</strong> de tournoi rapportent des <strong>Warlord Challenge Tokens</strong>, que l’on dépense dans l’événement compagnon <strong>Warlord Trial</strong>. MoreFun y cite notamment un <strong>IND70 Tactical Helmet</strong> et le <strong>Limitless Gear Skin</strong>, obtenables <em>gratuitement</em>. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="callout callout-success">
            <h4>La piste la plus sûre du tournoi</h4>
            <p>Le casque IND70 est une récompense lighthouse depuis le premier tournoi, et les jetons de mission ne dépendent pas de finir premier. Une escouade qui n’atteindra jamais Warlord peut tout de même repartir avec du matériel, à condition qu’elle fasse les missions. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="scoring">3. Le scoring : cinq règles à connaître</h2>
          <p>C’est la partie où la plupart des guides se trompent, parce que les règles ont changé entre les éditions. <span class="src-tag src-officiel">Officiel</span></p>

          <ol class="steps">
            <li><strong>L’équipe est classée sur la valeur du loot.</strong> Les règles originales de la S5 disaient : <em>« une fois dans le raid, des points sont attribués sur la valeur totale du loot de chaque équipe. Les points et classements des quatre meilleures équipes sont affichés en temps réel »</em>. Le premier tournoi était un salon à 5 équipes sur TV Station.</li>
            <li><strong>C’est le pic qui compte, pas le total final.</strong> Depuis la deuxième édition, <em>« les points sont calculés sur la valeur de loot totale la plus élevée accumulée par l’équipe pendant le raid »</em>. Le post du festival d’été ajoute que <em>« la mort d’un coéquipier n’affectera pas le classement »</em>. Concrètement, perdre un membre tardivement n’efface pas la valeur déjà atteinte.</li>
            <li><strong>Le classement est réglé à la fin du raid, pas à l’extraction.</strong> C’est le piège classique : un joueur l’a expliqué sur Reddit — <em>« tu reçois les points après la fin du match, pas après avoir extrait. Si le gars reste à l’intérieur et loot encore, il te passe devant et tu récupères presque rien »</em>. Extraire tôt avec une petite avance ne verrouille pas la première place.</li>
            <li><strong>Les étoiles viennent de deux sources, plafonnées à 3.</strong> Depuis la S6, les étoiles d’un raid sont <em>« basées à la fois sur le rang d’équipe et le rang d’éliminations personnelles, le total des étoiles gagnées sur ces deux parties dans un même raid restant plafonné à 3 »</em>. Un joueur très elim sur une équipe moyenne marque quand même bien. Personne ne saute plus de 3 étoiles par raid.</li>
            <li><strong>Les coéquipiers doivent être de rangs proches.</strong> Depuis la S6, le matchmaking <em>« ne peut pas démarrer si l’écart de rang entre les membres de l’escouade dépasse 2 grands rangs »</em>. Un Warlord ne peut pas emmener un Recruit dans le même salon.</li>
          </ol>

          <div class="callout">
            <h4>Le tableau des points par placement</h4>
            <p>Des décompositions communautaires de la deuxième édition rapportent une répartition d’environ <strong>+3 / +1 / 0 / −1 / −1</strong> pour les places de 1 à 5, plus <strong>+2 / +1 / +1</strong> pour les trois meilleurs par éliminations. MoreFun n’a jamais publié cette grille : traitez-la comme un guide, pas comme une règle. Ce qui est officiel, c’est le plafond de 3 étoiles et le fait qu’une dernière place peut coûter des points. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <figure class="page-figure">
            <img src="../img/events/encrypted-file.jpg" alt="Mallette de donnees chiffrees noire et ouverte sur une table en beton, voyant rouge clignotant" loading="lazy">
            <figcaption>Le fichier chiffré : un bonus de points qui se déclenche et se signale à toute la carte. Le récupérer, c’est choisir d’être une cible.</figcaption>
          </figure>

          <h2 id="encrypted">4. Le fichier chiffré : le multiplicateur qui vous trahit</h2>
          <p>Première des trois nouveautés de l’édition 2026, et la plus importante : <em>« les équipes qui obtiennent et détiennent un fichier chiffré reçoivent un bonus de multiplicateur dynamique sur leurs points de base. Si un membre de l’escouade portant un fichier chiffré extrait avec succès, le bonus de multiplicateur reste actif. »</em> <span class="src-tag src-officiel">Officiel</span></p>
          <ul>
            <li><strong>Le taux.</strong> L’annonce de la S7 donne un chiffre : les fichiers chiffrés peuvent offrir un bonus de points de <strong>1,5×</strong>, destiné à permettre aux équipes en retard de revenir. Mais les notes en direct parlent de multiplicateur <em>« dynamique »</em> : la valeur exacte peut varier. Ne comptez pas sur 1,5× pile.</li>
            <li><strong>Le signalement.</strong> Les notes de la S7 sont explicites : <em>« une diffusion globale aura lieu quand un fichier chiffré est acquis, et les autres escouades peuvent le consulter dans le panneau de détails du raid »</em>. Le ramasser informe toute la carte.</li>
            <li><strong>La conservation.</strong> Le bonus reste actif après l’extraction du porteur. Vous n’avez donc pas à le garder en vie jusqu’à la fin du raid.</li>
            <li><strong>Le bon plan.</strong> Attraper le fichier et <strong>sortir son porteur rapidement</strong>. Tout le temps de survie du porteur est un temps pendant lequel toute la carte sait où vous êtes.</li>
          </ul>

          <div class="callout callout-danger">
            <h4>Le risque de données de la communauté</h4>
            <p>Un fil Reddit sur les fichiers chiffrés en Season 7 relève la frustration de leur <strong>visibilité</strong> : le bonus attire l’attention de toute la carte sur une escouade précise, ce qui transforme un avantage de points en cible. Le mécanisme est officiel — la diffusion globale — mais l’interprétation de sa rentabilité est un débat de communauté. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <h2 id="dogtags">5. Les dog tags : l’intel que vous ne payez pas</h2>
          <p>Deuxième nouveauté : <em>« quand vous inspectez ou ramassez un dog tag ennemi, tous les membres de votre escouade sont notifiés de la défaite de son propriétaire. Le panneau de détails du raid est également mis à jour avec cette information. »</em> <span class="src-tag src-officiel">Officiel</span></p>
          <p>Dans un salon à 5 équipes, savoir qu’une équipe rivale est réduite à un seul joueur suffit à décider d’une poussée. C’est une règle modeste, mais elle pèse surtout sur les escouades qui consultent le panneau de détails et parlent au micro.</p>

          <h2 id="entree">6. Les conditions d’entrée</h2>
          <p>Attention ici : MoreFun <strong>n’a pas imprimé de conditions d’entrée</strong> pour le troisième tournoi dans les notes du 27 octobre. Ce qui est documenté vient des éditions précédentes. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Élément</th><th>Valeur</th><th>Statut</th></tr></thead>
              <tbody>
                <tr><td>Équipement minimum</td><td>400 000 Koen de valeur de loadout</td><td><span class="evt-badge evt-closed">Édition 2026 (avr.)</span></td></tr>
                <tr><td>Ticket par raid</td><td>50 000 Koen</td><td><span class="evt-badge evt-closed">Édition 2026 (avr.)</span></td></tr>
                <tr><td>Rang de saison minimum</td><td>Ace V</td><td><span class="evt-badge evt-unconfirmed">Rapporté, 2e édition</span></td></tr>
                <tr><td>Valeur de stash totale</td><td>40 000 000 Koen</td><td><span class="evt-badge evt-unconfirmed">Rapporté, 2e édition</span></td></tr>
                <tr><td>Conditions exactes du 3e tournoi</td><td>À vérifier sur l’écran d’événement</td><td><span class="evt-badge evt-soon">Non publiées</span></td></tr>
              </tbody>
            </table>
          </div>
          <p>Les plafonds d’équipement par mode de la S7 (Normal : T4 et moins, Lockdown : T5 et moins) s’appliquent aux zones Tactiques Ops normales. Le Warlord Tournament est un mode événementiel séparé : vérifiez son propre écran d’entrée au lieu de supposer que ces plafonds s’appliquent. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="callout callout-danger">
            <h4>N’achetez pas votre entrée</h4>
            <p>Cherchez cet événement et la plupart des premiers résultats sont des vendeurs de Koen et des services de carry. Ne le faites pas. MoreFun a supprimé l’achat de Koen à la version 1.0 et applique une politique de tolérance zéro qui punit les acheteurs comme les vendeurs : confiscation du Koen, baisse du score de Merit, bannissements. Le rapport de bannissement de la fortnighte du 13 au 26 juillet 2026 listait à lui seul 2 133 confiscations de Koen et 1 217 bannissements de dix ans. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="monter">7. Comment monter plus vite</h2>
          <p>Ces conseils découlent directement des règles officielles. Rien ici ne repose sur des chiffres cachés. <span class="src-tag src-officiel">Officiel</span></p>
          <ol class="steps">
            <li><strong>Lisez l’écran des loadouts avant le raid.</strong> L’équipe de départ de chaque escouade est visible avant et pendant le raid (les noms des joueurs sont masqués). Choisissez vos cibles et vos itinéraires en fonction de l’équipe la moins blindée et de l’équipe la plus empilée.</li>
            <li><strong>La valeur par emplacement bat le volume.</strong> Vous êtes classé sur la valeur du loot : remplissez vos sacs d’objets chers, pas de remplissage bon marché.</li>
            <li><strong>Attrapez le fichier chiffré, puis sortez son porteur.</strong> Le bonus survit à l’extraction, et la diffusion globale fait du porteur une cible publique.</li>
            <li><strong>Ne sortez pas tôt avec une petite avance.</strong> Le classement est réglé à la fin du raid sur la valeur de pic. Si un rival est encore dedans et juste derrière, rester pour ajouter de la valeur ou se battre peut rapporter plus que partir.</li>
            <li><strong>Les kills comptent, mais jusqu’au plafond seulement.</strong> Un match à éliminations élevées sur une équipe médiocre rapporte des étoiles, mais aucun raid n’en donne plus de 3. Se battre au point de perdre la première place est rarement rentable.</li>
            <li><strong>Exploitez les dog tags.</strong> Ramassez ou inspectez chaque plaque que vous pouvez atteindre sans risque : votre escouade voit la mise à jour et le panneau de détails montre quelles équipes sont affaiblies.</li>
            <li><strong>Alignez les rangs de votre escouade.</strong> On ne peut pas démarrer avec plus de deux grands rangs d’écart : triez l’équipe avant la dernière semaine.</li>
            <li><strong>Faites les missions même en visant rien.</strong> Les Challenge Tokens achètent le casque IND70 quel que soit votre rang.</li>
          </ol>

          <h2 id="halloween">8. Mysterious Pumpkin Night — le volet Halloween</h2>
          <p>La saison Halloween 2026 s’appelle <strong>Mysterious Pumpkin Night</strong> dans les notes, et le volet citrouille s’appelle <strong>Pumpkin Evolution II</strong>. Elle a tourné du <strong>29 octobre à 05:00 UTC jusqu’au 26 novembre 2026</strong>, soit 28 jours — contre 21 jours pour l’édition 2025, qui s’était tenue du 24 octobre au 13 novembre 2025. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Sous-événement</th><th>Dates</th><th>Objectif</th><th>Récompense clé</th></tr></thead>
              <tbody>
                <tr><td><strong>Pumpkin Evolution II</strong></td><td>29 oct. – 25 nov.</td><td>Entrer une Festive Pumpkin en raid et en extraire</td><td>Citrouilles évoluées, jusqu’à 880 000 Koen</td></tr>
                <tr><td><strong>Mysterious Night Adventure</strong></td><td>29 oct. – 25 nov.</td><td>Missions → Mysterious Points</td><td>Miraculous Festive Pumpkin, skins Night of Fear</td></tr>
                <tr><td><strong>Mysterious Night: Check In</strong></td><td>29 oct. – 25 nov.</td><td>Connexion sur 7 jours</td><td>Sleepless Night AK-12, Stormy Night SG550</td></tr>
                <tr><td><strong>Pumpkin Messenger Sighted</strong></td><td>29 oct. – 25 nov.</td><td>Tuer les Pumpkin Messengers</td><td>Autumn Pumpkin Helmet, citrouilles de tout stade</td></tr>
                <tr><td><strong>Corrupted Treasures</strong></td><td>29 oct. – 25 nov.</td><td>Coffres / fabrication en Trophy Room</td><td>Fading Dawn, Corrupted Clock</td></tr>
              </tbody>
            </table>
          </div>

          <figure class="page-figure">
            <img src="../img/events/pumpkin-halloween.jpg" alt="Citrouilles sculptes illuminees dans un depot ferroviaire nocturne humide, reflets orange sur les flaques" loading="lazy">
            <figcaption>Les Pumpkin Messengers apparaissent sur toutes les cartes pendant l’événement. Tuer l’un d’eux donne un casque et peut livrer une citrouille déjà évoluée.</figcaption>
          </figure>

          <h2 id="pumpkin">9. L’évolution des citrouilles : le mode d’emploi complet</h2>
          <p>Les règles 2026 sont volontairement courtes : <em>« apportez une Festive Pumpkin dans un raid, explorez, et extrayez avec succès pour avoir une chance de la faire évoluer. La Festive Pumpkin évoluée aura une apparence différente et vaudra significativement plus ! »</em> Les règles 2025 comblent les trous, et il faut le signaler : MoreFun n’a pas encore publié la page d’événement complète 2026. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Règle</th><th>Valeur</th><th>Statut</th></tr></thead>
              <tbody>
                <tr><td>Achat de citrouilles non mûres</td><td>100 Koen l’unité, limite de 2 achats par jour</td><td><span class="evt-badge evt-live">Officiel 2026</span></td></tr>
                <tr><td>Taille en inventaire</td><td>2×2, ne peut pas entrer dans le Secure Case</td><td><span class="evt-badge evt-live">Officiel 2026</span></td></tr>
                <tr><td>Calcul de l’EXP</td><td>2 EXP pour 10 000 Koen de valeur de loot extraite</td><td><span class="evt-badge evt-live">Officiel 2026</span></td></tr>
                <tr><td>Zones concernées</td><td>Lockdown et Forbidden</td><td><span class="evt-badge evt-closed">Règle 2025</span></td></tr>
                <tr><td>Étapes</td><td>Unripe → Ripe → Carved → Miraculous (niveau 4)</td><td><span class="evt-badge evt-closed">Noms 2025, échelle 2026 inchangée</span></td></tr>
                <tr><td>Valeur finale</td><td>880 000 Koen pour une citrouille pleinement évoluée</td><td><span class="evt-badge evt-live">Officiel 2026</span></td></tr>
                <tr><td>Non évoluée</td><td>Convertie en Koen à l’extraction</td><td><span class="evt-badge evt-live">Officiel 2026</span></td></tr>
                <tr><td>Miraculous non expirant</td><td>Stockable ou vendable 250 000 Koen aux contacts</td><td><span class="evt-badge evt-closed">Règle 2025</span></td></tr>
                <tr><td>Déblocage de l’écran</td><td>Niveau de personnage 13</td><td><span class="evt-badge evt-closed">Règle 2025</span></td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout">
            <h4>La règle du 2026 qui change tout</h4>
            <p>En 2025, les citrouilles évoluaient dans les raids Lockdown et Forbidden. Les notes 2026 introduisent un calcul d’EXP explicite : <strong>2 EXP pour 10 000 Koen de valeur de loot extraite</strong>. Et les citrouilles des ennemis morts comptent dans ce calcul : <em>« vous pouvez aussi ramasser les citrouilles des opérateurs ennemis et extraire avec elles. Leur valeur compte dans votre valeur totale de loot extraite et contribue à votre calcul d’EXP »</em>. Concrètement : un raid de farmage discipliné vaut mieux qu’un raid de combat risqué, parce que c’est la <strong>valeur extraite</strong> qui fait monter la citrouille, pas le nombre de kills. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h3>Est-ce que l’évolution vaut le coup ?</h3>
          <p>Oui si vous extrayez régulièrement. Non si vous êtes en série de morts. Une citrouille perdue est une citrouille perdue, et une citrouille restée à un stade intermédiaire n’a plus aucune valeur à la fin de l’événement. <span class="src-tag src-officiel">Officiel</span></p>
          <ul>
            <li><strong>Jouez la carte où vous extraisez le plus souvent.</strong> Pour beaucoup de joueurs, c’est Farm en Lockdown.</li>
            <li><strong>Ne mettez pas toutes vos citrouilles dans un seul raid.</strong> Répartissez-les sur plusieurs sorties : une seule mort ne doit pas réinitialiser toute votre série.</li>
            <li><strong>Commencez tôt.</strong> Chaque évolution demande une extraction réussie : démarrer le 29 octobre offrait le plus grand nombre de tentatives avant la date limite.</li>
            <li><strong>Ramassez les citrouilles ennemies.</strong> Elles comptent dans l’EXP et peuvent vous faire sauter une étape.</li>
            <li><strong>Terminez vos évolutions avant le 25/26 novembre.</strong> En 2025, seules les citrouilles Miraculous étaient conservées ; les stades intermédiaires « expiraient et étaient récupérés » à la fin de l’événement. La règle 2026 n’est pas confirmée : traitez-la comme active par prudence.</li>
          </ul>

          <h2 id="messengers">10. Les Pumpkin Messengers</h2>
          <p>Les Pumpkin Messengers ne faisaient pas partie de l’annonce 2025. Selon les notes, ils <em>« apparaîtront sur toutes les cartes pour une durée limitée »</em> pendant l’événement. Tuez-en un et vous obtenez un <strong>Autumn Pumpkin Helmet</strong>. Fouillez leur sac à dos pour <em>« avoir une chance de trouver une Festive Pumpkin de n’importe quel stade ou d’autres objets de valeur »</em>. <span class="src-tag src-officiel">Officiel</span></p>
          <p>Ce dernier point compte : un Messenger peut livrer une citrouille <strong>déjà évoluée</strong>, ce qui permet de sauter une partie de la série d’extractions — à condition de sortir avec. MoreFun n’a publié ni les points d’apparition, ni les horaires, ni les points de vie : traitez-les comme une cible temporaire à forte valeur. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="corrupted">11. Corrupted Treasures</h2>
          <p>Cet événement ajoute deux collectibles à durée limitée :</p>
          <ul>
            <li><strong>Fading Dawn</strong> — <em>« Cherchez dans les coffres de n’importe quelle carte pendant l’événement pour avoir une chance de le trouver. »</em> Rôle de caisse : c’est un jeton sûr, donc les itinéraires riches en coffres sont le moyen efficace de l’obtenir.</li>
            <li><strong>Corrupted Clock</strong> — <em>« Fabriquez-le dans la Trophy Room en utilisant des objets divers corrompus. Ces objets se trouvent sur toutes les cartes. »</em> C’est un projet de fabrication : ramassez les objets divers corrompus pendant l’événement et rapportez-les à la Trophy Room.</li>
          </ul>
          <p>MoreFun n’a pas indiqué si l’un ou l’autre survit au 25 novembre. Ne considérez pas un objet corrompu comme sûr à conserver au-delà de la date de fin tant que la page d’événement officielle ne l’a pas confirmé. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="gourmet">12. Dim Dou Duk Gourmet Market</h2>
          <p>Arrivé avec la mise à jour en direct du <strong>10 novembre 2026</strong> (en vigueur à 03:00 UTC+0), l’événement <strong>Dim Dou Duk Collaboration: Gourmet Market</strong> court du <strong>9 novembre au 6 décembre 2026</strong>. Dim Dou Duk est une véritable enseigne cantonaise de dim sum : l’événement ajoute deux objets au loot pool de toutes les cartes. <span class="src-tag src-officiel">Officiel</span></p>
          <p>La citation des notes est précise : <em>« pendant l’événement, vous pouvez trouver les Dim Dou Duk Shrimp Dumplings, l’aliment de la collaboration, et les Dim Sum Vouchers, l’objet d’événement, dans des conteneurs tels que sacs de sport et valises, sur toutes les cartes. Collectez assez de Dim Sum Vouchers pour échanger des récompenses sur l’écran d’événement. »</em> <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Élément</th><th>Valeur</th></tr></thead>
              <tbody>
                <tr><td>Nom de l’événement</td><td>Dim Dou Duk Collaboration: Gourmet Market</td></tr>
                <tr><td>Dates</td><td>9 nov. – 6 déc. 2026 (UTC+0), 28 jours — soit environ 27 jours jouables en pratique</td></tr>
                <tr><td>Objet d’événement</td><td>Dim Sum Voucher</td></tr>
                <tr><td>Aliment de collaboration</td><td>Dim Dou Duk Shrimp Dumplings</td></tr>
                <tr><td>Où ils droppent</td><td>Conteneurs « tels que sacs de sport et valises », toutes les cartes</td></tr>
                <tr><td>Où on les dépense</td><td>Écran d’événement, hors raid</td></tr>
                <tr><td>Taux de drop</td><td>Non publié</td></tr>
                <tr><td>Prix des récompenses</td><td>Non publiés dans les notes</td></tr>
              </tbody>
            </table>
          </div>

          <figure class="page-figure">
            <img src="../img/events/dim-sum-market.jpg" alt="Paniers de dim sum fumants sur un etal de rue dans un port asiatique, lanternes allumees et vapeur dans la lumiere" loading="lazy">
            <figcaption>Le Gourmet Market est entièrement cosmétique. Aucun objet de raid, aucune arme, aucune munition : tout se paie en vouchers collectés dans les sacs de sport et les valises.</figcaption>
          </figure>

          <h3>Ce qu’on achète avec les vouchers</h3>
          <ul>
            <li><strong>Dim Dou Duk Gear Skin</strong> — skin d’équipement, la récompense principale.</li>
            <li><strong>Dim Dou Duk Smoke Grenade</strong> — skin de grenade fumée.</li>
            <li><strong>Dim Dou Duk Badge</strong> — badge de profil.</li>
            <li><strong>Char Siu Spray</strong> — spray de la collaboration (le char siu est du porc grillé cantonais).</li>
            <li><strong>Tacti-Girl Charm Vouchers</strong> — également distribués par Halloween et le Warlord Tournament.</li>
            <li><strong>Season 7 Skin Supply Coupons</strong> — coupons de tirages de la saison 7.</li>
          </ul>
          <p>Deux points d’attention : toutes ces récompenses sont <strong>esthétiques ou de la monnaie de tirage</strong> — aucune raison de combat ne justifie une course. Et les <strong>coupons de tirages expirent avec la saison</strong> : les notes de la S6 indiquaient que les coupons S5 ne pouvaient pas être utilisés dans la nouvelle saison. Depensez ceux de la S7 avant la fin de la saison. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="callout callout-warning">
            <h4>Le piège du confit</h4>
            <p>Le Dim Sum Voucher est la monnaie. Les Shrimp Dumplings sont un objet de raid distinct, et c’est aussi l’un des quatre objets de l’enquête Kamona. <strong>Manger un ravioli en raid le retire de la remise.</strong> Portez-les jusqu’à l’enquête, pas jusqu’à votre barre de faim. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="investigation">13. Kamona Investigation — Tea Break Delights</h2>
          <p>Kamona Investigation est l’événement de remise récurrent d’Arena Breakout: Infinite. Chaque phase nomme une liste d’objets à collecting puis à rendre. La phase en cours est <strong>Tea Break Delights</strong>, et elle court du <strong>9 au 22 novembre 2026</strong> — quatorze jours, soit la moitié de la durée du Gourmet Market. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Objet à rendre</th><th>Nature</th></tr></thead>
              <tbody>
                <tr><td><strong>Lait</strong></td><td>Nourriture de raid standard</td></tr>
                <tr><td><strong>Miel</strong></td><td>Nourriture de raid standard</td></tr>
                <tr><td><strong>Pellicule</strong></td><td>Loot de valeur plus élevée, présent aussi dans les trocs de contacts</td></tr>
                <tr><td><strong>Dim Dou Duk Shrimp Dumplings</strong></td><td>Le nouvel aliment de la collaboration, dans les mêmes conteneurs que les vouchers</td></tr>
              </tbody>
            </table>
          </div>
          <p>Les notes ne donnent pas le nombre d’exemplaires à rendre pour chaque objet : l’écran d’événement l’affiche. <span class="src-tag src-officiel">Officiel</span></p>

          <h3>Les récompenses de l’enquête</h3>
          <ul>
            <li>Double-N Lute — Rain of Gold Gift Box</li>
            <li>Emerald Jade Flute — Shining Gold Gift Box</li>
            <li>Stroke of Luck Gift Box I</li>
            <li>Lucky Break Gift Box I</li>
            <li>Tacti-Girl Charm Vouchers</li>
            <li>Season 7 Skin Supply Coupons</li>
          </ul>

          <figure class="page-figure">
            <img src="../img/events/investigation-drawers.jpg" alt="Enqueteur ouvrant un tiroir de bureau poussiereux dans un batiment administratif abandonne, lumiere blanche traversant la brume" loading="lazy">
            <figcaption>La seconde couche de l’événement, <em>Investigate Drawers</em> : les tiroirs de toutes les cartes offrent une chance supplémentaire d’obtenir les objets exclusifs de la phase.</figcaption>
          </figure>

          <h3>Investigate Drawers, la seconde couche</h3>
          <p>Elle a deux niveaux :</p>
          <ul>
            <li><strong>Des missions de défi</strong> qui paient en <strong>Koen</strong>, en vouchers de charme Tacti-Girl et en coupons de skins S7.</li>
            <li><strong>Des tiroirs sur toutes les cartes</strong> qui offrent <em>« une chance supplémentaire d’obtenir des objets spéciaux exclusifs à cette phase de la Kamona Investigation »</em>.</li>
          </ul>
          <p>Autrement dit : les sacs de sport et les valises sont confirmés pour les vouchers et les raviolis, les tiroirs sont confirmés pour les objets exclusifs de l’enquête. Un itinéraire qui ouvre les trois couvre les deux événements d’un coup. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="callout callout-danger">
            <h4>Ne vendez pas votre pellicule</h4>
            <p>La tentation de vendre la pellicule sur le marché est réelle, mais l’enquête ferme le <strong>22 novembre</strong>. Gardez d’abord de quoi remplir la remise, vendez le reste ensuite. C’est le seul élément des quatre qui ait une valeur marchande significative. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="stack">14. Empiler les événements : la feuille de route</h2>
          <p>Tous ces événements se chevauchent, et leurs charges se cumulent sur les mêmes sorties. Le tableau ci-dessous est la synthèse opérationnelle de toute la page. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Événement</th><th>Fin (UTC+0)</th><th>Restant au 17 nov.</th><th>Compatible avec le farming Dim Sum ?</th></tr></thead>
              <tbody>
                <tr><td>Trash to Treasure (Smelter)</td><td>15 nov.</td><td>Clos</td><td>Oui — même formule PDA + câble + portable</td></tr>
                <tr><td>Kamona Investigation — Tea Break Delights</td><td>22 nov.</td><td><strong>5 jours</strong></td><td>Oui — mêmes conteneurs + tiroirs</td></tr>
                <tr><td>Halloween — Mysterious Pumpkin Night</td><td>25 nov.</td><td><strong>8 jours</strong></td><td>Oui — les Pumpkin Messengers apparaissent partout</td></tr>
                <tr><td>Dim Dou Duk — Gourmet Market</td><td>6 déc.</td><td>19 jours</td><td>Référence</td></tr>
                <tr><td>Troisième Warlord Tournament</td><td>7 déc.</td><td>20 jours</td><td>Mode séparé</td></tr>
              </tbody>
            </table>
          </div>

          <ol class="steps">
            <li><strong>Allez où sont les conteneurs civils.</strong> Sacs de sport, valises et tiroirs se trouvent dans les maisons, les bureaux, les chambres et les terminaux — pas dans les caisses militaires. À Farm, visez les bâtiments résidentiels plutôt que les champs ; à Airport, les intérieurs de terminal et de bureaux ; à Valley, Northridge, Armory et TV Station, les blocs de bureaux et d’habitations plutôt que les espaces ouverts.</li>
            <li><strong>Emportez un kit bon marché.</strong> Toutes les récompenses sont cosmétiques : risquer votre meilleur équipement pour un voucher n’a aucun sens. Un kit bon marché en zone Normal permet d’ouvrir beaucoup de conteneurs sans protection.</li>
            <li><strong>Gardez de la place dans le sac pour la nourriture.</strong> Les raviolis, le lait et le miel comptent pour l’enquête. Remontez-les hors raid, ne les mangez pas.</li>
            <li><strong>Empilez les autres événements sur les mêmes sorties.</strong> Le tableau ci-dessus montre exactement ce qui se cumule.</li>
            <li><strong>Priorisez par date limite.</strong> Trash to Treasure ferme en premier, puis l’enquête, puis Halloween. Les vouchers ont la fenêtre la plus longue : ne laissez pas le farming de vouchers ne doit pas écraser les remises qui ferment plus tôt.</li>
          </ol>

          <div class="callout callout-warning">
            <h4>Est-ce que ça vaut le coup de farm pour des Koen ?</h4>
            <p>Seulement avec un kit bon marché. Les missions de tiroirs de l’enquête paient en Koen, mais le Gourmet Market lui-même ne paie qu’en cosmétiques et coupons. Les Koen ne sont pas achetables contre de l’argent réel et MoreFun bannit les acheteurs comme les vendeurs : les récompenses viennent du jeu, il n’y a aucun raccourci sûr. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="sources">15. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Live Update du 27 octobre 2026 (UTC+0)</span> — annonce de la saison Halloween, du Troisième Warlord Tournament, des règles du fichier chiffré, des dog tags et du marqueur Kill Leader. <a href="https://x.com/ArenaBreakoutPC/status/2115421734728044892" target="_blank" rel="noopener">x.com/ArenaBreakoutPC</a></li>
            <li><span class="src-name">Live Update du 10 novembre 2026 (UTC+0)</span> — collaboration Dim Dou Duk, lancement de Kamona Investigation, 12 correctifs. <a href="https://patchbot.io/games/arena-breakout-infinite/articles/2145-nov-10-utc0-live-update" target="_blank" rel="noopener">patchbot.io</a></li>
            <li><span class="src-name">Notes de la Saison 7 — Utopia</span> — 15 septembre 2026 : fichier chiffré à 1,5×, diffusion globale, Red Drops. <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">Annonce Halloween 2025</span> — officielle Steam : première édition de Mysterious Pumpkin Night, règles d’évolution, achat à 100 Koen, expiration des stades intermédiaires. <a href="https://store.steampowered.com/news/app/2073620/view/509595167628462478" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">Live Update du 4 novembre 2025</span> — confirmation qu’une citrouille Miraculous n’expire pas et se vend 250 000 Koen aux contacts.</li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">timesaver.gg — Warlord Tournament (Season 7)</span> — historique des trois éditions, tableau des récompenses, règles de scoring, changement du multiplicateur et des dog tags. <a href="https://timesaver.gg/blog/arena-breakout-infinite-warlord-tournament" target="_blank" rel="noopener">timesaver.gg</a></li>
            <li><span class="src-name">timesaver.gg — Halloween Event 2026</span> — détail des six sous-événements, règles d’évolution, formule du Smelter. <a href="https://timesaver.gg/blog/arena-breakout-infinite-halloween-event" target="_blank" rel="noopener">timesaver.gg</a></li>
            <li><span class="src-name">timesaver.gg — Dim Sum Vouchers</span> — objets de l’enquête, lieu de drop des vouchers,Récompenses du Gourmet Market. <a href="https://timesaver.gg/blog/arena-breakout-infinite-dim-sum-vouchers" target="_blank" rel="noopener">timesaver.gg</a></li>
            <li><span class="src-name">r/ArenaBreakoutInfinite</span> — fil sur le règlement du classement à la fin du raid, files sur la visibilité du fichier chiffré, signalements « 5 raids havent found a single one » sur les vouchers. <a href="https://www.reddit.com/r/ArenaBreakoutInfinite/comments/1q90xzt/encrypted_files_are_just_really_lame/" target="_blank" rel="noopener">reddit.com</a></li>
          </ul>
          <h3>Non confirmé</h3>
          <ul class="src-list">
            <li>Le tableau de points par placement (<strong>+3 / +1 / 0 / −1 / −1</strong>) est une reconstruction communautaire de la deuxième édition ; MoreFun ne l’a jamais publié.</li>
            <li>Les conditions d’entrée <strong>Ace V</strong> et <strong>40 000 000 Koen de stash</strong> sont rapportées par des guides communautaires pour la deuxième édition, sans post Steam officiel. Vérifiez l’écran d’événement.</li>
            <li>Les <strong>points d’apparition, la vie et les horaires des Pumpkin Messengers</strong> ne sont pas publiés.</li>
            <li>La <strong>règle d’expiration 2026</strong> des citrouilles non évoluées et la <strong>survie de la pile de Dim Sum Vouchers</strong> à la fin de l’événement ne sont pas confirmées : les coupons de tirages expirent, mais rien n’est dit des currencies d’événement au-delà de la fermeture de l’écran.</li>
          </ul>
        """
