"""ABI NEXUS — micro-générateur de pages (coquille commune)."""
import re, pathlib

PAGE_DIR = pathlib.Path('/home/user/abi-nexus/pages')
_base = (PAGE_DIR / 'guide-debutant.html').read_text(encoding='utf-8')
_nav = re.search(r'<header class="site-nav">.*?</header>', _base, re.S).group(0)
_footer = re.search(r'<footer class="site-footer">.*?</footer>', _base, re.S).group(0)

NAV_ARMES = (_nav
    .replace('<a class="nav-link active" href="guide-debutant.html" aria-current="page">Guides</a>',
             '<a class="nav-link" href="guide-debutant.html">Guides</a>')
    .replace('<a class="nav-link" href="armes-fusils-assaut.html">Armes</a>',
             '<a class="nav-link active" href="armes-fusils-assaut.html" aria-current="page">Armes</a>'))

def page(filename, title, desc, og_image, eyebrow, h1, sub, content, toc_items, extra_js=True, nav=NAV_ARMES, crumb=('Armes', 'armes-tier-list.html')):
    toc = '\n'.join(f'<a href="#{i}">{l}</a>' for i, l in toc_items)
    js_weapons = ('\n  <script src="../js/weapons.js" defer></script>' if extra_js is True else
                  ('\n  <script src="../js/armors.js" defer></script>' if extra_js == 'armors' else
                   ('\n  <script src="../js/items.js" defer></script>' if extra_js == 'items' else
                    ('\n  <script src="../js/optimizer.js" defer></script>' if extra_js == 'optimizer' else ''))))
    html = f"""<!DOCTYPE html>
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
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"2026-09-26","dateModified":"2026-11-17","author":{{"@type":"Organization","name":"ABI NEXUS"}}}}
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
        <a href="{crumb[1]}">{crumb[0]}</a><span class="sep">/</span>
        <span aria-current="page">{h1_plain(h1)}</span>
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

  {_footer}

  <div class="audio-player" data-track="../audio/ambiance-menu.mp3" data-label="Briefing">
    <button aria-label="Lecture / Pause du briefing"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
    <span class="audio-label">Briefing</span>
    <input type="range" min="0" max="1" step="0.05" value="0.5" aria-label="Volume">
  </div>
  <button class="back-to-top" aria-label="Retour en haut"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M6 11l6-6 6 6"/></svg></button>

  <script src="../js/navigation.js" defer></script>
  <script src="../js/main.js" defer></script>{js_weapons}
</body>
</html>
"""
    (PAGE_DIR / filename).write_text(html, encoding='utf-8')
    print('OK', filename)

def h1_plain(h1):
    return re.sub(r'<[^>]+>', ' ', h1).replace('\n', ' ').strip()

def build_nav(active):
    """Renvoie le header avec la section active basculee ('Guides' | 'Armes' | 'Equipement' | 'Cartes' | 'Saison 7' | 'Tier List')."""
    n = _nav.replace(
        '<a class="nav-link active" href="guide-debutant.html" aria-current="page">Guides</a>',
        '<a class="nav-link" href="guide-debutant.html">Guides</a>')
    targets = {
        'Guides': ('guide-debutant.html', 'Guides'),
        'Armes': ('armes-fusils-assaut.html', 'Armes'),
        'Équipement': ('equipement-armures.html', 'Équipement'),
        'Cartes': ('map-farm.html', 'Cartes'),
        'Saison 7': ('saison7-utopia.html', 'Saison 7'),
        'Objets': ('items-munitions.html', 'Objets'),
        'Méta': ('meta-tier-list-globale.html', 'Méta'),
    }
    h, label = targets[active]
    old_link = '<a class="nav-link" href="' + h + '"'
    new_link = '<a class="nav-link active" href="' + h + '" aria-current="page"'
    n = n.replace(old_link, new_link, 1)
    return n