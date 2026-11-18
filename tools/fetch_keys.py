#!/usr/bin/env python3
"""Extraction des cles par carte depuis la page Keys du wiki ABI.

Format wiki : |-|<Carte> Keys= ... tableau {| !Icon !Name !Durability !Notes
Chaque cle : nom, durete, contenants debloques.
"""
import json, pathlib, re, urllib.request, urllib.parse

API = 'https://arena-breakout-infinite.fandom.com/api.php'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36'


def api(params):
    q = urllib.parse.urlencode(params)
    r = urllib.request.Request(API + '?' + q, headers={'User-Agent': UA})
    return json.loads(urllib.request.urlopen(r, timeout=45).read().decode())


def wikitext(title):
    d = api({'action': 'parse', 'page': title, 'prop': 'wikitext', 'format': 'json'})
    return d.get('parse', {}).get('wikitext', {}).get('*', '')


def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\{\{[^}]*\}\}', '', s)
    s = s.replace("'''", '').replace("''", '')
    s = re.sub(r'^\s*\|[^\n]*?(?=\|)', '', s)
    s = s.lstrip('|').strip()
    s = s.replace('ㅤ', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def parse_keys_page(wt):
    """-> {carte: [{name, durability, notes}]}"""
    out = {}
    # decoupe par onglet de carte
    parts = re.split(r'\|-\s*\|\s*([A-Za-z0-9 ]+?)\s*Keys\s*=', wt)
    for i in range(1, len(parts) - 1, 2):
        carte = parts[i].strip()
        body = parts[i + 1]
        keys = []
        rows = re.findall(r'\n\|-\s*\n(.*?)(?=\n\|-|\n\|\}|\Z)', body, re.S)
        for row in rows:
            cells = row.split('\n|')
            if len(cells) < 2:
                continue
            # format A : la premiere cellule contient {{ItemLink|...|text=Nom}}
            if '{{ItemLink' in cells[0]:
                m_item = re.search(r'\|text=([^|}]+)', cells[0])
                name = m_item.group(1).strip() if m_item else ''
                rest = cells[1:]
            else:
                name = clean(cells[1])
                # format B : [[Nom de la cle]]
                name = re.sub(r'^\[\[([^\]|]+)(?:\|[^\]]+)?\]\]$', r'\1', name).strip()
                rest = cells[2:]
            dur = clean(rest[0]) if rest else ''
            notes = clean(rest[1]) if len(rest) > 1 else ''
            if not name or name.lower() in ('name', 'item'):
                continue
            m = re.match(r'^(\d+)', dur)
            keys.append({
                'name': name,
                'durability': int(m.group(1)) if m else None,
                'notes': notes,
            })
        if keys:
            out[carte] = keys
    return out


if __name__ == '__main__':
    wt = wikitext('Keys')
    keys = parse_keys_page(wt)
    print('Cartes trouvees : %s' % ', '.join(sorted(keys)))
    for k in sorted(keys):
        print('  %-14s %d cles' % (k, len(keys[k])))
        for kk in keys[k][:3]:
            print('      - %-36s dur=%-5s %s' % (kk['name'], kk['durability'], kk['notes'][:60]))

    src = pathlib.Path('tools/_map_zones.json')
    data = json.loads(src.read_text(encoding='utf-8'))
    for title in data:
        for cand in (title, title.replace('TV Station', 'TV Station'), 'TVStation'):
            if cand in keys:
                data[title]['keys'] = keys[cand]
                break
        data[title].setdefault('keys', [])
    src.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    print('\n-> tools/_map_zones.json mis a jour')
