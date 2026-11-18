#!/usr/bin/env python3
"""Aligne les noms des season kits S7 sur les noms officiels de l'editeur.

Les notes de Saison 7 de MoreFun (16 septembre 2026) nomment exactement quatre
kits experimentaux :

  - le M110 binary trigger  (deux projectiles par pression de gachette)
  - le MPX Vulcan barrel    (branche de munitions a chair)
  - le FAL burst kit        (pouvoir de feu de "mid-low" a "high", au prix d'un
                             taux de feu legerement inferieur)
  - le PCC-9 fully-automatic kit (mode automatique plein)

Le site decrivait correctement les mecaniques mais utilisait des noms de
demonstration ("M110 Dual-Stage Trigger", "FAL Recoil Kit"). Le joueur, lui,
voit les noms officiels dans le jeu : il faut les employer.

Le script est idempotent : les noms deja corrects ne sont pas modifies.
"""
import pathlib, re

RENAMES = [
    # du plus long au plus court, pour eviter les remplacements partiels
    ('M110 Dual-Stage Trigger', 'M110 Binary Trigger'),
    ('M110 Dual-Stage',        'M110 Binary'),
    ('Dual-Stage Trigger',     'Binary Trigger'),
    ('Dual-Stage',             'Binary'),
    ('FAL Recoil Kit',         'FAL Burst Kit'),
    ('FAL + Recoil Kit',       'FAL + Burst Kit'),
    ('Recoil Kit',             'Burst Kit'),
    ('PCC-9 Full-Auto Kit',    'PCC-9 Fully-Automatic Kit'),
    ('PCC9 + Full-Auto Kit',   'PCC9 + Fully-Automatic Kit'),
    ('PCC-9 Full-Auto',        'PCC-9 Fully-Automatic'),
    ('MPX \u00ab Vulcan \u00bb Barrel', 'MPX Vulcan Barrel'),
]

TARGETS = sorted(list(pathlib.Path('pages').glob('*.html')) + list(pathlib.Path('js').glob('*.json')))

total = 0
for f in TARGETS:
    s = f.read_text(encoding='utf-8')
    before = s
    counts = {}
    for old, new in RENAMES:
        n = s.count(old)
        if n:
            s = s.replace(old, new)
            counts[old] = n
            total += n
    if s != before:
        f.write_text(s, encoding='utf-8')
        detail = ', '.join('%s x%d' % (k, v) for k, v in counts.items())
        print('  %-34s %s' % (f.name, detail))

print('total remplacements :', total)

# verification : plus aucun ancien nom
print()
print('=== controle final ===')
rest = 0
for f in TARGETS:
    s = f.read_text(encoding='utf-8')
    for old, _ in RENAMES:
        if old in s:
            print('  RESTE:', f.name, '->', old)
            rest += 1
print('noms restants :', rest)
