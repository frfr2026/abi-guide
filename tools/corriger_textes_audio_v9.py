#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - relecture grammaticale des textes de narration de la vague 9.

Corrige les formulations fautives relevees lors de la relecture humaine des
13 textes de tools/refresh_textes_audio_v9.py :

  - « l'APB le plus eye »        -> « l'APB le plus rare »
  - « qui cebdent faire »        -> « qui pretendent faire »
  - « que vous antioxidant »     -> « que vous transportez »
  - « si vous le collectes »     -> « si vous le ramassez »
  - « le changement ... est la » -> « ... est le suivant »
  - « vousconsideriez »          -> « vous estimiez »
  - « neuf cent rounds »         -> « neuf cents projectiles »
  - « une triche rapide »        -> « une astuce rapide »
  - « l advantage concurrentielle » -> « l'avantage concurrentiel est nul »
  - « son interpretation »      -> « l'interpretation »

Deux textes sont aussi completes avec des faits deja verifies (tirages de
formules a l'etabli, reinitialisation saisonniere des resultats).

Idempotent : chaque remplacement est ignore s'il est deja applique.
Ne touche qu'a tools/refresh_textes_audio_v9.py.
"""
import pathlib
import sys

CIBLE = pathlib.Path(__file__).resolve().parent / "refresh_textes_audio_v9.py"

REMPLACEMENTS = [
    # --- armes-pistolets
    ("l'APB le plus eye",
     "l'APB le plus rare"),
    # --- armes-dmr
    ("les joueurs qui cebdent faire du tout-terrain",
     "les joueurs qui pretendent faire du tout-terrain"),
    ("La munition est le vrai sujet : les tiers de perforation transpercent le gilet mais traversent mal un casque lourd, et l'inverse.",
     "La munition est le vrai sujet : chaque type a sa propre penetration et ses propres degats, et les tiers de perforation ne se comportent pas de la meme facon contre un gilet et contre un casque."),
    # --- armes-smg
    ("une cadence de neuf cent rounds par minute",
     "une cadence de neuf cents projectiles par minute"),
    ("une mitraillette sans bouton de retrait de chargeur",
     "une mitraillette sans rechargement rapide"),
    # --- equipement-headsets
    ("ce que vous entendez n'est une information fiable qu'une fois la source vue",
     "ce que vous entendez ne devient une information fiable qu'une fois la source vue"),
    # --- reglages-sensibilite
    ("Le preset visibilite et images par seconde arbitre entre lisibilite et fluidite",
     "Le reglage de visibilite et d'images par seconde arbitre entre lisibilite et fluidite"),
    ("un inventaire a une touche, une triche rapide et une commande de permutation",
     "un inventaire a une touche, une astuce rapide et une commande de permutation"),
    # --- items-craft-workbench
    ("Le changement le plus important est la : une formule debloquee arrive desormais a son niveau maximal.",
     "Le changement le plus important est le suivant : une formule debloquee arrive desormais a son niveau maximal."),
    ("Elle n'a plus besoin d'etre travaillee pour atteindre son plafond",
     "Elle n'a plus besoin d'etre amelioree pour atteindre son plafond"),
    ("les plans d'amelioration se trouvent dans les boites a documents, les vetements et les tiroirs, et permettent de debloquer des bonus saisonniers.",
     "les plans d'amelioration se trouvent dans les boites a documents, les vetements et les tiroirs. Chaque formule peut produire deux resultats a la fois, et celui que vous ne selectionnez pas est perdu : les resultats non choisis ne sont pas recuperes. Les recettes, elles, sont conservees d'une saison a l'autre, mais les resultats de fabrication sont reinitialises a chaque bascule de saison."),
    # --- items-craft-workbench : seconde passe (raccourcissement sous la limite de 1 450)
    ("les resultats non choisis ne sont pas recuperes",
     "les resultats non choisis sont perdus definitivement"),
    ("Les recettes, elles, sont conservees d'une saison a l'autre, mais les resultats de fabrication sont reinitialises a chaque bascule de saison.",
     "Les recettes sont conservees d'une saison a l'autre, mais les resultats de fabrication sont reinitialises a chaque bascule."),
    # --- communaute-streamers
    ("ce n'est pas la regle, c'est son interpretation",
     "ce n'est pas la regle, c'est l'interpretation"),
    # --- cosmetiques-skins-armes
    ("l advantage concurrentielle est nulle : deux joueurs",
     "l'avantage concurrentiel est nul : deux joueurs"),
    # --- equipement-armures
    ("un gilet que vousconsideriez comme une garantie",
     "un gilet que vous estimiez comme une garantie"),
    ("le type de munition que vous antioxidant",
     "le type de munition que vous transportez"),
]


def main():
    s = CIBLE.read_text(encoding="utf-8")
    appliques = 0
    deja = 0
    for avant, apres in REMPLACEMENTS:
        if apres in s and avant not in s:
            deja += 1
            continue
        if avant not in s:
            print("  [ABSENT] %r" % avant[:60])
            continue
        s = s.replace(avant, apres)
        appliques += 1
    CIBLE.write_text(s, encoding="utf-8")
    print("  %d remplacement(s) applique(s), %d deja a jour" % (appliques, deja))
    return 0


if __name__ == "__main__":
    sys.exit(main())
