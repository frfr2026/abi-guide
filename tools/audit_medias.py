#!/usr/bin/env python3
"""Audit complet des medias de /home/user/abi-nexus/img.

Verifie, pour chaque fichier :
  - le format reel (decode) vs l'extension ;
  - les dimensions ;
  - le mode couleur ;
  - la presence de corruption (truncated file) ;
  - le poids par megapixel ;
  - le fait qu'il s'agisse bien d'une photo (variabilite des valeurs) et non
    d'un aplat, d'un placeholder ou d'un logo.

Sert de garde-fou : le site doit n'héberger que du JPEG, et les visuels
editoriaux doivent etre assez grands pour un ecran large.
"""
import pathlib, json, collections
from PIL import Image, ImageStat

ROOT = pathlib.Path('.')
IMG = ROOT / 'img'

SEUIL_EDITORIAL = 1400   # largeur mini pour un visuel de page
SEUIL_ICON = 256         # largeur mini pour une vignette

rows = []
errors = []
by_format = collections.Counter()
by_size = collections.Counter()

for f in sorted(IMG.rglob('*')):
    if not f.is_file():
        continue
    rel = f.relative_to(ROOT).as_posix()
    ext = f.suffix.lower()
    try:
        with Image.open(f) as im:
            im.load()                      # force le decodage complet
            fmt, size, mode = im.format, im.size, im.mode
            # variabilite : ecart-type moyen sur une version reduite
            small = im.convert('L')
            small.thumbnail((160, 160))
            stat = ImageStat.Stat(small)
            stddev = stat.stddev[0] if stat.stddev else 0.0
            w, h = size
    except Exception as e:
        errors.append((rel, 'ILLISIBLE: %s' % e))
        continue

    by_format[fmt] += 1
    real_ext = {'JPEG': '.jpg', 'PNG': '.png', 'WEBP': '.webp', 'GIF': '.gif',
                'SVG': '.svg'}.get(fmt, ext)
    if real_ext != ext:
        errors.append((rel, 'EXTENSION %s != format reel %s' % (ext, fmt)))

    px = w * h
    kb = f.stat().st_size / 1024
    kind = 'editorial' if '/vis-' in rel or '/hero' in rel else 'icone'
    mini = SEUIL_EDITORIAL if kind == 'editorial' else SEUIL_ICON
    if w < mini:
        by_size[kind] += 1

    rows.append({
        'fichier': rel, 'format': fmt, 'l': w, 'h': h, 'mode': mode,
        'ko': round(kb, 1), 'ko_par_mp': round(kb / max(px / 1e6, 0.01), 1),
        'type': kind, 'variabilite': round(stddev, 1),
        'plat': stddev < 3.0,
        'sur_dimens': w > 3000 or h > 3000,
        'poids_faible': kb < 25,
    })

print('=' * 74)
print('AUDIT DES MEDIAS')
print('=' * 74)
print('Fichiers analyses :', len(rows))
print('Formats reels     :', dict(by_format))
print('Errors            :', len(errors))
for r, e in errors[:30]:
    print('   !', r, e)
print()
print('--- Sous-seuil de largeur ---')
print('visuels editoriaux < %d px : %d' % (SEUIL_EDITORIAL, by_size['editorial']))
print('icones           < %d px : %d' % (SEUIL_ICON, by_size['icone']))
print()
print('--- Plats (placeholder / aplat) : variabilite < 3.0 ---')
plats = [r for r in rows if r['plat']]
print('nombre :', len(plats))
for r in plats[:25]:
    print('   -', r['fichier'], r['l'], 'x', r['h'], 'var=%.1f' % r['variabilite'])
print()
print('--- Sur-dimensionnes (> 3000 px) ---')
sd = [r for r in rows if r['sur_dimens']]
print('nombre :', len(sd))
for r in sd[:25]:
    print('   -', r['fichier'], r['l'], 'x', r['h'], '%.0f Ko' % r['ko'])
print()
print('--- Poids faible (< 25 Ko) ---')
pf = [r for r in rows if r['poids_faible']]
print('nombre :', len(pf))
print()
print('--- Meilleures densites (Ko par megapixel) ---')
for r in sorted(rows, key=lambda x: -x['ko_par_mp'])[:8]:
    print('   %7.1f  %s' % (r['ko_par_mp'], r['fichier']))

(ROOT / 'tools' / '_media_audit.json').write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding='utf-8')
print()
print('Detail ecrit dans tools/_media_audit.json')
