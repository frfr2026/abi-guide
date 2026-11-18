#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - Veille du 18/11/2026, vague D.

Deux apports :
  1. saison7-battle-pass.html  -> objectifs de mission du conteneur securise 3x3
  2. communaute-ressources.html -> alerte sur les faux depots GitHub deguises

Mecanique auto-reparante : purge systematique avant reinsertion.
"""
import pathlib
import re
import sys

MISSIONS_3X3 = """          <div class="callout callout-success">
            <h3 class="h4">Comment obtenir la case 3×3 Titanium Case</h3>
            <p>Le conteneur sécurisé 3×3 se débloque en terminant les <strong>missions de saison</strong>, en
            deux difficultés : <strong>Normal</strong> et <strong>Hardcore</strong>. Les objectifs published
            pour la Saison&nbsp;7 tournent tous autour des zones infectées et de la signalétique de Valley.</p>
            <div class="table-wrap">
              <table class="data-table">
                <thead><tr><th>Objectif</th><th>Mission</th></tr></thead>
                <tbody>
                  <tr><td>Éliminer 10 ennemis ou mutants dans la zone ouest de Farm</td><td>Back in Shadow</td></tr>
                  <tr><td>Fouiller 15 conteneurs non fouillés dans la zone est de Valley</td><td>First Meeting</td></tr>
                  <tr><td>Localiser le signal au Crash Canyon de Valley</td><td>Checking the Clues</td></tr>
                  <tr><td>Localiser le signal à la Summit Platform de Valley</td><td>Military Isolation Zone</td></tr>
                  <tr><td>Localiser le signal à l'héliport de la Beach Villa de Valley</td><td>Military Isolation Zone</td></tr>
                  <tr><td>Éliminer 15 ennemis ou mutants dans Valley</td><td>Northridge Situation</td></tr>
                  <tr><td>Survivre 20 minutes à Northridge</td><td>Northridge Situation</td></tr>
                  <tr><td>Fouiller 4 boîtes à documents ou caisses de ravitaillement à Northridge</td><td>Northridge Situation</td></tr>
                </tbody>
              </table>
            </div>
            <p>Deux points de vigilance. D'abord, la plupart de ces objectifs se remplissent en <strong>Lockdown
            ou en Forbidden</strong> : le seuil de valeur d'équipement y est plus élevé, donc la mission coûte
            plus cher en matériel perdu qu'en Normal. Ensuite, la case 3×3 <strong>est réinitialisée au début de
            la saison suivante</strong> — c'est un objet de saison, pas un achat définitif.</p>
            <p class="small text-muted">Source&nbsp;: base de données de missions ABI Builder, recoupée avec les
            guides vidéo de déblocage de la case 3×3 de septembre 2026 — <strong>Documenté</strong>, non publiée
            par l'éditeur. Les objectifs de mission évoluent d'une saison à l'autre&nbsp;: vérifiez la liste
            active dans votre interface avant de planifier une rotation.</p>
          </div>
          """

ALERTE_GITHUB = """          <div class="callout callout-danger">
            <h3 class="h4">Le piège nouveau : des dépôts GitHub au nom innocent</h3>
            <p>La catégorie «&nbsp;ESP, wallhack, aimbot&nbsp;» est connue. Mais une nouvelle famille de dépôts
            trompeurs s'est installée en 2026 sur des noms qui <em>semblent</em> légitimes&nbsp;: ils ne
            promettent plus une triche, ils promettent un <strong>outil d'analyse</strong>.</p>
            <ul>
              <li><strong>«&nbsp;Loot Player Tracker Bundle&nbsp;»</strong> — présente un suivi du loot, un radar
              et un «&nbsp;aim assistant&nbsp;», avec un lien d'installation en gros bouton bleu.</li>
              <li><strong>«&nbsp;Raid Profit Tracker&nbsp;»</strong> — annonce un suivi de profit par raid, un
              tableau de bord et une base de prix de vente. Le nom est celui d'un utilitaire légitime.</li>
              <li><strong>«&nbsp;Tactical Radar&nbsp;»</strong> — se présente comme un overlay externe «&nbsp;sans
              injection&nbsp;» et «&nbsp;portable&nbsp;», ce qui est précisément l'argument qui rend crédible un
              exécutable malveillant.</li>
            </ul>
            <p>Le raisonnement qui doit rester&nbsp;: <strong>un dépôt GitHub ne devient pas sûr parce qu'il est
            utile</strong>. Les outils communautaires authentiques — le suivi des clés, la calculatrice
            balistique, la base de données — sont des <strong>applications web</strong> qui tournent dans votre
            navigateur, sans rien installer. Tout ce qui se présente comme un «&nbsp;outil&nbsp;» à
            <em>télécharger</em> pour Windows et qui promet une fonction d'analyse porte la signature du
            leurre.</p>
            <p class="small text-muted">Constat issu de l'observation des dépôts publiés sur GitHub en
            novembre 2026 — <strong>Communautaire</strong>. Les sanctions rappelées par l'éditeur
            (anti-triche kernel-level, bannissement de dix ans, confiscation du Koen) sont
            <strong>Officielles</strong>.</p>
          </div>
          """

BLOCS = [
    (
        "pages/saison7-battle-pass.html",
        "MISSIONS3X3",
        MISSIONS_3X3,
        r'<h2 id="autre-recompenses">|<h2[^>]*>\s*3\.\s*Les autres récompenses',
        r'<div class="callout callout-success">\s*<h3 class="h4">Comment obtenir la case 3×3.*?</div>\s*',
    ),
    (
        "pages/communaute-ressources.html",
        "GITHUB",
        ALERTE_GITHUB,
        r'<h2 id="youtube">',
        r'<div class="callout callout-danger">\s*<h3 class="h4">Le piège nouveau.*?</div>\s*',
    ),
]


MOTIF_UNICODE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]")


def purger_bloc(s, motif):
    """Supprime un bloc <div class=...> ... </div> en gerant l'imbrication."""
    while True:
        m = re.search(motif, s, flags=re.S)
        if not m:
            return s
        # remonte au <div class=...> qui ouvre le bloc
        debut = s.rfind('<div class="callout', 0, m.start())
        if debut == -1:
            debut = m.start()
        # compte les div pour trouver la fermeture correspondante
        i = debut
        profondeur = 0
        fin = None
        for d in re.finditer(r'<div\b|</div>', s[debut:]):
            if d.group(0).startswith('</'):
                profondeur -= 1
                if profondeur == 0:
                    fin = debut + d.end()
                    break
            else:
                profondeur += 1
        if fin is None:
            fin = m.end()
        s = s[:debut] + s[fin:]
        # nettoie les lignes vides laisseees
        s = s[:debut].rstrip() + "\n" + s[fin:].lstrip("\n")


def traiter(fichier, ident, contenu, ancre, motif_purge):
    hors = MOTIF_UNICODE.findall(contenu)
    if hors:
        print(f"  [!!] {ident} : caractere multilingue {set(hors)}")
        return False
    chemin = pathlib.Path(fichier)
    s = chemin.read_text(encoding="utf-8")

    s = re.sub(r"[ \t]*<!--VEILLE-D[^\n]*-->\n?", "", s)
    s = purger_bloc(s, motif_purge)

    m = re.search(ancre, s)
    if not m:
        print(f"  [!!] ancre introuvable dans {fichier} pour {ident}")
        return False

    ouverture = f"<!--VEILLE-D:{ident}:OPEN-->"
    fermeture = f"<!--VEILLE-D:{ident}:CLOSE-->"
    bloc = f"{ouverture}\n{contenu}\n          {fermeture}"
    s = s[: m.start()] + bloc + "\n" + s[m.start():]
    chemin.write_text(s, encoding="utf-8")
    return True


def main():
    for fichier, ident, contenu, ancre, motif in BLOCS:
        if traiter(fichier, ident, contenu, ancre, motif):
            print(f"  {fichier} : bloc {ident} insere")
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
