#!/usr/bin/env python3
"""Requalifie les badges de source de pages/items-cles.html.

Probleme : les tables de cles marquaient "Officiel" des donnees qui viennent
du wiki Fandom de reference. Or "officiel" designe chez ABI une publication de
l'editeur (MoreFun Studios). Un joueur qui lit "Officiel" sur une duree de cle
pense que l'editeur l'a publiee : c'est faux, et cela change sa confiance dans
la donnee.

On introduit un troisieme niveau, "Documente" : donnee reprise d'une source de
reference du wiki, verifiee et coherente, mais non publiee par l'editeur.
Les 39 badges concernes sont dans la section "Les cles par carte" : ils sont
donc tous concernes.

Idempotent.
"""
import pathlib, re

P = pathlib.Path('pages/items-cles.html')
s = P.read_text(encoding='utf-8')

if 'src-documente' in s:
    print('deja requalifie')
    raise SystemExit(0)

n1 = s.count('<span class="src-tag src-officiel">Officiel</span>')
s = s.replace('<span class="src-tag src-officiel">Officiel</span>',
              '<span class="src-tag src-documente">Document\u00e9</span>')

n2 = s.count('key-officiel-loot">Loot officiel :')
s = s.replace('key-officiel-loot">Loot officiel :', 'key-officiel-loot">Loot document\u00e9 :')

# legende explicative, inseree juste avant la premiere table de cles
LEG = '''          <div class="lore-legend">
            <span class="src-tag src-documente">Document\u00e9</span>
            <span>donn\u00e9e reprise de la source de r\u00e9f\u00e9rence du wiki ABI \u2014 coh\u00e9rente et recoup\u00e9e, mais <strong>non publi\u00e9e par l\u2019\u00e9diteur</strong>.</span>
            <span class="src-tag src-communautaire">Communautaire</span>
            <span>donn\u00e9e issue de retours de joueurs, variable selon les sources.</span>
          </div>
'''
i = s.find('id="par-carte"')
assert i > 0
j = s.find('</h2>', i)
assert j > 0
s = s[:j + 5] + '\n\n' + LEG + s[j + 5:]

P.write_text(s, encoding='utf-8')
print('pages/items-cles.html : %d badges requalifies en Documente, %d details de loot renommes'
      % (n1, n2))
