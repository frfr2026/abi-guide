#!/usr/bin/env python3
"""Telechargement des artworks officiels servant de visuels uniques de page.

Chaque page du site doit disposer d'un visuel JPG distinct. On exploite
l'integralite des artworks officiels du jeu (wiki ABI) pour cela : armes
officielles, casques, gilets, sacs, masques, objets de loot.
"""
import pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fetch_official import fetch

# page -> (fichier wiki, sortie)
V = {
    # --- pages d'armes par segment (visuels d'armes officielles) ---
    'img/armes/vis-carbine.jpg':  'AK74N.png',
    'img/armes/vis-lmg.jpg':      'MDR.png',
    'img/armes/vis-pistolets.jpg': 'MP9.png',
    'img/armes/vis-shotgun.jpg':  'M870.png',
    'img/armes/vis-sniper.jpg':   'SVDS.png',
    'img/armes/vis-dmr.jpg':      'M14.png',
    'img/armes/vis-smg.jpg':      'MP5.png',
    'img/armes/vis-assaut.jpg':   'SCAR-L.png',
    'img/armes/vis-builds.jpg':   'AKM.png',
    'img/armes/vis-attachements.jpg': 'AUG.png',
    'img/armes/vis-nouveautes.jpg': 'AK102.png',
    'img/armes/vis-tierlist.jpg': 'MDR.png',
    # --- pages d'equipement (artworks officiels d'equipement) ---
    'img/gear/vis-casques.jpg':   'IND_Tactical_Helmet.png',
    'img/gear/vis-rigs.jpg':      'B3_Universal_Chest_Rig.png',
    'img/gear/vis-sacs.jpg':      'Canvas.backpack.png',
    'img/gear/vis-headsets.jpg':  'GS2_Tactical_headset.png',
    # --- pages d'items ---
    'img/items/vis-cles.jpg':     'Key1.png',
    'img/items/vis-medical.jpg':  'Standard_Military_First_Aid_Kit.png',
    'img/items/vis-munitions.jpg': '5.56x45mm_M855.png',
    'img/items/vis-ammo-hero.jpg': '7.62x39mm_PS.png',
    'img/items/vis-koen.jpg':     'Koen.png',
    'img/items/vis-valeur.jpg':   'Gold.png',
    'img/items/vis-craft.jpg':    'Nitrocellulose.png',
    'img/items/vis-workbench.jpg': 'Toolbox.png',
    'img/items/vis-collection.jpg': 'Safe.png',
    # --- pages d'evenements / communaute / cosmétiques ---
    'img/events/vis-calendrier.jpg': 'Airdrop.png',
    'img/events/vis-supplies.jpg':   'Abondoned.crate.icon.png',
    'img/events/vis-warlord.jpg':    'Weaponboxico.png',
    'img/communaute/vis-patch.jpg':  'Event1.png',
    'img/communaute/vis-ressources.jpg': 'Locations.main.png',
    'img/communaute/vis-streamers.jpg': 'Support.png',
    'img/personnages/vis-opérateur.jpg': 'Renoir.png',
    'img/personnages/vis-dogtags.jpg': 'Brooch.png',
    # --- pages meta / lore ---
    'img/meta/vis-builds.jpg':   'Missions.main.png',
    'img/meta/vis-roles.jpg':    'Combat.main.png',
    'img/meta/vis-optimizer.jpg': 'Mods.png',
    'img/meta/vis-tierlist.jpg': 'Weapons.main.png',
    'img/meta/vis-strategies.jpg': 'Provisions.main.png',
    'img/univers/vis-darkzone.jpg': 'Site-background-light.png',
    'img/univers/vis-factions.jpg': 'Mafia.png',
    'img/univers/vis-lore.jpg':   'Locations.main.png',
    # --- zombies / modes ---
    'img/zombies/vis-infected.jpg': 'Bosses.main.png',
    'img/zombies/vis-endless.jpg': 'Combat.main.png',
    'img/zombies/vis-research.jpg': 'Doss.png',
    'img/zombies/vis-balance.jpg': 'Support.png',
}

if __name__ == '__main__':
    ok, ko = 0, []
    for i, (out, wiki) in enumerate(V.items(), 1):
        p = pathlib.Path(out)
        r = fetch(wiki, p, target=1024, use_cache=False)
        if r:
            ok += 1
            print('  [%2d/%2d] %-36s %-32s %4d Ko' % (i, len(V), out, wiki, p.stat().st_size // 1024))
        else:
            ko.append((out, wiki))
            print('  [%2d/%2d] %-36s ECHEC %s' % (i, len(V), out, wiki))
        time.sleep(0.12)
    print('\nOK : %d | echecs : %d' % (ok, len(ko)))
    for o, w in ko:
        print('   ! %s <- %s' % (o, w))
