#!/usr/bin/env python3
"""Met a jour les legendes et les visuels des pages cartes apres restauration des cartes officielles."""
import pathlib, re

ROOT = pathlib.Path('.')

CAPS = {
 'pages/map-airport.html': ('La carte officielle du jeu, telle qu\'affichée dans le client.',
   'Vue aerienne de la carte Airport avec ses zones nommees : Control Tower, Ticket Hall, Military Zone, Exhibition et Freight Center.',
   '1920', '1080'),
 'pages/map-armory.html': ('La carte officielle de l\'Armory : deux batiments, un niveau souterrain, et des couloirs qui ne pardonnent pas.',
   'Plan officiel de l\'Armory avec ses zones : Loose Cargo, Supply Depot, Military Zone et le niveau souterrain.',
   '1920', '1080'),
 'pages/map-farm.html': ('La carte officielle de Farm : 8 extractions, une ferme, un motel et un lac.',
   'Plan officiel de Farm avec ses zones nommees : SW Farmhouse, Grain Trade Center, Artificial Lake, Stables et Motel.',
   '1920', '1080'),
 'pages/map-northridge.html': ('La carte officielle de Northridge : 11 extractions, altitude et lignes de vue longues.',
   'Plan officiel de Northridge avec ses zones : Station, Al-Andalus, Bunker, Big House et le sommet de la falaise.',
   '1920', '1080'),
 'pages/map-tv-station.html': ('La carte officielle de TV Station : le plan des deux etages et du sous-sol.',
   'Plan officiel de TV Station, etage par etage, avec les pieces et les zones cles.',
   '1920', '1080'),
 'pages/map-valley.html': ('La carte officielle de Valley : 8 extractions, du front de mer au village de luxe.',
   'Plan officiel de Valley avec ses zones : Beach Villa, Port, Rock Courtyard, Luxury Complex et Eastern Farm.',
   '1920', '1080'),
}

for page, (cap, alt, w, h) in CAPS.items():
    p = ROOT / page
    s = p.read_text(encoding='utf-8')
    # legende
    s = re.sub(r'<figcaption>.*?</figcaption>', '<figcaption>%s</figcaption>' % cap, s, count=1)
    # alt + dimensions de l'image de carte
    def fix(m):
        tag = m.group(0)
        if 'maps/map-' not in tag:
            return tag
        tag = re.sub(r'alt="[^"]*"', 'alt="%s"' % alt, tag)
        tag = re.sub(r'width="\d+"', 'width="%s"' % w, tag)
        tag = re.sub(r'height="\d+"', 'height="%s"' % h, tag)
        return tag
    s = re.sub(r'<img[^>]*maps/map-[a-z]+\.jpg[^>]*>', fix, s)
    p.write_text(s, encoding='utf-8')
    print('  %-28s legende + alt mis a jour' % page)

# TV Station : la photo d'interieur devient un second visuel cinematographique
p = ROOT / 'pages/map-tv-station.html'
s = p.read_text(encoding='utf-8')
if 'var-tvstation-interieur.jpg' not in s:
    fig = ('          <figure class="page-figure">\n'
           '            <img width="1920" height="1080" src="../img/maps/var-tvstation-interieur.jpg" alt="Salle de controle circulaire de la TV Station, abandonnee, eclairage froid" loading="lazy" decoding="async">\n'
           '            <figcaption>Le coeur de la TV Station : la salle de controle circulaire. C\'est ici que '
           'dort le meilleur loot de la carte — et que se plantent les batailles les plus denses.</figcaption>\n'
           '          </figure>\n\n')
    m = re.search(r'(\n\s*)<figure class="page-figure">\s*\n\s*<img width="1920" height="1080" src="\.\./img/maps/map-tvstation\.jpg"',
                  s)
    if m:
        s = s[:m.start()] + '\n' + fig + s[m.start() + 1:]
        p.write_text(s, encoding='utf-8')
        print('  TV Station : photo d\'interieur ajoutee')
    else:
        print('  ! TV Station : motif non trouve')
