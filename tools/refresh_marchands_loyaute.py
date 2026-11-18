#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete la section Field Merchants de pages/guide-traders.html avec trois
elements qui manquaient :

  1. le systeme de fidelite du marchand (de Stern a Enthusiastic) et les
     seuils qui debloquent l'intel ;
  2. l'indice sonore qui permet d'identifier la valeur d'un mystery cargo
     avant de l'ouvrir ;
  3. les limites d'achat specifiques au mode (deux achats de mystery cargo
     par raid en Tactical Ops, trois ventes).

Statut des sources : le mecanisme de fidelite et l'indice sonore sont
rapportes par des sources communautaires et recoupes entre elles ; ils sont
donc presentes comme des indications de terrain, pas comme des regles
officielles. Les limites d'achat proviennent des notes de saison.

Idempotent : le bloc n'est insere qu'une fois.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/guide-traders.html")

BLOC = """
          <h3 id="fidelite-marchand">La fidélité : de « severe » à « enthousiaste »</h3>
          <p>Le Field Merchant ne traite pas tous les opérateurs de la même façon.
          Son attitude dépend du <strong>volume cumulé de transactions</strong> que
          vous avez réalisé avec lui. Le point de départ est <em>severe</em>, et
          l'attitude s'améliore au fil des raids jusqu'à <em>enthousiaste</em>.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Le palier de fidélité et ce qu'il débloque</caption>
              <thead><tr><th scope="col">Palier</th><th scope="col">Ce qu'il change</th>
              <th scope="col">Comment y aller</th></tr></thead>
              <tbody>
                <tr><td><strong>Severe</strong></td>
                <td>Le marchand accepte de commercer, mais ne dit rien sur la valeur
                des cargaisons</td>
                <td>Le point de départ : vous n'avez jamais échangé</td></tr>
                <tr><td><strong>Neutre</strong></td>
                <td>Quelques indices d'information sur la région et sur les cargaisons</td>
                <td>Quelques raids réguliers de vente de surplus</td></tr>
                <tr><td><strong>Amical</strong></td>
                <td>Plus d'intel exploitable, notamment sur la valeur des cargaisons
                de la zone</td>
                <td>Un volume de transactions cumulé significatif</td></tr>
                <tr><td><strong>Enthousiaste</strong></td>
                <td>Le palier haut : l'intel devient exploitable avant l'achat
                coûteux</td>
                <td>La régularité sur plusieurs saisons, pas un raid isolé</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>La règle d'or du marchand.</strong> Vendre d'abord, acheter
            ensuite. Chaque vente libère de l'espace dans le sac <em>et</em> fait
            monter votre palier de fidélité, ce qui est précisément ce qui rend
            l'achat intelligent possible. Le cercle est vertueux : on vend pour
            pouvoir acheter en connaissance de cause.</p>
          </div>
          <div class="callout callout-warning">
            <p><strong>Statut de ce tableau :</strong> les paliers de fidélité et leur
            intitulé exact circulent sous la forme de retours de joueurs ; ils sont
            recoupés par plusieurs sources indépendantes, mais ils ne figurent pas
            dans les notes de saison publiées. Ce sont donc des <em>indications de
            terrain</em>, pas des règles officielles. Ce qui est officiel, c'est le
            principe : plus vous échangez, plus le marchand vous renseigne.</p>
          </div>

          <h3 id="indice-sonore">L'indice sonore : identifier une cargaison sans l'ouvrir</h3>
          <p>Une cargaison mystère produit, au moment où vous la déplacez dans
          l'interface d'achat, un son qui correspond à ce qu'elle contient. Ce n'est
          pas une mention de l'éditeur mais une observation reproductible, et c'est
          de loin le mécanisme le plus rentable du Field Merchant pour qui veut
          acheter cher.</p>
          <ul>
            <li><strong>Les sons « certain »</strong> : certains objets ont une
            signature sonore unique et sans équivalent. Les presence d'un lion doré,
            d'un vase, d'une théière ou d'un collier sont des indicateurs forts.</li>
            <li><strong>Les sons « au moins »</strong> : d'autres sons correspondent à
            des objets de valeur au moins moyenne, sans être uniques. Ils indiquent
            un bon placement, pas un jackpot.</li>
            <li><strong>Le format de la cargaison</strong> : la taille affichée de la
            cargaison donne une information supplémentaire. Certaines dimensions
            sont statistiquement associées à des contenus plus élevés.</li>
          </ul>
          <div class="callout callout-success">
            <p><strong>La conséquence pratique.</strong> Un son unique vous donne
            une cargaison quasi certaine. Un son correspondant à un objet de valeur
            au moins moyenne vous donne une cargaison rentable, même si le résultat
            final reste variable. Le seul cas où vous devez vraiment hésiter, c'est
            l'absence d'indice : c'est le moment de passer votre chemin.</p>
          </div>
          <p>Les limites d'achat ajoutent une contrainte supplémentaire : en Tactical
          Ops, l'achat de cargaisons mystère est plafonné à <strong>deux par raid</strong>,
          et la vente à <strong>trois opérations</strong>. La rareté du marchand en
          raid — il n'apparaît qu'après un certain délai, et pas dans toutes les
          parties — transforme chaque négociation en décision à faible nombre de
          tirages : mieux vaut une bonne cargaison chanceuse qu'une mediocre.</p>
"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    if 'id="fidelite-marchand"' in s:
        print("  deja present")
        return 0
    m = re.search(r'<h2[^>]*id="erreurs"[^>]*>', s)
    if not m:
        print("  ANCRE erreurs introuvable")
        return 1
    s = s[: m.start()] + BLOC.strip() + "\n\n" + s[m.start():]
    PAGE.write_text(s, encoding="utf-8")
    print("  guide-traders.html : bloc fidelite insere")
    return 0


if __name__ == "__main__":
    sys.exit(main())
