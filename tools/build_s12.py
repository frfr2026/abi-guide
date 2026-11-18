# -*- coding: utf-8 -*-
"""S12 — Génération des 3 pages Lore + intégration à la navigation et au footer."""
import re
import pathlib
import sys

ROOT = pathlib.Path('/home/user/abi-nexus')
PAGES = ROOT / 'pages'

sys.path.insert(0, str(ROOT / 'tools'))
from s12_lore import CONTENT as C_LORE          # noqa: E402
from s12_factions import CONTENT as C_FACTIONS  # noqa: E402
from s12_darkzone import CONTENT as C_DARKZONE  # noqa: E402

BASE = (PAGES / 'guide-debutant.html').read_text(encoding='utf-8')
NAV = re.search(r'<header class="site-nav">.*?</header>', BASE, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', BASE, re.S).group(0)

# ── Bloc de navigation « Univers » ────────────────────────────────────────
def univers_block(prefix: str, active_top: bool = False) -> str:
    def a(h, label):
        return '<a class="nav-link" href="%s%s">%s</a>' % (prefix, h, label)

    top = ('<a class="nav-link active" href="%sunivers-lore.html" aria-current="page">Univers</a>'
           % prefix) if active_top else a('univers-lore.html', 'Univers')
    return """        <div class="has-mega">
          %s
          <div class="mega-menu">
            <div class="mega-col"><h5>Univers de Kamona</h5>
              %s
              %s
              %s
            </div>
            <div class="mega-col"><h5>Sur le terrain</h5>
              %s
              %s
              %s
              %s
            </div>
          </div>
        </div>
""" % (
        top,
        a('univers-lore.html', 'Histoire &amp; chronologie'),
        a('univers-factions.html', 'Factions &amp; personnages'),
        a('univers-dark-zone.html', 'La Dark Zone'),
        a('map-tv-station.html', 'TV Station'),
        a('map-armory.html', 'Armory'),
        a('map-farm.html', 'Farm'),
        a('saison7-utopia.html', 'Utopia (S7)'),
    )


NAV_UNIVERS = NAV.replace(
    '      </nav>\n      <div class="nav-actions">',
    univers_block('') + '      </nav>\n      <div class="nav-actions">')
NAV_UNIVERS_ACTIVE = NAV.replace(
    '<a class="nav-link active" href="guide-debutant.html" aria-current="page">Guides</a>',
    '<a class="nav-link" href="guide-debutant.html">Guides</a>').replace(
    '      </nav>\n      <div class="nav-actions">',
    univers_block('', True) + '      </nav>\n      <div class="nav-actions">')

FOOTER_CLEAN = re.sub(
    r'        <div class="footer-col"><h5>Univers</h5>.*?</div>\n', '', FOOTER, flags=re.S)

FOOTER_UNIVERS = FOOTER_CLEAN.replace(
    '        <div class="footer-col"><h5>Officiel</h5>',
    """        <div class="footer-col"><h5>Univers</h5>
          <a href="univers-lore.html">Histoire de Kamona</a><a href="univers-factions.html">Factions</a>
          <a href="univers-dark-zone.html">La Dark Zone</a><a href="meta-stratégies-s7.html">Stratégies S7</a>
        </div>
        <div class="footer-col"><h5>Officiel</h5>""")

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
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"2026-11-17","dateModified":"2026-11-17","author":{{"@type":"Organization","name":"ABI NEXUS"}},"about":"{{topic}}"}}
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
        <a href="univers-lore.html">Univers</a><span class="sep">/</span>
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


def build(filename, title, desc, og_image, eyebrow, h1, h1_plain, sub, content, toc_items, topic):
    toc = '\n'.join('          <a href="#%s">%s</a>' % (i, l) for i, l in toc_items)
    html = TPL.format(title=title, desc=desc, og_image=og_image, eyebrow=eyebrow,
                      h1=h1, h1_plain=h1_plain, sub=sub, content=content, toc=toc,
                      nav=NAV_UNIVERS_ACTIVE, footer=FOOTER_UNIVERS, topic=topic)
    (PAGES / filename).write_text(html, encoding='utf-8')
    print('OK', filename)


# ── 1. Création des 3 pages ──────────────────────────────────────────────
build(
    'univers-lore.html',
    "L'Univers de Kamona",
    "Histoire complète de Kamona : guerre Nord-Sud, intervention du Comité Sumek, Operation Blackout, fuite d'Utopia, chronologie et mystères non résolus, avec les sources de chaque affirmation.",
    "../img/univers/kamona-island.jpg",
    "Univers — Lore",
    "L'Univers de <strong>Kamona</strong>",
    "L'Univers de Kamona",
    "Une île, deux camps, trois rébellions et un avion qui ne transportait pas de l'aide. Voici l'histoire de Kamona — avec la source de chaque affirmation.",
    C_LORE,
    [('resume', '1. Kamona en bref'),
     ('geographie', '2. La géographie de l\'archipel'),
     ('avant-guerre', '3. Avant la guerre : la fracture'),
     ('guerre', '4. La guerre Nord-Sud'),
     ('sumek', '5. Sumek : la fin officielle'),
     ('blackout', '6. Operation Peacemaker et Blackout'),
     ('darkzone', '7. Naissance de la Dark Zone'),
     ('utopia', '8. Utopia et la Saison 7'),
     ('chronologie', '9. Chronologie'),
     ('mysteres', '10. Mystères non résolus'),
     ('implications', '11. Implications pratiques'),
     ('sources', '12. Sources')],
    "Univers de Kamona")

build(
    'univers-factions.html',
    "Les Factions de Kamona",
    "Toutes les factions de Kamona : Tevilla, Colom, White Wolves, Alpha Team, Blackgold Universal, Abyss Squad, MNST, CDIS, Kamona Liberation Army, Comité Sumek, famille Antonio, Mad Dogs — avec leurs personnages et leurs liens.",
    "../img/univers/blackgold-pmc.jpg",
    "Univers — Factions",
    "Les <strong>factions</strong> de Kamona",
    "Les factions de Kamona",
    "Qui soutient qui, qui se trahit, qui tire les profits. Le dossier complet des forces en présence sur l'archipel.",
    C_FACTIONS,
    [('vue', '1. Vue d\'ensemble'),
     ('puissances', '2. Les deux puissances étrangères'),
     ('locales', '3. Les forces locales'),
     ('pmc', '4. Les entreprises militaires privées'),
     ('neutres', '5. Les acteurs non belligérants'),
     ('criminelles', '6. Les organisations criminelles'),
     ('inconnues', '7. Les factions non confirmées'),
     ('personnages', '8. Les personnages'),
     ('relations', '9. Qui soutient qui'),
     ('boss', '10. Ce que révèlent les boss'),
     ('implications', '11. Implications pratiques'),
     ('sources', '12. Sources')],
    "Factions de Kamona")

build(
    'univers-dark-zone.html',
    "La Dark Zone",
    "La Dark Zone de Kamona : définition, modes Normal / Lockdown / Forbidden, Tac Ops et Covert Ops, nœuds de la Dark Zone par carte, impact d'Utopia en S7, règles non écrites et implications pratiques.",
    "../img/univers/dark-zone.jpg",
    "Univers — Dark Zone",
    "La <strong>Dark Zone</strong>",
    "La Dark Zone",
    "Le territoire sans loi de Kamona : ce que le lore y Cache, ce que le jeu y mesure, et comment en tirer parti.",
    C_DARKZONE,
    [('definition', '1. Qu\'est-ce que la Dark Zone ?'),
     ('modes', '2. Les trois modes'),
     ('origines', '3. Tac Ops, Covert Ops, pionniers'),
     ('cartes', '4. Les nœuds de la Dark Zone'),
     ('commite', '5. Le Comité Sumek sur le terrain'),
     ('utopia', '6. Utopia : la nouvelle couche'),
     ('regles', '7. Les lois non écrites'),
     ('implications', '8. Implications pratiques'),
     ('mysteres', '9. Ce qui reste inexpliqué'),
     ('sources', '10. Sources')],
    "Dark Zone de Kamona")

# ── 2. Ajout de l'entrée « Univers » dans la navigation de toutes les pages ──
NEW_PAGES = {'univers-lore.html', 'univers-factions.html', 'univers-dark-zone.html'}
count = 0
for f in sorted(PAGES.glob('*.html')):
    if f.name in NEW_PAGES:
        continue
    s = f.read_text(encoding='utf-8')
    if 'univers-lore.html' in s:
        continue
    anchor = '      </nav>\n      <div class="nav-actions">'
    if anchor not in s:
        print('!! ancre nav introuvable :', f.name)
        continue
    s = s.replace(anchor, univers_block('') + anchor, 1)
    f.write_text(s, encoding='utf-8')
    count += 1
print('Navigation mise a jour :', count, 'pages')

# ── 3. Footer : colonne « Univers » sur toutes les pages ─────────────────
count = 0
for f in sorted(PAGES.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    if '<h5>Univers</h5>' in s:
        continue
    anchor = '        <div class="footer-col"><h5>Officiel</h5>'
    if anchor not in s:
        print('!! ancre footer introuvable :', f.name)
        continue
    block = """        <div class="footer-col"><h5>Univers</h5>
          <a href="univers-lore.html">Histoire de Kamona</a><a href="univers-factions.html">Factions</a>
          <a href="univers-dark-zone.html">La Dark Zone</a><a href="meta-stratégies-s7.html">Stratégies S7</a>
        </div>
"""
    s = s.replace(anchor, block + anchor, 1)
    f.write_text(s, encoding='utf-8')
    count += 1
print('Footer mis a jour :', count, 'pages')

# ── 4. index.html : nav + footer ───────────────────────────────────────────
idx = ROOT / 'index.html'
s = idx.read_text(encoding='utf-8')
if 'pages/univers-lore.html' not in s:
    anchor = '      </nav>\n      <div class="nav-actions">'
    s = s.replace(anchor, univers_block('pages/') + anchor, 1)
if '<h5>Univers</h5>' not in s:
    anchor = '        <div class="footer-col"><h5>Officiel</h5>'
    block = """        <div class="footer-col"><h5>Univers</h5>
          <a href="pages/univers-lore.html">Histoire de Kamona</a><a href="pages/univers-factions.html">Factions</a>
          <a href="pages/univers-dark-zone.html">La Dark Zone</a><a href="pages/meta-stratégies-s7.html">Stratégies S7</a>
        </div>
"""
    s = s.replace(anchor, block + anchor, 1)
idx.write_text(s, encoding='utf-8')
print('index.html mis a jour')

# ── 5. CSS : footer a 6 colonnes ──────────────────────────────────────────
css = ROOT / 'css' / 'main.css'
c = css.read_text(encoding='utf-8')
if '1.4fr repeat(5, 1fr)' not in c:
    c = c.replace('grid-template-columns: 1.4fr 1fr 1fr 1fr 1fr;',
                  'grid-template-columns: 1.4fr repeat(5, 1fr);')
    css.write_text(c, encoding='utf-8')
    print('CSS footer mis a jour')

resp = ROOT / 'css' / 'responsive.css'
r = resp.read_text(encoding='utf-8')
if '.footer-grid { grid-template-columns: repeat(3, 1fr); }' not in r:
    r = r.replace("""@media (max-width: 1250px) and (min-width: 769px) {
  .nav-links { gap: var(--space-sm); }""",
"""@media (max-width: 1250px) and (min-width: 769px) {
  .footer-grid { grid-template-columns: repeat(3, 1fr); }
  .nav-links { gap: var(--space-sm); }""")
    resp.write_text(r, encoding='utf-8')
    print('CSS responsive mis a jour')

# ── 6. manifest.json : start_url / scope racine ───────────────────────────
mf = ROOT / 'manifest.json'
m = mf.read_text(encoding='utf-8')
m = m.replace('"start_url": "../index.html"', '"start_url": "./index.html"')
m = m.replace('"scope": "../"', '"scope": "./"')
mf.write_text(m, encoding='utf-8')
print('manifest.json corrige')
