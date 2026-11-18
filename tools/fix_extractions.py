#!/usr/bin/env python3
"""Corrige les comptes d'extractions et le boss d'Armory, puis enrichit la page.

Source unique et verifiable : wiki officiel Arena Breakout Infinite
(pages Locations, Armory, Farm, Valley, TV Station, Northridge, Bosses, Keys).

Corrections appliquees :
  - les meta descriptions annoncaient des nombres d'extractions errones
    (Armory 9, Farm 14, Valley 12, Northridge 10, TV Station 11, Airport 13)
    alors que le JSON data-maps.json et le wiki officiel donnent
    Armory 3, Farm 8, Valley 8, Northridge 11, TV Station 3 ;
  - la page Armory attribuait le boss Ajax a la carte : Ajax est le boss de
    Farm, Renoir est celui d'Armory (wiki officiel, page Bosses).
"""
import pathlib, re, json

# ── valeurs officielles ─────────────────────────────────────────────────
OFFICIAL = {
    'armory':    {'extractions': 3,  'boss': 'Renoir'},
    'farm':      {'extractions': 8,  'boss': 'Ajax Jones'},
    'valley':    {'extractions': 8,  'boss': 'Doss Anthony'},
    'northridge':{'extractions': 11, 'boss': 'Fred (Frade) Lee'},
    'tvstation': {'extractions': 3,  'boss': 'Kurt Williams / Bernard Martin'},
    'airport':   {'extractions': 4,  'boss': None},
}

PAGES = {
    'map-armory.html':     ('armory',    9,  3),
    'map-farm.html':       ('farm',      14, 8),
    'map-valley.html':     ('valley',    12, 8),
    'map-northridge.html': ('northridge',10, 11),
    'map-tv-station.html': ('tvstation', 11, 3),
    'map-airport.html':    ('airport',   13, 4),
}

for fname, (mid, wrong, right) in PAGES.items():
    p = pathlib.Path('pages') / fname
    s = p.read_text(encoding='utf-8')
    before = s
    # meta description + JSON-LD description : "9 extractions," -> "3 extractions,"
    s = s.replace(f'{wrong} extractions,', f'{right} extractions,')
    # le texte de la section extractions : "9 extractions seulement"
    s = s.replace(f'{wrong} extractions seulement', f'{right} extractions seulement')
    # les chiffres isoles dans un titre/tableau de stats : "Extractions<br>9 —"
    s = s.replace(f'>{wrong} —', f'>{right} —')
    p.write_text(s, encoding='utf-8')
    changed = 'MODIFIE' if s != before else 'inchangé'
    print(f'{fname:22s} {wrong} -> {right}  [{changed}]')

# ── Armory : le boss correct ────────────────────────────────────────────
p = pathlib.Path('pages/map-armory.html')
s = p.read_text(encoding='utf-8')
OLD_BOSS = '''          <div class="callout callout-danger">
            <h3 class="h4">Boss de la carte</h3>
            <p><strong>Ajax</strong> — spawn parmi les points d'intérêt : approchez avec une armure T3 minimum et surveillez le tour de garde.</p>
          </div>'''
if OLD_BOSS in s:
    NEW_BOSS = '''          <div class="callout callout-danger">
            <h3 class="h4">Boss de la carte</h3>
            <p><strong>Renoir</strong> — le boss de l'Armory. Spawn parmi les points d'intérêt : approchez avec une armure T3 minimum et surveillez le tour de garde. Ajax, lui, est le boss de <a href="map-farm.html">Farm</a>.</p>
          </div>'''
    s = s.replace(OLD_BOSS, NEW_BOSS, 1)
    p.write_text(s, encoding='utf-8')
    print('map-armory.html : boss Ajax -> Renoir (corrige)')
else:
    # variante : chercher un bloc Ajax dans une section boss
    m = re.search(r'<h3 class="h4">Boss de la carte</h3>\s*<p>(.*?)</p>', s, re.S)
    if m and 'Ajax' in m.group(1):
        new_p = re.sub(r'<strong>Ajax</strong>',
                       '<strong>Renoir</strong> — le boss de l\'Armory. Spawn parmi les points d\'intérêt : approchez avec une armure T3 minimum et surveillez le tour de garde. Ajax, lui, est le boss de <a href="map-farm.html">Farm</a>',
                       m.group(1))
        s = s[:m.start(1)] + new_p + s[m.end(1):]
        p.write_text(s, encoding='utf-8')
        print('map-armory.html : boss Ajax -> Renoir (variante)')
    else:
        print('map-armory.html : bloc boss non trouve, verifier manuellement')

# ── JSON : boss d'Armory ────────────────────────────────────────────────
jp = pathlib.Path('js/data-maps.json')
d = json.loads(jp.read_text(encoding='utf-8'))
maps = d['maps'] if isinstance(d, dict) and 'maps' in d else d
for m in maps:
    if m.get('id') == 'armory':
        m['boss'] = ['Renoir']
        print('js/data-maps.json : boss armory -> Renoir')
    # verification des comptes d'extractions contre la source officielle
    if m.get('id') in OFFICIAL:
        exp = OFFICIAL[m['id']]['extractions']
        if m.get('extractions') != exp:
            print(f'  ATTENTION {m["id"]}: JSON dit {m.get("extractions")}, wiki dit {exp}')
jp.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('js/data-maps.json : synchronise')
