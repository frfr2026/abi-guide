#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cable 5 nouvelles voix off sur les pages qui n'en avaient pas.

Le balisage est strictement identique a celui des 5 narrations deja en place
(guide-debutant, guide-extraction, map-valley, map-no-mans-land,
armes-tier-list) : un div.audio-narration avec data-track, insere juste avant
le div.audio-player existant dans le pied de page.

Idempotent.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGES = RACINE / "pages"

# (page, fichier mp3, etiquette)
JOBS = [
    ("guide-avance.html", "narration-guide-avance.mp3", "Narration : Guide avance"),
    ("items-medical.html", "narration-items-medical.mp3", "Narration : Items medicaux"),
    ("guide-economie.html", "narration-guide-economie.mp3", "Narration : Guide economie"),
    ("events-calendrier.html", "narration-events-calendrier.mp3", "Narration : Calendrier"),
    ("guide-traders.html", "narration-guide-traders.mp3", "Narration : Marchands"),
    ("map-farm.html", "narration-map-farm.mp3", "Narration : Carte Farm"),
    ("map-airport.html", "narration-map-airport.mp3", "Narration : Carte Airport"),
    ("items-cles.html", "narration-items-cles.mp3", "Narration : Cles et acces"),
    ("guide-craft.html", "narration-guide-craft.mp3", "Narration : Guide craft"),
    ("events-warlord-tournament.html", "narration-events-warlord.mp3", "Narration : Warlord Tournament"),
    ("equipement-armures.html", "narration-equipement-armures.mp3", "Narration : Equipement armures"),
    ("equipement-casques.html", "narration-equipement-casques.mp3", "Narration : Equipement casques"),
    ("communaute-patch-notes.html", "narration-communaute-patch-notes.mp3", "Narration : Patch notes"),
    ("saison7-utopia.html", "narration-saison7-utopia.mp3", "Narration : Saison 7 Utopia"),
    ("map-northridge.html", "narration-map-northridge.mp3", "Narration : Carte Northridge"),
    ("map-armory.html", "narration-map-armory.mp3", "Narration : Carte Armory"),
    ("items-munitions.html", "narration-items-munitions.mp3", "Narration : Munitions"),
    ("saison7-zombie-research.html", "narration-saison7-zombie-research.mp3", "Narration : Zombie Research"),
    ("saison8-attente.html", "narration-saison8-attente.mp3", "Narration : Attente Saison 8"),
    ("guide-progression.html", "narration-guide-progression.mp3", "Narration : Progression"),
    ("items-valeur.html", "narration-items-valeur.mp3", "Narration : Valeur des objets"),
    ("events-supplies-drops.html", "narration-events-supplies-drops.mp3", "Narration : Supply Drops"),
    ("saison7-zombie-infected-zone.html", "narration-saison7-zombie-infected-zone.mp3", "Narration : Zone infectee"),
    ("meta-stratégies-s7.html", "narration-meta-strategies-s7.mp3", "Narration : Strategies Saison 7"),
    ("map-tv-station.html", "narration-map-tv-station.mp3", "Narration : Carte TV Station"),
    ("equipement-tier-list.html", "narration-equipement-tier-list.mp3", "Narration : Tier list equipement"),
    ("saison7-balance-changes.html", "narration-saison7-balance-changes.mp3", "Narration : Balance S7"),
    ("meta-tier-list-globale.html", "narration-meta-tier-list-globale.mp3", "Narration : Tier list globale"),
    ("equipement-sacs.html", "narration-equipement-sacs.mp3", "Narration : Sacs a dos"),
    ("equipement-rigs.html", "narration-equipement-rigs.mp3", "Narration : Rigs"),
    ("items-koen-economy.html", "narration-items-koen-economy.mp3", "Narration : Koen et economie"),
    ("meta-builds-roles.html", "narration-meta-builds-roles.mp3", "Narration : Builds par role"),
    ("saison7-zombie-endless.html", "narration-saison7-zombie-endless.mp3", "Narration : Zombie Endless"),
    ("meta-loadout-optimizer.html", "narration-meta-loadout-optimizer.mp3", "Narration : Loadout Optimizer"),
    ("armes-builds.html", "narration-armes-builds.mp3", "Narration : Builds recommandes"),
    ("univers-dark-zone.html", "narration-univers-dark-zone.mp3", "Narration : Dark Zone"),
    ("communaute-ressources.html", "narration-communaute-ressources.mp3", "Narration : Ressources communautaires"),
    # --- vague 9 : 13 textes rediges le 18/11/2026
    ("armes-fusils-assaut.html", "narration-armes-fusils-assaut.mp3", "Narration : Fusils d'assaut"),
    ("armes-pistolets.html", "narration-armes-pistolets.mp3", "Narration : Pistolets"),
    ("armes-dmr.html", "narration-armes-dmr.mp3", "Narration : DMR"),
    ("armes-smg.html", "narration-armes-smg.mp3", "Narration : Mitraillettes"),
    ("equipement-armures.html", "narration-equipement-armures.mp3", "Narration : Equipement armures"),
    ("equipement-headsets.html", "narration-equipement-headsets.mp3", "Narration : Casques audio"),
    ("reglages-sensibilite.html", "narration-reglages-sensibilite.mp3", "Narration : Reglages et sensibilite"),
    ("items-craft-workbench.html", "narration-items-craft-workbench.mp3", "Narration : Craft et etabli"),
    ("items-collection-room.html", "narration-items-collection-room.mp3", "Narration : Salle de collection"),
    ("communaute-streamers.html", "narration-communaute-streamers.mp3", "Narration : Streamers"),
    ("cosmetiques-skins-armes.html", "narration-cosmetiques-skins-armes.mp3", "Narration : Skins d'armes"),
    ("univers-lore.html", "narration-univers-lore.mp3", "Narration : Lore de Kamona"),
    ("saison7-battle-pass.html", "narration-saison7-battle-pass.mp3", "Narration : Battle Pass S7"),
    # --- vague 10 : 11 textes rediges le 18/11/2026
    ("armes-attachements.html", "narration-armes-attachements.mp3", "Narration : Attachements"),
    ("armes-attachements-s7.html", "narration-armes-attachements-s7.mp3", "Narration : Attachements S7"),
    ("armes-carbine.html", "narration-armes-carbine.mp3", "Narration : Carabines"),
    ("armes-lmg.html", "narration-armes-lmg.mp3", "Narration : LMG"),
    ("armes-nouveautes-s7.html", "narration-armes-nouveautes-s7.mp3", "Narration : Armes S7"),
    ("armes-shotgun.html", "narration-armes-shotgun.mp3", "Narration : Fusils a pompe"),
    ("armes-sniper.html", "narration-armes-sniper.mp3", "Narration : Snipers"),
    ("cosmetiques-dog-tags.html", "narration-cosmetiques-dog-tags.mp3", "Narration : Dog tags"),
    ("cosmetiques-skins-perso.html", "narration-cosmetiques-skins-perso.mp3", "Narration : Skins de personnage"),
    ("saison7-nouveautes.html", "narration-saison7-nouveautes.mp3", "Narration : Nouveautes S7"),
    ("univers-factions.html", "narration-univers-factions.mp3", "Narration : Factions"),
]

BLOC = '''  <div class="audio-narration" data-track="../audio/%s" data-label="%s">
    <button aria-label="Ecouter la narration"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
    <span class="audio-label">Narration</span>
    <span class="audio-bar"><span class="audio-bar-fill"></span></span>
  </div>
'''


def main():
    total = 0
    for page, mp3, label in JOBS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT page :", page)
            continue
        s = f.read_text(encoding="utf-8")
        if mp3 in s:
            print("  deja cable :", page)
            continue
        if not (RACINE / "audio" / mp3).exists():
            print("  piste absente, cable ignore :", mp3)
            continue
        # inserer avant le div.audio-player du pied de page
        m = re.search(r'[ \t]*<div class="audio-player"', s)
        if not m:
            print("  ANCRE INTROUVABLE :", page)
            continue
        bloc = BLOC % (mp3, label)
        s = s[: m.start()] + bloc + s[m.start():]
        f.write_text(s, encoding="utf-8")
        total += 1
        print("  cable : %-26s %s" % (page, mp3))
    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
