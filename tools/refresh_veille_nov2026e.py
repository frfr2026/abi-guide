#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - Veille du 18/11/2026, vague E.

Apports issus de la recherche forums / Reddit / YouTube du 18 novembre 2026 :

  1. pages/guide-economie.html
     -> le seuil de rentabilite (regle du kit) : ce qui manque
  2. pages/guide-economie.html
     -> la boucle de revente Deke / ventes a duree limitee
  3. pages/saison7-zombie-endless.html
     -> les gisements d'IA (vent d'ascenseur, tumeur de l'escalier,
        voiture de police) et le piege des monstres d'IA

Mecanique de purge : suppression par div equilibre, c'est-a-dire comptage des
<div> et </div> pour trouver la fermeture correspondante. Un motif regex
non glouton s'arreterait au premier </div> imbrique et laisserait un residu
dans le document -- c'est exactement ce qui a casse les pages
guide-economie.html et saison7-zombie-endless.html lors des premieres
tentatives.

Le bloc est identifie par son titre de <h3 class="h4">, qui est unique dans
la page. Trois passes :
  1. suppression du div dont le titre correspond ;
  2. si le titre a disparu mais qu'un fragment du corps traine, suppression
     de ce fragment ;
  3. reinsertion a l'ancre.

Idempotent.
"""
import pathlib
import re
import sys

MOTIF_UNICODE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]")


# ── 1. Le seuil de rentabilité ────────────────────────────────────────────
SEUIL = """          <div class="callout callout-warning">
            <h3 class="h4">La règle du seuil : votre kit doit être plus petit que votre loot espéré</h3>
            <p>La phrase la plus utile du jeu, et la plus répétée par les joueurs qui
            survivent à une saison : <strong>n'entrez jamais avec un kit plus cher que ce que
            vous comptez sortir du raid</strong>. Et pas « à peu près » : <em>sensiblement</em>
            en dessous.</p>
            <p>La version outillée de cette règle est arithmétique, et elle tient en une
            ligne&nbsp;:</p>
            <div class="table-wrap">
              <table class="data-table">
                <caption>Le calcul qui décide de chaque raid</caption>
                <thead><tr><th>Étape</th><th>Calcul</th><th>Ce que ça vous donne</th></tr></thead>
                <tbody>
                  <tr><td>1. Loot espéré</td><td>ce que vous comptez réellement ramener</td><td>estimation <strong>pessimiste</strong>, jamais optimiste</td></tr>
                  <tr><td>2. Multiplier par votre taux d'extraction</td><td>loot espéré × 0,40 si vous extrayez 40 % du temps</td><td>la vraie recette espérée</td></tr>
                  <tr><td>3. Plafonner le kit</td><td>recette espérée − marge de sécurité</td><td>le budget maximum de votre prochain raid</td></tr>
                </tbody>
              </table>
            </div>
            <p>Concrètement&nbsp;: si vous estimez sortir <strong>600 000 K</strong> d'un raid et
            que votre taux d'extraction est de 40 %, votre recette espérée est de 240 000 K.
            Votre kit doit donc coûter nettement moins que ça — munitions et consommables
            compris. Entrer avec 600 000 K de kit pour viser 600 000 K de loot, c'est un raid
            déjà perdu d'avance&nbsp;: il suffit d'un seul raid raté pour l'emporter.</p>
            <p>Une variante encore plus prudente circule sur les Reddit economics&nbsp;: ne jamais
            engager plus de <strong>1 % de votre patrimoine total</strong> dans un raid. Avec
            20 millions de liquidités, cela fait 200 000 K de kit maximum&nbsp;; avec 10 millions,
            100 000 K. Ce plafond est brutal mais il protège&nbsp;: c'est le seul qui rende
            l'économie <em>stable</em> même quand le taux d'extraction s'effondre.</p>
            <p class="small text-muted">Sources&nbsp;: fils Reddit «&nbsp;Koen&nbsp;» et «&nbsp;how are you all
            making your koen efficiently&nbsp;», discussions sur le taux d'extraction et le
            seuil de rentabilité — <strong>Communautaire</strong>. Le plafond officiel de
            900 000 K en Lockdown reste la seule règle <strong>Officielle</strong> applicable.</p>
          </div>"""

# ── 2. La boucle de revente Deke ───────────────────────────────────────────
DEKE = """          <div class="callout callout-success">
            <h3 class="h4">La boucle sans raid : la revente au marchand de terrain</h3>
            <p>Il existe une source de Koen qui ne demande <strong>aucun raid</strong> et qui est
            régulièrement sous-estimée&nbsp;: la revente pure. Le principe est simple —
            acheter chez le marchand de terrain ce qui est sous son prix de marché, le
            revendre au marché ou l'utiliser au raid suivant.</p>
            <ul>
              <li><strong>Les ventes à durée limitée du marchand</strong> changent et se
              réapprovisionnent. Une rotation de trois achats par jour sur des articles en
              promotion suffit à dégager un profit régulier, sans risquer un seul Koen
              d'équipement.</li>
              <li><strong>Le seuil de rentabilité du marchand</strong> est bas&nbsp;: sur un article
              acheté 10 000 K sous le prix du marché, la marge est déjà nette. Il n'est pas
              question de faire un pari fou sur un seul achat.</li>
              <li><strong>Les clés font exception</strong> : une clé d'or achetée en
              promotion et revendue peut représenter à elle seule plusieurs centaines de
              milliers de Koen de profit.</li>
              <li><strong>Les accessoires</strong> se vendent en lots sur le marché&nbsp;:
              une grenade, un booster ou un consommable se négocie au prix du lot, pas à
              l'unité. Il faut comparer en volume.</li>
            </ul>
            <p>Le corollaire, lui aussi très cité&nbsp;: <strong>videz votre stockage</strong>. Un
            article qui dort dans votre inventaire ne rapporte rien et occupe un emplacement
            que vous privédez. Vendre ce dont vous n'avez pas besoin avant le prochain raid
            est un geste à rendement nul qui libère de la place — et votre place vaut de
            l'argent quand le sac est plein.</p>
            <p class="small text-muted">Sources&nbsp;: fils Reddit sur le merchandising et les
            «&nbsp;limited time deals&nbsp;» du marchand — <strong>Communautaire</strong>. Les prix
            et la disponibilité des articles varient à chaque rotation&nbsp;: vérifiez le
            marchand dans votre jeu avant de convertir un capital en stock.</p>
          </div>"""

# ── 3. Zombie Endless : gisements d'IA ─────────────────────────────────────
IA = """          <div class="callout callout-success">
            <h3 class="h4">Les gisements d'IA du mode Endless</h3>
            <p>Les zombies de la Saison 7 ne sont pas des points de vie qui marchent&nbsp;:
            ce sont des <strong>agents de jeu</strong> avec des règles de pathfinding, des
            routines et, parfois, une taille qui change leur comportement. Plusieurs zones de
            l'Airport sont neutralisables en compris le mécanisme, sans tirer un seul coup de
            feu.</p>
            <div class="table-wrap">
              <table class="data-table">
                <caption>Gisements et pièges signalés sur l'Airport</caption>
                <thead><tr><th>Zone</th><th>Ce qu'on y trouve</th><th>Comment l'exploiter</th></tr></thead>
                <tbody>
                  <tr><td>Conduit de ventilation dans la gaine d'ascenseur (zone centrale, salle du chariot élévateur)</td><td>Un abri où les zombies ne peuvent pas vous atteindre</td><td>On s'y cache ; seule l'ambushade d'un Assautant finit par y entrer, et sa taille diminue pendant le bond, ce qui ouvre une fenêtre</td></tr>
                  <tr><td>Sous les avions et dans les hangars de la zone d'exposition</td><td>Des zones où le Briseur ne peut pas charger</td><td>Les conteneurs et les avions bloquent sa course ; contre un Breacher, la parade est de se placer à l'abri et de tirer au corps à corps — impossible de viser la tête</td></tr>
                  <tr><td>Escaliers du secteur central</td><td>De petites tumeurs en travers</td><td>Laissées en place, elles bloquent la horde&nbsp;; ne tuez que les grosses tumeurs derrière elles</td></tr>
                  <tr><td>Voitures de police</td><td>Un piège sonore</td><td>Leur sirène attire la horde dès que vous approchez&nbsp;: approchez-en uniquement dans le cadre d'une mission, sinon vous déclenchez une vague pour rien</td></tr>
                  <tr><td>Automatique extérieur de l'Airport</td><td>Un moyen de contenir la horde</td><td>À utiliser en dernier recours, quand le combat est déjà perdu&nbsp;: elle bloque les zombies dans un couloir</td></tr>
                </tbody>
              </table>
            </div>
            <p>Deux avertissements qui découlent de cette lecture. D'abord, <strong>ne comptez
            pas sur le corps d'un teammate à terre</strong> pour retenir la horde&nbsp;: certains
            zombies passent devant sans s'y arrêter, mais d'autres s'y accumulent et bloquent
            alors le passage — le résultat est aléatoire, ne le construisez pas. Ensuite,
            <strong>ne vous approchez pas des voitures de police</strong> hors mission&nbsp;: la
            sirène est le moyen le plus sûr de transformer un raid tranquille en catastrophe.</p>
            <p class="small text-muted">Sources&nbsp;: retours Reddit de septembre et octobre 2026
            sur l'Airport en mode Endless — <strong>Communautaire</strong>. Ces positions sont
            propres au mode Endless et à la Saison 7&nbsp;: elles ne s'appliquent ni à la Zone
            infectée ni aux cartes classiques.</p>
          </div>"""


BLOCS = [
    (
        "pages/guide-economie.html",
        "La règle du seuil : votre kit doit être plus petit que votre loot espéré",
        "Concrètement&nbsp;: si vous estimez",
        SEUIL,
        r'<h2 id="regles-or">|<h2[^>]*>\s*3\.\s*Les règles d',
    ),
    (
        "pages/guide-economie.html",
        "La boucle sans raid : la revente au marchand de terrain",
        "Il existe une source de Koen qui ne demande",
        DEKE,
        r'<h2 id="plan-4-phases">|<h2[^>]*>\s*4\.\s*Le plan en 4 phases',
    ),
    (
        "pages/saison7-zombie-endless.html",
        "Les gisements d'IA du mode Endless",
        "Deux avertissements qui découlent de cette lecture",
        IA,
        r'<h2 id="astuces">|<h2[^>]*>\s*4\.\s*Astuces de terrain',
    ),
]


def retirer_div_equilibre(s, debut):
    """Supprime le <div> qui commence a `debut`, contenu imbrique compris."""
    prof = 0
    for m in re.finditer(r"<div\b|</div>", s[debut:]):
        if m.group(0) == "</div>":
            prof -= 1
            if prof == 0:
                return s[:debut] + s[debut + m.end():]
        else:
            prof += 1
    return s


def trouver_bloc(s, titre):
    """Retourne (debut, fin) du div appel dont le h3 porte `titre`."""
    h = re.search(r'<h3 class="h4">%s</h3>' % re.escape(titre), s)
    if not h:
        return None, None
    d = s.rfind('<div class="callout', 0, h.start())
    if d == -1:
        return None, None
    prof = 0
    for m in re.finditer(r"<div\b|</div>", s[d:]):
        if m.group(0) == "</div>":
            prof -= 1
            if prof == 0:
                return d, d + m.end()
        else:
            prof += 1
    return None, None


def purger(s, titre, signature):
    """Retire le bloc identifie par son titre, et tout fragment du meme corps."""
    d, f = trouver_bloc(s, titre)
    if d is not None:
        return s[:d] + s[f:]

    # le bloc a disparu mais son corps traine : on retire le fragment qui
    # va de la signature jusqu'au prochain <h2 ou la fin du conteneur.
    for m in list(re.finditer(re.escape(signature), s))[::-1]:
        p = s.rfind("<p", 0, m.start())
        if p == -1:
            continue
        # fin du fragment : le prochain </div> suivi d'un <h2, ou le prochain
        # <h2, ou la fin de la section
        fin = None
        for mm in re.finditer(r"</div>\s*(?=<h2)|<h2", s[m.start():]):
            fin = m.start() + mm.start()
            break
        if fin is None:
            fin = len(s)
        s = s[:p] + s[fin:]
    return s


def traiter(fichier, titre, signature, contenu, ancre):
    chemin = pathlib.Path(fichier)
    s = chemin.read_text(encoding="utf-8")

    hors = MOTIF_UNICODE.findall(contenu)
    if hors:
        print("  [!!] %s : caractere multilingue %s" % (titre[:30], set(hors)))
        return False

    s = purger(s, titre, signature)

    m = re.search(ancre, s)
    if not m:
        print("  [!!] ancre introuvable dans %s pour %s" % (fichier, titre[:30]))
        return False

    s = s[:m.start()] + contenu + "\n\n" + s[m.start():]
    # normalise les lignes vides residuelles : la purge peut en laisser
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    chemin.write_text(s, encoding="utf-8")
    return True


def main():
    for fichier, titre, signature, contenu, ancre in BLOCS:
        if traiter(fichier, titre, signature, contenu, ancre):
            print("  %s : bloc « %s » insere" % (fichier, titre[:38]))
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
