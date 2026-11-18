#!/usr/bin/env python3
"""Telechargement des cartes officielles ABI -> JPG 16:9, ratio preserve.

Les cartes du wiki sont des images larges (1920x1080 / 3840x2160 / 4096x2048).
Elles sont encodes en JPG a 1920x1080 maximum sans deformation, avec un fond
sombre pour les marges eventuelles.
"""
import io, pathlib, sys, urllib.request
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fetch_official import file_url, backdrop, UA

TARGET_W = 1920
TARGET_H = 1080


def to_jpg_wide(src_bytes, out_path):
    im = Image.open(io.BytesIO(src_bytes)).convert('RGB')
    w, h = im.size
    scale = min(TARGET_W / w, TARGET_H / h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    bg = backdrop(TARGET_W, TARGET_H)
    bg.paste(im, ((TARGET_W - nw) // 2, (TARGET_H - nh) // 2))
    bg.save(out_path, 'JPEG', quality=90, optimize=True, progressive=True)
    return bg.size


def fetch_map(filename, out_path):
    out_path = pathlib.Path(out_path)
    url = file_url(filename)
    if not url:
        return None
    req = urllib.request.Request(url, headers={'User-Agent': UA,
                                              'Referer': 'https://arena-breakout-infinite.fandom.com/'})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    return to_jpg_wide(data, out_path)


CARDS = {
    'img/maps/map-tvstation.jpg': 'TVimage.jpg',
    'img/maps/map-valley.jpg': 'ValleyMapBase.png',
    'img/maps/map-northridge.jpg': 'Northridge.png',
    'img/maps/map-armory.jpg': 'Armory.Map.png',
    'img/maps/map-farm.jpg': 'FarmMapBase.png',
}

if __name__ == '__main__':
    for out, wiki in CARDS.items():
        try:
            s = fetch_map(wiki, out)
            p = pathlib.Path(out)
            print('  %-30s <- %-22s %s  %d Ko' % (out, wiki, s, p.stat().st_size // 1024))
        except Exception as e:
            print('  %-30s <- %-22s ECHEC %s' % (out, wiki, e))
