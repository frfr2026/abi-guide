#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichit les pages d'armes courtes avec les statistiques officielles
recensees dans js/data-weapons-wiki.json (source de reference du wiki).

Chaque page de famille gagne :
  1. un tableau de stats officielles (cadence, ergonomie, portee, recul,
     modes de tir) pour toutes les armes de la famille documentees ;
  2. un encadre de lecture : ce que chaque chiffre change en jeu.

Le tableau est genere a partir du JSON, jamais saisi a la main : les chiffres
restent alignes sur la source. Les textes sont rediges en francais accentue.

Idempotent : le bloc n'est insere qu'une fois.
"""
import json
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")
WIKI = pathlib.Path("js/data-weapons-wiki.json")

# page -> (categories wiki, ancre h2, titre du bloc, lecture)
JOBS = [
    (
        "armes-lmg.html",
        ["Light Machine Guns", "LMG", "Light Machine Gun"],
        "regles",
        "Fusils de mitigation lourde : la cadence comme argument",
        "La mitigation lourde ne se joue pas sur la cadence, mais sur la tenue du tir. "
        "Le RPK16 est la seule arme de cette famille dans le catalogue documente : "
        "750 coups par minute en 5.45x39, avec une portee de 53 metres. Son recul "
        "vertical de 73 est le point faible : à 53 mètres de distance utile, chaque "
        "erreur de compensation se paie. L'arme est concu pour tenir une ligne de tir "
        "et non pour courir avec. C'est un choix de slot secondaire : elle prend la "
        "place que le fusil d'assaut ne peut pas prendre, celle de l'arme qui reste "
        "levee pendant que le reste de l'équipe avance.",
    ),
    (
        "armes-shotgun.html",
        ["Shotguns"],
        "regles",
        "Fusils a pompe : la portee reelle, c'est dix metres",
        "La donnee la plus utile d'un fusil a pompe est sa portee : dix a quatorze "
        "metres selon le modèle. Au-dela, la dispersion des gerbes rend le tir non "
        "fiable. Ce qui distingue les cinq armes de la famille, ce n'est pas la "
        "puissance, c'est le mode de tir. Le M870 et le MP-133 sont manuels, avec 70 "
        "et 60 coups par minute : un tir, une recharge, un temps mort long ou une "
        "cartouche rechangee. Le S12K et l'USAS12 sont semi-automatiques et montent a "
        "200 et 275 coups par minute. Le SPR310 est le plus rapide des trois a 300 coups "
        "par minute, avec la plus faible portee de la famille à dix mètres. La "
        "consequence pratique : en pièce fermée, un fusil semi-automatique gagne le "
        "duel. En extérieur, même le plus rapide ne tient pas la distance.",
    ),
    (
        "armes-smg.html",
        ["Submachine Guns", "SMG"],
        "regles",
        "Pistolets-mitraillettes : l'ergonomie comme vrai critere",
        "Sur quinze pistolets-mitraillettes documentes, la cadence ne distingue presque "
        "rien : de 450 à 1 100 coups par minute, l'ecart ne dit pas grand-chose. Ce qui "
        "distingue reellement une arme de cette famille, c'est l'ergonomie et la "
        "portee. Le MPX detient le record de la famille avec 81 points d'ergonomie : "
        "c'est l'arme la plus maniable du catalogue, et elle se pilote presque sans y "
        "penser. Le Vector 9 suit avec 74 points. En face, le P90 combine 1 000 coups "
        "par minute et une portee de 36 metres, la meilleure portee de la famille. La "
        "Vector 45 fait 1 100 coups par minute mais tombe à 25 mètres. La règle à "
        "retenir : au-delà de trente mètres, une arme de cette famille cesse d'etre la "
        "bonne reponse, quelle que soit sa cadence.",
    ),
    (
        "armes-sniper.html",
        ["Sniper", "Sniper Rifles", "Marksman Rifles"],
        "regles",
        "Fusils de precision : ce que la cadence ne dit pas",
        "Un fusil de precision se juge sur trois axes, et le premier n'est pas la "
        "cadence. La portee utile : le M24 atteint 120 metres, le SJ16 125 mètres, le "
        "Mosin-Nagant 100. La cadence : 26 à 30 coups par minute pour les trois a "
        "verrou. Et l'ergonomie : c'est la que le Mosin-Nagant se distingue, avec 22 "
        "points seulement, contre 39 pour le M24 et 32 pour le SJ16. Traduction : le "
        "Mosin est l'arme la moins maniable de la famille, la plus longue à relever "
        "après chaque tir. Le M24 est l'equilibre : le plus maniable des trois, avec "
        "une portee superieure a cent vingt metres. Le SJ16 va le plus loin, au prix "
        "de l'ergonomie. Pour la precision, la cadence ne compte presque pas : ce qui "
        "compte est le temps entre le declenchement et la capacite a tenir sa "
        "respiration.",
    ),
    (
        "armes-dmr.html",
        ["Marksman Rifles"],
        "regles",
        "Fusils de marqueur : le pont entre le fusil et le sniper",
        "Un DMR occupe l'espace entre le fusil d'assaut et le fusil de precision, et "
        "sa caracteristique distinctive est la cadence semi-automatique : de 225 a 850 "
        "coups par minute. Le M110 se distingue avec 80 metres de portee et 300 coups "
        "par minute, ce qui en fait le choix naturel quand on veut un second tir "
        "sans bouger de son angle. Le MK14 monte a 700 coups par minute mais descend a "
        "55 metres. Les deux vers l'extremite opposee : le VSS, avec 850 coups par "
        "minute mais seulement 26 metres de portee, est un DMR de proximite ; le SVDS, "
        "avec 225 coups par minute et 83 metres, est un DMR de tir semi-selectif. A 225 "
        "coups par minute, le SVDS ne permet pas de suivre une cible en deplacement : "
        "chaque tir est un engagement distinct. L'U191 fait 750 coups par minute avec "
        "64 metres de portee, mais son ergonomie de 46 en fait le plus lourd a manier "
        "de la famille.",
    ),
]


def charger():
    data = json.loads(WIKI.read_text(encoding="utf-8"))
    return data["weapons"] if isinstance(data, dict) else data


def bloc(titre, lecture, armes):
    lignes = []
    for a in armes:
        st = a.get("stats", {})
        modes = " / ".join(a.get("modes", []))
        lignes.append(
            "<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td>"
            "<td>%s</td><td>%s</td><td>%s</td></tr>"
            % (
                a.get("nomComplet") or a.get("name"),
                a.get("caliber", "—"),
                st.get("cadence", "—"),
                st.get("ergonomie", "—"),
                st.get("portee", "—"),
                st.get("reculVertical", "—"),
                modes,
            )
        )
    return """
          <div class="callout callout-info">
            <h3 class="h4">%s</h3>
            <p>%s</p>
          </div>

          <div class="table-wrap">
            <table class="data-table">
              <caption>%s — statistiques relevées sur la source de référence du wiki</caption>
              <thead><tr><th scope="col">Arme</th><th scope="col">Calibre</th>
              <th scope="col">Cadence</th><th scope="col">Ergonomie</th>
              <th scope="col">Portée (m)</th><th scope="col">Recul vert.</th>
              <th scope="col">Modes de tir</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>
""" % (titre, lecture, titre, "\n".join(lignes))


def main():
    armes_all = charger()
    total = 0
    for page, cats, ancre, titre, lecture in JOBS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT :", page)
            continue
        s = f.read_text(encoding="utf-8")
        if "statistiques relevées sur la source de référence du wiki" in s:
            print("  deja enrichi :", page)
            continue
        armes = [a for a in armes_all if a.get("categorieWiki") in cats]
        if not armes:
            print("  aucune arme pour :", page)
            continue
        armes.sort(key=lambda a: -(a.get("stats", {}).get("portee") or 0))
        b = bloc(titre, lecture, armes)
        m = re.search(r'<h2[^>]*id="%s"[^>]*>' % re.escape(ancre), s)
        if not m:
            print("  ANCRE INTROUVABLE :", page, ancre)
            continue
        s = s[: m.start()] + b.strip() + "\n\n" + s[m.start():]
        f.write_text(s, encoding="utf-8")
        total += 1
        print("  enrichi : %-28s %d armes" % (page, len(armes)))
    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
