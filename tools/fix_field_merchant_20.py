#!/usr/bin/env python3
"""Harmonise la mention du « +20 % » du Field Merchant dans tout le site.

L'editeur n'a jamais publie de pourcentage de prime sur les objets dore :
ni l'annonce S7, ni les notes de patch. La regle officielle verifiee est
« 1 marchand par raid, ouvert a T+5 min » + « volume de transactions qui
debloque l'intel ». Le « +20 % » est une donnee communautaire non confirmee.
"""
import pathlib

REPL = [
 # guide-debutant.html
 ('pages/guide-debutant.html',
  '<li><strong>Vendre à bas prix au Field Merchant</strong> : en S7 ils paient <strong>+20 %</strong> pour les objets haute valeur — optimisez vos v',
  '<li><strong>Vendre au Field Merchant</strong> : en S7, un marchand par raid ouvre à T+5 min ; vendre libère des cases et construit la faveur qui débloque l\'intel — optimisez vos v'),
 # guide-economie.html
 ('pages/guide-economie.html',
  '<tr><td>Field Merchants en raid (S7)</td><td>Faible</td><td><strong>+20 %</strong> sur les ventes d\'objets haute valeur</td></tr>',
  '<tr><td>Field Merchants en raid (S7)</td><td>Faible</td><td>Libère de la place et construit la faveur qui débloque l\'intel</td></tr>'),
 ('pages/guide-economie.html',
  '<li>Ils paient les objets <strong>dorés/jaunes</strong> avec un <strong>bonus forfaitaire de 20 %</strong> : encaissez cash, file directement au co',
  '<li>Un marchand par raid, <strong>interactif à T+5 min</strong> : vendre votre surplus libère des cases et fait monter le <strong>volume de transactions</strong>, condition de l\'intel — file directement au co'),
 # map-farm.html
 ('pages/map-farm.html',
  '<li><strong>Merchant in-raid</strong> : un marchand par raid, ouvert à T+5 min — ventes +20 % haute valeur, intel de caches.</li>',
  '<li><strong>Field Merchant</strong> : un marchand par raid, ouvert à T+5 min — vendre libère des cases, le volume de transactions débloque l\'intel de caches. <span class="src-tag src-officiel">Officiel</span></li>'),
 # map-valley.html
 ('pages/map-valley.html',
  '<li>Marchand in-raid à T+5 min : ventes haute valeur +20 %, intel de caches.</li>',
  '<li>Field Merchant à T+5 min : vendre libère des cases, le volume de transactions débloque l\'intel de caches. <span class="src-tag src-officiel">Officiel</span></li>'),
]

for f, old, new in REPL:
    p = pathlib.Path(f)
    s = p.read_text(encoding='utf-8')
    if old in s:
        p.write_text(s.replace(old, new), encoding='utf-8')
        print('corrige :', f)
    else:
        print('NON TROUVE :', f, '|', old[:70])

# meta guide-economie
p = pathlib.Path('pages/guide-economie.html')
s = p.read_text(encoding='utf-8')
s = s.replace('Rat kit, barter flips, Field Merchants +20 %, ventes Market hebdomadaires, règle des 20 % : le plan complet pour enrichir votre stash sur Arena Breakout Infinite.',
              'Rat kit, barter flips, Field Merchants, ventes Market hebdomadaires : le plan complet pour enrichir votre stash sur Arena Breakout Infinite.')
p.write_text(s, encoding='utf-8')
print('meta guide-economie harmonisee')
