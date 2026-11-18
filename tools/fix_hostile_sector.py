#!/usr/bin/env python3
"""Corrige la presentation de Hostile Sector et Distorted Valley.

Officiel (annonce S7, 15 septembre 2026) :
« Hostile Sector and Distorted Valley will not be available this season.
Players can sell their Hostile Sector: Solo Infiltration tickets to the contact.
The red drop Chaotic Matter, previously exclusive to Distorted Valley, will be
available as a drop on all maps during S7. »

Les quatre classes d'elite (breacher, sniper, grenadier, fumigator) sont
deploiementes sur les cartes du mode principal, a un niveau de menace inferieur.
"""
import pathlib, re

# ── 1. map-northridge.html : la section PvE ────────────────────────────────
P = pathlib.Path('pages/map-northridge.html')
s = P.read_text(encoding='utf-8')

OLD_SECTION = '''          <h2 id="pve">4. Hostile Sector PvE — le farm Koen</h2>
          <p>Le mode <strong>Hostile Sector Northridge</strong> reste la meilleure source de Koen sans PvP :</p>
          <ul>
            <li>Loot supérieur au Lockdown, équipe ne peut pas s'entre-tuer.</li>
            <li>Farmez les containers denses (coffres, boîtes d'armes) — 100K+/h de moyenne possible.</li>
            <li>Le test idéal pour vos <a href="guide-economie.html" id="lnk-map-northridge-094">rat kits rentables</a>.</li>
          </ul>'''

NEW_SECTION = '''          <h2 id="pve">4. Le PvE en S7 : ce qui a changé</h2>
          <div class="callout callout-warning">
            <h3 class="h4">Hostile Sector n'est plus disponible</h3>
            <p>Depuis la Saison 7, <strong>Hostile Sector et Distorted Valley ne sont plus accessibles</strong>.
            L'annonce officielle de la saison est explicite : les tickets <em>Hostile Sector : Solo
            Infiltration</em> restants peuvent être <strong>vendus à un contact</strong>. Ne planifiez donc plus
            aucun run Farm ou Northridge « solo » sur cette file. <span class="src-tag src-officiel">Officiel</span></p>
          </div>
          <p>Ce que la redirection donne concrètement sur Northridge :</p>
          <ul>
            <li><strong>Les quatre classes d'élite sont revenues dans le mode principal</strong> —
            breacher, sniper, grenadier et fumigator. Elles sont déployées sur les cartes de
            Tactical Ops, mais avec un <strong>niveau de menace global plus faible</strong> quen's
            Hostile Sector : comptez des escouades d'élites plus légères, pas l'ancienne expérience
            PvE. <span class="src-tag src-officiel">Officiel</span></p>
            <li><strong>Le vrai PvE de la saison est Zombie Endless</strong> — un mode survival sur
            l'Airport, en escouade de 1 à 4, avec loadout imposé et downed permanent. C'est
            aujourd'hui le seul mode où aucun opérateur adverse ne peut vous tuer. <a href="map-no-mans-land.html" id="lnk-map-northridge-pve1">Voir le guide des modes PvE</a>.</li>
            <li><strong>Le red drop Chaotic Matter est devenu global</strong> : jusque-là réservé à
            Distorted Valley, il apparaît maintenant sur <strong>toutes les cartes</strong> en S7. Si vous
            le cherchiez uniquement sur Valley, la bonne nouvelle est que Northridge peut désormais
            en produire. <span class="src-tag src-officiel">Officiel</span></li>
          </ul>
          <div class="callout callout-success">
            <h3 class="h4">Le substitut pour farmer sans PvP</h3>
            <p>Si votre but est la Koen sans risquer votre stuff, la chaîne qui remplace Hostile Sector
            est : <strong>Zombie Endless</strong> (PvE pur, Airport) pour la routine, et
            <strong>Secure Ops</strong> si vous voulez arena mais garder votre équipement. Le PvE
            « <a href="guide-economie.html" id="lnk-map-northridge-pve2">found money</a> » classique n'existe
            plus en S7 : les seules files PvP sans escouade restent les files classiques de Tactical
            Ops, où vous pouvez croiser une équipe.</p>
          </div>'''

assert OLD_SECTION in s, 'section PvE Northridge introuvable'
s = s.replace(OLD_SECTION, NEW_SECTION)

# TOC
s = s.replace('<a href="#pve" id="lnk-map-northridge-100">4. Hostile Sector</a>',
              '<a href="#pve" id="lnk-map-northridge-100">4. Le PvE en S7</a>')

# Facts : modes disponibles
s = s.replace('<span class="fact-value">Normal · Lockdown · Forbidden · Hostile Sector PvE',
              '<span class="fact-value">Normal · Lockdown · Forbidden · Infected Zone')

# Titres / sous-titres
s = s.replace('Longue portée, Hostile Sector et le boss Fred — la carte des patients.',
              'Longue portée, classes d\'élite et boss Fred — la carte des patients.')
s = s.replace("10 extractions, Hostile Sector PvE pour farmer, boss Fred à l'hôtel",
              "10 extractions, classes d'élite S7, boss Fred à l'hôtel")

P.write_text(s, encoding='utf-8')
print('map-northridge.html : section PvE reecrite')

# ── 2. Autres pages : Hostile Sector mentionne comme actif ───────────────
REPL = [
 # equipement-armures.html
 ('pages/equipement-armures.html',
  '<td>Rat kits, Hostile Sector, runs rapides</td>',
  '<td>Rat kits, PvE, runs rapides</td>'),
 # equipement-casques.html
 ('pages/equipement-casques.html',
  '<td>Rat kits, Hostile Sector</td>',
  '<td>Rat kits, PvE</td>'),
 # equipement-sacs.html
 ('pages/equipement-sacs.html',
  '<td>Warehouse raids, Hostile Sector</td>',
  '<td>Warehouse raids, PvE</td>'),
 # equipement-tier-list.html
 ('pages/equipement-tier-list.html',
  '<tr><td>Hostile Sector (PvE)</td><td>T3-T4</td><td>T3-T4</td><td>~150 000 K</td></tr>',
  '<tr><td>Zombie Endless (PvE)</td><td>T3-T4</td><td>T3-T4</td><td>~150 000 K</td></tr>'),
 # events-calendrier.html
 ('pages/events-calendrier.html',
  '<li><strong>Hostile Sector</strong> — secteurs reinforced, rotations de haut niveau.</li>',
  '<li><strong>Classes d\'élite S7</strong> — breacher, sniper, grenadier, fumigator déployés sur les cartes du mode principal, à menace réduite.</li>'),
 # items-munitions.html
 ('pages/items-munitions.html',
  'Farm / Northridge Hostile Sector',
  'Farm / Northridge en file classique'),
]

for f, old, new in REPL:
    p = pathlib.Path(f)
    s = p.read_text(encoding='utf-8')
    if old in s:
        p.write_text(s.replace(old, new), encoding='utf-8')
        print('corrige :', f)
    else:
        print('NON TROUVE dans %s : %r' % (f, old[:60]))
