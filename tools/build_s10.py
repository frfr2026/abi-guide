import sys
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Objets')

# ───────────────────────────────────────────── 1. COSMETIQUES PERSONNAGE
perso = """
          <figure class="page-figure">
            <img src="../img/personnages/emerald-operator.jpg" alt="Opératrice au masque arachne émeraude" loading="lazy">
            <figcaption>Les cosmétiques de personnage : l'apparence ne donne aucun avantage — mais dans une salle d'extraction, c'est la première chose que l'on remarque.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Impact gameplay</span><span class="fact-value">Aucun — strictement cosmétique</span></div>
            <div class="fact"><span class="fact-label">Supply S7</span><span class="fact-value">Emerald Arachnid + Toxic Edge</span></div>
            <div class="fact"><span class="fact-label">Premier tirage</span><span class="fact-value">Gratuit pour chaque Supply</span></div>
            <div class="fact"><span class="fact-label">Fenêtre</span><span class="fact-value">Mise à jour S7 → 29 décembre 2026</span></div>
          </div>

          <h2 id="regles">1. La règle d'or du cosmétique</h2>
          <p>Aucun cosmétique d'ABI n'améliore vos statistiques. Un skin de fusil, une tenue d'opérateur, un spray, un banner, un fond : <strong>zéro pixel de gameplay</strong>. Les seuls objets qui modifient votre performance sont les <strong>attachements</strong> et les <strong>season kits</strong>.</p>
          <div class="callout callout-warning">
            <h4>Ce qui est interdit à la vente</h4>
            <p>Ni le <strong>Koen</strong> ni la puissance de combat ne sont en vente. Les <strong>Bonds</strong> achètent des cosmétiques, des passes et de la commodité — rien de plus. C'est une règle de conception affichée par l'éditeur, et la raison pour laquelle chasing un skin ne coûte jamais de performance.</p>
          </div>

          <h2 id="supplies">2. Les Supplies de la Saison 7</h2>
          <p>Deux Supplies thématiques ont lancé la S7, tous deux le <strong>16 septembre 2026</strong>, sur une fenêtre qui court jusqu'au <strong>29 décembre</strong> :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Supply</th><th>Type</th><th>Récompenses principales</th></tr></thead>
              <tbody>
                <tr><td><strong>Emerald Arachnid</strong></td><td>Supply Personnage (Character)</td><td>Personnage exclusif <strong>Emerald Web Arachne</strong>, skins Emerald Arachnid P90, Emerald Web FAMAS, Emerald Web M14, skin de projectile Emerald Arachnid GLI-F4</td></tr>
                <tr><td><strong>Toxic Edge</strong></td><td>Supply Mélée (Melee)</td><td><strong>Venomfang Tactical Karambit</strong>, skins Venomfang AEK et Venomfang SCAR-L, Toxic Edge Gear Skin, skin de projectile Toxic Edge M67</td></tr>
                <tr><td><strong>Hazmat Suit</strong></td><td>Supply Tenue (Outfit)</td><td>Tenue <strong>Hazmat Suit</strong> + Hazmat Suit Gear Skin, skins Hazmat Suit T03 et Hazmat Suit Uzi</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h4>Les conditions d'accès</h4>
            <p>• <strong>Premier tirage gratuit</strong> sur chaque Supply — l'échantillon avant l'investissement.<br>• <strong>80 passes échangeables en Koen</strong> sur chaque Supply.<br>• <strong>10 Emerald Arachnid Supply Pass + 10 Toxic Edge Supply Pass gratuits</strong> pour tout joueur de <strong>niveau 10 ou plus</strong>, sur la page de l'événement.<br>• Le premier tirage gratuit <strong>ne garantit pas</strong> la récompense vedette : la trailer l'annonce sans le préciser.</p>
          </div>

          <h2 id="memoirs">3. Arachne's Web Memoirs</h2>
          <p>L'événement thématique d'<strong>Emerald Arachnid</strong> se joue à travers une série de missions de défis qui rapportent des <strong>Toxic-G Tokens</strong>, échangeables sur l'écran de l'événement :</p>
          <ul>
            <li><strong>Arachne's Web Jacket II</strong>, <strong>Glasses II</strong> et <strong>Mask II</strong> — personnalisation exclusive du personnage.</li>
            <li><strong>Universal Keycard Chain</strong> — la chaîne de carte d'accès universelle, qui elle-même ouvre n'importe quelle porte une fois.</li>
            <li><strong>Emerald Web Spray</strong> et l'<strong>Emerald Arachnid Tag</strong> — objets de personnalisation liés au thème.</li>
            <li>Terminer <strong>toutes</strong> les missions débloque une <strong>histoire exclusive au personnage</strong>.</li>
          </ul>
          <div class="callout callout-success">
            <h4>Le set Endless Weave</h4>
            <p>Si vous possédez <strong>à la fois</strong> le personnage Emerald Web Arachne et le couteau Venomfang Tactical Karambit, vous débloquez le <strong>background Endless Weave</strong> et le <strong>Endless Weave Set Part Bundle</strong> (Glasses / Mask / Jacket). C'est le parcours de complétion le plus rentable de la saison.</p>
          </div>

          <h2 id="pass">4. Les cosmétiques du Battle Pass</h2>
          <p>La piste du pass saisonnier distribue des cosmétiques de personnage, des <strong>designs de flashbang</strong>, des skins d'armes (M4A1, Banshee, MPX…) et de l'<strong>avatar animé premium</strong> dans les versions haut de gamme. La Saison 7 ajoute plusieurs designs inspirés du thème <strong>Avita</strong>.</p>
          <ul>
            <li><strong>Tacti-Girl Desert Eagle</strong> — skin d'arme obtenu via les <strong>top-ups de Bonds</strong> ou l'achat d'une valeur équivalente (avec <strong>Coin Raid Voucher ×10</strong> et une <strong>Premium Elite Card 30 jours</strong>).</li>
            <li><strong>Tacti-Girl Athletic Jacket</strong> — veste personnalisée, même série.</li>
            <li><strong>Challenger Banner</strong> et le spray <strong>Smoke Rises</strong> — via le Défi de Merit et le check-in quotidien.</li>
            <li><strong>Infiltration Mode Background</strong> — fond exclusif S7, via les missions de saison.</li>
          </ul>

          <h2 id="decorations">5. Les décorations du Trophy Room</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Objet</th><th>Comment l'obtenir</th></tr></thead>
              <tbody>
                <tr><td><strong>Central Sculpture: Destruction and Rebirth</strong></td><td>Missions « Enter Infected Area »</td></tr>
                <tr><td><strong>Central Piece: Revolution</strong></td><td>Missions « Enter Infected Area »</td></tr>
                <tr><td><strong>Infected Area Frame</strong></td><td>Élément de personnalisation thématique, missions zone infectée</td></tr>
                <tr><td><strong>Infected Area Background</strong></td><td>Missions (aussi via le RPK-16 Catastrophe Survivor)</td></tr>
                <tr><td><strong>Endless Weave Background</strong></td><td>Personnage Emerald Web Arachne <em>et</em> Venomfang Karambit</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="gratuit">6. Comment tout avoir gratuitement</h2>
          <p>Le pass premium n'est pas la seule source. La quasi-totalité des cosmétiques S7 est atteignable <strong>sans dépenser un centime</strong> :</p>
          <ol>
            <li><strong>Check-in quotidien</strong> — Pixel Soldier AKM, Pixelated Battlefield AK-74N, 15 vouchers, 15 Skin Supply Coupons, 4 Golden Gift Box, banner et spray.</li>
            <li><strong>7 / 14 / 21 jours de connexion</strong> — la <strong>Obstacle Clearing Sapper Shovel</strong> et ses évolutions (2 Dazzling Tokens), plus 2 skins de mêlée gratuits (Clearing Sapper Shovel et Battleforged Clearing Shovel) échangeables dans le menu Customize.</li>
            <li><strong>Événement Zombie No Man's Land</strong> — skin Pixel Soldier Uzi, 20 Skin Supply Coupons, 20 vouchers, titre <strong>S7 Wealthy Winner</strong>, Lunar Soil Sample.</li>
            <li><strong>Missions de saison</strong> — Black Rock Shooter ML Lever-Action, Basic Elite Trial Card 30j, 3×3 Titanium Case, Infiltration Mode Background.</li>
            <li><strong>Missions zone infectée</strong> — décorations Trophy Room, Koen, Coin Raid Vouchers, RPK-16 Catastrophe Survivor, Elysium.</li>
            <li><strong>Pass gratuit</strong> — des millions de Koen et des cosmétiques sur la piste gratuite.</li>
            <li><strong>Partage de formules</strong> — les blueprints d'assistance de vos amis financent vos recherches.</li>
          </ol>
          <div class="callout callout-success">
            <h4>La règle des 10 jours</h4>
            <p>Connectez-vous <strong>7 jours d'affilée</strong> pour la pelle, <strong>14</strong> et <strong>21</strong> jours pour ses évolutions. C'est le meilleur ratio valeur/temps de toute la saison : une connexion quotidienne pendant trois semaines vous offre une arme de mêlée évolutive et deux skins.</p>
          </div>

          <h2 id="conseils">7. Conseils de dépense</h2>
          <ul>
            <li><strong>N'achetez jamais un Supply avant le premier tirage gratuit</strong> — c'est le seul échantillon gratuit de la pool.</li>
            <li><strong>Un seul Supply à la fois</strong> : la diluer sur deux pools divise vos chances d'avoir le set complet.</li>
            <li><strong>Les passe-coins deKoen</strong> : si vous achetez 80 passes en Koen, comparez avec le prix du Skin Supply Coupon (qui s'obtient gratuitement en mission) avant de payer en Bonds.</li>
            <li><strong>Gardez vos Bonds pour l'expiration</strong> : un lot de 1 350 Supply Pass équivaut à 20 tirages (20 × 1 350 = 27 000 passes). L'obtention d'un premier skin vous donne en plus une remise sur le second.</li>
            <li><strong>La tenue</strong> n'affecte pas la performance : n'achetez jamais un skin d'arme pour une arme que vous ne sortez jamais.</li>
          </ul>
          <p>Pour les skins d'armes en détail, voir <a href="cosmetiques-skins-armes.html">le guide des skins d'armes</a>. Pour les plaques d'identité, voir <a href="cosmetiques-dog-tags.html">le guide des dog tags</a>.</p>
"""

page('cosmetiques-skins-perso.html',
     "Cosmétiques — Personnage",
     "Cosmétiques personnage ABI Saison 7 : Supply Emerald Arachnid et Toxic Edge, personnage Emerald Web Arachne, Venomfang Karambit, Arachne's Web Memoirs, décorations Trophy Room et Obtainable gratuitement.",
     "../img/personnages/emerald-operator.jpg",
     "Cosmétiques — Personnage", "Cosmétiques de personnage",
     "Emerald Arachnid, Toxic Edge, Hazmat Suit : les sets de la saison, et comment les obtenir gratuitement.",
     perso,
     [("regles", "1. La règle d'or"), ("supplies", "2. Les Supplies S7"), ("memoirs", "3. Arachne's Web Memoirs"),
      ("pass", "4. Cosmétiques du pass"), ("decorations", "5. Décorations Trophy Room"), ("gratuit", "6. Tout avoir gratuitement"),
      ("conseils", "7. Conseils de dépense")],
     extra_js=False, nav=NAV, crumb=('Cosmétiques', 'cosmetiques-skins-perso.html'))

# ───────────────────────────────────────────── 2. SKINS D'ARMES
armes = """
          <figure class="page-figure">
            <img src="../img/events/s7-battle-pass.jpg" alt="Récompenses holographiques du Battle Pass" loading="lazy">
            <figcaption>Les skins d'armes de la Saison 7 : un zoo de variantes, et six chemins différents pour les obtenir.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Impact</span><span class="fact-value">Aucun sur les statistiques</span></div>
            <div class="fact"><span class="fact-label">Sets S7</span><span class="fact-value">Pixel · Shooting Star Panorama · Streamlined · Emerald · Venomfang · Hazmat</span></div>
            <div class="fact"><span class="fact-label">Nouveau pool</span><span class="fact-value">+6 skins dans le Skin Supply</span></div>
            <div class="fact"><span class="fact-label">Carried over</span><span class="fact-value">Progression de tirage S6 conservée</span></div>
          </div>

          <h2 id="regles">1. Un skin ne change rien — sauf si le jeu le décide</h2>
          <p>Un skin d'arme est purement visuel : mêmes dégâts, même recul, même cadence. La seule nuance : certains skins d'armes ont une <strong>variante « évoluée »</strong> accessible par <strong>Weapon Evolution</strong>, un système de saison qui transforme l'apparence au fil des utilisations ou d'un événement de saison.</p>
          <div class="callout callout-warning">
            <h4>Attention à la confusion</h4>
            <p>Les <strong>season kits</strong> (PCC-9 Full-Auto, M110 Dual-Stage, FAL Recoil Kit, MPX Vulcan) modifient <strong>réellement</strong> l'arme. Un skin, jamais. Ne confondez jamais un « skin » (cosmétique) et un « kit » (attachement saisonnier).</p>
          </div>

          <h2 id="table">2. Le catalogue des skins S7</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Skin</th><th>Arme</th><th>Set</th><th>Comment l'obtenir</th></tr></thead>
              <tbody>
                <tr><td><strong>Pixel Soldier</strong></td><td>AKM</td><td>Pixel</td><td>Check-in quotidien / Défi de Merit</td></tr>
                <tr><td><strong>Pixelated Battlefield</strong></td><td>AK-74N</td><td>Pixel</td><td>Check-in quotidien / Défi de Merit</td></tr>
                <tr><td><strong>Pixel Soldier</strong></td><td>Uzi Micro SMG</td><td>Pixel</td><td>Événement Zombie No Man's Land</td></tr>
                <tr><td><strong>Shooting Star Panorama</strong></td><td>Banshee SMG</td><td>Shooting Star</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Shooting Star Panorama</strong></td><td>SPR310 (fusil à pompe double canon)</td><td>Shooting Star</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>MPX Micro SMG</td><td>Streamlined</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>Mk14 (fusil de précision)</td><td>Streamlined</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>SKS (carabine)</td><td>Streamlined</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>F57 (pistolet)</td><td>Streamlined</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Black Rock Shooter</strong></td><td>ML Lever-Action</td><td>—</td><td>Missions de saison</td></tr>
                <tr><td><strong>Catastrophe Survivor</strong></td><td>RPK-16 LMG</td><td>Infected Area</td><td>Missions zone infectée</td></tr>
                <tr><td><strong>Emerald Arachnid</strong></td><td>P90 Micro SMG</td><td>Emerald</td><td>Supply Emerald Arachnid</td></tr>
                <tr><td><strong>Emerald Web</strong></td><td>FAMAS</td><td>Emerald</td><td>Supply Emerald Arachnid</td></tr>
                <tr><td><strong>Emerald Web</strong></td><td>M14</td><td>Emerald</td><td>Supply Emerald Arachnid</td></tr>
                <tr><td><strong>Emerald Arachnid</strong></td><td>GLI-F4 (gaz lacrymogène)</td><td>Emerald</td><td>Supply Emerald Arachnid</td></tr>
                <tr><td><strong>Venomfang</strong></td><td>AEK</td><td>Toxic Edge</td><td>Supply Toxic Edge</td></tr>
                <tr><td><strong>Venomfang</strong></td><td>SCAR-L</td><td>Toxic Edge</td><td>Supply Toxic Edge</td></tr>
                <tr><td><strong>Toxic Edge</strong></td><td>M67 (grenade frag)</td><td>Toxic Edge</td><td>Supply Toxic Edge</td></tr>
                <tr><td><strong>Hazmat Suit</strong></td><td>T03</td><td>Hazmat</td><td>Supply Hazmat Suit</td></tr>
                <tr><td><strong>Hazmat Suit</strong></td><td>Uzi Micro SMG</td><td>Hazmat</td><td>Supply Hazmat Suit</td></tr>
                <tr><td><strong>Tacti-Girl</strong></td><td>Desert Eagle</td><td>Tacti-Girl</td><td>Top-ups de Bonds / valeur équivalente</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="sets">3. Les sets : la logique de complétion</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Streamlined — 5 armes</h3>
              <p class="card-text">Le set le plus large de la saison : MPX, Mk14, SKS, F57. Completement visuel mais cohérent sur 4 calibres différents — c'est le set des collectionneurs.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Shooting Star Panorama — 2 armes</h3>
              <p class="card-text">Banshee et SPR310. Petit set, mais deux armes de niche : parfait si vous ne jouez qu'au CQB et au shotgun.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Pixel — 3 armes</h3>
              <p class="card-text">AKM, AK-74N, Uzi. Le set rétro-pixel <strong>entièrement gratuit</strong> via le check-in et l'événement No Man's Land.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Emerald — 4 objets</h3>
              <p class="card-text">P90, FAMAS, M14 + le skin de projectile GLI-F4. Le set le plus rentable en pass gratuit (10 pass offerts au niveau 10+).</p>
            </div></div>
          </div>

          <h2 id="chemins">4. Les 6 chemins d'obtention</h2>
          <ol>
            <li><strong>Check-in quotidien</strong> — skins Pixel, vouchers, coupons.</li>
            <li><strong>Événement (Zombie No Man's Land, Défi de Merit)</strong> — skins RPK-16, Uzi, AKM, AK-74N, et skins exclusifs de personnage.</li>
            <li><strong>Battle Pass Store + vouchers</strong> — Shooting Star Panorama et Streamlined.</li>
            <li><strong>Missions de saison</strong> — Black Rock Shooter, fond Infiltration, Titanium Case, carte Élite.</li>
            <li><strong>Supplies (Emerald / Toxic Edge / Hazmat)</strong> — sets complets, premier tirage gratuit.</li>
            <li><strong>Top-ups de Bonds</strong> — Tacti-Girl Desert Eagle et veste Athletic Jacket.</li>
          </ol>
          <div class="callout callout-success">
            <h4>La progression de tirage est conservée</h4>
            <p>Si vous étiez à mi-parcours sur un banner de la <strong>Saison 6</strong>, vous reprenez <strong>exactement</strong> où vous vous étiez arrêté. Aucun tirage n'est perdu au changement de saison — c'est rare et très apprécié des collectionneurs.</p>
          </div>

          <h2 id="skinsupply">5. Le Skin Supply et le pool de la saison</h2>
          <ul>
            <li>Le <strong>Skin Supply</strong> de la saison ajoute <strong>6 nouvelles weapon skins</strong> à la pool de tirages.</li>
            <li>Un lot de <strong>1 350 Supply Pass</strong> équivaut à <strong>20 tirages</strong> (20 × 1 350 = 27 000 passes) : c'est la référence pour évaluer le prix d'un skin en Bonds.</li>
            <li>Obtenir <strong>un premier skin</strong> vous accorde une <strong>remise sur l'achat du second</strong> : le premier achat est toujours le plus rentable.</li>
            <li>Les <strong>Season 7 Skin Supply Coupon ×15 et ×20</strong> (check-in et événement) sont l'équivalent gratuit de ces tirages : <strong>utilisez-les en premier</strong>.</li>
          </ul>
          <div class="callout callout-warning">
            <h4>Le lexique à connaître</h4>
            <p><strong>Supply Pass</strong> = un tirage. <strong>Skin Supply Coupon</strong> = un tirage gratuit. <strong>Voucher</strong> (Tacti-Girl Charm Voucher) = un accès à la pool de charms. <strong>Dazzling Token</strong> = la monnaie de l'événement des 7/14/21 jours. <strong>Toxic-G Token</strong> = la monnaie d'Arachne's Web Memoirs. <strong>Bonds</strong> = la devise payante du magasin. <strong>Koen</strong> = la monnaie du jeu, jamais en vente.</p>
          </div>

          <h2 id="evolution">6. Weapon Evolution : la pelle qui évolue</h2>
          <p>C'est la mécanique de <strong>Weapon Evolution</strong> : la <strong>Obstacle Clearing Sapper Shovel</strong> s'obtient en se connectant <strong>7 jours</strong>, puis évolue aux <strong>14</strong> et <strong>21 jours</strong> de connexion. Elle est convertible en <strong>2 skins de mêlée</strong> (Clearing Sapper Shovel et Battleforged Clearing Shovel) via les Dazzling Tokens dans le menu Customize.</p>
          <div class="callout callout-success">
            <h4>Le geste le plus rentable de la saison</h4>
            <p>21 jours de connexion → une arme de mêlée évolutive <strong>et</strong> deux skins de mêlée. Aucun autre contenu de la saison n'offre ce rapport. Si vous ne deviez garder qu'une seule habitude de connexion, c'est celle-ci.</p>
          </div>

          <h2 id="strategie">7. La stratégie d'achat</h2>
          <ul>
            <li><strong>Commencez par le gratuit</strong> : coupons, check-in, événement, missions. Une grande partie du catalogue S7 est accessible sans dépenser.</li>
            <li><strong>Ne chasez que les armes que vous sortez</strong> : un skin du SKS sur une arme que vous ne sortez jamais est un achat mort. Le SKS est une carabine de budget ; le skin Streamlined est un must-have de collectionneur, pas de joueur.</li>
            <li><strong>Préparez le set complet avant de tirer</strong> : sur les sets de 2 à 5 armes, l'obtention d'un premier élément vous donne une remise sur le suivant.</li>
            <li><strong>Gardez des Bonds en réserve</strong> pour la fin de la saison : les banners limités se terminent, les cosmetics ne partent pas.</li>
            <li><strong>Le pass de battle reste rentable</strong> si vous visez l'<strong>avatar animé premium</strong> et la <strong>bannière</strong> — ce sont des éléments uniques que le BP Store ne vend pas.</li>
          </ul>
          <p>Pour le détail des sets de personnage et des Supply, voir <a href="cosmetiques-skins-perso.html">le guide des cosmétiques de personnage</a>. Pour le pass lui-même, voir <a href="saison7-battle-pass.html">le guide du Battle Pass S7</a>.</p>
"""

page('cosmetiques-skins-armes.html',
     "Cosmétiques — Skins d'armes",
     "Catalogue des skins d'armes ABI Saison 7 : Pixel, Shooting Star Panorama, Streamlined, Emerald Arachnid, Venomfang, Hazmat Suit, Black Rock Shooter et RPK-16. Comment les obtenir gratuitement.",
     "../img/events/s7-battle-pass.jpg",
     "Cosmétiques — Armes", "Skins d'armes",
     "21 skins S7, 6 sets complets, 6 chemins d'obtention et une seule règle : ne chasez que vos armes.",
     armes,
     [("regles", "1. Ce qu'est un skin"), ("table", "2. Catalogue S7"), ("sets", "3. Les sets"),
      ("chemins", "4. Chemins d'obtention"), ("skinsupply", "5. Skin Supply & devises"), ("evolution", "6. Weapon Evolution"),
      ("strategie", "7. Stratégie d'achat")],
     extra_js=False, nav=NAV, crumb=('Cosmétiques', 'cosmetiques-skins-perso.html'))

# ───────────────────────────────────────────── 3. DOG TAGS
tags = """
          <figure class="page-figure">
            <img src="../img/items/collection-room.jpg" alt="Étagère de collection de plaques d'identité" loading="lazy">
            <figcaption>Les plaques d'identité : un objet de loot minuscule qui porte pourtant la valeur de votre kill, vos titres et vos sorties de raid.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Source</span><span class="fact-value">Corps des Operators abattus</span></div>
            <div class="fact"><span class="fact-label">Valeur de base</span><span class="fact-value">≈ 500 Koen (rang Rookie)</span></div>
            <div class="fact"><span class="fact-label">Forbidden / Warlord</span><span class="fact-value">70 000 Koen (au lieu de 5 000)</span></div>
            <div class="fact"><span class="fact-label">Novelté S7</span><span class="fact-value">Animations d'inspection + 5 animations Interact</span></div>
          </div>

          <h2 id="quest-ce">1. Qu'est-ce qu'une plaque d'identité ?</h2>
          <p>Les <strong>dog tags</strong> (plaques d'identité) sont de petits objets récupérés sur les <strong>corps des Operators abattus</strong>. Ils occupent un slot minuscule, pèsent 0,11 kg, et portent trois informations : <strong>qui</strong> vous a tué, <strong>avec quelle arme</strong>, et — en jeu — une <strong>valeur</strong> qui dépend du rang du joueur.</p>
          <div class="callout callout-success">
            <h4>Elles ne sont pas que décoratives</h4>
            <p>Les plaques servent à : <strong>1)</strong> payer certaines extractions (extraction <strong>Hel</strong> sur Valley), <strong>2)</strong> remplir l'<strong>étagère de plaques</strong> (Dog Tag Shelf) de votre Trophy Room, <strong>3)</strong> alimenter le <strong>Dog Tag Gachapon</strong> en mode Supplies Drops, <strong>4)</strong> remplir des objectifs de mission, <strong>5)</strong> être revendues.</p>
          </div>

          <h2 id="valeur">2. Combien valent-elles ?</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Contexte</th><th>Valeur</th><th>Commentaire</th></tr></thead>
              <tbody>
                <tr><td>Rookie (rang le plus bas)</td><td>≈ 500 Koen</td><td>La valeur de base, +100 environ par rang</td></tr>
                <tr><td>Mode standard (Normal / Lockdown)</td><td>≈ 5 000 Koen</td><td>La valeur historique des plaques « Battleforged »</td></tr>
                <tr><td><strong>Forbidden &amp; Warlord Tournament</strong></td><td><strong>70 000 Koen</strong></td><td>Multiplicateur ×14 depuis l'introduction du mode Warlord</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Le changement de juillet 2026</h4>
            <p>Les plaques ne valent plus la même chose selon le mode : <strong>5 000 Koen</strong> en modes classiques, <strong>70 000 Koen</strong> en Forbidden et au Warlord Tournament. C'est une volonté assumée de récompenser le PvP à haut risque — mais cela rend les modes Forbidden très rentables pour qui sait les exploiter. La critique de la communauté : le barème n'est pas progressif (Normal bas, Lockdown moyen, Forbidden élevé), ce qui disadvantage les joueurs qui ne jouent qu'en modes accessibles.</p>
          </div>
          <div class="callout callout-callout">
            <h4>Attention aux bots</h4>
            <p>Les <strong>playerbots</strong> des faibles niveaux portent aussi des plaques. Pour distinguer un vrai joueur : un niveau 30, un rang <strong>ace / hero / legend</strong> est toujours un humain, et les bots utilisent presque toujours des kits d'entrée de gamme.</p>
          </div>

          <h2 id="utilises">3. À quoi elles servent vraiment</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Usage</th><th>Détail</th></tr></thead>
              <tbody>
                <tr><td><strong>Extraction Hel (Valley)</strong></td><td>Some extraction points require turning in a certain number of dog tags</td></tr>
                <tr><td><strong>Dog Tag Shelf</strong></td><td>Étagère dédiée dans la Trophy Room ; les plaques y sont exposées et peuvent être « améliorées » en niveau à force de collection</td></tr>
                <tr><td><strong>500 plaques</strong></td><td>La communauté rapporte qu'en sortir 500 en raid ou en secure ops débloque <strong>3 boîtes de plaques</strong> devant le mur de l'étagère</td></tr>
                <tr><td><strong>Gachapon</strong></td><td>Monnaie d'échange du mode Supplies Drops pour un système de tirages à récompense</td></tr>
                <tr><td><strong>Missions</strong></td><td>Certaines tâches hebdomadaires demandent des plaques</td></tr>
                <tr><td><strong>Vente</strong></td><td>500 Koen pièce en mode standard, jusqu'à 70 000 K en Forbidden</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="s7">4. Les nouveautés Saison 7</h2>
          <p>La S7 ne change pas la valeur des plaques, mais elle change <strong>la façon de les manipuler</strong> :</p>
          <ul>
            <li><strong>Inspection</strong> : quand vous portez une plaque (rig de poitrine, poche, sac ou case), un <strong>clic droit</strong> sur son icône fait apparaître un bouton <strong>« Inspect »</strong> qui déclenche l'animation d'inspection de cette plaque.</li>
            <li><strong>Interaction</strong> : le bouton « Interact » déclenche une animation d'inspection <strong>multiple</strong>. Il existe <strong>cinq animations Interact</strong> au total, déterminées par le <strong>nombre de plaques dans votre sac</strong>.</li>
            <li><strong>Marquage rouge restreint</strong> : l'indicateur de nouvelle plaque n'apparaît plus que sur l'<strong>Dog Tag Shelf</strong>, plus sur l'écran principal de la Trophy Room ni à l'entrée du lobby. Moins de notification inutile.</li>
          </ul>
          <div class="callout callout-success">
            <h4>Pourquoi c'est plus qu'un détail cosmétique</h4>
            <p>Ces animations ont un vrai impact de <strong>fluidité</strong> : inspecter une plaque après un kill est un micro-rituel qui prolonge le moment de la mort et affiche le score de l'adversaire. C'est exactement le type de feedback post-combat que les joueurs réclamaient depuis des années.</p>
          </div>

          <h2 id="gachapon">5. Le Dog Tag Gachapon</h2>
          <p>Dans le mode <strong>Supplies Drops</strong>, les plaques sont une <strong>monnaie secondaire</strong> : elles s'échangent contre des récompenses via un système de <strong>gachapon</strong> (tirage à lots).</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Rang de récompense</th><th>Type</th><th>Pour qui</th></tr></thead>
              <tbody>
                <tr><td><strong>S</strong></td><td>Récompense vedette (cosmétique rare)</td><td>Collectionneurs disposant de beaucoup de plaques</td></tr>
                <tr><td><strong>A</strong></td><td>Équipement, cosmetics d'arme, accessoires</td><td>Joueurs qui veulent du matériel ou du cosmétique d'arme</td></tr>
                <tr><td><strong>B</strong></td><td>Charms, objets utilitaires</td><td>Complétionnistes de sets</td></tr>
                <tr><td><strong>C</strong></td><td>Consommables courants</td><td>Débutants qui ont besoin de supplies</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Ce que le jeu ne publie pas</h4>
            <p>Les <strong>taux de tirage</strong>, le <strong>compteur de pity</strong>, la <strong>garantie de rareté</strong>, le <strong>shop d'échange</strong> et le <strong>taux de conversion des doublons</strong> ne sont pas publiés : vérifiez le panneau en jeu. En revanche, le principe « les doublons de rang inférieur se convertissent en monnaie d'échange » est confirmé par la documentation du mode Biohazard Draw.</p>
          </div>

          <h2 id="supplies">6. Supplies Drops 2.0 — le mode qui produit les plaques</h2>
          <ul>
            <li>Le mode se joue sur <strong>Airport</strong>, avec des <strong>loadouts prédéfinis</strong> et des <strong>respawns illimités</strong> : l'objectif est la coordination d'équipe pour déposer des ressources dans les <strong>coffres de squad</strong> et <strong>perso</strong>.</li>
            <li>La version <strong>2.0</strong> de la saison : les coffres s'<strong>agrandissent</strong> à mesure que l'équipe progresse, les <strong>terminaux</strong> normaux et <strong>clandestins</strong> apparaissent, et le nombre de conteneurs et de loot augmente.</li>
            <li><strong>5 niveaux de crate</strong> : on gagne de l'<strong>XP de caisse</strong> en fouillant des conteneurs, en éliminant des joueurs et en interagissant avec les terminaux.</li>
            <li>Les plaques se récupèrent sur les <strong>objectifs porte-plaques</strong> — ce sont des <strong>objectifs d'événement</strong>, pas du loot aléatoire. Il faut aller les chercher exprès.</li>
          </ul>

          <h2 id="strategie">7. Stratégie : ramasser ou vendre ?</h2>
          <div class="grid grid--2">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Vendez si…</h3>
              <p class="card-text">— vous êtes en <strong>Forbidden</strong> ou au Warlord (70 000 K la plaque) ;</p>
              <p class="card-text">— vous n'avez pas besoin de l'<strong>étagère</strong> et vous n'êtes pas collectionneur ;</p>
              <p class="card-text">— vous visez le <strong>gachapon</strong> et vous avez besoin du stock.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Gardez si…</h3>
              <p class="card-text">— vous voulez <strong>remplir l'étagère</strong> et les 3 boîtes à 500 plaques ;</p>
              <p class="card-text">— vous chasez le <strong>titre de collectionneur</strong> ;</p>
              <p class="card-text">— vous <strong>masquez votre nom</strong> et votre arme aux autres joueurs (usage très répandu dans la communauté).</p>
            </div></div>
          </div>
          <div class="callout callout-danger">
            <h4>Le conseil de la communauté</h4>
            <p>« Je les collecte par habitude, et une fois dans le lobby je me demande : à quoi ça sert ? » — la réponse la plus courante : <strong>pour l'auto-protection</strong>. Masquer son identité à celui que vous tuez est un avantage psychologique réel, et l'étagère est le seul endroit où l'objet a un usage durable. Sinon, une plaque en Forbidden vaut 70 000 Koen : c'est du loot.</p>
          </div>

          <h2 id="checklist">8. Check-list dog tags</h2>
          <ul>
            <li>Ramassez les plaques <strong>des hards</strong> (niveau 30, rangs ace/hero/legend) : ce sont des joueurs et ils valent plus.</li>
            <li>Surveillez votre <strong>étagère</strong> : c'est le seul endroit où elles ont un usage cosmétique durable.</li>
            <li>En Supplies Drops, suivez les <strong>objectifs porte-plaques</strong> au lieu de courir après les coffres.</li>
            <li>Vendez au contact avant le reset de saison si vous n'êtes pas collectionneur.</li>
          </ul>
          <p>Pour la valeur des autres objets, voir <a href="items-valeur.html">le guide de la valeur</a>. Pour l'étagère et la Trophy Room, voir <a href="items-collection-room.html">le guide Collection Room</a>.</p>
"""

page('cosmetiques-dog-tags.html',
     "Cosmétiques — Dog Tags",
     "Guide des plaques d'identité ABI : valeur 500 à 70 000 Koen, extraction Hel, Dog Tag Shelf, animations d'inspection S7 et Dog Tag Gachapon du mode Supplies Drops 2.0.",
     "../img/items/collection-room.jpg",
     "Cosmétiques — Dog Tags", "Dog Tags",
     "500 Koen en standard, 70 000 en Forbidden : la plaque d'identité, plus petite objet de loot, plus gros ratio de valeur.",
     tags,
     [("quest-ce", "1. Qu'est-ce que c'est"), ("valeur", "2. Valeur"), ("utilises", "3. Usages"),
      ("s7", "4. Nouveautés S7"), ("gachapon", "5. Dog Tag Gachapon"), ("supplies", "6. Supplies Drops 2.0"),
      ("strategie", "7. Vendre ou garder"), ("checklist", "8. Check-list")],
     extra_js=False, nav=NAV, crumb=('Cosmétiques', 'cosmetiques-skins-perso.html'))

print("OK S10")
