# -*- coding: utf-8 -*-
"""S13 — Génération des 3 pages Événements + intégration navigation/footer."""
import re
import pathlib
import sys

ROOT = pathlib.Path('/home/user/abi-nexus')
PAGES = ROOT / 'pages'

sys.path.insert(0, str(ROOT / 'tools'))
from s13_calendrier import CONTENT as C_CAL       # noqa: E402
from s13_supplies import CONTENT as C_SUPPLIES     # noqa: E402
from s13_warlord import CONTENT as C_WARLORD       # noqa: E402

BASE = (PAGES / 'guide-debutant.html').read_text(encoding='utf-8')
# Le template de base peut déjà contenir les blocs S13 (run précédent) : on les retire.
BASE = re.sub(r'[ \t]*<!--S13-NAV-->.*?<!--/S13-NAV-->\n?', '', BASE, flags=re.S)
BASE = re.sub(r'[ \t]*<!--S13-FOOTER-->.*?<!--/S13-FOOTER-->\n?', '', BASE, flags=re.S)
NAV = re.search(r'<header class="site-nav">.*?</header>', BASE, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', BASE, re.S).group(0)

NAV_END = '      </nav>\n      <div class="nav-actions">'
FOOTER_ANCHOR = '        <div class="footer-col"><h5>Officiel</h5>'

# ── Bloc de navigation « Événements » ─────────────────────────────────────
def evm_block(prefix: str, active: bool = False) -> str:
    def a(h, label):
        return '<a href="%s%s">%s</a>' % (prefix, h, label)

    top = ('<a class="nav-link active" href="%sevents-calendrier.html" aria-current="page">Événements</a>'
           % prefix) if active else ('<a class="nav-link" href="%sevents-calendrier.html">Événements</a>' % prefix)

    return """        <!--S13-NAV-->
        <div class="has-mega">
          %s
          <div class="mega-menu">
            <div class="mega-col"><h5>Saison 7 : Utopia</h5>
              %s
              %s
              %s
            </div>
            <div class="mega-col"><h5>Événements majeurs</h5>
              %s
              %s
              %s
            </div>
          </div>
        </div>
        <!--/S13-NAV-->
""" % (
        top,
        a('events-calendrier.html', 'Calendrier &amp; échéances'),
        a('events-supplies-drops.html', 'Supply Drops 2.0'),
        a('events-warlord-tournament.html', 'Warlord Tournament III'),
        a('saison7-utopia.html', 'Utopia (S7)'),
        a('saison7-battle-pass.html', 'Battle Pass S7'),
        a('saison7-zombie-infected-zone.html', 'Infected Zone'),
    )


def strip_nav(path: pathlib.Path) -> str:
    """Retire le bloc Events (marqueur) et renvoie le contenu nettoye."""
    s = path.read_text(encoding='utf-8')
    s = re.sub(r'[ \t]*<!--S13-NAV-->.*?<!--/S13-NAV-->\n?', '', s, flags=re.S)
    return s


def strip_footer(path: pathlib.Path) -> str:
    s = path.read_text(encoding='utf-8')
    s = re.sub(r'[ \t]*<!--S13-FOOTER-->.*?<!--/S13-FOOTER-->\n?', '', s, flags=re.S)
    return s


FOOTER_EVT_BLOCK = """        <!--S13-FOOTER-->
        <div class="footer-col"><h5>Événements</h5>
          <a href="events-calendrier.html">Calendrier S7</a><a href="events-supplies-drops.html">Supply Drops 2.0</a>
          <a href="events-warlord-tournament.html">Warlord Tournament III</a><a href="meta-stratégies-s7.html">Stratégies S7</a>
        </div>
        <!--/S13-FOOTER-->
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
        <a href="events-calendrier.html">Événements</a><span class="sep">/</span>
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
    # Le bloc S13 doit précéder un éventuel bloc S14 pour garder un ordre stable.
    anchor = '        <!--S14-NAV-->\n' if '        <!--S14-NAV-->\n' in nav else NAV_END
    return nav.replace(anchor, evm_block('', active) + anchor, 1)


def footer_for() -> str:
    return FOOTER.replace(FOOTER_ANCHOR, FOOTER_EVT_BLOCK + FOOTER_ANCHOR)


def build(filename, title, desc, og_image, eyebrow, h1, h1_plain, sub, content, toc_items, topic):
    toc = '\n'.join('          <a href="#%s">%s</a>' % (i, l) for i, l in toc_items)
    html = TPL.format(title=title, desc=desc, og_image=og_image, eyebrow=eyebrow,
                      h1=h1, h1_plain=h1_plain, sub=sub, content=content, toc=toc,
                      nav=nav_for(True), footer=footer_for(), topic=topic)
    (PAGES / filename).write_text(html, encoding='utf-8')
    print('OK', filename)


# ── 1. Création des 3 pages ──────────────────────────────────────────────
build(
    'events-calendrier.html',
    'Calendrier des événements — Saison 7',
    "Calendrier complet des événements d’Arena Breakout: Infinite en Saison 7 Utopia : échéances, festivals, pistes hebdomadaires, modes événementiels, statut live au 17 novembre 2026 et plan d’action.",
    "../img/events/loot-fest-arena.jpg",
    "Événements — Saison 7 : Utopia",
    "Le calendrier des <strong>événements</strong>",
    "Le calendrier des événements",
    "Six catégories d’événements, douze pistes, cinq échéances : ce qui est encore ouvert le 17 novembre 2026, ce qui ferme en premier, et ce qu’il faut faire dans quel ordre.",
    C_CAL,
    [('statut', '1. Où en est la Saison 7 au 17 novembre'),
     ('principes', '2. Comment fonctionnent les événements'),
     ('echeances', '3. Toutes les échéances de la Saison 7'),
     ('festival', '4. Le festival d’automne'),
     ('halloween', '5. Mysterious Pumpkin Night'),
     ('novembre', '6. Les événements de novembre'),
     ('modes', '7. Les modes événementiels'),
     ('biohazard', '8. La série Biohazard'),
     ('saison8', '9. Et la Saison 8 ?'),
     ('planification', '10. Plan d’action recommandé'),
     ('sources', '11. Sources')],
    "Événements d'Arena Breakout: Infinite en Saison 7")

build(
    'events-supplies-drops.html',
    'Supply Drops 2.0 & modes événementiels',
    "Supply Drops 2.0 en détail : caisse de récompense à 5 niveaux, terminaux standard et confidentiel, Smelter illimité au niveau 3, stratégie d’équipe, Trash to Treasure et modes infectés de la Saison 7.",
    "../img/events/supply-drops-airdrop.jpg",
    "Événements — Modes événementiels",
    "<strong>Supply Drops 2.0</strong> &amp; co",
    "Supply Drops 2.0 & modes événementiels",
    "Le mode où votre stuff n’est pas en jeu : la caisse à cinq niveaux, les deux types de terminaux, le Smelter, et la stratégie d’équipe qui va avec.",
    C_SUPPLIES,
    [('mode', '1. Supply Drops 2.0 en bref'),
     ('crate', '2. La caisse de récompense : cinq niveaux'),
     ('terminals', '3. Les deux types de terminaux'),
     ('smelter', '4. Le Smelter'),
     ('airdrop', '5. Airdrops, IA blindée et rythme'),
     ('strategie', '6. Stratégie d’équipe'),
     ('erreurs', '7. Les erreurs qui coûtent le plus cher'),
     ('trash', '8. Trash to Treasure'),
     ('biohazard-modes', '9. Les modes infectés de la S7'),
     ('merit', '10. Ce que le mode rapporte vraiment'),
     ('sources', '11. Sources')],
    "Supply Drops 2.0 et modes événementiels d'Arena Breakout: Infinite")

build(
    'events-warlord-tournament.html',
    'Warlord Tournament III & événements saisonniers',
    "Troisième Warlord Tournament : rangs, récompenses, scoring par valeur de loot, fichier chiffré multiplicateur, dog tags. Plus Mysterious Pumpkin Night, Dim Dou Duk Gourmet Market et Kamona Investigation Tea Break Delights.",
    "../img/events/warlord-tournament.jpg",
    "Événements — Tournois & saisonniers",
    "<strong>Warlord Tournament III</strong> &amp; co",
    "Warlord Tournament III & événements saisonniers",
    "Le classement le plus competitive du jeu, le fichier chiffré qui vous trahit, la citrouille qui vaut 880 000 Koen et l’enquête qui ferme le 22 novembre.",
    C_WARLORD,
    [('warlord', '1. Le Troisième Warlord Tournament'),
     ('ranks', '2. Rangs et récompenses'),
     ('scoring', '3. Le scoring : cinq règles'),
     ('encrypted', '4. Le fichier chiffré'),
     ('dogtags', '5. Les dog tags'),
     ('entree', '6. Les conditions d’entrée'),
     ('monter', '7. Comment monter plus vite'),
     ('halloween', '8. Mysterious Pumpkin Night'),
     ('pumpkin', '9. L’évolution des citrouilles'),
     ('messengers', '10. Les Pumpkin Messengers'),
     ('corrupted', '11. Corrupted Treasures'),
     ('gourmet', '12. Dim Dou Duk Gourmet Market'),
     ('investigation', '13. Kamona Investigation'),
     ('stack', '14. Empiler les événements'),
     ('sources', '15. Sources')],
    "Warlord Tournament III et événements saisonniers d'Arena Breakout: Infinite")

# ── 2. Navigation : ajout du bloc Événements sur toutes les pages ─────────
NEW_PAGES = {'events-calendrier.html', 'events-supplies-drops.html', 'events-warlord-tournament.html'}
# Si un bloc S14 (Communauté) est déjà présent, le bloc S13 doit être inséré AVANT lui
# pour garder un ordre stable : Événements puis Communauté.
S14_MARK = '        <!--S14-NAV-->\n'
count = 0
for f in sorted(PAGES.glob('*.html')):
    if f.name in NEW_PAGES:
        continue
    s = strip_nav(f)
    anchor = S14_MARK if S14_MARK in s else NAV_END
    if anchor not in s:
        print('!! ancre nav introuvable :', f.name)
        continue
    s = s.replace(anchor, evm_block('') + anchor, 1)
    f.write_text(s, encoding='utf-8')
    count += 1
print('Navigation mise a jour :', count, 'pages')

# ── 3. Footer : colonne « Événements » sur toutes les pages ──────────────
count = 0
for f in sorted(PAGES.glob('*.html')):
    if f.name in NEW_PAGES:
        continue
    s = strip_footer(f)
    if FOOTER_ANCHOR not in s:
        print('!! ancre footer introuvable :', f.name)
        continue
    s = s.replace(FOOTER_ANCHOR, FOOTER_EVT_BLOCK + FOOTER_ANCHOR, 1)
    f.write_text(s, encoding='utf-8')
    count += 1
print('Footer mis a jour :', count, 'pages')

# ── 4. index.html : nav + footer ─────────────────────────────────────────
idx = ROOT / 'index.html'
s = idx.read_text(encoding='utf-8')
s = re.sub(r'[ \t]*<!--S13-NAV-->.*?<!--/S13-NAV-->\n?', '', s, flags=re.S)
s = re.sub(r'[ \t]*<!--S13-FOOTER-->.*?<!--/S13-FOOTER-->\n?', '', s, flags=re.S)
if NAV_END in s:
    s = s.replace(NAV_END, evm_block('pages/') + NAV_END, 1)
else:
    print('!! ancre nav introuvable : index.html')
if FOOTER_ANCHOR in s:
    s = s.replace(FOOTER_ANCHOR, FOOTER_EVT_BLOCK.replace('href="events-', 'href="pages/events-')
                  .replace('href="meta-', 'href="pages/meta-') + FOOTER_ANCHOR, 1)
else:
    print('!! ancre footer introuvable : index.html')
idx.write_text(s, encoding='utf-8')
print('index.html mis a jour')

# ── 5. CSS : footer a 7 colonnes ─────────────────────────────────────────
css = ROOT / 'css' / 'main.css'
c = css.read_text(encoding='utf-8')
if '1.4fr repeat(6, 1fr)' not in c:
    c = c.replace('grid-template-columns: 1.4fr repeat(5, 1fr);',
                  'grid-template-columns: 1.4fr repeat(6, 1fr);')
    css.write_text(c, encoding='utf-8')
    print('CSS footer mis a jour')
