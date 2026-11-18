#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - etat du projet, vague G (18/11/2026, apres-midi).

Ajoute la section 12 de ETAT-PROJET.md : ce que la recherche fraiche a
confirme, les deux outils web de calcul ajoutes, le leurre GitHub documente,
le fragment anglais corrige, le modele de penetration, et l'etat des
compteurs.

Idempotent : la section est remplacee si elle existe deja.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
ETAT = RACINE / "ETAT-PROJET.md"

MARQUEUR = "<!--VAGUE-G:ETAT:OPEN-->"
FIN = "<!--VAGUE-G:ETAT:CLOSE-->"

SECTION = """<!--VAGUE-G:ETAT:OPEN-->
## 12. Bilan de la vague du 18/11/2026 (10ᵉ vague) — deux outils web de calcul, un leurre GitHub documenté, 10 voix produites

### A. Ce que la recherche fraîche a confirmé

Une nouvelle passe de recherche (Reddit, YouTube, GitHub, Steam, guides
tiers) a été menée sur les sujets du 18 novembre 2026 : mise à jour du
10 novembre, notes de bannissement du 11 novembre, estimation de la Saison 8,
guide du kit budget, tier lists de la saison, modes zombies.

**Le guide était déjà à jour sur l'essentiel.** Concrètement, ces éléments
étaient déjà présents, et aucune insertion en double n'a été faite :

| Information fraîche | Déjà dans le guide |
|---|---|
| Live Update du 10 novembre 2026 (Dim Dou Duk, Kamona Investigation) | `communaute-patch-notes.html` |
| Notes de bannissement du 11 novembre : 58 662 joueurs compensés, 10 883 bannis | `communaute-patch-notes.html` |
| Estimation de la Saison 8 : semaine du 8 – 14 décembre 2026, report possible en janvier 2027 | `saison8-attente.html` (avec les trois scénarios et leurs probabilités) |
| Best Budget Loadout du 14 novembre 2026 (munition tier 4, plafonds par mode) | `meta-stratégies-s7.html`, `meta-tier-list-globale.html` |
| Guide No Man's Land du 5 octobre 2026 | `map-no-mans-land.html` |
| Tier lists de septembre 2026, technique AN-94 en tir semi-auto simulé | `armes-fusils-assaut.html`, `meta-tier-list-globale.html` |

Deux apports de la recherche ont en revanche été retenus, parce qu'ils
n'étaient pas dans le guide : deux outils web de calcul, et un leurre.

### B. Deux outils web de calcul

- **abi-helper.com — Armor vs Ammo Calculator.** Calculateur entièrement
  client : il confronte chaque munition au catalogue complet des gilets et
  des casques, **durabilité restante comprise**, et publie le modèle
  communautaire qu'il applique — Pierce Level = plancher(pénétration ÷ 10),
  passage quasi certain au-dessus de la classe, 80 à 100 % à classe égale.
  Ajouté dans la section « Les outils communautaires à connaître » de
  `communaute-ressources.html`, avec son entrée de source.
- **qrts.ru — Loadout Builder Season 7.** Constructeur web qui recalcule
  dégâts, pénétration contre les six classes d'armure, recul, poids et
  pénalité de vitesse, et compare deux kits. Il documente explicitement la
  règle de la Saison 7 : les gilets de classe V et VI ne percent plus par
  chance, mais seulement une fois la durabilité abaissée — **seuil que
  l'éditeur n'a jamais publié**. Retenu comme confirmation de la règle, pas
  comme donnée officielle.

### C. Un leurre documenté

Le dépôt **« Arena Breakout Ammo & Armor Calc »**, mis à jour le
**16 novembre 2026**, a tout du projet sérieux : logo, tableau de fonctions
complet, activité récente. Trois détails le condamnent :

1. il ne contient que deux fichiers — un `README.md` et un logo — **sans
   code source ni licence**, donc rien à auditer ;
2. les boutons « Download for Windows » et « Download for macOS » pointent
   vers un **domaine tiers**, et non vers les pages du dépôt ;
3. le README interdit de modifier le fichier source — un fichier source
   qui n'existe pas.

Il est donc documenté dans un appel **danger** de `communaute-ressources.html`,
à côté des leurres déjà signalés, avec la même conclusion : **un calculateur
légitime est une page web**, il n'a rien à installer, donc rien à exécuter sur
la machine. L'entrée de source correspondante est explicitement notée
« à ne pas ouvrir ».

### D. Un fragment anglais corrigé

La carte « Calculateur d'armure » de `communaute-ressources.html` contenait
« il faut désormais **bringing** la durabilité sous un seuil ». Le fragment
anglais a été remplacé par « il faut désormais **abaisser** la durabilité sous
un seuil », et le correctif est porté par le script pour survivre aux
prochaines passes.

### E. Le modèle de pénétration, en clair

`equipement-armures.html` gagne un encadré qui met en langage courant le
modèle communautaire : le Pierce Level d'une munition vaut la pénétration
divisée par dix, arrondie à l'entier inférieur ; au-dessus de la classe de
l'armure la balle passe à chaque coup ; à classe égale elle passe dans 80 à
100 % des cas avec des dégâts réduits ; en dessous, la chance s'effondre et
il faut viser les zones non protégées. La durabilité compte autant que la
classe, et le seuil de la Saison 7 reste **non publié par l'éditeur** — ce
qui est écrit comme tel.

### F. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | 67 / 67 saines, **3 314 titres**, 0 erreur |
| QA finale | 0 erreur bloquante, 0 avertissement |
| Audit scripts | 0 anomalie sur 252 fichiers |
| HTTP | 65 / 65 en 200 |
| Mots | **144 462** (moyenne 2 222/page), 0 page courte |
| Visuels | 353 JPG exclusivement, 0 à faire |
| Audio sur disque | **53 MP3**, 53 / 53 décodés, 0 échec |
| Pages narrées | **51 / 65** — recette narration : 358 tests, 0 échec |

### G. Reste à faire

- Générer les **14 dernières voix** (10 au prochain tour, 4 au suivant), puis
  recâbler, relancer l'audit navigateur et reconstruire
  `tools/pending_visuals.json`.
- Relancer la validation globale complète en fin de vague.
<!--VAGUE-G:ETAT:CLOSE-->"""


def main():
    s = ETAT.read_text(encoding="utf-8")
    i = s.find(MARQUEUR)
    if i != -1:
        j = s.find(FIN, i)
        if j == -1:
            print("  [KO] marqueur de fin absent")
            return 1
        s = s[:i] + SECTION + s[j + len(FIN):]
        action = "remplace"
    else:
        if not s.endswith("\n"):
            s += "\n"
        s += "\n" + SECTION + "\n"
        action = "ajoute"
    ETAT.write_text(s, encoding="utf-8")
    print("  [OK] ETAT-PROJET.md : section 12 %s" % action)
    return 0


if __name__ == "__main__":
    sys.exit(main())
