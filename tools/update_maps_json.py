#!/usr/bin/env python3
"""Met a jour js/data-maps.json avec les donnees officielles du wiki ABI."""
import json, pathlib

ROOT = pathlib.Path('.')
P = ROOT / 'js/data-maps.json'
Z = json.loads((ROOT / 'tools/_map_zones.json').read_text(encoding='utf-8'))

WIKI = {'farm': 'Farm', 'valley': 'Valley', 'northridge': 'Northridge',
        'tvstation': 'TV Station', 'armory': 'Armory', 'airport': 'Airport'}

EXTRA = {
    'farm': {'extractions': 8, 'difficulty': 'Facile', 'players': 12, 'duration': '30 min'},
    'valley': {'extractions': 8, 'difficulty': 'Moyenne', 'players': 20, 'duration': '30 min'},
    'northridge': {'extractions': 11, 'difficulty': 'Difficile', 'players': 20, 'duration': '30 min'},
    'tvstation': {'extractions': 3, 'difficulty': 'Moyenne', 'players': 12, 'duration': '20 min'},
    'armory': {'extractions': 3, 'difficulty': 'Moyenne', 'players': 12, 'duration': '20 min'},
    'airport': {'extractions': 4, 'difficulty': 'Difficile', 'players': 12, 'duration': '30 min'},
}

if __name__ == '__main__':
    d = json.loads(P.read_text(encoding='utf-8'))
    for m in d['maps']:
        wid = WIKI.get(m['id'])
        if not wid:
            continue
        w = Z.get(wid, {})
        ex = EXTRA.get(m['id'], {})
        m['extractions'] = ex.get('extractions', m.get('extractions'))
        m['players'] = ex.get('players')
        m['duration'] = ex.get('duration')
        m['extractionNames'] = w.get('extractions', [])
        m['zones'] = [z['name'] for z in w.get('poi', [])]
        m['zoneDetails'] = [{'name': z['name'], 'features': z.get('features', [])} for z in w.get('poi', [])]
        m['keys'] = [{'name': k['name'], 'durability': k.get('durability')} for k in w.get('keys', [])]
        m['boss'] = w.get('bosses', [])
        m['officialDescription'] = w.get('description', '')
        m['imageSource'] = 'officielle'
        m['interactiveMap'] = 'https://maps.tcno.co/abi/' + {
            'farm': 'farm', 'valley': 'valley', 'northridge': 'northridge',
            'tvstation': 'tv-station', 'armory': 'armory', 'airport': 'airport'}[m['id']]
        m['referenceMaps'] = 'https://abibuilder.com/maps'

    d['meta']['visualStatus'] = ('6/6 cartes avec la carte officielle du jeu '
                                 '(wiki ABI, JPG 1920x1080). No Man\'s Land est un '
                                 'mode PvE a ticket, pas une carte : il fait tourner '
                                 'Farm, Valley et TV Station.')
    d['meta']['dataStatus'] = ('Zones, extractions, cles et boss releves sur la '
                                'base officielle du wiki ABI.')
    P.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for m in d['maps']:
        print('  %-12s %2d zones, %2d extractions, %2d cles, boss=%s' % (
            m['id'], len(m.get('zones', [])), len(m.get('extractionNames', [])),
            len(m.get('keys', [])), ','.join(m.get('boss', [])) or '—'))
