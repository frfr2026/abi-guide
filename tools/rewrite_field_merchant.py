#!/usr/bin/env python3
"""Reecrit la section Field Merchants de guide-traders avec les regles officielles S7.

Sources :
- Annonce de mise a jour S7 (15 septembre 2026)
- Notes beta S7 (8 septembre 2026)

Regles officielles : 1 marchand par raid, interactif 5 minutes apres le debut ;
achat et vente cumulent un volume de transactions qui debloque l'intel ;
mystery cargo a prix bas = rendement stable, a prix eleve = resultats polarises ;
en Zombie Endless la devise est le zombie token.

Le « +20 % sur les objets dore » est une donnee COMMUNIAUTAIRE, non confirmee.
"""
import pathlib, re

P = pathlib.Path('pages/guide-traders.html')
s = P.read_text(encoding='utf-8')

NEW = '''<h2 id="field">4. Field Merchants en raid (S7) — le marchand de la raid</h2>
<div class="callout callout-biohazard">
  <h3 class="h4">Nouveauté Utopia</h3>
  <p>La Saison 7 a introduit le premier marchand <strong>opérable pendant la raid</strong>. Jusqu'ici,
  tout le commerce se faisait <em>après</em> l'extraction, chez un contact ou sur le Market. Le Field
  Merchant casse cette règle : vous vendez votre loot au milieu de la raid pour libérer de l'espace, ou
  vous tentez le <strong>mystery cargo</strong>. <span class="src-tag src-officiel">Officiel</span></p>
</div>
<div class="table-wrap">
  <table class="data-table">
    <caption>Field Merchant — les règles publiées par l'éditeur</caption>
    <thead><tr><th scope="col">Règle</th><th scope="col">Ce que dit l'officiel</th></tr></thead>
    <tbody>
      <tr><td><strong>Nombre</strong></td><td>1 marchand par raid, <strong>interactif 5 minutes après le début</strong> de la raid</td></tr>
      <tr><td><strong>Où</strong></td><td>Jeu principal, Infected Zone <em>et</em> Zombie Endless</td></tr>
      <tr><td><strong>Vendre</strong></td><td>Des fournitures lootées, pour <strong>gagner de la place dans le sac</strong></td></tr>
      <tr><td><strong>Acheter</strong></td><td>Du <strong>mystery cargo</strong> — une boîte aveugle, un pari</td></tr>
      <tr><td><strong>Intel</strong></td><td>Acheter <em>et</em> vendre cumule un <strong>volume de transactions</strong> ; atteindre un certain volume <strong>débloque de l'intel</strong></td></tr>
      <tr><td><strong>Zombie Endless</strong></td><td>La devise n'est pas le Koen mais le <strong>zombie token</strong> : fournitures et contre-mesures zombie</td></tr>
    </tbody>
  </table>
</div>
<p>L'officiel a résumé la mécanique en une phrase : <em>« As you build favor through trading, the merchant
may also provide you with highly valuable battlefield and item intel. »</em> Autrement dit :
<strong>plus vous échangez, plus vous méritez l'intel</strong>. Le seuil exact n'a pas été publié — c'est
une donnée non confirmée jusqu'aux notes complètes ou à l'affichage en jeu. <span class="src-tag src-officiel">Officiel</span></p>
<h3 class="h4">Le risk ladder du mystery cargo</h3>
<ul>
  <li><strong>Prix bas</strong> — « offers more stable overall returns ». L'option du grind : plusieurs
    boîtes, un rendement modeste mais régulier. C'est le seul achat qui ne casse pas une économie.</li>
  <li><strong>Prix élevé</strong> — « much more polarized results, with a chance to make a fortune but
    also a significant risk of loss ». La septic jackpot peut tout vider. L'éditeur recommande
    explicitement de <strong>réunir l'intel avant</strong> d'acheter les boîtes chères. <span class="src-tag src-officiel">Officiel</span></li>
</ul>
<div class="callout callout-warning">
  <h3 class="h4">Le « +20 % sur les objets dorés » : à prendre pour un bruit de lobby</h3>
  <p>Vous circuler sur Reddit d'un <strong>bonus forfaitaire de 20 %</strong> pour les objets à fond
  doré ou jaune vendus en raid au Field Merchant. C'est un chiffre <strong>communautaire</strong> :
  <strong>ni l'annonce de la saison ni les notes de patch ne mentionnent aucun pourcentage de prime</strong>.
  Ce que l'éditeur confirme, c'est le mécanisme de volume de transactions et le déblocage d'intel.
  <span class="src-tag src-communautaire">Communautaire</span></p>
  <p>Conséquence pratique : ne bâtissez pas votre plan de farm sur une prime de 20 %. Ce qui est
  vérifié, c'est que <strong>vendre libère de la place et construit la faveur</strong> — les deux
  choses qui comptent réellement.</p>
</div>
<h3 class="h4">La boucle qui rapporte vraiment</h3>
<ol>
  <li><strong>Lootez normalement</strong> en priorité sur les zones denses.</li>
  <li><strong>Repérez le marchand</strong> et vendez votre surplus — ça libère des cases <em>et</em>
    ça construit la faveur.</li>
  <li><strong>Encaissez l'intel</strong> quand il tombe : caches haute valeur marqués sur la carte.</li>
  <li><strong>Utilisez l'intel</strong> pour décider si une boîte chère vaut le pari.</li>
  <li><strong>Ce n'est qu'à ce moment-là</strong> que la grosse boîte devient un pari raisonnable.</li>
</ol>
<div class="callout callout-success">
  <h3 class="h4">Trois usages selon votre profil</h3>
  <ul>
    <li><strong>Orientation loot :</strong> vendez le surplus, gamblez sur les boîtes chères seulement une
      fois l'intel en poche. C'est de la valeur quasi gratuite.</li>
    <li><strong>PvP agressif :</strong> le marchand est un arrêt en cours de route, pas un plan. Les
      combats d'abord, le commerce ensuite.</li>
    <li><strong>Zombie Endless :</strong> ce n'est pas un comptoir de spéculation mais un <strong>point de
      ravitaillement</strong> — jetez vos zombie tokens dans les contre-mesures pour tenir plus longtemps.</li>
  </ul>
</div>
'''

# bornes : du <h2 id="field"> jusqu'au <h2 id="erreurs">
m = re.search(r'\n([ \t]*)<h2 id="field">.*?(?=\n[ \t]*<h2 id="erreurs">)', s, re.S)
if not m:
    raise SystemExit('bornes de section Field Merchant introuvables')
old_block = m.group(0)
indent = re.match(r'\n([ \t]*)', old_block).group(1)
new_block = '\n' + indent + NEW.replace('\n', '\n' + indent)
s = s[:m.start()] + new_block + s[m.end():]

OLD_ROW = '<tr><td>Objet doré en raid</td><td>Field Merchant S7</td><td>+20 % forfaitaire, cash sécurisé</td></tr>'
NEW_ROW = '<tr><td>Fournitures encombrantes</td><td>Field Merchant en raid</td><td>Libère des cases et construit la faveur qui débloque l\'intel</td></tr>'
if OLD_ROW in s:
    s = s.replace(OLD_ROW, NEW_ROW)
else:
    print('ligne de synthese non trouvee')

s = s.replace('Field Merchants +20 % : le guide complet pour transformer vos loots en Koen optimal sur Arena Breakout Infinite.',
              'Field Merchants, intel et mystery cargo : le guide complet pour transformer vos loots en Koen optimal sur Arena Breakout Infinite.')

P.write_text(s, encoding='utf-8')
print('guide-traders.html : section Field Merchant reecrite sur les regles officielles')
