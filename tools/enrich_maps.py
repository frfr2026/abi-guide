#!/usr/bin/env python3
"""Enrichissement des 7 pages cartes d'ABI NEXUS avec les donnees officielles.

Source : wiki ABI (zones, extractions, boss, cles) + cartes officielles.
Ajoute a chaque page :
  - la carte officielle en grand (image de carte du jeu)
  - les zones reelles avec leurs caracteristiques
  - les points d'extraction officiels
  - les cles et leur durabilite
  - les liens vers les cartes interactives autorisees
    (abibuilder.com/maps et maps.tcno.co/abi)
"""
import json, pathlib, re

ROOT = pathlib.Path('.')
DATA = json.loads((ROOT / 'tools/_map_zones.json').read_text(encoding='utf-8'))

# identifiant site -> cle du wiki
WIKI_KEY = {
    'farm': 'Farm', 'valley': 'Valley', 'northridge': 'Northridge',
    'tvstation': 'TV Station', 'armory': 'Armory', 'airport': 'Airport',
}

# page -> (slug, nom affiche)
PAGES = {
    'map-farm.html': ('farm', 'Farm'),
    'map-valley.html': ('valley', 'Valley'),
    'map-northridge.html': ('northridge', 'Northridge'),
    'map-tv-station.html': ('tvstation', 'TV Station'),
    'map-armory.html': ('armory', 'Armory'),
    'map-airport.html': ('airport', 'Airport'),
}

TCNO_SLUG = {'farm': 'farm', 'valley': 'valley', 'northridge': 'northridge',
              'tvstation': 'tv-station', 'armory': 'armory', 'airport': 'airport'}


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


def feat_frag(feats):
    out = []
    for f in feats:
        t = f.replace('[[#Extractions|Extraction Point]]', 'point d\'extraction')
        t = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', t)
        t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)
        t = t.replace('<br>', ' ').strip()
        if t and t.lower() != 'none':
            out.append(t.lower())
    return out


def build_sections(slug, name):
    d = DATA.get(WIKI_KEY.get(slug, ''), {})
    pois = d.get('poi', [])
    exts = d.get('extractions', [])
    keys = d.get('keys', [])
    boss = d.get('bosses', [])
    info = d.get('infobox', {})
    desc = d.get('description', '')

    parts = []

    # --- zones officielles ---
    if pois:
        rows = []
        for z in pois:
            feats = feat_frag(z.get('features', []))
            feats = [f for f in feats if f not in ('safe',)][:3]
            rows.append('              <li><strong>%s</strong>%s</li>' % (
                esc(z['name']),
                (' — ' + esc(', '.join(f.capitalize() for f in feats))) if feats else ''))
        parts.append('''          <h2 id="zones">Zones officielles</h2>
          <p class="text-muted">Libellés relevés sur la <strong>carte officielle du jeu</strong> : ces noms sont ceux affichés en jeu et repris par les codes-cle.</p>
          <ul class="zone-list">
%s
          </ul>''' % '\n'.join(rows))

    # --- extractions ---
    if exts:
        items = '\n'.join('            <li>%s</li>' % esc(e) for e in exts)
        parts.append('''          <h2 id="extractions-officielles">Points d'extraction officiels</h2>
          <p>Liste exhaustive des sorties de la carte (noms de jeu). Les <strong>extractions vertes</strong> sont fixes ; les autres dépendent d'un vehicule, d'un abonnement ou d'une zone Nanotech.</p>
          <ul>
%s
          </ul>''' % items)

    # --- cles ---
    if keys:
        krows = []
        for k in keys:
            note = k.get('notes') or ''
            note = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', note)
            note = re.sub(r'\[\[([^\]]+)\]\]', r'\1', note)
            note = note.replace('Soon', 'bientôt disponible').replace('<br />', ' · ').strip(' ·')
            if note.lower() == 'soon':
                note = ''
            dur = k.get('durability')
            krows.append('            <tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (
                esc(k['name']),
                ('%d' % dur) if dur else '—',
                esc(note) if note else '—'))
        parts.append('''          <h2 id="cles">Clés de la carte</h2>
          <p>Chaque clé s'use à l'usage : <strong>1 point en Normal, 2 en Lockdown, 3 en Forbidden</strong>. Une clé à 45 de durabilité tient donc beaucoup moins longtemps en Forbidden.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Clés disponibles sur %s</caption>
              <thead><tr><th scope="col">Clé</th><th scope="col">Durabilité</th><th scope="col">Débloque</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>''' % (esc(name), '\n'.join(krows)))

    # --- boss ---
    if boss:
        b = [x.split('#')[-1] for x in boss]
        parts.append('''          <div class="callout callout-danger"><h3 class="h4">Boss de la carte</h3><p>%s — spawn parmi les points d'intérêt : approchez avec une armure T3 minimum et surveillez le tour de garde.</p></div>''' % esc(', '.join(sorted(set(b)))))

    # --- cartes interactives ---
    sl = TCNO_SLUG.get(slug, slug)
    parts.append('''          <h2 id="cartes-interactives">Cartes interactives</h2>
          <p>Deux ressources de référence pour aller plus loin que cette page :</p>
          <ul class="link-list">
            <li><a href="https://abibuilder.com/maps" rel="noopener nofollow" target="_blank">ABIBuilder — catalogue des cartes</a> : spawns, clés et stats de loot par carte.</li>
            <li><a href="https://maps.tcno.co/abi/%s" rel="noopener nofollow" target="_blank">TCNO — carte interactive de %s</a> : survol des zones, marqueurs d'extraction et de loot.</li>
          </ul>''' % (sl, esc(name)))

    return '\n'.join(parts), desc, info


if __name__ == '__main__':
    for page, (slug, name) in PAGES.items():
        p = ROOT / 'pages' / page
        raw = p.read_text(encoding='utf-8')
        blocks, desc, info = build_sections(slug, name)
        print('### %s : %d blocs, description %d car., boss %s' % (
            page, blocks.count('<h2'), len(desc), info.get('Enemies', '—')[:40]))
        (ROOT / 'tools' / ('_map_blocks_%s.html' % slug)).write_text(blocks, encoding='utf-8')
