#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige le bloc perime de tools/refresh_veille_oct2026.py.

Ce script ne modifie QUE tools/refresh_veille_oct2026.py. Il ne touche
pas au site. Le bloc vise decrit une "assurance" avec remboursement
conditionnel, fichiers chiffres exclus et primes : ce sont des
mecaniques du jeu MOBILE Arena Breakout, pas d'ABI Infinite.

La position officielle d'ABI Infinite, desormais exposee dans
pages/guide-extraction.html, est : il n'y a pas d'assurance. Ce que
vous perdez est perdu, sauf ce qui est place dans un emplacement
protege ou recupere par un coequiperier.

Ce correctif empeche la reintroduction de la contradiction si le
script de veille d'octobre est rejoue un jour.

Idempotent.
"""
import pathlib
import sys

CIBLE = pathlib.Path("tools/refresh_veille_oct2026.py")

NOUVEAU = """          <h2 id="conteneur-assurance">Conteneur sécurisé : ce qui survit à la mort</h2>
          <p>Quand vous mourez en raid, vous perdez tout ce que vous aviez
          emporté et tout ce que vous aviez trouvé — à deux exceptions près. Ces
          deux exceptions sont les seuls amortisseurs de risque du jeu, et elles
          sont très mal utilisées.</p>

          <h3>Le conteneur sécurisé : une seule chose survit</h3>
          <p>Le conteneur sécurisé, parfois appelé poche, garde un seul objet
          même si vous mourez. Sa taille est un choix : il existe en
          <strong>1×2, 2×2, 2×3</strong> et <strong>3×3</strong>. Le format 3×3
          est une récompense saisonnière : on l'obtient en remplissant les
          missions de la saison, et il ne reste valable que le temps de cette
          saison.</p>
          <ul>
            <li><strong>Ce qu'on y met</strong> : vos munitions les plus chères,
            un objet de valeur inestimable, ou une clé que vous n'avez pas les
            moyens de racheter.</li>
            <li><strong>Ce qu'on n'y met pas</strong> : une arme entière. La
            place vaut plus que la valeur d'une arme, et l'arme peut être
            reconstruite.</li>
            <li><strong>Le verrou Tactical Ops</strong> : un objet marqué
            « Tactical Ops locked » ne peut pas être placé dans le conteneur
            avant votre première extraction réussie avec lui. Le symbole de
            boîte apparaît sur l'objet une fois cette condition remplie.</li>
          </ul>

          <h3>Il n'y a pas d'assurance : ce qu'il faut savoir à la place</h3>
          <p><strong>ABI Infinite n'a pas de système d'assurance.</strong> C'est
          la position officielle, et elle est explicite : « insurance does not
          exist, what you lose is gone unless recovered manually ». Tout ce que
          vous portez hors d'un emplacement protégé est perdu sans
          contrepartie. Les guides qui décrivent un « remboursement
          conditionnel », un « remboursement si aucun joueur adverse n'a
          extrait votre arme assurée » ou des « fichiers chiffrés exclus de la
          couverture » décrivent une mécanique qui n'existe pas dans le jeu PC :
          ce sont les règles du jeu mobile Arena Breakout.
          <span class="src-tag src-documente">Documenté</span></p>
          <div class="callout callout-warning">
            <p><strong>Les quatre vrais filets de sécurité, à leur place.</strong>
            <strong>1. La Secure Case</strong> — un conteneur à grille loué en
            Bonds qui conserve son contenu même à la mort ; les munitions de
            haut tier en sont exclues par une règle de Saison 6. <strong>2. Le
            coéquipier</strong> — s'il sort vivant avec votre stuff, il vous le
            renvoie par la messagerie du jeu. <strong>3. Le Supplies Retrieval
            Device</strong> — expédié après le raid. <strong>4. Secure Ops</strong>
            — le mode où un échec ne coûte aucun équipement. En dehors de ces
            quatre voies, ce que vous perdez est perdu.
            <span class="src-tag src-documente">Documenté</span></p>
          </div>
          <p>La règle d'usage rationnelle est simple : mettez dans la Case ce qui
          est coûteux à remplacer, et laissez le reste. Couvrir un kit de raid
          complet revient à payer une prime qui dépasse souvent la marge
          disponible — à ce stade-là, mieux vaut réduire la valeur du kit que de
          tenter de le couvrir.</p>
"""


def main():
    s = CIBLE.read_text(encoding="utf-8")
    if "Il n'y a pas d'assurance : ce qu'il faut savoir à la place" in s:
        print("  deja corrige")
        return 0

    debut = s.find('          <h2 id="conteneur-assurance">')
    if debut < 0:
        print("  ANCRE introuvable")
        return 1
    i = s.find("couvrir.</p>", debut)
    fin = s.find('"""', i)
    if fin < 0:
        print("  FIN de bloc introuvable")
        return 1
    # conserver l'indentation de fin de bloc
    s = s[:debut] + NOUVEAU + s[fin:]
    CIBLE.write_text(s, encoding="utf-8")
    print("  refresh_veille_oct2026.py : bloc assurance corrige (position officielle)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
