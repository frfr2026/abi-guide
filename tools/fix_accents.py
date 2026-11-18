#!/usr/bin/env python3
"""Corrige les accents manquants dans les legendes et captions injectees.

Les scripts d'injection avaient ecrit des legendes sans accents ("Cartes de
reference", "modele recent"...). Ce script les corrige et reste idempotent.
"""
import pathlib, re

FIXES = [
    ('Cartes de reference', 'Cartes de référence'),
    ('Visuel de reference', 'Visuel de référence'),
    ("Portrait d'operateur : le visuel de reference de l'univers de Kamona.",
     "Portrait d'opérateur : le visuel de référence de l'univers de Kamona."),
    ('fusil de bataille de reference', 'fusil de bataille de référence'),
    ('modele recent de la famille', 'modèle récent de la famille'),
    ('Version.amelioree du 6B4, premiere evolution',
     'Version améliorée du 6B4, première évolution'),
    ("casque audio de l'equipe", "casque audio de l'équipe"),
    ('reference haute de gamme', 'référence haute de gamme'),
    ('Les modeles « Armored Rig » embarq', 'Les modèles « Armored Rig » embarq'),
    ("d'apres les annonces officielles", "d'après les annonces officielles"),
    ('il ajoute de la capacite', 'il ajoute de la capacité'),
]

FILES = sorted(pathlib.Path('pages').glob('*.html')) + [pathlib.Path('index.html')]

changed = 0
for f in FILES:
    s = f.read_text(encoding='utf-8')
    before = s
    for old, new in FIXES:
        s = s.replace(old, new)
    if s != before:
        f.write_text(s, encoding='utf-8')
        changed += 1
        print('corrige :', f.name)
print('%d fichiers corriges' % changed)
