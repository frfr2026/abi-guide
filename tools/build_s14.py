# -*- coding: utf-8 -*-
"""S14 — Génération des 3 pages Communauté + intégration navigation/footer."""
import re
import pathlib
import sys

ROOT = pathlib.Path('/home/user/abi-nexus')
PAGES = ROOT / 'pages'

sys.path.insert(0, str(ROOT / 'tools'))
from s14_ressources import CONTENT as C_RESSOURCES   # noqa: E402
from s14_streamers import CONTENT as C_STREAMERS     # noqa: E402
from s14_patchnotes import CONTENT as C_PATCHNOTES   # noqa: E402

BASE = (PAGES / 'guide-debutant.html').read_text(encoding='utf-8')
# On ne retire QUE les blocs S14 : les blocs S13 (Événements) doivent être conservés
# afin que les nouvelles pages héritent des deux méga-menus.
BASE = re.sub(r'[ \t]*<!--S14-NAV-->.*?<!--/S14-NAV-->\n?', '', BASE, flags=re.S)
BASE = re.sub(r'[ \t]*<!--S14-FOOTER-->.*?<!--/S14-FOOTER-->\n?', '', BASE, flags=re.S)
NAV = re.search(r'<header class="site-nav">.*?</header>', BASE, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', BASE, re.S).group(0)

NAV_END = '      </nav>\n      <div class="nav-actions">'
FOOTER_ANCHOR = '        <div class="footer-col"><h5>Officiel</h5>'


def com_block(prefix: str, active: bool = False) -> str:
    def a(h, label):
        return '<a href="%s%s">%s</a>' % (prefix, h, label)

    top = ('<a class="nav-link active" href="%scommunaute-ressources.html" aria-current="page">Communauté</a>'
           % prefix) if active else ('<a class="nav-link" href="%scommunaute-ressources.html">Communauté</a>' % prefix)

    return """        <!--S14-NAV-->
        <div class="has-mega">
          %s
          <div class="mega-menu">
            <div class="mega-col"><h5>Ressources</h5>
              %s
              %s
              %s
            </div>
            <div class="mega-col"><h5>Créateurs &amp; Patch notes</h5>
              %s
              %s
              %s
            </div>
          </div>
        </div>
        <!--/S14-NAV-->
""" % (
        top,
        a('communaute-ressources.html', 'Ressources communautaires'),
        a('communaute-patch-notes.html', 'Patch notes &amp; mises à jour'),
        a('communaute-streamers.html', 'Streamers &amp; créateurs'),
        a('meta-stratégies-s7.html', 'Stratégies S7'),
        a('saison7-utopia.html', 'Utopia (S7)'),
        a('guide-craft.html', 'Craft &amp; Workbench'),
    )


FOOTER_COM_BLOCK = """        <!--S14-FOOTER-->
        <div class="footer-col"><h5>Communauté</h5>
          <a href="communaute-ressources.html">Ressources</a><a href="communaute-streamers.html">Streamers</a>
          <a href="communaute-patch-notes.html">Patch notes</a><a href="meta-stratégies-s7.html">Stratégies S7</a>
        </div>
        <!--/S14-FOOTER-->
"""

TPL = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ABI NEXUS</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title} — ABI NEXUS">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="{og_image}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@400;500;600;700&family=Exo+2:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/main.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <link rel="icon" type="image/jpeg" sizes="64x64" href="../img/ui/favicon-64.jpg">
  <link rel="apple-touch-icon" href="../img/ui/favicon-180.jpg">
  <link rel="manifest" href="../manifest.json">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"2026-11-17","dateModified":"2026-11-17","author":{{"@type":"Organization","name":"ABI NEXUS"}},"about":"{topic}"}}
  </script>
</head>
<body>
  <a class="skip-link" href="#contenu">Aller au contenu</a>
  <div class="progress-bar" aria-hidden="true"></div>

  {nav}

  <main id="contenu" class="section">
    <div class="container">
      <nav class="breadcrumb" aria-label="Fil d'Ariane">
        <a href="../index.html">Accueil</a><span class="sep">/</span>
        <a href="communaute-ressources.html">Communauté</a><span class="sep">/</span>
        <span aria-current="page">{h1_plain}</span>
      </nav>

      <header class="page-head">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="page-sub">{sub}</p>
      </header>

      <div class="page-layout">
        <article class="content-col">
{content}
        </article>
        <aside class="toc" aria-label="Sommaire">
          <h4>Sommaire</h4>
{toc}
        </aside>
      </div>
    </div>
  </main>

  {footer}

  <div class="audio-player" data-track="../audio/ambiance-menu.mp3" data-label="Briefing">
    <button aria-label="Lecture / Pause du briefing"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
    <span class="audio-label">Briefing</span>
    <input type="range" min="0" max="1" step="0.05" value="0.5" aria-label="Volume">
  </div>
  <button class="back-to-top" aria-label="Retour en haut"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M6 11l6-6 6 6"/></svg></button>

  <script src="../js/navigation.js" defer></script>
  <script src="../js/main.js" defer></script>
</body>
</html>
"""


def nav_for(active: bool) -> str:
    nav = NAV.replace(
        '<a class="nav-link active" href="guide-debutant.html" aria-current="page">Guides</a>',
        '<a class="nav-link" href="guide-debutant.html">Guides</a>')
    return nav.replace(NAV_END, com_block('', active) + NAV_END)


def footer_for() -> str:
    return FOOTER.replace(FOOTER_ANCHOR, FOOTER_COM_BLOCK + FOOTER_ANCHOR)


def build(filename, title, desc, og_image, eyebrow, h1, h1_plain, sub, content, toc_items, topic):
    toc = '\n'.join('          <a href="#%s">%s</a>' % (i, l) for i, l in toc_items)
    html = TPL.format(title=title, desc=desc, og_image=og_image, eyebrow=eyebrow,
                      h1=h1, h1_plain=h1_plain, sub=sub, content=content, toc=toc,
                      nav=nav_for(True), footer=footer_for(), topic=topic)
    (PAGES / filename).write_text(html, encoding='utf-8')
    print('OK', filename)


# ── 1. Création des 3 pages ──────────────────────────────────────────────
build(
    'communaute-ressources.html',
    'Ressources communautaires — Discord, Reddit, bases de données',
    "Toutes les ressources communautaires d’Arena Breakout: Infinite : Discord officiel et serveurs régionaux, subreddit et ses règles, bases de données versionnées par patch, outils open source GitHub, programme Mentor et Inspector Community, et méthode de croisement des sources.",
    "../img/communaute/discord-voice.jpg",
    "Communauté — Ressources",
    "Les <strong>ressources</strong> communautaires",
    "Les ressources communautaires",
    "Discord, Reddit, bases de données, GitHub, mentorat, inspection : où se trouve l’information fiable — et comment ne pas se faire avoir.",
    C_RESSOURCES,
    [('reperes', '1. La règle d’or'),
     ('discord', '2. Le Discord et les régions'),
     ('reddit', '3. Reddit : règles et fils'),
     ('wikis', '4. Les bases de données'),
     ('outils', '5. Les outils communautaires'),
     ('github', '6. Les projets open source'),
     ('phishing', '7. Sécurité : les pièges'),
     ('mentor', '8. Le programme Mentor'),
     ('inspector', '9. L’Inspector Community'),
     ('methodo', '10. Méthode de croisement'),
     ('sources', '11. Sources')],
    "Ressources communautaires d'Arena Breakout: Infinite")

build(
    'communaute-streamers.html',
    'Streamers & créateurs — Twitch, événements sponsorisés, Twitch Drops',
    "Les streamers et créateurs d’Arena Breakout: Infinite : chaîne Twitch officielle, événements sponsorisés (KCD Edge 30 000 $, 48H Global Clash, Pumpkin Party), Twitch Drops, créateurs recommandés par la communauté, scènes par langue et risques du chase de giveaways.",
    "../img/communaute/tournament-broadcast.jpg",
    "Communauté — Créateurs",
    "<strong>Streamers</strong> &amp; créateurs",
    "Streamers & créateurs",
    "Les événements sponsorisés, les Twitch Drops et les créateurs que la communauté recommande — avec la liste des pièges à éviter.",
    C_STREAMERS,
    [('officiel', '1. Les canaux officiels'),
     ('events', '2. Les événements sponsorisés'),
     ('drops', '3. Les Twitch Drops'),
     ('creators', '4. Les créateurs à suivre'),
     ('top-streamers', '5. Les plus regardés'),
     ('langues', '6. Les communautés par langue'),
     ('debuter', '7. Comment s’y prendre'),
     ('avertissement', '8. Ce qu’il ne faut pas suivre'),
     ('sources', '9. Sources')],
    "Streamers et createurs d'Arena Breakout: Infinite")

build(
    'communaute-patch-notes.html',
    'Patch notes & mises à jour — Seasons 7, live updates, sécurité',
    "Où lire les notes de patch officielles d’Arena Breakout: Infinite, les miroirs et agrégateurs, le détail complet de la mise à jour Saison 7 Utopia, le format des Live Updates, les rapports de sécurité B.D.C. et la méthode de lecture d’une note de patch.",
    "../img/communaute/patch-notes.jpg",
    "Communauté — Mises à jour",
    "<strong>Patch notes</strong> &amp; mises à jour",
    "Patch notes & mises à jour",
    "La source primaire, les miroirs utiles, ce que la Saison 7 a réellement changé, et les chiffres de l’anti-triche que personne ne lit.",
    C_PATCHNOTES,
    [('ou', '1. Où lire les notes officielles'),
     ('trackers', '2. Les miroirs'),
     ('s7', '3. Ce que la Saison 7 a changé'),
     ('live', '4. Le format des Live Updates'),
     ('securite', '5. Les rapports de sécurité'),
     ('lire', '6. Lire une note en dix minutes'),
     ('historique', '7. Chronologie des mises à jour'),
     ('sources', '8. Sources')],
    "Patch notes et mises a jour d'Arena Breakout: Infinite")

# ── 2. Navigation : ajout du bloc Communauté sur toutes les pages ─────────
NEW_PAGES = {'communaute-ressources.html', 'communaute-streamers.html', 'communaute-patch-notes.html'}
count = 0
for f in sorted(PAGES.glob('*.html')):
    if f.name in NEW_PAGES:
        continue
    s = f.read_text(encoding='utf-8')
    s = re.sub(r'[ \t]*<!--S14-NAV-->.*?<!--/S14-NAV-->\n?', '', s, flags=re.S)
    if NAV_END not in s:
        print('!! ancre nav introuvable :', f.name)
        continue
    s = s.replace(NAV_END, com_block('') + NAV_END, 1)
    f.write_text(s, encoding='utf-8')
    count += 1
print('Navigation mise a jour :', count, 'pages')

# ── 3. Footer : colonne « Communauté » sur toutes les pages ─────────────
count = 0
for f in sorted(PAGES.glob('*.html')):
    if f.name in NEW_PAGES:
        continue
    s = f.read_text(encoding='utf-8')
    s = re.sub(r'[ \t]*<!--S14-FOOTER-->.*?<!--/S14-FOOTER-->\n?', '', s, flags=re.S)
    if FOOTER_ANCHOR not in s:
        print('!! ancre footer introuvable :', f.name)
        continue
    s = s.replace(FOOTER_ANCHOR, FOOTER_COM_BLOCK + FOOTER_ANCHOR, 1)
    f.write_text(s, encoding='utf-8')
    count += 1
print('Footer mis a jour :', count, 'pages')

# ── 4. index.html : nav + footer ─────────────────────────────────────────
idx = ROOT / 'index.html'
s = idx.read_text(encoding='utf-8')
s = re.sub(r'[ \t]*<!--S14-NAV-->.*?<!--/S14-NAV-->\n?', '', s, flags=re.S)
s = re.sub(r'[ \t]*<!--S14-FOOTER-->.*?<!--/S14-FOOTER-->\n?', '', s, flags=re.S)
if NAV_END in s:
    s = s.replace(NAV_END, com_block('pages/') + NAV_END, 1)
else:
    print('!! ancre nav introuvable : index.html')
if FOOTER_ANCHOR in s:
    s = s.replace(FOOTER_ANCHOR, FOOTER_COM_BLOCK.replace('href="communaute-', 'href="pages/communaute-')
                  .replace('href="meta-', 'href="pages/meta-') + FOOTER_ANCHOR, 1)
else:
    print('!! ancre footer introuvable : index.html')
idx.write_text(s, encoding='utf-8')
print('index.html mis a jour')

# ── 5. CSS : footer a 8 colonnes ─────────────────────────────────────────
css = ROOT / 'css' / 'main.css'
c = css.read_text(encoding='utf-8')
if '1.4fr repeat(7, 1fr)' not in c:
    c = c.replace('grid-template-columns: 1.4fr repeat(6, 1fr);',
                  'grid-template-columns: 1.4fr repeat(7, 1fr);')
    css.write_text(c, encoding='utf-8')
    print('CSS footer mis a jour')
