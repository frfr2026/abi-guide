#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI NEXUS - mise a jour du bilan de projet (vague du 18/11/2026, apres veille)."""
import pathlib
import re

P = pathlib.Path("ETAT-PROJET.md")
s = P.read_text(encoding="utf-8")

# ---------------------------------------------------------------- 1. compteurs
s = s.replace(
    "| Volume de texte | **141 389 mots** (moyenne 2 175/page) |",
    "| Volume de texte | **142 414 mots** (moyenne 2 190/page) |",
)
s = s.replace(
    "| Médias | **354 JPG** (51,3 Mo) · **0 PNG / SVG / WebP** · **0 fichier illisible** · **0 aplat/placeholder** |",
    "| Médias | **353 JPG** · **0 PNG / SVG / WebP / GIF** · **0 fichier illisible** · **0 aplat/placeholder** |",
)
s = s.replace(
    "| Audios | **31 MP3** — 2 ambiances + **29 voix off** françaises |",
    "| Audios | **34 MP3** — 2 ambiances + **32 voix off** françaises |",
)

# ---------------------------------------------------------------- 2. validation
remplacements = [
    (
        "| Profond (audit_deep.py) | **0 erreur** · 165 avertissements",
        "| Profond (audit_deep.py) | **0 erreur** · 153 avertissements",
    ),
    (
        "| Images rendu navigateur | **281 références · 280 distinctes · 0 doublon · 0 non décodée** |",
        "| Images rendu navigateur | **281 références · 279 distinctes · 1 multi-page · 0 non décodée** |",
    ),
    (
        "| Recette narration | **26/26** (`tools/test_narration.js`) |",
        "| Recette narration | **225/225** (`tools/test_narration.js`, catalogue auto-découvert) |",
    ),
    (
        "| MP3 | **12/12 décodés** — 44,1 kHz stéréo, durées 24,0 s (ambiances) à 60,8 s (narrations), RMS 3 169-5 837 (signal réel, non silencieux) |",
        "| MP3 | **34/34 décodés** (`tools/audit_audio_browser.js`) — 44,1 kHz stéréo, durées 24,0 s (ambiances) à 88,6 s (narrations) |",
    ),
    (
        "| Lecteur de narration | **26/26** — composant non bouclé, lecture réelle, barre de progression, sur **24 pages** |",
        "| Lecteur de narration | **32 pages** — composant non bouclé, lecture réelle, barre de progression |",
    ),
    (
        "| Garde-fou scripts | **0 anomalie sur 225 fichiers** (`tools/check_scripts.py`) |",
        "| Garde-fou scripts | **0 anomalie sur 229 fichiers** (`tools/check_scripts.py`) |",
    ),
]
for a, b in remplacements:
    if a not in s:
        print(f"  [!!] absent : {a[:60]}")
    s = s.replace(a, b)

# ------------------------------------------------- 3. nouvelle section de vague
NOUVELLE = """## 2. Travaux de cette session

### Vague du 18/11/2026 (6ᵉ vague) — 10 visuels, 3 voix off, veille et correction majeure des clés

**1. Dix visuels cinématographiques produits et intégrés.** Tous en **JPEG haute qualité**, entre 1 536×1 024 et
1 672×941, photoréalistes et immersifs : `vis-tierlist`, `vis-roles`, `vis-optimizer` (meta), `vis-research`,
`vis-infected` (zombies), `vis-koen`, `vis-medical` (items), `vis-supplies`, `vis-warlord` (events),
`vis-patch` (communaute). Chaque ancien visuel ciblé a été purgé. **57 visuels cinématographiques** au total.

**2. Trois voix off produites et câblées** : `map-tv-station` (57,48 s), `equipement-tier-list` (56,80 s) et
`saison7-balance-changes` (55,78 s, concaténée depuis 3 blocs). Couverture : **32 pages narrées sur 65**.

**3. Un bug d'appariement corrigé.** `tools/refresh_visuels_cine4.py` recherche les images par **nom de base** :
`img/armes/vis-tierlist.jpg` et `img/meta/vis-tierlist.jpg` partageaient le même nom, si bien que le nouveau
visuel global avait remplacé l'arme-tier-list et laissé l'ancien fichier orphelin. L'ancien visuel a été rattaché
au catalogue puis purgé ; `img/meta/vis-tierlist-cinematique.jpg` sert désormais les **deux** pages concernées.

**4. La veille a révélé une erreur de fond sur la durée de vie des clés.** Les notes de patch officielles de
l'éditeur (*Full Release*, Season 3 : Breach, X / @ArenaBreakoutPC, 15/09/2025) indiquent que la durabilité des
clés produites après la Saison 3 a été **multipliée par trois**. Le guide affichait encore les valeurs
d'avant refonte (10 / 15 / 25) sur ses tableaux Farm, Valley et TV Station — incohérence avec le reste du site,
qui raisonnait déjà sur des clés à 30 points. **21 valeurs ont été corrigées** et la recommandation inversée :
le guide conseillait de dépenser les clés anciennes en Normal, alors que l'éditeur demande explicitement de
les **prioriser en Lockdown et en Forbidden** — ce que confirme l'arithmétique, puisqu'une ancienne clé
consomme un point par ouverture quel que soit le mode et vaut donc 15 ouvertures où qu'elle soit dépensée.
Deux nouveaux encadrés documentent la règle **« ouverture à crédit »** (le dernier point restant ouvre encore
une porte en Forbidden) et le comportement **officiel** des clés universelles.

**5. Trois apports de veille, classés par nature.**

| Apport | Page | Nature |
|---|---|---|
| Top-loading : chargeur à deux étages, munitions hautes en premier | `items-munitions.html` | Communautaire |
| Lobby de bots en Lockdown après six morts consécutives | `meta-stratégies-s7.html` | Communautaire |
| TikTok, X et le format court : une piste, jamais une source | `communaute-ressources.html` | Communautaire + Officielles |

**6. Deux outils de contrôle réparés.** `tools/test_narration.js` ne listait que 6 pages en dur : il découvre
désormais le catalogue depuis le HTML, ce qui porte la recette de 31 à **225 assertions sur 32 pages** et
supprime toute dérive future. `tools/test_s17_browser.js` lançait Chromium sans `--no-sandbox` et échouait
en environment sandboxé : il est repassé à **48/48**.

**7. Le suivi documentaire a été remis à jour** : `tools/pending_visuals.json` reconstruit (353 JPG, 34 MP3,
32 pages narrées), `tools/AUDIO_A_REGENERER.md` réécrit (plus aucun audio en attente, historique complet).

### Validation après la vague

| Audit | Résultat |
|---|---|
| QA global | **0 erreur bloquante · 0 avertissement** |
| Statique / SEO | **65/65** en 200 · **0 erreur** SEO |
| Profond | **0 erreur** · 153 avertissements |
| Scripts | **0 anomalie sur 229 fichiers** |
| Images | **281 références · 0 non décodée** · **0 référence cassée** |
| Audio | **34/34 décodés** |
| Narration | **225/225** sur 32 pages |
| Recettes S15 / S16 / S17 / S18 / catalogue | **58/58 · 51/51 · 48/48 · 141/141 · 8/8** |
| Multilingue | **0 fragment** CJK / hangul / cyrillique |
| Volume | **142 414 mots** · moyenne **2 190/page** · **0 page** sous 1 300 |

"""

if "### Vague du 18/11/2026 (6ᵉ vague)" not in s:
    s = s.replace("## 2. Travaux de cette session\n\n", NOUVELLE, 1)
    print("  nouvelle section ajoutee")

# ------------------------------------------------- 4. section 3.B (audio)
s = s.replace(
    "### B. Audio — **19 pages narrées sur 65**",
    "### B. Audio — **32 pages narrées sur 65**",
)
s = s.replace(
    "Test dédié `tools/test_narration.js` : **26/26**.",
    "Test dédié `tools/test_narration.js` : **225/225** sur 32 pages, catalogue auto-découvert.",
)
s = s.replace(
    "| 18/11 (3ᵉ vague) | `map-northridge`, `map-armory`, `items-munitions`, `saison7-zombie-research`, `saison8-attente` (+ `guide-extraction` et `map-valley` réécrits) | **24** |",
    "| 18/11 (3ᵉ vague) | `map-northridge`, `map-armory`, `items-munitions`, `saison7-zombie-research`, `saison8-attente` (+ `guide-extraction` et `map-valley` réécrits) | 24 |\n"
    "| 18/11 (4ᵉ-5ᵉ vague) | `guide-progression`, `meta-stratégies-s7`, `map-tv-station`, `equipement-tier-list`, `saison7-balance-changes`, `events-supplies-drops`, `meta-builds-roles` | **32** |",
)
s = s.replace(
    "**Reste à faire** : 41 pages sans narration. Le plafond de 10 audios par réponse impose\n5 vagues supplémentaires pour couvrir tout le site.",
    "**Reste à faire** : 33 pages sans narration. Le plafond de 10 audios par réponse impose\n4 vagues supplémentaires pour couvrir tout le site.",
)

P.write_text(s, encoding="utf-8")
print("  ETAT-PROJET.md mis a jour")
