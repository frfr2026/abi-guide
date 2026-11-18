#!/usr/bin/env python3
"""Ajoute le tableau officiel des boss noms par l'editeur aux pages cartes.

Source : senseos.gg, "Arena Breakout: Infinite Bosses: Every Name by Map",
qui a passe en revue les 483 publications de MoreFun Studios au 1er novembre
2026. La distinction est importante et le site doit la faire :

  - Six personnages sont nommes boss PAR L'EDITEUR : Fred (Northridge),
    Kurt, Rolf et Bernard (TV Station), Hecate (Farm), Phobos (zones infectees).
  - Ajax (Farm) et Renoir (Armory) sont attaches a leur carte par le TEXTE
    RECIT de l'editeur, sans que le mot "boss" y soit employe.
  - Doss (Valley) n'apparait dans AUCUNE publication de MoreFun : son nom
    est rapporte par la communaute et par le wiki, il ne vaut pas annonce
    officielle.

Regle de publication : une affirmation officielle est etiquete comme telle,
une donnee communautaire est attribuee.
"""
import pathlib, re

PAGES = {
 'pages/map-farm.html': {
   'anchor': 'Boss de la carte',
   'title': 'Les boss de Farm',
   'h3': True,
   'rows': [
     ('<strong>Hecate</strong>', 'Nommé boss par l\'éditeur', '« Abyss Captain » dans les notes, « Abyss Squad Leader » dans le communiqué. Mobile et agile, elle contourne. Présente depuis l\'extension de Farm en Saison 2. Apparaît à la Small Hall et au Grain Trade Center. Une voix de Joel à l\'entrée du raid vous prévient qu\'elle est sur la carte.'),
     ('<strong>Phobos</strong>', 'Nommé boss par l\'éditeur', 'Le boss des zones infectieuses. Un breacher en armure lourde : il arrache son armure quand il est assez touché et revient plus furieux. Les notes de Saison 7 le présentent comme <strong>le mutant le plus formidable</strong>. En S7, il est présent dans la Heavy Infected Zone de Farm.'),
     ('<strong>Ajax</strong>', 'Attaché à Farm par le texte récit de l\'éditeur', 'Tenait Armory avant que Renoir ne s\'en empare ; le texte de la Saison 2 l\'oppose à l\'Abyss sur Farm. Apparaît au Motel, aux Étables et parfois à la Loading Area. Le mot « boss » n\'est pas employé par l\'éditeur — ses caractéristiques et son jeton (Pocket Knife) viennent du wiki.'),
   ],
 },
 'pages/map-tv-station.html': {
   'anchor': '3. Les trois boss de la station',
   'title': 'Les trois boss de TV Station',
   'rows': [
     ('<strong>Kurt</strong>', 'Nommé boss par l\'éditeur', 'Chef des boss de TV Station, « heavy assault weapons and explosives ». Repérable à son AUG au laser bleu-violet, chargeurs tambour de 60 coups et munitions T4. Casque T5 03 Heavy ou IND200 T4. Jeton : <strong>Combat Compass</strong>. Ses gardes manient des ACE31 en PS et portent des harnois T5 H-Tac A8.'),
     ('<strong>Rolf</strong>', 'Nommé boss par l\'éditeur', '« Fast and deadly with melee ». L\'éditeur le décrit comme le boss de TV Station qui charge au corps à corps — c\'est ce qui le distingue des deux autres.'),
     ('<strong>Bernard</strong>', 'Nommé boss par l\'éditeur', '« A highly accurate sniper ». Utilise un M110 en M80 T4 et un G18 en AP6.3. Harnois TM2 ou T6 Tactical Armored Rig, casque audio GS2. Très précis, dangereux à toute distance. Jeton : <strong>Airborne Badge</strong>. Ses gardes manient des Mini 14 modifiés en M855.'),
   ],
   'after': '''          <div class="callout callout-info">
            <h3 class="h4">Trois boss d'un coup</h3>
            <p>TV Station est la seule carte où l'éditeur a nommé <strong>plusieurs boss pour la même carte</strong> : Kurt, Rolf et Bernard ont été présentés ensemble le 27 avril 2025, et l'éditeur a précisé qu'ils pouvaient apparaître simultanément. En Saison 6, en Hostile Sector, les trois étaient réellement possibles dans un même raid — mais le Hostile Sector n'est pas disponible en S7. Le Boss Rally, lui, reste un événement de Forbidden Zone : plusieurs boss apparaissent alors sur la carte, sans qu'aucune probabilité ne soit publiée.</p>
          </div>''',
 },
 'pages/map-northridge.html': {
   'anchor': '5. Fred, le boss de la crête',
   'title': 'Fred, le boss de Northridge',
   'rows': [
     ('<strong>Fred</strong>', 'Nommé boss par l\'éditeur', 'Tient l\'hôtel Northridge avec une escouade depuis l\'arrivée de la carte (27 avril 2025). MoreFun le décrit comme le <strong>boss principal de la carte</strong>, avec un armement varié et un casque et une armure T4. Apparaît à l\'hôtel, au Campus Services ou à la Cable Car Station. Son jeton est l\'« Frade\'s Wedding Ring ».'),
   ],
   'after': '''          <div class="callout callout-warning">
            <h3 class="h4">Le boss melee anonyme</h3>
            <p>En janvier 2026, un événement de Combat Melee-Only sur Northridge a fait apparaître au centre de la piscine un boss <strong>non nommé</strong>. Remarque : l\'éditeur ne l\'a jamais appelé, et il lâche systématiquement une Keycard Chain universelle. Vous le reconnaissez à son arme melee — pas à un nom.</p>
          </div>''',
 },
}

for f, data in PAGES.items():
    p = pathlib.Path(f)
    s = p.read_text(encoding='utf-8')
    if 'boss-officiel-table' in s:
        print('deja traite :', f)
        continue

    rows = '\n'.join(
        '                <tr><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in data['rows'])

    block = '''

          <h2 id="boss-officiel-table">%s — ce que dit l'éditeur</h2>
          <p>La distinction entre ce que l'éditeur a <em>dit</em> et ce que la communauté <em>rapporte</em> compte. Le tableau ci-dessous s'appuie sur la revue exhaustive des <strong>483 publications de MoreFun Studios</strong> menée au 1er novembre 2026 : chaque nom de boss vient d'une publication officielle datée.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Nom</th><th>Statut</th><th>Ce que l'éditeur en dit</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>
%s
''' % (data['title'], rows, data.get('after', ''))

    # inserer apres la section d'ancrage
    if data.get('h3'):
        # le titre est un h3 dans un callout : on insere apres la fermeture du div
        m = re.search(r'<h3 class="h4">' + re.escape(data['anchor']) + r'</h3>.*?</div>', s, re.S)
        if not m:
            print('ancre h3 introuvable :', f)
            continue
        pos = m.end()
    else:
        m = re.search(r'<h[23][^>]*id="[^"]*"[^>]*>' + re.escape(data['anchor']) + r'</h[23]>', s)
        if not m:
            print('ancre introuvable :', f, '->', data['anchor'])
            continue
        rest = s[m.end():]
        nxt = re.search(r'\n\s*<h2 ', rest)
        pos = m.end() + nxt.start() if nxt else m.end()
    s = s[:pos] + block + s[pos:]
    p.write_text(s, encoding='utf-8')
    print('enrichi :', f)
