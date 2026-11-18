#!/usr/bin/env python3
"""Corrige les espaces manquants et les collages de mots dans pages/.

Un scan heuristique (minuscule suivi d'un majuscule, ou mot colle a une
abreviation) a denonce plusieurs dozenes de collages restants dans le site.
Chacun est corrige a la source, dans le HTML.

Idempotent : une correction deja appliquee n'est pas retrouvee.
"""
import pathlib

FIXES = {
    'armes-carbine': [
        ('la maniabilite d\'une arme de poing, laMunition d\'un fusil',
         "la maniabilite d'une arme de poing, la puissance d'un fusil"),
        ('la maniabilité d\'une arme de poing, laMunition d\'un fusil',
         "la maniabilité d'une arme de poing, la puissance d'un fusil"),
        ('et lesLep EUR dépen TTK',
         'et le choix change complètement le TTK'),
        ('vous perdez la seule avantage de la classe',
         'vous perdez le seul avantage de la classe'),
    ],
    'armes-sniper': [
        ("règle laVertical", "règle le vertical"),
        ('La penetrates maximale : le tirSupported en pleine tête traverse.',
         'La pénétration maximale : le tir soutenu en pleine tête traverse.'),
    ],
    'communaute-streamers': [
        ('Esprit d’équipe etAnalyse', 'Esprit d’équipe et analyse'),
        ('Twitch Drops etChallenges communautaires', 'Twitch Drops et challenges communautaires'),
    ],
    'cosmetiques-skins-perso': [
        ('Les passe-coins deKoen', 'Les passe-coins de Koen'),
    ],
    'items-munitions': [
        ('laMunition T4 de référence', 'la munition T4 de référence'),
    ],
    'equipement-headsets': [
        ('ce que vousPerdez exactement', 'ce que vous perdez exactement'),
    ],
    'saison7-zombie-infected-zone': [
        ('Saute et sprinte vers les_OPERATORs', 'Saute et sprinte vers les opérateurs'),
        ('terrain àugaliser', 'terrain à égaliser'),
    ],
    'saison7-utopia': [
        ('Check-inAutomne', 'Check-in Automne'),
    ],
}

total = 0
for page, pairs in FIXES.items():
    p = pathlib.Path('pages/%s.html' % page)
    if not p.exists():
        print('  page absente :', page)
        continue
    s = p.read_text(encoding='utf-8')
    n = 0
    for old, new in pairs:
        if old in s:
            c = s.count(old)
            s = s.replace(old, new)
            n += c
            total += c
    if n:
        p.write_text(s, encoding='utf-8')
        print('  %-26s %d correction(s)' % (page, n))

print('total :', total)
