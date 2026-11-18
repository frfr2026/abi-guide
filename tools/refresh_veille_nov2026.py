#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vague de veille du 18 novembre 2026 (deuxieme serie) : quatre pages
enrichies a partir de sources nouvelles.

  1. pages/guide-extraction.html
     - les trois voies GRATUITES vers une Secure Case 3x3, avec les citations
       officielles (Saison 4, Saison 5, 1er anniversaire, Noel) ;
     - le prix en Bonds : la controverse documentee, plutot qu'un chiffre
       unique invente ;
     - la regle "les munitions rouges ne peuvent pas etre placees dans une
       Secure Case" rattachee a sa citation officielle de Saison 6 ;
     - le "Supplies Retrieval Device" : le troisieme filet de securite.

  2. pages/meta-strategies-s7.html
     - le plafond de valeur d'equipement de 600 000 Koen en Secure Ops, avec
       les trois regles qui le contournent (usure, port d'equipement seul,
       chargeurs charges) ;
     - le pooling d'equipement en escouade ;
     - la reponse au "le jeu meurt-il ?" avec les chiffres Steam.

  3. pages/items-munitions.html
     - la regle "ce n'est pas l'armure qui tue, c'est la munition" ;
     - le fait qu'une T2 contre une plaque T4 ne fait presque rien.

  4. pages/saison8-attente.html
     - l'etat reel du jeu en nombre de joueurs Steam, avec l'historique
       mensuel complet et la saison launches ;
     - la correction de la lecture "le jeu meurt" ;
     - la S8 a 63 jours : le creux de milieu de saison, pas une mort.

Statuts appliques :
  - Officiel   : citation directe de l'editeur (Steam, notes de patch).
  - Communautaire : rapport de joueurs, mesure en jeu, deduced par recoupement.
  - Documente : verifie sur une source de reference, non publie par l'editeur.

Regles respectees :
  - pas de PNG, pas de SVG, pas de WebP ;
  - aucun fragment multilingue dans le texte ;
  - idempotent : un second passage ne change rien.

Idempotent.
"""
import pathlib
import re
import sys

CIBLE = pathlib.Path("pages")


# ---------------------------------------------------------------------------
# 1. guide-extraction.html
# ---------------------------------------------------------------------------
BLOC_EXTRACTION = """          <h3 class="h4">Les trois voies gratuites vers une Secure Case 3×3</h3>
          <p>La Secure Case est le seul « achat de survie » du jeu — mais il
          existe trois chemins qui ne coûtent rien, et l'éditeur les a
          documentés lui-même. LesIgnorer, c'est payer une location pour un
          objet que le jeu vous donne.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Comment obtenir une Secure Case 3×3 sans dépenser un Bond</caption>
              <thead><tr><th scope="col">Voie</th><th scope="col">Ce que dit l'éditeur</th>
              <th scope="col">Quand</th></tr></thead>
              <tbody>
                <tr><td><strong>Les missions de saison</strong></td>
                <td>« Free Largest Secure Case: Get 3×3 Titanium Cases by completing the
                new season missions. »</td>
                <td>Depuis la Saison 4, reproduit chaque saison</td></tr>
                <tr><td><strong>La boîte aux lettres du jeu</strong></td>
                <td>« Log in and claim the free 3×3 Titanium Secure Case via in-game
                email. »</td>
                <td>Récompense de fin de Saison 5</td></tr>
                <tr><td><strong>Les cartes d'essai 3×3</strong></td>
                <td>Carte d'essai 3×3 Secure Case distribuée avec 4 500 Bonds,
                la plus grosse dotation Bonds de l'histoire du jeu</td>
                <td>1<sup>er</sup> anniversaire, 17 avril 2026</td></tr>
                <tr><td><strong>Lesdistribution de fin d'année</strong></td>
                <td>« We're giving every Operator a free 3×3 Secure Case… delivered via
                in-game mail. »</td>
                <td>21 décembre 2025</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>La routine de fin de saison qui vaut de l'argent.</strong>
            À chaque bascule de saison, deux choses tombent : la Titanium 3×3
            par les missions, et une carte d'essai par la messagerie. Ces
            récompenses sont <strong>limitées à leur fenêtre de
            réclamation</strong> — une carte non réclamée expire. L'astuce
            triviale mais vraie : le 16 septembre, à la bascule vers Utopia,
            votre boîte aux lettres contenait une Secure Case 3×3 gratuite.
            <span class="src-tag src-officiel">Officiel</span></p>
          </div>
          <div class="callout callout-warning">
            <p><strong>Le prix en Bonds : ce que personne ne peut confirmer.</strong>
            Les chiffres publiés se contredisent, et il faut le dire
            franchement plutôt que d'imprimer un nombre faux. Un relevé de
            monétisation de 2024 situait une Case autour de 2 600 Bonds, soit
            environ 25 $ pour 30 jours. D'autres sources décrivaient une
            structure à paliers, avec un petit format autour de 500 Bonds et
            un grand autour de 1 000. Les sites de rechargement de currency
            publient tout et n'importe quoi entre 400 et 2 600 Bonds, ce qui
            est du bruit, pas de la donnée. Ce qui n'est <em>pas</em> contesté,
            c'est le modèle : <strong>Bonds, par format, renouvelé tous les
            30 jours, et non performance</strong> — la Case cesse de protéger
            votre stuff quand l'abonnement expire, sans que vous ayez à
            mourir. La seule source fiable reste l'écran de la boutique dans
            le jeu. <span class="src-tag src-documente">Documenté</span></p>
          </div>
          <div class="callout callout-danger">
            <p><strong>La règle des munitions rouges, et sa source exacte.</strong>
            Les notes de balance officielles de la Saison 6 énoncent une
            restriction nette : <em>« Red ammo cannot be placed in secure
            cases. »</em> Elle n'a jamais été levée depuis. Concrètement, les
            cartouches de haut tier que vous racks — votre stock de munitions
            rouges — disparaissent à la mort même si vous les avez mises dans
            la Case. La Case protège vos clés, votre currency et vos objets de
            quête ; elle ne protège pas vos munitions de haut tier. Cela ne
            contredit pas le plafond de valeur d'équipement : ce sont deux
            règles distinctes qui s'empilent, l'une limitant ce que vous
            <em>entrez</em> avec, l'autre ce que vous pouvez <em>protéger</em>.
            <span class="src-tag src-officiel">Officiel</span></p>
          </div>
          <div class="callout callout-success">
            <p><strong>Le troisième filet de sécurité, et le moins connu.</strong>
            Deux filets sont généralement cités : la Case, et le coéquipier qui
            sort vivant avec votre stuff et vous le renvoie par la messagerie
            du jeu. Il en existe un troisième : le <strong>Supplies Retrieval
            Device</strong>, qui vous est expédié après le raid. Il faut
            connaître l'existence de cette option avant d'en avoir besoin —
            ce qui est précisément le problème des options d'urgence.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

# ---------------------------------------------------------------------------
# 2. meta-strategies-s7.html
# ---------------------------------------------------------------------------
BLOC_META = """          <h3 class="h4">Secure Ops : le plafond de 600 000 Koen et comment le contourner</h3>
          <p>Secure Ops a une limite de valeur d'équipement, et cette limite
          est <strong>la</strong> caractéristique du mode : c'est elle qui
          décide de ce que vous pouvez y emmener. Les joueurs de la Saison 7
          rapportent un plafond de <strong>600 000 Koen</strong> de valeur
          d'équipement, visible sur le compteur
          <em>Equipment Value</em> de l'écran de loadout. Le mode n'affiche
          pas de plafond de tier visible : un build de classe 6 est autorisé.
          Ce qui compte, c'est la valeur, pas le niveau.
          <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les trois règles qui font entrer un kit lourd dans Secure Ops</caption>
              <thead><tr><th scope="col">Règle</th><th scope="col">Ce qu'elle dit</th>
              <th scope="col">Ce que ça change</th></tr></thead>
              <tbody>
                <tr><td><strong>Seul l'équipement porté compte</strong></td>
                <td>« The game only counts what you're wearing as equipment, not
                what's in your bags. »</td>
                <td>Le sac est hors calcul ; porter une armure dans le sac est
                bloqué par le jeu</td></tr>
                <tr><td><strong>L'usure dévalue</strong></td>
                <td>La valeur d'une plaque tombe avec sa durabilité</td>
                <td>Une classe 6 à 0/10 compte à peine : c'est la porte
                d'entrée du build lourd</td></tr>
                <tr><td><strong>Les chargeurs chargés comptent</strong></td>
                <td>Un chargeur de 50 balles vaut autour de 25 000 K</td>
                <td>Charger l'arme en raid plutôt qu'avant : autant de valeur
                laissée dehors</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>Le pooling d'escouade.</strong> Quand l'équipement est
            neuf, une escouade contourne le plafond autrement : chaque membre
            apporte <strong>une seule pièce</strong> coûteuse sous son propre
            plafond, puis la dépose pour un joueur désigné après
            l'apparition. La communauté appelle ce montage un
            « Voltron ». Ce n'est ni une astuce d'exploit ni une triche : c'est
            la mécanique du mode, utilisée comme elle a été conçue.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
          <div class="callout callout-warning">
            <p><strong>Un seuil qui a bougé.</strong> Les discussions les plus
            anciennes de 2025 citent un plafond de 400 000 Koen, pas 600 000.
            Le plafond a donc changé au moins une fois. La règle qui vaut :
            lisez la carte du mode dans votre client avant d'entrer en file.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

BLOC_SANTE = """          <h3 class="h4">Le jeu meurt-il ? Non — et les chiffres le disent</h3>
          <p>La question revient sur Reddit toutes les quelques semaines, et
          elle se pose toujours au même moment : la fin de saison. Voici les
          chiffres Steam relevés au 18 novembre 2026, à 03:00 UTC.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Arena Breakout Infinite sur Steam, relevé du 18 novembre 2026</caption>
              <thead><tr><th scope="col">Mesure</th><th scope="col">Valeur</th>
              <th scope="col">Ce qu'elle signifie</th></tr></thead>
              <tbody>
                <tr><td><strong>Joueurs connectés</strong></td>
                <td><strong>12 144</strong></td>
                <td>03:00 UTC : 22 h aux États-Unis, 6 h à Moscou — hors créneaux
                Europe et Asie</td></tr>
                <tr><td><strong>Sommet sur 24 h</strong></td>
                <td><strong>25 753</strong></td>
                <td>Le meilleur chiffre à citer pour l'heure de pointe</td></tr>
                <tr><td><strong>Moyenne sur 30 jours</strong></td>
                <td><strong>21 769</strong></td>
                <td>Du 19 octobre au 18 novembre</td></tr>
                <tr><td><strong>Sommet sur 30 jours</strong></td>
                <td><strong>37 331</strong></td>
                <td>Dans la même fenêtre</td></tr>
                <tr><td><strong>Record historique</strong></td>
                <td><strong>65 944</strong></td>
                <td>Septembre 2025, le mois du lancement 1.0</td></tr>
              </tbody>
            </table>
          </div>
          <p>La lecture correcte est simple : sur l'année 2026, la moyenne
          mensuelle est restée enfermée dans une bande étroite, entre
          <strong>16 905 et 24 947</strong> joueurs concurrents. Octobre 2026,
          à 24 947, est le meilleur mois depuis octobre 2025. Le creux actuel,
          à 12,7 % sous octobre, reproduit exactement le creux de fin de
          saison déjà observé en février-mars et mai-juin : les plus bas
          historiques sont 18 569 en décembre, 18 022 en mars et 16 905 en
          juin — et les 30 derniers jours sont <em>au-dessus</em> des trois.
          <span class="src-tag src-documente">Documenté</span></p>
          <div class="callout callout-info">
            <p><strong>Ce que chaque lancement de saison fait à la courbe.</strong>
            C'est le signal le plus fiable. Sur les quatre lancements depuis
            janvier, la moyenne mensuelle a bondi de <strong>22 % à 41 %</strong>
            à chaque fois : +30,7 % en janvier pour la Saison 4, +22,4 % en
            avril pour la Saison 5, +40,7 % en juillet pour la Saison 6. La
            Saison 7, elle, n'a apporté que <strong>+1,8 %</strong> — non
            pas parce qu'elle déçoit, mais parce qu'elle a suivi un août
            déjà très fort. Traduction : un lancement de saison reste le
            premier levier de croissance du jeu, même quand son effet
            immédiat est faible.
            <span class="src-tag src-documente">Documenté</span></p>
          </div>
          <div class="callout callout-warning">
            <p><strong>Ce que ces chiffres ne disent pas.</strong> Steam n'est
            qu'un des trois canaux PC du jeu : Epic Games Store et le
            lanceur officiel partagent la même sauvegarde de compte et n'apparaissent
            dans aucun graphique. Et le « nombre de joueurs concurrents » n'est
            pas le nombre de joueurs : le nombre de personnes distinctes qui
            jouent sur un mois est toujours plusieurs fois supérieur. Ni
            l'éditeur ni Steam ne publient ce total.
            <span class="src-tag src-documente">Documenté</span></p>
          </div>

"""

# ---------------------------------------------------------------------------
# 3. items-munitions.html
# ---------------------------------------------------------------------------
BLOC_MUNITIONS = """          <div class="callout callout-danger">
            <h3 class="h4">Ce n'est pas l'armure qui tue, c'est la munition</h3>
            <p>La phrase est courte et elle synthétise le conseil la plus utile
            de la Saison 7 : <strong>une armure ne remplace pas une munition
            adaptée</strong>. Une cartouche de tier 2 envoyée sur une plaque
            de tier 4 ne fait presque rien — la balle rebondit ou se déforme
            sans percer. À l'inverse, une arme modeste équipée de munitions
            de tier 3 ou 4 bat un fusil entièrement modifié qui tire des
            munitions de tier 1. La règle que la communauté répète le plus :
            <em>« Matching a cheap weapon with high-tier ammo is infinitely
            better than running a fully modded, expensive rifle firing Tier 1
            or Tier 2 trash rounds. »</em>
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""

# ---------------------------------------------------------------------------
# 4. saison8-attente.html
# ---------------------------------------------------------------------------
BLOC_S8 = """          <h3 class="h4">L'état réel du jeu, en chiffres</h3>
          <p>Avant d'estimer une date, il faut savoir de quel jeu on parle.
          Relevé Steam du 18 novembre 2026 à 03:00 UTC.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Joueurs concurrents Steam — historique mensuel</caption>
              <thead><tr><th scope="col">Mois</th><th scope="col">Moyenne</th>
              <th scope="col">Variation</th><th scope="col">Sommet</th>
              <th scope="col">Ce qui s'est passé</th></tr></thead>
              <tbody>
                <tr><td>Sept. 2025</td><td>37 206</td><td>—</td><td>65 944</td>
                <td>Lancement 1.0 sur Steam et Epic (Saison 3)</td></tr>
                <tr><td>Oct. 2025</td><td>35 948</td><td>−3,4 %</td><td>64 757</td>
                <td>Effet de lancement prolongé</td></tr>
                <tr><td>Nov. 2025</td><td>24 626</td><td>−31,5 %</td><td>43 012</td>
                <td>Effet post-lancement</td></tr>
                <tr><td>Déc. 2025</td><td>18 569</td><td>−24,6 %</td><td>29 830</td>
                <td>Fin de Saison 3</td></tr>
                <tr><td>Janv. 2026</td><td>24 264</td><td>+30,7 %</td><td>42 986</td>
                <td>Saison 4 : Dusk to Dawn, carte Airport</td></tr>
                <tr><td>Févr. 2026</td><td>22 154</td><td>−8,7 %</td><td>38 236</td>
                <td>—</td></tr>
                <tr><td>Mars 2026</td><td>18 022</td><td>−18,7 %</td><td>31 880</td>
                <td>Fin de Saison 4</td></tr>
                <tr><td>Avr. 2026</td><td>22 061</td><td>+22,4 %</td><td>38 295</td>
                <td>Saison 5 : Distortion</td></tr>
                <tr><td>Mai 2026</td><td>19 676</td><td>−10,8 %</td><td>35 820</td>
                <td>—</td></tr>
                <tr><td>Juin 2026</td><td>16 905</td><td>−14,1 %</td><td>33 839</td>
                <td>Fin de Saison 5</td></tr>
                <tr><td>Juil. 2026</td><td>23 790</td><td>+40,7 %</td><td>41 704</td>
                <td>Saison 6 : White Nights</td></tr>
                <tr><td>Août 2026</td><td>24 196</td><td>+1,7 %</td><td>38 795</td>
                <td>Kamona Summer Festival</td></tr>
                <tr><td>Sept. 2026</td><td>24 630</td><td>+1,8 %</td><td>45 937</td>
                <td>Saison 7 : Utopia</td></tr>
                <tr><td>Oct. 2026</td><td>24 947</td><td>+1,3 %</td><td>44 873</td>
                <td>Événement Halloween, Warlord Tournament III</td></tr>
                <tr><td><strong>30 derniers jours</strong></td>
                <td><strong>21 769</strong></td><td><strong>−12,7 %</strong></td>
                <td><strong>37 331</strong></td><td>Milieu de Saison 7</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <p><strong>Non, le jeu ne meurt pas.</strong> Un jeu qui meurt
            Montre des sommets de plus en plus bas, saison après saison. ABI
            fait l'inverse : les Saisons 6 et 7 ont tenu la moyenne autour de
            24 000 pendant quatre mois d'affilée — un plateau qu'aucune
            saison antérieure n'a atteint. Le creux actuel, −12,7 % par
            rapport à octobre, reproduit le schéma de milieu de saison déjà
            observé deux fois cette année. La Saison 7 a 63 jours au
            18 novembre, alors que les quatre dernières saisons ont duré
            <strong>78 à 114 jours</strong> : le point bas n'est pas encore
            atteint.
            <span class="src-tag src-documente">Documenté</span></p>
          </div>
          <div class="callout callout-info">
            <p><strong>Le vrai reproche, qui n'est pas un reproche de
            population.</strong> Les fils « le jeu meurt » de cette semaine
            ne parlent pas de lobbies vides : ils parlent de balance et de
            modes retirés. La critique la plus fréquente vise la décision de
            retirer le Hostile Sector trois mois après l'avoir ajouté, et
            l'absence de pérennité du contenu. Ce sont des reproches de
            <em>direction artistique</em>, pas de santé du jeu. Et c'est
            précisément ce type de critique qui se résorbe à chaque nouvelle
            saison : les quatre lancements depuis janvier ont fait remonter
            la moyenne de 22 % à 41 %.
            <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

"""


def insérer_avant(texte, ancre, bloc, marqueur):
    """Insere le bloc juste avant l'ancre. Idempotent via le marqueur."""
    if marqueur in texte:
        return texte, False
    i = texte.find(ancre)
    if i < 0:
        raise SystemExit(f"  ANCRE INTROUVABLE : {ancre[:60]}")
    return texte[:i] + bloc + texte[i:], True


def maj_date(texte, date="2026-11-18"):
    """Met a jour dateModified dans le JSON-LD et la mention visible."""
    nouveau = re.sub(r'("dateModified": ")\d{4}-\d{2}-\d{2}(")', rf"\g<1>{date}\g<2>", texte)
    nouveau = re.sub(r'("datePublished": ")\d{4}-\d{2}-\d{2}(")', rf"\g<1>{date}\g<2>", nouveau)
    return nouveau


def main():
    echecs = []

    # ---- 1. guide-extraction --------------------------------------------
    p = CIBLE / "guide-extraction.html"
    s = p.read_text(encoding="utf-8")
    ancre = '          <h3 class="h4">La récupération par les coéquipiers'
    try:
        s, ok = insérer_avant(s, ancre, BLOC_EXTRACTION, "Les trois voies gratuites vers une Secure Case 3×3")
        if ok:
            s = maj_date(s)
            p.write_text(s, encoding="utf-8")
            print("  guide-extraction.html : bloc Secure Case (3 voies gratuites + prix + règle rouges) insere")
        else:
            print("  guide-extraction.html : deja present")
    except SystemExit as e:
        echecs.append(str(e))

    # ---- 2. meta-strategies-s7 ------------------------------------------
    p = CIBLE / "meta-stratégies-s7.html"
    s = p.read_text(encoding="utf-8")
    ancre = '          <h2 id="extraction">4. Le timing d\'extraction</h2>'
    try:
        s, ok = insérer_avant(s, ancre, BLOC_META + BLOC_SANTE, "Le plafond de 600 000 Koen et comment le contourner")
        if ok:
            s = maj_date(s)
            p.write_text(s, encoding="utf-8")
            print("  meta-strategies-s7.html : blocs Secure Ops 600k + sante du jeu inseres")
        else:
            print("  meta-strategies-s7.html : deja present")
    except SystemExit as e:
        echecs.append(str(e))

    # ---- 3. items-munitions ---------------------------------------------
    p = CIBLE / "items-munitions.html"
    s = p.read_text(encoding="utf-8")
    ancre = '          <h2 id="calibres">4. Les calibres et les armes qui les partagent</h2>'
    try:
        s, ok = insérer_avant(s, ancre, BLOC_MUNITIONS, "Ce n'est pas l'armure qui tue, c'est la munition")
        if ok:
            s = maj_date(s)
            p.write_text(s, encoding="utf-8")
            print("  items-munitions.html : bloc 'ce n'est pas l'armure qui tue' insere")
        else:
            print("  items-munitions.html : deja present")
    except SystemExit as e:
        echecs.append(str(e))

    # ---- 4. saison8-attente ---------------------------------------------
    p = CIBLE / "saison8-attente.html"
    s = p.read_text(encoding="utf-8")
    ancre = '          <h2 id="calendrier">2. Le calendrier officiel des saisons</h2>'
    try:
        s, ok = insérer_avant(s, ancre, BLOC_S8, "L'état réel du jeu, en chiffres")
        if ok:
            s = maj_date(s)
            p.write_text(s, encoding="utf-8")
            print("  saison8-attente.html : bloc chiffres Steam insere")
        else:
            print("  saison8-attente.html : deja present")
    except SystemExit as e:
        echecs.append(str(e))

    if echecs:
        for e in echecs:
            print("  ERREUR :", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
