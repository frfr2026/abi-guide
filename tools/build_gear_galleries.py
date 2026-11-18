#!/usr/bin/env python3
"""Injecte des galeries d'artworks officiels dans les pages d'equipement."""
import pathlib, re

ROOT = pathlib.Path('.')

# chemin local -> nom wiki (source : tools/fetch_gear.py)
GEAR = {
 'img/gear/helmet-6b4.jpg': '6B4_Helmet.png',
 'img/gear/helmet-6b5.jpg': '6B5_Helmet.png',
 'img/gear/helmet-f70.jpg': 'F70_Tactical_Helmet.png',
 'img/gear/helmet-f80.jpg': 'F80_Tactical_Helmet.png',
 'img/gear/helmet-kss2.jpg': 'KSS2_Tactical_Helmet.png',
 'img/gear/helmet-sh40.jpg': 'SH40_Military_Helmet.png',
 'img/gear/helmet-sh60.jpg': 'SH60_Military_Helmet.png',
 'img/gear/helmet-ind70.jpg': 'IND70_Tactical_Helmet.png',
 'img/gear/helmet-an95.jpg': 'AN95_Heavy_Blast_Helmet.png',
 'img/gear/helmet-6bnt.jpg': '6BNT_Helmet.png',
 'img/gear/rig-b3.jpg': 'B3_Universal_Chest_Rig.png',
 'img/gear/rig-b4.jpg': 'B4_Tactical_Chest_Rig.png',
 'img/gear/rig-b6.jpg': 'B6_Tactical_Chest_Rig.png',
 'img/gear/rig-militia.jpg': 'Militia_Chest_Rig.png',
 'img/gear/rig-al-assault.jpg': 'AL_Assault_Armored_Rig.png',
 'img/gear/rig-h_tac-a8.jpg': 'H-Tac_A8_Armored_Rig.png',
 'img/gear/rig-service.jpg': 'Service_Tactical_Vest.png',
 'img/gear/rig-926-nightowl.jpg': '926_Night_Owl_Chest_Rig.png',
 'img/gear/rig-stormtrooper.jpg': 'Stormtrooper_Type_3_Tactical_Chest_Rig.png',
 'img/gear/bag-canvas.jpg': 'Canvas.backpack.png',
 'img/gear/bag-cowhide.jpg': 'Cowhide.backpack.png',
 'img/gear/bag-chapman.jpg': 'Chapman.military.backpack.png',
 'img/gear/bag-large.jpg': 'Large.camping.backpack.png',
 'img/gear/bag-lightweight.jpg': 'Lightweight.camping.backpack.png',
 'img/gear/bag-luc.jpg': 'Luc.expanded.tactical.backpack.png',
 'img/gear/bag-med.jpg': 'Med.field.backpack.png',
 'img/gear/bag-rush.jpg': 'Rush.tactical.backpack.png',
 'img/gear/bag-simple.jpg': 'Simple.backpack.png',
 'img/gear/bag-sports.jpg': 'Sports.backpack.png',
 'img/gear/bag-duffle.jpg': 'Duffle_Bag.png',
 'img/gear/bag-sling.jpg': 'Sling_Bag.png',
 'img/gear/headset-com1.jpg': 'Com1_Tactical_Headset.png',
 'img/gear/headset-cmd.jpg': 'Commander_A_Tactical_Headset.png',
 'img/gear/headset-gs2.jpg': 'GS2_Tactical_headset.png',
 'img/gear/headset-m32.jpg': 'M32_Tactical_Headset.png',
 'img/gear/headset-z038.jpg': 'Z038_Tactical_Headset.png',
 'img/gear/mask-an95.jpg': 'AN95_Military_Bulletproof_Mask.png',
 'img/gear/mask-dk7.jpg': 'DK7_Premium_Bulletproof_Mask.png',
 'img/gear/mask-sh60.jpg': 'SH60_Mask.png',
 'img/gear/mask-sh65.jpg': 'SH65_Military_Mask_B.png',
 'img/gear/mask-rst.jpg': 'RST_Special_Forces_Mask.png',
 'img/gear/mask-gli-f4.jpg': 'GLI-F4_Tear_Gas.png',
}

# familles -> (page cible, titre, chapeau, cle d'image relative a la page)
FAMILLES = {
 'helmet': ('pages/equipement-casques.html', 'Les casques du jeu, article par article',
            'Artworks officiels du wiki ABI. Le numero de fin de nom est le <strong>tier de protection</strong> : '
            'plus le chiffre est eleve, plus le casque encaisse — et plus il pese.'),
 'rig': ('pages/equipement-rigs.html', 'Les rigs et gilets, article par article',
         'Artworks officiels du wiki ABI. Un rig n\'ajoute aucune protection : il ajoute de la capacite. '
         'Les modeles « Armored Rig » embarquent une plaque, les autres non.'),
 'bag': ('pages/equipement-sacs.html', 'Les sacs, article par article',
         'Artworks officiels du wiki ABI. La taille du sac dicte votre debit d\'extraction : chaque kilo '
         'supplementaire ralentit votre sortie de zone.'),
 'headset': ('pages/equipement-headsets.html', 'Les casques audio, article par article',
             'Artworks officiels du wiki ABI. Un casque audio ne change pas vos statistiques : il change '
             'le moment ou vous apprenez qu\'un enemy est la.'),
 'mask': ('pages/equipement-casques.html', 'Les masques, article par article',
          'Artworks officiels du wiki ABI. Le casque protege le crane, le masque protege le mid-face : '
          'nez, bouche et yeux restent la faille numero 1 des tirs a la tete.'),
}

DESC = {
 '6B4': 'Casque lourd d\'entree de gamme, le standard des petits calibres.',
 '6B5': 'Version.amelioree du 6B4, premiere evolution notable de la serie.',
 'F70': 'Casque tactique F70, equilibre protection et mobilite.',
 'F80': 'Le F80, un cran au-dessus du F70 en protection contre les tirs.',
 'KSS2': 'Casque KSS2 concu pour leshfill, correcteur integre.',
 'SH40': 'Casque militaire SH40, cap Serie T5.',
 'SH60': 'SH60 militaire, protection superieure et poids en consequence.',
 'IND70': 'IND70, l\'un des meilleurs casques du jeu pour les lobbies Forbidden.',
 'AN95': 'Casque lourd anti-blast AN95, usage special pour les raids et les boss.',
 '6BNT': '6BNT, modele recent de la famille 6B.',
 'B3': 'Chest rig universal B3, six a huit poches et un poids negligeable.',
 'B4': 'Chest rig tactique B4, plus de poches que le B3.',
 'B6': 'B6, l\'evolution la plus chargeuse de la famille B.',
 'Militia': 'Rig milice,charge et modules Rig.',
 'AL Assault': 'Rig AL Assault, premier pas vers le blindage.',
 'H-Tac A8': 'H-Tac A8, rig blindé pour l\'endurance.',
 'Service': 'Gilet de service, l\'entree de gamme du vestiaire.',
 '926 Night Owl': 'Rig 926 Night Owl, très reconnu en escouade.',
 'Stormtrooper': 'Stormtrooper Type 3, la version haute capacite.',
 'Canvas': 'Sac canvas, l\'EDC le plus simple.',
 'Cowhide': 'Sac cowhide, rendue solide et lourdement capacitaire.',
 'Chapman': 'Sac militaire Chapman, usage terrain.',
 'Large': 'Grand sac de camping, volume maximal.',
 'Lightweight': 'Sac leger, l\'opte du raid rapide.',
 'Luc': 'Luc expanded, sac tactique deployable.',
 'Med': 'Sac de terrain Med, usage medical et raid standard.',
 'Rush': 'Rush, sac tactique rapide a ouvrir.',
 'Simple': 'Sac simple, le compromis standard.',
 'Sports': 'Sac de sport, grande capacite peu structuree.',
 'Duffle': 'Duffle bag, volume de transport classique.',
 'Sling': 'Sling bag, port rapide en epaule.',
 'Com1': 'Com1, casque audio tactique basique.',
 'Commander A': 'Commander A, le modele de reference du jeu.',
 'GS2': 'GS2, casque audio avec isolation renforcee.',
 'M32': 'M32, casque audio de l\'equipe.',
 'Z038': 'Z038, reference haute de gamme.',
 'AN95 Mask': 'Masque pare-balles AN95, couvre le mid-face.',
 'DK7': 'Masque DK7 premium, protection du visage complete.',
 'SH60 Mask': 'Masque SH60, associe au casque SH60.',
 'SH65': 'Masque militaire SH65, robuste et sealed.',
 'RST': 'Masque RST des forces speciales.',
 'GLI-F4': 'Masque anti-gaz GLI-F4, protection chimique.',
}


def label(path, wiki):
    stem = pathlib.Path(path).stem
    key = stem.split('-', 1)[1] if '-' in stem else stem
    key = key.replace('_', ' ').replace('-', ' ')
    # correspondance avec la description
    best = ''
    for k in DESC:
        kk = k.lower().replace(' ', '')
        if kk.replace(' ', '') in key.replace(' ', '').lower() or key.lower().replace(' ', '').startswith(kk.replace(' ', '')):
            best = k
            break
    return key, DESC.get(best, '')


def build_gallery(famille):
    items = [(p, w) for p, w in GEAR.items() if pathlib.Path(p).stem.split('-')[0] == famille]
    cards = []
    for p, w in items:
        name, desc = label(p, w)
        cards.append(
            '            <article class="item-card">\n'
            '              <div class="card-media"><img width="1024" height="1024" src="../%s" alt="%s" loading="lazy" decoding="async"></div>\n'
            '              <div class="card-body">\n'
            '                <h3 class="card-title weapon-name">%s</h3>\n'
            '                <p class="card-text">%s</p>\n'
            '              </div>\n'
            '            </article>' % (p, name, name, desc))
    return '\n'.join(cards)


def inject(famille):
    page, titre, chapeau = FAMILLES[famille]
    p = ROOT / page
    s = p.read_text(encoding='utf-8')
    ancre = 'galerie-officielle' if famille != 'mask' else 'galerie-masques'
    if 'id="%s"' % ancre in s:
        print('  %-34s deja presente' % page)
        return
    gallery = '''          <h2 id="%s">%s</h2>
          <p>%s</p>
          <div class="items-grid">
%s
          </div>

''' % (ancre, titre, chapeau, build_gallery(famille))
    # insertion avant la fermeture de l'article
    end = s.find('        </article>')
    if end < 0:
        print('  ! %s : article introuvable' % page); return
    s = s[:end] + gallery + s[end:]
    # entree de sommaire
    m = re.search(r'(<aside class="toc".*?)(</aside>)', s, re.S)
    if m:
        libelle = titre.replace('Les ', '').replace('les ', '').replace(', article par article', '')
        s = s[:m.end(1)] + '\n<a href="#%s" id="lnk-galerie-%s">%s</a>' % (ancre, famille, libelle) + s[m.end(1):]
    p.write_text(s, encoding='utf-8')
    n = len(build_gallery(famille).split('<article'))
    print('  %-34s galerie de %d elements' % (page, n))


if __name__ == '__main__':
    for f in FAMILLES:
        inject(f)
