#!/usr/bin/env python3
"""Inventaire exhaustif des occurrences d'images site-wide (HTML/CSS/JS/JSON)."""
import re, pathlib, collections, json

ROOT = pathlib.Path('.')
IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)
URL_RE = re.compile(r'["\'(]((?:\.\./)?(?:img|audio)/[A-Za-z0-9_./-]+\.(?:jpg|jpeg|png|webp|svg))["\')]')


def norm(u, base):
    p = pathlib.Path(base).parent / u
    try:
        return str(p.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return u


occ = collections.defaultdict(list)
files = sorted(list(ROOT.rglob('*.html')) + list(ROOT.rglob('*.css'))
               + list(ROOT.rglob('*.js')) + list(ROOT.rglob('*.json')))
for f in files:
    if 'node_modules' in str(f):
        continue
    raw = f.read_text(encoding='utf-8', errors='ignore')
    rel = str(f)
    for m in IMG_TAG.finditer(raw):
        a = re.search(r'src\s*=\s*["\']([^"\']+)', m.group(0))
        if a:
            occ[norm(a.group(1), f)].append((rel, 'img'))
    for m in URL_RE.finditer(raw):
        occ[norm(m.group(1), f)].append((rel, 'ref'))

multi = {k: v for k, v in occ.items() if len(v) > 1}
print('Fichiers image distincts references : %d' % len(occ))
print('References totales : %d' % sum(len(v) for v in occ.values()))
print('Images referencees PLUSIEURS fois : %d' % len(multi))
print()
for k in sorted(multi, key=lambda x: -len(multi[x])):
    pages = sorted(set(p for p, _ in multi[k]))
    print('  %-42s %2d refs | %s' % (k, len(multi[k]), ', '.join(p.replace('pages/', '') for p in pages)))
