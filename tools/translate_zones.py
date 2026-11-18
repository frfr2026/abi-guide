#!/usr/bin/env python3
"""Traduit en francais les caracteristiques de zones (issues du wiki anglais)."""
import json, pathlib, re

P = pathlib.Path('tools/_map_zones.json')

TRAD = {
    'loose loot': 'Loot libre',
    'locked office with safe': 'Bureau verrouillé avec coffre',
    'potential extraction': 'Extraction possible',
    'potential boss spawn': 'Spawn de boss possible',
    'main split of the map': 'Bifurcation principale de la carte',
    'large open areas': 'Grandes zones ouvertes',
    'toolboxes': 'Boîtes à outils',
    'safe': 'Coffre-fort',
    'safe (locked room)': 'Coffre-fort (pièce verrouillée)',
    'many loot containers': 'Nombreux conteneurs de loot',
    'multiple loot containers': 'Plusieurs conteneurs de loot',
    'multiple scavangers': 'Plusieurs Scavengers',
    'many scavangers': 'Nombreux Scavengers',
    'multiple safes': 'Plusieurs coffres-forts',
    'extraction point': "Point d'extraction",
    'premium loot': 'Loot premium',
    'military loot': 'Loot militaire',
    'medical loot': 'Loot médical',
    'storage area': 'Zone de stockage',
    'construction site': 'Chantier',
    'loose loot ': 'Loot libre',
    'office areas': 'Zones de bureaux',
    'beds': 'Lits',
    'rare loot spawn': 'Spawn de loot rare',
    'sniper perches': 'Postes de sniper',
    'many loot container': 'Nombreux conteneurs de loot',
    'multiple computers': 'Plusieurs ordinateurs',
    'multiple PCs': 'Plusieurs ordinateurs',
    'document box': 'Boîte à documents',
    'rare spawn on table': 'Spawn rare sur la table',
    'rare spawn on shelf': 'Spawn rare sur l\'étagère',
    "premium weapon container": "Conteneur d'armes premium",
    "premium weapon case": "Mallette d'armes premium",
    'electronic safe': 'Coffre électronique',
    "long weapon box": "Longue boîte d'armes",
    "winter coat": "Manteau d'hiver",
    'working clothes': 'Vêtements de travail',
    'duffle bag': 'Sac de sport',
    'jacket': 'Veste',
    'suitcase': 'Valise',
    'computer': 'Ordinateur',
    'toolbox': 'Boîte à outils',
    "multiple scavangers ": "Plusieurs Scavengers",
    "couple loot containers": "Quelques conteneurs de loot",
    "multiple documents": "Plusieurs documents",
    "documents": "Documents",
    "rare spawn": "Spawn rare",
    "boss spawn": "Spawn de boss",
}

# corrections manuelles de libelles de zones
ZONE_FIX = {
    'Bridge Fracture': 'Bridge Fracture (pont)',
    'Exhibition Coridor': 'Couloir d\'exposition',
    'Villa': 'Villa',
    'Storage': 'Zone de stockage',
}


def tr(s):
    if not s:
        return s
    t = s.strip()
    # retire les liens wiki [[A|B]] -> B, [[A]] -> A
    t = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', t)
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)
    tl = t.lower()
    if tl in TRAD:
        return TRAD[tl]
    # trait par trait
    parts = [p.strip() for p in re.split(r'[;,]', t) if p.strip()]
    out = []
    for p in parts:
        out.append(TRAD.get(p.lower(), p))
    res = ', '.join(out)
    if res == t:
        return t
    return res


if __name__ == '__main__':
    d = json.loads(P.read_text(encoding='utf-8'))
    n = 0
    for carte, info in d.items():
        for z in info.get('poi', []):
            feats = z.get('features', [])
            new = [tr(f) for f in feats]
            if new != feats:
                n += sum(1 for a, b in zip(feats, new) if a != b)
                z['features'] = new
            z['name'] = ZONE_FIX.get(z['name'], z['name'])
    P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
    print('Libelles traduits : %d' % n)
