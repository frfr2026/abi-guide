#!/usr/bin/env python3
"""ABI NEXUS — build_s16_files.py : fichiers racine du site (S16).

Produit :
  • sitemap.xml     — 64 URL indexables, <loc> + <lastmod> W3C (pas de
                      priority/changefreq : Google les ignore) ;
  • robots.txt      — regles d'exploration, crawlers IA traites a part,
                      directive Sitemap absolute ;
  • 404.html        — page d'erreur personnalisee (navigation globale
                      conservee, recherche, raccourcis) ;
  • manifest.json   — manifeste PWA mis a jour (icones JPG, raccourcis).

Usage : python3 tools/build_s16_files.py
"""
import pathlib, re, json, sys, os, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import seo_config as C  # noqa: E402

TZ = datetime.timezone(datetime.timedelta(hours=1))  # Europe/Paris (CET, novembre)


# ════════════════════════════════════════════════════════════════
#  sitemap.xml
# ════════════════════════════════════════════════════════════════
def build_sitemap():
    targets = [ROOT / C.ROOT_INDEX] + sorted((ROOT / C.PAGES_DIR).glob('*.html'))
    entries = []
    for f in targets:
        rel = str(f.relative_to(ROOT))
        if f.name in C.SITEMAP_EXCLUDE:
            continue
        mtime = datetime.datetime.fromtimestamp(f.stat().st_mtime, TZ)
        # W3C Datetime avec decalage horaire explicite : seule forme
        # acceptee par le schema officiel du protocole sitemaps.
        stamp = mtime.replace(microsecond=0).isoformat()
        entries.append((C.page_url(rel), stamp, rel))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<!-- Sitemap ABI NEXUS — Guide Arena Breakout Infinite -->')
    lines.append('<!-- %d URL indexables. Ni <priority> ni <changefreq> : Google ignore ces deux balises. -->' % len(entries))
    lines.append('<!-- <lastmod> reflete la derniere modification reelle du fichier (mtime). -->')
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for loc, stamp, rel in entries:
        lines.append('  <url>')
        lines.append('    <loc>%s</loc>' % loc)
        lines.append('    <lastmod>%s</lastmod>' % stamp)
        lines.append('  </url>')
    lines.append('</urlset>')
    (ROOT / 'sitemap.xml').write_text("\n".join(lines) + "\n", encoding='utf-8')
    return len(entries)


# ════════════════════════════════════════════════════════════════
#  robots.txt
# ════════════════════════════════════════════════════════════════
def build_robots():
    L = []
    L.append('# robots.txt — ABI NEXUS — Guide Arena Breakout Infinite')
    L.append('# Mis a jour le %s' % C.CONTENT_DATE)
    L.append('#')
    L.append('# Regle de base : robots.txt controle l\'exploration, pas l\'indexation.')
    L.append('# Pour desinterdire une page de l\'index, il faut une balise meta robots=noindex')
    L.append('# sur une page que le robot peut au contraire lire.')
    L.append('#')
    L.append('# Les robots de recherche classiques (Googlebot, Bingbot) sont autorises :')
    L.append('# le guide doit etre trouvable et citable.')
    L.append('# Les robots d\'entrainement IA sont bloques : le contenu reste cite')
    L.append('# (PerplexityBot, AI Overviews) mais n\'alimente pas les corpus d\'entrainement.')
    L.append('# Pour inverser ce choix, editez tools/seo_config.py puis relancez ce script.')
    L.append('')
    L.append('User-agent: *')
    L.append('Allow: /')
    L.append('Disallow: /tools/')
    L.append('Disallow: /backup/')
    L.append('')
    L.append('# ── Robots d\'entrainement IA (bloques) ──────────────────────────')
    for bot in C.AI_TRAINING_BOTS:
        L.append('User-agent: %s' % bot)
        L.append('Disallow: /')
        L.append('')
    L.append('# ── Robots de citation (autorises) ──────────────────────────────')
    for bot in C.AI_CITATION_BOTS:
        L.append('User-agent: %s' % bot)
        L.append('Allow: /')
        L.append('')
    L.append('# ── Sitemaps ───────────────────────────────────────────────────')
    L.append('Sitemap: %s' % C.abs_url('sitemap.xml'))
    (ROOT / 'robots.txt').write_text("\n".join(L) + "\n", encoding='utf-8')
    return len(L)


# ════════════════════════════════════════════════════════════════
#  404.html
# ════════════════════════════════════════════════════════════════
SECTIONS = [
    ("Guide du débutant", "pages/guide-debutant.html", "Premiers pas, modes, extraction, economy."),
    ("Loadout Optimizer", "pages/meta-loadout-optimizer.html", "Construisez votre kit et calculez son cout."),
    ("Tier List des armes", "pages/armes-tier-list.html", "Classement S7 et tier list interactive."),
    ("Cartes", "pages/map-farm.html", "Farm, Valley, Northridge, Armory, TV Station, Airport."),
    ("Munitions", "pages/items-munitions.html", "Penetration, degats de chair, classe d'armure."),
    ("Strategies S7", "pages/meta-stratégies-s7.html", "Patience, rat run, timing d'extraction."),
    ("Communaute", "pages/communaute-ressources.html", "Reddit, Discord, streamers, patch notes."),
    ("Univers de Kamona", "pages/univers-lore.html", "Factions, guerre Nord-Sud, Dark Zone.")
]


def build_404():
    """Construit 404.html a partir du gabarit d'index.html : la navigation
    globale et le footer sont conserves a l'identique."""
    src = (ROOT / C.ROOT_INDEX).read_text(encoding='utf-8')

    # <head> d'origine (avant <body>)
    header = src[:src.index('<body>')]
    header = header.replace('<html lang="fr" data-theme="dark">', '<html lang="fr" data-theme="dark">')
    # titre / description propres
    header = re.sub(r'<title>.*?</title>',
                     '<title>Page introuvable (404) — ABI NEXUS</title>', header, flags=re.S)
    header = re.sub(r'<meta name="description" content=".*?">',
                     '<meta name="description" content="Cette page n\'existe pas ou a ete deplacee. '
                     'Retrouvez le guide ABI NEXUS : armes, armures, cartes, strategies et outils '
                     'interactifs d\'Arena Breakout Infinite, Saison 7 : Utopia.">', header, flags=re.S)
    header = re.sub(r'<link rel="canonical" href=".*?">',
                     '<link rel="canonical" href="%s">' % C.abs_url('404.html'), header)
    header = re.sub(r'<meta property="og:title" content=".*?">',
                     '<meta property="og:title" content="Page introuvable — ABI NEXUS">', header)
    header = re.sub(r'<meta property="og:description" content=".*?">',
                     '<meta property="og:description" content="Le secteur est vide. '
                     'Retournez au guide ABI NEXUS ou cherchez une page.">', header)
    header = re.sub(r'<meta property="og:url" content=".*?">',
                     '<meta property="og:url" content="%s">' % C.abs_url('404.html'), header)
    # une page d'erreur ne doit pas etre indexee
    header = header.replace('<meta name="robots" content="%s">' % C.ROBOTS,
                            '<meta name="robots" content="noindex, follow">')
    header = header.replace('<link rel="alternate" hreflang="fr" href="%s">' % C.abs_url('index.html'),
                            '<link rel="alternate" hreflang="fr" href="%s">' % C.abs_url('index.html'))

    # en-tete du site (logo + navigation globale + actions) repris a l'identique
    site_header = src[src.index('<body>'):src.index('</header>') + len('</header>')]
    # pied de page repris a l'identique
    footer = src[src.index('<footer class="site-footer">'):src.index('</footer>') + len('</footer>')]

    cards = "".join(
        '        <a class="card err-card reveal" href="%s">'
        '<div class="card-body"><h3 class="card-title">%s</h3>'
        '<p class="card-text">%s</p></div></a>\n' % (href, name, desc)
        for name, href, desc in SECTIONS
    )

    main = '''  <main id="contenu" class="section">
    <div class="container">
      <header class="page-head err-head">
        <p class="eyebrow">Erreur 404 — Secteur perdu</p>
        <h1>Ce secteur<br>n'existe pas</h1>
        <p class="page-sub">La page que vous cherchez a ete deplacee, renommee, ou n'a jamais existe. Sur Kamona, on appelle ca une extraction ratee. Voici par ou reprendre.</p>
      </header>

      <figure class="page-figure err-figure">
        <img src="img/seo/404-secteur-perdu.jpg" width="1938" height="812" alt="Operateur seul au bord d'une plateforme d'extraction abandonnee sous la pluie, balise de secours rouge dans la brume" loading="eager" fetchpriority="high" decoding="async">
        <figcaption>Poste d'extraction desert — Kamona, secteur inconnu. Repars par la ou tu as le plus de munitions.</figcaption>
      </figure>

      <div class="err-actions">
        <a class="btn btn-primary" href="index.html">Retour a l'accueil</a>
        <a class="btn btn-outline" href="pages/guide-debutant.html">Guide du debutant</a>
      </div>

      <h2>Les sections les plus consultees</h2>
      <div class="grid grid--4 err-grid">
%s      </div>

      <div class="callout callout-warning">
        <h4>Vous cherchiez une page precise ?</h4>
        <p>Utilisez la barre de recherche en haut de page (raccourci <kbd>/</kbd> ou <kbd>Ctrl</kbd> + <kbd>K</kbd>) : elle interroge les 63 pages du guide ainsi que les armes, armures, munitions, objets et cartes. La page <a href="pages/communaute-patch-notes.html">Patch notes</a> recense les URL qui ont change depuis la Saison 7.</p>
      </div>
    </div>
  </main>

''' % cards

    scripts = ''.join(re.findall(r'  <script src="[^"]+"[^>]*></script>\n', src))
    # la recherche doit etre presente sur la page 404 : elle utilise la meme nav
    if 'js/search.js' not in scripts:
        scripts = scripts.replace('  <script src="js/main.js" defer></script>\n',
                                  '  <script src="js/main.js" defer></script>\n  <script src="js/search.js" defer></script>\n')

    out = (header + '<body>\n'
           '  <a class="skip-link" href="#contenu">Aller au contenu</a>\n'
           '  <div class="progress-bar" aria-hidden="true"></div>\n\n'
           + site_header + '\n\n'
           + main + '\n' + footer + '\n\n' + scripts + '</body>\n</html>\n')

    # le correcteur S17 (identifiants de liens, hierarchie des titres)
    # est reapplique sur la page 404 comme sur les autres pages
    try:
        sys.path.insert(0, str(ROOT / 'tools'))
        import build_s17
        out = build_s17.fix_headings(out)[0]
        out = build_s17.fix_links(out, '404')
    except Exception as exc:  # pragma: no cover
        print('  (correcteur S17 non applique : %s)' % exc)

    (ROOT / '404.html').write_text(out, encoding='utf-8')
    return len(SECTIONS)


# ════════════════════════════════════════════════════════════════
#  manifest.json
# ════════════════════════════════════════════════════════════════
def build_manifest():
    manifest = {
        "id": "/",
        "name": C.SITE_LONG_NAME,
        "short_name": C.SITE_NAME,
        "description": "Le guide de reference francais d'Arena Breakout Infinite — "
                       "Saison 7 : Utopia. Armes, armures, munitions, cartes, strategies, "
                       "tier lists et outils interactifs.",
        "lang": "fr",
        "dir": "ltr",
        "start_url": "./index.html",
        "scope": "./",
        "display": "standalone",
        "display_override": ["standalone", "minimal-ui", "browser"],
        "orientation": "portrait-primary",
        "background_color": C.THEME_COLOR_DARK,
        "theme_color": C.THEME_COLOR_DARK,
        "categories": ["games", "reference", "guides"],
        "prefer_related_applications": False,
        "icons": [
            {"src": "img/ui/favicon-64.jpg", "sizes": "64x64", "type": "image/jpeg"},
            {"src": "img/ui/favicon-180.jpg", "sizes": "180x180", "type": "image/jpeg"},
            {"src": "img/ui/favicon-512.jpg", "sizes": "512x512", "type": "image/jpeg", "purpose": "any"},
            {"src": "img/ui/favicon-512.jpg", "sizes": "512x512", "type": "image/jpeg", "purpose": "maskable"}
        ],
        "shortcuts": [
            {"name": "Guide du debutant", "short_name": "Debuter",
             "url": "pages/guide-debutant.html", "icons": [{"src": "img/ui/favicon-180.jpg", "sizes": "180x180", "type": "image/jpeg"}]},
            {"name": "Loadout Optimizer", "short_name": "Loadout",
             "url": "pages/meta-loadout-optimizer.html", "icons": [{"src": "img/ui/favicon-180.jpg", "sizes": "180x180", "type": "image/jpeg"}]},
            {"name": "Tier List des armes", "short_name": "Tier List",
             "url": "pages/armes-tier-list.html", "icons": [{"src": "img/ui/favicon-180.jpg", "sizes": "180x180", "type": "image/jpeg"}]},
            {"name": "Cartes", "short_name": "Cartes",
             "url": "pages/map-farm.html", "icons": [{"src": "img/ui/favicon-180.jpg", "sizes": "180x180", "type": "image/jpeg"}]}
        ]
    }
    (ROOT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                                        encoding='utf-8')
    return len(manifest["shortcuts"])


if __name__ == '__main__':
    n = build_sitemap()
    print('sitemap.xml : %d URL' % n)
    build_robots()
    print('robots.txt : ecrit')
    s = build_404()
    print('404.html : %d raccourcis' % s)
    k = build_manifest()
    print('manifest.json : %d raccourcis' % k)
