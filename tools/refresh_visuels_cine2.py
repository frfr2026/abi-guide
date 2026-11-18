#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vague 2 : remplace les 10 figures de page en 800x450 / 720x480 par des visuels
cinematographiques en haute definition, et supprime les fichiers remplaces.

Idempotent.
"""
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")

# (page, ancien src, nouveau src, width, height, nouvel alt)
SWAPS = [
    (
        "armes-fusils-assaut.html",
        "../img/cards/card-fal.jpg",
        "../img/armes/vis-fal-cinematique.jpg",
        3120, 2080,
        "Fusil d'assaut a crosse en bois appuye contre un mur de beton dans une armurerie",
    ),
    (
        "armes-nouveautes-s7.html",
        "../img/cards/card-ak15sc.jpg",
        "../img/armes/vis-ak15sc-cinematique.jpg",
        3120, 2080,
        "Fusil d'assaut noir moderne sur un râtelier d'armurerie",
    ),
    (
        "cosmetiques-skins-armes.html",
        "../img/cards/card-s7battle.jpg",
        "../img/armes/vis-skins-armes-cinematique.jpg",
        3120, 2080,
        "Fusil orne d'un skin iridescent violet et turquoise presente sur un support",
    ),
    (
        "items-collection-room.html",
        "../img/cards/card-collection.jpg",
        "../img/items/vis-trophy-room-cinematique.jpg",
        3184, 2147,
        "Salle de trophees(ICV) : des vitrines eclairees Alignment presentationnent des objets rares recuperes",
    ),
    (
        "items-munitions.html",
        "../img/cards/card-ammo.jpg",
        "../img/items/vis-stand-tir-cinematique.jpg",
        3120, 2080,
        "Stand de tir couvert de douilles de bronze, dans la poussiere des projecteurs",
    ),
    (
        "meta-builds-roles.html",
        "../img/cards/card-m24.jpg",
        "../img/meta/vis-sniper-cinematique.jpg",
        3120, 2080,
        "Fusil de precision a lunette posee sur un rebord de fenetre, ville brumeuse a l'aube",
    ),
    (
        "saison7-utopia.html",
        "../img/cards/card-saison7.jpg",
        "../img/saison7/vis-utopia-cinematique.jpg",
        3184, 2156,
        "Ferme envahie par une contamination biologique verte et lumineuse",
    ),
    (
        "saison7-nouveautes.html",
        "../img/cards/card-s7news.jpg",
        "../img/events/vis-s7news-cinematique.jpg",
        3120, 2080,
        "Mur de newsroom couvert de documents epingles, eclaire par une lampe de bureau",
    ),
    (
        "saison7-utopia.html",
        "../img/events/var-s7news.jpg",
        "../img/events/var-s7news-cinematique.jpg",
        3120, 2080,
        "Studio de diffusionTV abandonne, melangeur et eclairage mort dans le noir",
    ),
    (
        "saison7-zombie-endless.html",
        "../img/cards/card-endless.jpg",
        "../img/zombies/vis-endless-entree.jpg",
        3184, 2151,
        "Arene souterraine foddee de projecteurs,propylenee d'un groupe a l'entree du tunnel",
    ),
]

SUPPRIMER = [
    "img/cards/card-fal.jpg",
    "img/cards/card-ak15sc.jpg",
    "img/cards/card-s7battle.jpg",
    "img/cards/card-collection.jpg",
    "img/cards/card-ammo.jpg",
    "img/cards/card-m24.jpg",
    "img/cards/card-saison7.jpg",
    "img/cards/card-s7news.jpg",
    "img/events/var-s7news.jpg",
    "img/cards/card-endless.jpg",
]


def swap(text, old_src, new_src, w, h, alt):
    if new_src in text:
        pattern = re.compile(
            r'<img\s+width="\d+"\s+height="\d+"\s+src="' + re.escape(new_src) + r'"\s+alt="[^"]*"'
        )
        return pattern.subn(
            '<img width="%d" height="%d" src="%s" alt="%s"' % (w, h, new_src, alt), text
        )
    pattern = re.compile(
        r'<img\s+width="\d+"\s+height="\d+"\s+src="' + re.escape(old_src) + r'"\s+alt="[^"]*"'
    )
    return pattern.subn(
        '<img width="%d" height="%d" src="%s" alt="%s"' % (w, h, new_src, alt), text
    )


def main():
    total = 0
    for page, old_src, new_src, w, h, alt in SWAPS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT page :", page)
            continue
        text = f.read_text(encoding="utf-8")
        new_text, n = swap(text, old_src, new_src, w, h, alt)
        if n:
            f.write_text(new_text, encoding="utf-8")
            total += n
            print("  swap  %-32s %s -> %s" % (page, old_src.split("/")[-1], new_src.split("/")[-1]))
        else:
            print("  SKIP  %-32s %s" % (page, old_src.split("/")[-1]))

    # supprimer les remplaces orphelins
    corpus = ""
    for pat in ("*.html", "pages/*.html", "css/*.css", "js/*.js", "js/*.json"):
        for p in pathlib.Path(".").glob(pat):
            if "node_modules" in str(p):
                continue
            try:
                corpus += p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                pass
    for old in SUPPRIMER:
        base = old.split("/")[-1]
        if base in corpus:
            print("  garde  %s (reference subsistante)" % old)
            continue
        p = pathlib.Path(old)
        if p.exists():
            p.unlink()
            print("  purge %s" % old)

    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
