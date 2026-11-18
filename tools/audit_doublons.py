#!/usr/bin/env python3
"""Audit des images dupliquées : une image ne doit servir qu'une seule fois."""
import re, pathlib, collections

ROOT = pathlib.Path('.')
pages = sorted(ROOT.rglob('*.html'))
css = sorted(ROOT.rglob('css/*.css'))
js = sorted(ROOT.rglob('js/*.js')) + sorted(ROOT.rglob('js/*.json'))

usage = collections.defaultdict(set)      # image -> {pages}
same_page = collections.defaultdict(list)  # image -> [(page, count)]

IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)


def norm(u, base):
    """Resout un chemin d'image relatif vers un chemin relatif a la racine."""
    if not u or u.startswith(('http://', 'https://', 'data:')):
        return None
    if u.startswith('/'):
        p = pathlib.Path(u.lstrip('/'))
    else:
        p = (pathlib.Path(base).parent / u)
    try:
        return str(p.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return None


for f in pages + css + js:
    txt = f.read_text(encoding='utf-8', errors='ignore')
    found = []
    for m in IMG_TAG.finditer(txt):
        tag = m.group(0)
        a = re.search(r'src\s*=\s*["\']([^"\']+)', tag)
        if a:
            found.append(a.group(1))
    for m in re.finditer(r'url\(\s*["\']?([^\)"\']+)', txt):
        found.append(m.group(1))
    # chemins d'images dans les JSON de donnees et les JS
    for m in re.finditer(r'["\']([^"\']*\.(?:jpg|jpeg|png|svg|webp))["\']', txt):
        found.append(m.group(1))
    for u in found:
        p = norm(u, f)
        if p:
            usage[p].add(str(f))

print("=" * 74)
print("AUDIT DES IMAGES DUPLIQUEES")
print("=" * 74)
dups = {k: v for k, v in usage.items() if len(v) > 1}
used_once = {k: v for k, v in usage.items() if len(v) == 1}
unused = []
allimg = {str(p) for p in ROOT.rglob('img/**/*') if p.is_file()}
for p in sorted(allimg - set(usage.keys())):
    unused.append(p)

print(f"Images sur le site        : {len(allimg)}")
print(f"Images referencees        : {len(usage)}")
print(f"  utilisees sur 1 seule page : {len(used_once)}")
print(f"  utilisees sur PLUSIEURS pages : {len(dups)}")
print(f"  jamais referencees       : {len(unused)}")
print()
if dups:
    print("--- DOUBLONS ---")
    for k in sorted(dups, key=lambda x: -len(dups[x])):
        v = sorted(dups[k])
        print(f"  {k}  ({len(v)} pages)")
        for page in v[:12]:
            print(f"      {page}")
        if len(v) > 12:
            print(f"      ... et {len(v)-12} autres")
print()
if unused:
    print("--- JAMAIS REFERENCEES ---")
    for u in unused:
        print("  " + u)
