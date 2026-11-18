#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - Correctif editorial des cles (dureabilite post-Saison 3).

Source officielle : notes de patch "Full Release" de l'editeur, Season 3 : Breach,
X / @ArenaBreakoutPC, 15 septembre 2025.
  - "The durability of newly-produced keys from beyond Season 3 has been increased
     to 3 times the original, and their durability is consumed by 1, 2, and 3 in
     normal modes, Lockdown Zone, and Forbidden Zone, respectively."
  - "Your existing keys can still be used according to pre-existing rules, and an
     'old' prefix has been added to them."
  - "We recommend prioritizing the usage of old keys in Lockdown and Forbidden Zone raids."
  - "Universal Keys remain as single-use items that are not affected by the map and difficulty."

Source documentee : ABI Wiki, page Keys (dureabilite de base apres le x3 officiel).

Approche auto-reparante : le script purge d'abord toute version existante des blocs
(marquees ou non), puis les reinserts avec des marqueurs ouvrants/fermants distincts.
Idempotent et reparateur.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/items-cles.html")

TAG_OFF = '<span class="src-tag src-officiel">Officiel</span>'

VALEURS = [
    ("Motel Main Guest Room Key", 30),
    ("Motel 201 Key", 45),
    ("Barn Office Key", 45),
    ("Master Bedroom Key", 45),
    ("Stables Warehouse Key", 75),
    ("Beach Villa Main Bedroom Key", 30),
    ("Beach Villa Storage Key", 30),
    ("Factory Dressing Room Key", 45),
    ("Factory File Room Key", 45),
    ("Staff Dormitory Key", 45),
    ("RV Camp Cabin Cafeteria Key", 45),
    ("Courtyard Basement Key", 30),
    ("Private Lounge Key", 45),
    ("Second Floor Lounge Key", 45),
    ("2F Directors Office Card", 30),
    ("2F General Office Card", 30),
    ("Post Production Room Key", 30),
    ("Editing Room Key", 30),
    ("Planning Room Key", 30),
    ("Infirmary Key", 45),
    ("Darkroom Key", 45),
]

CONTENU_ANC = """          <div class="callout callout-warning">
            <h3 class="h4">Les clés anciennes ne suivent pas la règle des nouvelles</h3>
            <p>Les notes de patch officielles du <strong>15 septembre 2025</strong> (Season&nbsp;3&nbsp;: Breach) ont
            changé la règle&nbsp;: la <strong>durabilité des clés produites après la Saison&nbsp;3 a été multipliée
            par trois</strong>, et leur consommation suit le barème <strong>1&nbsp;point en Normal, 2 en Lockdown,
            3 en Forbidden</strong>. Vos clés déjà possédées <strong>gardent les règles d'avant</strong> et ont reçu
            le préfixe «&nbsp;old&nbsp;».</p>
            <p>Concrètement, une clé ancienne consomme <strong>un seul point d'usage, quel que soit le mode</strong>.
            Elle ne vous fait donc <strong>rien perdre</strong> en Lockdown ou en Forbidden — c'est même là que
            l'éditeur recommande de l'utiliser&nbsp;: <em>«&nbsp;We recommend prioritizing the usage of old keys in
            Lockdown and Forbidden Zone raids.&nbsp;»</em></p>
            <p>L'argument inverse — «&nbsp;les anciennes clés se dépensent en Normal&nbsp;» — est un contresens
            économique&nbsp;: ses 15&nbsp;points s'échangent contre 15&nbsp;ouvertures, où que vous les croisiez.
            Les dépenser en Normal transforme 15&nbsp;portes de Forbidden à fort loot en 15&nbsp;portes de valeur
            faible. <strong>Les anciennes clés vont en Lockdown et en Forbidden&nbsp;; les neuves, plus durables,
            peuvent être diluées sur plusieurs modes.</strong></p>
            <p class="small text-muted">Source&nbsp;: notes de patch officielles de l'éditeur
            (X&nbsp;/ @ArenaBreakoutPC, 15/09/2025) — <strong>Officielles</strong>. La lecture économique
            «&nbsp;une ouverture de Forbidden vaut plus qu'une ouverture de Normal&nbsp;» est recoupée avec les
            retours de joueurs sur r/ArenaBreakoutInfinite — <strong>Communautaire</strong>.</p>
          </div>"""

CONTENU_CREDIT = """          <div class="callout callout-success">
            <h3 class="h4">L'ouverture « à crédit » : votre clé vous offre une porte de plus</h3>
            <p>Une clé neuve consomme 3&nbsp;points par ouverture en Forbidden. Mais quand il ne reste que
            <strong>1 ou 2&nbsp;points</strong> sur la clé, le jeu accepte tout de même l'ouverture&nbsp;: le dernier
            point se dépense «&nbsp;à crédit&nbsp;».</p>
            <p>Résultat&nbsp;: <strong>une clé neuve à 30&nbsp;points n'est pas limitée à 10&nbsp;ouvertures en
            Forbidden</strong> — elle vaut <strong>10&nbsp;ouvertures en Forbidden <em>plus</em> 2&nbsp;ouvertures
            en Normal</strong> (ou 1&nbsp;en Lockdown), récupérées sur les 1 ou 2&nbsp;points restants. Le même
            raisonnement vaut pour toutes les clés neuves, à la durée près.</p>
            <p class="small text-muted">Source&nbsp;: retours de joueurs sur r/ArenaBreakoutInfinite et guide
            Steam de la communauté — <strong>Communautaire</strong>, non publiée par l'éditeur. À vérifier
            dans le jeu, mais cohérent avec le barème officiel de consommation.</p>
          </div>"""

CONTENU_UNI = """          <div class="callout callout-info">
            <h3 class="h4">Ce que dit la note de patch officielle sur les clés universelles</h3>
            <p><em>«&nbsp;Universal Keys remain as single-use items that are not affected by the map and
            difficulty.&nbsp;»</em> Les notes de l'éditeur précisent aussi que le <strong>système de porte-clefs</strong>
            a été amélioré&nbsp;: il se configure par carte <strong>hors raid</strong>, et seules les chaînes
            correspondant à la carte en cours s'affichent pendant le raid.</p>
            <p>Une clé universelle trouvée en raid est donc à <strong>usage unique et sur place</strong>&nbsp;: elle
            ouvre une porte, puis elle disparaît. Ne la gardez pas dans un conteneur fermé en espérant la
            récupérer.</p>
            <p class="small text-muted">Source&nbsp;: notes de patch officielles de l'éditeur
            (X&nbsp;/ @ArenaBreakoutPC, 15/09/2025) — <strong>Officielles</strong>.</p>
          </div>"""

CONTENU_ANNULER = """            <li><strong>Vous pouvez annuler le déverrouillage</strong> — depuis les notes de patch officielles&nbsp;:
            il est possible d'interrompre le déverrouillage <em>avant</em> de pousser la porte, ce qui évite
            qu'une clé soit consommée par une ouverture ratée quand un ennemi arrive. Une clé perdue l'est
            définitivement, un point de durabilité en moins aussi.</li>"""

# (id, contenu, ancre, regex de purge)
BLOCS = [
    (
        "ANC",
        CONTENU_ANC,
        r'<div class="callout callout-success">\s*<h3 class="h4">L\'arithmétique qui décide</h3>',
        r'<div class="callout callout-warning">\s*<h3 class="h4">Les clés anciennes.*?</div>\s*',
    ),
    (
        "CREDIT",
        CONTENU_CREDIT,
        r'<div class="callout callout-success">\s*<h3 class="h4">L\'arithmétique qui décide</h3>',
        r'<div class="callout callout-success">\s*<h3 class="h4">L\'ouverture « à crédit ».*?</div>\s*',
    ),
    (
        "UNI",
        CONTENU_UNI,
        r'<h2 id="rentabilite">',
        r'<div class="callout callout-info">\s*<h3 class="h4">Ce que dit la note de patch officielle sur les clés universelles.*?</div>\s*',
    ),
    (
        "ANNULER",
        CONTENU_ANNULER,
        r"<li>\s*En <strong>Infected Zone</strong>",
        r'\s*<li><strong>Vous pouvez annuler le déverrouillage</strong>.*?</li>',
    ),
]


def purger(s):
    """Retire marqueurs et blocs (marques ou non) pour repartir d'une base propre."""
    s = re.sub(r"[ \t]*<!--CLES-S3[^\n]*-->\n?", "", s)
    for _, _, _, motif in BLOCS:
        s = re.sub(motif, "", s, flags=re.S)
    return s


def poser(s, ident, contenu, ancre):
    ouverture = f"<!--CLES-S3:{ident}:OPEN-->"
    fermeture = f"<!--CLES-S3:{ident}:CLOSE-->"
    bloc = f"{ouverture}\n{contenu}\n          {fermeture}"
    m = re.search(ancre, s)
    if not m:
        raise ValueError("ancre introuvable : " + ancre)
    i = m.start()
    return s[:i] + bloc + "\n" + s[i:]


def corriger_dureabilite(s):
    n = 0
    for nom, valeur in VALEURS:
        pattern = re.compile(
            r"(<tr><td>(?:<strong>)?" + re.escape(nom) + r"(?:</strong>)?</td><td>)(\d+)(\s*"
            + re.escape(TAG_OFF)
            + r"?)(</td>)",
            re.IGNORECASE,
        )
        m = pattern.search(s)
        if not m:
            print(f"  [absent] {nom}")
            continue
        if m.group(2) == str(valeur) and TAG_OFF in m.group(3):
            continue
        s = s[: m.start()] + m.group(1) + str(valeur) + " " + TAG_OFF + m.group(4) + s[m.end():]
        n += 1
    return s, n


def main():
    s = PAGE.read_text(encoding="utf-8")
    avant = s

    # 1. dureabilites officielles
    s, n = corriger_dureabilite(s)
    print(f"  dureabilites corrigees : {n}/{len(VALEURS)}")

    # 2. base propre
    s = purger(s)

    # 3. reinsertion des blocs (ordre : ANC puis CREDIT, meme ancre -> ANCIENNES avant CREDIT)
    for ident, contenu, ancre, _ in BLOCS:
        if not re.search(ancre, s):
            print(f"  [!!] ancre introuvable pour {ident}")
            sys.exit(1)
        s = poser(s, ident, contenu, ancre)
        print(f"  bloc {ident} insere")

    # 4. legende
    if "durée de vie post-Saison 3" not in s:
        s = s.replace(
            '<span class="src-tag src-documente">Documenté</span>\n            <span>donnée reprise de la source de référence du wiki ABI',
            '<span class="src-tag src-officiel">Officiel</span>\n            <span>durée de vie post-Saison 3 (règle ×3 des notes de patch de l\'éditeur).</span>\n            <span class="src-tag src-documente">Documenté</span>\n            <span>donnée reprise de la source de référence du wiki ABI',
        )
        print("  legende mise a jour")

    # 5. date
    s = s.replace(
        "Dernière mise à jour :</span> <span>17 novembre 2026",
        "Dernière mise à jour :</span> <span>18 novembre 2026",
    )

    if s != avant:
        PAGE.write_text(s, encoding="utf-8")
        print("  page ecrite")
    else:
        print("  aucune modification")


if __name__ == "__main__":
    main()
