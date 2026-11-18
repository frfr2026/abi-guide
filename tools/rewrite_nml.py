#!/usr/bin/env python3
"""Reecrit pages/map-no-mans-land.html comme un vrai guide du mode PvE a tickets."""
import pathlib, re

P = pathlib.Path('pages/map-no-mans-land.html')
s = P.read_text(encoding='utf-8')

DESC = ("No Man's Land est le mode PvE a tickets d'Arena Breakout Infinite : rotation Farm, "
        "Valley et TV Station, loadout impose, aucun joueur adverse, butin conserve en "
        "extraction complete. Guide, tickets et strategie.")

# --- metadonnees ---
s = s.replace("<title>No Man&#x27;s Land — La zone PvE | ABI NEXUS</title>",
              "<title>No Man&#x27;s Land — Le mode PvE à tickets | ABI NEXUS</title>")
s = re.sub(r'<meta name="description" content="[^"]*">',
           '<meta name="description" content="%s">' % DESC, s, count=1)
s = re.sub(r'<meta property="og:title" content="[^"]*">',
           '<meta property="og:title" content="No Man&#x27;s Land — Le mode PvE à tickets — ABI NEXUS">', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*">',
           '<meta property="og:description" content="%s">' % DESC, s, count=1)
s = re.sub(r'<meta name="twitter:title" content="[^"]*">',
           '<meta name="twitter:title" content="No Man&#x27;s Land — Le mode PvE à tickets — ABI NEXUS">', s, count=1)
s = re.sub(r'<meta name="twitter:description" content="[^"]*">',
           '<meta name="twitter:description" content="%s">' % DESC, s, count=1)
s = re.sub(r'<meta property="og:image" content="https://abinexus\.fr/img/seo/og-archives\.jpg">',
           '<meta property="og:image" content="https://abinexus.fr/img/cards/var-nml.jpg">', s, count=1)
s = re.sub(r'<meta name="twitter:image" content="https://abinexus\.fr/img/seo/og-archives\.jpg">',
           '<meta name="twitter:image" content="https://abinexus.fr/img/cards/var-nml.jpg">', s, count=1)
s = s.replace('<meta property="og:image:width" content="1200">', '<meta property="og:image:width" content="1672">')
s = s.replace('<meta property="og:image:height" content="630">', '<meta property="og:image:height" content="941">')
s = s.replace('<meta property="og:image:alt" content="ABI NEXUS — guide Arena Breakout Infinite, Saison 7 : Utopia">',
              '<meta property="og:image:alt" content="No Man\'s Land — mode PvE a tickets d\'Arena Breakout Infinite">')
s = s.replace('<meta name="twitter:image:alt" content="ABI NEXUS — guide Arena Breakout Infinite, Saison 7 : Utopia">',
              '<meta name="twitter:image:alt" content="No Man\'s Land — mode PvE a tickets d\'Arena Breakout Infinite">')

# --- en-tete de page ---
s = s.replace('<p class="eyebrow">Maps — No Man\'s Land</p>',
              '<p class="eyebrow">Mode PvE — No Man\'s Land</p>')
s = s.replace('<h1>No Man\'s Land<br>La Zone PvE</h1>',
              '<h1>No Man\'s Land<br>Le mode PvE à tickets</h1>')
s = s.replace('<p class="page-sub">Zéro risque, que du skill : la salle de tir militaire de Kamona.</p>',
              '<p class="page-sub">Un ticket, un loadout imposé, aucun opérateur adverse : vous '
              'reparrtez avec tout votre butin. Le mode le plus rentable du jeu — si on l\'abuse pas.</p>')

# --- figure ---
s = s.replace('<img width="1024" height="1536" src="../img/cards/var-nml.jpg" alt="Zone d\'exclusion biohazard au crépuscule" loading="lazy" decoding="async">',
              '<img width="1672" height="941" src="../img/cards/var-nml.jpg" alt="Point de contrôle industriel abandonné, zone d\'exclusion biohazard au crépuscule" loading="lazy" decoding="async">')
s = s.replace('<figcaption>No Man\'s Land — la zone d\'entraînement PvE : efficacité militaire sans risque PMC.</figcaption>',
              '<figcaption>Checkpoint industriel abandonné : l\'ambiance de No Man\'s Land, où aucun opérateur adverse ne '
              'peut vous tuer — seuls les Militants, les Élites et les zombies le peuvent.</figcaption>')

# --- bloc de faits ---
old_facts = s[s.find('          <div class="facts">'):s.find('          </div>\n\n          <h2 id="vue">')+len('          </div>\n')]
new_facts = '''          <div class="facts">
            <div class="fact"><span class="fact-label">Entrée</span><span class="fact-value">1 ticket par run</span></div>
            <div class="fact"><span class="fact-label">Équipement</span><span class="fact-value">Charge imposée par le mode</span></div>
            <div class="fact"><span class="fact-label">Cartes</span><span class="fact-value">Farm · Valley · TV Station</span></div>
            <div class="fact"><span class="fact-label">Adversaires</span><span class="fact-value">IA seule — Militants, Élites, zombies</span></div>
            <div class="fact"><span class="fact-label">Butin</span><span class="fact-value">Pack complet conservé à l'extraction</span></div>
            <div class="fact"><span class="fact-label">Introduit en</span><span class="fact-value">Saison 5 : Distortion (2 avril 2026)</span></div>
          </div>
'''
s = s.replace(old_facts, new_facts)

# --- corps de l'article ---
start = s.find('          <h2 id="vue">')
end = s.find('        </article>')
if start < 0 or end < 0:
    raise SystemExit('bornes article introuvables')

body = '''          <h2 id="vue">1. Ce qu'est vraiment No Man's Land</h2>
          <p><strong>No Man's Land n'est pas une carte.</strong> C'est un <strong>mode PvE à tickets</strong> :
          vous entrez avec un ticket et un <strong>équipement imposé par le mode</strong>, vous piller la carte en
          rotation, et vous repartez avec <strong>tout votre sac</strong> — sans qu'aucun joueur adverse puisse
          vous tuer. <span class="src-tag src-officiel">Officiel</span></p>
          <p>Le mode a été introduit par Morefun en <strong>Saison 5 : Distortion</strong> (2 avril 2026),
          aux côtés du Warlord Tournament. L'annonce officielle le décrit sans ambiguïté :
          <em>« No Man's Land — Farm, Valley, TV Station rotate : Run solo or only with your squad in a
          pure PvE mode with fixed loadout. Tickets needed for entry. »</em> <span class="src-tag src-officiel">Officiel</span></p>
          <p>La fiche du premier anniversaire du jeu résume l'intention :
          <em>« scavenge, survive, and extract with full pack loot, all without the threat of hostile
          operatives »</em>. Autrement dit : on vous retire la peur, on vous laisse le loot. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="regles">2. Les quatre règles qui changent tout</h2>
          <div class="table-wrap">
            <table class="data-table">
              <caption>No Man's Land contre un Tactical Ops classique</caption>
              <thead><tr><th scope="col">Règle</th><th scope="col">Tactical Ops</th><th scope="col">No Man's Land</th></tr></thead>
              <tbody>
                <tr><td><strong>PvP</strong></td><td>Oui — tout le monde tire à tout le monde</td><td><strong>Non.</strong> Aucun opérateur adverse ne peut vous tuer</td></tr>
                <tr><td><strong>Équipement</strong></td><td>Votre stash, votre budget</td><td><strong>Imposé</strong> par le mode, selon son palier de difficulté</td></tr>
                <tr><td><strong>Entrée</strong></td><td>Gratuite</td><td><strong>1 ticket</strong> par run</td></tr>
                <tr><td><strong>Extraction</strong></td><td>Case sécurisée ou clé pour les rouges</td><td><strong>Pack complet conservé</strong>, rien ne peut vous le prendre</td></tr>
                <tr><td><strong>Équipe</strong></td><td>Matchmaking libre</td><td>Solo, ou votre propre escouade uniquement</td></tr>
                <tr><td><strong>Qui peut vous tuer</strong></td><td>Joueurs + IA</td><td><strong>IA uniquement</strong> : Militants, Élites, et zombies en S7</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Pourquoi c'est le mode le plus rentable du jeu</h3>
            <p>Un ticket ne se perd pas quand vous mourez : vous perdez le run, pas votre armure. Combiné au
            <strong>pack complet conservé</strong>, chaque ticket est une mise risquée quasi nulle pour des
            dizaines de milliers de Koen, des munitions, des matériaux et parfois un rouge. <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

          <h2 id="cartes">3. La rotation : Farm, Valley, TV Station</h2>
          <p>No Man's Land ne se joue pas sur les six cartes. Trois seulement tournent en mode PvE, et elles
          tournent <strong>en rotation</strong> : le mode ne vous laisse pas choisir votre terrain à chaque run.
          Ce sont exactement les trois cartes les plus « core » du jeu.</p>
          <ul class="zone-list">
            <li><strong><a href="map-farm.html">Farm</a></strong> — la plus petite et la plus lisible. Ideal pour
              roder un extract et apprendre les rotations. <a href="map-farm.html">Guide Farm →</a></li>
            <li><strong><a href="map-valley.html">Valley</a></strong> — la plus dense en loot et en points d'intérêt.
              C'est ici que se trouve le fameux <strong>Small Factory</strong>, dont les boîtes à outils sont
              la source de rouges la plus citée en No Man's Land. <a href="map-valley.html">Guide Valley →</a></li>
            <li><strong><a href="map-tv-station.html">TV Station</a></strong> — la plus rapide. Parfaite pour les
              runs de routine et de farm de composants. <a href="map-tv-station.html">Guide TV Station →</a></li>
          </ul>
          <p>Les trois autres cartes — <a href="map-northridge.html">Northridge</a>,
          <a href="map-armory.html">Armory</a> et <a href="map-airport.html">Airport</a> — ne sont pas
          disponibles en No Man's Land standard. <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="tickets">4. Les tickets : où les obtenir</h2>
          <p>Un run = un ticket. Deux objets coexistent : les <strong>No Man's Land Tickets</strong> (version
          standard) et les <strong>Zombie / Biohazard No Man's Land Passes</strong> (variante infectée de la
          Saison 7). Ils s'obtiennent presque tous gratuitement.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Sources de tickets et de passes</caption>
              <thead><tr><th scope="col">Source</th><th scope="col">Ce que ça donne</th><th scope="col">Période</th></tr></thead>
              <tbody>
                <tr><td>Événement de connexion d'octobre 2026</td><td>2 400 Bonds limités + <strong>14 tickets Zombie No Man's Land</strong> en se connectant 7 jours</td><td>1er – 21 octobre 2026</td></tr>
                <tr><td>Festival Biohazard &amp; Bountiful Autumn</td><td><strong>3 passes Biohazard</strong> à la connexion, puis 1 passe Zombie à chaque palier de tâches (4, 8, 16) chaque semaine</td><td>Depuis le 24 septembre 2026</td></tr>
                <tr><td>Drops en mode Infected Area</td><td>Chance d'obtenir des passes Zombie No Man's Land pendant un raid</td><td>Toute la durée de l'événement</td></tr>
                <tr><td>Tactical Ops classiques</td><td>Tickets No Man's Land standards, historiquement <strong>échangeables hors raid</strong></td><td>En continu</td></tr>
                <tr><td>Événement du 1er anniversaire</td><td>36 tickets No Man's Land au total</td><td>Début 2026</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">Le bon réflexe</h3>
            <p>Pendant une fenêtre d'événement, <strong>vous n'avez rien à acheter</strong>. Connectez-vous chaque
            jour et videz vos tâches quotidiennes : les passes s'accumulent tout seuls. Les Combat Pass n'ont
            jamais été le bon canal pour les tickets.</p>
          </div>

          <h2 id="zombies">5. La variante Zombies No Man's Land (Saison 7)</h2>
          <p>La Saison 7 : Utopia a transformée Kamona en foyer d'infection. Le mode a donc une variante
          saisonnière : <strong>Zombies No Man's Land</strong>, qui se joue sur les cartes infectées et où vous
          nettoyez des hordes de zombies en même temps que vous pillez. L'officialisation de la saison :
          <em>« Season 7 has begun, and zombies are running rampant across Kamona! It's time to join forces,
          fight back the horde, and save Kamona! »</em> <span class="src-tag src-officiel">Officiel</span></p>
          <p>La variante s'inscrit dans la série d'événements <strong>Biohazard</strong> qui distribue aussi
          l'ensemble de tenue Hazmat, la mechanics de <strong>Supplies Drops 2.0</strong> et le collectionnable
          <strong>Lunar Soil Sample</strong>. Le <strong>Merit Challenge</strong> de l'événement convertit votre
          meilleur score hebdomadaire de Merit en <strong>Koen × 3, jusqu'à 3 000 000 Koen par semaine</strong> —
          c'est le levier principal du mode, bien plus rentable que les rouges. <span class="src-tag src-communautaire">Communautaire</span></p>
          <p>Le mode applique le <strong>Mode-Based Ammo and Gear Cap</strong> de la saison : <strong>Tier 4
          maximum en Normal, Tier 5 en Lockdown</strong>, et le RNG de pénétration des armures T5/T6 a été
          supprimé. Comme l'équipement est imposé, vous êtes de toute façon dans le plafond du palier —
          traitez ce mode comme un <strong>run de butin</strong>, jamais comme un run de démonstration d'équipement.
          <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="rendement">6. Ce que le mode rapporte vraiment</h2>
          <p>La question qui revient sur Reddit et sur les forums : <em>« ça vaut le coup ? »</em>. Réponse
          nuancée, et les chiffres de la communauté sont explicites.</p>
          <ul>
            <li><strong>Les Koen et l'or sont le revenu fiable.</strong> Plusieurs dizaines de milliers de Koen par
              run correct. C'est la base.</li>
            <li><strong>Les rouges ne sont jamais garantis.</strong> Les rapports de la semaine sur
              r/ArenaBreakoutInfinite vont d'« un rouge environ tous les 4 raids » à « un rouge en deux
              semaines », en passant par « 7 runs, pas un seul rouge, mais une tonne de comics et 35k d'or ».
              <span class="src-tag src-communautaire">Communautaire</span></li>
            <li><strong>Les rouges viennent des conteneurs, pas d'un type précis de coffre.</strong> Un joueur
              qui en a sorti deux d'un coup les a trouvés « dans des boîtes à outils du Small Factory » — pas
              dans un coffre précis. Donc : pillez toute la carte, ne foncez pas sur les gros safes. <span class="src-tag src-communautaire">Communautaire</span></li>
            <li><strong>Le ratio Koen par ticket est le vrai rendement.</strong> Consommables, munitions et
              objets divers s'accumulent sans risque : c'est ce que vous.runneriez dans un raid classique.</li>
          </ul>
          <div class="callout callout-danger">
            <h3 class="h4">L'erreur de débutant</h3>
            <p>Passer dix tickets d'affilée en espérant le rouge. Le mode ne « fait pas » de rouge : il fait
            <strong>du Koen massif et régulier</strong>. Le rouge est un bonus, jamais le plan.</p>
          </div>

          <h2 id="strategie">7. La stratégie qui marche</h2>
          <p>En No Man's Land, la méta communautaire est simple et bon marché. Sur r/ArenaBreakoutInfinite,
          face à la question « c'est quoi la méta sur ce mode maintenant ? », la réponse de référence :
          <em>« C'est des zombies et des scavs, donc prends la munition la moins chère avec le plus de
          dégâts sur la chair, et prends-en beaucoup. Armure pas chère, gros sac. C'est tout ce que j'ai. »</em>
          <span class="src-tag src-communautaire">Communautaire</span></p>
          <ol>
            <li><strong>Ammo-first.</strong> La munition la moins chère avec le maximum de dégâts sur la chair
              (dum-dum, buckshot) et en grande quantité. Contre les zombies et les IA, la économie de munitions
              tue plus de raids que la précision.</li>
            <li><strong>Armure légère.</strong> Contre de l'IA, la protection et le poids sont du pur gaspillage :
              vous n'avez personne à percer. Gardez de la place pour le loot.</li>
            <li><strong>Le plus gros sac possible.</strong> Un sac plein sort en une run ce qu'un raid classique
              sort en trois.</li>
            <li><strong>Parcourez, ne rush pas.</strong> Les conteneurs valent plus que les safes, et les
              « safes » sont précisément ce que les IA gardent.</li>
            <li><strong>Quittez avant la nuit.</strong> Le mode a un cycle de jour/nuit : les IA deviennent
              plus actives, et votre butin ne vaut plus le risque du ticket perdu.</li>
          </ol>

          <h2 id="faq">8. FAQ</h2>
          <h3 class="h4">No Man's Land est-il une carte ?</h3>
          <p>Non. C'est un <strong>mode</strong> qui fait tourner trois cartes existantes en rotation. C'est la
          confusion la plus fréquente, y compris sur les wikis : No Man's Land n'a ni carte propre, ni ses
          propres extractions, ni sa propre table de loot.</p>
          <h3 class="h4">Peut-on jouer en équipe ?</h3>
          <p>Oui, mais <strong>uniquement avec sa propre escouade</strong>. Il n'y a pas de matchmaking : pas de
          groupe avec des inconnus.</p>
          <h3 class="h4">Les tickets sont-ils payants ?</h3>
          <p>Ils sont le plus souvent <strong>offerts par les événements</strong> (connexion, tâches,
          drops en Infected Area). Les tickets standards tombent aussi en Tactical Ops et sont
          échangeables hors raid.</p>
          <h3 class="h4">Garde-t-on le butin si on meurt ?</h3>
          <p>Non. Si l'IA vous tue, vous perdez le butin de la run — c'est le seul vrai risque du mode, et il
          ne vient jamais d'un joueur.</p>
          <h3 class="h4">Est-ce le meilleur moyen de farm des Koen ?</h3>
          <p>C'est le moyen le plus <strong>rentable en valeur par ticket</strong>, parce que rien ne peut
          vous voler votre extraction. Pour le <strong>Merit</strong> de la Zombie Research, en revanche, les
          modes dédiés (Zombie Endless) sont plus efficaces.</p>

'''
s = s[:start] + body + s[end:]

# --- sommaire ---
toc_start = s.find('        <aside class="toc" aria-label="Sommaire">')
toc_end = s.find('        </aside>', toc_start)
new_toc = '''        <aside class="toc" aria-label="Sommaire">
          <h4>Sommaire</h4>
<a href="#vue" id="lnk-map-no-mans-land-094">1. Ce qu'est vraiment No Man's Land</a>
<a href="#regles" id="lnk-map-no-mans-land-095">2. Les quatre règles</a>
<a href="#cartes" id="lnk-map-no-mans-land-096">3. La rotation des cartes</a>
<a href="#tickets" id="lnk-map-no-mans-land-097">4. Les tickets</a>
<a href="#zombies" id="lnk-map-no-mans-land-098">5. Variante Zombies (S7)</a>
<a href="#rendement" id="lnk-map-no-mans-land-099">6. Ce que le mode rapporte</a>
<a href="#strategie" id="lnk-map-no-mans-land-100">7. La stratégie</a>
<a href="#faq" id="lnk-map-no-mans-land-101">8. FAQ</a>
'''
s = s[:toc_start] + new_toc + s[toc_end:]

P.write_text(s, encoding='utf-8')
print('map-no-mans-land.html reecrit : %d caracteres' % len(s))
