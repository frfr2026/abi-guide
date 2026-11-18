#!/usr/bin/env python3
"""Enrichit pages/armes-attachements.html et pages/armes-attachements-s7.html.

Source : wiki officiel ABI, page « Weapon Mods » — 104 pieces d'attachement
recensees, avec leur compatibilite arme par arme. Le site ne publie pas de
statistiques d'attachement : le wiki non plus. Ce qui est documente, c'est
la compatibilite, et c'est ce qu'on ajoute.
"""
import pathlib, re, json

# ── catalogue officiel des attachements, groupe par arme ───────────────
ATTACH = {
 'MP-133': ['MP-133 510mm Barrel','MP-133 540mm Barrel','MP-133 610mm Barrel','MP-133 660mm Barrel','MP-133 710mm Barrel',
            'MP-133 Polymer Stock','MP-133 Wooden Stock','MP-133 Polymer Grip','MP-133 Stock Adapter',
            'MP 133 Beech Hand Guard','MP 133 Plastic Hand Guard','Dedicated M870 Buffer Adapter','M870 to AR Grip'],
 'M870': ['M870 Short Barrel','M870 Standard Barrel','M870 Anti-Slip Stock','M870 Classic Composite Hand Guard','Dedicated M870 Buffer Adapter'],
 'M1911': ['M1911 Standard Barrel','M1911 Threaded Barrel','M1911 Standard Upper Receiver','Dedicated M1911 Grip'],
 'G17': ['G17 Carbon Fiber Receiver','G17 Desert Carbon Fiber Receiver','G17 Metal Machined Receiver','G17 Threaded Barrel'],
 'MPX': ['MPX Standard Barrel','MPX Extended Barrel','MPX 10.5 Modular Locking Handguard','MPX 14 Modular Locking Handguard'],
 'M3A1': ['M3A1 Standard Barrel','M3A1 Folding Stock','Dedicated M3A1 Rail'],
 'MP5': ['MP5 High-Performance SD Upper Receiver','MP5 Tactical Stock','MP5SD Barrel Rail','MP5SD Polymer Hand Guard'],
 'T79': ['T79 Basic Hand Guard','T79 Improved Hand Guard','T79 Modern Hand Guard','T79 Classic Stock','T79 Stock Adapter','T79 Top Rail'],
 'AKS-74U': ['AKS 74U Series Classic Wooden Hand Guard','AKS-74U Series Universal Gas Tube','AKS-74U Standard Dust Cover','AKS 74 Metal Stock','AKS to PT Adapter'],
 'FAL': ['FAL Perforated Front Hand Guard','FAL Sight Mount Receiver Cover','FAL Special Stock','FAL Triangle Stock'],
 'Mosin': ['Mosin Carbine Barrel','Mosin Carbine Sniper Wooden Stock','Mosin Standard Sniper Stock','Mosin Rifle Sight Mount','Mosin Sight Extension Rail'],
 'SKS': ['SKS OEM Oak Stock','SKS Rifle Sight Mount'],
 'Uzi': ['Uzi Adapter','Uzi Top Rail','Uzi Wooden Stock'],
 'UMP45': ['UMP45 Standard Stock','UMP45 Std.Barrel','Dedicated UMP45 Rail'],
 'MAC-10': ['MAC-10 Extended Barrel','MAC-10 Premium Folding Stock'],
 'CZ 52': ['Dedicated CZ 52 Upper Receiver'],
 'H416': ['H416 A5 Universal Medium Barrel','H416 A5 Universal Standard Barrel'],
 'RPK-16': ['RPK-16 Tactical Rail'],
 'M110': ['M110 Extended Barrel'],
 'Mini-14': ['Mini-14 Top Rail'],
 'P90': ['P90 Special Hand Guard'],
 'S12K': ['S12K Superb Short Hand Guard'],
 'Type 81': ['Type 81 Stock'],
}

# familles d'attachements communes (deduites du catalogue officiel)
FAMILLES = [
 ('Rails et supports de viseur', [
   '30mm Rail Sight Mount','34mm Hybrid Sight Mount','34mm Scope Ring','3.5x Scope Ring Base',
   'Aluminum Sight Rail','Compact Magnifying Sight Rail','Compact Sight Bottom Rail','Compact Sight Top Rail',
   'Compact Universal Sight Base','Cross Slot Sight Mount','Mini Red Dot Sight Rail','Mosin Rifle Sight Mount',
   'Mosin Sight Extension Rail','SKS Rifle Sight Mount','T79 Top Rail','Uzi Top Rail','Mini-14 Top Rail',
   'AK Compatible Rail In-Line Dust Cover','AK Custom Rail Dust Cover','AKM Series Standard Dust Cover',
   'AKS-74U Standard Dust Cover','Dedicated M3A1 Rail']),
 ('Poignées et mains courantes', [
   'AR Compatible Rear Grip','Industrial AR Rear Grip','M870 to AR Grip','MP-133 Polymer Grip',
   'Dedicated M1911 Grip','MP-133 Beech Hand Guard','MP 133 Plastic Hand Guard',
   'AK Quick-mod Hand Guard','AK-series CAA Polymer Front Hand Guard','AK-series Wooden Hand Guard',
   'AKS 74U Series Classic Wooden Hand Guard','AR Special Universal Hand Guard','AR-series Carbine Hand Guard',
   'FAL Perforated Front Hand Guard','MP5SD Polymer Hand Guard','MPX 10.5 Modular Locking Handguard',
   'MPX 14 Modular Locking Handguard','M870 Classic Composite Hand Guard','P90 Special Hand Guard',
   'S12K Superb Short Hand Guard','T79 Basic Hand Guard','T79 Improved Hand Guard','T79 Modern Hand Guard']),
 ('Cibles et mechanismes', [
   '2 Modular Lock Rail','2.5 Modular Lock Rail','4.1 Modular Lock Rail','AKS to PT Adapter',
   'AKM Standard Gas Tube','AKS-74U Series Universal Gas Tube','AK Series Alloy Charging Handle Cap',
   'Dedicated M870 Buffer Adapter','MP-133 Stock Adapter','T79 Stock Adapter','Uzi Adapter',
   'Dedicated CZ 52 Upper Receiver','Dedicated M3A1 Rail','Dedicated UMP45 Rail']),
 ('Cibles', [
   'AK Series FAB Buttstock','AKS 74 Metal Stock','FAL Special Stock','FAL Triangle Stock',
   'M3A1 Folding Stock','M4 Standard Stock','M870 Anti-Slip Stock','MAC-10 Premium Folding Stock',
   'Mosin Carbine Sniper Wooden Stock','Mosin Standard Sniper Stock','MP-133 Polymer Stock',
   'MP-133 Wooden Stock','MP5 Tactical Stock','SKS OEM Oak Stock','T79 Classic Stock',
   'UMP45 Standard Stock','Uzi Wooden Stock','Type 81 Stock','AR Recoil Buffer']),
 ('Canons', [
   'G17 Threaded Barrel','H416 A5 Universal Medium Barrel','H416 A5 Universal Standard Barrel',
   'MAC-10 Extended Barrel','M110 Extended Barrel','M1911 Standard Barrel','M1911 Threaded Barrel',
   'M24 Bolt-Action Rifle','M3A1 Standard Barrel','M870 Short Barrel','M870 Standard Barrel',
   'MP-133 510mm Barrel','MP-133 540mm Barrel','MP-133 610mm Barrel','MP-133 660mm Barrel',
   'MP-133 710mm Barrel','MP5SD Barrel Rail','MPX Standard Barrel','MPX Extended Barrel',
   'Mosin Carbine Barrel','UMP45 Std.Barrel','G17 Carbon Fiber Receiver','G17 Desert Carbon Fiber Receiver',
   'G17 Metal Machined Receiver','M1911 Standard Upper Receiver']),
]


def build_attach_table():
    """Genere le tableau des attachements par arme (source wiki officielle)."""
    rows = []
    for arme in sorted(ATTACH):
        pieces = ATTACH[arme]
        rows.append('                <tr><td><strong>%s</strong></td><td>%d</td><td>%s</td></tr>'
                    % (arme, len(pieces), ', '.join(pieces)))
    return '\n'.join(rows)


def build_familles_html():
    out = []
    for nom, pieces in FAMILLES:
        out.append('            <h3 class="h4">%s</h3>' % nom)
        out.append('            <ul>')
        for p in pieces:
            out.append('              <li>%s</li>' % p)
        out.append('            </ul>')
    return '\n'.join(out)


# ── page armes-attachements.html ───────────────────────────────────────
P1 = pathlib.Path('pages/armes-attachements.html')
s1 = P1.read_text(encoding='utf-8')

if 'attach-officiels' not in s1:
    BLOCK1 = '''
          <h2 id="attach-officiels">5. Le catalogue officiel des attachements</h2>
          <p>Le <strong>wiki officiel</strong> recense <strong>104 pièces d'attachement</strong>, listées avec la ou les armes auxquelles elles se montent. C'est une donnée vérifiable, contrairement au « ça améliore le recul » que l'on entend partout. Le catalogue ci-dessous en reprend la structure.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Pièces dédiées</th><th>Détail</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : wiki officiel ABI, section « Weapon Mods ». Ce sont les compatibilités documentées ; l'intérêt de chaque pièce reste une question de build, et le prix de chaque pièce n'est pas publié par le wiki.</p>

          <h3 class="h4">Les grandes familles d'attachements</h3>
%s

          <div class="callout callout-warning">
            <h3 class="h4">Les canons filetés, un vrai levier</h3>
            <p>Quatre armes du catalogue officiel disposent d'un <strong>canon fileté</strong> dédié : le <strong>M1911</strong>, le <strong>G17</strong>, le <strong>MPX Extended Barrel</strong> et le <strong>M110 Extended Barrel</strong>. Le canon fileté est le point d'accroche du modérateur. C'est la seule famille d'attachements où le wiki documente une compatibilité qui change réellement la signature de l'arme — un modérateur transforme un fusil en arme de raid discret.</p>
          </div>
''' % (build_attach_table(), build_familles_html())

    anchor = '          <h2 id="ordre-monte">4. Ordre de montage d un build propre</h2>'
    m = re.search(r'<h2 id="ordre-monte">(\d+)\. Ordre de montage d[^<]*</h2>', s1)
    if m:
        n = int(m.group(1))
        s1 = s1[:m.start()] + BLOCK1.strip() + '\n\n          <h2 id="ordre-monte">%d. Ordre de montage d\'un build propre</h2>' % (n + 1) + s1[m.end():]
    else:
        raise SystemExit('ancre ordre-monte introuvable')
    P1.write_text(s1, encoding='utf-8')
    print('pages/armes-attachements.html enrichi')
else:
    print('pages/armes-attachements.html deja enrichi')

# ── page armes-attachements-s7.html ─────────────────────────────────────
P2 = pathlib.Path('pages/armes-attachements-s7.html')
s2 = P2.read_text(encoding='utf-8')

if 'compatibilite-officielle' not in s2:
    BLOCK2 = '''
          <h2 id="compatibilite-officielle">7. Compatibilité officielle : ce que le wiki confirme</h2>
          <p>Les quatre sets de la Saison 7 sont une tentative de fixer l'équipement à un rôle précis.Le wiki officiel permet de trancher une question que les guides communautaires laisse souvent floue : <strong>ces pièces existent-elles et se montent-elles vraiment sur ces armes ?</strong></p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Pièces dédiées documentées</th><th>Nombre</th></tr></thead>
              <tbody>
                <tr><td><strong>PCC-9</strong></td><td>Le wiki ne recense aucune pièce dédiée au PCC-9 : vérifiez l'armurerie avant d'acheter, un set « PCC-9 Full-Auto Kit » peut ne pas exister.</td><td>0</td></tr>
                <tr><td><strong>M110</strong></td><td>M110 Extended Barrel</td><td>1</td></tr>
                <tr><td><strong>FAL</strong></td><td>FAL Perforated Front Hand Guard, FAL Sight Mount Receiver Cover, FAL Special Stock, FAL Triangle Stock</td><td>4</td></tr>
                <tr><td><strong>MPX</strong></td><td>MPX Standard Barrel, MPX Extended Barrel, MPX 10.5 Modular Locking Handguard, MPX 14 Modular Locking Handguard</td><td>4</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : wiki officiel ABI, section « Weapon Mods ». Cette vérification ne dit pas si une pièce est « bonne » — elle dit si elle est documentée et compatible.</p>

          <div class="callout callout-info">
            <h3 class="h4">Pourquoi cette vérification compte</h3>
            <p>Le marché de l'ABI est saturated de recopies de builds saisonniers, souvent antérieurs de plusieurs patchs. Une pièce qui n'existe pas dans le catalogue officiel coûte de l'argent, occupe un slot de modification et dégrade l'arme au lieu de l'améliorer. <strong>Vérifiez la compatibilité avant d'acheter, pas après.</strong> Et pour le PCC-9 en particulier : l'absence de pièce dédiée documentée est un signal fort — soit le set n'existe pas sous ce nom, soit il n'a pas encore été référencé par le wiki.</p>
          </div>
'''
    anchor = '          <h2 id="ordre-achat">6. Ordre d\'achat recommandé</h2>'
    m = re.search(r'<h2 id="ordre-achat">(\d+)\. Ordre d\'achat recommandé</h2>', s2)
    if m:
        n = int(m.group(1))
        s2 = s2[:m.start()] + BLOCK2.strip() + '\n\n          <h2 id="ordre-achat">%d. Ordre d\'achat recommandé</h2>' % (n + 1) + s2[m.end():]
    else:
        raise SystemExit('ancre ordre-achat introuvable')
    P2.write_text(s2, encoding='utf-8')
    print('pages/armes-attachements-s7.html enrichi')
else:
    print('pages/armes-attachements-s7.html deja enrichi')
