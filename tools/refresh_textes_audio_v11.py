#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - textes audio V11 : le sondage de mi-saison du 17 novembre 2026.

Quatre textes de narration sont mis a jour (ou crees) pour tenir compte de la
vague H :

  - communaute-patch-notes.txt  (cree : la page n'avait pas de texte source)
  - saison8-attente.txt
  - meta-strategies-s7.txt
  - equipement-tier-list.txt

Controles appliques a chaque texte :
  - longueur <= 1500 caracteres (limite de la synthese vocale par appel) ;
  - accents corrects ;
  - aucun caractere CJK, cyrillique ou arabe ;
  - pas de markdown ni de balise.

Idempotent : le script ecrit le contenu, il ne l'ajoute pas.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
DEST = RACINE / "tools" / "textes_audio"
LIMITE = 1500

TEXTE_PATCH_NOTES = """Les notes officielles de l'éditeur sont la source la plus rentable du jeu, et la plupart des joueurs ne les ouvrent jamais. Elles se lisent sur le fil Steam de l'application, sur le site de MoreFun, et dans l'onglet Actualités du client. Des miroirs comme PatchBot les archivent. La Saison 7 a rebattu l'équilibre : plafonds par mode, classe quatre en Normal et classe cinq en Lockdown, bonus de tir à la tête, mode zombie et Continuous Mastery. Entre deux saisons, l'éditeur livre deux à trois correctifs à chaud par mois. Le dix novembre : la collaboration Dim Dou Duk, l'enquête Kamona Investigation, et douze correctifs. Le dix-sept novembre, il a ouvert un sondage de mi-saison sur les règles d'entrée : il demande aux joueurs s'ils accepteraient de voir le plafond de munitions de Lockdown passer de la classe cinq à la classe quatre, exception pour les calibres de sniper, et si ils accepteraient une valeur d'équipement minimale plus élevée en Forbidden Zone et au Warlord Tournament. C'est une consultation, pas une règle appliquée : tant qu'aucun correctif n'est publié, rien ne change. Enfin, l'avis de bannissement du onze novembre reste la meilleure source chiffrée sur la communauté."""

TEXTE_SAISON8 = """La Saison 8 n'est pas annoncée. C'est le fait le plus important à savoir, et il faut le dire plutôt que de combler le vide par des rumeurs. L'éditeur n'a publié ni nom de saison, ni date, ni teaser, ni compte à rebours. Le fil Steam officiel ne mentionne aucune nouvelle saison, et le Live Update du dix novembre n'en dit rien non plus. Ce qui existe, ce sont des estimations. La cadence des trois dernières saisons est de soixante-dix-huit à quatre-vingt-neuf jours. La Saison 7 ayant commencé le seize septembre, la fenêtre la plus probable se situe entre le trois et le seize décembre. Deux facteurs font pencher vers la mi-décembre : les événements de la Saison 7 courent jusqu'au sept décembre, et l'éditeur ne publie que huit jours d'avance en moyenne. Mais il y a un risque réel de report. La Saison 3 a débordé sur les fêtes et la Saison 4 n'a commencé que le huit janvier. Si ce scénario se répète, la Saison 8 arrive en janvier. Un signal a néanmoins été ajouté : le dix-sept novembre, l'éditeur a ouvert un sondage de mi-saison sur les règles d'entrée, où il demande l'avis des joueurs sur une baisse du plafond de munitions en Lockdown. Ce n'est pas une règle, mais un éditeur qui consulte sur ses plafonds prépare une révision. En attendant l'annonce, la seule préparation rationnelle est d'optimiser son kit pour la fin de la saison sept, de liquider le surplus, et de conserver des munitions de classe trois et quatre, valides quelle que soit la saison."""

TEXTE_META = """Les stratégies de la saison sept tiennent en une phrase : la maîtrise du jeu passe avant l'équipement. Un joueur de la communauté l'a formulé ainsi : la précision d'abord, la prudence ensuite. La survie de la session reste le véritable intérêt du jeu. Les délais se sont allongés, ce qui rend chaque confrontation plus risquée. La méthode la plus rentable pour qui ne vise pas le haut du classement s'apprend en une phrase : entrez léger, restez discret, et récupérez ce que le terrain abandonne. Selon le mode, le seuil de butin change : cinq mille Koen par case en Normal, dix mille en Lockdown, davantage en Forbidden. Une session Normal bien menée rapporte vingt à trente mille Koen. Les sorties conditionnelles s'ouvrent vers la dixième minute. Chaque bruit est une information que vous offrez, le silence est un multiplicateur de butin. Et le poids est un ennemi : un équipement de neuf virgule huit kilos et un sac de quarante-cinq litres transforment vos douze minutes de course en quatre. Enfin, l'erreur la plus répandue est la peur de l'équipement : vous ne serez jamais prêts, vous le deviendrez au fil de l'expérience. Une précision avant de conclure : le dix-sept novembre, l'éditeur a interrogé les joueurs sur une possible baisse du plafond de munitions en Lockdown, de la classe cinq vers la classe quatre. Ce n'est qu'une consultation. N'achetez donc pas de munitions de classe cinq en gros, gardez vos kits modulaires, et traitez la classe quatre comme la valeur sûre."""

TEXTE_TIER_LIST = """Le classement de l'équipement de la saison sept repose sur une méthode avant de reposer sur des chiffres. Les sources sont croisées : les notes officielles pour les plafonds par mode et le bonus de tir à la tête, le subreddit pour les retours de milliers de raids, une base de données versionnée pour la durabilité et les zones réelles, et les créateurs de contenu pour les tests balistiques en vidéo. Un principe de lecture avant tout : le palier d'un gilet se lit dans la densité de la protection, pas dans son prix. Les découvertes de la saison sont nettes. Le casque sous le palier quatre n'existe plus : c'est devenu un accessoire de mode, et les tirs à la tête sont trop payants pour qu'on s'en passe. Les paliers quatre sont devenus la norme en mode Normal, et tout ce qui est au-dessus y est du gaspillage. Une réserve toutefois : la ligne Lockdown en palier cinq reste la règle en vigueur, mais l'éditeur a ouvert le dix-sept novembre un sondage de mi-saison qui pourrait en abaisser le plafond des munitions. Tant qu'aucun correctif n'est publié, votre build palier cinq en Lockdown est légal. La règle de décision, enfin : mesurez vos morts réelles sur dix raids, et non pas les points que vous avez en jeu. C'est cette mesure, et elle seule, qui dit si vous devez monter d'un palier."""


def ecrire(nom, texte):
    chemin = DEST / (nom + ".txt")
    erreurs = 0
    if len(texte) > LIMITE:
        print("  [KO] %s : %d caracteres (limite %d)" % (nom, len(texte), LIMITE))
        erreurs += 1
    suspects = sorted({c for c in texte if ord(c) > 0x24F and c not in "×—–’‘“”«»…€•·"})
    if suspects:
        print("  [KO] %s : caracteres suspects %s" % (nom, suspects))
        erreurs += 1
    if re.search(r"[<>*#\[\]]", texte):
        print("  [KO] %s : marqueur de markup detecte" % nom)
        erreurs += 1
    if erreurs:
        return erreurs
    chemin.write_text(texte, encoding="utf-8")
    print("  [OK] %-28s %4d caracteres" % (nom + ".txt", len(texte)))
    return 0


def main():
    ecarts = 0
    ecarts += ecrire("communaute-patch-notes", TEXTE_PATCH_NOTES)
    ecarts += ecrire("saison8-attente", TEXTE_SAISON8)
    ecarts += ecrire("meta-strategies-s7", TEXTE_META)
    ecarts += ecrire("equipement-tier-list", TEXTE_TIER_LIST)
    if ecarts:
        print("\n  %d anomalie(s)" % ecarts)
        return 1
    print("\n  textes V11 ecrits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
