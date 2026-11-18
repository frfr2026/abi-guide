#!/usr/bin/env python3
"""Recale js/data-weapons.json avec le catalogue de reference du wiki ABI.

Constat : le site ne documente que 24 armes, alors que la source de reference
en documente 77. Les 24 locales sont l'edition complete (tier, prix, photo,
description) ; les 53 autres n'existent que sous forme de statistiques brutes.

Le recalage se fait en deux temps, et volontairement sans toucher au fichier
consomme par les modules interactifs :

  1. js/data-weapons-wiki.json (nouveau) : les 77 armes, en nomenclature du
     wiki, avec les statistiques completes (recul vertical et horizontal,
     stabilite, precision, stabilite a l'hipfire, portee, vitesse du projectile,
     cadence, poids) et la source explicitement notee "documentee".

  2. js/data-weapons.json : les 24 armes locales recoivent en plus un bloc
     "statsWiki" strictement additif. Aucun champ existant n'est modifie, donc
     la tier list, l'optimiseur, le comparateur et le builder ne changent pas
     de comportement.

Cinq armes du wiki n'avaient pas de categorie : leur nom de base ne se termine
par aucune des categories connues ("Micro SMG", "Lever-Action Rifle", et un
pistolet prefixe par "Gold"). Elles sont recategorisees a la main.

Idempotent.
"""
import json, pathlib, re, unicodedata

ROOT = pathlib.Path('.')
LOCAL = ROOT / 'js' / 'data-weapons.json'
WIKI_IN = pathlib.Path('/tmp/wiki_weapons_full.json')
OUT = ROOT / 'js' / 'data-weapons-wiki.json'

if not WIKI_IN.exists():
    raise SystemExit('source absente : /tmp/wiki_weapons_full.json')

wiki = json.loads(WIKI_IN.read_text(encoding='utf-8'))

# ── categories ────────────────────────────────────────────────────────────
CAT = {
    'Assault Rifles': "Fusil d'assaut",
    'Submachine Guns': 'SMG',
    'Pistols': 'Pistolet',
    'Carbines': 'Carabine',
    'Marksman Rifles': 'DMR',
    'Shotguns': 'Shotgun',
    'Light Machine Guns': 'LMG',
}
# Recategorisation manuelle des cinq entrees sans categorie.
CAT_FIX = {
    'ump45': 'SMG',            # UMP45 Micro SMG
    'vector45': 'SMG',         # Vector 45 Micro SMG
    'vector9': 'SMG',          # Vector 9 Micro SMG
    'ml': 'Sniper',            # ML Lever-Action Rifle : accuracite 86, portee 64
    'gold_desert_eagle': 'Pistolet',
}
# Les trois fusils a verrou : le site les classe en "Sniper".
CAT_BOLT = {'m24', 'mosin', 'sj16'}

MODE_FR = {
    'Semi': ['Semi-automatique'],
    'Full': ['Automatique'],
    'Semi, Full': ['Semi-automatique', 'Automatique'],
    'Fully Automatic': ['Automatique'],
    'Bolt-Action': ['Manuel'],
    'Pump-Action': ['Manuel'],
    'Burst': ['Rafale'],
    '2 Round Burst': ['Rafale 2 balles'],
    '3 Round Burst': ['Rafale 3 balles'],
    '2 Round Burst, Semi, Full': ['Rafale 2 balles', 'Semi-automatique', 'Automatique'],
    '3 Round Burst, Semi, Full': ['Rafale 3 balles', 'Semi-automatique', 'Automatique'],
    'Semi, 3 Round Burst': ['Semi-automatique', 'Rafale 3 balles'],
}

CAL_FR = {
    '5.56x45mm': '5.56×45mm', '9x19mm': '9×19mm', '7.62x51mm': '7.62×51mm',
    '.45 Caliber': '.45 ACP', '7.62x39mm': '7.62×39mm', '5.45x39mm': '5.45×39mm',
    '5.8x42mm': '5.8×42mm', '7.62x25mm': '7.62×25mm', '12x70mm': '12×70mm',
    '5.7x28mm': '5.7×28mm', '7.62x54mm': '7.62×54mm', '.44 Caliber': '.44 Magnum',
    '9x39mm': '9×39mm', '.338 Caliber': '.338 Lapua',
}


def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]', '', s.lower())


def short_name(nom, cat_en):
    """Retire le suffixe de categorie du nom complet du wiki."""
    n = nom
    for suf in (' Micro SMG', ' Assault Rifle', ' Submachine Gun', ' Marksman Rifle',
                ' Bolt-Action Rifle', ' Lever-Action Rifle', ' Pump-Action Shotgun',
                ' Shotgun', ' Pistol', ' Sniper Rifle', ' Carabine Rifle',
                ' Light Machine Gun', ' Automatic Rifle', ' Carbine'):
        if n.endswith(suf):
            return n[:-len(suf)].strip()
    return n


def category_of(wid, v):
    if wid in CAT_FIX:
        return CAT_FIX[wid]
    c = CAT.get(v['categorie'])
    if c is None:
        raise SystemExit('categorie inconnue pour %s : %r' % (wid, v['categorie']))
    if wid in CAT_BOLT:
        return 'Sniper'
    return c


def modes_of(m):
    parts = [p.strip() for p in m.split(',')]
    out = []
    for p in parts:
        out.extend(MODE_FR.get(p, [p]))
    return out


# ── 1. construction du catalogue complet ──────────────────────────────────
catalogue = []
for wid, v in wiki.items():
    catalogue.append({
        'id': v['id'],
        'name': short_name(v['nom'], v['categorie']),
        'nomComplet': v['nom'],
        'category': category_of(v['id'], v),
        'categorieWiki': v['categorie'] or CAT_FIX.get(v['id'], ''),
        'caliber': CAL_FR.get(v['calibre'], v['calibre']),
        'modes': modes_of(v['mode']),
        'poids': float(v['poids']),
        'stats': {
            'reculVertical': int(v['recul_v']),
            'reculHorizontal': int(v['recul_h']),
            'ergonomie': int(v['ergonomie']),
            'stabilite': int(v['stabilite']),
            'precision': int(v['precision']),
            'stabiliteHipfire': int(v['stab_hip']),
            'portee': int(v['portee']),
            'vitesseProjectile': int(v['vitesse']),
            'cadence': int(v['cadence']),
        },
        'source': 'wiki',
    })

catalogue.sort(key=lambda x: (x['category'], x['name'].lower()))

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    'meta': {
        'game': 'Arena Breakout Infinite',
        'source': 'Wiki ABI de reference (Fandom) — donnee documentee, non publiee par l\'editeur',
        'updated': '2026-11-17',
        'count': len(catalogue),
        'note': ('Catalogue complet des armes documentees par la source de reference. '
                 'Les statistiques sont sur une echelle de 0 a 100, sauf la cadence (tours/min), '
                 'la vitesse du projectile (m/s) et le poids (kg). Aucun tier ni prix : '
                 'ces valeurs ne sont pas documentees par cette source et restent '
                 'reservees au catalogue local de js/data-weapons.json.'),
    },
    'weapons': catalogue,
}, ensure_ascii=False, indent=1), encoding='utf-8')

print('%s : catalogue de %d armes ecrit' % (OUT, len(catalogue)))

# ── 2. enrichissement additif du catalogue local ──────────────────────────
local = json.loads(LOCAL.read_text(encoding='utf-8'))
by_norm = {norm(c['name']): c for c in catalogue}
ALIAS = {'vector': 'Vector 45', 'ak15sc': 'AK-15SC', 'aek971': 'AEK-971',
         'pcc9': 'PCC-9', 'usas12': 'USAS-12', 'sj16': 'SJ16',
         'mosin': 'Mosin-Nagant', 'sks': 'SKS'}

linked = 0
for w in local['weapons']:
    key = ALIAS.get(w['id'], w['name'])
    c = by_norm.get(norm(key))
    if not c:
        continue
    w['statsWiki'] = dict(c['stats'], poids=c['poids'], modes=c['modes'],
                          caliberWiki=c['caliber'], categorieWiki=c['categorieWiki'])
    linked += 1

# les armes locales absentes du wiki le sont signale
for w in local['weapons']:
    if 'statsWiki' not in w:
        w['sourceStats'] = 'absente de la source de reference'

local['meta']['recale'] = (
    '%d armes locales sur %d : les statistiques completes de la source de '
    'reference sont ajoutees sous "statsWiki". Le catalogue complet des %d '
    'armes documentees est dans js/data-weapons-wiki.json.'
    % (linked, len(local['weapons']), len(catalogue)))
local['meta']['updated'] = '2026-11-17'
LOCAL.write_text(json.dumps(local, ensure_ascii=False, indent=1), encoding='utf-8')

print('js/data-weapons.json : %d/%d armes enrichies en statsWiki' % (linked, len(local['weapons'])))
print('sans correspondant wiki :', [w['id'] for w in local['weapons'] if 'statsWiki' not in w])
