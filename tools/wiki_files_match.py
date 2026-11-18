#!/usr/bin/env python3
"""Apparie les entites du site aux fichiers d'artwork officiels du wiki."""
import json, re, pathlib, difflib

ROOT = pathlib.Path('.')
FILES = [l.strip() for l in open('/tmp/wiki_files.txt', encoding='utf-8') if l.strip()]
STEMS = {}
for f in FILES:
    STEMS.setdefault(f[:-4].lower(), f)


def norm(s):
    s = s.lower().replace('&', ' and ')
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r"['’]", '', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    return s


NORM_FILES = {norm(k): v for k, v in STEMS.items()}

# variantes manuelles : nom du site -> nom de fichier wiki
MANUAL = {
    'ak12': 'AK12 Assault Rifle', 'aek971': 'AEK Assault Rifle',
    'pcc9': 'PCC-9 Assault Rifle', 'sj16': 'SJ16 Bolt-Action Rifle',
    'vector45': 'Vector 45 Micro SMG', 'rpk16': 'RPK16 Light Machine Gun',
    'mosin': 'Mosin-Nagant Bolt-Action Rifle', 'usas12': 'USAS-12 Shotgun',
    'kn': 'KN Tactical Helmet', '6b43': '6B43 Body Armor',
    '926composite': '926 Composite Body Armor', 'bt6': 'BT6 Tactical Body Armor',
    'hvk': 'HVK Body Armor', 'bt5': 'BT5 Body Armor',
    '6b12': '6B12 Body Armor', '6b2': '6B2 Body Armor',
    '6b62': '6B62 Body Armor', '6b13': '6B13 Body Armor',
    '6b23': '6B23 Body Armor', '6b45': '6B45 Heavy Body Armor',
    'bt101': 'BT101 Tactical Body Armor',
    'goldbar': 'Gold Bar', 'gpu': 'Graphics Card', 'rolex': 'Gold Watch',
    'morphine': 'Morphine', 'y40': 'Y40 Treatment',
    'flaregun': 'Flare Gun', 'pheromone': 'Type II Lure Pheromone Grenade',
    'healingsmoke': 'Healing Smoke Grenade', 'm290stun': 'M290 Stun Grenade',
    'keycard': 'Keycard', 'medkit': 'IFAK', 'bandage': 'Bandage',
    'mrid': 'Laptop MRID', 'elysium': 'Elysium',
    'northernstars': 'Northern Stars', 'lute': 'Double Neck Lute',
    'jadeflute': 'Emerald Jade Flute', 'militarycircuit': 'Military Circuit',
}


def find(*names):
    for n in names:
        k = norm(n)
        if k in NORM_FILES:
            return NORM_FILES[k]
    return None


def match_weapon(name, cat):
    base = norm(name)
    cands = [base]
    for suf in ['Assault Rifle', 'Marksman Rifle', 'Micro SMG', 'SMG', 'Sniper Rifle',
                'Shotgun', 'Pistol', 'Light Machine Gun', 'Carbine', 'Bolt-Action Rifle']:
        cands.append('%s %s' % (base, suf))
    for c in cands:
        if c in NORM_FILES:
            return NORM_FILES[c]
    for c in cands:
        for k, v in NORM_FILES.items():
            if k.startswith(c + ' '):
                return v
    return None


def match_item(name):
    base = norm(name)
    if base in NORM_FILES:
        return NORM_FILES[base]
    close = difflib.get_close_matches(base, list(NORM_FILES.keys()), n=1, cutoff=0.82)
    if close:
        return NORM_FILES[close[0]]
    for k, v in NORM_FILES.items():
        if k.startswith(base):
            return v
    return None


if __name__ == '__main__':
    out = []
    # armes
    d = json.loads((ROOT / 'js/data-weapons.json').read_text(encoding='utf-8'))
    for e in d['weapons']:
        stem = pathlib.Path(e.get('image', '')).stem
        f = MANUAL.get(stem.lower()) and find(MANUAL[stem.lower()])
        f = f or match_weapon(e['name'], e.get('category', ''))
        out.append({'kind': 'weapon', 'id': e['id'], 'name': e['name'],
                    'image': e.get('image', ''), 'file': f})
    # objets
    d = json.loads((ROOT / 'js/data-items.json').read_text(encoding='utf-8'))
    for e in d['items']:
        stem = pathlib.Path(e.get('image', '')).stem
        f = MANUAL.get(stem.lower()) and find(MANUAL[stem.lower()])
        f = f or match_item(e['name'])
        out.append({'kind': 'item', 'id': e['id'], 'name': e['name'],
                    'image': e.get('image', ''), 'file': f})
    # armures
    d = json.loads((ROOT / 'js/data-armors.json').read_text(encoding='utf-8'))
    for e in d['armors']:
        stem = pathlib.Path(e.get('image', '')).stem
        f = MANUAL.get(stem.lower()) and find(MANUAL[stem.lower()])
        f = f or match_item(e['name'])
        out.append({'kind': 'armor', 'id': e['id'], 'name': e['name'],
                    'image': e.get('image', ''), 'file': f})
    # munitions
    d = json.loads((ROOT / 'js/data-ammo.json').read_text(encoding='utf-8'))
    for e in d['ammo']:
        out.append({'kind': 'ammo', 'id': e['id'], 'name': e['name'],
                    'image': '', 'file': match_item(e['name'])})

    ok = [o for o in out if o['file']]
    ko = [o for o in out if not o['file']]
    print('Couvert par l art officiel : %d / %d' % (len(ok), len(out)))
    from collections import Counter
    c = Counter(o['kind'] for o in ok)
    t = Counter(o['kind'] for o in out)
    for k in t:
        print('  %-7s %2d / %2d' % (k, c[k], t[k]))
    print('\nSANS ART OFFICIEL (%d) :' % len(ko))
    for o in ko:
        print('  %-7s %-28s (%s)' % (o['kind'], o['name'], o['id']))
    json.dump(out, open('tools/_asset_map.json', 'w'), ensure_ascii=False, indent=1)
    print('\n -> tools/_asset_map.json')
