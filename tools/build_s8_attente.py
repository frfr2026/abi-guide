#!/usr/bin/env python3
"""Cree pages/saison8-attente.html a partir du gabarit saison7-balance-changes.html."""
import pathlib, re

ROOT = pathlib.Path('.')
TPL = ROOT / 'pages/saison7-balance-changes.html'
OUT = ROOT / 'pages/saison8-attente.html'

DESC = ("Saison 8 d'ABI : calendrier officiel des saisons, fin estimée de l'Utopia en décembre 2026, "
        "ce qui se réinitialise et la checklist de préparation.")

TPL_S = TPL.read_text(encoding='utf-8')
s = TPL_S

# ---------- renommage des identifiants de liens ----------
s = s.replace('lnk-saison7-balance-changes-', 'lnk-saison8-attente-')
s = s.replace('saison7-balance-changes.html', 'saison8-attente.html')

# ---------- metadonnees ----------
s = re.sub(r'<title>.*?</title>',
           '<title>Saison 8 : la fin de l\'Utopia et ce qui arrive | ABI NEXUS</title>', s, count=1)
s = re.sub(r'<meta name="description" content="[^"]*">',
           '<meta name="description" content="%s">' % DESC.replace("'", "&#x27;"), s, count=1)
s = re.sub(r'<meta property="og:title" content="[^"]*">',
           '<meta property="og:title" content="Saison 8 : la fin de l&#x27;Utopia — ABI NEXUS">', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*">',
           '<meta property="og:description" content="%s">' % DESC.replace("'", "&#x27;"), s, count=1)
s = re.sub(r'<meta name="twitter:title" content="[^"]*">',
           '<meta name="twitter:title" content="Saison 8 : la fin de l&#x27;Utopia — ABI NEXUS">', s, count=1)
s = re.sub(r'<meta name="twitter:description" content="[^"]*">',
           '<meta name="twitter:description" content="%s">' % DESC.replace("'", "&#x27;"), s, count=1)
s = s.replace('https://abinexus.fr/img/zombies/balance-pvp.jpg',
              'https://abinexus.fr/img/cards/card-balance.jpg')
s = s.replace('<meta property="og:image:width" content="1536">', '<meta property="og:image:width" content="800">')
s = s.replace('<meta property="og:image:height" content="1024">', '<meta property="og:image:height" content="450">')
s = s.replace('<meta property="og:image:alt" content="ABI NEXUS — guide Arena Breakout Infinite, Saison 7 : Utopia">',
              '<meta property="og:image:alt" content="ABI NEXUS — la fin de la Saison 7 Utopia et la venue de la Saison 8">')
s = s.replace('"datePublished": "2026-09-16"', '"datePublished": "2026-11-17"')
s = s.replace('"headline": "Balance Changes S7', '"headline": "Saison 8')
# JSON-LD : descriptions et noms
s = re.sub(r'"description": "R[eé]équilibrage Saison 7 Utopia d\'ABI[^"]*"',
           '"description": "%s"' % DESC.replace("'", "'"), s)
s = s.replace('"name": "Balance Changes S7', '"name": "Saison 8')
s = re.sub(r'"headline": "Balance Changes S7[^"]*"',
           '"headline": "Saison 8 : la fin de l\'Utopia et ce qui arrive"', s)

# ---------- fil d'ariane ----------
s = re.sub(r'<nav class="breadcrumb" aria-label="Fil d\'Ariane">.*?</nav>',
           '''<nav class="breadcrumb" aria-label="Fil d'Ariane">
        <a href="../index.html" id="lnk-saison8-attente-001">Accueil</a><span class="sep">/</span>
        <a href="saison7-utopia.html" id="lnk-saison8-attente-002">Saison 7 : Utopia</a><span class="sep">/</span>
        <span aria-current="page">Saison 8 : ce qui arrive</span>
      </nav>''', s, flags=re.S)

# ---------- en-tete ----------
s = re.sub(r'<header class="page-head">.*?</header>',
           '''<header class="page-head">
        <p class="eyebrow">Saison 7 : Utopia — Passerelle</p>
        <h1>Saison 8 : la fin de l'Utopia</h1>
        <p class="page-sub">Ce que le calendrier officiel des saisons permet de prévoir, ce qui
        réinitialise à la bascule, et la checklist à faire avant la dernière semaine de la S7.</p>
      </header>''', s, flags=re.S)

# ---------- corps ----------
CONTENT = '''        <article class="content-col">
          <figure class="page-figure">
            <img width="800" height="450" src="../img/cards/card-balance.jpg" alt="Salle d'armurerie, lumière rasante sur les armes alignées" loading="lazy" decoding="async">
            <figcaption>La Saison 7 : Utopia est la cinquième saison d'ABI Infinite. D'après le rythme officiel,
            elle devrait céder la place à la Saison 8 autour de la première quinzaine de décembre 2026.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Saison en cours</span><span class="fact-value">Saison 7 : Utopia</span></div>
            <div class="fact"><span class="fact-label">En direct depuis</span><span class="fact-value">16 septembre 2026</span></div>
            <div class="fact"><span class="fact-label">Durée observée</span><span class="fact-value">78 à 89 jours sur les saisons 4 à 6</span></div>
            <div class="fact"><span class="fact-label">Fin estimée de la S7</span><span class="fact-value">Semaine du 8 – 14 décembre 2026</span></div>
            <div class="fact"><span class="fact-label">Statut de la S8</span><span class="fact-value">Non annoncée officiellement</span></div>
            <div class="fact"><span class="fact-label">Wipe du stash</span><span class="fact-value">Non — ABI ne wipe pas</span></div>
          </div>

          <h2 id="etat">1. Où en est-on réellement</h2>
          <p>Au <strong>13 novembre 2026</strong>, la <strong>Saison 7 : Utopia</strong> est la saison en cours
          d'Arena Breakout: Infinite. Elle a démarré le <strong>16 septembre 2026</strong> et approche de ses
          deux mois d'existence. Aucune date de lancement pour la Saison 8 n'a été annoncée par Morefun :
          pas de post de révélation, pas d'annonce sur Steam, pas de mention dans les notes de patch —
          la dernière mise à jour en date étant le <strong>Live Update du 10 novembre</strong>. <span class="src-tag src-officiel">Officiel</span></p>
          <p>En revanche, le rythme des saisons est très régulier, et c'est ce rythme qui permet d'estimer la
          bascule avec une précision raisonnable.</p>

          <h2 id="calendrier">2. Le calendrier officiel des saisons</h2>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les cinq saisons d'ABI Infinite, d'après les annonces Steam de Morefun</caption>
              <thead><tr><th scope="col">Saison</th><th scope="col">Nom</th><th scope="col">Mise en ligne</th><th scope="col">Durée</th></tr></thead>
              <tbody>
                <tr><td>Saison 3</td><td>Breach (sortie complète)</td><td>16 septembre 2025</td><td>114 jours</td></tr>
                <tr><td>Saison 4</td><td>Dusk to Dawn (Airport Hunt)</td><td>8 janvier 2026</td><td>84 jours</td></tr>
                <tr><td>Saison 5</td><td>Distortion</td><td>2 avril 2026</td><td>89 jours</td></tr>
                <tr><td>Saison 6</td><td>White Nights</td><td>30 juin 2026</td><td>78 jours</td></tr>
                <tr><td><strong>Saison 7</strong></td><td><strong>Utopia</strong></td><td><strong>16 septembre 2026</strong></td><td>En cours</td></tr>
              </tbody>
            </table>
          </div>
          <p>Les saisons 4, 5 et 6 ont duré <strong>78 à 89 jours</strong>. En appliquant ce rythme à la
          saison 7, la fin de l'Utopia se situe entre le <strong>3 et le 14 décembre 2026</strong> — la
          fourchette la plus probable étant la <strong>semaine du 8 au 14 décembre</strong>. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="callout callout-warning">
            <h3 class="h4">Le risque à garder en tête</h3>
            <p>La Saison 4 a glissé sur janvier 2026 à cause des fêtes. Une saison 8 repoussée en
            <strong>janvier 2027</strong> n'est donc pas impossible : c'est le scénario le plus prudent
            pour qui vend des plans de Battle Pass ou planifie un gros achat de Bonds.</p>
          </div>

          <h2 id="annonce">3. Comment l'annonce est-elle faite</h2>
          <p>Morefun n'annonce pas ses saisons d'un bloc : le schéma est constant, et il permet de savoir
          à quel moment guetter.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Le délai entre le premier signal officiel et le lancement</caption>
              <thead><tr><th scope="col">Saison</th><th scope="col">Premier post officiel</th><th scope="col">Lancement</th><th scope="col">Délai</th></tr></thead>
              <tbody>
                <tr><td>Saison 4</td><td>10 décembre 2025 (« Coming Early Jan. »)</td><td>8 janvier 2026</td><td>29 jours</td></tr>
                <tr><td>Saison 5</td><td>20 mars 2026</td><td>2 avril 2026</td><td>13 jours</td></tr>
                <tr><td>Saison 6</td><td>23 juin 2026</td><td>30 juin 2026</td><td>7 jours</td></tr>
                <tr><td>Saison 7</td><td>8 septembre 2026</td><td>16 septembre 2026</td><td>8 jours</td></tr>
              </tbody>
            </table>
          </div>
          <p>Concrètement : à partir de la mi-novembre, le premier post « reveal » est attendu, et le
          lancement suit généralement <strong>une à deux semaines</strong> plus tard. C'est le moment de
          surveiller l'onglet <strong>Actualités</strong> du jeu et les annonces Steam de l'app 2073620.
          <span class="src-tag src-officiel">Officiel</span></p>

          <h2 id="compte-a-rebours">4. Le compte à rebours des événements de la S7</h2>
          <p>La saison n'est pas une fin brutale : elle a une queue. Les événements de fin de saison se
          chevauchent, et c'est là que se joue la dernière fenêtre pour obtenir des récompenses qui ne
          reviendront pas. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Événements de fin de Saison 7 — dates en UTC+0</caption>
              <thead><tr><th scope="col">Événement</th><th scope="col">Fin</th><th scope="col">Ce qu'il faut faire avant</th></tr></thead>
              <tbody>
                <tr><td>Trash to Treasure Smelter</td><td><strong>15 novembre 2026</strong></td><td>Échanger les derniers composants contre des récompenses avant la fermeture</td></tr>
                <tr><td>Kamona Investigation : Tea Break Delights</td><td><strong>22 novembre 2026</strong></td><td>Finir les tâches quotidiennes : les récompenses sont conditionnées aux tâches</td></tr>
                <tr><td>Halloween : Mysterious Pumpkin Night</td><td><strong>25 novembre 2026</strong></td><td>Récupérer les récompenses d'Halloween restantes</td></tr>
                <tr><td>Third Warlord Tournament</td><td><strong>7 décembre 2026</strong></td><td>Terminer le classement et encaisser les primes</td></tr>
                <tr><td>Fin de saison estimée</td><td><strong>8 – 14 décembre 2026</strong></td><td>Dernière chance de solder le Pass et les missions saisonnières</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="reset">5. Ce qui se réinitialise, ce qui reste</h2>
          <p>C'est le point le plus mal compris d'ABI, et la mauvaise réponse fait perdre beaucoup d'argent
          aux nouveaux joueurs. <strong>ABI ne wipe pas votre stash.</strong> À la fin d'une saison, ce qui
          est remis à zéro est strictement le <strong>progression saisonnière</strong> — le reste est conservé.
          <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Ce que la fin de saison touche — et ce qu'elle ne touche pas</caption>
              <thead><tr><th scope="col">Réinitialisé</th><th scope="col">Conservé</th></tr></thead>
              <tbody>
                <tr><td>Rang de saison</td><td><strong>Votre stash</strong></td></tr>
                <tr><td>Missions saisonnières</td><td><strong>Vos Koen</strong></td></tr>
                <tr><td>Progression saisonnière</td><td><strong>Votre niveau de personnage</strong></td></tr>
                <tr><td>Core Masteries ajoutés en S7 (« reset every season »)</td><td><strong>Vos Bonds</strong></td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Ce que cela change pour votre budget</h3>
            <p>Vous n'avez <strong>aucune raison de vider votre stash</strong> en fin de saison pour « ne pas
            perdre » ce que vous avez. Le risque de perte n'existe que dans les <strong>raids</strong>. Gardez
            votre capital en Koen et en Bonds, et de le dépenser au moment où le rapport valeur/prix est bon.</p>
          </div>

          <h2 id="checklist">6. La checklist des dix derniers jours</h2>
          <ol>
            <li><strong>Relever le niveau de Core Masteries avant le reset.</strong> Les Masteries ajoutés en S7
              se réinitialisent : notez ce que vous avez débloqué, pas ce que vous comptez débloquer.</li>
            <li><strong>Solder les événements avant leur date de fin.</strong> Smelter le 15, Tea Break le 22,
              Halloween le 25, Warlord le 7 décembre : chaque date est une occasion de repartir avec quelque chose
              qui ne reviendra pas.</li>
            <li><strong>Ne pas acheter de Battle Pass hors saison.</strong> Le Pass suit la saison ; un Pass
              acheté en S7 devient caduc à la bascule.</li>
            <li><strong>Conserver les événements saisonniers au lieu de les dépenser.</strong> Les objets de
              collection et tickets d'événement n'ont de valeur qu'avant le reset.</li>
            <li><strong>Préparer le kit post-saison, pas le kit d'aujourd'hui.</strong> La prochaine saison
              rééquilibrera la pénétration, les TTK et les plafonds de tier : n'achetez pas de T6 « au cas où »
              avant d'avoir vu les notes de patch.</li>
            <li><strong>Surveiller les changements de carte.</strong> Les six cartes de base sont stables
              depuis plusieurs saisons, mais chaque saison a déjà modifié une carte. L Airborne Hunt de la
              S4, ou la carte zombie de la S7, montrent que c'est possible.</li>
            <li><strong>Garder une marge de Koen liquide.</strong> Le marché des composants et des armes de
              valeur se réaligne à la sortie de saison : c'est le meilleur moment pour acheter, pas le pire.</li>
          </ol>

          <h2 id="ce-qui-ne-change-pas">7. Ce qui ne changera pas</h2>
          <p>Mieux vaut se rassurer sur ce qui est stable : la structure du jeu d'extraction est fixe depuis
          la sortie complète, et les fondamentaux de la maîtrise s'apprennent une fois pour toutes.</p>
          <ul>
            <li><strong>Six cartes jouables</strong> : Airport, Armory, Farm, Northridge, TV Station et Valley.
              Aucune n'a été retirée depuis la Saison 3.</li>
            <li><strong>Les trois niveaux de raid</strong> : Normal, Lockdown et Forbidden, avec leurs
              plafonds de tier respectifs.</li>
            <li><strong>Le mode PvE à tickets</strong> : No Man's Land reste le mode farm permanent,
              avec sa rotation Farm / Valley / TV Station.</li>
            <li><strong>La règle des clés</strong> : 1 point de clé en Normal, 2 en Lockdown, 3 en Forbidden.
              Ce rapport ne change pas d'une saison à l'autre.</li>
            <li><strong>La structure du loot</strong> : la valeur d'un run se joue sur les rouges, pas sur le
              volume — et le volume est ce que le mode PvE vous apporte.</li>
          </ul>
          <div class="callout callout-danger">
            <h3 class="h4">La seule vraie question à se poser</h3>
            <p>Pas « qu'est-ce que la S8 va changer ? » mais « <strong>ce que je veux optimiser</strong> ».
            Un joueur qui farm en No Man's Land n'a pas le même agenda qu'un joueur qui vise le Forbidden
            Zone. La S8 ne fait que redistribuer les cartes ; elle ne change pas ce que le jeu demande.</p>
          </div>

          <h2 id="faq">8. FAQ</h2>
          <h3 class="h4">La Saison 8 est-elle annoncée&nbsp;?</h3>
          <p>Non. Au 13 novembre 2026, Morefun n'a ni date ni nom. L'estimation de la semaine du 8 au
          14 décembre 2026 repose uniquement sur la durée des trois saisons précédentes. <span class="src-tag src-communautaire">Communautaire</span></p>
          <h3 class="h4">ABI fait-il un wipe comme Tarkov&nbsp;?</h3>
          <p>Non. Ni le stash, ni les Koen, ni le niveau de personnage, ni les Bonds ne sont effacés. Seul
          le classement de saison et les missions saisonnières repartent de zéro. <span class="src-tag src-officiel">Officiel</span></p>
          <h3 class="h4">Puis-je simplement ne rien faire&nbsp;?</h3>
          <p>Oui, et c'est souvent le meilleur choix : un kit cohérent et du Koen liquide valent mieux
          qu'une course aux événements dont les récompenses de saison ne servent plus après le reset.</p>
          <h3 class="h4">Les collectionnables de la S7 perdront-ils toute valeur&nbsp;?</h3>
          <p>Ceux liés aux événements de fin de saison, oui. Les collectionnables permanents et les plans
          d'armes conservent leur valeur. Vérifiez la mention « non restituable » ou « seasonal » sur chaque objet
          avant de, convertir votre Koen.</p>
          <h3 class="h4">Où suivre l'annonce&nbsp;?</h3>
          <p>Dans l'onglet <strong>Actualités</strong> du client, sur les annonces Steam de l'app 2073620,
          et sur les comptes officiels d'ABI Infinite. La première annonce de la saison 4 est venue
          29 jours avant le lancement : c'est votre fenêtre d'anticipation. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="callout callout-success"><h4>Suivre la saison de près</h4><p>Croisez cette pass
          <a href="communaute-patch-notes.html" id="lnk-saison8-attente-002">page des patch notes</a> et
          <a href="events-calendrier.html" id="lnk-saison8-attente-003">le calendrier des événements</a> :
          c'est là que les rééquilibrages et les fins d'événement sont annoncés en premier.</p></div>
        </article>'''

# Remplace l'article d'origine.
# Le builder est idempotent : si la page existe deja et contient les blocs enrichis
# (historique, scenarios, signal a surveiller, deadline), on conserve son <article>
# et on ne met a jour que la coquille (metadonnees, nav, sommaire, pied).
PRESERVE = ('id="scenarios"', 'id="calendrier"', 'id="etat"')
article_src = CONTENT
if OUT.exists():
    prev = OUT.read_text(encoding='utf-8')
    if all(mark in prev for mark in PRESERVE):
        a0 = prev.find('<article class="content-col">')
        a1 = prev.find('</article>', a0)
        if a0 != -1 and a1 != -1:
            article_src = prev[a0:a1 + len('</article>')]
            print('article existant conserve (blocs enrichis detectes)')

start = s.find('        <article class="content-col">')
end = s.find('        </article>', start)
if start < 0 or end < 0:
    raise SystemExit('article introuvable')
s = s[:start] + article_src + s[end + len('        </article>'):]

# ---------- sommaire ----------
toc_items = [('etat', '1. Où en est-on'), ('calendrier', '2. Calendrier officiel'),
             ('scenarios', '3. Les trois scénarios'),
             ('annonce', '4. Comment l\'annonce est faite'), ('compte-a-rebours', '5. Compte à rebours'),
             ('reset', '6. Ce qui se réinitialise'), ('checklist', '7. Checklist des 10 derniers jours'),
             ('ce-qui-ne-change-pas', '8. Ce qui ne change pas'), ('faq', '9. FAQ')]
toc = '\n'.join('<a href="#%s" id="lnk-saison8-attente-%03d">%s</a>' % (a, 100 + i, l)
                for i, (a, l) in enumerate(toc_items))
s = re.sub(r'<aside class="toc" aria-label="Sommaire">.*?</aside>',
           '<aside class="toc" aria-label="Sommaire">\n          <h4>Sommaire</h4>\n%s\n        </aside>' % toc,
           s, flags=re.S)

# ---------- validation JSON-LD ----------
import json as _json
for _m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    try:
        _json.loads(_m.group(1))
    except Exception as _e:
        raise SystemExit('JSON-LD invalide : %s' % _e)

OUT.write_text(s, encoding='utf-8')
print('pages/saison8-attente.html cree : %d caracteres (JSON-LD valide)' % len(s))
