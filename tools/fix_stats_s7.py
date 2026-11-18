#!/usr/bin/env python3
"""Corrige les statistiques des deux armes de la Saison 7 (A545, AK-15SC).

Le site portait deux valeurs contradictoires pour l'A545 : 700 RPM dans les
donnees structurees et la page fusils d'assaut, 900 RPM dans le rappel "Meta
complet" repete sur huit pages. La fiche de reference de la communaute
(abibuilder.com/wiki/weapons/a545-assault-rifle) donne 900 RPM, ce que
corroborent le wiki NamuWiki (900 rpm) et l'analyse de marche du 24 aout 2026
(900 RPM). L'AK-15SC etait a 600 RPM sur le site, contre 730 RPM documentees.

Ces deux armes n'existaient pas dans la base de 77 armes extraite du wiki
Fandom : leurs statistiques venaient donc d'une source differente, et
l'heterogeneite a produit l'ecart. On les aligne sur la meme source que les
autres, et on conserve la source dans le JSON.

Idempotent.
"""
import json, pathlib, re

# ── 1. donnees structurees ────────────────────────────────────────────────
J = pathlib.Path('js/data-weapons.json')
d = json.loads(J.read_text(encoding='utf-8'))

# id -> (rpm, recul vertical, recul horizontal, ergonomie, precision,
#        stabilite, stabilite hipfire, portee, vitesse du projectile, modes)
STATS = {
    'a545': {
        'rpm': 900,
        'statsWiki': {
            'reculVertical': 77, 'reculHorizontal': 63, 'ergonomie': 70,
            'precision': 65, 'stabilite': 60, 'stabiliteHipfire': 61,
            'portee': 48, 'vitesseProjectile': 880, 'cadence': 900,
            'poids': None, 'modes': ['Semi-automatique', 'Rafale 2 balles', 'Automatique'],
            'caliberWiki': '5.45×39mm', 'categorieWiki': 'Assault Rifles',
        },
    },
    'ak15sc': {
        'rpm': 730,
        'statsWiki': {
            'reculVertical': 65, 'reculHorizontal': 56, 'ergonomie': 72,
            'precision': 44, 'stabilite': 46, 'stabiliteHipfire': 66,
            'portee': 44, 'vitesseProjectile': 710, 'cadence': 730,
            'poids': None, 'modes': ['Semi-automatique', 'Automatique'],
            'caliberWiki': '7.62×39mm', 'categorieWiki': 'Assault Rifles',
        },
    },
}

n = 0
for w in d['weapons']:
    if w['id'] in STATS:
        st = STATS[w['id']]
        w['rpm'] = st['rpm']
        w['statsWiki'] = st['statsWiki']
        w['sourceStats'] = 'A545 et AK-15SC : fiche de reference communautaire (abibuilder.com/wiki), absentes du wiki Fandom'
        n += 1
        print('  %-8s rpm -> %d' % (w['id'], st['rpm']))

d['meta']['updated'] = '2026-11-17'
d['meta']['recale'] = (
    'Les 24 armes du catalogue local : les statistiques completes de la source de '
    'reference sont ajoutees sous "statsWiki". A545 et AK-15SC (nouvelles armes S7, '
    'absentes du wiki Fandom) sont alignees sur la fiche de reference communautaire. '
    'Le catalogue complet des 77 armes documentees est dans js/data-weapons-wiki.json.')
J.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
print('js/data-weapons.json : %d arme(s) recalee(s)' % n)

# ── 2. pages ──────────────────────────────────────────────────────────────
PAGE_FIX = {
    'armes-fusils-assaut.html': [
        ('<strong>A545</strong> (nouveau apex S7, 700 RPM, comparable U191/H416)',
         '<strong>A545</strong> (nouveau apex S7, 900 RPM, comparable U191/H416)'),
    ],
    'saison7-balance-changes.html': [
        ('A545 (700 RPM) vs H416 (800 RPM)', 'A545 (900 RPM) vs H416 (800 RPM)'),
    ],
}
for f, pairs in PAGE_FIX.items():
    p = pathlib.Path('pages') / f
    s = p.read_text(encoding='utf-8')
    c = 0
    for old, new in pairs:
        if old in s:
            c += s.count(old)
            s = s.replace(old, new)
    if c:
        p.write_text(s, encoding='utf-8')
        print('  %-30s %d correction(s)' % (f, c))

# ── 3. controle global : plus aucune valeur A545 contradictoire ──────────
bad = []
for p in list(pathlib.Path('pages').glob('*.html')) + [J]:
    s = p.read_text(encoding='utf-8')
    for m in re.finditer(r'A545[^<]{0,60}?(\d{3})\s*RPM', s):
        if m.group(1) != '900':
            bad.append((p.name, m.group(0)[:70]))
print('\nvaleurs A545 non conformes :', len(bad))
for b in bad:
    print('   ', b)
