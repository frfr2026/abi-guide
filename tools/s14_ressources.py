# -*- coding: utf-8 -*-
"""S14 — Contenu de la page communaute-ressources.html."""

CONTENT = r"""
          <div class="evt-legend">
            <span class="src-tag src-officiel">Officiel</span><span class="lg-txt">liens publiés par MoreFun lui-même</span>
            <span class="src-tag src-communautaire">Communauté</span><span class="lg-txt">outils, wikis et guides communautaires</span>
            <span class="src-tag src-rapporte">Rapporte</span><span class="lg-txt">signalé par des joueurs, non vérifié</span>
            <span class="evt-badge evt-unconfirmed">À surveiller</span><span class="lg-txt">ressource qui peut bouger ou disparaître</span>
          </div>

          <div class="facts">
            <div class="fact"><span class="fact-label">Serveur Discord officiel</span><span class="fact-value">discord.gg/arenabreakoutinfinite</span></div>
            <div class="fact"><span class="fact-label">Serveur communautaire</span><span class="fact-value">discord.gg/AqtPAx5Xsn — programme Mentor</span></div>
            <div class="fact"><span class="fact-label">Subreddit</span><span class="fact-value">r/ArenaBreakoutInfinite — 8 règles de subreddit</span></div>
            <div class="fact"><span class="fact-label">Base de données</span><span class="fact-value">2 647 entrées — patch 1.0.0.142.19</span></div>
          </div>

          <figure class="page-figure">
            <img src="../img/communaute/discord-voice.jpg" alt="Joueur avec un casque speaking dans un micro face a son ecran dans une chambre sombre, lumiere de l ecran" loading="lazy">
            <figcaption>Le Discord est le point de rencontre le plus dense : équipes LFG, discussion de patch, signalements de bugs et programmes communautaires officiels.</figcaption>
          </figure>

          <h2 id="reperes">1. La règle d’or : ne jamais suivre un lien trouvé par un moteur de recherche</h2>
          <p>La quasi-totalité des problèmes de la communauté ABI ne viennent pas du jeu, mais d’un faux lien. Les serveurs Discord « officiels » clonés, les pages de codes de giveaway, les sites de Koen à bas prix : ce sont des vecteurs de phishing à ciel ouvert, et le jeu y est directement exposé. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="callout callout-danger">
            <h4>La seule méthode fiable</h4>
            <p>MoreFun publie ses liens d’invite Discord <strong>dans ses propres annonces Steam</strong>. C’est le seul point d’entrée de confiance. Un lien trouvé sur un moteur de recherche, dans un commentaire YouTube ou dans une bannière de serveur tiers doit être considéré comme non fiable, quelle que soit sa apparence. <span class="src-tag src-officiel">Officiel</span></p>
          </div>
          <ul>
            <li><strong>Discord officiel</strong> — <a href="https://discord.gg/arenabreakoutinfinite" target="_blank" rel="noopener">discord.gg/arenabreakoutinfinite</a> : annonces, discussion de patch, recherche d’équipe, rapports de bugs.</li>
            <li><strong>Discord communautaire (programme Mentor)</strong> — <a href="https://discord.gg/AqtPAx5Xsn" target="_blank" rel="noopener">discord.gg/AqtPAx5Xsn</a> : c’est là que s’ouvrent les tickets de mentorat.</li>
            <li><strong>Steam News</strong> — <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com/news/app/2073620</a> : chaque note de patch et chaque annonce de saison.</li>
            <li><strong>X / Twitter</strong> — <a href="https://x.com/ArenaBreakoutPC" target="_blank" rel="noopener">@ArenaBreakoutPC</a> : les giveaways y sont annoncés.</li>
            <li><strong>YouTube</strong> — <a href="https://www.youtube.com/@ArenaBreakoutInfinite" target="_blank" rel="noopener">@ArenaBreakoutInfinite</a> : trailers et dev talks.</li>
            <li><strong>Reddit</strong> — <a href="https://www.reddit.com/r/ArenaBreakoutInfinite/" target="_blank" rel="noopener">r/ArenaBreakoutInfinite</a> : modération non officielle, mais les posts officiels y apparaissent.</li>
          </ul>

          <h2 id="discord">2. Le Discord, et les serveurs par région</h2>
          <p>Le Discord officiel est multilingue et se dédouble en serveurs régionaux gérés par la communauté. Ce n’est pas une obligation, mais c’est là que se font les groupes LFG durables et que se trouve l’aide en direct quand une mécanique vient de changer. <span class="src-tag src-communautaire">Communauté</span></p>

          <ul class="link-list">
            <li><span class="lk-name">Arena Breakout: Infinite — serveur officiel<span class="lk-desc">Annonces de l’éditeur, discussion de patch, channels LFG, rapports de bugs. Le seul lien de confiance.</span></span><span class="lk-kind">Officiel</span></li>
            <li><span class="lk-name">Serveur communautaire / Mentor Program<span class="lk-desc">Hébergement des tickets de mentorat. Les mentors répondent quand ils sont libres : ce n’est pas une file d’attente en direct.</span></span><span class="lk-kind">Officiel</span></li>
            <li><span class="lk-name">Arena Breakout Community<span class="lk-desc">Serveur LFG généraliste, Community Hub, gameplay tactique de haut niveau, files d’attente de 8 secondes.</span></span><span class="lk-kind">Communautaire</span></li>
            <li><span class="lk-name">Serveurs régionaux FR / PL / PT / HU<span class="lk-desc">Communautés francophones, polonaises, portugaises et hongroises : recherche de coéquipiers dans la langue locale, conseils et retours de patch.</span></span><span class="lk-kind">Communautaire</span></li>
            <li><span class="lk-name">Comunidad Arena Breakout Infinite (ES / LATAM)<span class="lk-desc">Espagnol et Amérique latine : formation d’équipes, partage de stratégies, discussion des mises à jour.</span></span><span class="lk-kind">Communautaire</span></li>
            <li><span class="lk-name">Serveur officiel japonais (Japan Official Server)<span class="lk-desc">Serveur japonais officiel du studio : guides pour débutants en abundance, haute qualité de canal vocal, événements et distributions de présents réguliers.</span></span><span class="lk-kind">Officiel</span></li>
          </ul>

          <div class="callout callout-warning">
            <h4>Comment LFG correctement</h4>
            <p>Le système d’amis en jeu ajoute des étiquettes de recommandation basées sur votre style de jeu depuis la Saison 4. Côté Discord, la règle qui fait le plus gagner de temps : précisez <strong>votre langue, votre région, votre niveau de jeu et vos disponibilités</strong> dans le ticket. Un message de trois lignes « niveau 12, farm/normal, dispo 20h-23h » obtient des réponses ; « anyone? » n’en obtient aucune. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <h2 id="reddit">3. Reddit : r/ArenaBreakoutInfinite</h2>
          <p>Le subreddit est le meilleur endroit pour les retours d’expérience non filtrés. Sa modération est indépendante de l’éditeur, mais les publications officielles y apparaissent — et ses règles sont strictes sur ce qui est autorisé. <span class="src-tag src-communautaire">Communauté</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Règle</th><th>Ce qu’elle impose en pratique</th></tr></thead>
              <tbody>
                <tr><td><strong>1. Pas dReserved</strong></td><td>La règle la plus longue : ni attaques personnelles, ni chasse aux sorciers, ni discrimination (sexisme, racisme, ableisme, homophobie, transphobie). Le Brigadier — attaques coordonnées — est interdit.</td></tr>
                <tr><td><strong>2. Contenu lié à ABI</strong></td><td>Tout doit concerner Arena Breakout: Infinite. Le hors-sujet est supprimé, sauf dans les méga-fils de discussion hebdomadaire épinglés.</td></tr>
                <tr><td><strong>3. Contenu restreint</strong></td><td>Interdits : NSFW, chasse aux sorciers, politique, religion, juridique, offensant ou haineux, hacks et exploits, vente et échange. Suppression automatique.</td></tr>
                <tr><td><strong>4. Low-quality et spam</strong></td><td>Pas de rage-bait, pas de doublons, pas de captures d’écran postées sans commentaire.</td></tr>
                <tr><td><strong>5. Flair obligatoire</strong></td><td>Le flair facilite la recherche. Évitez de republier un contenu de moins de deux mois.</td></tr>
                <tr><td><strong>6. Créditer la source</strong></td><td>Fanart, cosplay, guides, vidéos : nommez le créateur dans le titre et lienez la source en commentaire.</td></tr>
                <tr><td><strong>7. Auto-promotion</strong></td><td>Autorisée si vous contribuez aussi. La règle empirique est <strong>80/20</strong> : 80 % de participation, 20 % d’auto-promotion.</td></tr>
                <tr><td><strong>8. No leak</strong></td><td>Aucune fuite de contenu non annoncé.</td></tr>
              </tbody>
            </table>
          </div>

          <figure class="page-figure">
            <img src="../img/communaute/forum-discussion.jpg" alt="Deux joueurs penches sur un ordinateur portable dans un appartement sombre, lisant un long fil de forum ensemble" loading="lazy">
            <figcaption>Reddit, c’est surtout des fils de discussion écrits à deux ou à trois, corrigés par les commentaires. Le format «ULTIMATE TIPS N’ TRICKS » en est l’exemple le plus abouti.</figcaption>
          </figure>

          <h3>Les fils de référence à connaître</h3>
          <ul>
            <li><strong>ULTIMATE TIPS N’ TRICKS GUIDE 3.0</strong> — le guide communautaire le plus complet du jeu, mis à jour en mars 2026 : réglages, placement de réticule, inclinaison, combat, indices sonores, loot rapide, règles de marché, marchands, casque et audio, armures, médecine, munitions, loadouts budgétaires, entraînement de visée, connaissance des cartes. C’est la référence communautaire la plus dense sur la mechanics. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>SEASON 7 « UTOPIA » COMPLETE SURVIVOR &amp; BEGINNER GUIDE</strong> — le guide de survie de la saison en cours, avec le détail des missions d’Intern Disruption et de Comms Interference. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>« Give me your one piece of advice for a beginner »</strong> — le fil de conseils le plus dense du subreddit : extraction en équipe de raid, boîtes de récupération, gestion des listes de morts, economy de marché, etc. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>Fils de plans de Workbench</strong> — « List of All Workbench Blueprints », « Workbench Research », « Research results guide? » : les tables de recettes de la communauté, à recouper avec la base de données. <span class="src-tag src-communautaire">Communauté</span></li>
            <li><strong>Signaler un tricheur</strong> — dans le jeu, via le bouton Report sur l’écran de résultats, ou dans les 24 heures via Personal Info → Match History → Using Cheating Tools. <span class="src-tag src-officiel">Officiel</span></li>
          </ul>

          <h2 id="wikis">4. Les bases de données : où lire la règle exacte</h2>
          <p>C’est le point le plus important de cette page. La plupart des guides YouTube deviennent caducs dès qu’un patch change un chiffre. Une base de données versionnée par patch, elle, vous dit de quel patch elle date. <span class="src-tag src-communautaire">Communauté</span></p>

          <div class="tool-grid">
            <div class="tool-card">
              <h4>ABI Database</h4>
              <span class="tool-tag">Base de données indépendante</span>
              <p>La plus complète et la mieux structurée : <strong>2 647 enregistrements</strong>, versionnés par patch, chaque chiffre marqué vérifié ou non. Contenu : armes, munitions, attachements, armures, casques, headsets, rigs, sacs, objets médicaux, clés, marchands, boss, missions.</p>
              <div class="tool-foot">Patch suivi : 1.0.0.142.19 — mise à jour du 4 novembre 2026. Outils intégrés : comparaison d’armes et de munitions, calculateur d’armure, builder de loadout, suivi de missions, calculateur de valeur des clés, optimiseur de Secure Case. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></div>
            </div>
            <div class="tool-card">
              <h4>ABI Builder</h4>
              <span class="tool-tag">Successeur d’ABI Guide</span>
              <p>La référence la plus vivante du jeu : plans de travail du Workbench, table STK/TTK, Weapon Build Codes partagés par la communauté, <strong>Field Merchant</strong>, tier lists, table de durabilité, maîtrise. C’est aussi le site où résident les codes d’armes « à copier-coller ».</p>
              <div class="tool-foot">Anciennement <strong>abi-guide.dev</strong>, qui n’est plus maintenu et dont les données sont périmées : le site a fusionné avec abibuilder.com. Ne suivez plus l’ancien domaine. <a href="https://abibuilder.com/" target="_blank" rel="noopener">abibuilder.com</a></div>
            </div>
            <div class="tool-card">
              <h4>ABI Tracker</h4>
              <span class="tool-tag">Données &amp; outils</span>
              <p>Un tracker qui suit à la fois le <strong>marché</strong> (prix, quantités, historique, comparaison prix de marché / prix de contact) et le <strong>joueur</strong> (statut, équipe, rang, valeur du stash, historique d’éliminations). Côté outils : Field Merchant, données d’armes et de balles, données d’armures, recherche de Workbench, données de grenades, et un journal de modifications.</p>
              <div class="tool-foot">Plus un tableau des dégâts par balle, un STK/TTK moyen, un « Lag Lover » et un stand de tir. Interface en anglais et en chinois traditionnel. <a href="https://abi-tracker.azurewebsites.net/" target="_blank" rel="noopener">abi-tracker.azurewebsites.net</a></div>
            </div>
            <div class="tool-card">
              <h4>Fandom Wiki — Workbench</h4>
              <span class="tool-tag">Wiki de la communauté</span>
              <p>Le wiki le plus ancien et le plus detailed sur les recettes du Workbench : coûts en niveau 5, coûts réduits, quantités, niveau requis et temps de fabrication. Attention : la page note explicitement que les coûts de fabrication aux niveaux inférieurs restent inconnus.</p>
              <div class="tool-foot">À recouper avec abibuilder.com/workbench, qui sert de référence de l’ancien site officiel. <a href="https://arena-breakout-infinite.fandom.com/wiki/Workbench" target="_blank" rel="noopener">arena-breakout-infinite.fandom.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Guides tiers</h4>
              <span class="tool-tag">Analyse et patches</span>
              <p>Trois-Hung stable de guides sérieux, tous datés et vérifiés contre les notes officielles : <strong>senseos.gg</strong> (objets rouges, anti-triche, données de saison), <strong>timesaver.gg</strong> (calendriers d’événements, règles de modes, analyses détaillées) et <strong>overgear.com</strong> (vues d’ensemble de mechanics, loadouts budgétaires).</p>
              <div class="tool-foot">Tous trois non officiels. Leur atout : ils citent la date du patch auquel ils s’appliquent. <a href="https://senseos.gg/guides/arena-breakout-infinite/" target="_blank" rel="noopener">senseos.gg</a> · <a href="https://timesaver.gg/blog/arena-breakout-infinite-season-8" target="_blank" rel="noopener">timesaver.gg</a> · <a href="https://overgear.com/guides/arena-breakout/" target="_blank" rel="noopener">overgear.com</a></div>
            </div>
            <div class="tool-card dead">
              <h4>ABI Guide (abi-guide.dev)</h4>
              <span class="tool-tag">Obsolète — ne plus utiliser</span>
              <p>Le site le plus populaire de la communauté a cessé d’être maintenu et ses données sont devenues fausses. Il a fusionné avec abibuilder.com.</p>
              <div class="tool-foot">Les liens vers les anciennes pages de l’ABI Guide sont encore partagés sur Reddit et YouTube : c’est la principale source de chiffres périmés en circulation.</div>
            </div>
          </div>

          <figure class="page-figure">
            <img src="../img/communaute/database-workstation.jpg" alt="Poste de travail multi-ecrans avec tableaux de donnees denses, utilisateur vu de dos face aux ecrans dans une piece sombre" loading="lazy">
            <figcaption>Une base versionnée par patch, c’est l’outil qui remplace dix guides YouTube. Vérifiez toujours la date du patch avant de citer un chiffre.</figcaption>
          </figure>

          <h2 id="outils">5. Les outils communautaires à connaître</h2>
          <div class="tool-grid">
            <div class="tool-card">
              <h4>Codes d’arme partageables</h4>
              <span class="tool-tag">abibuilder.com</span>
              <p>Chaque configuration de loadout dispose d’un code exportable. Le code encode l’arme, les attachements et les munitions : un tiers peut le coller et obtenir exactement le même build, y compris les valeurs de stats modifiées par un patch.</p>
              <div class="tool-foot">C’est le format le plus fiable pour partager un build — bien plus sûr qu’une capture d’écran de l’inventaire. <a href="https://abibuilder.com/" target="_blank" rel="noopener">abibuilder.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Calculateur d’armure</h4>
              <span class="tool-tag">ABI Database</span>
              <p>Calcule l’efficacité d’une round contre une plaque de classe donnée. Essential depuis la Saison 7 : la pénétration à faible probabilité contre les armures de classe V et VI a été supprimée, il faut désormais bringing la durabilité sous un seuil pour percer de façon fiable.</p>
              <div class="tool-foot">Le tableau STK/TTK moyen et le stand de tir d’ABI Tracker couvrent le même besoin en lecture rapide. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Optimiseur de Secure Case</h4>
              <span class="tool-tag">ABI Database</span>
              <p>Indique quoi protéger et quoi laisser dans le sac. Pertinent depuis la Saison 7, où la limite de niveau de la Collection Room a été relevée de 2 et le stockage de loot rouge porté à 999.</p>
              <div class="tool-foot">Un point de vigilance a changé avec les événements : les citrouilles ne peuvent pas entrer en Secure Case, et rien n’est dit des vouchers d’événement. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Calculateur de valeur des clés</h4>
              <span class="tool-tag">ABI Database</span>
              <p>Calcule le retour attendu par usage d’une clé. Les « trending entities » de la base au 4 novembre 2026 give un ordre de grandeur : AOC Secret Archives Keycard (Guoyapo Airport, 30 usages, 6 000 K Koen), Motel Main Guest Room Key (Farm, 30 usages, 5 000 K), VIP Reception Keycard (Airport, 3 000 K), Executive Lounge Key (Airport, 2 700 K), Planning Room Key (TV Station, 2 700 K).</p>
              <div class="tool-foot">Les chiffres varient avec le prix de marché du jour : traitez-les comme un ordre de grandeur, pas comme une garantie. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></div>
            </div>
            <div class="tool-card">
              <h4>Field Merchant</h4>
              <span class="tool-tag">abibuilder.com · ABI Tracker</span>
              <p>La liste complète des cargaisons du marchand, avec leur format, leur taille, leur prix et le pool d’objets correspondant. Combinée aux outils open source de reconnaissance sonore, elle donne les probabilités de chaque cargaison.</p>
              <div class="tool-foot">C’est le cœur de l’écosystème d’analyse économique de la communauté : les catégories et les prix des armes, munitions, clés, objets médicaux et objets tactiques sont tous consultables directement.</div>
            </div>
            <div class="tool-card">
              <h4>Suivi de marché</h4>
              <span class="tool-tag">Tracker · GitHub · web</span>
              <p>Suivi des prix et de l’historique, utile pour arbitrer entre vendre au marchand, au contact ou au marché — et pour dater la valeur d’un item de saison avant sa fin.</p>
              <div class="tool-foot">Le <strong>Koen</strong> ne peut pas être acheté contre de l’argent réel : la seule économie saine est l Extraction productive.</div>
            </div>
          </div>

          <h2 id="github">6. Les projets open source sur GitHub</h2>
          <p>La communauté a produit des outils open source remarkable. Ils ne sont pas sanctionnés par l’éditeur : ils exploitent des données publiques et, pour certains, l’audio du client — ce qui les place dans une zone grise dont il faut connaître les limites. <span class="src-tag src-communautaire">Communauté</span></p>

          <ul class="link-list">
            <li><span class="lk-name">ABIDB — Arena Breakout Infinite Offline Database<span class="lk-desc">Application de bureau complète en PowerShell, licence MIT, version 1.0.2. Plus de 19 catégories d’objets, recherche multi-critères, export CSV, comparateur d’armes côte à côte sur 2 à 3 armes, module de mise à jour qui vérifie l’existence de nouvelles versions.</span></span><span class="lk-kind">MIT · Desktop</span></li>
            <li><span class="lk-name">arena.report<span class="lk-desc">Application Next.js / TypeScript / Tailwind. Suivi de l’usage des clés et de la durabilité des armures, calculateur de réparation, analytics de profit par clé, calendrier de performance journalier. Tout est stocké localement en IndexedDB, avec fallback localStorage. MIT.</span></span><span class="lk-kind">MIT · Web</span></li>
            <li><span class="lk-name">Merchant Ear<span class="lk-desc">GPL v3. Reconnaissance sonore + OCR de l’écran du Field Merchant : liste d’objets possibles par cargaison, probabilité de loot rouge, verdict « achetable / pari / pas rentable », et classement des meilleurs achats du raid. Reconnaissance du son par un client C# (.NET 10), traitement web côté navigateur. Dérivé d’ABI Kaluvan.</span></span><span class="lk-kind">GPL v3 · Sons</span></li>
            <li><span class="lk-name">ABI: Merchant Helper<span class="lk-desc">Application Windows en Rust. Écoute le son du glisser-déposer d’une cargaison et surveille la fenêtre du marchand pour en déduire le contenu, avec la probabilité de loot rouge. Base d’achats partagée via purchases.json. Aucune donnée nominative stockée.</span></span><span class="lk-kind">Rust · Sons</span></li>
            <li><span class="lk-name">ABI-Market<span class="lk-desc">Tableau de prix en HTML et JavaScript, déployé sur GitHub Pages. Les données proviennent de captures d’écran du jeu, saisies et datées manuellement — aucun scraping automatique.</span></span><span class="lk-kind">MIT · Web</span></li>
            <li><span class="lk-name">ABI Market Tracker<span class="lk-desc">Scraper Playwright et tableau de suivi des prix. Indispensable pour le MvP économique, inutile pour les règles événementielles.</span></span><span class="lk-kind">Playwright</span></li>
            <li><span class="lk-name">Raid Profit Tracker<span class="lk-desc">Journal de raids : coût du kit, valeur extraite, profit net par session, suivi du K/D et de l’efficacité de loot, tableau de bord des tendances. Disponible pour Windows et macOS.</span></span><span class="lk-kind">Desktop</span></li>
          </ul>

          <div class="callout callout-danger">
            <h4>Les dépôts à ne pas ouvrir</h4>
            <p>Vous croiserez sur GitHub des dépôts au nom évocateur — « ESP », « wallhack », « aimbot », « hack menu », « overlay cheat » — qui prétendent offrir une vision de l ennemi ou un menu de triche. Ils sont à la fois <strong>juridiquement dangereux</strong> et <strong>techniquement mortels pour votre compte</strong> : MoreFun fait tourner un anti-triche kernel-level (ACE) et un DMA Guard depuis août 2026, et sanctionne les comptes qui les utilisent d’un bannissement de dix ans, avec confiscation du Koen et du matériel. Un dépôt de ce type n’est pas un outil, c’est un piège : beaucoup ne contiennent que des scripts qui volent vos identifiants. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h2 id="phishing">7. Sécurité : les pièges à connaître</h2>
          <div class="dodont">
            <div class="dd-card dd-do">
              <h4>Les réflexes qui sauvent</h4>
              <ul>
                <li>Rejoindre un Discord <strong>depuis les annonces Steam</strong>, jamais depuis un résultat de recherche.</li>
                <li>Vérifier le nom exact du compte officiel avant toute interaction : les clones utilisent des noms quasi identiques.</li>
                <li>Ne jamais saisir vos identifiants Steam sur un site de « codes de giveaway » : MoreFun n’a aucun gift system dans le jeu.</li>
                <li>Utiliser le bouton <strong>Report</strong> de l’écran de résultats pour signaler un tricheur, et le canal dédié du Discord pour les bugs.</li>
                <li>Activer la protection 2FA sur Steam et sur le compte de jeu.</li>
              </ul>
            </div>
            <div class="dd-card dd-dont">
              <h4>Les lignes rouges absolues</h4>
              <ul>
                <li><strong>Acheter du Koen.</strong> La vente a été supprimée à la version 1.0 et la politique de tolérance zéro punit acheteurs et vendeurs : confiscation, baisse de Merit, bannissements de dix ans.</li>
                <li><strong>Faire une transaction hors du jeu.</strong> Sans système de cadeau, toute livraison passe par un transfert en raid — exactement ce que la cellule de sécurité surveille.</li>
                <li><strong>Utiliser un ESP, un overlay de radar ou un aimbot.</strong> Bannissement de dix ans, sur le compte et sur l’appareil.</li>
                <li><strong>Faire de l’équipe avec un tricheur</strong> pour connaître ses positions : les sanctions pour les complices montent jusqu’à 3 650 jours.</li>
              </ul>
            </div>
          </div>

          <h2 id="mentor">8. Le programme Mentor : la ressource la plus sous-estimée</h2>
          <p>Le <strong>Kamona Mentor Program</strong> a été lancé le <strong>22 juin 2026</strong>, peu avant la Saison 6. C’est un dispositif officiel de longue haleine qui relie les joueurs expérimentés aux nouveaux. <span class="src-tag src-officiel">Officiel</span></p>

          <figure class="page-figure">
            <img src="../img/communaute/mentor-program.jpg" alt="Joueur experimenté guidant un nouveau joueur devant un ecran montrant une carte tactique" loading="lazy">
            <figcaption>Le mentorat porte sur le jeu, pas sur le support technique : mécaniques de base, connaissance des cartes et itinéraires d’extraction, choix d’équipement et loadouts, conseils tactiques et jeu en escouade.</figcaption>
          </figure>

          <div class="lore-grid">
            <div class="lore-card gold">
              <h4>Demander de l’aide</h4>
              <div class="lore-sub">Étapes 1 à 2</div>
              <ol style="padding-left:1.1rem">
                <li>Rejoindre le serveur communautaire <strong>discord.gg/AqtPAx5Xsn</strong>.</li>
                <li>Ouvrir un ticket dans <strong>#REQUEST-MENTORING</strong> en décrivant : votre besoin, votre langue, votre région, vos disponibilités.</li>
              </ol>
              <p>Les mentors répondent <strong>quand ils sont libres</strong> : ce n’est pas une file d’attente en direct. Et le programme ne traite que du gameplay ; les problèmes de compte et techniques vont au support officiel.</p>
            </div>
            <div class="lore-card north">
              <h4>Devenir mentor</h4>
              <div class="lore-sub">Formulaire + serveur applicant</div>
              <ol style="padding-left:1.1rem">
                <li>Remplir le <strong>formulaire de candidature</strong> lié depuis l’annonce officielle.</li>
                <li>Rejoindre le serveur dédié aux candidats : <strong>discord.gg/CwBXaSd669</strong>.</li>
                <li>En cas de question : contacter le coordinateur communautaire.</li>
              </ol>
              <p>Les mentors actifs reçoivent un rôle communautaire officiel, une reconnaissance publique, un accès prioritaire à certaines activités et, selon les termes de MoreFun, « des récompenses potentielles comme des Bonds, des cartes de nom ou des titres exclusifs ».</p>
            </div>
          </div>

          <div class="callout callout-success">
            <h4>Ce que le mentorat rapporte vraiment</h4>
            <p>Ce n’est pas un simple canal d’entraide : c’est la voie la plus rapide pour éviter les erreurs de débutant qui coûtent une cascade de Koen. Les trois erreurs qui reviennent le plus dans les tickets sont <strong>fouiller un corps sans se placer</strong>, <strong>sursemer son sac au lieu d’extraire au bon moment</strong>, et <strong>vendre au contact ce qui vaut plus au marché</strong> — alors que l’inverse est vrai au-dessus de 5 à 8 k Koen. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <h2 id="inspector">9. L’Inspector Community : la sécurité, à voter</h2>
          <p>Créée à partir de la Saison 4 et ouverte à tous depuis le <strong>11 juin 2026</strong>, l’Inspector Community est une plateforme de relecture vidéo par les joueurs. Les Inspectors regardent les replays de parties signalées ou suspectes et votent sur la présence d’une violation ; la décision finale appartient à l’équipe de sécurité de MoreFun. <span class="src-tag src-officiel">Officiel</span></p>
          <ul>
            <li><strong>Accès</strong> : site officiel → Security Center → bouton Inspector Community ; ou dans le jeu, via le profil et le centre d’événements / Security Center.</li>
            <li><strong>Récompenses</strong> : Koen et Quick Kits selon les paliers, titres d’Inspector, et en fin de saison le titre « Expert Inspector » avec des récompenses exclusives comme les Morale Badges.</li>
            <li><strong>Deux clarifications officielles</strong> qui évitent les erreurs de débutant : les encadrés, surlignages et marqueurs de distance ajoutés par MoreFun dans le replay ne sont <strong>pas</strong> le cheat du joueur signalé ; et les portes ou le loot absents du replay sont <strong>normaux</strong>, pas un signe de triche.</li>
            <li><strong>Un seul Inspecteur ne suffit pas</strong> : chaque replay suspect est envoyé au hasard à plusieurs Inspectors, et l’équipe officielle revoit les verdicts avant toute sanction.</li>
          </ul>
          <div class="stat-strip">
            <div class="stat-box"><div class="sb-val">24 765</div><div class="sb-key">Inspectors — Saison 5</div></div>
            <div class="stat-box"><div class="sb-val">1 617 674</div><div class="sb-key">cas examinés — Saison 5</div></div>
            <div class="stat-box"><div class="sb-val">1 401</div><div class="sb-key">tricheurs bannis — Saison 5</div></div>
            <div class="stat-box"><div class="sb-val">13 058</div><div class="sb-key">Inspectors — Saison 6</div></div>
          </div>
          <p>En Saison 6, 13 058 joueurs ont participé et 618 tricheurs ont été bannis grâce à ce travail. Ce n’est pas le moteur de bannissement principal — les Inspectors sont surtout utiles sur les cas limites, comme le radar, où un regard humain sur le replay complet ajoute ce que la détection automatique ne voit pas. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="methodo">10. Méthode : comment croiser une information</h2>
          <p>Une info trouvée dans un guide, un fil Reddit ou une vidéo YouTube n’a pas la même valeur selon sa provenance. Voici l’ordre de préférence que nous appliquons dans ABI NEXUS. <span class="src-tag src-communautaire">Communauté</span></p>
          <ol class="steps">
            <li><strong>Note de patch officielle datée.</strong> C’est la seule source qui vaut pour un chiffre de règle : multiplicateur, plafond, date, seuil.</li>
            <li><strong>Annonce officielle datée.</strong> X, Steam News, Discord officiel. Utile pour les événements et les giveaways.</li>
            <li><strong>Base de données versionnée par patch.</strong> Pour les stats d’items, dont elle indique la version.</li>
            <li><strong>Guide tiers daté.</strong> Utile pour l’interprétation et les tableaux de synthèse, à condition de vérifier la date du patch qu’il cite.</li>
            <li><strong>Retour d’expérience sur Reddit ou Discord.</strong> Utile pour la sensation, l’expérience de jeu et les pièges non documentés. Jamais pour un chiffre de règle.</li>
            <li><strong>Vidéo YouTube.</strong> Excellente pour la gestuelle et le positionnement, qui ne s’écrivent pas. À noter : une vidéo ancienne sur un patch ancien est un piège fréquent.</li>
          </ol>
          <div class="callout callout-warning">
            <h4>Le test des cinq secondes</h4>
            <p>Pour n’importe quel chiffre que vous lisez — un multiplicateur, un seuil, une date, un pourcentage — demandez-vous : <em>de quel patch daté cette affirmation vient-elle ?</em> Si la réponse est « aucune », le chiffre est à traiter comme une rumeur, quelle que soit la qualité de la source. <span class="src-tag src-communautaire">Communauté</span></p>
          </div>

          <h2 id="sources">11. Sources</h2>
          <h3>Officiel</h3>
          <ul class="src-list">
            <li><span class="src-name">Annonces Steam officielles</span> — source primaire des notes de patch et des liens d’invite Discord. <a href="https://store.steampowered.com/news/app/2073620" target="_blank" rel="noopener">store.steampowered.com</a></li>
            <li><span class="src-name">Lancement du Mentor Program</span> — 22 juin 2026 : serveur communautaire, ticket #REQUEST-MENTORING, formulaire de candidature, récompenses. <a href="https://steamcommunity.com/app/2073620/discussions/0/690870825661914139/" target="_blank" rel="noopener">steamcommunity.com</a></li>
            <li><span class="src-name">Inspector Community est arrivé</span> — annonce de lancement et mode d’accès. <a href="https://x.com/ArenaBreakoutPC/status/2011800620999881152" target="_blank" rel="noopener">x.com/ArenaBreakoutPC</a></li>
            <li><span class="src-name">Protectors of Peace — merci à chaque Inspector</span> — chiffres de la saison. <a href="https://steamcommunity.com/games/2073620/announcements/detail/536631984572597235" target="_blank" rel="noopener">steamcommunity.com</a></li>
            <li><span class="src-name">Discord et liens officiels</span> — inventaire des canaux, avec l’avertissement sur les serveurs tiers. <a href="https://arenabreakout-infinite.com/guides/discord-and-community/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></li>
          </ul>
          <h3>Communautaire</h3>
          <ul class="src-list">
            <li><span class="src-name">ABI Database</span> — 2 647 enregistrements, patch 1.0.0.142.19, outils de comparaison et de calcul. <a href="https://arenabreakout-infinite.com/" target="_blank" rel="noopener">arenabreakout-infinite.com</a></li>
            <li><span class="src-name">ABI Builder / abibuilder.com</span> — plans de Workbench, STK/TTK, codes d’arme, Field Merchant. Successeur d’ABI Guide, dont l’obsolescence est signalée sur place. <a href="https://abibuilder.com/" target="_blank" rel="noopener">abibuilder.com</a></li>
            <li><span class="src-name">ABI Tracker</span> — marché, recherche de joueur, données d’armes et de munitions, journal de modifications. <a href="https://abi-tracker.azurewebsites.net/" target="_blank" rel="noopener">abi-tracker.azurewebsites.net</a></li>
            <li><span class="src-name">r/ArenaBreakoutInfinite</span> — règles du subreddit, fils ULTIMATE TIPS N’ TRICKS 3.0, guide de survie S7, fil de conseils pour débutants, plans de Workbench. <a href="https://www.reddit.com/r/ArenaBreakoutInfinite/" target="_blank" rel="noopener">reddit.com</a></li>
            <li><span class="src-name">Projets GitHub</span> — ABIDB, arena.report, Merchant Ear, ABI Merchant Helper, ABI-Market, ABI Market Tracker, Raid Profit Tracker. <a href="https://github.com/" target="_blank" rel="noopener">github.com</a></li>
            <li><span class="src-name">senseos.gg, timesaver.gg, overgear.com, gamers.wiki, disboard.org</span> — guides datés, wiki, et annuaire des serveurs Discord par langue. <a href="https://disboard.org/servers/tag/arena-breakout-infinite?sort=member_count" target="_blank" rel="noopener">disboard.org</a></li>
          </ul>
          <h3>Non confirmé</h3>
          <ul class="src-list">
            <li>Les <strong>récompenses précises du mentorat</strong> (cartes Steam jusqu’à 100 $, bundles) varient selon les sources et les versions des pages ; seule la mention de « récompenses potentielles comme des Bonds, cartes de nom ou titres exclusifs » est explicitement attribuable à MoreFun.</li>
            <li>Le <strong>nom des coordinateurs</strong> et l’URL exacte des formulaires changent selon les Relational Community Coordinators par langue ; vérifiez sur l’annonce Discord en cours.</li>
            <li>Les <strong>chiffres de l’Inspector Community</strong> (24 765 participants / 1 617 674 cas / 1 401 bannis pour la Saison 5 ; 13 058 / 618 pour la Saison 6) proviennent de publications officielles mais couvrent des saisons différentes : ne les additionnez pas.</li>
          </ul>
        """
