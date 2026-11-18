#!/usr/bin/env python3
"""Recuperation des artworks officiels ABI depuis le wiki MediaWiki.

Correspondance entre les entites du site (armes, objets, armures, munitions)
et les pages du wiki, puis telechargement de l'image de lead et conversion
en JPG haute qualite (le site ne doit contenir que du JPG).
"""
import json, re, pathlib, urllib.request, urllib.parse, time, io, sys

API = 'https://arena-breakout-infinite.fandom.com/api.php'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
ROOT = pathlib.Path('.')


def api(params, tries=3):
    q = urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            req = urllib.request.Request(API + '?' + q, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as e:
            if i == tries - 1:
                print('  ! api echoue:', e, file=sys.stderr)
                return None
            time.sleep(2 + i * 2)


def all_pages():
    out, cont = [], {}
    while True:
        p = {'action': 'query', 'list': 'allpages', 'aplimit': '500',
             'apnamespace': '0', 'format': 'json'}
        p.update(cont)
        d = api(p)
        if not d:
            break
        out += [x['title'] for x in d['query']['allpages']]
        if 'continue' in d:
            cont = d['continue']
        else:
            break
    return out


def lead_image(title):
    """Renvoie (url, largeur, hauteur) de l'image principale d'une page."""
    d = api({'action': 'query', 'titles': title, 'prop': 'pageimages',
             'piprop': 'original', 'format': 'json'})
    if not d:
        return None
    pages = d.get('query', {}).get('pages', {})
    for _, pg in pages.items():
        orig = pg.get('original')
        if orig:
            return orig.get('source'), orig.get('width'), orig.get('height')
    return None


def imageinfo_url(filename):
    d = api({'action': 'query', 'titles': 'File:' + filename,
             'prop': 'imageinfo', 'iiprop': 'url|size|mime', 'format': 'json'})
    if not d:
        return None
    for _, pg in d.get('query', {}).get('pages', {}).items():
        ii = pg.get('imageinfo')
        if ii:
            return ii[0].get('url'), ii[0].get('width'), ii[0].get('height')
    return None


def build_index():
    """Table de correspondance : cle normalisee -> titre de page wiki."""
    idx = {}
    for title in all_pages():
        key = normalize(title)
        idx.setdefault(key, title)
    return idx


def normalize(s):
    s = s.lower()
    s = s.replace('&', ' and ')
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r"['’]", '', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    return s


def site_entities():
    """Toutes les entites du site needing une image reelle."""
    out = []
    for jf, key, folder in (('js/data-weapons.json', 'weapons', 'img/armes'),
                             ('js/data-items.json', 'items', 'img/items'),
                             ('js/data-armors.json', 'armors', 'img/armures')):
        d = json.loads((ROOT / jf).read_text(encoding='utf-8'))
        for e in d.get(key, []):
            out.append({'src': jf, 'id': e['id'], 'name': e['name'],
                        'folder': folder, 'image': e.get('image', '')})
    return out


if __name__ == '__main__':
    print('Index des pages wiki...')
    idx = build_index()
    print('  %d pages indexees' % len(idx))
    ents = site_entities()
    print('  %d entites sur le site' % len(ents))
    hit = miss = 0
    misses = []
    for e in ents:
        k = normalize(e['name'])
        if k in idx:
            hit += 1
        else:
            # essai par le nom de fichier de l'image actuelle
            base = pathlib.Path(e.get('image', '')).stem
            kb = normalize(base)
            if kb in idx:
                hit += 1
            else:
                miss += 1
                misses.append((e['name'], base))
    print('  correspondances : %d | non trouvees : %d' % (hit, miss))
    for n, b in misses:
        print('    - %s   (image actuelle : %s)' % (n, b))
    pathlib.Path('tools/_wiki_index.json').write_text(
        json.dumps({'index': idx}, ensure_ascii=False), encoding='utf-8')
    print('  index enregistre dans tools/_wiki_index.json')
