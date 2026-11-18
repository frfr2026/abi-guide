#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - Veille du 18 novembre 2026, vague C.

Trois apports issus de la recherche en ligne, classes par nature :

1. items-munitions.html  -> top-loading du chargeur          [Communaute]
2. meta-strategies-s7.html-> lobby de bots Lockdown (6 morts) [Communaute]
3. communaute-ressources.html -> TikTok / X : la verticale     [Mixte]

Mecanique auto-reparante : purge systematique des blocs existants (marques ou
non) avant reinsertion, marqueurs ouvrants/fermants distincts. Idempotent.
"""
import pathlib
import re
import sys

# --------------------------------------------------------------------------
# 1. TOP-LOADING du chargeur  (items-munitions.html)
# --------------------------------------------------------------------------
TOP_LOADING = """          <div class="callout callout-success">
            <h3 class="h4">Le top-loading : un chargeur à deux étages</h3>
            <p>Le chargeur ne se vide pas au hasard&nbsp;: il part par le haut. Charger les
            <strong>premières balles en munitions hautes</strong> et le reste du chargeur en munitions
            bon marché donne une <strong>rafale d'ouverture à pleine pénétration</strong>, puis un appoint
            ordinaire pour la suite du combat. C'est le <strong>top-loading</strong>.</p>
            <p>Concrètement&nbsp;: sur un FAL en 7.62×51, dix balles de <strong>M80</strong> (Tier&nbsp;4) ou de
            <strong>M62</strong> (Tier&nbsp;5) en haut du chargeur, le reste en munitions d'appoint&nbsp;; sur un
            A545 en 5.45×39, le même principe avec la <strong>7N39</strong> (Tier&nbsp;5) ou les
            <strong>PPBS</strong> (Tier&nbsp;6). Les guides S7 citent aussi le chargeur «&nbsp;top-loadé&nbsp;» comme
            l'un des leviers les plus rentables en Forbidden.</p>
            <p>Le calcul est simple&nbsp;: vous ne payez la munitions haute que pour les dix premières balles,
            et ce sont précisément celles qui ouvrent le feu. Sur un budget serré, c'est le meilleur rapport
            «&nbsp;pénétration dépensée&nbsp;/&nbsp;balles transportées&nbsp;» de tout le jeu.</p>
            <p class="small text-muted">Source&nbsp;: guides communautaires de la Saison&nbsp;7 et retours de
            joueurs — <strong>Communautaire</strong>, non publiée par l'éditeur. L'ordre de dégagement du
            chargeur est le comportement standard du jeu, mais vérifiez-le une fois en Terrain d'entraînement
            avant de reconstruire vos chargeurs sur cette hypothèse.</p>
          </div>"""

# --------------------------------------------------------------------------
# 2. LOBBY DE BOTS en Lockdown  (meta-strategies-s7.html)
# --------------------------------------------------------------------------
BOT_LOBBY = """          <div class="callout callout-warning">
            <h3 class="h4">Le lobby de bots en Lockdown après six morts</h3>
            <p>Les guides de la communauté signalent un comportement que l'éditeur n'a jamais documenté&nbsp;:
            après <strong>six morts consécutives</strong> sur une carte Tactical Ops en <strong>Lockdown</strong>,
            la <strong>septième partie est tirée dans un lobby composé uniquement de bots</strong>, sans aucun
            joueur réel.</p>
            <p>Les conditions rapportées sont strictes&nbsp;: <strong>ne tuer aucun opérateur ni aucun Scav, ne
            rien looter, et ne rien placer dans son conteneur sécurisé</strong>. L'astuce consiste à rester sous
            le seuil de valeur d'équipement — au besoin en retirant son armure dès l'apparition — pour ne jamais
            être pris pour une cible.</p>
            <p>Deux usages en découlent. Le premier est le <strong>ramassage de munitions de niveau 4 sur les
            bots</strong>, qui est le but le plus simple. Le second est le <strong>mode Warlord</strong>, dont le
            score se fait sur la valeur de loot extraite&nbsp;: un lobby sans joueur réel transforme l'événement
            le plus compétitif du jeu en bureaucratie. Rappel&nbsp;: Lockdown exige un équipement d'un minimum
            de <strong>150&nbsp;000 Koen</strong> à l'entrée, budget à intégrer au calcul.</p>
            <p class="small text-muted">Source&nbsp;: guide de la communauté Steam (Achievement guide, mars&nbsp;2026)
            et confirmation rapportée après la mise à jour S5 — <strong>Communautaire</strong>, non publiée par
            l'éditeur. Le comportement est décrit par les joueurs eux-mêmes&nbsp;: traitez-le comme une astuce
            fragile, jamais comme une mécanique garantie.</p>
          </div>"""

# --------------------------------------------------------------------------
# 3. RESEAUX SOCIAUX / FORMAT COURT  (communaute-ressources.html)
# --------------------------------------------------------------------------
RESEAUX = """          <div class="callout callout-warning">
            <h3 class="h4">TikTok, X et le format court : une piste, jamais une source</h3>
            <p>Les réseaux courts sont le canal le plus rapide et le plus douteux. Sur <strong>TikTok</strong>, les
            formats les plus répandus chez les joueurs d'ABI sont les codes d'arme à copier et les stratégies de
            clé universelle — celle de la Saison IGNITION, par exemple, a tourné sur la plateforme. Sur
            <strong>X</strong>, le compte officiel <strong>@ArenaBreakoutPC</strong> publie les notes de patch
            complètes&nbsp;: c'est la source à privilégier, chaque patch y étant déposé le jour de la
            maintenance.</p>
            <p>Le réflexe à adopter&nbsp;: <strong>une vidéo courte est une piste, pas une source</strong>. Le
            format court supprime le contexte — la version du jeu, le mode, la date. Une astuce sans date ni mode
            est inexploitable&nbsp;; une astuce sans source est un pari.</p>
            <p>Les trois erreurs les plus fréquentes en vidéo courte&nbsp;: un build présenté sans son mode, donc
            potentiellement hors plafond de tier&nbsp;; une ammunition dont le Pierce Level a changé depuis&nbsp;;
            un code d'arme copié d'une version antérieure. Reprenez les <a
            href="communaute-ressources.html#outils">codes d'arme partageables</a> et vérifiez le build dans le
            jeu avant de le payer.</p>
            <p class="small text-muted">Source&nbsp;: TikTok (JawlArena, Rizukyd), X / @ArenaBreakoutPC —
            <strong>Communautaire</strong> pour les formats courts, <strong>Officielles</strong> pour les notes de
            patch publiées par l'éditeur.</p>
          </div>"""

BLOCS = [
    (
        "pages/items-munitions.html",
        "TOPLOAD",
        TOP_LOADING,
        "<h2 id=\"speciales\">",
        r'<div class="callout callout-success">\s*<h3 class="h4">Le top-loading.*?</div>\s*',
    ),
    (
        "pages/meta-stratégies-s7.html",
        "BOTLOBBY",
        BOT_LOBBY,
        '<h2 id="extraction">',
        r'<div class="callout callout-warning">\s*<h3 class="h4">Le lobby de bots en Lockdown.*?</div>\s*',
    ),
    (
        "pages/communaute-ressources.html",
        "RESEAUX",
        RESEAUX,
        "<h2 id=\"phishing\">",
        r'<div class="callout callout-warning">\s*<h3 class="h4">TikTok, X et le format court.*?</div>\s*',
    ),
]


def traiter(fichier, ident, contenu, ancre, motif_purge):
    chemin = pathlib.Path(fichier)
    s = chemin.read_text(encoding="utf-8")

    # purge des marqueurs de tous types + du bloc existant
    s = re.sub(r"[ \t]*<!--VEILLE-C[^\n]*-->\n?", "", s)
    s = re.sub(motif_purge, "", s, flags=re.S)

    if ancre not in s:
        print(f"  [!!] ancre introuvable dans {fichier} pour {ident}")
        return False

    ouverture = f"<!--VEILLE-C:{ident}:OPEN-->"
    fermeture = f"<!--VEILLE-C:{ident}:CLOSE-->"
    bloc = f"{ouverture}\n{contenu}\n          {fermeture}"
    i = s.index(ancre)
    s = s[:i] + bloc + "\n" + s[i:]
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
