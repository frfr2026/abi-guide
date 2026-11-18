#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichit pages/map-airport.html avec la logique de sorties et de rentabilite
recoltee lors de la veille du 18/11/2026 (guides d'analyse, Reddit,
communautes) — trois sorties petitionnaires n'etaient pas documentees :

- Northern Outpost  : activation 10-20 min + 1 elimination requise
- Parking Lot Helicopter : activation 1 min, tres forte pression PvP
- Central Elevator : extraction conditionnelle liee aux controles de la tour

Et la regle de decision qui manque : la rentabilite se calcule en
Koen par minute, pas en loot total.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/map-airport.html")

BLOC = '''
          <div class="callout callout-info">
            <h3 class="h4">Les sorties d'Airport ne se valent pas : lisez l'activation avant de charger</h3>
            <p>Sur Airport, la différence entre une sortie de 10 minutes et une sortie de 25 minutes
            décide du profit de la journée. Une extraction n'est pas un bouton : c'est un
            <strong>contrat</strong> — un délai d'activation, parfois une condition, et toujours une
            exposition au risque qui augmente avec le temps qui passe.</p>
            <div class="table-wrap">
              <table class="data-table">
                <caption>Les sorties d'Airport, lues comme des engagements</caption>
                <thead><tr><th scope="col">Sortie</th><th scope="col">Activation</th><th scope="col">Condition</th><th scope="col">Ce que ça implique</th></tr></thead>
                <tbody>
                  <tr><td><strong>Drainage Pipe</strong></td><td>0 à 10 min</td><td>Sac à dos interdit</td><td>La sortie de secours. Vous videz votre sac avant de l'utiliser : elle sert à sauver une pockets valuable, pas un run complet.</td></tr>
                  <tr><td><strong>Northern Outpost</strong></td><td>10 à 20 min</td><td>1 élimination</td><td>Transforme un combat contre l'IA en prérequis d'extraction. Il faut tuer quelqu'un — donc s'attendre à unfight, mais seulement au moment où vous partez.</td></tr>
                  <tr><td><strong>Cluster 15 minutes</strong></td><td>15 min</td><td>Minuteur de 20 s</td><td>Le meilleur compromis : une minuterie courte sur plusieurs sorties simultanées, donc toujours une option de repli.</td></tr>
                  <tr><td><strong>Access Bridge</strong></td><td>25 min</td><td>—</td><td>La sortie de fin de raid. Faible densité de joueurs, mais au-delà de 20 minutes la concentration de PvP sur les dernières sorties devient forte : le risque augmente plus vite que la récompense.</td></tr>
                  <tr><td><strong>Parking Lot Helicopter</strong></td><td>1 min</td><td>—</td><td>La plus rapide, et la plus violente. Réservée aux escouades coordonnées qui contrôlent la zone : en solo ou en duo, elle est rarement rentable.</td></tr>
                  <tr><td><strong>Central Elevator</strong></td><td>Conditionnelle</td><td>Contrôles dans la Control Tower</td><td>La sortie qui rapporte le plus, parce qu'elle débouche au cœur du loot premium. Elle se débloque en passant par la tour — donc on ne l'active pas au hasard, on l'anticipe.</td></tr>
                </tbody>
              </table>
            </div>
            <p>La règle de décision qui en découle est simple : <strong>ce n'est pas le loot total qui
            compte, c'est le Koen par minute</strong>. Une sortie à 15 minutes qui rapporte 250 000 K
            vaut mieux qu'une sortie à 25 minutes qui en rapporte 400 000. Et la durée du raid doit
            toujours être comparée au trajet qu'il reste à faire, en comptant les healed, le poids du
            sac, les interrupteurs à activer et les approches contestées.</p>
            <p class="small text-muted">Source : guides d'analyse de la communauté et retours
            de joueurs sur les sorties d'Airport (novembre 2026). Les délais d'activation sont
            rapportés par les joueurs ; ils peuvent varier selon la saison. Donnée communautaire,
            non publiée par l'éditeur.</p>
          </div>
'''

MARQUEUR = "Les sorties d'Airport ne se valent pas"


def main():
    s = PAGE.read_text(encoding="utf-8")
    if MARQUEUR in s:
        print("  deja present")
        return 0
    m = re.search(r'<h2[^>]*id="zones"[^>]*>', s)
    assert m, "ancre zones introuvable"
    s = s[: m.start()] + BLOC.strip() + "\n\n" + s[m.start():]
    PAGE.write_text(s, encoding="utf-8")
    print("  enrichi : pages/map-airport.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
