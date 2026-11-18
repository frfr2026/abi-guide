#!/usr/bin/env python3
"""Extraction structuree des donnees de cartes officielles du wiki ABI.

Pour chaque carte on recupere :
  - les zones nommees (sections == Description / Localites)
  - les points d'extraction (tableau Extraction Points)
  - les boss
  - la duree et le nombre de joueurs (infobox {{location}})
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
    s = re.sub(r'^\s*\|[^\n]*?(?=\|)', '', s)   # attribut de cellule wiki
    s = s.lstrip('|').strip()
    s = s.replace('ㅤ', ' ')                     # espace invisible wiki
    return re.sub(r'\s+', ' ', s).strip()


def infobox(wt):
    out = {}
    m = re.search(r'\{\{location\s*(.*?)\n\}\}', wt, re.S)
    if m:
        for line in m.group(1).split('\n'):
            if '=' in line:
                k, v = line.split('=', 1)
                out[clean(k)] = clean(v)
    return out


def sections(wt):
    """Renvoie {titre: contenu} pour chaque section de niveau 2."""
    res, cur, buf = {}, None, []
    for line in wt.split('\n'):
        if line.startswith('==') and not line.startswith('==='):
            if cur:
                res[cur] = '\n'.join(buf)
            cur = clean(line.strip('='))
            buf = []
        elif cur is not None:
            buf.append(line)
    if cur:
        res[cur] = '\n'.join(buf)
    return res


def extractions(wt):
    """Extrait les noms d'extraction de la table wikitext."""
    names, m = [], re.search(r'==\s*Extractions\s*==(.*?)(?=\n==[^=]|\Z)', wt, re.S | re.I)
    if not m:
        return names
    tbl = m.group(1)
    for row in re.findall(r'\n\|-\s*\n(.*?)(?=\n\|-|\Z)', tbl, re.S):
        cells = re.split(r'\n\|', row)
        if not cells:
            continue
        first = clean(cells[0])
        if first and len(first) < 60 and not first.startswith('!') and first.lower() != 'name':
            names.append(first)
    return names


def points_of_interest(wt):
    """Section Points Of Interest : zones cles + caracteristiques.

    Formats wiki rencontres :
      <big>Zone</big>          (Valley)
      ===<big>Zone</big>===   (Farm)
    suivi de puces "- ...".
    """
    m = re.search(r'==\s*\'*\'*Points\s*Of\s*Interest\'*\'*\s*==(.*?)(?=\n==[^=]|\Z)', wt, re.S | re.I)
    if not m:
        return []
    body = m.group(1)
    zones = []
    # decoupe sur chaque <big>Nom</big> (que le nom soit encadre de === ou non)
    parts = re.split(r'<big>.*?</big>', body, flags=re.S)
    names = [clean(x) for x in re.findall(r'<big>(.*?)</big>', body, re.S)]
    for idx, name in enumerate(names):
        if not name:
            continue
        chunk = parts[idx + 1] if idx + 1 < len(parts) else ''
        feats = []
        for line in chunk.split('\n'):
            s = line.strip()
            if not s.startswith('-'):
                continue
            feat = clean(s.lstrip('-').strip())
            if feat:
                feats.append(feat)
        zones.append({'name': name, 'features': feats})
    return zones


def bosses(wt):
    m = re.search(r'==\s*Bosses\s*==(.*?)(?=\n==[^=]|\Z)', wt, re.S | re.I)
    if not m:
        return []
    body = m.group(1)
    out = []
    for x in re.findall(r'^\*+\s*<big>\[\[([^\]|]+)', body, re.M):
        out.append(clean(x))
    if not out:
        for x in re.findall(r'^\*+\s*\[\[([^\]|]+)', body, re.M):
            nm = clean(x)
            if nm.lower() not in ('location', 'boss'):
                out.append(nm)
    return out


def zone_links(wt):
    """Liens [[Valley#Villa|Villa]] -> zones internes."""
    seen = []
    for tgt, label in re.findall(r'\[\[([^\]|#]+)(?:#[^\]|]*)?\|([^\]]+)\]\]', wt):
        if label.strip() and label.strip() != tgt.strip():
            seen.append(clean(label))
    return seen


CARDS = ['Valley', 'Farm', 'Northridge', 'TV Station', 'Armory']

if __name__ == '__main__':
    data = {}
    for title in CARDS:
        wt = wikitext(title)
        if not wt:
            print('  ! page introuvable : ' + title)
            continue
        secs = sections(wt)
        desc = ''
        for k, v in secs.items():
            if 'description' in k.lower():
                desc = clean(v)
                break
        data[title] = {
            'infobox': infobox(wt),
            'description': desc,
            'extractions': extractions(wt),
            'bosses': bosses(wt),
            'poi': points_of_interest(wt),
            'zones': zone_links(wt),
            'sections': list(secs.keys()),
        }
        print('### %s' % title)
        print('   infobox : %s' % data[title]['infobox'])
        print('   boss    : %s' % data[title]['bosses'])
        print('   extract : %s' % ', '.join(data[title]['extractions'][:18]))
        print('   POI     : %s' % ' | '.join(z['name'] for z in data[title]['poi'][:20]))
        print('   sections: %s' % ', '.join(data[title]['sections'][:14]))
    pathlib.Path('tools/_map_zones.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    print('\n-> tools/_map_zones.json (%d cartes)' % len(data))
