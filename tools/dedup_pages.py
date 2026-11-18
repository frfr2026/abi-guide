#!/usr/bin/env python3
"""Cable chaque page sur un visuel JPG unique (artworks officiels du jeu).

Objectif : plus aucune image ne sert sur deux pages differentes.
Les favicons (img/ui/) et les images SEO/OG restent des exceptions
techniques documentees (une seule occurrence par page de toute façon).
"""
import re, pathlib, json

ROOT = pathlib.Path('.')

# page -> visuel unique a utiliser
PAGE_VISUAL = {
    'armes-carbine.html':      '../img/armes/vis-carbine.jpg',
    'armes-lmg.html':          '../img/armes/vis-lmg.jpg',
    'armes-pistolets.html':    '../img/armes/vis-pistolets.jpg',
    'armes-shotgun.html':      '../img/armes/vis-shotgun.jpg',
    'armes-sniper.html':       '../img/armes/vis-sniper.jpg',
    'armes-dmr.html':          '../img/armes/vis-dmr.jpg',
    'armes-smg.html':          '../img/armes/vis-smg.jpg',
    'armes-fusils-assaut.html': '../img/armes/vis-assaut.jpg',
    'armes-builds.html':       '../img/armes/vis-builds.jpg',
    'armes-attachements.html': '../img/armes/vis-attachements.jpg',
    'armes-nouveautes-s7.html': '../img/armes/vis-nouveautes.jpg',
    'armes-tier-list.html':    '../img/armes/vis-tierlist.jpg',
    'equipement-casques.html':  '../img/gear/vis-casques.jpg',
    'equipement-rigs.html':     '../img/gear/vis-rigs.jpg',
    'equipement-sacs.html':     '../img/gear/vis-sacs.jpg',
    'equipement-headsets.html': '../img/gear/vis-headsets.jpg',
    'items-cles.html':          '../img/items/vis-cles.jpg',
    'items-medical.html':       '../img/items/vis-medical.jpg',
    'items-munitions.html':     '../img/items/vis-munitions.jpg',
    'guide-craft.html':         '../img/items/vis-craft.jpg',
    'items-craft-workbench.html': '../img/items/vis-workbench.jpg',
    'items-collection-room.html': '../img/items/vis-collection.jpg',
    'items-koen-economy.html':  '../img/items/vis-koen.jpg',
    'items-valeur.html':        '../img/items/vis-valeur.jpg',
    'events-calendrier.html':   '../img/events/vis-calendrier.jpg',
    'events-supplies-drops.html': '../img/events/vis-supplies.jpg',
    'events-warlord-tournament.html': '../img/events/vis-warlord.jpg',
    'communaute-patch-notes.html': '../img/communaute/vis-patch.jpg',
    'communaute-ressources.html': '../img/communaute/vis-ressources.jpg',
    'communaute-streamers.html': '../img/communaute/vis-streamers.jpg',
    'cosmetiques-skins-perso.html': '../img/personnages/vis-opérateur.jpg',
    'cosmetiques-dog-tags.html': '../img/personnages/vis-dogtags.jpg',
    'meta-builds-roles.html':   '../img/meta/vis-builds.jpg',
    'meta-loadout-optimizer.html': '../img/meta/vis-optimizer.jpg',
    'meta-tier-list-globale.html': '../img/meta/vis-tierlist.jpg',
    'meta-stratégies-s7.html':  '../img/meta/vis-strategies.jpg',
    'univers-dark-zone.html':   '../img/univers/vis-darkzone.jpg',
    'univers-factions.html':    '../img/univers/vis-factions.jpg',
    'univers-lore.html':        '../img/univers/vis-lore.jpg',
    'saison7-zombie-infected-zone.html': '../img/zombies/vis-infected.jpg',
    'saison7-zombie-endless.html': '../img/zombies/vis-endless.jpg',
    'saison7-zombie-research.html': '../img/zombies/vis-research.jpg',
    'saison7-balance-changes.html': '../img/zombies/vis-balance.jpg',
}

# images de hero a remplacer sur les pages concernees
HERO_REPLACEMENT = {
    'img/hero/hero-armes.jpg': {
        'armes-carbine.html': 'img/armes/vis-carbine.jpg',
        'armes-lmg.html': 'img/armes/vis-lmg.jpg',
        'armes-pistolets.html': 'img/armes/vis-pistolets.jpg',
        'armes-shotgun.html': 'img/armes/vis-shotgun.jpg',
        'armes-sniper.html': 'img/armes/vis-sniper.jpg',
    },
    'img/hero/hero-armures.jpg': {
        'equipement-casques.html': 'img/gear/vis-casques.jpg',
        'equipement-headsets.html': 'img/gear/vis-headsets.jpg',
        'equipement-rigs.html': 'img/gear/vis-rigs.jpg',
        'equipement-sacs.html': 'img/gear/vis-sacs.jpg',
    },
}

IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)


def rewrite_page(path, replacements):
    """Remplace les src d'images selon un dict {ancien_src: nouveau_src}."""
    raw = path.read_text(encoding='utf-8')
    changed = [0]

    def sub_tag(m):
        tag = m.group(0)
        a = re.search(r'src\s*=\s*["\']([^"\']+)["\']', tag)
        if not a:
            return tag
        cur = a.group(1)
        # chemin relatif a la racine
        root_rel = str((path.parent / cur).resolve().relative_to(ROOT.resolve()))
        if root_rel in replacements:
            new = '../' + replacements[root_rel] if path.parent != ROOT else replacements[root_rel]
            tag = tag.replace('src="%s"' % cur, 'src="%s"' % new).replace(
                "src='%s'" % cur, "src='%s'" % new)
            changed[0] += 1
        return tag

    out = IMG_TAG.sub(sub_tag, raw)
    if changed[0]:
        path.write_text(out, encoding='utf-8')
    return changed[0]


total = 0
for page, vis in PAGE_VISUAL.items():
    p = ROOT / 'pages' / page
    if not p.exists():
        print('  ABSENT pages/%s' % page)
        continue
    n = rewrite_page(p, {})
    # remplace le premier <img> de contenu par le visuel unique
    raw = p.read_text(encoding='utf-8')
    # cible : toute image de contenu actuelle (hors ui/ et seo/)
    m = re.search(r'<img\b[^>]*src\s*=\s*["\']((?:\.\./)?img/(?!ui/|seo/)[^"\']+)["\'][^>]*>', raw, re.I)
    if m:
        old = m.group(1)
        raw = raw[:m.start()] + m.group(0).replace(old, vis) + raw[m.end():]
        p.write_text(raw, encoding='utf-8')
        total += 1
        print('  %-38s %-36s -> %s' % (page, old, vis))
    else:
        print('  %-38s (aucune image de contenu)' % page)

print('\nPages recablees : %d' % total)
