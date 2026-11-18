#!/usr/bin/env python3
"""Telechargement des artworks officiels ABI (wiki MediaWiki) -> JPG haute qualite.

Le site ne doit contenir que du JPG : les PNG officiels sont composites sur
un fond sombre (coherent avec le theme du site) puis encodes en JPEG.
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.parse
from PIL import Image, ImageFilter

API = 'https://arena-breakout-infinite.fandom.com/api.php'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
ROOT = pathlib.Path('.')
CACHE = ROOT / 'tools' / '_imgcache'
CACHE.mkdir(exist_ok=True, parents=True)

BG_TOP = (34, 37, 44)
BG_BOT = (16, 17, 21)


def api(params, tries=3):
    q = urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            req = urllib.request.Request(API + '?' + q, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as e:
            if i == tries - 1:
                print('   ! API:', e, file=sys.stderr)
                return None
            time.sleep(2 + i * 2)


def file_url(filename):
    """URL de resolution du fichier wiki (renvoie aussi l'extension reelle)."""
    d = api({'action': 'query', 'titles': 'File:' + filename,
             'prop': 'imageinfo', 'iiprop': 'url|size|mime', 'format': 'json'})
    if not d:
        return None
    for _, pg in d.get('query', {}).get('pages', {}).items():
        ii = pg.get('imageinfo')
        if ii:
            return ii[0]['url']
    return None


def backdrop(w, h):
    """Fond degrade sombre avec vignettage."""
    from PIL import ImageDraw
    img = Image.new('RGB', (w, h), BG_BOT)
    dr = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        dr.line([(0, y), (w, y)], fill=c)
    # vignettage
    import numpy as np
    a = np.asarray(img).astype('float32')
    yy, xx = np.mgrid[0:h, 0:w]
    cx, cy = w / 2, h / 2
    d = np.sqrt(((xx - cx) / cx) ** 2 + ((yy - cy) / cy) ** 2)
    vig = np.clip(1.12 - 0.42 * np.clip(d - 0.35, 0, None), 0.55, 1.0)
    a *= vig[:, :, None]
    return Image.fromarray(np.clip(a, 0, 255).astype('uint8'))


def to_jpg(src_bytes, out_path, target=1024):
    """Composite l artwork (souvent PNG transparent) sur fond sombre -> JPG."""
    im = Image.open(io.BytesIO(src_bytes))
    im = im.convert('RGBA')
    # detacher la zone utile
    bbox = im.getbbox()
    alpha = im.getchannel('A')
    if bbox is None:
        bbox = alpha.getbbox()
    if bbox:
        im = im.crop(bbox)
        alpha = alpha.crop(bbox)
    w, h = im.size
    if w == 0 or h == 0:
        raise ValueError('image vide')
    # marge de 8 %
    margin = 0.08
    canvas = max(w, h) * (1 + 2 * margin)
    bg = backdrop(int(canvas), int(canvas))
    scale = (canvas * (1 - 2 * margin)) / max(w, h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    alpha = alpha.resize((nw, nh), Image.LANCZOS)
    px = int((canvas - nw) / 2)
    py = int((canvas - nh) / 2)
    bg.paste(im, (px, py), alpha)
    if bg.width != target:
        bg = bg.resize((target, target), Image.LANCZOS)
    bg.save(out_path, 'JPEG', quality=92, optimize=True, progressive=True)
    return bg.size


def fetch(filename, out_path, target=1024, use_cache=True):
    out_path = pathlib.Path(out_path)
    if use_cache and out_path.exists() and out_path.stat().st_size > 5000:
        return 'cache'
    url = file_url(filename)
    if not url:
        return None
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Referer': 'https://arena-breakout-infinite.fandom.com/'})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            break
        except Exception as e:
            if i == 2:
                return None
            time.sleep(2 + i * 2)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        size = to_jpg(data, out_path, target)
    except Exception as e:
        print('   ! conversion:', filename, e, file=sys.stderr)
        return None
    return size


if __name__ == '__main__':
    print('module de telechargement — utiliser tools/fetch_assets.py')
