import sys
sys.path.insert(0, '/home/user/axi-nexus/tools') if False else None
sys.path.insert(0, '/home/user/abi-nexus/tools')
from pagekit import page, build_nav

NAV = build_nav('Saison 7')
CRUMB = ('Saison 7', 'saison7-utopia.html')

# ─────────────────────────────────────────────── 6. BATTLE PASS
bp = """
          <figure class="page-figure">
            <img src="../img/events/s7-battle-pass.jpg" alt="Récompenses du Battle Pass Saison 7 Utopia" loading="lazy">
            <figcaption>Battle Pass S7 — paliers, skins exclusifs et Koen : le programme de récompenses de la saison Utopia.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Saison</span><span class="fact-value">Saison 7 — Utopia</span></div>
            <div class="fact"><span class="fact-label">Durée</span><span class="fact-value">16 sept. 2026 → fin de saison</span></div>
            <div class="fact"><span class="fact-label">Récompenses</span><span class="fact-value">Skins d'armes, cosmétiques, Koen, clés, clés de carte</span></div>
            <div class="fact"><span class="fact-label">Devise premium</span><span class="fact-value">Bonds (500 pour l'upgrade instantané)</span></div>
          </div>

          <h2 id="structure">1. Structure du pass</h2>
          <p>Le pass de saison fonctionne sur le modèle free / premium classique d'ABI, enrichi cette année par les <strong>événements limités</strong> : les quatre récompenses de progression des <strong>missions d'activité</strong> du Battle Pass incluent désormais un <strong>bonus issu des événements à durée limitée</strong>. Concrètement, vos événements de saison font monter votre palier de pass plus vite.</p>
          <ul>
            <li><strong>Piste gratuite</strong> : des Koen en quantité — le passage de saison annonce littéralement des <strong>millions de Koen</strong> récupérables en se connectant.</li>
            <li><strong>Piste premium</strong> : encore plus de Koen, plus de skins, plus de cosmétiques, et l'accès aux articles du <strong>Battle Pass Store</strong>.</li>
            <li><strong>Progression d'activité</strong> : les missions d'activité quotidiennes sont le moteur du pass. Elles sont <strong>rafraîchies chaque lundi à 05:00 UTC</strong>.</li>
          </ul>
          <div class="callout callout-warning">
            <h4>Les récompenses d'activité ne se rattrapent pas</h4>
            <p>Les récompenses d'étoile (star rewards) sont <strong>réinitialisées chaque lundi à 05:00 UTC</strong>, et les récompenses non réclamées <strong>ne sont pas rééditées</strong>. La ligne de missions zombies de 40 missions suit la même logique :rattrapez chaque semaine.</p>
          </div>

          <h2 id="skins">2. Les skins exclusifs de la saison</h2>
          <p>Les skins d'armes exclusifs de la saison s'obtiennent via le <strong>Battle Pass Store</strong> et les <strong>vouchers</strong> gagnés en missions ou en événements. Liste annoncée officiellement :</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Skin</th><th>Arme</th><th>Obtention</th></tr></thead>
              <tbody>
                <tr><td><strong>Shooting Star Panorama</strong></td><td>Banshee (SMG)</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Shooting Star Panorama</strong></td><td>SPR310 (fusil à pompe double canon)</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>MPX Micro (SMG)</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>Mk14 (fusil de précision)</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>SKS (carabine)</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Streamlined</strong></td><td>F57 (pistolet)</td><td>Battle Pass Store / vouchers</td></tr>
                <tr><td><strong>Pixel Soldier</strong></td><td>AKM</td><td>Défi de Merit / check-in quotidien</td></tr>
                <tr><td><strong>Pixelated Battlefield</strong></td><td>AK-74N</td><td>Défi de Merit / check-in quotidien</td></tr>
                <tr><td><strong>Black Rock Shooter</strong></td><td>ML Lever-Action</td><td>Missions de saison</td></tr>
              </tbody>
            </table>
          </div>
          <p>Le <strong>« Streamlined »</strong> se décline sur cinq armes de la même famille visuelle — c'est le set le plus rentable en effort. Le <strong>Pixel Soldier / Pixelated Battlefield</strong> est le set « rétro pixel » de la saison, obtenu gratuitement via le check-in et le Défi de Merit.</p>
          <div class="callout callout-success">
            <h4>La progression de tirage est conservée</h4>
            <p>La progression de tirage de la <strong>Saison 6 est intégralement reportée</strong> : si vous étiez à mi-parcours sur un banner de la saison précédente, vous reprenez exactement où vous vous étiez arrêté. Aucun tirage perdu au changement de saison.</p>
          </div>

          <h2 id="recompenses">3. Les autres récompenses</h2>
          <ul>
            <li><strong>Tacti-Girl Charm Voucher ×15</strong>, <strong>S7 Skin Supply Coupon ×15</strong>, <strong>Golden Gift Box ×4</strong>, <strong>Challenger Banner</strong> et le spray <strong>Smoke Rises</strong> — via le Défi de Merit et le check-in quotidien.</li>
            <li><strong>Background de mode Infiltration</strong> exclusif S7 — via les missions de saison.</li>
            <li><strong>Black Rock Shooter</strong> (skin ML Lever-Action), <strong>Basic Elite Trial Card (30 jours)</strong>, <strong>3×3 Titanium Case</strong> — également via les missions de saison.</li>
            <li><strong>Season Mission Skip Cards</strong>, <strong>Coin Raid Vouchers</strong> et <strong>Premium Quick Kits</strong> (nouveauté de la saison) — via des missions spécifiques.</li>
            <li>Skins d'armes pour le <strong>M4A1</strong>, le <strong>Banshee</strong>, le <strong>MPX</strong>, cosmétiques de personnage et designs de flashbang supplémentaires.</li>
            <li><strong>Cartes Élite Premium (7 jours)</strong> et <strong>millions de Koen</strong> à claiming dans <em>Event → More Events → Season 7 Utopia</em>.</li>
          </ul>

          <h2 id="achat">4. Où et comment acheter</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Offre</th><th>Contenu</th><th>Prix</th></tr></thead>
              <tbody>
                <tr><td><strong>Upgrade du Battle Pass</strong></td><td>500 Bonds immédiatement, skins, tenue, Koen</td><td>500 Bonds</td></tr>
                <tr><td><strong>Bundles limités</strong></td><td>450 Bonds + carte Élite 7 jours + skin d'arme exclusif (6 bundles au total)</td><td>4,50 $ par bundle</td></tr>
                <tr><td><strong>Koen</strong></td><td>Koen via les bundles Premium Koen / top-ups</td><td>Jamais de puissance jouable payante</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h4>Ce qui n'est pas en vente</h4>
            <p>Les Bonds achètent des cosmétiques, des passes et de la commodité — <strong>jamais du Koen jouable ni de la puissance de combat</strong>. C'est une règle de conception de la saison et elle est affichée par l'éditeur.</p>
          </div>

          <h2 id="vaut-il">5. Le pass vaut-il le coup ?</h2>
          <p>La réponse dépend d'une seule variable : <strong>quand</strong> vous l'achetez. Un contributeur Reddit a fait le calcul d'un pass de fin de saison et a résumé la logique mieux que tout le monde :</p>
          <ul>
            <li>Beaucoup de récompenses du pass ont été <strong>converties en « season points »</strong>, à dépenser dans le magasin de fournitures de la saison.</li>
            <li>Les articles de ce magasin sont <strong>en moyenne de niveau T4</strong> et marqués « op supplies » : ils ne peuvent être revendus sur le marché <strong>qu'après avoir été extraits</strong> en opération.</li>
            <li>Avec environ <strong>27 000 season points</strong>, vous ne couvrez que <strong>environ trois semaines d'offres hebdomadaires</strong> — soit de l'ordre de 5 000 points par semaine si vous tout prenez.</li>
            <li>À cela s'ajoute le <strong>bundle FAL</strong>, disponible une seule fois par saison — bon, mais pas revolutionnaire (il contient de la munitions T5).</li>
          </ul>
          <div class="callout callout-warning">
            <h4>La règle simple</h4>
            <p><strong>Début de saison : achetez.</strong> Fin de saison : le pass ne se rentabilise plus, sauf si un skin vous intéresse vraiment — dans ce cas, attendez la prochaine saison et économisez vos Bonds. Un pass acheté à 70 % de la saison se joue mais ne se amortit pas.</p>
          </div>

          <h2 id="objectifs">6. Objectifs réalistes</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Profil</th><th>Objectif</th><th>Commentaire</th></tr></thead>
              <tbody>
                <tr><td>Joueur régulier (~1 h/jour)</td><td>Palier 60–70</td><td>Atteignable confortablement en jouant un peu chaque jour</td></tr>
                <tr><td>Joueur intensif</td><td>Palier 80</td><td>Accessible si vous enchaînez les missions d'activité sans interruption</td></tr>
                <tr><td>Passif</td><td>Palier 30–40</td><td>La piste gratuite seule reste rentable en Koen</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="calendrier">7. Calendrier de la saison</h2>
          <ul>
            <li><strong>Semaine 1</strong> : revival des événements de connectivité, bonus de connexion, premiers skins.</li>
            <li><strong>Semaine 2</strong> : lancement du Festival Biohazard & Automne (24 sept.) — boutique, Défi de Vinson, Lunar Soil Sample.</li>
            <li><strong>Semaine 3</strong> : loot Bountiful Autumn Store (28 sept.), Defi d'Automne, Patrouille de zone sombre.</li>
            <li><strong>Semaine 4+</strong> : Warlord Tournament 3 (29 oct. → 7 déc.) et pass de fin de saison.</li>
          </ul>
          <p>Pour le détail des événements, voir <a href="saison7-utopia.html#agenda">l'agenda de la Saison 7</a>. Pour les rewards d'armes, voir <a href="cosmetiques-skins-perso.html">le guide des cosmétiques</a>.</p>

          <div class="callout callout-success">
            <h4>Le meilleur rapport qualité/prix</h4>
            <p>Les <strong>vouchers</strong> obtenus via le Défi de Merit et les missions de saison offrent le même accès aux skins que le pass premium, sans achat de Bonds. Commencez par la piste gratuite et les événements, et réservez vos Bonds pour un skin que vous n'obtiendrez pas autrement.</p>
          </div>
"""

page('saison7-battle-pass.html',
     "Battle Pass S7 — Utopia",
     "Battle Pass Saison 7 Utopia d'ABI : skins exclusifs (Shooting Star Panorama, Streamlined, Pixel Soldier), Koen, vouchers, coût des Bonds et analyse Reddit pour savoir s'il vaut le coup.",
     "../img/events/s7-battle-pass.jpg",
     "Saison 7 — Pass", "Battle Pass S7",
     "Tous les skins de la saison, leur prix réel, et la question que tout le monde pose : faut-il l'acheter maintenant ?",
     bp,
     [("structure", "1. Structure"), ("skins", "2. Skins exclusifs"), ("recompenses", "3. Autres récompenses"),
      ("achat", "4. Où acheter"), ("vaut-il", "5. Vaut-il le coup ?"), ("objectifs", "6. Objectifs"), ("calendrier", "7. Calendrier")],
     extra_js=False, nav=NAV, crumb=CRUMB)

# ─────────────────────────────────────────────── 7. NOUVEAUTÉS
nouv = """
          <figure class="page-figure">
            <img src="../img/events/s7-nouveautes.jpg" alt="Nouvelles armes de la Saison 7 sur une caisse militaire" loading="lazy">
            <figcaption>Saison 7 Utopia — le récapitulatif complet de tout ce qui est arrivé dans le jeu le 16 septembre 2026.</figcaption>
          </figure>

          <div class="facts">
            <div class="fact"><span class="fact-label">Lancement</span><span class="fact-value">16 septembre 2026</span></div>
            <div class="fact"><span class="fact-label">Armes</span><span class="fact-value">A545 · AK-15SC</span></div>
            <div class="fact"><span class="fact-label">Season kits</span><span class="fact-value">4 (PCC-9, M110, FAL, MPX)</span></div>
            <div class="fact"><span class="fact-label">Modes</span><span class="fact-value">Infected Zone · Zombie Endless</span></div>
          </div>

          <h2 id="recap">1. Le récapitulatif</h2>
          <div class="grid grid--3">
            <div class="card"><div class="card-body">
              <h3 class="card-title">Combat</h3>
              <p class="card-text">Portées effectives augmentées, headshots renforcés, TTK global allongé, ricochets supprimés, RNG T5/T6 retiré, flashlight à -7 d'ergonomie.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Zombies</h3>
              <p class="card-text">6 mutants, 2 modes dédiés (Infected Zone PvPvE, Zombie Endless PvE), No Man's Land, Zombie Research, 40 missions, marchand in-raid.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Équipement</h3>
              <p class="card-text">A545 et AK-15SC, 4 season kits inaugurant le concept, plafonds d'équipement par mode, crafter violet illimité.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Économie</h3>
              <p class="card-text">Marchand de terrain (vente, cargaisons mystères, intel), Elysium en drop rouge, Improvement Blueprint et formules de recherche.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Loot</h3>
              <p class="card-text">Conteneurs exclusifs zombies, sacs de zombies, lance-roquettes qui fait tomber de la cargaison, air-drops massifs en fin de raid.</p>
            </div></div>
            <div class="card"><div class="card-body">
              <h3 class="card-title">Événements</h3>
              <p class="card-text">Supplies Drops 2.0 à 5 niveaux de crate, mission d'extermination, Warlord Tournament 3, Festival Biohazard & Automne.</p>
            </div></div>
          </div>

          <h2 id="armes">2. Les deux nouvelles armes</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Arme</th><th>Positionnement</th><th>Caractéristique</th></tr></thead>
              <tbody>
                <tr><td><strong>A545</strong></td><td>Haut de gamme, « au niveau du U191 et du H416 »</td><td>Cadence 700 RPM — maniabilité contre le H416 à 800 RPM</td></tr>
                <tr><td><strong>AK-15SC</strong></td><td>Fusil de dégâts élevés, « idéal pour le close-to-mid »</td><td>Dégâts brute dans la moyenne distance courte</td></tr>
              </tbody>
            </table>
          </div>
          <p>Ce sont les seules armes entièrement nouvelles du patch. Le reste de l'armurerie a été rééquilibré (voir <a href="saison7-balance-changes.html">le détail des patchs</a>) et quatre <strong>season kits</strong> ont été ajoutés.</p>

          <h2 id="kits">3. Les 4 season kits — une première dans ABI</h2>
          <p>La Saison 7 est la <strong>première fois</strong> qu'ABI introduit des <em>attachements saisonniers</em>. Ils ne sont pas cosmétiques : ils modifient fondamentalement l'arme.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Kit</th><th>Arme</th><th>Effet</th></tr></thead>
              <tbody>
                <tr><td><strong>PCC-9 Full-Auto Kit</strong></td><td>PCC-9</td><td>La PCC-9 devient une arme automatique</td></tr>
                <tr><td><strong>M110 Dual-Stage Trigger</strong></td><td>M110</td><td>Déclencheur binaire : <strong>2 projectiles par gâchette</strong>, dégâts massifs</td></tr>
                <tr><td><strong>FAL Recoil Kit</strong></td><td>FAL</td><td>La cadence passe de « moyennement-faible » à « élevée », au prix d'une cadence légèrement réduite</td></tr>
                <tr><td><strong>MPX « Vulcan » Barrel</strong></td><td>MPX Micro</td><td>Ouvre une <strong>branche de munitions à chair</strong> (meta jambes / chair)</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h4>Les season kits rétrécissent le meta au lieu de l'élargir</h4>
            <p>Le risque identifié par la communauté : si un kit saisonnier supprime la principale faiblesse d'une arme déjà forte, le meta se referme au lieu de s'ouvrir. Les prix, la disponibilité et les pénalités d'attachement comptent donc autant que les avantages affichés dans le menu équipement.</p>
          </div>

          <h2 id="objets">4. Les nouveaux objets</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Catégorie</th><th>Objet</th><th>Effet</th></tr></thead>
              <tbody>
                <tr><td>Tactique</td><td><strong>M290</strong> (nouvelle grenade stun)</td><td>Désormais craftable ; les formules de matériaux ont été réajustées</td></tr>
                <tr><td>Zombie</td><td><strong>Grenade phéromone</strong></td><td>Attire les mutants vers un point choisi</td></tr>
                <tr><td>Zombie</td><td><strong>Fumigène de soin</strong></td><td>Restaure progressivement la santé dans la zone</td></tr>
                <tr><td>Zombie</td><td><strong>Lance-roquettes</strong></td><td>Provoque la chute de cargaison</td></tr>
                <tr><td>Zombie</td><td><strong>Contre-mesures zombie</strong></td><td>Tirées au sort au marchand Endless, exclusives à la raid</td></tr>
                <tr><td>Zombie</td><td><strong>Réactifs expérimentaux</strong></td><td>Pathfinder (+PV torse), Messenger (+vitesse), résistance aux blessures critiques — mais + dégâts subis et détection facilitée</td></tr>
                <tr><td>Marchand</td><td><strong>Cargaison mystère</strong></td><td>Prix bas = rendement stable, prix élevé = jackpot ou perte</td></tr>
                <tr><td>Rouge</td><td><strong>Elysium</strong></td><td>Nouveau drop rouge de l'Infected Zone, valeur équivalente à l'Utopia</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="rouge">5. Les nouveaux collectibles rouges</h2>
          <ul>
            <li><strong>Elysium</strong> — drop rouge majeur de l'Infected Zone, garanti par la fin de la série de missions zombies.</li>
            <li><strong>MRID laptop</strong> — nouveau collectible rouge ajouté en S7.</li>
            <li><strong>Northern Stars</strong>, <strong>double-neck lute</strong> et <strong>emerald jade flute</strong> — nouveaux objets de collection rouges.</li>
            <li><strong>Trophy Room</strong> : le niveau de la Collection Room augmente de <strong>+2</strong> et la limite de stockage des drops rouges passe à <strong>999</strong>. Le marquage rouge des nouvelles plaques d'identité est restreint à l'étagère dédiée.</li>
          </ul>

          <h2 id="craft">6. Le nouveau système de recherche et de craft</h2>
          <ul>
            <li><strong>Improvement Blueprint</strong> — nouveau matériau de recherche, obtenu via les missions actives et les raids réguliers ; <strong>plus probable dans les boîtes à documents, les vêtements et les tiroirs</strong>.</li>
            <li>Un blueprint sert à <strong>rechercher une formule</strong> ; le résultat s'<strong>équipe</strong> pour accorder un buff unique.</li>
            <li><strong>Partage de formules</strong> : apprendre et partager des formules avec des amis rapporte des blueprints d'assistance, <strong>prioritaires</strong> dans la file de recherche.</li>
            <li><strong>Reset saisonnier</strong> : les résultats de recherche sont réinitialisés à chaque saison — un buff appris en S7 ne sert qu'en S7.</li>
            <li><strong>Crafter violet</strong> : l'utilisation est illimitée mais il n'accepte que les objets <strong>de qualité violette ou inférieure</strong>. Son accès se débloque par niveau de crate.</li>
          </ul>

          <h2 id="raid">7. Les nouvelles mécaniques de raid</h2>
          <ul>
            <li><strong>Terminaux</strong> : terminal normal (une interaction par squad pour un peu de XP de caisse) et <strong>terminal clandestin</strong> (à tenir/garnir après interaction, contestable par les autres squads, pour un gros lot de XP de caisse d'un coup).</li>
            <li><strong>Horde de mutants</strong> : tirer sur les <strong>voitures de police</strong> déclenche un événement de horde. Certaines actions d'Operator en déclenchent aussi.</li>
            <li><strong>Air-drops massifs</strong> en milieu et fin de raid, et <strong>unités IA en armure lourde</strong> sur les cartes.</li>
            <li><strong>Retours plus rapides</strong> en début de raid, la durée de respawn augmentant au fil de la partie.</li>
            <li><strong>Broadcasts in-raid</strong> des actions et de la voix ; le <strong>volume de la musique</strong> baisse automatiquement en multijoueur pour mieux entendre vos coéquipiers.</li>
            <li>Le <strong>crafter violet</strong> et l'augmentation des <strong>quantités de conteneurs et de rendement</strong> en raid.</li>
          </ul>

          <h2 id="qol">8. Qualité de vie et correctifs</h2>
          <ul>
            <li><strong>Chargement de chargeur</strong> désormais disponible sur les pistolet et les fusils à pompe.</li>
            <li><strong>Inspection interruptible</strong> en s'accroupissant ; <strong>contrôles de fin de soin</strong> améliorés ; <strong>gestes d'arme au corps</strong> redessinés.</li>
            <li><strong>Perspectives 1ʳᵉ et 3ᵉ personne en inclinaison</strong> unifiées.</li>
            <li><strong>Inspections de plaques d'identité animées</strong> selon le nombre de plaques portées, <strong>journal de dégâts détaillés sur les 30 dernières secondes</strong> d'un combat, et <strong>partage des temps forts et accomplissements</strong> d'une raid.</li>
            <li>Correctifs : <strong>sprint</strong> qui se bloquait par intermittence, <strong>audio</strong> qui disparaissait, <strong>longueur d'arme</strong> qui influençait le recul, valeurs de portée erronées sur les canons Vector 45 standard et moyen.</li>
            <li>La <strong>couverture du disque « Spark »</strong> a été redessinée ; le <strong>niveau de la Collection Room</strong> est relevé de 2 et le stockage rouge passe à 999.</li>
          </ul>

          <h2 id="evenements">9. Les événements de la saison</h2>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Événement</th><th>Contenu</th></tr></thead>
              <tbody>
                <tr><td><strong>Supplies Drops 2.0</strong></td><td>5 niveaux de crate de récompense ; on gagne de l'XP de crate en fouillant, en éliminant des joueurs et en utilisant les terminaux</td></tr>
                <tr><td><strong>Mission d'extermination</strong></td><td>Récompense : Hazmat Suit Supply Passes (1 pass = 5 000 Koen à la fin de l'événement)</td></tr>
                <tr><td><strong>Warlord Tournament 3</strong></td><td>29 oct. → 7 déc. 2026 : classement sur la <strong>valeur du loot</strong>, loadouts visibles, multiplicateur de fichier chiffré, intel de plaques d'identité, marque de leader de kill ; entrée à <strong>400 K de gear minimum + 50 K de ticket</strong>, rang dédié de Recruit IV à Warlord</td></tr>
                <tr><td><strong>Biohazard &amp; Automne</strong></td><td>Festival du 24 sept. : check-in, boutique Bountiful Autumn, Défi de Vinson, Lunar Soil Sample (2×2, 780 000 Koen dans les coffres), Patrouille de zone sombre, Trash to Treasure</td></tr>
                <tr><td><strong>Défi de Merit</strong></td><td>Hebdomadaire : meilleur Merit Endless = 3× Koen, jusqu'à 3 000 000 Koen par semaine</td></tr>
                <tr><td><strong>Zombie No Man's Land</strong></td><td>Pass de check-in et paliers à 4 / 8 / 16 tâches quotidiennes ; les passes droppent aussi en raid infecté</td></tr>
              </tbody>
            </table>
          </div>

          <h2 id="roadmap">10. À retenir pour la route</h2>
          <div class="callout callout-success">
            <h4>Le résumé en 5 lignes</h4>
            <p>1) La contamination est le cœur de la saison : deux modes, six mutants, une progression permanente.<br>
            2) Le rééquilibrage est plus important que les zombies : plus de portée, headshots payants, T4/T5/T6 plafonnés par mode, pénétration déterministe.<br>
            3) Deux armes et quatre kits saisonniers arrivent, et le FAL / M110 / MPX / PCC-9 changent de nature.<br>
            4) L'économie se déplace en raid : marchand de terrain, cargaisons mystères, Elysium en drop rouge.<br>
            5) Commencez par No Man's Land, puis Valley en Infected Zone standard, et gardez votre stash rouge pour le Forbidden.</p>
          </div>
          <p>Pour aller plus loin : <a href="saison7-zombie-infected-zone.html">le guide de la Zone infectée</a>, <a href="saison7-zombie-endless.html">le guide Zombie Endless</a>, <a href="saison7-zombie-research.html">l'arbre Zombie Research</a> et <a href="saison7-balance-changes.html">le détail du rééquilibrage</a>.</p>
"""

page('saison7-nouveautes.html',
     "Saison 7 — Toutes les nouveautés",
     "Tout ce que contient la Saison 7 Utopia d'Arena Breakout Infinite : A545, AK-15SC, 4 season kits, Infected Zone, Zombie Endless, Zombie Research, marchand de terrain, Elysium, Supplies Drops 2.0 et Warlord Tournament 3.",
     "../img/events/s7-nouveautes.jpg",
     "Saison 7 — Utopia", "Nouveautés S7",
     "Le récapitulatif complet de la saison Utopia : tout ce qui est neuf, du champ de mutants au nouveau système de recherche.",
     nouv,
     [("recap", "1. Récapitulatif"), ("armes", "2. Nouvelles armes"), ("kits", "3. Season kits"),
      ("objets", "4. Nouveaux objets"), ("rouge", "5. Collectibles rouges"), ("craft", "6. Recherche & craft"),
      ("raid", "7. Mécaniques de raid"), ("qol", "8. Qualité de vie"), ("evenements", "9. Événements"), ("roadmap", "10. À retenir")],
     extra_js=False, nav=NAV, crumb=CRUMB)

print("OK batch C")
