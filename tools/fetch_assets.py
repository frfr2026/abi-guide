#!/usr/bin/env python3
"""Telechargement en lot des artworks officiels ABI (wiki) et cablage JSON."""
import json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fetch_official import fetch

ROOT = pathlib.Path('.')

# id du site -> fichier wiki officiel
MAP = {
    # armes
    'm4a1': ('img/armes/m4a1.jpg', 'M4A1.png'),
    'ak12': ('img/armes/ak12.jpg', 'AK12.png'),
    'aek971': ('img/armes/aek971.jpg', 'AEK.png'),
    'an94': ('img/armes/an94.jpg', 'AN94.png'),
    'fal': ('img/armes/fal.jpg', 'FAL.png'),
    'm110': ('img/armes/m110.jpg', 'M110.png'),
    'mk14': ('img/armes/mk14.jpg', 'MK14.png'),
    'sj16': ('img/armes/sj16.jpg', 'SJ16.png'),
    'm24': ('img/armes/m24.jpg', 'M24.png'),
    'mosin': ('img/armes/mosin.jpg', 'Mosin.png'),
    'mpx': ('img/armes/mpx.jpg', 'MPX.png'),
    'p90': ('img/armes/p90.jpg', 'P90.png'),
    'vss': ('img/armes/vss.jpg', 'VSS.png'),
    'vector': ('img/armes/vector.jpg', 'Vector 45.png'),
    'sks': ('img/armes/sks.jpg', 'SKS.png'),
    'usas12': ('img/armes/usas12.jpg', 'USAS12.png'),
    'rpk16': ('img/armes/rpk16.jpg', 'RPK16.png'),
    'h416': ('img/armes/h416.jpg', 'H416.png'),
    'u191': ('img/armes/u191.jpg', 'U191.png'),
    'pcc9': ('img/armes/pcc9.jpg', 'PCC-9.png'),
    # armures
    'bt101': ('img/armures/bt101.jpg', 'BT101 Tactical Body Armor.png'),
    '926composite': ('img/armures/926composite.jpg', '926 Composite Body Armor.png'),
    'bt6': ('img/armures/bt6.jpg', 'BT6 Heavy Body Armor.png'),
    '6b13': ('img/armures/6b13.jpg', '6B13 Body Armor.png'),
    '6b23': ('img/armures/6b23.jpg', '6B23 Body Armor.png'),
    '6b45': ('img/armures/6b45.jpg', '6B45 Heavy Body Armor.png'),
    'kn': ('img/armures/kn.jpg', 'KN Assault Body Armor.png'),
    # objets
    'gpu': ('img/items/gpu.jpg', 'Graphics_Card.png'),
    'militarycircuit': ('img/items/militarycircuit.jpg', 'Circuit_Board.png'),
    'goldbar': ('img/items/goldbar.jpg', 'Gold.png'),
    'rolex': ('img/items/rolex.jpg', 'Gold_Watch.png'),
    'keycard': ('img/items/keycard.jpg', 'Command.room.keycard.png'),
    'medkit': ('img/items/medkit.jpg', '100D_Battlefield_Medkit.png'),
    'bandage': ('img/items/bandage.jpg', 'Field_Bandage.png'),
    # munitions
    '545hp': ('img/ammo/545hp.jpg', '5.45x39mm_HP.png'),
    '545ps': ('img/ammo/545ps.jpg', '5.45x39mm_PS.png'),
    '545pp': ('img/ammo/545pp.jpg', '5.45x39mm_PP.png'),
    '545bp': ('img/ammo/545bp.jpg', '5.45x39mm_BP.png'),
    '545bs': ('img/ammo/545bs.jpg', '5.45x39mm_BS.png'),
    'm855': ('img/ammo/m855.jpg', '5.56x45mm_M855.png'),
    'm855a1': ('img/ammo/m855a1.jpg', '5.56x45mm_M855A1.png'),
    'm995': ('img/ammo/m995.jpg', '5.56x45mm_M995.png'),
    'ss190': ('img/ammo/ss190.jpg', '5.7x28mm_SS190.png'),
    'l191': ('img/ammo/l191.jpg', '5.7x28mm_L191.png'),
    'ss198': ('img/ammo/ss198.jpg', '5.7x28mm_SS198.png'),
    'ss197sr': ('img/ammo/ss197sr.jpg', '5.7x28mm_SS197SR.png'),
    '762ps': ('img/ammo/762ps.jpg', '7.62x39mm_PS.png'),
    't45m': ('img/ammo/t45m.jpg', '7.62x39mm_T45M.png'),
    'bp762': ('img/ammo/bp762.jpg', '7.62x39mm_BP.png'),
    'ap762': ('img/ammo/ap762.jpg', '7.62x39mm_AP.png'),
    'bpz': ('img/ammo/bpz.jpg', '7.62x51mm_BPZ.png'),
    'm80': ('img/ammo/m80.jpg', '7.62x51mm_M80.png'),
    'm62': ('img/ammo/m62.jpg', '7.62x51mm_M62.png'),
    'm61': ('img/ammo/m61.jpg', '7.62x51mm_M61.png'),
    'lps': ('img/ammo/lps.jpg', '7.62x54mm_LPS.png'),
    't46m': ('img/ammo/t46m.jpg', '7.62x54mm_T46M.png'),
    '7bt1': ('img/ammo/7bt1.jpg', '7.62x54mm_7BT1.png'),
    'snb': ('img/ammo/snb.jpg', '7.62x54mm_SNB.png'),
    '7n37': ('img/ammo/7n37.jpg', '7.62x54mm_7N37.png'),
    'pso': ('img/ammo/pso.jpg', '9x19mm_PSO.png'),
    'pst9': ('img/ammo/pst9.jpg', '9x19mm_Pst.png'),
    'ap63': ('img/ammo/ap63.jpg', '9x19mm_AP6.3.png'),
    '7n31': ('img/ammo/7n31.jpg', '9x19mm_7N31.png'),
    'dumdum': ('img/ammo/dumdum.jpg', '9x19mm_DumDum.png'),
    'sp5': ('img/ammo/sp5.jpg', '9x39mm_SP5.png'),
    'sp6': ('img/ammo/sp6.jpg', '9x39mm_SP6.png'),
    '7n9': ('img/ammo/7n9.jpg', '9x39mm_7N9.png'),
    '7n12': ('img/ammo/7n12.jpg', '9x39mm_7N12.png'),
    '45hs': ('img/ammo/45hs.jpg', '.45_HS.png'),
    '45fmj': ('img/ammo/45fmj.jpg', '.45_FMJ.png'),
    '45ap': ('img/ammo/45ap.jpg', '.45_AP.png'),
    'gtslug': ('img/ammo/gtslug.jpg', '12x70mm_GT_Slug.png'),
    'apslug': ('img/ammo/apslug.jpg', '12x70mm_Armor-Piercing_Slug.png'),
    'flechette': ('img/ammo/flechette.jpg', '12x70mm_Flechette_Buckshot.png'),
    'ripslug': ('img/ammo/ripslug.jpg', '12x70mm_RIP_Slug.png'),
    'type5': ('img/ammo/type5.jpg', '12x70mm_Type_5_Buckshot.png'),
}

if __name__ == '__main__':
    only = sys.argv[1] if len(sys.argv) > 1 else None
    ok, ko, skip = [], [], []
    for i, (key, (out, wiki)) in enumerate(MAP.items(), 1):
        if only and only not in key:
            continue
        p = ROOT / out
        r = fetch(wiki, p, target=1024, use_cache=False)
        if r:
            ok.append((key, out, p.stat().st_size // 1024))
            print('  [%2d/%2d] %-16s %-34s %4d Ko' % (i, len(MAP), key, wiki, p.stat().st_size // 1024))
        else:
            ko.append((key, wiki))
            print('  [%2d/%2d] %-16s ECHEC %s' % (i, len(MAP), key, wiki))
        time.sleep(0.15)
    print('\nTelecharges : %d | echecs : %d' % (len(ok), len(ko)))
    if ko:
        for k, w in ko:
            print('   ! %s -> %s' % (k, w))
