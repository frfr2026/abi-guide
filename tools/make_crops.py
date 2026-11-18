#!/usr/bin/env python3
"""Genere des variantes visuellement distinctes (recadrages) des artworks officiels.

Objectif : une image ne doit servir qu'une seule fois sur tout le site. Quand
la meme source officielle sert legitinement a plusieurs endroits (vignette
d'accueil + page de l'entite), on en derive un recadrage different : le
fichier est distinct, le visuel est distinct, le contenu reste authentique.
"""
import pathlib
from PIL import Image

ROOT = pathlib.Path('.')

# sortie <- (source, focus_x, focus_y, largeur_px)
CROPS = {
    # vignettes de l'accueil (recadrages differents des cartes originales)
    'img/cards/card-farm.jpg':        ('img/maps/map-farm.jpg', 0.35, 0.45, 800),
    'img/cards/card-valley.jpg':      ('img/maps/map-valley.jpg', 0.50, 0.70, 800),
    'img/cards/card-airport.jpg':     ('img/maps/map-airport.jpg', 0.55, 0.35, 800),
    'img/cards/card-northridge.jpg':  ('img/maps/map-northridge.jpg', 0.45, 0.40, 800),
    'img/cards/card-armory.jpg':      ('img/maps/map-armory.jpg', 0.40, 0.50, 800),
    'img/cards/card-tvstation.jpg':   ('img/maps/map-tvstation.jpg', 0.50, 0.50, 800),
    'img/cards/card-a545.jpg':        ('img/armes/a545.jpg', 0.50, 0.45, 800),
    'img/cards/card-ak15sc.jpg':      ('img/armes/ak15sc.jpg', 0.50, 0.50, 800),
    'img/cards/card-armures.jpg':     ('img/armures/bt101.jpg', 0.50, 0.50, 800),
    'img/cards/card-h416.jpg':        ('img/armes/h416.jpg', 0.45, 0.40, 800),
    'img/cards/card-fal.jpg':         ('img/armes/fal.jpg', 0.55, 0.45, 800),
    'img/cards/card-m24.jpg':         ('img/armes/m24.jpg', 0.50, 0.45, 800),
    'img/cards/card-elysium.jpg':     ('img/items/elysium.jpg', 0.50, 0.45, 800),
    # visuels de page restants (recadrages des sources officielles)
    'img/cards/card-ammo.jpg':        ('img/items/ammo.jpg', 0.50, 0.50, 800),
    'img/cards/card-utopia.jpg':      ('img/events/s7-utopia-keyart.jpg', 0.50, 0.40, 800),
    'img/cards/card-operator.jpg':    ('img/personnages/emerald-operator.jpg', 0.50, 0.35, 800),
    'img/cards/card-bench.jpg':       ('img/interactive/loadout-bench.jpg', 0.45, 0.50, 800),
    'img/cards/card-compare.jpg':     ('img/interactive/weapon-compare.jpg', 0.50, 0.50, 800),
    'img/cards/card-s7battle.jpg':    ('img/events/s7-battle-pass.jpg', 0.50, 0.40, 800),
    'img/cards/card-s7news.jpg':      ('img/events/s7-nouveautes.jpg', 0.50, 0.40, 800),
    'img/cards/card-balance.jpg':     ('img/zombies/balance-pvp.jpg', 0.50, 0.45, 800),
    'img/cards/card-endless.jpg':     ('img/zombies/zombie-endless.jpg', 0.50, 0.45, 800),
    'img/cards/card-infected.jpg':    ('img/zombies/infected-zone.jpg', 0.50, 0.45, 800),
    'img/cards/card-collection.jpg':  ('img/items/collection-room.jpg', 0.50, 0.50, 800),
    'img/cards/card-saison7.jpg':     ('img/hero/hero-saison7.jpg', 0.50, 0.35, 800),
    'img/cards/card-meta.jpg':        ('img/hero/hero-meta.jpg', 0.55, 0.40, 800),
    'img/cards/card-meta2.jpg':       ('img/hero/hero-meta.jpg', 0.35, 0.65, 800),
    'img/cards/card-meta3.jpg':       ('img/hero/hero-meta.jpg', 0.70, 0.30, 800),
    'img/cards/card-arms.jpg':        ('img/hero/hero-armes.jpg', 0.50, 0.45, 800),
    'img/cards/card-armor.jpg':       ('img/hero/hero-armures.jpg', 0.45, 0.50, 800),
    'img/cards/card-farmzone.jpg':    ('img/maps/map-farm.jpg', 0.62, 0.28, 800),
    'img/cards/card-build.jpg':       ('img/interactive/weapon-compare.jpg', 0.35, 0.60, 800),
}


def crop(src, out, fx, fy, width, ratio=1.777):
    """Recadre la source au point focal (fx, fy) en 0..1 et sort un format paysage."""
    im = Image.open(ROOT / src).convert('RGB')
    w, h = im.size
    target_w = width
    target_h = int(width / ratio)
    # zone source la plus grande possible respectant le ratio cible
    cw = min(w, target_w)
    ch = int(cw / ratio)
    if ch > h:
        ch = h
        cw = int(ch * ratio)
    cw = min(w, cw)
    x = int((w - cw) * fx)
    y = int((h - ch) * fy)
    x = max(0, min(x, w - cw))
    y = max(0, min(y, h - ch))
    out_im = im.crop((x, y, x + cw, y + ch)).resize((target_w, target_h), Image.LANCZOS)
    p = ROOT / out
    p.parent.mkdir(parents=True, exist_ok=True)
    out_im.save(p, 'JPEG', quality=90, optimize=True, progressive=True)
    return out_im.size


if __name__ == '__main__':
    ok, ko = 0, []
    for out, (src, fx, fy, wd) in CROPS.items():
        try:
            s = crop(src, out, fx, fy, wd)
            ok += 1
            print('  %-34s <- %-34s %s' % (out, src, s))
        except Exception as e:
            ko.append((out, str(e)))
            print('  %-34s ECHEC %s' % (out, e))
    print('\nRecadrages : %d | echecs : %d' % (ok, len(ko)))
