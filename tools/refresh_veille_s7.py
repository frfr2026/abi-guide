#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integrations des trouvailles de la veille du 18/11/2026 (Reddit, forums,
YouTube, sites d'analyse) qui n'etaient pas encore sur le site :

1. pages/items-medical.html — le membre noirci (Blacked Out). Les guides
   publient une erreur repetee : un bandeau ou un medkit ne repare pas un
   membre noirci, il faut d'abord un kit chirurgical. C'est une source de
   mort avoidable.

2. pages/equipement-casques.html — le casque et le masque sont deux zones
   de degat distinctes en S7, et la penetration est geree par l'endurance
   de la plaque. Les hits disperses sur le casque ET le masque echouent
   la ou trois tirs sur la meme zone reussissent.

3. pages/saison7-utopia.html — les trois sections de mission de faction les
   plus couteuses en raids, et la facon de les contourner.

4. pages/equipement-headsets.html — le reverse lean ne masque plus la zone
   de tete en S7 : le bonus de protection est ferme.

Idempotent.
"""
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")

# ── 1. membre noirci ──────────────────────────────────────────────────────
NOIRCI = '''
          <div class="callout callout-danger">
            <h3 class="h4">Un membre noirci ne se répare pas avec un bandeau</h3>
            <p>Quand un membre arrive à <strong>0 PV</strong>, il passe <em>noirci</em> (Blacked Out).
            <strong>Un bandeau, une trousse ou un medkit ne le réparent pas</strong> : ces objets
            s'appliquent à un membre blessé, pas à un membre noirci. La seule chose qui le remet
            en état est le <strong>kit chirurgical</strong> (Surg-Kit), utilisé sur le membre noirci
            lui-même. Un medkit ne restaure que les <strong>PV</strong> du membre, une fois qu'il
            n'est plus noirci.</p>
            <p>La séquence correcte est donc : <strong>kit chirurgical d'abord</strong> pour débloquer
            le membre, <strong>puis medkit</strong> pour lui rendre ses PV. Inverser l'ordre est la
            mistake la plus répandue, et elle coûte la sortie : on FIGE sur place, on se fait
            abattre, et on repart sans rien.</p>
            <p>Conséquence tactique directe : <strong>un membre noirci vous ralentit à l'amble</strong>.
            Vous courez moins vite, votre bruit change, et vous devenez la cible la plus facile de
            la zone. Dans une zone infectée de Saison 7, où le son attire les horde, c'est souvent
            ce qui décide du raid. Deux antalgiques au minimum dans la trousse, et un kit chirurgical
            par membre apparaissent indispensable dès que la zone est bruyante.</p>
            <p class="small text-muted">Source : guides de survie S7 et retours de joueurs
            (r/ArenaBreakoutInfinite). Donnée communautaire, non publiée par l'éditeur.</p>
          </div>
'''

# ── 2. casque / masque ────────────────────────────────────────────────────
CASQUE = '''
          <div class="callout callout-warning">
            <h3 class="h4">En S7, la tête n'est plus une seule zone</h3>
            <p>Depuis la Saison 7, le <strong>casque</strong> et le <strong>masque</strong> sont
            <strong>deux zones de dégât séparées</strong>. Une balle qui touche le casque et une
            balle qui touche le masque consomment l'endurance de deux pièces différentes : les
            rounds dispersés sur l'ensemble de la tête <strong>échouent là où trois tirs concentrés
            sur la même zone réussissent</strong>.</p>
            <p>Et la <strong>penétration est désormais conditionnée à l'endurance</strong>. L'éditeur
            a supprimé la « faible probabilité de pénétration » contre l'armure de classe V et VI :
            il faut d'abord user la plaque jusqu'à un seuil, et les rounds ne passent ensuite
            qu'assez regularly. En pratique, les tests de terrain convergent sur
            <strong>environ trois tirs de munitions T5 sur le même point</strong> — parfois quatre —
            pour percer un casque de classe VI neuf.</p>
            <p>La conséquence tactique est contre-intuitive etKnown de la plupart des joueurs du
            top : <strong>contre un casque sur-tier, visez la poitrine</strong>, pas la tête. La
            poitrine est une seule grande plaque, bien plus rapide à user qu'un casque splitté
            casque/masque. On réserve la tête aux cas où votre niveau de perforation dépasse
            franchement la classe de l'adversaire, et on tire les membres quand on est très
            sous-tier : les bras et les jambes ne sont pas protégés, et les dégâts de membre
            font saigner et vaciller.</p>
            <p class="small text-muted">Source : notes de patch S7 de l'éditeur et tests de terrain
            publiés (r/ArenaBreakoutInfinite, analyses d'octobre 2026). La règle des « trois tirs »
            est un ordre de grandeur observé, pas une valeur publiée par l'éditeur.</p>
          </div>
'''

# ── 3. sections de mission ────────────────────────────────────────────────
MISSIONS = '''
          <div class="callout callout-info">
            <h3 class="h4">Trois sections de mission qu'il vaut mieux contourner</h3>
            <p>La progression de faction de la Saison 7 se fait par sections obligatoires. Trois
            d'entre elles sont <strong>très coûteuses en raids pour une progression de second
            rang</strong>, et il existe un mécanisme de contournement : passer à la section
            suivante sans les valider complètement.</p>
            <ul>
              <li><strong>Section 1 — « Underground Exploration »</strong> : exige de survivre à
              <strong>dix missions d'extraction urgentes</strong>. Le trafic y est dense, et c'est
              un goulot d'étranglement économique : beaucoup de raids pour une récompense qui se
              débloque ailleurs plus vite.</li>
              <li><strong>Section 2 — « Intern Disruption »</strong> : impose d'extraire par un
              <strong>ascenseur de deuxième étage très exposé</strong>, tout en étant restreint à
              l'usage de grenades. C'est le piège à wipe d'escouade le plus signalé de la saison.</li>
              <li><strong>Section 3 — « Comms Interference »</strong> : force à interagir avec un
              marchand précis <strong>dix fois, plafonnées à deux interactions par déploiement</strong>.
              Contourner la section économise au moins <strong>cinq raids pénibles</strong>.</li>
            </ul>
            <p>Le calcul est simple : ces trois sections ne paient pas en proportion du temps de
            raid qu'elles consomment. La bonne méthode est de passer à la section suivante et de
            revenir sur les récalcitrantes avec un kit de pillage optimisé, une fois la base
            économique solide.</p>
            <p class="small text-muted">Source : guide de survie communautaire S7
            (r/ArenaBreakoutInfinite, septembre 2026). Le mécanisme de contournement des sections
            est rapporté par les joueurs et n'est pas documenté par l'éditeur.</p>
          </div>
'''

# ── 4. reverse lean ───────────────────────────────────────────────────────
REVERSE = '''
          <div class="callout callout-warning">
            <h3 class="h4">Le reverse lean ne masque plus la tête</h3>
            <p>Jusqu'à la Saison 6, s'accroupir et incliner le buste vers l'arrière pouvait
            <strong>réduire la surface de la zone de tête</strong> : on absorbait davantage de
            balles au casque en se penchant. L'éditeur a corrigé ce fonctionnement — « reverse
            leaning could be used to obscure the head hit area » — et la tête est désormais
            exactement là où elle semble être.</p>
            <p>Concrètement, un joueur qui counting sur cette posture perd l'avantage. Le reverse
            lean reste utile pour la <strong>stabilité du tir</strong> et pour se replier vite,
            mais il ne constitue plus un bonus de protection. La contre-mesure n'a pas changé :
            viser la poitrine, qui reste une seule grande plaque, plutôt que la tête.</p>
            <p class="small text-muted">Source : notes de patch S7 de l'éditeur. Donnée publiée
            par l'éditeur.</p>
          </div>
'''

JOBS = [
    ("items-medical.html", "ordre", NOIRCI, True),
    ("equipement-casques.html", None, CASQUE, False),
    ("saison7-utopia.html", None, MISSIONS, False),
    ("equipement-headsets.html", None, REVERSE, False),
]

MARQUEURS = {
    "items-medical.html": "Un membre noirci ne se répare pas",
    "equipement-casques.html": "la tête n'est plus une seule zone",
    "saison7-utopia.html": "Trois sections de mission qu'il vaut mieux contourner",
    "equipement-headsets.html": "Le reverse lean ne masque plus la tête",
}


def inserer_apres_table(s, anchor, block):
    """Insere le bloc juste apres la fermeture du tableau qui suit l'ancre."""
    i = s.find('id="%s"' % anchor)
    assert i > 0, "ancre introuvable : " + anchor
    k = s.find("</table>", i)
    assert k > 0, "tableau introuvable apres " + anchor
    k = s.find("</div>", k)
    assert k > 0
    return s[: k + len("</div>")] + "\n" + block.strip() + s[k + len("</div>"):]


def inserer_avant_h2(s, titre_h2, block):
    """Insere le bloc juste avant le <h2> dont le texte contient titre_h2.

    La comparaison ignore accents et ponctuation : "L'economie change de visage"
    doit retrouver "L'économie change de visage".
    """
    def norm(t):
        t = re.sub(r'<[^>]+>', "", t).lower()
        for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("à", "a"),
                     ("ç", "c"), ("û", "u"), ("ô", "o"), ("î", "i"),
                     ("'", " "), ("’", " "), ("-", " ")):
            t = t.replace(a, b)
        return re.sub(r"\s+", " ", t).strip()

    cible = norm(titre_h2)
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', s, re.S):
        if cible in norm(m.group(1)):
            return s[: m.start()] + block.strip() + "\n\n" + s[m.start():]
    raise AssertionError("h2 introuvable : " + titre_h2)


def main():
    total = 0
    for page, anchor, block, apres_table in JOBS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT page :", page)
            continue
        s = f.read_text(encoding="utf-8")
        marque = MARQUEURS[page]
        if marque in s:
            print("  deja present :", page)
            continue
        if apres_table:
            s = inserer_apres_table(s, anchor, block)
        else:
            # inserer avant le premier h2 de la section concernee
            if page == "equipement-casques.html":
                s = inserer_avant_h2(s, "Les paliers de casques", block)
            elif page == "saison7-utopia.html":
                s = inserer_avant_h2(s, "L'economie change de visage", block)
            elif page == "equipement-headsets.html":
                s = inserer_avant_h2(s, "Les familles de casques audio", block)
        f.write_text(s, encoding="utf-8")
        total += 1
        print("  enrichi :", page)
    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
