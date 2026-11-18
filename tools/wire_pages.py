#!/usr/bin/env python3
"""Câblage final : chaque page reçoit des visuels uniques (artworks officiels
et recadrages dérivés), et chaque image n'apparait plus que sur une page.

Le catalogue JSON (data-weapons / data-armors / data-items / data-maps)
n'est pas modifie : ce sont les images des ENTITES, uniques par nature.
Les visuels de page (heroes, vignettes) sont eux dedoublonnes.
"""
import re, pathlib, json

ROOT = pathlib.Path('.')

# ---------------------------------------------------------------------------
# 1. Remplacement des visuels de page partages
# ---------------------------------------------------------------------------
# (page, ancien_src, nouveau_src)
REPL = [
    # --- accueil : les vignettes "categorie" doivent differer des pages cibles
    ('index.html', 'img/hero/hero-armes.jpg', 'img/cards/card-arms.jpg'),
    ('index.html', 'img/hero/hero-armures.jpg', 'img/cards/card-armor.jpg'),
    ('index.html', 'img/hero/hero-meta.jpg', 'img/cards/card-meta.jpg'),
    ('index.html', 'img/hero/hero-meta.jpg', 'img/cards/card-meta2.jpg'),
    ('index.html', 'img/hero/hero-meta.jpg', 'img/cards/card-meta3.jpg'),
    ('index.html', 'img/hero/hero-saison7.jpg', 'img/cards/card-saison7.jpg'),
    ('index.html', 'img/events/s7-utopia-keyart.jpg', 'img/cards/card-utopia.jpg'),
    ('index.html', 'img/personnages/emerald-operator.jpg', 'img/cards/card-operator.jpg'),
    ('index.html', 'img/items/elysium.jpg', 'img/cards/card-elysium.jpg'),
    ('index.html', 'img/interactive/loadout-bench.jpg', 'img/cards/card-bench.jpg'),
    ('index.html', 'img/interactive/weapon-compare.jpg', 'img/cards/card-compare.jpg'),
    ('index.html', 'img/zombies/infected-zone.jpg', 'img/cards/card-infected.jpg'),
    ('index.html', 'img/armes/a545.jpg', 'img/cards/card-a545.jpg'),
    ('index.html', 'img/armes/a545.jpg', 'img/cards/card-build.jpg'),
    ('index.html', 'img/maps/map-farm.jpg', 'img/cards/card-farm.jpg'),
    ('index.html', 'img/maps/map-valley.jpg', 'img/cards/card-valley.jpg'),
    ('index.html', 'img/maps/map-airport.jpg', 'img/cards/card-airport.jpg'),
    ('index.html', 'img/maps/map-northridge.jpg', 'img/cards/card-northridge.jpg'),
    ('index.html', 'img/maps/map-armory.jpg', 'img/cards/card-armory.jpg'),
    ('index.html', 'img/maps/map-tvstation.jpg', 'img/cards/card-tvstation.jpg'),
    ('index.html', 'img/maps/map-farm.jpg', 'img/cards/card-farmzone.jpg'),
    # --- pages armes : hero -> artwork officiel dedie
    ('pages/armes-carbine.html', 'img/hero/hero-armes.jpg', 'img/armes/vis-carbine.jpg'),
    ('pages/armes-lmg.html', 'img/hero/hero-armes.jpg', 'img/armes/vis-lmg.jpg'),
    ('pages/armes-pistolets.html', 'img/hero/hero-armes.jpg', 'img/armes/vis-pistolets.jpg'),
    ('pages/armes-shotgun.html', 'img/hero/hero-armes.jpg', 'img/armes/vis-shotgun.jpg'),
    ('pages/armes-sniper.html', 'img/hero/hero-armes.jpg', 'img/armes/vis-sniper.jpg'),
    ('pages/armes-dmr.html', 'img/armes/fal.jpg', 'img/armes/vis-dmr.jpg'),
    ('pages/armes-fusils-assaut.html', 'img/armes/h416.jpg', 'img/armes/vis-assaut.jpg'),
    ('pages/armes-builds.html', 'img/armes/h416.jpg', 'img/armes/vis-builds.jpg'),
    ('pages/armes-attachements.html', 'img/armes/an-94.jpg', 'img/armes/vis-attachements.jpg'),
    ('pages/armes-nouveautes-s7.html', 'img/armes/a545.jpg', 'img/armes/vis-nouveautes.jpg'),
    ('pages/armes-nouveautes-s7.html', 'img/armes/ak15sc.jpg', 'img/cards/card-ak15sc.jpg'),
    ('pages/armes-tier-list.html', 'img/interactive/weapon-compare.jpg', 'img/armes/vis-tierlist.jpg'),
    # --- pages equipement
    ('pages/equipement-casques.html', 'img/hero/hero-armures.jpg', 'img/gear/vis-casques.jpg'),
    ('pages/equipement-rigs.html', 'img/hero/hero-armures.jpg', 'img/gear/vis-rigs.jpg'),
    ('pages/equipement-sacs.html', 'img/hero/hero-armures.jpg', 'img/gear/vis-sacs.jpg'),
    ('pages/equipement-headsets.html', 'img/hero/hero-armures.jpg', 'img/gear/vis-headsets.jpg'),
    ('pages/equipement-armures.html', 'img/hero/hero-armures.jpg', 'img/armures/armor-t6.jpg'),
    ('pages/equipement-tier-list.html', 'img/armures/vest-t5.jpg', 'img/armures/vest-t5.jpg'),
    # --- pages items
    ('pages/items-cles.html', 'img/items/keys.jpg', 'img/items/vis-cles.jpg'),
    ('pages/items-medical.html', 'img/items/medical.jpg', 'img/items/vis-medical.jpg'),
    ('pages/items-munitions.html', 'img/items/ammo.jpg', 'img/items/vis-munitions.jpg'),
    ('pages/guide-craft.html', 'img/items/ammo.jpg', 'img/items/vis-craft.jpg'),
    ('pages/items-craft-workbench.html', 'img/items/ammo.jpg', 'img/items/vis-workbench.jpg'),
    ('pages/items-collection-room.html', 'img/items/collection-room.jpg', 'img/items/vis-collection.jpg'),
    ('pages/items-koen-economy.html', 'img/items/koen-economy.jpg', 'img/items/vis-koen.jpg'),
    ('pages/items-valeur.html', 'img/items/red-drop.jpg', 'img/items/vis-valeur.jpg'),
    # --- pages evenements / communaute / cosmetiques
    ('pages/events-calendrier.html', 'img/events/loot-fest-arena.jpg', 'img/events/vis-calendrier.jpg'),
    ('pages/events-supplies-drops.html', 'img/events/supply-drops-airdrop.jpg', 'img/events/vis-supplies.jpg'),
    ('pages/events-warlord-tournament.html', 'img/events/warlord-tournament.jpg', 'img/events/vis-warlord.jpg'),
    ('pages/communaute-patch-notes.html', 'img/communaute/patch-notes.jpg', 'img/communaute/vis-patch.jpg'),
    ('pages/communaute-ressources.html', 'img/communaute/forum-discussion.jpg', 'img/communaute/vis-ressources.jpg'),
    ('pages/communaute-streamers.html', 'img/communaute/streamer-setup.jpg', 'img/communaute/vis-streamers.jpg'),
    ('pages/cosmetiques-skins-perso.html', 'img/personnages/emerald-operator.jpg', 'img/personnages/vis-opérateur.jpg'),
    ('pages/cosmetiques-dog-tags.html', 'img/items/collection-room.jpg', 'img/personnages/vis-dogtags.jpg'),
    ('pages/cosmetiques-skins-armes.html', 'img/events/s7-battle-pass.jpg', 'img/cards/card-s7battle.jpg'),
    # --- pages meta / lore
    ('pages/meta-builds-roles.html', 'img/meta/meta-builds.jpg', 'img/meta/vis-builds.jpg'),
    ('pages/meta-builds-roles.html', 'img/armes/m24.jpg', 'img/cards/card-m24.jpg'),
    ('pages/meta-loadout-optimizer.html', 'img/interactive/loadout-bench.jpg', 'img/meta/vis-optimizer.jpg'),
    ('pages/meta-tier-list-globale.html', 'img/meta/meta-tier-list.jpg', 'img/meta/vis-tierlist.jpg'),
    ('pages/meta-stratégies-s7.html', 'img/meta/meta-stratégies.jpg', 'img/meta/vis-strategies.jpg'),
    ('pages/univers-dark-zone.html', 'img/univers/dark-zone.jpg', 'img/univers/vis-darkzone.jpg'),
    ('pages/univers-factions.html', 'img/univers/blackgold-pmc.jpg', 'img/univers/vis-factions.jpg'),
    ('pages/univers-lore.html', 'img/univers/kamona-island.jpg', 'img/univers/vis-lore.jpg'),
    # --- pages zombie / saison 7
    ('pages/saison7-utopia.html', 'img/events/s7-utopia-keyart.jpg', 'img/events/s7-utopia-keyart.jpg'),
    ('pages/saison7-utopia.html', 'img/zombies/infected-zone.jpg', 'img/zombies/infected-zone.jpg'),
    ('pages/saison7-zombie-infected-zone.html', 'img/zombies/infected-zone.jpg', 'img/zombies/vis-infected.jpg'),
    ('pages/saison7-zombie-endless.html', 'img/zombies/zombie-endless.jpg', 'img/zombies/vis-endless.jpg'),
    ('pages/saison7-zombie-research.html', 'img/zombies/zombie-research.jpg', 'img/zombies/vis-research.jpg'),
    ('pages/saison7-balance-changes.html', 'img/zombies/balance-pvp.jpg', 'img/zombies/vis-balance.jpg'),
    ('pages/saison7-battle-pass.html', 'img/events/s7-battle-pass.jpg', 'img/events/s7-battle-pass.jpg'),
    ('pages/saison7-nouveautes.html', 'img/events/s7-nouveautes.jpg', 'img/events/s7-nouveautes.jpg'),
    ('pages/guide-progression.html', 'img/hero/hero-meta.jpg', 'img/cards/card-meta.jpg'),
    ('pages/map-no-mans-land.html', 'img/hero/hero-saison7.jpg', 'img/cards/card-saison7.jpg'),
]

IMG_TAG = re.compile(r'<img\b[^>]*>', re.I)


def apply_page(page_rel, mapping):
    """mapping : {src_racine_ancien : [nouveau_1, nouveau_2, ...]}

    Chaque occurrence successive de l'ancien src est remplacee par la
    nouvelle image correspondante, dans l'ordre.
    """
    p = ROOT / page_rel
    raw = p.read_text(encoding='utf-8')
    counters = {k: 0 for k in mapping}
    out, pos, hits = [], 0, 0
    for m in IMG_TAG.finditer(raw):
        a = re.search(r'src\s*=\s*["\']([^"\']+)["\']', m.group(0))
        if not a:
            continue
        src = a.group(1)
        try:
            cur = str((p.parent / src).resolve().relative_to(ROOT.resolve()))
        except ValueError:
            continue
        if cur not in mapping:
            continue
        lst = mapping[cur]
        i = counters[cur]
        if i >= len(lst):
            continue
        new_root = lst[i]
        counters[cur] = i + 1
        new_src = ('../' + new_root) if p.parent != ROOT else new_root
        tag = m.group(0).replace('src="%s"' % src, 'src="%s"' % new_src)
        tag = tag.replace("src='%s'" % src, "src='%s'" % new_src)
        out.append(raw[pos:m.start()]); out.append(tag)
        pos = m.end()
        hits += 1
    if hits:
        out.append(raw[pos:])
        p.write_text(''.join(out), encoding='utf-8')
    for k, v in counters.items():
        if v < len(mapping[k]):
            print('  ! %-42s %s : %d/%d remplacement(s)' % (page_rel, k, v, len(mapping[k])))
    return hits


if __name__ == '__main__':
    per_page = {}
    order = []
    for page_rel, old, new in REPL:
        if page_rel not in per_page:
            per_page[page_rel] = {}
            order.append(page_rel)
        per_page[page_rel].setdefault(old, []).append(new)

    total = 0
    for page_rel in order:
        n = apply_page(page_rel, per_page[page_rel])
        total += n
        print('  %-42s %d remplacement(s)' % (page_rel, n))
    print('\nRemplacements effectues : %d' % total)
