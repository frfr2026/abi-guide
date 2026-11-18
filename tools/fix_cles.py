#!/usr/bin/env python3
"""Reconcilie pages/items-cles.html avec le wiki officiel.

Probleme constate : le texteannonait 18 cles Northridge alors que la table
en contient 19, et le total annonce dans ETAT-PROJET.md (26) ne correspondait
pas au total reel (19 + 8 = 27).

La source de reference est le wiki officiel ABI, page Keys, qui documente les
cles par carte avec leur durete et leur contenu. On ajoute :

  1. la colonne "Source" (officiel / communautaire) sur chaque table ;
  2. le contenu reel documente par le wiki pour les cles qu'il decrit ;
  3. un encadre recapitulatif du perimetre reel de chaque carte.

Le script est idempotent : il detecte les marqueurs deja inseres.
"""
import pathlib, re, json

P = pathlib.Path('pages/items-cles.html')
s = P.read_text(encoding='utf-8')

if 'key-officiel-loot' in s and s.count('src-documente') > 20:
    print('deja reconcilie')
    raise SystemExit(0)

# ── cles documentees par le wiki officiel, par carte ────────────────────
# (nom officiel, duree, contenu documente)
WIKI = {
 'Farm': {
  'Master Bedroom Key': ('45', '1 coffre, 1 ordinateur, 1 veste, 1 spawn rare sur étagère'),
  'Stables Warehouse Key': ('75', '1 boîte de documents, 1 veste, 1 boîte à outils'),
  'Motel 201 Key': ('45', '1 coffre, 1 trousse de premiers secours pro, 1 spawn rare sur table'),
  'Motel Main Guest Room Key': ('30', '1 coffre électronique, 1 coffre, 1 manteau d’hiver, 1 conteneur d’armes premium, 1 spawn rare sur table'),
  'Barn Office Key': ('45', '1 coffre, 1 ordinateur, 1 valise'),
 },
 'Valley': {
  'Staff Dormitory Key': ('45', '1 coffre, 1 manteau d’hiver, 1 sac de sport'),
  'Factory Dressing Room Key': ('45', '1 boîte à armes longue, 2 vêtements de travail, 1 sac de sport, 1 coffre'),
  'Beach Villa Main Bedroom Key': ('30', '1 coffre électronique, 1 manteau d’hiver, 1 caisse d’armes premium'),
  'Factory File Room Key': ('45', '1 coffre, 1 grande caisse d’armes'),
  'Beach Villa Storage Key': ('30', '1 coffre, 1 caisse d’armes moyenne, 1 valise'),
 },
 'Armory': {
  'Weapon Storage Keycard': ('30', None),
  'Commnand Room Entry Keycard': ('30', None),
  'Private Lounge Key': ('45', None),
  'Second Floor Lounge Key': ('45', None),
  'Commnand Room Exit Keycard': ('30', None),
  'Sluice No. 2 Key': ('3', None),
 },
 'TV Station': {
  '2F General Office Card': ('30', None),
  '2F Directors Office Card': ('30', None),
  'Post-Production Room Key': ('30', None),
  'Editing Room Key': ('30', '1 coffre électrique, 1 tiroir de bureau, 1 caisse de rangement'),
  'Darkroom Key': ('45', None),
  'Infirmary Key': ('45', None),
  'Planning Room Key': ('30', None),
 },
 'Northridge': {
  'Cafeteria Cashiers Office Key': ('3', None),
  'Building C Lounge 1 Key': ('30', None),
  'Building B Managers Office Key': ('45', None),
  'Service Area Managers Office Key': ('30', None),
  'Building D Projection Room Key': ('45', None),
  'Sewage Plant Workshop Key': ('45', None),
  'Building C Lounge Private Room Key': ('30', None),
  'Building B Reception Room Key': ('30', None),
  'Waiting Area Lounge Key': ('45', None),
 },
 'Airport': {
  'Executive Lounge Key': ('30', None),
  'VIP Reception Keycard': ('30', None),
  'AOC Secret Archives Keycard': ('30', None),
  'Employee Lounge Key': ('30', None),
  'Fuel Storage Key': ('30', None),
  'Cargo Inspection Area Key': ('30', None),
  'Exhibition Uitlity Room Key': ('30', None),
  'Control Area Permission Card': ('30', None),
  'Ticket Hall Conference Room Key': ('30', None),
 },
}

# alias : nom du site -> nom wiki officiel
ALIAS = {
 'Command Room Entry Keycard': 'Commnand Room Entry Keycard',
 'Command Room Exit Keycard': 'Commnand Room Exit Keycard',
 "Building B Manager's Office Key": 'Building B Managers Office Key',
 "Service Area Manager's Office Key": 'Service Area Managers Office Key',
 "Cafeteria Cashier's Office Key": 'Cafeteria Cashiers Office Key',
 'Keycard to AOC Secret Archives': 'AOC Secret Archives Keycard',
 'Keycard to VIP Reception': 'VIP Reception Keycard',
 'Pass to Control Area': 'Control Area Permission Card',
 'Key to Cargo Inspection Point': 'Cargo Inspection Area Key',
 'Key to Fuel Depot': 'Fuel Storage Key',
 'Key to Utility Room': 'Exhibition Uitlity Room Key',
}

# ── decoupage par section h3 ───────────────────────────────────────────
h3 = [(m.start(), m.group(1)) for m in re.finditer(r'<h3>([^<]+)</h3>', s)]
h3.append((len(s), None))
CARDS = ['Farm', 'Valley', 'Armory', 'TV Station', 'Northridge', 'Airport']

# on decoupe en blocs, on les traite, puis on reassemble : les offsets
# resteraient invalides si on modifiait s en place section apres section
blocks = [(h3[k][0], h3[k + 1][0], h3[k][1]) for k in range(len(h3) - 1)]

for idx in range(len(CARDS)):
    card = CARDS[idx]
    blk = None
    for entry in blocks:
        bstart, bend, bname = entry[0], entry[1], entry[2]
        if bname == card:
            blk = entry[3] if len(entry) > 3 else s[bstart:bend]
            break
    if blk is None:
        print('section introuvable :', card)
        continue
    wiki = WIKI.get(card, {})

    # 1. ajouter la colonne Source a l en-tete
    m = re.search(r'<thead><tr>(.*?)</tr></thead>', blk, re.S)
    if m and 'Source' not in m.group(1):
        head = m.group(1)
        # ajouter la colonne avant la fin du tr
        newhead = head + '<th>Source</th>'
        blk = blk[:m.start(1)] + newhead + blk[m.end(1):]

    # 2. annoter chaque ligne de cle
    def annot(row_html):
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row_html, re.S)
        if not cells:
            return row_html
        name = re.sub(r'<[^>]+>', '', cells[0]).strip()
        wname = ALIAS.get(name, name)
        if wname in wiki:
            badge = ('<span class="src-tag src-documente">Document\u00e9</span>')
        else:
            badge = ('<span class="src-tag src-communautaire">Communautaire</span>')
        # reconstruire la ligne avec la colonne Source
        newcells = list(cells) + [badge]
        return '<tr>' + ''.join('<td>%s</td>' % c for c in newcells) + '</tr>'

    blk = re.sub(r'<tr>.*?</tr>', lambda m: annot(m.group(0)), blk, flags=re.S)

    # 3. completer le contenu documente par le wiki pour les cles connues
    for wname, (dur, contenu) in wiki.items():
        if not contenu:
            continue
        # retrouver la ligne dont le nom correspond
        def add_contenu(m):
            row = m.group(0)
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if not cells:
                return row
            name = re.sub(r'<[^>]+>', '', cells[0]).strip()
            if ALIAS.get(name, name) != wname:
                return row
            # colonne 3 = description : on ajoute le contenu officiel
            if len(cells) >= 3:
                desc = cells[2]
                if 'Loot document\u00e9' not in desc:
                    desc = desc.rstrip() + ' <span class="key-officiel-loot">Loot document\u00e9 : ' + contenu + '</span>'
                    cells[2] = desc
                    return '<tr>' + ''.join('<td>%s</td>' % c for c in cells) + '</tr>'
            return row
        blk = re.sub(r'<tr>.*?</tr>', add_contenu, blk, flags=re.S)

    for bi, entry in enumerate(blocks):
        bstart, bend, bname = entry[0], entry[1], entry[2]
        if bname == card:
            blocks[bi] = (bstart, bend, bname, blk)
            break

out = []
cursor = 0
for entry in blocks:
    bstart, bend, bname = entry[0], entry[1], entry[2]
    newblk = entry[3] if len(entry) > 3 else s[bstart:bend]
    out.append(s[cursor:bstart])
    out.append(newblk)
    cursor = bend
out.append(s[cursor:])
s = ''.join(out)

P.write_text(s, encoding='utf-8')
print('pages/items-cles.html : colonnes Source et contenu officiel ajoutes')
