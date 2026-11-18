#!/usr/bin/env python3
"""Variantes dediees pour les derniers doublons multi-pages.

Recadrages distincts (fichiers distincts, visuels distincts) derives des
artworks officiels, pour l'explorateur de cartes, le tier list global et
la page saison 7.
"""
import pathlib
from PIL import Image

ROOT = pathlib.Path('.')

V = {
    # explorateur de cartes de meta-strategies-s7 (6 variantes)
    'img/maps/var-farm.jpg':       ('img/maps/map-farm.jpg', 0.30, 0.60),
    'img/maps/var-valley.jpg':     ('img/maps/map-valley.jpg', 0.70, 0.75),
    'img/maps/var-airport.jpg':    ('img/maps/map-airport.jpg', 0.50, 0.50),
    'img/maps/var-northridge.jpg': ('img/maps/map-northridge.jpg', 0.70, 0.30),
    'img/maps/var-armory.jpg':     ('img/maps/map-armory.jpg', 0.50, 0.70),
    'img/maps/var-tvstation.jpg':  ('img/maps/map-tvstation.jpg', 0.35, 0.35),
    # saison 7 : visuel des nouveautes (different de la page dediee)
    'img/events/var-s7news.jpg':   ('img/events/s7-nouveautes.jpg', 0.30, 0.65),
    # guide de progression (different de la vignette d'accueil)
    'img/cards/var-progression.jpg': ('img/hero/hero-meta.jpg', 0.25, 0.35),
    # no man's land (different de la vignette d'accueil)
    # 'img/cards/var-nml.jpg' : variante photorealiste generee, a ne pas ecraser
    # variantes armees pour le tier list global (recadrage serré distinct)
    'img/armes/var-sks.jpg':       ('img/armes/sks.jpg', 0.35, 0.40),
    'img/armes/var-mk14.jpg':      ('img/armes/mk14.jpg', 0.60, 0.40),
    'img/armes/var-m110.jpg':      ('img/armes/m110.jpg', 0.45, 0.60),
    'img/armes/var-sj16.jpg':      ('img/armes/sj16.jpg', 0.55, 0.55),
    'img/armes/var-t88.jpg':       ('img/armes/t88.jpg', 0.40, 0.45),
    'img/armes/var-h416.jpg':      ('img/armes/h416.jpg', 0.60, 0.60),
    'img/armes/var-u191.jpg':      ('img/armes/u191.jpg', 0.40, 0.35),
    'img/armes/var-a545.jpg':      ('img/armes/a545.jpg', 0.60, 0.55),
    'img/armes/var-ak12.jpg':      ('img/armes/ak12.jpg', 0.45, 0.50),
    'img/armes/var-aek971.jpg':    ('img/armes/aek971.jpg', 0.55, 0.40),
    'img/armes/var-fal.jpg':       ('img/armes/fal.jpg', 0.40, 0.55),
    'img/armes/var-ak15sc.jpg':    ('img/armes/ak15sc.jpg', 0.50, 0.60),
    'img/armes/var-an94.jpg':      ('img/armes/an94.jpg', 0.60, 0.50),
    'img/armes/var-m4a1.jpg':      ('img/armes/m4a1.jpg', 0.45, 0.45),
    'img/armes/var-rpk16.jpg':     ('img/armes/rpk16.jpg', 0.55, 0.55),
    'img/armes/var-usas12.jpg':    ('img/armes/usas12.jpg', 0.40, 0.50),
    'img/armes/var-p90.jpg':       ('img/armes/p90.jpg', 0.60, 0.40),
    'img/armes/var-vector.jpg':    ('img/armes/vector.jpg', 0.45, 0.60),
    'img/armes/var-pcc9.jpg':      ('img/armes/pcc9.jpg', 0.55, 0.45),
    'img/armes/var-mpx.jpg':       ('img/armes/mpx.jpg', 0.40, 0.60),
    'img/armes/var-vss.jpg':       ('img/armes/vss.jpg', 0.60, 0.50),
    'img/armes/var-banshee.jpg':   ('img/armes/banshee.jpg', 0.50, 0.55),
    'img/armes/var-m24.jpg':       ('img/armes/m24.jpg', 0.60, 0.45),
    'img/armes/var-mosin.jpg':     ('img/armes/mosin.jpg', 0.40, 0.55),
}


def make(src, out, fx, fy, width=720, ratio=1.5):
    im = Image.open(ROOT / src).convert('RGB')
    w, h = im.size
    cw = min(w, width)
    ch = int(cw / ratio)
    if ch > h:
        ch = h
        cw = int(ch * ratio)
    x = max(0, min(int((w - cw) * fx), w - cw))
    y = max(0, min(int((h - ch) * fy), h - ch))
    im2 = im.crop((x, y, x + cw, y + ch)).resize((width, int(width / ratio)), Image.LANCZOS)
    p = ROOT / out
    p.parent.mkdir(parents=True, exist_ok=True)
    im2.save(p, 'JPEG', quality=90, optimize=True, progressive=True)
    return im2.size


if __name__ == '__main__':
    ok, ko = 0, 0
    for out, (src, fx, fy) in V.items():
        try:
            make(src, out, fx, fy)
            ok += 1
        except Exception as e:
            ko += 1
            print('  ! %-34s %s' % (out, e))
    print('Variantes : %d ok | %d echecs' % (ok, ko))
