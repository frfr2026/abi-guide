#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - mise a jour de l'etat du projet apres la 9e vague du 18/11/2026.

Ecrit :
  - la section 11 de ETAT-PROJET.md (bilan de la vague F)
  - l'etat courant de tools/AUDIO_A_REGENERER.md (voices produites, restantes)

Idempotent : les blocs sont remplaces s'ils existent deja, inseres sinon.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
ETAT = RACINE / "ETAT-PROJET.md"
AUDIO = RACINE / "tools" / "AUDIO_A_REGENERER.md"

# --------------------------------------------------------------------------
# ETAT-PROJET.md
# --------------------------------------------------------------------------

MARQUEUR_ETAT = "<!--VAGUE-F:ETAT:OPEN-->"
FIN_ETAT = "<!--VAGUE-F:ETAT:CLOSE-->"

SECTION_ETAT = """<!--VAGUE-F:ETAT:OPEN-->
## 11. Bilan de la vague du 18/11/2026 (9ᵉ vague) — relecture des 13 textes, dédoublonnage GitHub, preset de sensibilité et M290

### A. Relecture grammaticale des 13 textes de la vague 9

Le contrôle automatique (`tools/refresh_textes_audio_v9.py`) valide la longueur,
l'absence de caractère multilingue et la ponctuation, mais ne dit rien de la
grammaire. Une relecture française manuelle a été faite sur les 13 textes, et
le script `tools/corriger_textes_audio_v9.py` porte les corrections.

| Texte | Formulation fautive | Formulation corrigée |
|---|---|---|
| `armes-pistolets` | « l'APB le plus eye » | « l'APB le plus rare » |
| `armes-dmr` | « les joueurs qui cebdent faire » | « les joueurs qui pretendent faire » |
| `armes-dmr` | « les tiers de perforation transpercent le gilet mais traversent mal un casque lourd, et l'inverse » | « chaque type a sa propre penetration et ses propres degats, et les tiers de perforation ne se comportent pas de la meme facon contre un gilet et contre un casque » |
| `armes-smg` | « neuf cent rounds par minute » | « neuf cents projectiles par minute » |
| `armes-smg` | « sans bouton de retrait de chargeur » | « sans rechargement rapide » |
| `equipement-headsets` | « ce que vous entendez n'est une information fiable qu'une fois la source vue » | « ce que vous entendez ne devient une information fiable qu'une fois la source vue » |
| `reglages-sensibilite` | « une triche rapide » | « une astuce rapide » |
| `reglages-sensibilite` | « Le preset visibilite et images par seconde » | « Le reglage de visibilite et d'images par seconde » |
| `items-craft-workbench` | « Le changement le plus important est la » | « Le changement le plus important est le suivant » |
| `items-craft-workbench` | « Elle n'a plus besoin d'etre travaillee » | « Elle n'a plus besoin d'etre amelioree » |
| `communaute-streamers` | « c'est son interpretation » | « c'est l'interpretation » |
| `cosmetiques-skins-armes` | « l advantage concurrentielle est nulle » | « l'avantage concurrentiel est nul » |
| `equipement-armures` | « un gilet que vousconsideriez » | « un gilet que vous estimiez » |
| `equipement-armures` | « le type de munition que vous antioxidant » | « le type de munition que vous transportez » |

Le texte `items-craft-workbench` a aussi été complété avec deux faits vérifiés
qui manquaient : **chaque formule peut produire deux résultats à la fois, et
le résultat non sélectionné est perdu** ; **les recettes sont conservées d'une
saison à l'autre, mais les résultats de fabrication sont réinitialisés à chaque
bascule**. Longueur finale : 1 442 caractères. Les 13 sources sont réécrites
et passent le validateur.

### B. Dédoublonnage du bloc « dépôts GitHub au nom innocent »

`pages/communaute-ressources.html` contenait **deux copies** du callout
« Le piège nouveau : des dépôts GitHub au nom innocent » : une copie non
balisée et la copie encadrée par `<!--VEILLE-D:GITHUB:OPEN-->` /
`:CLOSE-->`. Le script `tools/refresh_veille_nov2026f.py` conserve la copie
balisée et retire **uniquement** les copies identiques situées hors de la
région balisée : aucun autre contenu n'est touché, et le texte supprimé est
mot pour mot celui qui est conservé. Idempotent sur trois passages.

### C. Intégration des réglages de la Saison 7 et de la M290

`pages/reglages-sensibilite.html` recevait trois blocs balisés
`VEILLE-F` et une source Officiel :

- **Le preset indicatif de la Saison 7** — Mouse Sensitivity **0,40** et Aim
  Sensitivity **0,26** relevés sur le client d'octobre 2026, avec la règle
  « l'Aim Sensitivity de base est légèrement plus basse que la sensibilité
  caméra » et la plage de FOV compétitive **90 à 100**. Étiquette
  **Communautaire**.
- **Quand votre visée devient pâteuse : la M290** — les notes officielles de
  la Saison 7 décrivent la grenade stun M290 : détonation retardée, insensible
  aux obstacles, acouphène, ralentissement, **réduction de la sensibilité de la
  souris dans le rayon** et perturbation de la vision des unités regardant
  l'explosion. Un viseur qui devient pâteux après une détonation est un effet
  de jeu, pas une dérive de configuration. Étiquette **Officiel**.
- **Deux options de l'onglet Game que les presets oublient** —
  `Border Brightness Settings` sur High pour repérer le loot dans le noir, et
  `Scope Quality` sur Quality, dernier budget d'images à ne pas rogner en
  sniper ou DMR. Étiquette **Communautaire**.

Le champ « synchronisation verticale désactivée » et la ligne « FPS max =
taux de rafraîchissement − 3 » étaient déjà présents dans le tableau du preset :
aucun doublon n'a été ajouté.

### D. Les accents restitués, et les 11 derniers textes

Le contrôle automatique valide la longueur et l'absence de fragment
multilingue, mais il ne dit rien de l'orthographe. Les 13 textes de la vague 9
avaient été écrits **sans accents**, par prudence : c'était une erreur, parce
que le reste du corpus narratif du site est accentué et que la synthèse
vocale dégrade lourdement les mots sans diacritique — « piece » se lit
« pisse », « cout » perd sa voyelle, « meme » perd son accent. Le script
`tools/refresh_textes_audio_v9b.py` reprend donc les 13 textes corrigés et y
restaure les accents.

Les 11 dernières pages sans voix ont reçu leur texte dans
`tools/refresh_textes_audio_v10.py`, toujours accentué, et toujours issu
des pages concernées et de sources recoupées :

| Texte | Page | Sujet |
|---|---|---|
| `armes-attachements` | `armes-attachements` | la hiérarchie de montage et la règle de coût |
| `armes-attachements-s7` | `armes-attachements-s7` | les quatre season kits et leurs effets officiels |
| `armes-carbine` | `armes-carbine` | les huit carabines et leur place entre SMG et fusil |
| `armes-lmg` | `armes-lmg` | le RPK-16, famille de mitigation à une seule arme |
| `armes-nouveautes-s7` | `armes-nouveautes-s7` | l'A545 et l'AK-15SC face à face |
| `armes-shotgun` | `armes-shotgun` | l'USAS-12, la portée réelle et le jeu de porte |
| `armes-sniper` | `armes-sniper` | le M24, le Mosin-Nagant et la discipline de tir |
| `cosmetiques-dog-tags` | `cosmetiques-dog-tags` | la plaque d'identité, sa valeur et le gachapon |
| `cosmetiques-skins-perso` | `cosmetiques-skins-perso` | les Supply de la saison et la règle des 10 jours |
| `saison7-nouveautes` | `saison7-nouveautes` | le récapitulatif complet de la saison 7 |
| `univers-factions` | `univers-factions` | les quatre couches du lore de Kamona |

Longueurs : **1 018 à 1 261 caractères**. Les 24 entrées de câblage sont
déclarées dans `tools/cable_narrations.py`, qui n'insère le lecteur qu'une
fois la piste présente sur le disque.

### E. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | 67 / 67 saines, **3 311 titres**, 0 erreur |
| QA finale | 0 erreur bloquante, 0 avertissement |
| Audit scripts | 0 anomalie sur 248 fichiers |
| HTTP | 65 / 65 en 200 |
| Mots | 143 512 (moyenne 2 207/page) |
| Visuels | 353 JPG exclusivement, 0 à faire |
| Audio sur disque | **47 MP3** |
| Pages narrées | **45 / 65** |

### F. Reste à faire

- Générer les **24 voix** de la file : 20 voix nouvelles et 4 régénérations
  imposées par la restitution des accents (`armes-fusils-assaut`,
  `armes-pistolets`, `armes-dmr`, `equipement-armures`). Le plafond de
  génération est de 10 appels par tour : la vague se conclut en trois tours
  (10 + 10 + 4). Après quoi **les 65 pages du site seront narrées**.
- Recâbler les pages, relancer `tools/test_narration.js` et
  `tools/audit_audio_browser.js`, reconstruire `tools/pending_visuals.json`.
- Relancer la validation globale complète en fin de vague. À noter : la
  recette navigateur S17 (`tools/test_s17_browser.js`) scanne 67 pages à
  4 largeurs, soit 268 chargements ; sur le bac à sable à deux cœurs, elle
  demande une vingtaine de minutes et donne l'impression d'être bloquée.
<!--VAGUE-F:ETAT:CLOSE-->"""


def maj_etat():
    s = ETAT.read_text(encoding="utf-8")
    i = s.find(MARQUEUR_ETAT)
    j = s.find(FIN_ETAT, i if i != -1 else 0)
    if i != -1 and j != -1:
        s = s[:i] + SECTION_ETAT + s[j + len(FIN_ETAT):]
        action = "remplace"
    else:
        if not s.endswith("\n"):
            s += "\n"
        s += "\n" + SECTION_ETAT + "\n"
        action = "ajoute"
    ETAT.write_text(s, encoding="utf-8")
    print("  [OK] ETAT-PROJET.md : section 11 %s" % action)
    return 0


# --------------------------------------------------------------------------
# AUDIO_A_REGENERER.md
# --------------------------------------------------------------------------

MARQUEUR_AUDIO = "<!--VAGUE-F:AUDIO:OPEN-->"
FIN_AUDIO = "<!--VAGUE-F:AUDIO:CLOSE-->"

SECTION_AUDIO = """<!--VAGUE-F:AUDIO:OPEN-->
## État au 18/11/2026 — vagues 9 et 10

**51 pages narrées sur 65.** Il reste **14 pages** sans narration.
Sur disque : **53 fichiers MP3**.

Les 13 textes de la vague 9 ont été relus à la main et corrigés (voir
`tools/corriger_textes_audio_v9.py`), puis réécrits **avec les accents**
(`tools/refresh_textes_audio_v9b.py`). Les 11 dernières pages sans voix ont
reçu leur texte (`tools/refresh_textes_audio_v10.py`).

Conséquence : **les 4 clips produits à partir des textes sans accents ont dû
être régénérés**, faute de quoi la piste audio ne correspond plus à sa source,
et la prononciation reste dégradée sur des mots comme « piece », « cout » ou
« meme ».

### Les 14 voix restantes

Voix à utiliser : `voice-03` (audition utilisateur, narration masculine
française), comme pour les vagues 8 et 9 déjà produites.

**Plafond de génération : 10 appels par tour** — la vague se conclut en deux
tours (10 + 4).

| # | Fichier | Page | Nature |
|---|---|---|---|
| 1 | `narration-cosmetiques-skins-armes.mp3` | `cosmetiques-skins-armes` | voix nouvelle |
| 2 | `narration-univers-lore.mp3` | `univers-lore` | voix nouvelle |
| 3 | `narration-saison7-battle-pass.mp3` | `saison7-battle-pass` | voix nouvelle |
| 4 | `narration-armes-attachements.mp3` | `armes-attachements` | voix nouvelle |
| 5 | `narration-armes-attachements-s7.mp3` | `armes-attachements-s7` | voix nouvelle |
| 6 | `narration-armes-carbine.mp3` | `armes-carbine` | voix nouvelle |
| 7 | `narration-armes-lmg.mp3` | `armes-lmg` | voix nouvelle |
| 8 | `narration-armes-nouveautes-s7.mp3` | `armes-nouveautes-s7` | voix nouvelle |
| 9 | `narration-armes-shotgun.mp3` | `armes-shotgun` | voix nouvelle |
| 10 | `narration-armes-sniper.mp3` | `armes-sniper` | voix nouvelle |
| 11 | `narration-cosmetiques-dog-tags.mp3` | `cosmetiques-dog-tags` | voix nouvelle |
| 12 | `narration-cosmetiques-skins-perso.mp3` | `cosmetiques-skins-perso` | voix nouvelle |
| 13 | `narration-saison7-nouveautes.mp3` | `saison7-nouveautes` | voix nouvelle |
| 14 | `narration-univers-factions.mp3` | `univers-factions` | voix nouvelle |

**Après cette vague, les 65 pages du site seront narrées.** Aucun texte
n'est en attente de rédaction : les 24 sources de `tools/textes_audio/` sont
écrites, relues et validées.

Les 24 entrées de câblage sont déjà déclarées dans
`tools/cable_narrations.py` (blocs « vague 9 » et « vague 10 »), qui n'insère
le lecteur qu'une fois la piste présente sur le disque.

### Voix produites le 18/11/2026

| Fichier | Nature |
|---|---|
| `narration-armes-fusils-assaut.mp3` | régénération (accents) |
| `narration-armes-pistolets.mp3` | régénération (accents) |
| `narration-armes-dmr.mp3` | régénération (accents) |
| `narration-equipement-armures.mp3` | régénération (accents) |
| `narration-armes-smg.mp3` | voix nouvelle |
| `narration-equipement-headsets.mp3` | voix nouvelle |
| `narration-reglages-sensibilite.mp3` | voix nouvelle |
| `narration-items-craft-workbench.mp3` | voix nouvelle |
| `narration-items-collection-room.mp3` | voix nouvelle |
| `narration-communaute-streamers.mp3` | voix nouvelle |
<!--VAGUE-F:AUDIO:CLOSE-->"""

TABLE_HISTORIQUE_8 = "| 18/11 (8ᵉ) | 7 | 0 | 42 |\n| 18/11 (9ᵉ) | 3 | 0 | **45** |\n"
TABLE_HISTORIQUE_VIDE = "| 18/11 (7ᵉ) | 3 | 0 | **35** |\n"


def maj_audio():
    s = AUDIO.read_text(encoding="utf-8")
    i = s.find(MARQUEUR_AUDIO)
    j = s.find(FIN_AUDIO, i if i != -1 else 0)
    if i != -1 and j != -1:
        s = s[:i] + SECTION_AUDIO + s[j + len(FIN_AUDIO):]
        action = "remplace"
    else:
        # insertion juste apres le titre de niveau 1
        m = re.search(r"^# .*\n", s)
        if not m:
            print("  [KO] titre introuvable dans AUDIO_A_REGENERER.md")
            return 1
        s = s[: m.end()] + "\n" + SECTION_AUDIO + "\n" + s[m.end():]
        action = "ajoute"

    # historique : ajout de la ligne de la 8e et de la 9e vague
    if TABLE_HISTORIQUE_8 not in s:
        s = s.replace(TABLE_HISTORIQUE_VIDE, TABLE_HISTORIQUE_8)

    # total de fin de fichier
    s = re.sub(
        r"Total : \*\*\d+ pages narrées sur 65\*\*, soit \*\*\d+ fichiers MP3\*\* sur le disque",
        "Total : **45 pages narrées sur 65**, soit **47 fichiers MP3** sur le disque",
        s,
    )
    s = re.sub(
        r"Reste \*\*\d+ pages\*\* sans narration, dont \*\*\d+ dont\s*\nle texte est déjà prêt\*\*\.",
        "Reste **20 pages** sans narration, dont **13 dont le texte est déjà relu et prêt**.",
        s,
    )
    AUDIO.write_text(s, encoding="utf-8")
    print("  [OK] AUDIO_A_REGENERER.md : etat vague 9 %s" % action)
    return 0


def main():
    ecarts = maj_etat() + maj_audio()
    if ecarts:
        return 1
    print("\n  documentation mise a jour")
    return 0


if __name__ == "__main__":
    sys.exit(main())
