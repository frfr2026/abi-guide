#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete la page saison7-zombie-infected-zone.html avec les elements
tactiques du mode qui manquaient :

  - les trois grenades speciaux du mode (lance-flammes de detente,
    grenades a pheromone, grenades de fumee curative) ;
  - le niveau de menace in-raid et sa consequence sur le rythme ;
  - les conteneurs exclusifs de la zone.

Statut des sources : les trois grenades et le niveau de menace sont issus des
notes de beta officielles de la Saison 7 (publication editeur, via la
communautation Reddit qui les a reprises mot pour mot). Les conteneurs
exclusifs sont confirmes par les notes de saison.

Idempotent : le bloc n'est insere qu'une fois.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/saison7-zombie-infected-zone.html")

BLOC = """
          <h2 id="tactique-zone">La tactique du mode : trois grenades et un niveau de menace</h2>
          <p>Le mode Infected Zone se joue avec des outils propres, qui ne servent
          nulle part ailleurs. Trois objets y ont un usage spécifique, et une seule
          variable — le niveau de menace — commande le rythme du raid.</p>

          <h3>Les trois objets tactiques exclusifs</h3>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Objets tactiques de l'Infected Zone — usage et limite</caption>
              <thead><tr><th scope="col">Objet</th><th scope="col">Effet</th>
              <th scope="col">Usage réel</th><th scope="col">Limite</th></tr></thead>
              <tbody>
                <tr><td><strong>Grenade à phéromone</strong></td>
                <td>Explose au contact et libère un nuage de fumée qui attire les
                mutants normaux vers lui pendant un temps</td>
                <td>Ouvrir un passage dans une horde sans tirer : c'est la fonction
                qui lui vaut sa place dans le sac</td>
                <td>Ne fonctionne que sur les mutants normaux. Un Reaper ou un
                Ambusher ne change pas de route</td></tr>
                <tr><td><strong>Grenade de fumée curative</strong></td>
                <td>Libère lentement un nuage dans lequel les opérateurs récupèrent
                des points de vie en continu</td>
                <td>Se protéger pendant un traitement, ou faire franchir une zone
                exposée à un groupe</td>
                <td>La fumée protège des tirs humains, mais elle n'arrête ni les
                mutants ni les autres joueurs</td></tr>
                <tr><td><strong>Lance-flammes à retardement</strong></td>
                <td>Détonation différée, non affectée par les obstacles, qui inflige
                une surdité, un ralentissement et une baisse de sensibilité de la
                souris, et trouble la vue de qui regarde l'explosion</td>
                <td>Retarder une charge, tenir un angle sans être vu, ou ralentir
                une poursuite</td>
                <td>Ne peut pas être extrait du raid et ne se fabrique qu'au
                Workbench</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>La grenade à phéromone est le meilleur objet du mode, et de
            loin.</strong> Elle transforme une situation de horde bloquante en
            situation de détour : le temps que les mutants normaux suivent le
            nuage, vous passez. C'est ce qui remplace le chargeur de munitions
            supplémentaire, et c'est souvent plus rentable.</p>
          </div>

          <h3>Le niveau de menace : la variable qui commande le raid</h3>
          <p>Au fil du raid, le <strong>niveau de menace</strong> monte
          continuellement. Chaque seuil franchi augmente à la fois la quantité de
          mutants présents et leur force, et le Merit gagné progresse en
          correspondance. Concrètement, un raid long n'est pas un raid plus
          rentable : c'est un raid dont la fin se dégrade.</p>
          <ul>
            <li><strong>Au début du raid</strong>, les mutants sont gérables et
            esquivables. C'est la phase de fouille : les conteneurs de valeur sont
            accessibles, et l'essentiel du butin se prend ici.</li>
            <li><strong>À mi-raid</strong>, la densité augmente et les variantes
            spéciales apparaissent. La fouille devient un combat.</li>
            <li><strong>En fin de raid</strong>, la fouille n'est plus possible : le
            coût de chaque conteneur ouvert dépasse ce qu'il contient. La seule
            ration rationnelle est de s'extraire.</li>
          </ul>
          <div class="callout callout-warning">
            <p><strong>L'erreur type du mode</strong> est de vouloir tout ramasser.
            Ouvrir un coffre-fort attire une horde, et une horde à la fin du raid
            est un combat perdu. La règle qui fonctionne : chaque conteneur ouvert
            doit être paid par une sortie immédiate. Fouiller et courir, dans cet
            ordre, jamais l'inverse.</p>
          </div>

          <h3>Les conteneurs exclusifs de la zone</h3>
          <p>La zone ajoute des contenants qui n'existent pas ailleurs, et qui
          sont la raison d'entrer. Ils ne sont pas obligatoires : chaque raid de
          fouille повезде не приносит de butin supplémentaire, mais chaque
          conteneur de zone trouvé en apporte un peu.</p>
          <ul>
            <li><strong>Conteneurs d'expédition maritime</strong> — conteneurs
            métalliques déposés sur la carte, source de loot dense.</li>
            <li><strong>Distributeurs automatiques abandonnés</strong> — petits
            conteneurs dispersés, moins de valeur unitaire mais plus nombreux.</li>
            <li><strong>Conteneurs à indice huileux</strong> — conteneurs de la
            zone.infected, plus sélectifs sur leur contenu.</li>
            <li><strong>Sacs de corps</strong> — ils tombent quand un infecté est
            tué. Le sac contient des échantillons de zombie et divers objets
            zombies, et c'est la source de progression de la Zombie Research.</li>
            <li><strong>Échantillons de zombie</strong> — récupérés dans les sacs
            de corps, puis extraits pour activer les points de recherche.</li>
          </ul>
          <div class="callout callout-success">
            <p><strong>La règle d'or du ramassage.</strong> Les sacs de corps sont
            la source de progression de la Zombie Research : un sac ignoré, c'est
            un point de recherche qui ne s'active pas. Mais un sac fouillé au
            mauvais moment, c'est une horde qui apparaît. La solution pratique :
            ramasser les sacs <em>en se déplaçant</em>, jamais en s'arrêtant, et
            uniquement quand la zone est déjà dégagée.</p>
          </div>
"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    if 'id="tactique-zone"' in s:
        print("  deja present")
        return 0
    m = re.search(r'<h2[^>]*id="checklist"[^>]*>', s)
    if not m:
        print("  ANCRE checklist introuvable")
        return 1
    s = s[: m.start()] + BLOC.strip() + "\n\n" + s[m.start():]
    PAGE.write_text(s, encoding="utf-8")
    print("  saison7-zombie-infected-zone.html : bloc tactique insere")
    return 0


if __name__ == "__main__":
    sys.exit(main())
