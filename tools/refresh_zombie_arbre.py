#!/usr/bin/env python3
"""Complete l'arbre Zombie Research et les nouveaux conteneurs S7.

Trois pages sont concernees :

  - pages/saison7-zombie-research.html : les 7 passifs nommes de l'arbre
    (Melee Mastery, Undying Spirit, Pain Killer, Sustained Combat,
    Sample Identification, Vending Machine Hunter, Hyper Intuition), avec
    l'effet exact de chacun, et le fait que le boss d'Airport garantit un
    echantillon Gold ;
  - pages/saison7-zombie-infected-zone.html : les conteneurs et objets
    introduits en S7 — Signal Gun, distributeurs, missions urgentes, Flesh
    Growths, mutation traces et bio-echantillons ;
  - pages/map-no-mans-land.html : le detail du mode PvE a tickets (balles T3,
    bio-echantillons, plans de workbench).

Source : base de reference communautaire (abibuilder.com/guides/s7-loot-guide).
Donnee documentee et recoupree, non publiee par l'editeur.

Idempotent.
"""
import pathlib

# ── 1. arbre de recherche ────────────────────────────────────────────────
RESEARCH = '''          <h3 class="h4">Les sept passifs de l'arbre, un par un</h3>
          <p>L'arbre n'affiche pas que des nombres : sept de ses branches ont un <strong>nom</strong> et un
          <strong>effet identifiable</strong>. Ce sont eux qui décident de la forme d'un raid, pas le level up
          générique.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th scope="col">Passive</th><th scope="col">Ce qu'elle change</th><th scope="col">Priorité</th></tr></thead>
              <tbody>
                <tr>
                  <td><strong>Melee Mastery</strong></td>
                  <td>Augmente les <strong>dégâts de corps à corps contre les zombies</strong>. Permet de les eliminer en silence, sans gaspiller de munitions.</td>
                  <td>Élevée — en raid où vous avez marqué des munitions T5, chaque balle zombie gaspillée se compte.</td>
                </tr>
                <tr>
                  <td><strong>Undying Spirit</strong></td>
                  <td>Rend une partie de votre <strong>endurance</strong> à chaque zombie tué. Vous nettoyez une horde sans être à sec.</td>
                  <td>Moyenne — se combine naturellement avec Melee Mastery.</td>
                </tr>
                <tr>
                  <td><strong>Pain Killer</strong></td>
                  <td>Réduit les dégâts subis des zombies. Les zombies qui <strong>bondissent et crachent</strong> vident la barre de vie très vite : ici, vous ne prenez presque rien.</td>
                  <td>Élevée en Heavy Infected Zone.</td>
                </tr>
                <tr>
                  <td><strong>Sustained Combat</strong></td>
                  <td>Tuer des zombies <strong>rend une partie de votre santé manquante</strong>. Se battre contre de grandes hordes finit toujours par faire mal : cette branche compense avant que le médical ne prenne le relais.</td>
                  <td>Moyenne.</td>
                </tr>
                <tr>
                  <td><strong>Sample Identification</strong></td>
                  <td>Augmente <strong>directement</strong> vos chances de trouver des objets rouges dans les conteneurs zombies.</td>
                  <td><strong>La première à débloquer</strong> si votre objectif est le revenu.</td>
                </tr>
                <tr>
                  <td><strong>Vending Machine Hunter</strong></td>
                  <td>Ajoute une chance que les <strong>distributeurs</strong> lâchent des objets de valeur. Les machines ne servent qu'au premier joueur qui les utilise : c'est un passif de vitesse, pas de farm.</td>
                  <td>Élevée si vous ouvrez les distributeurs en premier.</td>
                </tr>
                <tr>
                  <td><strong>Hyper Intuition</strong></td>
                  <td>Vous permet de <strong>voir les traces de mutation sur la carte</strong>. En les suivant, vous menez aux récompenses cachées.</td>
                  <td>Élevée — c'est la clé des bio-échantillons.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : base de référence communautaire, guide loot et progression S7
          (abibuilder.com/guides/s7-loot-guide). Donnée documentée, non publiée par l'éditeur.</p>

          <div class="callout callout-success">
            <h3 class="h4">L'échantillon Gold garanti</h3>
            <p>Les échantillons zombies se trouvent dans les <strong>coffres zombies</strong>, les
            <strong>conteneurs zombies</strong> et les <strong>Flesh Growths</strong> (croûtes de chair qui
            poussent sur les murs et le sol). Mais il y a une source garantie : <strong>descendre le boss
            d'Airport garantit un échantillon de niveau Gold</strong>. C'est le seul point du jeu où le loot
            facial est garanti, et cela vaut un raid à lui seul quand on cherche à monter l'arbre vite.</p>
          </div>
'''

# ── 2. nouveaux conteneurs de la zone infectee ───────────────────────────
CONTAINERS = '''          <h3 class="h4">Les conteneurs et objets introduits en S7</h3>
          <p>La Saison 7 n'a pas seulement ajouté des zombies : elle a ajouté des <strong>conteneurs</strong>,
          et ce sont eux qui ont changé le rendement de la zone. Un raid sans en ouvrir un seul est un raid
          raté.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th scope="col">Élément</th><th scope="col">Où</th><th scope="col">Ce qu'il faut savoir</th></tr></thead>
              <tbody>
                <tr>
                  <td><strong>Signal Gun</strong></td>
                  <td>Exclusif de la <strong>Heavy Infected Zone</strong>, trouvé dans des conteneurs aléatoires.</td>
                  <td>On la tire en l'air pour <strong>appeler une parachutiste sur votre position</strong>. La caisse a <strong>4 compartiments</strong>, et <strong>chacun peut contenir un objet rouge</strong>. Contrepartie : la zone d'atterrissage se voit de loin. Utilisez-la <strong>seulement</strong> dans un coin dégagé.</td>
                </tr>
                <tr>
                  <td><strong>Distributeurs</strong></td>
                  <td>Sur la carte, dans les zones bâties.</td>
                  <td>Nouveauté S7 : ils donnent de la <strong>nourriture</strong>. Sans passif, c'est de la bouffe ; avec <strong>Vending Machine Hunter</strong>, ils lâchent des objets de valeur. Comme seule la première personne qui les utilise en profite, c'est une course.</td>
                </tr>
                <tr>
                  <td><strong>Missions urgentes</strong></td>
                  <td>Visibles sur la carte, <strong>par tous les joueurs</strong> de la Heavy Infected Zone.</td>
                  <td>Elles paient en <strong>caisses de loot</strong> et en <strong>grandes caisses de loot</strong>. La grande caisse donne <strong>deux chances de fouille à chaque membre de l'escouade</strong> — le butin se partage, mais la fouille, non.</td>
                </tr>
                <tr>
                  <td><strong>Flesh Growths</strong></td>
                  <td>Sur les murs et le sol, en fouillant.</td>
                  <td>Contenants de la S7. Ils peuvent contenir des <strong>passes No Man's Land</strong>, utilisables pour entrer dans le mode PvE. Si le mode ne vous intéresse pas, ces passes se vendent directement pour <strong>500 000 Koen</strong> chacun.</td>
                </tr>
                <tr>
                  <td><strong>Traces de mutation</strong></td>
                  <td>Partout sur la carte, mais <strong>invisibles par défaut</strong>.</td>
                  <td>Une trace seule ne donne rien. Avec <strong>Hyper Intuition</strong>, vous voyez des <strong>empreintes bleues</strong> qui en partent : suivez-les, elles mènent au <strong>bio-échantillon</strong>.</td>
                </tr>
                <tr>
                  <td><strong>Bio-échantillon</strong></td>
                  <td>Au bout des traces de mutation.</td>
                  <td>Son <strong>tableau de loot est comparable à celui d'un petit coffre</strong>. C'est la principale source d'échantillons zombies, donc la principale voie de progression de l'arbre.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : base de référence communautaire, guide loot et progression S7
          (abibuilder.com/guides/s7-loot-guide). Donnée documentée, non publiée par l'éditeur.</p>

          <div class="callout callout-danger">
            <h3 class="h4">L'erreur de parcours la plus fréquente</h3>
            <p>Passer devant une <strong>Flesh Growth</strong> sans la fouiller. Ces croûtes de chair sont
           drues, mais elles contiennent potentiellement un passe No Man's Land, c'est-à-dire 500 000 Koen ou
            un accès gratuit au mode PvE. De même, ignorer les <strong>missions urgentes</strong> : elles sont
            publiques, donc quelqu'un d'autre les fera si vous ne le faites pas.</p>
          </div>
'''

# ── 3. No Man's Land ─────────────────────────────────────────────────────
NML = '''          <h3 class="h4">Comment on s'y prend concrètement</h3>
          <p>Le mode a été entièrement simplifié par rapport au Hostile Sector de S6. Les <strong>scavs sont
          très mauvais tireurs et infligent très peu de dégâts</strong> : la seule chose qui vous pose vraiment
          problème, ce sont les hordes de zombies.</p>
          <ul>
            <li><strong>Ball ammunition : 120 à 180 balles de T3</strong> suffisent. Si vous avez investi dans l'arbre de recherche, ce nombre peut être encore plus bas. La munitions T5 y est du gaspillage pur.</li>
            <li><strong>Votre cible principale : les bio-échantillons.</strong> Leur qualité de loot est comparable à celle d'un petit coffre, et ils contiennent des objets de valeur ou des échantillons purs pour l'arbre.</li>
            <li><strong>Sans Hyper Intuition, les trouver est laborieux.</strong> Le passif vous montre les empreintes bleues ; il transforme un raid en fouille aléatoire.</li>
            <li><strong>Les caisses de mission donnent des échantillons supplémentaires</strong> et de l'équipement de valeur : terminez-les, elles paient.</li>
            <li><strong>Les boîtes à documents et les tiroirs de bureau contiennent les plans du workbench.</strong> Si vous enlistez pour le craft, c'est là qu'ils sont.</li>
            <li><strong>Le taux de loot global est proche de celui du mode Lockdown</strong>. Vous pouvez utiliser des clés, mais rien ne garantit un objet de valeur : le mode est calme, pas généreux.</li>
          </ul>
          <p class="small text-muted">Source : base de référence communautaire, guide loot et progression S7
          (abibuilder.com/guides/s7-loot-guide). Donnée documentée, non publiée par l'éditeur.</p>
'''

# (fichier, ancre de la section h2 qui doit SUIVRE le bloc insere, bloc)
JOBS = [
    ('pages/saison7-zombie-research.html', 'ordre', RESEARCH),
    ('pages/saison7-zombie-infected-zone.html', 'events', CONTAINERS),
    ('pages/map-no-mans-land.html', 'rendement', NML),
]

for path, next_anchor, block in JOBS:
    p = pathlib.Path(path)
    s = p.read_text(encoding='utf-8')
    if 's7-loot-guide' in s:
        print('  deja enrichi :', path)
        continue
    i = s.find('id="%s"' % next_anchor)
    assert i > 0, path
    j = s.rfind('<h2 ', 0, i)
    assert j > 0, path
    s = s[:j] + block.strip() + '\n\n' + s[j:]
    p.write_text(s, encoding='utf-8')
    print('  %-42s enrichi (avant #%s)' % (path, next_anchor))
