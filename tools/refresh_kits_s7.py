#!/usr/bin/env python3
"""Ajoute le tableau officiel des season kits S7 sur pages/armes-attachements-s7.html.

Source : notes de Saison 7 de MoreFun (Steam, 16 septembre 2026). L'editeur
nomme quatre kits experimentaux et décrit precisement leur effet. Ces kits
sont retires a la fin de la saison, ce qui change completement leur valeur en
marche : c'est le point que les guides oublient.

Le script est idempotent.
"""
import pathlib, re

P = pathlib.Path('pages/armes-attachements-s7.html')
s = P.read_text(encoding='utf-8')

if 'kits-officiels' in s:
    print('deja enrichi')
    raise SystemExit(0)

BLOCK = '''
          <h2 id="kits-officiels">2. Les quatre kits saisonniers — les noms et les effets officiels</h2>
          <p>Ce sont des <strong>season kits</strong> : des pièces expérimentales, concept propre à la Saison 7. L'éditeur les présente dans ses notes de mise à jour du 16 septembre 2026, avec quatre noms et quatre effets précis. Ce sont ces noms que le joueur voit dans le jeu — les guides communautaires qui les nomment autrement induisent en erreur.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Nom officiel</th><th>Arme</th><th>Effet officiel</th></tr></thead>
              <tbody>
                <tr><td><strong>PCC-9 fully-automatic kit</strong></td><td>PCC-9</td><td>Apporte un mode de tir <strong>fully-automatic</strong> au PCC-9.</td></tr>
                <tr><td><strong>M110 binary trigger</strong></td><td>M110</td><td>Tire <strong>deux projectiles par pression</strong> de détente, ce qui donne au M110 une puissance de dégâts immédiatement menaçante.</td></tr>
                <tr><td><strong>MPX Vulcan barrel</strong></td><td>MPX</td><td>Offre au MPX des <strong>options de munitions à chair</strong> (branche de munitions).</td></tr>
                <tr><td><strong>FAL burst kit</strong></td><td>FAL</td><td> fait passer le pouvoir de feu du FAL de <strong>« mid-low » à « high »</strong>, au prix d'un taux de feu légèrement inférieur.</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : notes de mise à jour de la Saison 7, MoreFun Studios (16 septembre 2026). Traduction française des libellés anglais.</p>

          <div class="callout callout-danger">
            <h3 class="h4">L'erreur d'achat la plus coûteuse de la saison</h3>
            <p>Les notes de l'éditeur sont explicites : <strong>« Ces kits seront retirés à la fin de la saison, et une nouvelle série de kits pour d'autres armes sera introduite la saison suivante. »</strong></p>
            <ul>
              <li>Un kit saisonnier acheté en décembre ne vaut <strong>rien en janvier</strong>. Son prix monte dans les dernières semaines — puis tombe à zéro d'un coup.</li>
              <li>Le stock <strong>non équipé</strong> est perdu. Seule la pièce <strong>déjà montée sur l'arme</strong> suit l'arme.</li>
              <li>La logique d'achat est donc inversée : on achète tôt pour l	use intensive pendant la saison, et on <strong>arrête d'en acheter</strong> dès que la fin de saison s'approche.</li>
            </ul>
          </div>

          <div class="callout callout-info">
            <h3 class="h4">Et pour le FAL Burst Kit, une nuance de vocabulaire</h3>
            <p>La fiche du FAL est le seul kit dont l'effet est une <strong>conversion de mode</strong> plutôt qu'un simple ajout. Le libellé officiel parle de « power » — passer de « mid-low » à « high » — ce qui recouvre à la fois le profil de dégâts et la docilité du tir. Et le prix à payer est explicite : <strong>un taux de feu légèrement inférieur</strong>. C'est précisément ce qui en fait un kit « low-RPM » : le FAL Burst Kit ne vous rend pas plus rapide, il rend le FAL plus violent par projectile.</p>
          </div>
'''

# inserer apres la section "1. Vue d'ensemble"
m = re.search(r'<h2 id="vue-ensemble">(\d+)\. Vue d\'ensemble[^<]*</h2>', s)
if not m:
    raise SystemExit('ancre vue-ensemble introuvable')
n = int(m.group(1))
s = s[:m.end()] + BLOCK.strip() + '\n\n          ' + s[m.end():]

# renumeroter les sections suivantes
ORDER = ['vue-ensemble','kits-officiels','pcc9','m110','fal','mpx','compatibilite-officielle','ordre-achat']
for i, sid in enumerate(ORDER, start=1):
    pat = re.compile(r'(<h2 id="' + re.escape(sid) + r'">)(\d+)(\. )')
    mm = pat.search(s)
    if mm:
        s = s[:mm.start()] + mm.group(1) + str(i) + mm.group(3) + s[mm.end():]

# sommaire
mt = re.search(r'<aside class="toc"[^>]*>.*?</aside>', s, re.S)
if mt:
    blk = mt.group(0)
    head = blk[:blk.find('<h4>Sommaire</h4>') + len('<h4>Sommaire</h4>')]
    existing = re.findall(r'<a href="#([^"]+)" id="([^"]+)">([^<]+)</a>', blk)
    LABELS = {'vue-ensemble':"1. Vue d'ensemble",'kits-officiels':"2. Les kits officiels",
              'pcc9':"3. PCC-9",'m110':"4. M110 Binary",'fal':"5. FAL Burst",
              'mpx':"6. MPX Vulcan",'compatibilite-officielle':"7. Compatibilité",
              'ordre-achat':"8. Ordre d'achat"}
    lines = []
    for sid in ORDER:
        old_id = next((i for h, i, t in existing if h == sid), 'lnk-armes-attachements-s7-%03d' % (100 + len(lines)))
        lines.append('<a href="#%s" id="%s">%s</a>' % (sid, old_id, LABELS[sid]))
    for h, i, t in existing:
        if h not in ORDER:
            lines.append('<a href="#%s" id="%s">%s</a>' % (h, i, t))
    s = s[:mt.start()] + head + '\n' + '\n'.join(lines) + '\n        </aside>' + s[mt.end():]

P.write_text(s, encoding='utf-8')
print('pages/armes-attachements-s7.html : tableau des kits officiels ajoute')
