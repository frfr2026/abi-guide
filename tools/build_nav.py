#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI NEXUS — build_nav.py : generateur canonique de la navigation globale.

Probleme corrige
----------------
Le bloc <header class="site-nav"> etait assemble par substitutions successives
(S13, S14, S17) qui avaient laisse un </div> surnumeraire : la balise
<nav class="nav-links"> se fermait avant « Saison 7 ». Les entrees restantes
sortaient alors du conteneur flex .nav-inner, ce qui :
  - pushing le bouton hamburger hors de l'ecran en 375 px (x = 623 px) ;
  - rendait la barre de navigation mobile inutilisable ;
  - produisait un HTML mal forme (41 <div> ouverts / 42 </div> fermes).

Ce script reconstruit le header ENTIEREMENT a partir d'un modele unique
(NAV ci-dessous), pour les 65 pages du site. Le HTML genere est equilibre,
la structure est identique sur toutes les pages et les chemins sont resolus
correctement depuis la racine comme depuis le dossier /pages.

Identifiants
------------
Les ancres du header sont generees SANS identifiant, comme les autres
ancres du site ; build_s17.py les renumerote ensuite (lnk-<page>-<n>) dans
l'ordre du document, ce qui garantit l'unicite des identifiants sur la page.

Usage : python3 tools/build_nav.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE_DIR = ROOT / 'pages'
PAGES = sorted(PAGE_DIR.glob('*.html')) + [ROOT / 'index.html', ROOT / '404.html']

# ══════════════════════════════════════════════════════════════════════
#  MODELE DE NAVIGATION (source unique de verite)
# Chaque section : (cle, libelle, cible, badge, [colonnes])
#  Une colonne : (titre, [(libelle, cible), ...])
#  Les cibles sont des noms de fichiers « pages/ » : le prefixe est calcule
#  selon l'emplacement de la page (racine ou dossier /pages).
# ══════════════════════════════════════════════════════════════════════
NAV = [
    ('guides', 'Guides', 'guide-debutant.html', None, [
        ('Progression', [
            ('Guide du débutant', 'guide-debutant.html'),
            ('Guide avancé', 'guide-avance.html'),
            ('Progression', 'guide-progression.html'),
            ('Extraction', 'guide-extraction.html'),
        ]),
        ('Économie', [
            ('Économie Koen', 'guide-economie.html'),
            ('Craft &amp; Workbench', 'guide-craft.html'),
            ('Marchands', 'guide-traders.html'),
        ]),
        ('Stratégie', [
            ('Stratégies S7', 'meta-stratégies-s7.html'),
            ('Builds par rôle', 'meta-builds-roles.html'),
            ('Loadout Optimizer', 'meta-loadout-optimizer.html'),
            ('Réglages &amp; sensibilité', 'reglages-sensibilite.html'),
        ]),
    ]),
    ('armes', 'Armes', 'armes-fusils-assaut.html', None, [
        ('Catégories', [
            ("Fusils d'assaut", 'armes-fusils-assaut.html'),
            ('DMR', 'armes-dmr.html'),
            ('SMG', 'armes-smg.html'),
            ('Snipers', 'armes-sniper.html'),
            ('Shotguns', 'armes-shotgun.html'),
            ('Pistolets', 'armes-pistolets.html'),
            ('LMG', 'armes-lmg.html'),
            ('Carabines', 'armes-carbine.html'),
        ]),
        ('Saison 7', [
            ('A545 &amp; AK-15SC', 'armes-nouveautes-s7.html'),
            ('Attachements S7', 'armes-attachements-s7.html'),
            ('Tous attachements', 'armes-attachements.html'),
        ]),
        ('Méta', [
            ('Tier List Armes', 'armes-tier-list.html'),
            ('Meilleurs builds', 'armes-builds.html'),
            ('Tier List globale S7', 'meta-tier-list-globale.html'),
        ]),
    ]),
    ('equipement', 'Équipement', 'equipement-armures.html', None, [
        ('Protection', [
            ('Armures T1–T6', 'equipement-armures.html'),
            ('Casques', 'equipement-casques.html'),
            ('Rigs', 'equipement-rigs.html'),
            ('Sacs à dos', 'equipement-sacs.html'),
            ('Casques audio', 'equipement-headsets.html'),
        ]),
        ('Méta', [
            ('Tier List Équipement', 'equipement-tier-list.html'),
        ]),
    ]),
    ('cartes', 'Cartes', 'map-farm.html', None, [
        ('Cartes', [
            ('Farm', 'map-farm.html'),
            ('Valley', 'map-valley.html'),
            ('Northridge', 'map-northridge.html'),
            ('Armory', 'map-armory.html'),
            ('TV Station', 'map-tv-station.html'),
            ('Airport', 'map-airport.html'),
            ("No Man's Land", 'map-no-mans-land.html'),
        ]),
    ]),
    ('objets', 'Objets', 'items-munitions.html', None, [
        ('Munitions &amp; Valeur', [
            ('Munitions &amp; Pénétration', 'items-munitions.html'),
            ('Valeur des objets', 'items-valeur.html'),
            ('Koen &amp; Économie', 'items-koen-economy.html'),
        ]),
        ('Accès &amp; Production', [
            ('Clés &amp; Accès', 'items-cles.html'),
            ('Collection Room', 'items-collection-room.html'),
            ('Craft &amp; Workbench', 'items-craft-workbench.html'),
        ]),
        ('Soins &amp; Cosmétiques', [
            ('Médical &amp; Soins', 'items-medical.html'),
            ("Skins d'armes", 'cosmetiques-skins-armes.html'),
            ('Cosmétiques de personnage', 'cosmetiques-skins-perso.html'),
            ('Dog Tags', 'cosmetiques-dog-tags.html'),
        ]),
    ]),
    ('saison7', 'Saison 7', 'saison7-utopia.html', 'Utopia', [
        ('La saison', [
            ('Utopia (S7)', 'saison7-utopia.html'),
            ('Nouveautés S7', 'saison7-nouveautes.html'),
            ('Balance Changes', 'saison7-balance-changes.html'),
            ('Battle Pass S7', 'saison7-battle-pass.html'),
        ]),
        ('Modes zombies', [
            ('Infected Zone', 'saison7-zombie-infected-zone.html'),
            ('Zombie Endless', 'saison7-zombie-endless.html'),
            ('Zombie Research', 'saison7-zombie-research.html'),
        ]),
    ]),
    ('meta', 'Méta', 'meta-tier-list-globale.html', None, [
        ('Classements', [
            ('Tier List globale S7', 'meta-tier-list-globale.html'),
            ('Builds par rôle', 'meta-builds-roles.html'),
        ]),
        ('Stratégie &amp; Outils', [
            ('Stratégies Saison 7', 'meta-stratégies-s7.html'),
            ('Loadout Optimizer', 'meta-loadout-optimizer.html'),
        ]),
    ]),
    ('univers', 'Univers', 'univers-lore.html', None, [
        ('Univers de Kamona', [
            ('Histoire &amp; chronologie', 'univers-lore.html'),
            ('Factions &amp; personnages', 'univers-factions.html'),
            ('La Dark Zone', 'univers-dark-zone.html'),
        ]),
        ('Sur le terrain', [
            ('TV Station', 'map-tv-station.html'),
            ('Armory', 'map-armory.html'),
            ('Farm', 'map-farm.html'),
            ('Utopia (S7)', 'saison7-utopia.html'),
        ]),
    ]),
    ('evenements', 'Événements', 'events-calendrier.html', None, [
        ('Saison 7 : Utopia', [
            ('Calendrier &amp; échéances', 'events-calendrier.html'),
            ('Supply Drops 2.0', 'events-supplies-drops.html'),
            ('Warlord Tournament III', 'events-warlord-tournament.html'),
        ]),
        ('Événements majeurs', [
            ('Utopia (S7)', 'saison7-utopia.html'),
            ('Battle Pass S7', 'saison7-battle-pass.html'),
            ('Infected Zone', 'saison7-zombie-infected-zone.html'),
        ]),
    ]),
    ('communaute', 'Communauté', 'communaute-ressources.html', None, [
        ('Ressources', [
            ('Ressources communautaires', 'communaute-ressources.html'),
            ('Patch notes &amp; mises à jour', 'communaute-patch-notes.html'),
            ('Streamers &amp; créateurs', 'communaute-streamers.html'),
        ]),
        ('Créateurs &amp; Patch notes', [
            ('Stratégies S7', 'meta-stratégies-s7.html'),
            ('Utopia (S7)', 'saison7-utopia.html'),
            ('Craft &amp; Workbench', 'guide-craft.html'),
        ]),
    ]),
]

# Sections marquees par les anciens builders : les marqueurs sont conserves
# pour que build_s13.py et build_s14.py restent rejouables.
MARKERS = {'evenements': ('S13-NAV',), 'communaute': ('S14-NAV',)}

# ══════════════════════════════════════════════════════════════════════
#  ETAT ACTIF : section correspondiente a chaque page
# ══════════════════════════════════════════════════════════════════════
ACTIVE_RULES = [
    ('armes-', 'armes'),
    ('equipement-', 'equipement'),
    ('reglages-', 'guides'),
    ('guide-', 'guides'),
    ('items-', 'objets'),
    ('cosmetiques-', 'objets'),
    ('map-', 'cartes'),
    ('meta-', 'meta'),
    ('saison7-', 'saison7'),
    ('univers-', 'univers'),
    ('events-', 'evenements'),
    ('communaute-', 'communaute'),
]


def active_key(stem):
    for prefix, key in ACTIVE_RULES:
        if stem.startswith(prefix):
            return key
    return None


# ══════════════════════════════════════════════════════════════════════
#  RENDU DU HEADER
# ══════════════════════════════════════════════════════════════════════
LOGO_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="#C8A84B" stroke-width="2">'
            '<path d="M12 2l8 4.5v9L12 20l-8-4.5v-9z"/>'
            '<path d="M12 22V12M12 12L4 6.5M12 12l8-5.5"/></svg>')
THEME_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
             '<circle cx="12" cy="12" r="4"/>'
             '<path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4'
             'M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')
BURGER_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<path d="M4 6h16M4 12h16M4 18h16"/></svg>')


def build_header(prefix, active, home):
    """prefix : '' depuis /pages, 'pages/' depuis la racine.
    home   : chemin de la page d'accueil (racine du site)."""
    out = []
    out.append('  <header class="site-nav">')
    out.append('    <div class="nav-inner">')
    out.append('      <a class="logo" href="%s" aria-label="ABI NEXUS — Accueil">' % home)
    out.append('        <span class="logo-mark">%s</span>' % LOGO_SVG)
    out.append('        ABI<span class="logo-accent">NEXUS</span>')
    out.append('      </a>')
    out.append('      <nav class="nav-links" aria-label="Navigation principale">')

    for key, label, target, badge, cols in NAV:
        marker = MARKERS.get(key)
        if marker:
            out.append('        <!--%s-->' % marker[0])
        href = prefix + target
        if cols is None:
            # entree directe (Saison 7 Utopia) : pas de mega-menu
            if active == key:
                out.append('        <a class="nav-link active" href="%s" aria-current="page">%s'
                           ' <span class="badge badge-s7">%s</span></a>' % (href, label, badge))
            else:
                out.append('        <a class="nav-link" href="%s">%s'
                           ' <span class="badge badge-s7">%s</span></a>' % (href, label, badge))
        else:
            badge_html = (' <span class="badge badge-s7">%s</span>' % badge) if badge else ''
            if active == key:
                out.append('        <div class="has-mega">')
                out.append('          <a class="nav-link active" href="%s" aria-current="page">%s%s</a>'
                           % (href, label, badge_html))
            else:
                out.append('        <div class="has-mega">')
                out.append('          <a class="nav-link" href="%s">%s%s</a>' % (href, label, badge_html))
            out.append('          <div class="mega-menu">')
            for head, links in cols:
                out.append('            <div class="mega-col"><h5>%s</h5>' % head)
                for llabel, ltarget in links:
                    out.append('              <a href="%s%s">%s</a>' % (prefix, ltarget, llabel))
                out.append('            </div>')
            out.append('          </div>')
            out.append('        </div>')
        if marker:
            out.append('        <!--/%s-->' % marker[0])

    out.append('      </nav>')
    out.append('      <div class="nav-actions">')
    out.append('        <button class="nav-icon-btn" data-theme-toggle aria-label="Basculer le thème">')
    out.append('          %s' % THEME_SVG)
    out.append('        </button>')
    out.append('        <a class="btn btn-primary btn-sm" href="%smeta-loadout-optimizer.html">'
               'Loadout Builder</a>' % prefix)
    out.append('        <button class="hamburger" aria-label="Ouvrir le menu" aria-expanded="false">')
    out.append('          %s' % BURGER_SVG)
    out.append('        </button>')
    out.append('      </div>')
    out.append('    </div>')
    out.append('  </header>')
    return '\n'.join(out) + '\n'


HEADER_RE = re.compile(r'[ \t]*<header class="site-nav">.*?</header>\n', re.S)
A_ID_RE = re.compile(r'(<a\b[^>]*?)\s+id="lnk-[^"]*"')


def main():
    changed = 0
    for f in PAGES:
        s = f.read_text(encoding='utf-8')
        in_pages = f.parent.name == 'pages'
        prefix = '' if in_pages else 'pages/'
        home = '../index.html' if in_pages else 'index.html'
        header = build_header(prefix, active_key(f.stem), home)

        m = HEADER_RE.search(s)
        if not m:
            print('  ! header introuvable :', f.name)
            continue
        s = s[:m.start()] + header + s[m.end():]

        # les identifiants lnk-* sont regeneres par build_s17.py :
        # on les retire pour eviter toute collision avec la numerotation
        # qui suit l'ordre du document.
        s = A_ID_RE.sub(r'\1', s)

        f.write_text(s, encoding='utf-8')
        changed += 1

    print('Navigation reconstruite sur %d / %d pages' % (changed, len(PAGES)))
    print('Structure : %d sections, %d entrees de premier niveau'
          % (len(NAV), len(NAV)))
    print('Les identifiants lnk-* sont renumerotes par build_s17.py (a relancer).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
