#!/usr/bin/env python3
"""Detaille la section "ce qui se reinitialise" de pages/saison8-attente.html.

Source : avis de reset de Saison 5 de MoreFun (25 juin 2026) et notes de la
Saison 7 (16 septembre 2026). La regle officielle est simple : ABI ne fait pas
de wipe. Ce qui tombe a zero est saisonnier, et le detail merite d'etre connu
precisement, parce que c'est lui qui decide de la valeur de votre stuff en fin
de saison.
"""
import pathlib, re

P = pathlib.Path('pages/saison8-attente.html')
s = P.read_text(encoding='utf-8')

if 'reset-detail-officiel' in s:
    print('deja enrichi')
    raise SystemExit(0)

BLOCK = '''
          <h3 class="h4" id="reset-detail-officiel">Le détail officiel, ligne par ligne</h3>
          <p>Le tableau simplifié ci-dessus est un raccourci. Voici la liste exacte, tirée de l'<strong>avis de reset de saison</strong> que l'éditeur publie quelques jours avant la bascule — celui de la Saison 5 date du 25 juin 2026.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Ce qui retombe à zéro</th><th>Détail</th></tr></thead>
              <tbody>
                <tr><td><strong>Le rang</strong></td><td>Il redescend selon une table propre à l'éditeur. La dernière fois : <strong>Legend est retombé à Master I</strong>, Hero I et II à Master II, et <strong>Vanguard I et en dessous restent inchangés</strong>. Autrement dit : le plafond de prestige retombe, mais le bas du classement ne bouge pas.</td></tr>
                <tr><td><strong>Les Core Masteries</strong></td><td>Ceux ajoutés en S7 — <strong>Acoustic Earpads</strong>, <strong>Tactical Belt</strong>, <strong>Hidden Compartment</strong> — sont remis à zéro chaque saison. Ils ne consomment pas de points : ils se débloquent en remplissant les missions de la saison et on en équipe un seul à la fois.</td></tr>
                <tr><td><strong>Les season kits</strong></td><td>Les kits expérimentaux sont <strong>retirés à la fin de la saison</strong> : le <em>M110 binary trigger</em>, le <em>MPX Vulcan barrel</em>, le <em>FAL burst kit</em> et le <em>PCC-9 fully-automatic kit</em>. L'éditeur annonce une nouvelle série de kits pour d'autres armes la saison suivante. Le stock non équipé est perdu.</td></tr>
                <tr><td><strong>Les résultats de l'Improvement Research</strong></td><td>La recherche d'amélioration est remise à zéro chaque saison : elle ne vous sert que pour la saison où vous l'avez faite.</td></tr>
                <tr><td><strong>Les Skin Supply Coupons</strong></td><td>Les coupons de la saison précédente cessent de fonctionner. En revanche, la <strong>progression de tirage</strong> est conservée — elle a déjà survécu aux passages S3 → S4 et S4 → S5.</td></tr>
                <tr><td><strong>Les événements de fin de saison</strong></td><td>Limités aux derniers jours, ils ne se|reportent pas.</td></tr>
                <tr><td><strong>Le Battle Pass</strong></td><td>Chaque saison a son propre pass.</td></tr>
              </tbody>
            </table>
          </div>
          <p class="small text-muted">Source : avis de reset de Saison 5 de MoreFun (25 juin 2026) et notes de la Saison 7 (16 septembre 2026).</p>

          <h3 class="h4">Ce qui traverse la saison, point par point</h3>
          <ul>
            <li><strong>Votre niveau de personnage</strong> — et avec lui vos 12 Mastery Points si vous étiez au niveau maximum : l'éditeur a précisé que vous les récupérez intégralement au niveau max, sans rien avoir à regagner.</li>
            <li><strong>Vos choix de maîtrises ordinaires</strong> — ils se réinitialisent gratuitement hors raid, avec restitution intégrale de chaque point. Il n'y a donc rien à perdre de ce côté non plus.</li>
            <li><strong>La progression de tirage du Skin Supply</strong> — déjà conservée de la S3 à la S4 puis de la S4 à la S5.</li>
            <li><strong>Le Zombie Research</strong> — les points de recherche de l'Infected Zone sont <strong>permanents pour ce mode</strong> et ne peuvent pas être réinitialisés.</li>
            <li><strong>La progression du Zombie Endless</strong> — chaque niveau de croissance débloque une capacité conservée définitivement dans ce mode.</li>
          </ul>

          <div class="callout callout-info">
            <h3 class="h4">La règle de l'éditeur, et sa limite</h3>
            <p>Au lancement complet du jeu sur Steam, le 16 septembre 2025, l'éditeur a répondu dans sa FAQ qu'<strong>aucun wipe n'était prévu</strong>. Aucune publication ultérieure, sur Steam ou sur son site, n'en a annoncé un : les Saisons 4, 5, 6 et 7 ont toutes commencé sans wipe.</p>
            <p>Deux nuances, et deux seulement. D'abord, l'éditeur a dit « <em>actuellement</em> il n'y a pas de plan de wipe » — c'est une réserve, pas une promesse éternelle. Ensuite, et c'est le point que les guides ignorent souvent : <strong>un événement de fin de saison peut survivre à la saison</strong>. La Saison 6 s'est terminée le 16 septembre, et l'un de ses événements de fin était encore daté au 30 septembre. Une date de clôture d'événement est donc un indice, pas une garantie.</p>
          </div>
'''

ANCHOR = '''          <div class="callout callout-success">
            <h3 class="h4">Ce que cela change pour votre budget</h3>'''
assert ANCHOR in s
s = s.replace(ANCHOR, BLOCK.strip() + '\n\n' + ANCHOR, 1)

P.write_text(s, encoding='utf-8')
print('pages/saison8-attente.html : section reset detaillee')
