#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - vague G : outils web de calcul, et un leurre GitHub documente.

Recherche du 18/11/2026 sur GitHub, Reddit et les guides tiers.

1) pages/communaute-ressources.html
   - corrige un fragment anglais laisse dans la carte « Calculateur d'armure »
     (« il faut desormais bringing la durabilite » -> « abaisser ») ;
   - ajoute la carte « Calculateur d'armure avec durabilite » (abi-helper.com),
     un calculateur web qui tient compte de la durabilite restante ;
   - ajoute un appel danger sur le depot « Arena Breakout Ammo & Armor Calc »,
     mis a jour le 16 novembre 2026 : ni code source ni licence, et boutons
     d'installation pointant vers un domaine tiers. Ce depot est signale
     comme piege, jamais recommande ;
   - ajoute les trois entrees de sources correspondantes.

2) pages/equipement-armures.html
   - ajoute le modele communautaire de penetration (Pierce Level, classes,
     durabilite) avec les deux calculateurs web qui l'appliquent, et le rappel
     que l'editeur n'a jamais publie le seuil de durabilite de la Saison 7.

Chaque bloc insere est encadre par un marqueur : relancer le script remplace
le contenu encadre au lieu de le dupliquer.

Idempotent.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGES = RACINE / "pages"


def inserer_balise(s, ancre, bloc):
    """Insere ou remplace un bloc balise juste avant l'ancre donnee."""
    nom = bloc.split("-->")[0].strip()
    marqueur_open = nom
    marqueur_close = nom.replace(":OPEN", ":CLOSE") + "-->"

    i = s.find(marqueur_open)
    if i != -1:
        j = s.find(marqueur_close, i)
        if j == -1:
            print("  [KO] marqueur de fin absent :", marqueur_open)
            return s, 1
        fin = j + len(marqueur_close)
        while s[fin:fin + 3] == "-->":
            fin += 3
        s = s[:i] + bloc + s[fin:]
        return s, 0

    k = s.find(ancre)
    if k == -1:
        print("  [KO] ancre introuvable :", ancre[:70])
        return s, 1
    s = s[:k] + bloc + "\n" + s[k:]
    return s, 0


# --------------------------------------------------------------------------
# communaute-ressources.html
# --------------------------------------------------------------------------

CARTE_CALCULATEUR = """<!--VEILLE-F:OUTIL-ARMOR:OPEN-->
            <div class="tool-card">
              <h4>Calculateur d’armure avec durabilité</h4>
              <span class="tool-tag">abi-helper.com</span>
              <p>Calculateur <strong>web, rien à installer</strong> : il confronte chaque munition au catalogue complet des gilets et des casques, <strong>durabilité courante comprise</strong> — vous réglez les points restants de la plaque et la probabilité de pénétration se recalcule. Il publie aussi son modèle communautaire : Pierce Level = plancher(pénétration ÷ 10), passage quasi certain au-dessus de la classe, 80 à 100 % à classe égale.</p>
              <div class="tool-foot">À croiser avec la page <a href="items-munitions.html" id="lnk-communaute-ressources-179">munitions</a>, qui rappelle la formule : l’outil la fait calculer sur la pièce que vous portez réellement. <a href="https://abi-helper.com/armor-calculator" target="_blank" rel="noopener" id="lnk-communaute-ressources-180">abi-helper.com<span class="sr-only"> (nouvel onglet)</span></a></div>
            </div>
<!--VEILLE-F:OUTIL-ARMOR:CLOSE-->"""

APPEL_LEURRE = """<!--VEILLE-G:GITHUB-LURE:OPEN-->
          <div class="callout callout-danger">
            <h3 class="h4">Le leurre du 16 novembre : un « calculateur d’armure » qui n’est qu’un exécutable</h3>
            <p>Un dépôt nommé <strong>« Arena Breakout Ammo &amp; Armor Calc »</strong> a été mis à jour le <strong>16 novembre 2026</strong>. Il a tout du projet sérieux : un logo, un tableau de fonctions complet — matrice de pénétration, calculateur de TTK, comparaison de munitions, sélection de munitions économiques — et une activité récente qui donne l’impression d’un projet vivant. Trois détails le condamnent.</p>
            <ul>
              <li><strong>Il ne contient aucun code.</strong> Le dépôt ne contient que deux fichiers : un <code>README.md</code> et un logo. Pas de source, pas de licence, rien à auditer.</li>
              <li><strong>Les boutons de téléchargement pointent ailleurs.</strong> « Download for Windows » et « Download for macOS » mènent à un domaine tiers, et non aux pages du dépôt lui-même.</li>
              <li><strong>Le README interdit de modifier le fichier source</strong> — un fichier source qui n’existe pas.</li>
            </ul>
            <p>La conclusion est celle de la section précédente, appliquée à un cas concret : <strong>un calculateur légitime est une page web</strong>. Il n’a rien à installer, donc rien à exécuter sur votre machine. Besoin du même calcul ? <a href="https://abi-helper.com/armor-calculator" target="_blank" rel="noopener" id="lnk-communaute-ressources-181">abi-helper.com<span class="sr-only"> (nouvel onglet)</span></a> et le simulateur balistique d’ABIDB Web font le même travail dans le navigateur. Si un exécutable vous est proposé pour « analyser » le jeu, c’est un leurre : les conséquences sont celles d’un ESP, bannissement de dix ans et confiscation en prime. <span class="src-tag src-communautaire">Communautaire</span> <span class="src-tag src-officiel">Officiel</span></p>
          </div>
<!--VEILLE-G:GITHUB-LURE:CLOSE-->"""

SOURCES_OUTILS = """<!--VEILLE-F:SRC-GITHUB:OPEN-->
            <li><span class="src-name">ABI Armor vs Ammo Calculator</span> — calculateur web, sans installation : confronte chaque munition au catalogue des gilets et des casques en tenant compte de la durabilité restante, et publie son modèle communautaire de pénétration (Pierce Level = plancher(pénétration ÷ 10)). <a href="https://abi-helper.com/armor-calculator" target="_blank" rel="noopener" id="lnk-communaute-ressources-182">abi-helper.com<span class="sr-only"> (nouvel onglet)</span></a></li>
            <li><span class="src-name">Loadout Builder — Season 7</span> — constructeur web : recalcule dégâts, pénétration contre les six classes d’armure, recul, poids et pénalité de vitesse, et compare deux kits côte à côte ; signale explicitement qu’en Saison 7 les gilets de classe V et VI ne percent plus par chance mais seulement une fois la durabilité abaissée, seuil que l’éditeur n’a pas publié. <a href="https://qrts.ru/en/games/arena-breakout-infinite/builder/" target="_blank" rel="noopener" id="lnk-communaute-ressources-183">qrts.ru<span class="sr-only"> (nouvel onglet)</span></a></li>
            <li><span class="src-name">Dépôt « Arena Breakout Ammo &amp; Armor Calc » — à ne pas ouvrir</span> — dépôt mis à jour le 16 novembre 2026 : ni code source ni licence, et boutons d’installation redirigés vers un domaine tiers. Signalé ici pour le documenter, jamais pour le recommander. <a href="https://github.com/SentinelScreenSay/arena-breakout-ammo-armor-calc" target="_blank" rel="noopener" id="lnk-communaute-ressources-184">github.com/SentinelScreenSay<span class="sr-only"> (nouvel onglet)</span></a></li>
<!--VEILLE-F:SRC-GITHUB:CLOSE-->"""


def maj_communaute_ressources():
    chemin = PAGES / "communaute-ressources.html"
    s = chemin.read_text(encoding="utf-8")
    erreurs = 0

    # 1. fragment anglais
    avant = "il faut désormais bringing la durabilité sous un seuil pour percer de façon fiable"
    apres = "il faut désormais abaisser la durabilité sous un seuil pour percer de façon fiable"
    if avant in s:
        s = s.replace(avant, apres)
        print("  [OK] fragment anglais « bringing » corrigé")
    elif apres in s:
        print("  [OK] fragment anglais déjà corrigé")
    else:
        print("  [KO] fragment « bringing » introuvable")
        erreurs += 1

    # 2. carte du calculateur web
    s, e = inserer_balise(
        s,
        '<div class="tool-card">\n              <h4>Optimiseur de Secure Case</h4>',
        CARTE_CALCULATEUR,
    )
    erreurs += e

    # 3. appel sur le leurre
    s, e = inserer_balise(s, "<!--VEILLE-D:GITHUB:CLOSE-->", APPEL_LEURRE)
    erreurs += e

    # 4. sources
    s, e = inserer_balise(
        s,
        '<h3>Non confirmé</h3>\n          <ul class="src-list">',
        SOURCES_OUTILS,
    )
    erreurs += e

    if erreurs:
        print("  [KO] %d anomalie(s) sur communaute-ressources.html" % erreurs)
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] communaute-ressources.html : carte calculateur, appel leurre et 3 sources")
    return 0


# --------------------------------------------------------------------------
# equipement-armures.html
# --------------------------------------------------------------------------

APPEL_PENETRATION = """<!--VEILLE-F:ARMURES-PEN:OPEN-->
          <div class="callout callout-info">
            <h3 class="h4">Le modèle de pénétration, en clair</h3>
            <p>Depuis la Saison 7, les gilets de classe V et VI ne se percent plus par chance de tir : il faut abaisser leur durabilité sous un seuil. Ce seuil, l’éditeur ne l’a pas publié. En revanche, le modèle communautaire est stable et documenté : le <strong>Pierce Level</strong> d’une munition vaut la pénétration divisée par dix, arrondie à l’entier inférieur ; au-dessus de la classe de l’armure, la balle passe à chaque coup ; à classe égale, elle passe dans 80 à 100 % des cas avec des dégâts réduits ; en dessous, la chance s’effondre et il faut viser les zones non protégées.</p>
            <p>Deux calculateurs <strong>web</strong> appliquent ce modèle sur la durabilité réelle de votre pièce, sans rien installer : le calculateur d’armure d’<a href="https://abi-helper.com/armor-calculator" target="_blank" rel="noopener" id="lnk-equipement-armures-138">abi-helper.com<span class="sr-only"> (nouvel onglet)</span></a> et le constructeur de loadout de <a href="https://qrts.ru/en/games/arena-breakout-infinite/builder/" target="_blank" rel="noopener" id="lnk-equipement-armures-139">qrts.ru<span class="sr-only"> (nouvel onglet)</span></a>. Le second affiche volontairement une chance de pénétration à zéro sur un gilet de classe V ou VI neuf, tant que le seuil de durabilité n’est pas atteint : c’est la traduction directe de la règle de la Saison 7. <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
<!--VEILLE-F:ARMURES-PEN:CLOSE-->"""


def maj_equipement_armures():
    chemin = PAGES / "equipement-armures.html"
    s = chemin.read_text(encoding="utf-8")
    s, erreurs = inserer_balise(s, '<h2 id="leadership">4. Le leadership T5 et T6, pièce par pièce</h2>', APPEL_PENETRATION)
    if erreurs:
        print("  [KO] anomalie sur equipement-armures.html")
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] equipement-armures.html : modèle de pénétration inséré")
    return 0


def main():
    ecarts = maj_communaute_ressources() + maj_equipement_armures()
    if ecarts:
        print("\n  %d anomalie(s)" % ecarts)
        return 1
    print("\n  vague G appliquee")
    return 0


if __name__ == "__main__":
    sys.exit(main())
