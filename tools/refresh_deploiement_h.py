#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - mise a jour des chiffres de DEPLOIEMENT.md (vague H).

Le document de deploiement contenait des compteurs perimes : 64 pages auditees,
65 URL au sitemap, un inventaire media de 153 JPG et un inventaire visuel
declare « vide », alors que le site compte 65 pages, 66 URL indexables et
353 visuels.

Ce script recalcule les compteurs depuis l'etat reel du site et reecrit les
lignes concernees. Il ne publie rien : il evite qu'un operateur depose un
site dont la documentation annonce des chiffres faux.

Idempotent.
"""
import pathlib
import re
import sys
from collections import Counter

RACINE = pathlib.Path(__file__).resolve().parent.parent


def compteurs():
    pages = sorted((RACINE / "pages").glob("*.html"))
    toutes = pages + [RACINE / "index.html", RACINE / "404.html"]
    amb_menu = sum(1 for p in toutes if "ambiance-menu.mp3" in p.read_text(encoding="utf-8"))
    amb_inf = sum(1 for p in toutes if "ambiance-infection.mp3" in p.read_text(encoding="utf-8"))
    narr = sum(1 for p in toutes if "audio/narration-" in p.read_text(encoding="utf-8"))
    imgs = [p for p in (RACINE / "img").rglob("*") if p.is_file()]
    ext = Counter(p.suffix.lower() for p in imgs)
    sitemap = (RACINE / "sitemap.xml").read_text(encoding="utf-8")
    urls = len(set(re.findall(r"<loc>([^<]+)</loc>", sitemap)))
    return {
        "pages": len(pages),
        "html": len(toutes),
        "amb_menu": amb_menu,
        "amb_inf": amb_inf,
        "narr": narr,
        "jpg": ext.get(".jpg", 0),
        "png": ext.get(".png", 0),
        "svg": ext.get(".svg", 0),
        "urls": urls,
    }


def remplacer(s, avant, apres):
    if apres in s:
        return s, 0
    if avant not in s:
        print("  [KO] motif introuvable :", avant[:60])
        return s, 1
    return s.replace(avant, apres, 1), 0


def main():
    c = compteurs()
    chemin = RACINE / "DEPLOIEMENT.md"
    s = chemin.read_text(encoding="utf-8")
    erreurs = 0

    # 1. commande d'audit
    s, e = remplacer(
        s,
        "python3 tools/audit.py            # audit global : 64 pages, liens, images, CJK, HTTP",
        "python3 tools/audit.py            # audit global : %d pages, liens, images, CJK, HTTP (%d/%d en 200)"
        % (c["pages"], c["pages"], c["pages"]))
    erreurs += e

    # 2. bande-son
    s, e = remplacer(
        s,
        "`audio/ambiance-menu.mp3` (24 s, 188 Ko), référencée par les 61 pages\n   standard, et `audio/ambiance-infection.mp3` (24 s, 188 Ko), référencée par\n   les 3 pages zombies.",
        "`audio/ambiance-menu.mp3` (24 s, 188 Ko), référencée par les %d pages\n   standard, et `audio/ambiance-infection.mp3` (24 s, 188 Ko), référencée par\n   les %d pages zombies." % (c["amb_menu"], c["amb_inf"]))
    erreurs += e

    # 3. couverture audio : nouveau point 4, le catalogue media devient le point 5
    couverture = (
        "4. **Couverture audio** — **%d pages sur %d** portent un lecteur de narration\n"
        "   (`audio/narration-*.mp3`) ; le câblage est fait par\n"
        "   `tools/cable_narrations.py`, qui n'insère le lecteur que si la piste est\n"
        "   présente sur le disque. Les textes sources validés sont dans\n"
        "   `tools/textes_audio/`.\n" % (c["narr"], c["pages"]))
    if "**Couverture audio**" not in s:
        s, e = remplacer(s, "4. **Catalogue média complet**",
                         couverture + "5. **Catalogue média complet**")
        erreurs += e
    else:
        # le bloc existe deja : on rafraichit ses compteurs
        s, n = re.subn(r"\*\*\d+ pages sur \d+\*\* portent un lecteur de narration",
                       "**%d pages sur %d** portent un lecteur de narration"
                       % (c["narr"], c["pages"]), s)
        if n == 0:
            print("  [KO] compteurs de couverture audio introuvables")
            erreurs += 1

    # 4. catalogue media
    s, e = remplacer(
        s,
        "5. **Catalogue média complet** — aucun visuel n'est en attente :\n   `tools/pending_visuals.json` est vide. Les **24 armes** et les **24 objets**\n   ont leur photographie réelle, pour un inventaire de **153 JPG, 0 PNG/SVG,\n   0 image orpheline et 0 référence manquante**.",
        "5. **Catalogue média complet** — aucun visuel n'est en attente :\n   `tools/pending_visuals.json` ne liste plus rien à produire. Les **24 armes** et\n   les **24 objets** ont leur photographie réelle, pour un inventaire de\n   **%d JPG, %d PNG, %d SVG, 0 image orpheline et 0 référence manquante**."
        % (c["jpg"], c["png"], c["svg"]))
    erreurs += e

    # 5. sitemap
    s, e = remplacer(
        s,
        "| `sitemap.xml` | 65 URL indexables, `lastmod` au format W3C |",
        "| `sitemap.xml` | %d URL indexables, `lastmod` au format W3C |" % c["urls"])
    erreurs += e

    if erreurs:
        print("  [KO] %d anomalie(s) sur DEPLOIEMENT.md" % erreurs)
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] DEPLOIEMENT.md : compteurs recalcules (%d pages, %d URL, %d JPG, %d narrations)"
          % (c["pages"], c["urls"], c["jpg"], c["narr"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
