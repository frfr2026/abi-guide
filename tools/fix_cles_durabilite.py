#!/usr/bin/env python3
"""Ajoute deux corrections de fond aux pages cles et attachements S7.

1. pages/items-cles.html — la duree de cles : le site indiquait le cout par
   mode (Normal 1, Lockdown 2, Forbidden 3) sans dire ce qui arrive aux
   cles anciennes. Or ces regles ne s'appliquent qu'aux cles neuves : une
   cle heritee d'avant la regle consomme 1 point d'usage quel que soit le
   mode. C'est une source directe de perte de Koen, et c'est invisible si
   on ne le dit pas.

2. pages/armes-attachements-s7.html — le MPX Vulcan Barrel : le site
   decrit correctement l'effet (degats chair augmentes, degats armure
   reduits) mais ne dit pas avec quelles munitions l'utiliser. Les
   recommandations de la communaute sont sans appel : du Dum-Dum, pas du
   7N39. Le 7N39 est une munition a tres forte penetration ; sur une piece
   qui reduit volontairement la penetration, il est gaspille.

Idempotent.
"""
import pathlib

# ── 1. duree des cles ─────────────────────────────────────────────────────
CLES = '''            <div class="callout callout-warning">
              <h3 class="h4">Les clés anciennes ne suivent pas la règle des nouvelles</h3>
              <p>Le tableau ci-dessus — <strong>1 point en Normal, 2 en Lockdown, 3 en Forbidden</strong> —
              s'applique aux <strong>clés neuves</strong>, qui arrivent avec une réserve d'usages. Une clé
              <strong>heritée d'avant cette règle</strong> fonctionne autrement : elle consomme
              <strong>un seul point d'usage, quel que soit le mode</strong>.</p>
              <p>Concrètement, ouvrir une vieille clé en Lockdown ou en Forbidden est une perte sèche : la clé
              ne vaut plus qu'une ouverture, là où une clé neuve en vaudrait deux ou trois. La bonne pratique
              est donc simple : <strong>les anciennes clés se dépensent en Normal</strong>, où une ouverture
              coûte le même, et les nouvelles se gardent pour le Forbidden.</p>
              <p class="small text-muted">Source : retours de joueurs documentés sur r/ArenaBreakoutInfinite.
              Donnée communautaire, non publiée par l'éditeur. Le tableau des coûts par mode, lui, est appliqué
              par le jeu.</p>
            </div>
'''

# ── 2. MPX Vulcan Barrel : la munition qui compte ───────────────────────
MPX = '''            <div class="callout callout-danger">
              <h3 class="h4">L'erreur de munition sur le Vulcan Barrel</h3>
              <p>Le MPX Vulcan Barrel <strong>augmente les dégâts infligés aux cibles non protégées et
              réduit les dégâts infligés aux cibles armées</strong>. C'est une pièce de <strong>chair</strong>,
              pas de pénétration.</p>
              <p>La conséquence est directe et coûteuse : <strong>ne gaspillez pas de 7N39 sur ce MPX</strong>.
              Le 7N39 est une munition à très forte pénétration ; sur une pièce qui réduit volontairement la
              pénétration, il perd l'essentiel de son intérêt. Les munitions à utiliser sont les
              <strong>Dum-Dum</strong> : elles infligent des dégâts de chair très élevés de près, et la
              pénalité de l'armure ne les concernait pas au départ.</p>
              <p>Les ordres de grandeur rapportés par les joueurs : environ <strong>90+ de dégâts de chair au
              contact</strong>, et encore <strong>60+ vers 80–100 mètres</strong>. Le canon du MPX garde une
              portée correcte, mais sa vraie zone utile reste courte.</p>
              <p class="small text-muted">Source : retours de joueurs et de créateurs de contenu sur
              YouTube et Reddit. Donnée communautaire, non publiée par l'éditeur.</p>
            </div>
'''

JOBS = [
    # (chemin, ancre, bloc, apres_table)
    # Le callout "cles anciennes" doit vivre DANS la section h2 qui porte le
    # tableau des couts : le inserer avant ce h2 creerait un saut de niveau
    # h1 -> h3, et son renvoi "le tableau ci-dessus" ne serait pas vrai.
    ('pages/items-cles.html', 'fonctionnement', CLES, True),
    ('pages/armes-attachements-s7.html', 'mpx', MPX, False),
]

for path, anchor, block, apres_table in JOBS:
    p = pathlib.Path(path)
    s = p.read_text(encoding='utf-8')
    if 'Les cl\u00e9s anciennes ne suivent pas' in s or 'erreur de munition sur le Vulcan' in s:
        print('  deja enrichi :', path)
        continue
    i = s.find('id="%s"' % anchor)
    assert i > 0, path
    if apres_table:
        # inserer juste apres la fermeture du <div class="table-wrap"> qui suit
        k = s.find('</table>', i)
        assert k > 0, path
        k = s.find('</div>', k)
        assert k > 0, path
        j = k + len('</div>')
    else:
        j = s.rfind('<h2 ', 0, i)
        if j < 0:
            j = s.rfind('<h3 ', 0, i)
        assert j > 0, path
    s = s[:j] + '\n' + block.strip() + s[j:]
    p.write_text(s, encoding='utf-8')
    print('  %-38s enrichi' % path)
