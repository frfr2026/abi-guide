#!/usr/bin/env python3
"""Inventaire image par page + plan de deduplication."""
import re, pathlib, collections, json

ROOT = pathlib.Path('.')
pages = sorted(ROOT.rglob('*.html'))
IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)


def norm(u, base):
    if not u or u.startswith(('http://', 'https://', 'data:')):
        return None
    p = pathlib.Path(base).parent / u
    try:
        return str(p.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return None


page_imgs = collections.defaultdict(list)
for f in pages:
    raw = f.read_text(encoding='utf-8', errors='ignore')
    for m in IMG_TAG.finditer(raw):
        a = re.search(r'src\s*=\s*["\']([^"\']+)', m.group(0))
        if a:
            p = norm(a.group(1), f)
            if p:
                page_imgs[str(f)].append(p)

# images de premier niveau (figures/heros) par page
print('%-52s %s' % ('PAGE', 'IMAGES (hors ui/ et seo/)'))
print('-' * 110)
content_use = collections.defaultdict(set)
for pg in sorted(page_imgs):
    imgs = [i for i in page_imgs[pg]
            if not i.startswith(('img/ui/', 'img/seo/'))]
    for i in page_imgs[pg]:
        content_use[i].add(pg)
    print('%-52s %s' % (pg.replace('pages/', ''), ', '.join(i.replace('img/', '') for i in imgs) or '—'))

print()
print('=' * 110)
shared = {k: v for k, v in content_use.items() if len(v) > 1}
print('Images de contenu utilisees sur plusieurs pages : %d' % len(shared))
for k in sorted(shared, key=lambda x: -len(shared[x])):
    print('  %-40s %d pages' % (k, len(shared[k])))
