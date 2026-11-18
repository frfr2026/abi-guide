#!/usr/bin/env python3
"""ABI NEXUS — qa_final.py : recette finale du site (S17 QA_FINAL).

Controle exhaustif en 12 volets :
   1. Structure HTML et hierarchie des titres
   2. Accessibilite : noms accessibles, libelles, skip link, landmarks
   3. Accessibilite : focus visible, target size, reduced motion
   4. Navigation globale : coherence entre toutes les pages
   5. Liens internes : resolution et unicite des identifiants
   6. Liens externes : rel=noopener, annonce du nouvel onglet
   7. Images : existence, dimensions, alt, chargement, formats
   8. JavaScript : syntaxe, presence des modules, regions live
   9. Performance : budgets de poids
  10. Contenu : CJK, unicite des titres et descriptions
  11. Fichiers racine : sitemap, robots, manifest, 404
  12. Orthographe francaise (accents manquants sur les mots frequents)

Usage : python3 tools/qa_final.py
"""
import pathlib, re, json, sys, subprocess, gzip, html
from collections import Counter, OrderedDict
from xml.etree import ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import seo_config as C  # noqa: E402

errors, warns, infos = [], [], []
PAGES = sorted((ROOT / 'pages').glob('*.html')) + [ROOT / 'index.html', ROOT / '404.html']
CJK = re.compile(r'[　-鿿＀-￯]')


def err(m): errors.append(m)
def warn(m): warns.append(m)
def info(m): infos.append(m)


def rel_of(f): return str(f.relative_to(ROOT))


print('═══ ABI NEXUS — Recette finale (S17) ═══\n')
print('Fichiers analyses : %d pages + racine\n' % len(PAGES))

# ════════════════════════════════════════════════════════════════
# 1. Structure HTML et hierarchie des titres
# ════════════════════════════════════════════════════════════════
print('1. Structure HTML et hierarchie des titres')
HEAD_RE = re.compile(r'<h([1-6])([^>]*)>(.*?)</h\1>', re.S)
skip_errors = 0
h1_errors = 0
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    for tag in ('<html', '</html>', '<head>', '</head>', '<body', '</body>'):
        if tag not in s:
            err('%s : balise %s absente' % (rel_of(f), tag))
    body = s[s.index('<body>'):]
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', body, flags=re.S)
    hs = [(int(m.group(1)), re.sub(r'<[^>]+>', '', m.group(3)).strip()) for m in HEAD_RE.finditer(body)]
    prev = 0
    for lvl, txt in hs:
        if prev and lvl > prev + 1:
            err('%s : saut de niveau h%d -> h%d (%s)' % (rel_of(f), prev, lvl, txt[:40]))
            skip_errors += 1
        prev = lvl
    n1 = len([t for l, t in hs if l == 1])
    if n1 != 1:
        err('%s : %d balise(s) h1 (attendu 1)' % (rel_of(f), n1))
        h1_errors += 1
print('   sauts de niveau : %d | h1 incorrect : %d' % (skip_errors, h1_errors))

# ════════════════════════════════════════════════════════════════
# 2. Accessibilite : noms accessibles et libelles
# ════════════════════════════════════════════════════════════════
print('\n2. Accessibilite — noms accessibles, libelles, skip link')
no_name = 0
no_label = 0
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<(button|a|input|select|textarea)\b([^>]*)>', s):
        tag, attrs = m.group(1), m.group(2)
        if tag == 'a' and 'href=' not in attrs:
            continue
        if tag == 'input' and 'type="hidden"' in attrs:
            continue
        named = ('aria-label=' in attrs) or ('aria-labelledby=' in attrs) or ('title=' in attrs)
        if tag in ('input', 'select', 'textarea'):
            # 1) nom accessible explicite
            if 'aria-label=' in attrs or 'aria-labelledby=' in attrs:
                continue
            # 2) libelle explicite (for="id")
            fid = re.search(r'id="([^"]+)"', attrs)
            if fid and ('for="%s"' % fid.group(1)) in s:
                continue
            # 3) libelle implicite : le champ est dans un <label>...</label>
            before = s[:m.start()]
            last_open = before.rfind('<label')
            last_close = before.rfind('</label>')
            if last_open > last_close:
                continue
            no_label += 1
            err('%s : champ sans libelle associe (%s)' % (rel_of(f), attrs[:70]))
            continue
        if not named:
            end = s.find('>', m.end())
            inner = re.sub(r'<[^>]+>', '', s[m.end():end]).strip()
            if not inner:
                no_name += 1
                err('%s : element interactif sans nom accessible (%s)' % (rel_of(f), attrs[:70]))
    # skip link + landmarks
    if 'skip-link' not in s:
        err('%s : skip link absent' % rel_of(f))
    for lm in ('<main', '<header', '<footer', '<nav'):
        if lm not in s:
            err('%s : landmark %s absent' % (rel_of(f), lm))
print('   elements sans nom : %d | champs sans libelle : %d' % (no_name, no_label))

# ════════════════════════════════════════════════════════════════
# 3. Accessibilite : focus visible, target size, reduced motion
# ════════════════════════════════════════════════════════════════
print('\n3. Accessibilite — focus, cible tactile, mouvements reduits')
css = "\n".join((ROOT / 'css' / f).read_text(encoding='utf-8') for f in
                 ('variables.css', 'main.css', 'animations.css', 'components.css', 'responsive.css'))
checks = [
    (':focus-visible' in css, 'indicateur :focus-visible present'),
    ('outline: none' not in css and 'outline:none' not in css, 'aucun outline: none'),
    ('scroll-padding-top' in css, 'scroll-padding-top (focus non masque)'),
    ('prefers-reduced-motion' in css, 'prefers-reduced-motion gere'),
    ('min-height: 24px' in css, 'cible tactile minimale de 24 px'),
]
for cond, label in checks:
    if cond:
        print('   ✓ ' + label)
    else:
        err('CSS : ' + label + ' manquant')

# ════════════════════════════════════════════════════════════════
# 4. Navigation globale : coherence entre les pages
# ════════════════════════════════════════════════════════════════
print('\n4. Navigation globale')
nav_sig = Counter()
missing_nav = []
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    m = re.search(r'<header class="site-nav">(.*?)</header>', s, re.S)
    if not m:
        missing_nav.append(rel_of(f))
        continue
    nav = m.group(1)
    links = tuple(sorted(set(re.findall(
        r'<a class="nav-link[^"]*" href="([^"]+)"', nav))))
    nav_sig[links] += 1
    if nav.count('mega-menu') < 6:
        warn('%s : moins de 6 mega-menus dans la navigation' % rel_of(f))
if missing_nav:
    err('navigation absente : %s' % ', '.join(missing_nav))
# les chemins de la racine sont prefixes par « pages/ » : on normalise
norm = Counter()
for links, c in nav_sig.items():
    norm[tuple(l.replace('pages/', '', 1) for l in links)] += c
print('   variantes de navigation : %d (normalisees : %d)' % (len(nav_sig), len(norm)))
if len(norm) > 1:
    warn('la barre de navigation differe d\'une page a l\'autre')

# etat actif
active = sum(1 for f in PAGES if 'aria-current="page"' in f.read_text(encoding='utf-8'))
print('   pages avec etat actif (aria-current) : %d / %d' % (active, len(PAGES)))
if active < len(PAGES) - 2:
    warn('plusieurs pages sans marqueur aria-current')

# ════════════════════════════════════════════════════════════════
# 5. Liens internes et identifiants
# ════════════════════════════════════════════════════════════════
print('\n5. Liens internes et identifiants')
broken = 0
dup_ids = 0
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    base = f.parent
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(('http', '#', 'mailto:', 'data:', 'tel:')):
            continue
        target = href.split('#')[0]
        if not target:
            continue
        if not (base / target).resolve().exists():
            err('%s : lien interne casse (%s)' % (rel_of(f), href))
            broken += 1
    ids = re.findall(r'\bid="([^"]+)"', s)
    dups = [i for i, c in Counter(ids).items() if c > 1]
    if dups:
        err('%s : identifiants dupliques (%s)' % (rel_of(f), dups[:3]))
        dup_ids += 1
print('   liens casses : %d | pages avec doublons d\'id : %d' % (broken, dup_ids))

# ancres internes verifiees
anchor_err = 0
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    base = f.parent
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    for href in re.findall(r'href="([^"]*#[^"]+)"', s):
        if href.startswith(('http', 'mailto:')):
            continue
        path, frag = href.split('#', 1)
        path = path.split('#')[0]
        target = (base / path).resolve() if path else f.resolve()
        if target == f.resolve():
            if frag not in ids:
                err('%s : ancre #%s inexistante' % (rel_of(f), frag))
                anchor_err += 1
        elif target.exists():
            tids = set(re.findall(r'\bid="([^"]+)"', target.read_text(encoding='utf-8')))
            if frag and frag not in tids:
                err('%s : ancre #%s absente de %s' % (rel_of(f), frag, path))
                anchor_err += 1
print('   ancres internes verifiees : %d erreur(s)' % anchor_err)

# ════════════════════════════════════════════════════════════════
# 6. Liens externes
# ════════════════════════════════════════════════════════════════
print('\n6. Liens externes')
ext = 0
no_noopener = 0
no_announce = 0
hosts = OrderedDict()
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', s, re.S):
        attrs, inner = m.group(1), m.group(2)
        hm = re.search(r'href="(https?://[^"]+)"', attrs)
        if not hm:
            continue
        ext += 1
        if 'noopener' not in attrs:
            err('%s : lien externe sans rel=noopener (%s)' % (rel_of(f), hm.group(1)[:50]))
            no_noopener += 1
        if 'target="_blank"' in attrs and '(nouvel onglet)' not in inner:
            err('%s : ouverture dans un nouvel onglet non annoncee (%s)' % (rel_of(f), hm.group(1)[:50]))
            no_announce += 1
        host = hm.group(1).split('/')[2]
        hosts.setdefault(host, 0)
        hosts[host] += 1
print('   liens externes : %d | sans noopener : %d | non annonces : %d' % (ext, no_noopener, no_announce))
print('   hotes distincts : %d' % len(hosts))

# ════════════════════════════════════════════════════════════════
# 7. Images
# ════════════════════════════════════════════════════════════════
print('\n7. Images')
missing_img = 0
no_dims = 0
no_alt = 0
no_lazy = 0
used = set()
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    for tag in re.findall(r'<img[^>]*>', s):
        sm = re.search(r'src="([^"]+)"', tag)
        if not sm:
            continue
        src = sm.group(1)
        if src.startswith(('http', 'data:')):
            continue
        used.add(str((f.parent / src).resolve()))
        if not (f.parent / src).resolve().exists():
            err('%s : image manquante (%s)' % (rel_of(f), src))
            missing_img += 1
        if 'width=' not in tag or 'height=' not in tag:
            no_dims += 1
            err('%s : image sans width/height (%s)' % (rel_of(f), src))
        if 'alt=' not in tag:
            no_alt += 1
            err('%s : image sans attribut alt (%s)' % (rel_of(f), src))
        if 'loading=' not in tag:
            no_lazy += 1
print('   images manquantes : %d | sans dimensions : %d | sans alt : %d | sans loading : %d'
      % (missing_img, no_dims, no_alt, no_lazy))

# references supplementaires : JSON de donnees, chaines JS,
# favicons et images sociales
json_images = []
for jf in (ROOT / 'js').glob('*.json'):
    try:
        data = json.loads(jf.read_text(encoding='utf-8'))
    except Exception:
        continue
    stack = [data]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ('image', 'imageVariant') and isinstance(v, str):
                    target = (ROOT / 'js' / v).resolve()
                    used.add(str(target))
                    json_images.append((rel_of(jf), v, target))
                else:
                    stack.append(v)
        elif isinstance(node, list):
            stack.extend(node)

# chaque image referencee par les donnees JSON doit exister sur le disque
missing_json = []
for jf, rel, target in json_images:
    if not target.exists():
        missing_json.append('%s : %s' % (jf, rel))
        err('donnees %s : image manquante (%s)' % (jf, rel))
print('   images referencees par les JSON : %d (manquantes : %d)'
      % (len(json_images), len(missing_json)))
for jf in (ROOT / 'js').glob('*.js'):
    for m in re.finditer(r"['\"]((?:\.\./)?img/[^'\"]+\.(?:jpg|jpeg|png|webp|svg))['\"]", jf.read_text(encoding='utf-8')):
        used.add(str((ROOT / 'js' / m.group(1)).resolve()))
IMG_EXT = ('jpg', 'jpeg', 'png', 'webp', 'svg')


def _abs(base, url):
    u = url.strip()
    if u.startswith(('http://', 'https://', 'data:')):
        u = u.split(C.SITE_URL.rstrip('/') + '/')[-1] if C.SITE_URL in u else ''
        if not u:
            return None
        return str((ROOT / u.lstrip('/')).resolve())
    return str((base / u).resolve())


for f in PAGES:
    s = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<link[^>]+href="([^"]+)"', s):
        if 'img/' in m.group(1):
            a = _abs(f.parent, m.group(1))
            if a:
                used.add(a)
    for m in re.finditer(r'<meta property="og:image" content="([^"]+)"', s):
        a = _abs(f.parent, m.group(1))
        if a:
            used.add(a)
    # images en arriere-plan (style inline ou feuille de style liee)
    for m in re.finditer(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)', s):
        if 'img/' in m.group(1):
            a = _abs(f.parent, m.group(1))
            if a:
                used.add(a)
for cssf in (ROOT / 'css').glob('*.css'):
    for m in re.finditer(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)', cssf.read_text(encoding='utf-8')):
        if 'img/' in m.group(1):
            a = _abs(cssf.parent, m.group(1))
            if a:
                used.add(a)
mf_ref = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
for ic in mf_ref.get('icons', []):
    used.add(str((ROOT / ic['src']).resolve()))
all_img = {str(p.resolve()) for p in (ROOT / 'img').rglob('*')
           if p.is_file() and p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.svg')}
orphans = sorted(all_img - used)
for o in orphans:
    warn('image orpheline (non referencee) : %s' % o.replace(str(ROOT) + '/', ''))
bad_fmt = [o for o in all_img if o.lower().endswith(('.png', '.svg'))]
for b in bad_fmt:
    err('format interdit (PNG/SVG) : %s' % b.replace(str(ROOT) + '/', ''))
print('   images du site : %d | orphelines : %d | PNG/SVG : %d'
      % (len(all_img), len(orphans), len(bad_fmt)))

# ════════════════════════════════════════════════════════════════
# 8. JavaScript
# ════════════════════════════════════════════════════════════════
print('\n8. JavaScript')
js_files = sorted((ROOT / 'js').glob('*.js'))
for j in js_files:
    r = subprocess.run(['node', '--check', str(j)], capture_output=True)
    if r.returncode != 0:
        err('%s : erreur de syntaxe (%s)' % (rel_of(j), r.stderr.decode()[:120]))
print('   fichiers JS verifies : %d' % len(js_files))

REQUIRED_MODULES = ['search.js', 'loadout-builder.js', 'weapon-compare.js',
                    'map-explorer.js', 'tier-list.js', 'optimizer.js', 'weapons.js',
                    'armors.js', 'items.js', 'main.js', 'navigation.js',
                    'ballistics.js']
for m in REQUIRED_MODULES:
    if not (ROOT / 'js' / m).exists():
        err('module manquant : js/%s' % m)
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    if 'js/search.js' not in s:
        err('%s : module de recherche non charge' % rel_of(f))
# ── derive de l'index de recherche ──────────────────────────────────
# js/search.js porte une liste codee en dur des pages indexables.
# Toute page ajoutee sans y etre inscrite devient invisible dans la
# recherche : ce controle empeche la derive.
search_js = (ROOT / 'js' / 'search.js').read_text(encoding='utf-8')
m = re.search(r'const PAGES = \[(.*?)\n  \];', search_js, re.S)
if not m:
    err('js/search.js : liste PAGES introuvable')
else:
    listed = set(re.findall(r"\['([^']+)'", m.group(1)))
    real = {f.name for f in (ROOT / 'pages').glob('*.html')}
    # Une entree commencee par '/' designe une page de la racine du site
    # (l'accueil) : elle n'appartient pas au dossier /pages/.
    root_listed = {p for p in listed if p.startswith('/')}
    listed = {p for p in listed if not p.startswith('/')}
    missing = sorted(real - listed)
    extra = sorted(listed - real)
    for p in root_listed:
        if not (ROOT / p.lstrip('/')).exists():
            err('js/search.js : page racine listee(s) mais inexistante(s) : %s' % p)
    if missing:
        err('js/search.js : %d page(s) absente(s) de l index de recherche : %s'
            % (len(missing), ', '.join(missing[:5])))
    if extra:
        err('js/search.js : %d page(s) listee(s) mais inexistante(s) : %s'
            % (len(extra), ', '.join(extra[:5])))
    print('   index de recherche : %d pages, derive : %d' % (len(listed) + len(root_listed), len(missing) + len(extra)))

live = 0
for j in js_files:
    t = j.read_text(encoding='utf-8')
    if 'aria-live' in t:
        live += 1
    if j.name == 'main.js' and 'IntersectionObserver' in t \
       and "'IntersectionObserver' in window" not in t:
        warn('main.js : IntersectionObserver sans repli')
print('   modules avec region live : %d' % live)

# ════════════════════════════════════════════════════════════════
# 9. Performance
# ════════════════════════════════════════════════════════════════
print('\n9. Performance')
css_gz = sum(len(gzip.compress(f.read_bytes(), 9)) for f in (ROOT / 'css').glob('*.css'))
js_gz = sum(len(gzip.compress(f.read_bytes(), 9)) for f in (ROOT / 'js').glob('*.js'))
html_sizes = [f.stat().st_size for f in PAGES]
print('   CSS gzip : %.1f Ko (budget 80) | JS gzip : %.1f Ko (budget 300)'
      % (css_gz / 1024, js_gz / 1024))
print('   HTML : moyenne %.1f Ko, max %.1f Ko'
      % (sum(html_sizes) / len(html_sizes) / 1024, max(html_sizes) / 1024))
if css_gz > 80 * 1024:
    err('CSS compresse au-dessus du budget')
if js_gz > 300 * 1024:
    err('JS compresse au-dessus du budget')
heavy = []
for f in PAGES:
    gz = len(gzip.compress(f.read_bytes(), 9)) / 1024
    if gz > 25:
        heavy.append((f.name, f.stat().st_size / 1024, gz))
for n, raw, gz in heavy:
    info('page dense : %s (%.0f Ko brut, %.1f Ko gzip)' % (n, raw, gz))
print('   pages > 25 Ko gzip : %d' % len(heavy))

# ════════════════════════════════════════════════════════════════
# 10. Contenu
# ════════════════════════════════════════════════════════════════
print('\n10. Contenu')
cjk_hits = 0
titles, descs = {}, {}
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    h = set(CJK.findall(body))
    if h:
        err('%s : CJK visible %s' % (rel_of(f), sorted(h)))
        cjk_hits += 1
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    if m:
        t = html.unescape(m.group(1)).strip()
        if t in titles:
            err('titre duplique : %s et %s' % (titles[t], rel_of(f)))
        titles[t] = rel_of(f)
    m = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    if m:
        d = html.unescape(m.group(1)).strip()
        if d in descs:
            err('description dupliquee : %s et %s' % (descs[d], rel_of(f)))
        descs[d] = rel_of(f)
print('   pages avec CJK : %d | titres uniques : %d/%d | descriptions uniques : %d/%d'
      % (cjk_hits, len(titles), len(PAGES), len(descs), len(PAGES)))

# ════════════════════════════════════════════════════════════════
# 11. Fichiers racine
# ════════════════════════════════════════════════════════════════
print('\n11. Fichiers racine')
sm = ROOT / 'sitemap.xml'
if not sm.exists():
    err('sitemap.xml absent')
else:
    tree = ET.fromstring(sm.read_text(encoding='utf-8'))
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    urls = tree.findall(ns + 'url')
    listed = set()
    for u in urls:
        loc = u.find(ns + 'loc').text
        local = loc.replace(C.SITE_URL.rstrip('/') + '/', '')
        listed.add(local)
        if not (ROOT / local).exists():
            err('sitemap.xml : URL inexistante (%s)' % local)
    for f in PAGES:
        if f.name == '404.html':
            continue
        if rel_of(f) not in listed:
            err('sitemap.xml : page absente (%s)' % rel_of(f))
    if '404.html' in listed:
        err('sitemap.xml : 404.html ne doit pas etre liste')
    print('   sitemap : %d URL' % len(urls))

rb = (ROOT / 'robots.txt').read_text(encoding='utf-8')
if not re.search(r'^Sitemap: https://', rb, re.M):
    err('robots.txt : directive Sitemap absolute absente')
if 'Disallow: /tools/' not in rb:
    warn('robots.txt : /tools/ n\'est pas exclu')
if re.search(r'^(Allow|Disallow):.*noindex', rb, re.M | re.I):
    err('robots.txt : noindex interdit dans ce fichier')
print('   robots.txt : %d lignes, %d User-agent' % (len(rb.split('\n')),
                                                    len(re.findall(r'^User-agent:', rb, re.M))))

mf = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
for ic in mf.get('icons', []):
    if not (ROOT / ic['src']).exists():
        err('manifest.json : icone absente (%s)' % ic['src'])
for sc in mf.get('shortcuts', []):
    if not (ROOT / sc['url']).exists():
        err('manifest.json : raccourci invalide (%s)' % sc['url'])
print('   manifest : %d icones, %d raccourcis' % (len(mf.get('icons', [])), len(mf.get('shortcuts', []))))

p404 = (ROOT / '404.html').read_text(encoding='utf-8')
for needle, label in (('nav-actions', 'navigation globale'), ('js/search.js', 'recherche'),
                      ('noindex', 'balise noindex'), ('id="contenu"', 'cible du skip link')):
    if needle not in p404:
        err('404.html : %s absent' % label)
print('   404.html : %d Ko, navigation et recherche presentes' % (len(p404) / 1024))

# ════════════════════════════════════════════════════════════════
# 12. Orthographe : accents manquants
# ════════════════════════════════════════════════════════════════
print('\n12. Orthographe francaise')
# mots dont la forme sans accent est toujours fautive en francais
# (on ecarte « complet », « situation », « comparaison », « explicite »,
#  « agression » : ces formes sans accent sont correctes)
NEEDS_ACCENT = {
    'deja': 'deja', 'apres': 'apres', 'tres': 'tres', 'meme': 'meme',
    'premiere': 'premiere', 'reference': 'reference', 'strategie': 'strategie',
    'securite': 'securite', 'economie': 'economie', 'categorie': 'categorie',
    'donnees': 'donnees', 'creation': 'creation', 'selection': 'selection',
    'verification': 'verification', 'bientot': 'bientot', 'probleme': 'probleme',
    'modele': 'modele', 'regle': 'regle', 'echec': 'echec', 'equipe': 'equipe',
    'periode': 'periode', 'priorite': 'priorite', 'qualite': 'qualite',
    'disponibilite': 'disponibilite', 'regles': 'regles', 'equipes': 'equipes',
    'modeles': 'modeles', 'donnees ': 'donnees', 'reperes': 'reperes',
}
accents = 0
for f in PAGES:
    s = f.read_text(encoding='utf-8')
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(body)
    for w in sorted(NEEDS_ACCENT):
        for m in re.finditer(r'(?<![\w\u00c0-\u024f])' + re.escape(w) + r'(?![\w\u00c0-\u024f])',
                             body, re.I):
            ctx = body[max(0, m.start() - 30):m.end() + 30].strip()
            warn('%s : accent manquant dans « %s » (%s)' % (rel_of(f), w, ctx[:60]))
            accents += 1
            break
print('   occurrences suspectes : %d' % accents)

# ════════════════════════════════════════════════════════════════
# Verdict
# ════════════════════════════════════════════════════════════════
print('\n' + '=' * 66)
if errors:
    print('ERREURS BLOQUANTES : %d' % len(errors))
    seen = set()
    for e in errors:
        key = e.split(':')[0]
        if key in seen and len([x for x in errors if x.split(':')[0] == key]) > 3:
            continue
        seen.add(key)
        print('  ✗ ' + e)
else:
    print('RECETTE FINALE : AUCUNE erreur bloquante')
print('-' * 66)
print('Avertissements : %d' % len(warns))
for w in warns[:25]:
    print('  ! ' + w)
if len(warns) > 25:
    print('  ... et %d autres' % (len(warns) - 25))
if infos:
    print('-' * 66)
    print('Informations : %d' % len(infos))
    for i in infos[:15]:
        print('  · ' + i)
    if len(infos) > 15:
        print('  ... et %d autres' % (len(infos) - 15))
print('=' * 66)
sys.exit(1 if errors else 0)
