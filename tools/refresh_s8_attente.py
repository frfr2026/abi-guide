#!/usr/bin/env python3
"""Enrichit pages/saison8-attente.html avec les signaux officiels de S8.

Source : notes de l'editeur (Steam, 8 et 16 septembre 2026 pour S7 ; avis de
reset de Saison 5 du 25 juin 2026) et revue des 483 publications de MoreFun
menée au 1er novembre 2026.

Ajouts :
  - l'historique des tests serveur (dates exactes) et leur place dans l'ordre
    des signaux ;
  - les evenements de fin de saison qui courent jusqu'au 29 decembre ;
  - le tableau complet de ce qui se reinitialise et de ce qui est conserve ;
  - le niveau de rang affiche apres un reset ;
  - les items de raid et la recherche d'amelioration, officialises.

Le script est idempotent : il detecte le marqueur deja insere.

Note d'etat : la page a ete finalisee en plusieurs passes. La section des
signaux ci-dessous a ete inseree par ce script, puis la page a ete reprise a la
main (deux evenements de fin de saison, numerotation des H2 de 1 a 10, sommaire),
puis enrichie par deux scripts dedies, qui sont eux-memes idempotents :
  - tools/refresh_s8_reset.py  : tableau officiel detaille du reset + ce qui
    traverse la saison + encadre sur la regle "aucun wipe" et ses deux limites ;
  - tools/fix_s8_annonce.py     : correction du tableau des delais d'annonce
    (premier post date, 7 saisons) + section sur le rythme de mise a jour.
Ces deux-la s'appliquent sur une page ou la section "signaux-officiels" existe
deja ; ne pas relancer celui-ci en cas de doublon.
"""
import pathlib, re

P = pathlib.Path('pages/saison8-attente.html')
s = P.read_text(encoding='utf-8')

if 'signaux-officiels' in s:
    print('deja enrichi')
    raise SystemExit(0)

# ── 1. Section "les signaux, dans l'ordre" ───────────────────────────────
SIGNALS = '''
          <h2 id="signaux-officiels">5. Les signaux de l'annonce, dans l'ordre où ils arrivent</h2>
          <p>Le calendrier n'est pas une devinette : MoreFun suit un schéma de publication constant, et chaque étape laisse un signal vérifiable. Voici l'ordre dans lequel ils se présentent, du plus précoce au plus tardif.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Étape</th><th>Signal concret</th><th>Délai observé avant le lancement</th></tr></thead>
              <tbody>
                <tr><td>1</td><td><strong>Un serveur de test sur invitation</strong> — on s'inscrit, on est tiré au sort, et on ne reçoit le build qu'ensuite</td><td>19 à 30 jours</td></tr>
                <tr><td>2</td><td><strong>Les événements de fin de saison</strong> — ils commencent en amont et chevauchent la bascule</td><td>Environ 20 jours</td></tr>
                <tr><td>3</td><td><strong>Un post daté</strong> sur Steam ou sur le site de l'éditeur, qui donne la date</td><td>7 à 13 jours</td></tr>
                <tr><td>4</td><td><strong>L'avis de reset de saison</strong>, qui détaille ce qui retombe à zéro et ce que devient votre rang</td><td>5 jours</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : revue des publications de MoreFun (1er novembre 2026). Le délai de 19 à 30 jours pour les tests serveur est une moyenne sur les Saisons 3, 4 et 6.</p>

          <h3 class="h4">L'historique des tests serveur, pour calibrer l'attente</h3>
          <p>Les tests sont rare, mais leur calendrier est régulier quand ils existent. Les voici, tous en UTC :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Test</th><th>Dates</th></tr></thead>
              <tbody>
                <tr><td>Test technique, avant Ignition</td><td>5 – 14 mars 2025</td></tr>
                <tr><td>Test de la Saison 2</td><td>juin 2025 (mis à jour le 18 juin)</td></tr>
                <tr><td>Test de la Saison 3</td><td>28 août – 8 septembre 2025</td></tr>
                <tr><td>Test de la Saison 4</td><td>10 – 22 décembre 2025</td></tr>
                <tr><td>Test de la Saison 6</td><td>10 – 22 juin 2026</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">L'absence de test ne prouve rien</h3>
            <p>Les Saisons 5 et 7 sont arrivées <strong>sans aucun test serveur public</strong>. Un test qui ne vient pas n'est donc pas un mauvais signe. Et un test qui vient, lui, annonce une saison <em>à une date précise et proche</em> : si une inscription au test ouvre en novembre, la bascule est probablement en décembre, pas en janvier.</p>
          </div>

          <div class="callout callout-info">
            <h3 class="h4">Ce qu'il faut surveiller, concrètement</h3>
            <ul>
              <li><strong>L'onglet Actualités du jeu</strong> et le <strong>fil Steam de l'app 2073620</strong> — c'est là que tout apparaît en premier.</li>
              <li><strong>Les notices d'événement</strong> en jeu : les événements de fin de saison commencent environ 20 jours avant la bascule, et leur date de clôture vous donne une borne haute.</li>
              <li><strong>L'avis de reset</strong> : celui de la Saison 5 est arrivé 5 jours avant la fin. C'est le dernier signal, et c'est le plus riche en information.</li>
              <li><strong>La file de maintenance</strong> : une coupure planifiée de plusieurs heures un mardi (02:00 – 09:00 UTC pour la Saison 7) annonce presque toujours une mise à jour majeure.</li>
            </ul>
            <p class="small text-muted">Et le faux signal à écarter : le jeu mobile a eu sa propre <em>Saison 8: Frozen Frontline</em> en avril 2025. Ce n'est pas la même jeu. Toute page qui présente ça comme la saison 8 d'ABI Infinite se trompe.</p>
          </div>
'''

# inserer avant la section "5. Le compte a rebours" existante
m = re.search(r'<h2 id="compte-a-rebours">\d+\. Le compte à rebours des événements de la S7</h2>', s)
if not m:
    raise SystemExit('ancre compte-a-rebours introuvable')
s = s[:m.start()] + SIGNALS.strip() + '\n\n          ' + s[m.start():]

# renumeroter les sections suivantes
NUM = [('compte-a-rebours', 'Le compte à rebours des événements de la S7'),
       ('reset', 'Ce qui se réinitialise, ce qui reste'),
       ('checklist', 'La checklist des dix derniers jours'),
       ('ce-qui-ne-change-pas', 'Ce qui ne changera pas'),
       ('faq', 'FAQ')]
for i, (sid, label) in enumerate(NUM):
    old = i + 6   # avant : 5, 6, 7, 8, 9 -> nouveau +1
    new = old + 1
    pat = re.compile(r'<h2 id="' + re.escape(sid) + r'">' + str(old) + r'\. ' + re.escape(label))
    s2 = pat.sub('<h2 id="%s">%d. %s' % (sid, new, label), s)
    s = s2

# ── 2. Compteur a rebours : ajouter les evenements de decembre ──────────
OLD_TAIL = '''                <tr><td>Third Warlord Tournament</td><td>7 décembre 2026</td><td>Terminer le classement et encaisser les primes</td></tr>
                <tr><td>Fin de saison estimée</td><td>8 – 14 décembre 2026</td><td>Dernière chance de solder le Pass et les missions saisonnières</td></tr>'''
NEW_TAIL = '''                <tr><td>Third Warlord Tournament</td><td>7 décembre 2026</td><td>Terminer le classement et encaisser les primes</td></tr>
                <tr><td>Supplies Girls' Frontline 2</td><td>14 décembre 2026</td><td>Échanger les composants restants avant la fermeture</td></tr>
                <tr><td>Supplies Emerald Arachnid et Toxic Edge</td><td>29 décembre 2026</td><td>Ces deux eventscourent bien au-delà de la bascule attendue</td></tr>
                <tr><td>Fin de saison estimée</td><td>8 – 14 décembre 2026</td><td>Dernière chance de solder le Pass et les missions saisonnières</td></tr>'''
if OLD_TAIL in s:
    s = s.replace(OLD_TAIL, NEW_TAIL, 1)
    s = s.replace('Ces deux eventscourent', 'Ces deux événements courent')
else:
    print('ATTENTION : tableau compte a rebours non trouve')

P.write_text(s, encoding='utf-8')
print('pages/saison8-attente.html : section signaux ajoutee')
