#!/usr/bin/env python3
"""Audit approfondi du site ABI NEXUS : médias, textes, liens, données, SEO."""
import json, re, struct, pathlib, html
from collections import defaultdict

ROOT = pathlib.Path('.')
errors, warns, info = [], [], []
E, W, I = errors.append, warns.append, info.append

# ─────────────────────────── 1. IMAGES ───────────────────────────
all_img = [p for p in ROOT.rglob('img/**/*') if p.is_file()]
by_ext = defaultdict(list)
for p in all_img:
    by_ext[p.suffix.lower()].append(p)
I(f"Images du site : {len(all_img)}")
for ext in sorted(by_ext):
    n = len(by_ext[ext])
    if ext in ('.png', '.svg'):
        E(f"FORMAT INTERDIT : {n} fichier(s) {ext} — {', '.join(str(x) for x in by_ext[ext][:5])}")
    elif ext in ('.jpg', '.jpeg'):
        I(f"  {ext} : {n}")
    else:
        W(f"Format d'image inhabituel : {n} x {ext}")


def jpeg_dims(data):
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1; continue
        m = data[i+1]
        if m in (0xC0,0xC1,0xC2,0xC3,0xC5,0xC6,0xC7,0xC9,0xCA,0xCB):
            h, w = struct.unpack('>HH', data[i+5:i+9]); return w, h
        if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
            i += 2; continue
        if i + 4 > len(data): break
        seg = struct.unpack('>H', data[i+2:i+4])[0]
        if seg == 0: return None, None
        i += 2 + seg
    return None, None


bad_jpeg, small_jpeg = [], []
for p in by_ext.get('.jpg', []) + by_ext.get('.jpeg', []):
    d = p.read_bytes()
    if not (d[:2] == b'\xff\xd8' and d[-2:] == b'\xff\xd9'):
        bad_jpeg.append(p); continue
    w, h = jpeg_dims(d)
    if not w or not h: bad_jpeg.append(p)
    elif w < 1200 and h < 1200 and 'favicon' not in str(p) and 'icon' not in str(p):
        small_jpeg.append((p, w, h))
for p in bad_jpeg: E(f"JPEG invalide ou tronque : {p}")
if not bad_jpeg: I(f"  {len(by_ext.get('.jpg',[]))+len(by_ext.get('.jpeg',[]))} JPG : signature FFD8...FFD9 et dimensions lisibles")
if small_jpeg:
    for p, w, h in small_jpeg: W(f"Image de faible resolution : {p} ({w}x{h})")
else: I("  Resolution : toutes les images de contenu >= 1200 px sur les deux cotes")

html_files = sorted(ROOT.rglob('*.html'))
css_files = sorted(ROOT.rglob('css/*.css'))
js_files = sorted(ROOT.rglob('js/*.js'))
json_files = sorted(ROOT.rglob('js/*.json'))
text_files = html_files + css_files + js_files + json_files + [ROOT/'manifest.json']

referenced = set()
IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)
TEMPLATE = re.compile(r'\$\{[^}]*\}')          # littéraux de template JS : ignorés
for f in text_files:
    txt = TEMPLATE.sub(' ', f.read_text(encoding='utf-8', errors='ignore'))
    for m in IMG_TAG.finditer(txt):
        tag = m.group(0)
        for attr in ('src', 'data-src', 'srcset'):
            a = re.search(attr + r'\s*=\s*["\']([^"\']+)', tag)
            if a:
                for u in a.group(1).split(','):
                    u = u.strip().split(' ')[0]
                    if u and not u.startswith(('http', 'data:', '#', '$')):
                        referenced.add((f, u, False))
    for m in re.finditer(r'url\(\s*["\']?([^\)"\']+)', txt):
        u = m.group(1).strip()
        if u and not u.startswith(('http', 'data:', '$')): referenced.add((f, u, False))
    for m in re.finditer(r'["\']([^"\'$]*\.(?:jpg|jpeg|png|svg|webp))["\']', txt):
        u = m.group(1).strip()
        if not u: continue
        if u.startswith('https://abinexus.fr/'):
            referenced.add((f, u[len('https://abinexus.fr/'):], True))
        elif not u.startswith(('http', 'data:')):
            referenced.add((f, u, False))
    for m in re.finditer(r'(?:og:image|twitter:image)["\']?\s*[:=]\s*["\']([^"\']+)', txt):
        u = m.group(1)
        if not u: continue
        if u.startswith('https://abinexus.fr/'):
            referenced.add((f, u[len('https://abinexus.fr/'):], True))
        elif not u.startswith(('http', 'data:')):
            referenced.add((f, u, False))

resolved, missing_ref = set(), []
for f, u, is_root in referenced:
    if is_root or u.startswith('/'):
        tgt = (ROOT / u.lstrip('/')).resolve()
    else:
        tgt = (f.parent / u).resolve()
    try: rel = str(tgt.relative_to(ROOT.resolve()))
    except ValueError: missing_ref.append((f, u, 'hors site')); continue
    if not tgt.exists(): missing_ref.append((f, u, 'fichier absent'))
    else: resolved.add(rel)
for f, u, why in missing_ref[:20]: E(f"Reference media cassee : {f} -> {u} ({why})")
if not missing_ref: I(f"  References media : {len(referenced)} verifiees, 0 cassee")

orphans = [str(p) for p in all_img if str(p) not in resolved]
for o in orphans[:20]: W(f"Image orpheline (jamais referencee) : {o}")
I(f"  Images orphelines : {len(orphans)}")

# ─────────────────────────── 2. AUDIO ───────────────────────────
aud_files = [p for p in ROOT.rglob('audio/*') if p.is_file()]
I(f"audios : {len(aud_files)}")
audio_ref = set()
for f in text_files:
    txt = TEMPLATE.sub(' ', f.read_text(encoding='utf-8', errors='ignore'))
    for m in re.finditer(r'["\']([^"\'$]*\.(?:mp3|wav|ogg|m4a|flac|aac))["\']', txt):
        u = m.group(1)
        if not u.startswith(('http', 'data:')): audio_ref.add((f, u))
for f, u in audio_ref:
    if not (f.parent / u).resolve().exists(): E(f"Reference audio cassee : {f} -> {u}")
for p in aud_files:
    d = p.read_bytes()
    if p.suffix.lower() == '.mp3':
        if not (d[:3] == b'ID3' or d[:2] in (b'\xff\xfb', b'\xff\xf3', b'\xff\xf2')):
            W(f"MP3 sans en-tete valide : {p}")
        if len(d) < 20000: W(f"MP3 suspicieusement court : {p} ({len(d)} o)")
I(f"  References audio : {len(audio_ref)} verifiees, toutes presentes")

# ─────────────────────────── 3. TEXTES ───────────────────────────
CJK = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uac00-\ud7af]')
DRAFT = re.compile(r'lorem ipsum|placeholder|\bTODO\b|\bFIXME\b|\bXXX\b|\bTBD\b|à compléter|a completer|bientôt disponible|coming soon|texte de substitution|dummy sample', re.I)
empty_tags, multi_space = [], []
for f in html_files:
    raw = f.read_text(encoding='utf-8')
    stripped = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', raw, flags=re.S | re.I)
    body = html.unescape(re.sub(r'<[^>]+>', ' ', stripped))
    if CJK.search(body): E(f"Caractere CJK detecte dans {f}")
    for m in DRAFT.finditer(body): E(f"Marqueur de brouillon dans {f} : '{m.group(0)}'")
    for tag in ('h1','h2','h3','h4','h5','p','li','td','th'):
        for m in re.finditer(r'<' + tag + r'\b[^>]*>(.*?)</' + tag + r'>', raw, re.S | re.I):
            inner = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
            if not inner: empty_tags.append((f, tag))
    # espaces multiples : examine chaque noeud de texte isole (hors indentation).
    # On neutralise d'abord les retours a la ligne + indentation du code source
    # (que le navigateur reduit de toute facon) : seuls les doubles espaces
    # reellement ecrits dans le texte sont signales.
    for m in re.finditer(r'>([^<>]+)<', stripped):
        node = m.group(1)
        if not node.strip(): continue
        core = re.sub(r'\s*\n\s*', ' ', node).strip()
        if re.search(r'[ \t]{2,}', core): multi_space.append((f, core[:50]))
for f, tag in empty_tags[:15]: E(f"Balise <{tag}> vide dans {f}")
if not empty_tags: I("  Aucun h1/h2/h3/h4/h5/p/li/td/th vide")
if multi_space:
    for f, s in multi_space[:10]: W(f"Espaces multiples dans un noeud de texte : {f} ('{s}')")
    I(f"  Noeuds de texte avec espaces multiples : {len(multi_space)}")
else: I("  Aucun noeud de texte avec espaces multiples")

titles, descs = defaultdict(list), defaultdict(list)
for f in html_files:
    raw = f.read_text(encoding='utf-8')
    t = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', raw, re.S)
    if t: titles[html.unescape(t.group(1)).strip()].append(str(f))
    if d: descs[html.unescape(d.group(1)).strip()].append(str(f))
for k, v in titles.items():
    if len(v) > 1: E(f"Titre duplique ({len(v)} pages) : '{k[:60]}'")
for k, v in descs.items():
    if len(v) > 1: E(f"Description dupliquee ({len(v)} pages) : '{k[:60]}'")
I(f"  Titres uniques {len(titles)}/{len(html_files)} | Descriptions uniques {len(descs)}/{len(html_files)}")

# ─────────────────────────── 4. LIENS ───────────────────────────
internal, broken = set(), []
for f in html_files:
    raw = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<a\b[^>]*href\s*=\s*["\']([^"\']+)["\']', raw, re.I):
        h = m.group(1).strip()
        if h.startswith(('http://','https://','mailto:','tel:','#','javascript:')): continue
        internal.add((str(f), h))
        tgt, _, frag = h.partition('#')
        if not tgt:
            if frag and f'id="{frag}"' not in raw: broken.append((f, h, 'ancre absente'))
            continue
        p = (pathlib.Path(f).parent / tgt).resolve()
        if not p.exists(): broken.append((f, h, 'fichier absent'))
        elif frag:
            if f'id="{frag}"' not in p.read_text(encoding='utf-8', errors='ignore'):
                broken.append((f, h, 'ancre absente'))
for f, h, why in broken[:20]: E(f"Lien interne casse : {f} -> {h} ({why})")
if not broken: I(f"  Liens internes : {len(internal)} verifies, 0 casse")

# ─────────────────────────── 5. JSON / DONNEES ───────────────────────────
for jf in json_files + [ROOT/'manifest.json']:
    try: json.loads(jf.read_text(encoding='utf-8'))
    except Exception as e: E(f"JSON invalide : {jf} — {e}")
I(f"  Fichiers JSON : {len(json_files)+1} valides")
# data-ammo.json n'est jamais rendu en carte image (tableaux + simulateur
# balistique) : il est volontairement sans visuel.
IMAGE_CARD_DATASETS = (('js/data-weapons.json','weapons'), ('js/data-items.json','items'),
                       ('js/data-armors.json','armors'), ('js/data-maps.json','maps'))
for name, key in IMAGE_CARD_DATASETS:
    p = ROOT/name
    if not p.exists(): continue
    d = json.loads(p.read_text(encoding='utf-8'))
    items = d.get(key) or []
    if not items: continue
    noimg = [i.get('id','?') for i in items if not i.get('image')]
    pend  = [i.get('id','?') for i in items if i.get('imagePending')]
    if noimg: E(f"{name} : {len(noimg)} sans image : {noimg}")
    if pend: E(f"{name} : {len(pend)} imagePending residuel : {pend}")
    if not noimg and not pend: I(f"  {name} : {len(items)}/{len(items)} avec photo reelle, 0 imagePending")

# ─────────────────────────── 6. SEO / HEAD ───────────────────────────
for f in html_files:
    raw = f.read_text(encoding='utf-8')
    if f.name == '404.html':
        if 'noindex' not in raw: E("404.html sans noindex")
        continue
    if raw.count('<h1') != 1: E(f"{f} : {raw.count('<h1')} H1")
    for tag, label in (('<title', 'title'), ('name="description"', 'meta description'),
                       ('rel="canonical"', 'canonical'), ('application/ld+json', 'JSON-LD')):
        if tag not in raw: E(f"{f} : pas de {label}")
    t = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    if t and len(html.unescape(t.group(1))) > 70: W(f"{f} : title trop long ({len(html.unescape(t.group(1)))})")
    d = re.search(r'<meta name="description" content="(.*?)"', raw, re.S)
    if d and len(html.unescape(d.group(1))) > 175: W(f"{f} : description trop longue")
    if re.search(r'<img\b(?![^>]*\balt=)[^>]*>', raw, re.I): E(f"{f} : <img> sans alt")
    if re.search(r'<img\b(?![^>]*\bloading=)[^>]*>', raw, re.I): E(f"{f} : <img> sans loading")

sm = (ROOT/'sitemap.xml').read_text(encoding='utf-8')
locs = re.findall(r'<loc>([^<]+)</loc>', sm)
I(f"  sitemap : {len(locs)} URL")
for u in locs:
    rel = u.replace('https://abinexus.fr/', '').lstrip('/')
    if not (ROOT/rel if rel else ROOT/'index.html').exists(): E(f"sitemap : URL sans fichier : {u}")
if any('404' in u for u in locs): E("sitemap : 404.html ne doit pas y figurer")

# index de recherche : tableau de tuples -> capturer jusqu'a la fermeture du tableau
sj = (ROOT/'js/search.js').read_text(encoding='utf-8')
start = sj.find('const PAGES')
if start != -1:
    depth, i = 0, sj.find('[', start)
    for j in range(i, len(sj)):
        if sj[j] == '[': depth += 1
        elif sj[j] == ']':
            depth -= 1
            if depth == 0: break
    block = sj[i:j+1]
    raw_listed = {m.group(1) for m in re.finditer(r"['\"]([^'\"]+\.html)['\"]", block)}
    root_entries = {p for p in raw_listed if p.startswith('/')}
    listed = {('pages/' + p) for p in raw_listed if not p.startswith('/')}
    actual = {str(p.relative_to(ROOT)) for p in html_files if p.parent.name == 'pages'} | {'index.html'}
    for r in root_entries:
        if not (ROOT / r.lstrip('/')).exists(): E(f"js/search.js : page racine inexistante : {r}")
        actual.discard(r.lstrip('/'))
    miss, extra = actual - listed, listed - actual
    if miss: E(f"js/search.js : {len(miss)} page(s) non indexee(s) : {sorted(miss)[:6]}")
    if extra: E(f"js/search.js : {len(extra)} page(s) en trop : {sorted(extra)[:6]}")
    if not miss and not extra: I(f"  Index de recherche : {len(actual)} pages, 0 derive")

# navigation
nav_links = set()
for f in html_files:
    raw = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<nav\b.*?</nav>', raw, re.S | re.I):
        for a in re.finditer(r'href\s*=\s*["\']([^"\']+\.html)["\']', m.group(0)):
            nav_links.add(a.group(1))
pages_set = {p.name for p in html_files if p.parent.name == 'pages'}
orphan_nav = pages_set - nav_links
I(f"  Pages 'pages/' hors navigation principale : {len(orphan_nav)} {sorted(orphan_nav) if orphan_nav else ''}")

# ─────────────────────────── RAPPORT ───────────────────────────
print("=" * 72)
print("AUDIT APPROFONDI ABI NEXUS")
print("=" * 72)
for i in info: print("  i", i)
print("-" * 72)
for w in warns: print("  !", w)
print("-" * 72)
for e in errors: print("  X", e)
print("=" * 72)
print(f"ERREURS : {len(errors)} | AVERTISSEMENTS : {len(warns)}")
