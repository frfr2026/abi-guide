#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - vague F : deduplication du bloc GitHub + integration des
reglages de sensibilite de la Saison 7.

1) pages/communaute-ressources.html
   Le callout « Le piege nouveau : des depots GitHub au nom innocent » a ete
   insere deux fois : une copie non balisee (avant le marqueur VEILLE-D) et
   une copie balisee (<!--VEILLE-D:GITHUB:OPEN--> ... :CLOSE-->). Le script
   conserve la copie balisee et retire uniquement les copies identiques
   situees en dehors de la region balisee. Aucun autre contenu n'est touche :
   le texte supprime est, mot pour mot, celui qui est conserve.

2) pages/reglages-sensibilite.html
   Ajoute trois blocs balises (idempotents et reversibles) :
     - le preset indicatif de la Saison 7 (Mouse 0,40 / Aim 0,26, FOV 90-100)
     - l'effet de la grenade stun M290 sur la sensibilite de la souris
     - les deux options de l'onglet Game que les presets oublient
   et une source « Officiel » (notes de patch S7) pour l'effet de la M290.

Chaque bloc insere est encadre par un marqueur VEILLE-F : relancer le
script remplace le contenu encadre au lieu de le dupliquer.

Idempotent.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGES = RACINE / "pages"

# --------------------------------------------------------------------------
# 1. deduplication du bloc GitHub
# --------------------------------------------------------------------------

TITRE_GITHUB = "Le piège nouveau : des dépôts GitHub au nom innocent"

MOTIF_BLOC_GITHUB = re.compile(
    r'<div class="callout callout-danger">\s*<h3 class="h4">' + re.escape(TITRE_GITHUB) + r"</h3>.*?</div>",
    re.S,
)


def normaliser(t):
    return re.sub(r"\s+", " ", t).strip()


def dedupliquer_github(chemin):
    s = chemin.read_text(encoding="utf-8")
    if TITRE_GITHUB not in s:
        print("  [INFO] bloc GitHub absent de", chemin.name)
        return 0

    # region balisee VEILLE-D
    m_open = s.find("<!--VEILLE-D:GITHUB:OPEN-->")
    m_close = s.find("<!--VEILLE-D:GITHUB:CLOSE-->")
    if m_open == -1 or m_close == -1 or m_close < m_open:
        print("  [KO] marqueurs VEILLE-D:GITHUB introuvables dans", chemin.name)
        return 1

    blocs = list(MOTIF_BLOC_GITHUB.finditer(s))
    if not blocs:
        print("  [KO] aucun bloc GitHub detecte dans", chemin.name)
        return 1

    cible = None
    for b in blocs:
        if b.start() >= m_open and b.end() <= m_close:
            cible = b
            break
    if cible is None:
        print("  [KO] aucune copie balisee du bloc GitHub dans", chemin.name)
        return 1

    a_supprimer = [b for b in blocs if b is not cible]
    if not a_supprimer:
        print("  [OK] aucune copie en double du bloc GitHub dans", chemin.name)
        return 0

    # suppression en fin de ligne, du bas vers le haut
    for b in reversed(a_supprimer):
        fin = b.end()
        # emporte le retour a la ligne final pour ne pas laisser de ligne vide
        while fin < len(s) and s[fin] in " \t":
            fin += 1
        if fin < len(s) and s[fin] == "\n":
            fin += 1
        s = s[: b.start()] + s[fin:]

    chemin.write_text(s, encoding="utf-8")
    print("  [OK] %s : %d copie(s) en double retiree(s), copie balisee conservee"
          % (chemin.name, len(a_supprimer)))
    return 0


# --------------------------------------------------------------------------
# 2. reglages-sensibilite.html
# --------------------------------------------------------------------------

BLOC_PRESET = """<!--VEILLE-F:SENS-PRESET:OPEN-->
        <div class="callout callout-info">
          <h3 class="h4">Le preset indicatif de la Saison 7</h3>
          <p>La configuration de référence relevée sur le client de la Saison 7, en octobre 2026, est la suivante : <strong>Mouse Sensitivity 0,40</strong> et <strong>Aim Sensitivity 0,26</strong>. Le repère tient en une phrase : l'Aim Sensitivity de base est réglée <em>légèrement plus basse</em> que la sensibilité caméra, pour que le point rouge et le fer de visée suivent l'hip-fire à peu près au même rythme. Les optiques grossissantes se réduisent ensuite : une 6x doit déplacer beaucoup moins le réticule par centimètre qu'une 1x, sinon le réticule passe à côté de la cible. Le champ de vision se joue dans la même logique — <strong>90 à 100</strong> est la plage compétitive la plus citée, parce qu'un FOV trop large rapetisse les cibles lointaines et qu'un FOV trop étroit retire de la vision périphérique. Ce sont des repères de départ, pas une norme : la seule valeur qui compte est celle que vous tenez d'un raid à l'autre. <span class="src-tag src-communautaire">Communautaire</span></p>
        </div>
<!--VEILLE-F:SENS-PRESET:CLOSE-->"""

BLOC_M290 = """<!--VEILLE-F:SENS-M290:OPEN-->
        <div class="callout callout-warning">
          <h3 class="h4">Quand votre visée devient pâteuse : la M290</h3>
          <p>Si votre souris vous paraît soudain lente au milieu d'un combat, ne rebrouillez pas vos réglages : les notes officielles de la Saison 7 précisent que la <strong>grenade stun M290</strong> «&nbsp;inflige une acouphène, un ralentissement et réduit la sensibilité de la souris des unités à portée&nbsp;». Concrètement, une détonation de M290 transforme votre visée en bouillie pendant quelques secondes, et l'image reste partiellement brouillée si vous regardiez l'explosion. C'est un effet de jeu, pas une dérive de votre configuration : vérifiez seulement que vous n'avez pas abaissé votre sensibilité entre deux raids, et vous éviterez de corriger un réglage qui était bon. <span class="src-tag src-officiel">Officiel</span></p>
        </div>
<!--VEILLE-F:SENS-M290:CLOSE-->"""

BLOC_GAME = """<!--VEILLE-F:SENS-GAME:OPEN-->
        <div class="callout callout-info">
          <h3 class="h4">Deux options de l'onglet Game que les presets oublient</h3>
          <ul>
            <li><strong>Border Brightness Settings</strong> — règle la luminosité du contour qui cerne les objets à ramasser. Réglé sur <strong>High</strong>, il rend le loot nettement plus repérable dans une pièce sombre : c'est du temps gagné au ramassage, donc de l'économie, pas du confort.</li>
            <li><strong>Scope Quality</strong> — la qualité de l'image <em>dans</em> la lunette. C'est le dernier budget d'images à ne pas rogner pour un sniper ou un DMR : une image interne molle fait perdre l'avantage que vous avez payé en optique.</li>
          </ul>
          <p class="small text-muted">Valeurs issues des retours de joueurs cités par le guide communautaire de réglages du 26 octobre 2026 — <strong>Communautaire</strong>.</p>
        </div>
<!--VEILLE-F:SENS-GAME:CLOSE-->"""

BLOC_SOURCE = """<!--VEILLE-F:SENS-SRC:OPEN-->
        <h3 class="h4">Officiel</h3>
        <ul class="src-list">
          <li><span class="src-name">Season 7 Update Announcement — grenade stun M290</span> — description officielle de la M290 : détonation retardée, insensible aux obstacles, acouphène, ralentissement, réduction de la sensibilité de la souris dans le rayon et perturbation de la vision des unités regardant l'explosion. <a href="https://patchbot.io/games/arena-breakout-infinite/articles/1423-season-7-update-announcement" target="_blank" rel="noopener" id="lnk-reglages-sensibilite-106">patchbot.io<span class="sr-only"> (nouvel onglet)</span></a></li>
        </ul>
<!--VEILLE-F:SENS-SRC:CLOSE-->"""

INSERTIONS = [
    # (ancre avant laquelle insérer, bloc balisé)
    ('<h2 id="visibilite">3. Le preset visibilité et FPS</h2>', BLOC_PRESET),
    ('<h2 id="visibilite">3. Le preset visibilité et FPS</h2>', BLOC_M290),
    ('<h2 id="touches">4. Les raccourcis qui changent un raid</h2>', BLOC_GAME),
    ('<h3 class="h4">Communautaire</h3>\n        <ul class="src-list">\n          <li><span class="src-name">Best Settings (Season 7)', BLOC_SOURCE),
]


def inserer_balise(s, ancre, bloc):
    """Insere ou remplace un bloc balise juste avant l'ancre donnee."""
    nom = bloc.split("-->")[0].strip()
    marqueur_open = nom
    marqueur_close = nom.replace(":OPEN", ":CLOSE") + "-->"

    # le bloc existe deja : on remplace son contenu
    i = s.find(marqueur_open)
    if i != -1:
        j = s.find(marqueur_close, i)
        if j == -1:
            print("  [KO] marqueur de fin absent :", marqueur_open)
            return s, 1
        fin = j + len(marqueur_close)
        # nettoie les residus "-->" laisses par une version anterieure du script
        while s[fin:fin + 3] == "-->":
            fin += 3
        # on englobe le contenu balise, pas l'ancre
        s = s[:i] + bloc + s[fin:]
        return s, 0

    k = s.find(ancre)
    if k == -1:
        print("  [KO] ancre introuvable :", ancre[:60])
        return s, 1
    s = s[:k] + bloc + "\n" + s[k:]
    return s, 0


def integrer_reglages(chemin):
    s = chemin.read_text(encoding="utf-8")
    erreurs = 0
    for ancre, bloc in INSERTIONS:
        s, e = inserer_balise(s, ancre, bloc)
        erreurs += e
    if erreurs:
        print("  [KO] %d insertion(s) en echec" % erreurs)
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] %s : 4 blocs balises VEILLE-F inseres ou mis a jour" % chemin.name)
    return 0


def main():
    ecarts = 0
    ecarts += dedupliquer_github(PAGES / "communaute-ressources.html")
    ecarts += integrer_reglages(PAGES / "reglages-sensibilite.html")
    if ecarts:
        print("\n  %s" % ("%d anomalie(s)" % ecarts))
        return 1
    print("\n  vague F appliquee")
    return 0


if __name__ == "__main__":
    sys.exit(main())
