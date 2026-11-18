#!/usr/bin/env python3
"""ABI NEXUS — audit_seo.py : controle de conformite SEO / performance (S16).

Verifie, page par page et sur les fichiers racine :
  • title <= 60 caracteres, description <= 160, uniques ;
  • canonical absolute et coherent avec l'URL de la page ;
  • balise robots explicite, Open Graph complet, Twitter Card ;
  • JSON-LD valide, avec Organization / WebSite / WebPage / BreadcrumbList ;
  • chaque <img> avec width, height, alt et loading ;
  • sitemap.xml : XML valide, URLs existantes, lastmod au format W3C,
    absence de priority/changefreq, 404.html absent ;
  • robots.txt : directive Sitemap absolue, CSS/JS accessibles ;
  • manifest.json : JSON valide, icones presentes et au format JPG ;
  • liens internes resolus et absence de CJK.

Usage : python3 tools/audit_seo.py
"""
import pathlib, re, json, sys, os, html
from xml.etree import ElementTree as ET
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import seo_config as C  # noqa: E402

errors, warns = [], []
pages = sorted((ROOT / 'pages').glob('*.html')) + [ROOT / 'index.html']
CJK = re.compile(r'[　-鿿＀-￯]')


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def rel_of(f):
    return str(f.relative_to(ROOT))


# ════════════════════════════════════════════════════════════════
print('═══ ABI NEXUS — Audit SEO / Performance (S16) ═══\n')
print('Site : %s' % C.SITE_URL)
print('Pages auditées : %d\n' % len(pages))

# ── 1. Balises <head> ────────────────────────────────────────────
seen_titles, seen_descs = {}, {}
REQUIRED_META = ['description', 'robots', 'author', 'language', 'theme-color']
REQUIRED_OG = ['og:type', 'og:site_name', 'og:locale', 'og:title', 'og:description',
               'og:url', 'og:image', 'og:image:width', 'og:image:height', 'og:image:alt']
REQUIRED_TW = ['twitter:card', 'twitter:title', 'twitter:description',
               'twitter:image', 'twitter:image:alt']

for f in pages:
    rel = rel_of(f)
    s = f.read_text(encoding='utf-8')
    head = s[:s.index('</head>')]

    # --- title ---
    m = re.search(r'<title>(.*?)</title>', head, re.S)
    if not m:
        err('%s : balise <title> absente' % rel)
        title = ''
    else:
        title = html.unescape(m.group(1)).strip()
        if len(title) > 60:
            err('%s : title de %d caracteres (> 60)' % (rel, len(title)))
        if len(title) < 15:
            warn('%s : title de %d caracteres, trop court' % (rel, len(title)))
        if title in seen_titles:
            err('%s : title identique a %s' % (rel, seen_titles[title]))
        seen_titles[title] = rel

    # --- description ---
    m = re.search(r'<meta name="description" content="(.*?)"', head, re.S)
    if not m:
        err('%s : meta description absente' % rel)
    else:
        d = html.unescape(m.group(1)).strip()
        if len(d) > 160:
            err('%s : description de %d caracteres (> 160)' % (rel, len(d)))
        if len(d) < 70:
            warn('%s : description de %d caracteres, trop courte' % (rel, len(d)))
        if d in seen_descs:
            err('%s : description identique a %s' % (rel, seen_descs[d]))
        seen_descs[d] = rel

    # --- meta requis ---
    for name in REQUIRED_META:
        if ('name="%s"' % name) not in head:
            err('%s : meta %s absente' % (rel, name))

    # --- canonical ---
    m = re.search(r'<link rel="canonical" href="([^"]+)"', head)
    if not m:
        err('%s : canonical absente' % rel)
    else:
        canon = m.group(1)
        if not canon.startswith('http'):
            err('%s : canonical relative (%s)' % (rel, canon))
        elif canon != C.page_url(rel):
            err('%s : canonical incoherent (%s)' % (rel, canon))

    # --- Open Graph ---
    for prop in REQUIRED_OG:
        m = re.search(r'<meta property="%s" content="([^"]*)"' % re.escape(prop), head)
        if not m:
            err('%s : og:%s absente' % (rel, prop.split(':')[1]))
        elif not m.group(1).strip():
            err('%s : og:%s vide' % (rel, prop.split(':')[1]))
    m = re.search(r'<meta property="og:image" content="([^"]*)"', head)
    if m and not m.group(1).startswith('http'):
        err('%s : og:image relative (%s)' % (rel, m.group(1)))

    # --- Twitter Card ---
    for name in REQUIRED_TW:
        if ('name="%s"' % name) not in head:
            err('%s : %s absent' % (rel, name))
    if 'name="twitter:card" content="summary_large_image"' not in head:
        err('%s : twitter:card n\'est pas summary_large_image' % rel)

    # --- JSON-LD ---
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
    if not blocks:
        err('%s : aucun bloc JSON-LD' % rel)
    else:
        for blk in blocks:
            try:
                data = json.loads(blk)
            except Exception as e:
                err('%s : JSON-LD invalide (%s)' % (rel, e))
                continue
            graph = data.get('@graph', [data])
            types = set()
            for node in graph:
                types.add(node.get('@type'))
            for t in ('Organization', 'WebSite', 'WebPage'):
                if t not in types:
                    err('%s : JSON-LD sans entite %s' % (rel, t))
            if f.name != 'index.html' and 'BreadcrumbList' not in types:
                err('%s : JSON-LD sans BreadcrumbList' % rel)
            ids = {n.get('@id') for n in graph if n.get('@id')}
            for node in graph:
                for key in ('isPartOf', 'publisher', 'author', 'breadcrumb', 'mainEntityOfPage'):
                    ref = node.get(key)
                    if isinstance(ref, dict) and ref.get('@id') and ref['@id'] not in ids:
                        err('%s : reference JSON-LD orpheline (%s)' % (rel, ref['@id']))

    # --- images ---
    for tag in re.findall(r'<img[^>]*>', s):
        if 'width=' not in tag or 'height=' not in tag:
            err('%s : <img> sans width/height : %s' % (rel, tag[:90]))
        if 'alt=' not in tag:
            err('%s : <img> sans attribut alt' % rel)
        if 'loading=' not in tag:
            warn('%s : <img> sans loading=lazy' % rel)

    # --- CJK ---
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    hits = set(CJK.findall(body))
    if hits:
        err('%s : CJK visible %s' % (rel, sorted(hits)))

print('1. Balises <head> : %d pages controlees' % len(pages))

# ════════════════════════════════════════════════════════════════
# 2. sitemap.xml
# ════════════════════════════════════════════════════════════════
print('\n2. sitemap.xml')
sm = ROOT / 'sitemap.xml'
if not sm.exists():
    err('sitemap.xml absent')
else:
    raw = sm.read_text(encoding='utf-8')
    try:
        tree = ET.fromstring(raw)
    except Exception as e:
        err('sitemap.xml : XML invalide (%s)' % e)
        tree = None
    if tree is not None:
        ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
        urls = tree.findall(ns + 'url')
        print('   URL : %d' % len(urls))
        local_seen = set()
        for u in urls:
            loc = u.find(ns + 'loc')
            lastmod = u.find(ns + 'lastmod')
            if loc is None or not loc.text:
                err('sitemap.xml : url sans <loc>')
                continue
            if lastmod is None or not lastmod.text:
                err('sitemap.xml : %s sans <lastmod>' % loc.text)
            elif not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$', lastmod.text):
                err('sitemap.xml : lastmod non W3C (%s)' % lastmod.text)
            if u.find(ns + 'priority') is not None:
                warn('sitemap.xml : <priority> present, Google l\'ignore')
            if u.find(ns + 'changefreq') is not None:
                warn('sitemap.xml : <changefreq> present, Google l\'ignore')
            if not loc.text.startswith('http'):
                err('sitemap.xml : <loc> relatif (%s)' % loc.text)
            local = loc.text.replace(C.SITE_URL.rstrip('/') + '/', '')
            if local.endswith('404.html'):
                err('sitemap.xml : 404.html ne doit pas etre dans le sitemap')
            if not (ROOT / local).exists():
                err('sitemap.xml : URL inexistante (%s)' % local)
            local_seen.add(local)
        # toutes les pages indexables doivent etre listees
        for f in pages:
            r = rel_of(f)
            if r not in local_seen:
                err('sitemap.xml : page absente du sitemap (%s)' % r)

# ════════════════════════════════════════════════════════════════
# 3. robots.txt
# ════════════════════════════════════════════════════════════════
print('\n3. robots.txt')
rb = ROOT / 'robots.txt'
if not rb.exists():
    err('robots.txt absent')
else:
    raw = rb.read_text(encoding='utf-8')
    lines = [l.strip() for l in raw.split('\n')
             if l.strip() and not l.strip().startswith('#')]
    if not any(l.startswith('Sitemap: http') for l in lines):
        err('robots.txt : directive Sitemap absolute absente')
    if 'Disallow: /css' in raw or 'Disallow: /js' in raw:
        err('robots.txt : CSS ou JS bloque (Google ne peut plus rendre la page)')
    for l in lines:
        if l.lower().startswith(('disallow:', 'allow:')) and 'noindex' in l.lower():
            err('robots.txt : noindex n\'y est pas autorise (il ne fonctionne pas ici)')
    if 'crawl-delay' in raw.lower():
        warn('robots.txt : crawl-delay ignore par Google')
    # le groupe User-agent: * doit autoriser la racine
    star = False
    for l in lines:
        if l.startswith('User-agent:'):
            star = (l.strip() == 'User-agent: *')
        elif star and l == 'Disallow: /':
            err('robots.txt : la racine est bloquee pour User-agent *')
    bots = re.findall(r'User-agent:\s*(\S+)', raw)
    print('   User-agent declares : %d' % len(bots))

# ════════════════════════════════════════════════════════════════
# 4. manifest.json
# ════════════════════════════════════════════════════════════════
print('\n4. manifest.json')
mf = ROOT / 'manifest.json'
if not mf.exists():
    err('manifest.json absent')
else:
    try:
        m = json.loads(mf.read_text(encoding='utf-8'))
    except Exception as e:
        err('manifest.json : JSON invalide (%s)' % e)
        m = None
    if m:
        for key in ('name', 'short_name', 'start_url', 'scope', 'display', 'icons'):
            if key not in m:
                err('manifest.json : cle %s absente' % key)
        for ic in m.get('icons', []):
            p = ROOT / ic['src']
            if not p.exists():
                err('manifest.json : icone absente (%s)' % ic['src'])
            if not ic['src'].lower().endswith(('.jpg', '.jpeg')):
                err('manifest.json : icone non JPG (%s)' % ic['src'])
        for sc in m.get('shortcuts', []):
            if not (ROOT / sc['url']).exists():
                err('manifest.json : raccourci invalide (%s)' % sc['url'])
        print('   icones : %d | raccourcis : %d' % (len(m.get('icons', [])), len(m.get('shortcuts', []))))

# ════════════════════════════════════════════════════════════════
# 5. 404.html
# ════════════════════════════════════════════════════════════════
print('\n5. 404.html')
p404 = ROOT / '404.html'
if not p404.exists():
    err('404.html absent')
else:
    s = p404.read_text(encoding='utf-8')
    for t in ('<html', '</html>', '<head>', '</head>', '<body', '</body>', '<main', '</main>'):
        if t not in s:
            err('404.html : balise %s absente' % t)
    if 'nav-actions' not in s:
        err('404.html : navigation globale absente')
    if 'js/search.js' not in s:
        err('404.html : recherche globale absente')
    if 'noindex' not in s:
        err('404.html : balise noindex absente')
    if 'robots.txt' in s:
        warn('404.html : reference a robots.txt dans le corps')
    # liens internes
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(('http', '#', 'mailto:')):
            continue
        target = href.split('#')[0]
        if target and not (ROOT / target).exists():
            err('404.html : lien casse (%s)' % href)
    print('   navigation globale : presente | recherche : presente')

# ════════════════════════════════════════════════════════════════
# 6. Images sociales
# ════════════════════════════════════════════════════════════════
print('\n6. Images sociales')
for f in pages:
    s = f.read_text(encoding='utf-8')
    m = re.search(r'<meta property="og:image" content="([^"]+)"', s)
    if not m:
        continue
    url = m.group(1)
    local = url.replace(C.SITE_URL.rstrip('/') + '/', '')
    p = ROOT / local
    if not p.exists():
        err('%s : og:image introuvable (%s)' % (rel_of(f), local))
        continue
    if p.suffix.lower() not in ('.jpg', '.jpeg'):
        err('%s : og:image non JPG (%s)' % (rel_of(f), local))
    with Image.open(p) as im:
        w, h = im.size
        ratio = w / h
        if ratio < 1.5 or ratio > 2.1:
            warn('%s : og:image ratio %.2f hors zone 1.5-2.1 (%s)' % (rel_of(f), ratio, local))
        if w < 600:
            warn('%s : og:image trop petit (%dx%d)' % (rel_of(f), w, h))

# ════════════════════════════════════════════════════════════════
# 7. Liens internes (toutes pages + 404)
# ════════════════════════════════════════════════════════════════
print('\n7. Liens internes')
broken = 0
for f in pages + [p404]:
    s = f.read_text(encoding='utf-8')
    base = f.parent
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(('http', '#', 'mailto:', 'data:')):
            continue
        target = href.split('#')[0]
        if not target:
            continue
        if not (base / target).resolve().exists():
            err('%s : lien interne casse (%s)' % (rel_of(f), href))
            broken += 1
print('   liens internes verifies sur %d fichiers' % (len(pages) + 1))

# ════════════════════════════════════════════════════════════════
# 8. Performance : poids des ressources
# ════════════════════════════════════════════════════════════════
print('\n8. Performance')
css_total = sum(f.stat().st_size for f in (ROOT / 'css').glob('*.css'))
js_total = sum(f.stat().st_size for f in (ROOT / 'js').glob('*.js'))
import gzip
css_gz = sum(len(gzip.compress(f.read_bytes(), 9)) for f in (ROOT / 'css').glob('*.css'))
js_gz = sum(len(gzip.compress(f.read_bytes(), 9)) for f in (ROOT / 'js').glob('*.js'))
print('   CSS total : %.1f Ko bruts / %.1f Ko gzip (budget < 80 Ko compresse)'
      % (css_total / 1024, css_gz / 1024))
print('   JS total  : %.1f Ko bruts / %.1f Ko gzip (budget < 300 Ko compresse)'
      % (js_total / 1024, js_gz / 1024))
if css_gz > 80 * 1024:
    warn('CSS compresse au-dessus du budget de performance (80 Ko)')
if js_gz > 300 * 1024:
    warn('JS compresse au-dessus du budget de performance (300 Ko)')
img_total = sum(f.stat().st_size for f in (ROOT / 'img').rglob('*.jpg'))
print('   Images    : %.1f Mo (%d fichiers)' % (img_total / 1048576,
                                                 len(list((ROOT / 'img').rglob('*.jpg')))))

# ════════════════════════════════════════════════════════════════
# Verdict
# ════════════════════════════════════════════════════════════════
print('\n' + '=' * 62)
if errors:
    print('ERREURS : %d' % len(errors))
    for e in errors[:40]:
        print('  ✗ ' + e)
    if len(errors) > 40:
        print('  ... et %d autres' % (len(errors) - 40))
else:
    print('Audit SEO : AUCUNE erreur')
if warns:
    print('\nAVERTISSEMENTS : %d' % len(warns))
    for w in warns[:20]:
        print('  ! ' + w)
    if len(warns) > 20:
        print('  ... et %d autres' % (len(warns) - 20))
print('=' * 62)
sys.exit(1 if errors else 0)
