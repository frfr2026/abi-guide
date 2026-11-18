#!/usr/bin/env python3
"""Detaille les Core Masteries S7 dans pages/guide-progression.html.

Le site ne donnait qu'un tableau de trois lignes, avec des formulations
imprecises ("Compartiment cache dans l'inventaire : du loot securise
supplementaire") qui ne disent pas ce que fait reellement la maitrise.

La regle reelle de la S7 : on choisit UNE core mastery parmi trois, en plus
des 12 points de maitrise ordinaires. Les effets precis sont documentes par la
base de reference communautaire (abibuilder.com/guides/s7-loot-guide) :

  - Acoustic Earpads  : reduit l'effet d'obstruction sonore des casques qui ne
                        supportent pas de casque audio, +10 a 15 m de portee
                        auditive ;
  - Tactical Belt     : quatre poches 1x1 supplementaires (grenades, medical) ;
  - Hidden Compartment: deverrouille les compartiments caches des conteneurs,
                        soit une tentative de fouille supplementaire.

Les deux montages de maitrise publies (PvP et economie) sont donnes avec
leurs niveaux exacts.

Idempotent.
"""
import pathlib

P = pathlib.Path('pages/guide-progression.html')
s = P.read_text(encoding='utf-8')

if 'masteries-detail' in s:
    print('deja enrichi')
    raise SystemExit(0)

OLD = """          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Mastery</th><th>Effet gameplay</th></tr></thead>
              <tbody>
                <tr><td><strong>Acoustic Earpads</strong></td><td>Neutraliser les pics sonores (grenades, tirs) : garder les informations dans le bruit</td></tr>
                <tr><td><strong>Tactical Belt</strong></td><td>Slots de ceinture supplémentaires : plus de meds et de munitions à portée</td></tr>
                <tr><td><strong>Hidden Compartment</strong></td><td>Compartiment caché dans l'inventaire : du loot sécurisé supplémentaire en raid</td></tr>
              </tbody>
            </table>
          </div>"""

NEW = """          <div class="callout callout-info" id="masteries-detail">
            <h3 class="h4">La règle d'abord : une seule, parmi trois</h3>
            <p>La Saison 7 introduit les <strong>core masteries</strong>. Ce n'est pas une catégorie de points
            à distribuer : c'est <strong>un choix unique</strong>. Vous pickez <strong>une</strong> des trois core
            masteries, et elle s'ajoute à vos <strong>12 points de maîtrise ordinaires</strong>. Pas les trois à la
            fois, pas une par saison : une seule, et elle vaut dans tous les modes où elle s'applique.</p>
            <p>Concrètement, c'est ce qui change votre façon de charger un raid. Les trois ne répondent pas au même
            problème — l'une gagne des duels, l'autre gagne des extractions, la troisième gagne de l'argent.</p>
          </div>

          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th scope="col">Core mastery</th><th scope="col">Ce qu'elle fait réellement</th><th scope="col">Elle vaut si…</th></tr></thead>
              <tbody>
                <tr>
                  <td><strong>Acoustic Earpads</strong></td>
                  <td>Réduit l'<strong>effet d'obstruction sonore des casques qui ne supportent pas un casque audio</strong>, et rend environ <strong>10 à 15 mètres</strong> de portée auditive supplémentaire.</td>
                  <td>Vous jouez en large, sur Northridge, Valley ou Airport, et vous comptez sur l'oreille autant que sur le viseur.</td>
                </tr>
                <tr>
                  <td><strong>Tactical Belt</strong></td>
                  <td>Ajoute <strong>quatre poches 1×1</strong> : quatre emplacements de plus pour des grenades ou du médical, en plus de votre gilet et de votre rig.</td>
                  <td>Vous vous battez en intérieur serré, sur Armory en particulier, où la grenade décide du round.</td>
                </tr>
                <tr>
                  <td><strong>Hidden Compartment</strong></td>
                  <td><strong>Déverrouille les compartiments cachés</strong> des conteneurs : cela vous donne une <strong>tentative de fouille supplémentaire</strong>.</td>
                  <td>Vous farm. C'est la maîtrise qui rapporte de l'argent, et elle rapporte d'autant plus qu'il y a de conteneurs sur votre route.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : base de référence communautaire, guide loot et progression S7
          (abibuilder.com/guides/s7-loot-guide). Donnée documentée, non publiée par l'éditeur.</p>

          <h3 class="h4">Les montages qui marchent, avec leurs niveaux exacts</h3>
          <p>Les core masteries ne servent à rien si les points de maîtrise ordinaires qui les accompagnent sont
          distribués au hasard. Deux montages sont documentés, et ils répondent à deux objectifs opposés. Le
          principe est le même dans les deux cas : <strong>tout mettre au niveau 3</strong>, parce qu'un niveau 2
          ne donne presque rien.</p>

          <div class="grid grid--2">
            <article class="card">
              <div class="card-body">
                <h3 class="h4">Montage PvP — gagner les duels</h3>
                <ul>
                  <li><strong>FOCUS PULLER (niveau 3)</strong> — <strong>+18 %</strong> de vitesse de peek gauche et droite. Dans un couloir étroit, 18 % de millisecondes suffisent à voir l'angle en premier.</li>
                  <li><strong>SLEIGHT OF HAND (niveau 3)</strong> — permet de recharger un chargeur de 100 balles en <strong>26 secondes</strong>, soit <strong>+27 %</strong> de vitesse de rechargement.</li>
                  <li><strong>HEAVY MOTOR (niveau 3)</strong> — réduit de <strong>35 %</strong> le ralentissement de déplacement imposé par les casques et les armures.</li>
                  <li><strong>PORTER (niveau 3)</strong> — augmente directement la limite de poids de <strong>10 kg</strong>.</li>
                  <li><strong>ACOUSTIC EARPADS</strong> — la core mastery, qui réduit l'obstruction sonore des casques.</li>
                </ul>
              </div>
            </article>
            <article class="card">
              <div class="card-body">
                <h3 class="h4">Montage économie — maximiser le gain</h3>
                <ul>
                  <li><strong>PORTER (niveau 3)</strong> — <strong>+10 kg</strong> de limite de poids, qui protège de la zone de pénalité jaune quand on charge un peu de loot.</li>
                  <li><strong>EFFECTIVE LOOTING (niveau 3)</strong> — <strong>20 %</strong> de chance de passer directement la phase de fouille à l'ouverture d'un conteneur.</li>
                  <li><strong>VINSON'S FRIEND I (niveau 3)</strong> — <strong>10 %</strong> de chance de <strong>récupérer votre arme</strong> même si vous échouez à l'extraction.</li>
                  <li><strong>EMERGENCY EVASION (niveau 3)</strong> — utile pour se replier et se remettre rapidement après une embuscade.</li>
                  <li><strong>HIDDEN COMPARTMENT</strong> — la core mastery, pour maximiser le loot et trouver les objets cachés.</li>
                </ul>
              </div>
            </article>
          </div>

          <div class="callout callout-success">
            <h3 class="h4">Le point qui décide de tout : l'unique exception</h3>
            <p><strong>Vinson's Friend I mérite un cas à part.</strong> C'est la seule maîtrise du jeu qui
            s'applique <strong>quand vous perdez</strong> : elle vous rend une chance de récupérer votre arme
            même en cas d'échec d'extraction. Sur une arme à 300 000 K, 10 % de chance de la sauver, c'est
            30 000 K d'assurance par raid. Aucun autre point de maîtrise ne protège votre stuff comme ça.</p>
          </div>"""

assert OLD in s, 'tableau des core masteries introuvable'
s = s.replace(OLD, NEW, 1)

P.write_text(s, encoding='utf-8')
print('pages/guide-progression.html : core masteries detaillees')
