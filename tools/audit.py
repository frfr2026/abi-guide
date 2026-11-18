#!/usr/bin/env python3
"""Audit global du site ABI NEXUS : CJK, liens internes, images, HTML, HTTP."""
import pathlib, re, json, sys, urllib.request, urllib.parse, socket

ROOT = pathlib.Path('/home/user/abi-nexus')
PAGES = ROOT / 'pages'
BASE = 'http://localhost:8000/'

errors = []

# ── 1. Scan CJK / caractères hors alphabet latin dans le texte visible ──
CJK = re.compile(r'[\u3000-\u9fff\uff00-\uffef]')
for f in sorted(PAGES.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    hits = set(CJK.findall(body))
    if hits:
        errors.append(f'CJK {f.name}: {sorted(hits)}')

# ── 2. Liens internes ──
pages_set = {p.name for p in PAGES.glob('*.html')}
root_files = {p.name for p in ROOT.glob('*.html')}
for f in sorted(PAGES.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(('http', 'mailto:', '#', 'data:')):
            continue
        target = href.split('#')[0]
        if not target:
            continue
        base = (PAGES / target).resolve()
        if not base.exists():
            errors.append(f'LIEN {f.name} -> {href}')

# ── 3. Images référencées ──
for f in sorted(PAGES.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    for src in re.findall(r'<img[^>]+src="([^"]+)"', s):
        if src.startswith(('http', 'data:')):
            continue
        p = (PAGES / src).resolve()
        if not p.exists():
            errors.append(f'IMG {f.name} -> {src}')

# ── 4. Structure HTML : balises de base ──
for f in sorted(PAGES.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    for tag in ('<html', '</html>', '<head>', '</head>', '<body', '</body>', '<main', '</main>'):
        if tag not in s:
            errors.append(f'HTML {f.name}: balise manquante {tag}')
    if 'lang="fr"' not in s:
        errors.append(f'HTML {f.name}: attribut lang manquant')
    if '<title>' not in s:
        errors.append(f'HTML {f.name}: title manquant')
    if 'name="description"' not in s:
        errors.append(f'HTML {f.name}: meta description manquante')

# ── 5. JSON ──
for j in sorted((ROOT / 'js').glob('*.json')):
    try:
        json.loads(j.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'JSON {j.name}: {e}')

# ── 6. Favicon : JPG uniquement ──
for f in sorted(PAGES.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    if 'data:image/svg+xml' in s:
        errors.append(f'FAVICON {f.name}: SVG inline present')

print('=' * 62)
print(f'Pages analysees : {len(list(PAGES.glob("*.html")))}')
if errors:
    print(f'ERREURS : {len(errors)}')
    for e in errors[:60]:
        print('  -', e)
else:
    print('Audit statique : AUCUNE erreur')

# ── 7. HTTP ──
print('=' * 62)
codes = {}
for f in sorted(PAGES.glob('*.html')):
    try:
        url = BASE + 'pages/' + urllib.parse.quote(f.name)
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=10) as r:
            codes[f.name] = r.status
    except Exception as e:
        codes[f.name] = str(e)
bad = {k: v for k, v in codes.items() if v != 200}
print(f'Reponses HTTP 200 : {sum(1 for v in codes.values() if v == 200)}/{len(codes)}')
if bad:
    for k, v in bad.items():
        print('  -', k, v)

# ── 8. Racine ──
for f in sorted(ROOT.glob('*.html')):
    try:
        req = urllib.request.Request(BASE + urllib.parse.quote(f.name), method='HEAD')
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f'racine {f.name}: {r.status}')
    except Exception as e:
        print(f'racine {f.name}: {e}')

sys.exit(1 if (errors or bad) else 0)
