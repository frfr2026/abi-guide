#!/usr/bin/env python3
"""Ajoute le catalogue complet des 77 armes documentees.

Insertion dans pages/meta-tier-list-globale.html, juste apres la section
"L'armurerie de reference" : la grille existante montre les 24 armes du
catalogue local (avec tier, prix et photo), la nouvelle table montre les 77
armes de la source de reference, avec leurs statistiques completes.

Les deux ne se recouvrent pas : le tier list est un avis classe, le tableau
n'est qu'une base de donnees. Les badges distinguent explicitement les deux
niveaux de source.

Idempotent.
"""
import pathlib, re

P = pathlib.Path('pages/meta-tier-list-globale.html')
s = P.read_text(encoding='utf-8')

if 'catalogue-77' in s:
    print('deja present')
    raise SystemExit(0)

BLOCK = '''
          <h2 id="catalogue-77">8 bis. Le catalogue complet : 77 armes document\u00e9es</h2>
          <p>La grille ci-dessus ne montre que <strong>24 armes</strong> \u2014 celles pour lesquelles le site
          dispose d\u2019un tier, d\u2019un prix et d\u2019une photo. La source de r\u00e9f\u00e9rence en documente
          <strong>77</strong>. Voici les 77, avec leurs statistiques brutes. Ce ne sont pas des
          recommandations : ce sont des mesures, et c\u2019est au lecteur d\u2019en tirer son \u00e9quipement.</p>
          <div class="callout callout-info">
            <h3 class="h4">Comment lire ce tableau</h3>
            <ul>
              <li><strong>Toutes les valeurs sont sur une \u00e9chelle de 0 \u00e0 100</strong>, sauf la cadence (tours par minute), la vitesse du projectile (m/s) et le poids (kg).</li>
              <li><strong>Recul vertical et horizontal</strong> : plus la valeur est \u00e9lev\u00e9e, plus le tir est violent. Le rapport entre les deux compte autant que leur valeur \u2014 un recul horizontal fort est celui qui fait partir la balle \u00e0 c\u00f4t\u00e9.</li>
              <li><strong>Port\u00e9e</strong> : la distance \u00e0 laquelle l\u2019arme reste efficace, pas la port\u00e9e th\u00e9orique.</li>
              <li><strong>Vitesse du projectile</strong> : \u00e0 \u00e0 700 m/s, la balle commence \u00e0 perdre de l\u2019\u00e9nergie ; c\u2019est ce qui s\u00e9pare un fusil de pr\u00e9cision d\u2019un fusil d\u2019assaut \u00e0 courte distance.</li>
              <li><strong>Stabilit\u00e9 \u00e0 l\u2019hipfire</strong> : la capacit\u00e9 \u00e0 tenir le tir sans viser. C\u2019est le crit\u00e8re qui d\u00e9cide si une arme tient en int\u00e9rieur.</li>
              <li><strong>Ni tier ni prix ici</strong> : cette source ne les publie pas. Les valeurs de march\u00e9 du site (section 8) restent la r\u00e9f\u00e9rence pour l\u2019\u00e9conomie.</li>
            </ul>
          </div>
          <div class="table-wrap">
            <table class="data-table" id="catalogue-77-table">
              <caption>Les 77 armes document\u00e9es \u2014 <span class="src-tag src-documente">Document\u00e9</span></caption>
              <thead>
                <tr>
                  <th scope="col">Arme</th><th scope="col">Cat\u00e9gorie</th><th scope="col">Calibre</th>
                  <th scope="col">Modes</th><th scope="col">Rec. V</th><th scope="col">Rec. H</th>
                  <th scope="col">Erg.</th><th scope="col">Stab.</th><th scope="col">Pr\u00e9c.</th>
                  <th scope="col">Hip.</th><th scope="col">Port\u00e9e</th><th scope="col">Vit. (m/s)</th>
                  <th scope="col">Cadence</th><th scope="col">Poids</th>
                </tr>
              </thead>
              <tbody id="catalogue-77-body">
                <tr><td colspan="14" class="text-muted">Chargement du catalogue\u2026</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : wiki ABI de r\u00e9f\u00e9rence (Fandom), page Weapons. Donn\u00e9e
          document\u00e9e et recoup\u00e9e, non publi\u00e9e par l\u2019\u00e9diteur. Fichier de donn\u00e9es :
          <code>js/data-weapons-wiki.json</code>.</p>
'''

ANCHOR = '''          <h2 id="verdict">'''
assert ANCHOR in s
s = s.replace(ANCHOR, BLOCK.strip() + '\n\n' + ANCHOR, 1)

# renumeroter les sections suivantes
ORDER = ['methode', 'global', 'par-mode', 'par-categorie', 'kits', 'par-carte',
         'zombies', 'armures', 'armurerie', 'catalogue-77', 'verdict', 'faq']
for i, sid in enumerate(ORDER, start=1):
    pat = re.compile(r'(<h2 id="' + re.escape(sid) + r'">)([^<]*?)(\d+\.? ?bis?\.?)')
    m = pat.search(s)
    if m:
        # on conserve le suffixe "bis" de l'ancre d'origine si present
        num = m.group(3)
        suffix = ' bis.' if 'bis' in num else '.'
        s = s[:m.start()] + m.group(1) + m.group(2) + str(i) + suffix + s[m.end():]

# sommaire
mt = re.search(r'<aside class="toc"[^>]*>.*?</aside>', s, re.S)
if mt:
    blk = mt.group(0)
    head = blk[:blk.find('<h4>Sommaire</h4>') + len('<h4>Sommaire</h4>')]
    existing = re.findall(r'<a href="#([^"]+)" id="([^"]+)">([^<]+)</a>', blk)
    LABELS = {
        'methode': "1. Méthode", 'global': "2. Tier list global",
        'par-mode': "2 bis. Meta par mode", 'par-categorie': "3. Par catégorie",
        'kits': "4. Season kits", 'par-carte': "5. Par carte",
        'zombies': "6. Modes zombies", 'armures': "7. Armures",
        'armurerie': "8. Armurerie du site", 'catalogue-77': "8 bis. Catalogue des 77 armes",
        'verdict': "9. Par tier", 'faq': "10. FAQ",
    }
    lines = []
    for sid in ORDER:
        old_id = next((i2 for h, i2, t in existing if h == sid), None)
        if old_id is None:
            continue
        lines.append('<a href="#%s" id="%s">%s</a>' % (sid, old_id, LABELS[sid]))
    for h, i2, t in existing:
        if h not in ORDER:
            lines.append('<a href="#%s" id="%s">%s</a>' % (h, i2, t))
    s = s[:mt.start()] + head + '\n' + '\n'.join(lines) + '\n        </aside>' + s[mt.end():]

P.write_text(s, encoding='utf-8')
print('pages/meta-tier-list-globale.html : section catalogue 77 inseree')
