#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integration des visuels cinematiques dans les pages ABI NEXUS.

Deux actions :
  1. swap_visuel() remplace un fichier de figure par un visuel cinematique
     et met a jour width/height + alt.
  2. fix_alt() recale un alt sur le contenu reel du fichier (le fichier etait
     partage entre deux pages, l'alt decrivait une autre image).

Idempotent : rejouer le script ne change rien.
"""
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")

# ---------------------------------------------------------------- swaps
# (page, ancien src, nouveau src, width, height, nouvel alt)
SWAPS = [
    (
        "guide-progression.html",
        "../img/cards/var-progression.jpg",
        "../img/meta/vis-progression.jpg",
        1672, 941,
        "Operateur en silhouette gravissant un escalier metallique vers un rai de lumiere",
    ),
    (
        "saison8-attente.html",
        "../img/cards/card-balance.jpg",
        "../img/events/vis-attente-s8.jpg",
        1536, 1024,
        "Hangar militaire vide la nuit, caisses sous housses et bureau eclaire",
    ),
    (
        "saison7-zombie-endless.html",
        "../img/zombies/vis-endless.jpg",
        "../img/zombies/vis-endless-cinematique.jpg",
        1536, 1024,
        "Horde d'infectes avances dans le terminal desert d'un aeroport",
    ),
    (
        "events-calendrier.html",
        "../img/events/vis-calendrier.jpg",
        "../img/events/vis-calendrier-cinematique.jpg",
        1536, 1024,
        "Salle de planification tactique, carte du site epinglee au mur et lampe de bureau",
    ),
    (
        "equipement-armures.html",
        "../img/cards/card-armures.jpg",
        "../img/equipement/vis-armures-cinematique.jpg",
        1536, 1024,
        "Gilet pare-balles et casque balistique eclaires par une ampoule nue",
    ),
    (
        "items-collection-room.html",
        "../img/items/vis-collection.jpg",
        "../img/items/vis-collection-cinematique.jpg",
        1536, 1024,
        "Collectionnee d'objets rares ranges sur des etageres dans un batiment industriel abandonne",
    ),
    (
        "armes-tier-list.html",
        "../img/cards/card-h416.jpg",
        "../img/armes/vis-tierlist-cinematique.jpg",
        1536, 1024,
        "Deux fusils d'assaut poses sur un etabli dluive, cartouches a cote",
    ),
    (
        "univers-dark-zone.html",
        "../img/univers/vis-darkzone.jpg",
        "../img/univers/vis-darkzone-cinematique.jpg",
        1928, 816,
        "Port industriel noye de brume, conteneurs et grues sous un projecteur lointain",
    ),
]

# ---------------------------------------------------------------- alts
# (page, src, nouvel alt)  -- l'alt decrivait une image differente
ALTS = [
    (
        "communaute-ressources.html",
        "../img/communaute/vis-ressources.jpg",
        "Key art officiel du jeu : des photographies de sites poses sur une table, "
        "surmontes du titre LOCATIONS",
    ),
    (
        "univers-lore.html",
        "../img/univers/vis-lore.jpg",
        "Key art officiel du jeu : des photographies de sites poses sur une table, "
        "surmontes du titre LOCATIONS",
    ),
    (
        "communaute-streamers.html",
        "../img/communaute/vis-streamers.jpg",
        "Ecran de remerciement officiel du jeu mentionnant Tencent Games, Arena Breakout "
        "Infinite et Morefun Studio",
    ),
    (
        "saison7-balance-changes.html",
        "../img/zombies/vis-balance.jpg",
        "Ecran de remerciement officiel du jeu mentionnant Tencent Games, Arena Breakout "
        "Infinite et Morefun Studio",
    ),
    (
        "meta-builds-roles.html",
        "../img/meta/vis-roles.jpg",
        "Key art officiel du jeu : des mains tenant une arme, surmontes du titre COMBAT",
    ),
    (
        "items-valeur.html",
        "../img/items/vis-valeur.jpg",
        "Lingots d'or empiles, symbole de la valeur d'un butin a l'arene",
    ),
    (
        "items-munitions.html",
        "../img/items/vis-ammo-hero.jpg",
        "Cartouche 7.62x39 posee sur sa boite de munitions militaires",
    ),
    (
        "items-munitions.html",
        "../img/items/vis-munitions.jpg",
        "Cartouche 5.56x45 posee sur sa boite de munitions militaires",
    ),
    (
        "armes-tier-list.html",
        "../img/armes/vis-tierlist.jpg",
        "Armes alignees sur des rails dans une armurerie, sous un eclairage rasant",
    ),
]


def swap_visuel(text, page, old_src, new_src, w, h, alt):
    """Remplace src + width/height + alt pour toutes les occurrences de old_src."""
    if new_src in text:
        # deja migre : on se contente d'homogeneiser l'alt et les dimensions
        pattern = re.compile(
            r'<img\s+width="\d+"\s+height="\d+"\s+src="' + re.escape(new_src) + r'"'
            r'\s+alt="[^"]*"'
        )
        new_text, n = pattern.subn(
            '<img width="%d" height="%d" src="%s" alt="%s"' % (w, h, new_src, alt),
            text,
        )
        return new_text, n

    pattern = re.compile(
        r'<img\s+width="\d+"\s+height="\d+"\s+src="' + re.escape(old_src) + r'"'
        r'\s+alt="[^"]*"'
    )
    new_text, n = pattern.subn(
        '<img width="%d" height="%d" src="%s" alt="%s"' % (w, h, new_src, alt),
        text,
    )
    return new_text, n


def fix_alt(text, src, alt):
    """Recale l'alt d'un src donne, sans toucher au reste du tag."""
    pattern = re.compile(
        r'(<img\s+width="\d+"\s+height="\d+"\s+src="' + re.escape(src) + r'"\s+alt=")[^"]*(")'
    )
    new_text, n = pattern.subn(lambda m: m.group(1) + alt + m.group(2), text)
    return new_text, n


def main():
    total = 0
    for page, old_src, new_src, w, h, alt in SWAPS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT page :", page)
            continue
        text = f.read_text(encoding="utf-8")
        new_text, n = swap_visuel(text, page, old_src, new_src, w, h, alt)
        if n:
            f.write_text(new_text, encoding="utf-8")
            total += n
            print("  swap  %-32s %s -> %s (%d)" % (page, old_src.split("/")[-1],
                                                 new_src.split("/")[-1], n))
        else:
            print("  SKIP  %-32s %s" % (page, old_src.split("/")[-1]))

    for page, src, alt in ALTS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT page :", page)
            continue
        text = f.read_text(encoding="utf-8")
        new_text, n = fix_alt(text, src, alt)
        if n:
            f.write_text(new_text, encoding="utf-8")
            total += n
            print("  alt   %-32s %s" % (page, src.split("/")[-1]))
        else:
            print("  SKIP  %-32s %s" % (page, src.split("/")[-1]))

    print("\ntotal :", total)
    return 0 if total >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())
