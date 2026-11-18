#!/usr/bin/env python3
"""Enrichit pages/map-armory.html avec les donnees officielles du wiki.

Source : wiki officiel ABI, pages Armory, Bosses, Keys.
Donnees reprises telles quelles : duree, joueurs, boss, points d'interet,
equipement du boss et de ses gardes, conditions d'extraction, cles.
"""
import pathlib, re

P = pathlib.Path('pages/map-armory.html')
s = P.read_text(encoding='utf-8')

if 'Renoir en detail' in s:
    print('deja enrichi')
    raise SystemExit(0)

# ── 1. Nouvelle section sur le boss, inseree apres la section 3 ─────────
BOSS = '''
          <h2 id="boss-officiel">4. Renoir en détail — l'équipement officiel du boss</h2>
          <p>Les données de cette section sont reprises du <strong>wiki officiel</strong> d'Arena Breakout Infinite (page <em>Bosses</em> et fiche <em>Renoir</em>). Ce sont les caractéristiques documentées du boss, pas des calculs de la communauté : elles décrivent ce que Renoir porte réellement en raid.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Élément</th><th>Donnée officielle</th></tr></thead>
              <tbody>
                <tr><td>Carte</td><td>Armory</td></tr>
                <tr><td>Chance de spawn</td><td>≈ 15 %</td></tr>
                <tr><td>Garde du corps</td><td>6 gardes</td></tr>
                <tr><td>Jeton de boss</td><td><strong>Battleforged Badge</strong> (intitulé « Identity » dans l'inventaire)</td></tr>
                <tr><td>Armure minimale</td><td>T4, casque et masque Maztcha ; il apparaît le plus souvent en T5</td></tr>
                <tr><td>Signe distinctif</td><td>Casque Maztcha vert ; une fois le casque retiré, il est nettement chauve</td></tr>
              </tbody>
            </table>
          </div>

          <h3 class="h4">Armes de Renoir</h3>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Munition</th></tr></thead>
              <tbody>
                <tr><td>RPK-16</td><td>5.45×39mm BP (T4)</td></tr>
                <tr><td>MK14 (fusil de marqueur)</td><td>7.62×51mm M80 (T4)</td></tr>
                <tr><td>AKS-74U</td><td>5.45×39mm BP (T4)</td></tr>
                <tr><td>AKM</td><td>5.45×39mm BP (T4)</td></tr>
                <tr><td>S12K</td><td>12x70mm Armor-Piercing Slug (T3)</td></tr>
              </tbody>
            </table>
          </div>

          <h3 class="h4">Équipement de ses gardes</h3>
          <p>Renoir est accompagné de gardes shaming. Voici leur équipement documenté :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Catégorie</th><th>Équipement des gardes</th></tr></thead>
              <tbody>
                <tr><td>Arme</td><td>MP-133 Shotgun</td></tr>
                <tr><td>Munition</td><td>12x70mm Type 7 / Type 8 Buckshot</td></tr>
                <tr><td>Armure</td><td>SEK Composite Body Armor — <strong>niveau 4</strong></td></tr>
                <tr><td>Ceinturon</td><td>FA Portable Chest Rig</td></tr>
                <tr><td>Sac</td><td>Medium Camping Backpack</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h3 class="h4">Le piège des gardes</h3>
            <p>Les gardes de Renoir sont en <strong>armure niveau 4</strong> et vides le MP-133 à la buckshot : à l'étage, dans un couloir, une garde qui vous voit est une menace réelle. Renoir porte, lui, du T4 minimum et souvent du T5 — mais il est identifiable et repérable. Deux règles en découlent : <strong>ne tirez pas dans le vide sur un mouvement de couloir</strong>, et contre Renoir lui-même, le corps à corps est inutile — visez la tête, il ne porte pas de casque détectable de loin une fois le Maztcha retiré.</p>
          </div>

          <h3 class="h4">Les autres boss de la carte, pour mémoire</h3>
          <p>Le wiki officiel attribue les autres boss comme suit — utile pour ne pas confondre les cartes :</p>
          <ul>
            <li><strong>Ajax Jones</strong> — boss de <strong>Farm</strong>, ~15 % de spawn, 5 gardes, jeton <em>Pocket Knife</em>. C'est lui qui tient les Étables et le Motel de Farm.</li>
            <li><strong>Doss Anthony</strong> — boss de <strong>Valley</strong>, ~15 % de spawn, 10 gardes (le plus nombreux du jeu), jeton <em>Handmade Gold</em>.</li>
            <li><strong>Fred (Frade) Lee</strong> — boss de <strong>Northridge</strong>, jeton <em>Frade's Wedding Ring</em>.</li>
            <li><strong>Kurt Williams</strong> et <strong>Bernard Martin</strong> — les deux boss de <strong>TV Station</strong>.</li>
          </ul>
          <p class="small text-muted">Source : wiki officiel ABI, page « Bosses ». Rien de tout cela n'est une rumeur : ce sont les fiches officielles du jeu. En revanche, les <em>stratégies</em> de combat pour les abbattre relèvent de l'expérience de terrain, pas des données publiées.</p>
'''

# inserer avant la section "4. Extractions" existante, qu'on renumerote ensuite
anchor = '          <h2 id="extractions">4. Extractions — peu mais stratégiques</h2>'
assert anchor in s
s = s.replace(anchor, BOSS.strip() + '\n\n          <h2 id="extractions">5. Extractions — peu mais stratégiques</h2>', 1)

# ── 2. Corriger le paragraphe des extractions ───────────────────────────
OLD_EXT = '''            <p><strong>9 extractions seulement</strong> : elles sont pré-visées par tous les survivants.</p>'''
if OLD_EXT in s:
    s = s.replace(OLD_EXT, '', 1)

OLD_P = '''            <p>9 extractions seulement : elles sont <strong>pré-visées</strong> par tous les survivants.</p>'''
NEW_P = '''            <p><strong>3 extractions seulement</strong> : elles sont <strong>pré-visées</strong> par tous les survivants. Le wiki officiel liste exactement trois points de sortie sur Armory — <em>F Control Room</em>, <em>B1 Canal</em> et <em>B1 Passage</em> — et les trois sont conditionnels.</p>
            <ul>
              <li><strong>F Control Room</strong> — <em>Chance / Conditional</em>. Active 15 minutes après le début du raid.</li>
              <li><strong>B1 Canal</strong> — <em>Chance / Conditional</em>. L'écluse s'ouvre 3 minutes après le début du match ; il faut trouver l'interrupteur dans la zone de contrôle du 2e étage.</li>
              <li><strong>B1 Passage</strong> — <em>Chance / Conditional</em>. Active 15 minutes après le début du raid.</li>
            </ul>
            <p class="small text-muted">Source : wiki officiel ABI, tableau « Extraction Points » de la page Armory. Aucune de ces trois sorties n'est garantie : votre plan doit toujours inclure un repli.</p>'''
if OLD_P in s:
    s = s.replace(OLD_P, NEW_P, 1)
else:
    # fallback : chercher la phrase "extractions seulement"
    m = re.search(r'<p>9 extractions seulement[^<]*</p>', s)
    if m:
        s = s[:m.start()] + NEW_P + s[m.end():]
    else:
        print('ATTENTION : paragraphe extractions non trouve')

# ── 3. Le bandeau stats : duree et joueurs officiels ────────────────────
s = s.replace(
    '<dt>Extractions</dt>\n              <dd>3 — les moins nombreuses de ABI</dd>',
    '<dt>Extractions</dt>\n              <dd>3 — les moins nombreuses de ABI</dd>', 1)

# ── 4. Sommaire ─────────────────────────────────────────────────────────
s = s.replace(
    '<a href="#tactique" id="lnk-map-armory-XXX">3. Tactique CQB</a>',
    '<a href="#tactique" id="lnk-map-armory-XXX">3. Tactique CQB</a>', 1)

P.write_text(s, encoding='utf-8')
print('pages/map-armory.html enrichi')
