#!/usr/bin/env python3
"""Telechargement des artworks officiels d'equipement (casques, rigs, sacs, headsets) -> JPG."""
import pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fetch_official import fetch

GEAR = {
    # casques (page equipement-casques)
    'img/gear/helmet-6b4.jpg':      '6B4_Helmet.png',
    'img/gear/helmet-6b5.jpg':      '6B5_Helmet.png',
    'img/gear/helmet-f70.jpg':      'F70_Tactical_Helmet.png',
    'img/gear/helmet-f80.jpg':      'F80_Tactical_Helmet.png',
    'img/gear/helmet-kss2.jpg':     'KSS2_Tactical_Helmet.png',
    'img/gear/helmet-sh40.jpg':     'SH40_Military_Helmet.png',
    'img/gear/helmet-sh60.jpg':     'SH60_Military_Helmet.png',
    'img/gear/helmet-ind70.jpg':    'IND70_Tactical_Helmet.png',
    'img/gear/helmet-an95.jpg':     'AN95_Heavy_Blast_Helmet.png',
    'img/gear/helmet-6bnt.jpg':     '6BNT_Helmet.png',
    # rigs / gilets (page equipement-rigs)
    'img/gear/rig-b3.jpg':          'B3_Universal_Chest_Rig.png',
    'img/gear/rig-b4.jpg':          'B4_Tactical_Chest_Rig.png',
    'img/gear/rig-b6.jpg':          'B6_Tactical_Chest_Rig.png',
    'img/gear/rig-militia.jpg':     'Militia_Chest_Rig.png',
    'img/gear/rig-al-assault.jpg':  'AL_Assault_Armored_Rig.png',
    'img/gear/rig-h_tac-a8.jpg':    'H-Tac_A8_Armored_Rig.png',
    'img/gear/rig-service.jpg':     'Service_Tactical_Vest.png',
    'img/gear/rig-926-nightowl.jpg': '926_Night_Owl_Chest_Rig.png',
    'img/gear/rig-stormtrooper.jpg': 'Stormtrooper_Type_3_Tactical_Chest_Rig.png',
    # sacs (page equipement-sacs)
    'img/gear/bag-canvas.jpg':      'Canvas.backpack.png',
    'img/gear/bag-cowhide.jpg':     'Cowhide.backpack.png',
    'img/gear/bag-chapman.jpg':     'Chapman.military.backpack.png',
    'img/gear/bag-large.jpg':       'Large.camping.backpack.png',
    'img/gear/bag-lightweight.jpg': 'Lightweight.camping.backpack.png',
    'img/gear/bag-luc.jpg':         'Luc.expanded.tactical.backpack.png',
    'img/gear/bag-med.jpg':         'Med.field.backpack.png',
    'img/gear/bag-rush.jpg':        'Rush.tactical.backpack.png',
    'img/gear/bag-simple.jpg':      'Simple.backpack.png',
    'img/gear/bag-sports.jpg':      'Sports.backpack.png',
    'img/gear/bag-duffle.jpg':      'Duffle_Bag.png',
    'img/gear/bag-sling.jpg':       'Sling_Bag.png',
    # headsets (page equipement-headsets)
    'img/gear/headset-com1.jpg':    'Com1_Tactical_Headset.png',
    'img/gear/headset-cmd.jpg':     'Commander_A_Tactical_Headset.png',
    'img/gear/headset-gs2.jpg':     'GS2_Tactical_headset.png',
    'img/gear/headset-m32.jpg':     'M32_Tactical_Headset.png',
    'img/gear/headset-z038.jpg':    'Z038_Tactical_Headset.png',
    # masques
    'img/gear/mask-an95.jpg':       'AN95_Military_Bulletproof_Mask.png',
    'img/gear/mask-dk7.jpg':        'DK7_Premium_Bulletproof_Mask.png',
    'img/gear/mask-sh60.jpg':       'SH60_Mask.png',
    'img/gear/mask-sh65.jpg':       'SH65_Military_Mask_B.png',
    'img/gear/mask-rst.jpg':        'RST_Special_Forces_Mask.png',
    'img/gear/mask-gli-f4.jpg':     'GLI-F4_Tear_Gas.png',
}

if __name__ == '__main__':
    ok, ko = 0, []
    for i, (out, wiki) in enumerate(GEAR.items(), 1):
        p = pathlib.Path(out)
        r = fetch(wiki, p, target=1024, use_cache=False)
        if r:
            ok += 1
            print('  [%2d/%2d] %-30s %4d Ko' % (i, len(GEAR), out, p.stat().st_size // 1024))
        else:
            ko.append(out)
            print('  [%2d/%2d] %-30s ECHEC' % (i, len(GEAR), out))
        time.sleep(0.12)
    print('\nOK : %d | echecs : %d' % (ok, len(ko)))
    for k in ko:
        print('   ! ' + k)
