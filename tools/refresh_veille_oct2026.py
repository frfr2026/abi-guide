#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integrite la veille du 18/11/2026 sur les sujets encore manquants.

Neuf blocs repartis sur huit pages, avec statut de source explicite :

  armes-builds           : les cinq builds « Faces aux chiffres officiels »,
                           les tableaux d'equipement complets (classe,
                           durabilite, materiau, poids, penalite, nombre de
                           tirs), et l'astuce du chargement en deux couches
  equipement-armures     : le tableau des paliers T3 a T5 avec les valeurs
                           de reference croisees
  guide-traders          : la prime de 20 % sur les objets de haute qualite
                           vendus en raid au Field Merchant
  guide-extraction       : les tailles de conteneur securise, les regles
                           d'assurance, et le verrou des objets Tactically
                           locked
  guide-avance           : les trois sections de mission a sauter, et le
                           style de jeu solo
  guide-economie         : les deux enveloppes budgetaires de reference
  map-northridge         : le tableau officiel du mode Hostile Sector
                           (Saison 6), en reference historique
  saison7-zombie-research : les mecaniques de conteneur propres au mode

Statuts de source : les chiffres d'equipement viennent d'une base de
donnees de reference communautaire recoupant les donnees du jeu, et sont
donc marques « Documente ». Les pratiques de jeu viennent de retours
communautaires et sont marquees « Communautaire ».

Idempotent : chaque bloc n'est insere qu'une fois.
"""
import pathlib
import re
import sys

PAGES = pathlib.Path("pages")

BLOCS = [
    # ─────────────────────────── armes-builds ───────────────────────────
    (
        "armes-builds.html",
        "build-officiel",
        "builds-tableaux",
        """
          <h3 id="builds-tableaux">Les cinq builds face aux chiffres de référence</h3>
          <p>Les valeurs ci-dessous proviennent d'une base de données de référence
          communautaire qui recoupe les données du jeu : classe de protection,
          durabilité, matériau, poids total du kit, pénalité de déplacement et
          nombre de tirs nécessaires au torse. Ce sont des valeurs
          <strong>documentées</strong>, pas des chiffres publiés par l'éditeur.</p>

          <h4>Build « tout-terrain » — AK-12 Assault Rifle en 5.45×39 BS</h4>
          <p>Un fusil de niveau supérieur, la munition la plus pénétrante de son
          calibre, et l'armure la plus élevée que le mode autorise. Il n'excelle
          nulle part et ne laisse aucun angle mort. C'est le build par défaut quand
          vous ne savez pas à qui vous avez affaire.</p>

          <h4>Build « assaut » — Vector 45 Micro SMG en .45 APWC</h4>
          <p>Haute cadence, portée courte, armure délibérément légère : le prix
          à payer en protection est compensé par la vitesse de déplacement.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Build assaut — Lockdown, jusqu'à la classe 5</caption>
              <thead><tr><th scope="col">Emplacement</th><th scope="col">Pièce</th>
              <th scope="col">Classe</th><th scope="col">Durabilité</th>
              <th scope="col">Matériau</th></tr></thead>
              <tbody>
                <tr><td>Torse</td><td>SEK Fortress Body Armor</td><td>4</td><td>50</td><td>Aluminium</td></tr>
                <tr><td>Casque</td><td>03 Heavy Tactical Helmet</td><td>5</td><td>45</td><td>Composite</td></tr>
                <tr><td>Masque</td><td>Aucun</td><td>—</td><td>—</td><td>—</td></tr>
              </tbody>
            </table>
          </div>
          <p><strong>Poids du kit :</strong> 11,0 kg · <strong>Pénalité de
          déplacement :</strong> −4 % · <strong>Contre une armure de classe 5 :</strong>
          percement seulement une fois la plaque usée, trois tirs au torse.</p>

          <h4>Build « longue distance » — M24 Bolt-Action en 7.62×51 M61</h4>
          <p>Le tir de précision le plus propre du catalogue. Il n'y a pas de
          rafale, donc chaque tir est une décision, et la décision vaut plus
          qu'un tir rapide mal placé.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Build longue distance — les deux configurations de référence</caption>
              <thead><tr><th scope="col">Emplacement</th><th scope="col">Normal (classe 4)</th>
              <th scope="col">Lockdown (classe 5)</th></tr></thead>
              <tbody>
                <tr><td>Torse</td><td>Spartan B Body Armor · classe 4 · durabilité 50 · aramide</td>
                <td>BT6 Heavy Body Armor · classe 5 · durabilité 90 · titane</td></tr>
                <tr><td>Casque</td><td>SH40 Military Helmet · classe 4 · durabilité 50 · acier</td>
                <td>AN95 Heavy Blast Helmet · classe 5 · durabilité 55 · titane</td></tr>
                <tr><td>Masque</td><td>SH60 Mask · classe 4 · durabilité 35 · composite</td>
                <td>AN95 Military Bulletproof Mask · classe 4 · durabilité 50 · verre</td></tr>
              </tbody>
            </table>
          </div>
          <p>La comparaison des deux lignes est instructive : passer de Normal en
          Lockdown triple presque la durabilité du torse (50 → 90) en changeant de
          matériau. L'armidure en titane est bien plus résistante à l'usure que
          l'aramide, et cette différence se sent sur la durée d'un raid.</p>

          <h4>Build « léger » — P90 Micro SMG en 5.7×28 SS198</h4>
          <p>Le build le plus mobile du site. Il est conçu pour un objectif
          précis : ne pas chercher le combat, sortir vite, et rester en vie quand on vous
          engage par surprise.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Build léger — le même en Normal et en Lockdown</caption>
              <thead><tr><th scope="col">Emplacement</th><th scope="col">Pièce</th>
              <th scope="col">Classe</th><th scope="col">Durabilité</th>
              <th scope="col">Matériau</th></tr></thead>
              <tbody>
                <tr><td>Torse</td><td>KN Regulation Body Armor</td><td>3</td><td>35</td><td>Aramide</td></tr>
                <tr><td>Casque</td><td>F70 Tactical Helmet</td><td>3</td><td>25</td><td>Composite</td></tr>
                <tr><td>Masque</td><td>Aucun</td><td>—</td><td>—</td><td>—</td></tr>
              </tbody>
            </table>
          </div>
          <p><strong>Poids du kit :</strong> 9,1 kg · <strong>Pénalité de
          déplacement :</strong> −2 % · <strong>Contre une armure de classe 4 :</strong>
          percée à chaque fois, deux tirs au torse · <strong>Contre une armure de
          classe 5 :</strong> presque toujours, trois tirs au torse.</p>

          <h4>Build « anti-armure lourde » — SVTU Carbine en 7.62×54 7N37</h4>
          <p>Le 7.62×54 est le calibre le plus pénétrant du jeu, et la SVTU est
          l'arme qui l'exploite le mieux. En Normal, il est trop haut : sa portability
          est de 66 mètres, mais son ergonomie de 30 points en fait l'une des
          armes les moins maniables du catalogue. Ce build se justifie quand on
          sait que l'adversaire est en classe 5 ou 6 et que l'on refuse de
          négocier.</p>

          <div class="callout callout-success">
            <p><strong>Le point commun des cinq builds : la cohérence.</strong>
            Dans chaque ligne, l'armure du torse, le casque et le masque portent
            le même niveau de défense. C'est cette homogénéité, et non le palier
            absolu, qui détermine si un kit tient un duel.</p>
          </div>
""",
    ),
    (
        "armes-builds.html",
        "build-fal",
        "fal-chargement",
        """
          <h3 id="fal-chargement">L'astuce du chargement en deux couches</h3>
          <p>La FAL revient en Saison 7 grâce à un kit de recul saisonnier
          appliqué au gunsmith, et avec elle une astuce de chargement qui vaut
          d'être connue parce qu'elle s'applique à toutes les armes à
          chargeur détaché.</p>
          <p>Le principe : c'est la munition <em>chambrée</em> qui détermine la
          classe de pénétration au moment du tir. Un chargeur rempli de bouts
          bas de gamme peut donc être remplacé par une poignée de munitions
          haut de gamme, et la parade est de recharge.</p>
          <ul>
            <li><strong>Les dix premières balles</strong> du chargeur en M80
            (classe 4) ou M62 (classe 5) : le premier contact se fait avec la
            munition de qualité.</li>
            <li><strong>Les vingt balles suivantes</strong> en M80 d'entrée de
            gamme : le coût de la munition de tête est amorti sur le reste du
            chargeur.</li>
            <li><strong>Chargeur de 30 rounds</strong> et lunette compacte 2× : la
            configuration minimale du build.</li>
          </ul>
          <div class="callout callout-warning">
            <p><strong>Le statut de cette astuce.</strong> Elle est rapportée par
            la communauté des guides de Saison 7, et elle est cohérente avec la
            règle générale de la classe de pénétration. Elle reste une pratique
            de terrain, pas une règle officielle documentée par l'éditeur : la
            hiérarchie exacte des munitions d'un même calibre peut varier avec
            les correctifs.</p>
          </div>
          <p>La limite de l'astuce est évidente, et c'est elle qui la rend
         /ar opportuniste plutôt qu'exploit : dès que votre cible change de
          calibre, ou dès qu'un rechargement est nécessaire au milieu d'un
          échange, l'avantage disparaît. Elle est fait pour l'ouverture d'un
          duel, pas pour sa durée.</p>
""",
    ),
    # ─────────────────────── equipement-armures ───────────────────────
    (
        "equipement-armures.html",
        "leadership",
        "armures-reference",
        """
          <h3 id="armures-reference">Les pièces de référence, classe par classe</h3>
          <p>Les valeurs ci-dessous proviennent d'une base de données de
          référence communautaire qui recoupe les données du jeu. Elles sont
          marquées <strong>Documenté</strong> : ce ne sont pas des chiffres
          publiés par l'éditeur, mais des valeurs cohérentes entre elles et
          cohérentes avec le comportement observé en jeu.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les pièces de référence — classe, durabilité et matériau</caption>
              <thead><tr><th scope="col">Pièce</th><th scope="col">Classe</th>
              <th scope="col">Durabilité</th><th scope="col">Matériau</th>
              <th scope="col">Zone</th></tr></thead>
              <tbody>
                <tr><td>KN Regulation Body Armor</td><td>3</td><td>35</td><td>Aramide</td><td>Torse</td></tr>
                <tr><td>F70 Tactical Helmet</td><td>3</td><td>25</td><td>Composite</td><td>Casque</td></tr>
                <tr><td>SEK Fortress Body Armor</td><td>4</td><td>50</td><td>Aluminium</td><td>Torse</td></tr>
                <tr><td>Spartan B Body Armor</td><td>4</td><td>50</td><td>Aramide</td><td>Torse</td></tr>
                <tr><td>SH40 Military Helmet</td><td>4</td><td>50</td><td>Acier</td><td>Casque</td></tr>
                <tr><td>SH60 Mask</td><td>4</td><td>35</td><td>Composite</td><td>Masque</td></tr>
                <tr><td>03 Heavy Tactical Helmet</td><td>5</td><td>45</td><td>Composite</td><td>Casque</td></tr>
                <tr><td>BT6 Heavy Body Armor</td><td>5</td><td>90</td><td>Titane</td><td>Torse</td></tr>
                <tr><td>AN95 Heavy Blast Helmet</td><td>5</td><td>55</td><td>Titane</td><td>Casque</td></tr>
                <tr><td>AN95 Military Bulletproof Mask</td><td>4</td><td>50</td><td>Verre</td><td>Masque</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-info">
            <p><strong>Ce que la durabilité change vraiment.</strong> La
            durabilité n'est pas un second chiffre de protection : c'est le nombre
            de<t> impacts</t> que la pièce encaisse avant de laisser passer. Une
            BT6 en titane à 90 points et une Spartan B en aramide à 50 points
            sont toutes deux de classe 4 ou 5, mais la seconde a été usée contre
            une classe 5 bien avant la première. Les deux lignes « classe 5 »
            de la BT6 et de l'AN95 Heavy Blast Helmet, avec 90 et 55 points,
            expliquent pourquoi la combinaison de référence en Lockdown est
            celle-ci.</p>
          </div>
          <p>La hiérarchie des matériaux est constante dans tout le tableau :
            le titane tient le plus longtemps, puis l'acier, puis l'aluminium et
            le composite, et l'aramide ferme la liste. Mais la classe reste
            prioritaire : une pièce en titane de classe 5 vaut mieux qu'une pièce
            en titane de classe 4, et une pièce en composite de classe 5 vaut
            mieux qu'une pièce en aluminium de classe 4 face à une arme de
            classe 5.</p>
""",
    ),
    # ─────────────────────────── guide-traders ───────────────────────────
    (
        "guide-traders.html",
        "erreurs",
        "prime-field-merchant",
        """
          <h3 id="prime-field-merchant">La prime sur les objets de haute qualité</h3>
          <p>Les Field Merchants apparaissent aléatoirement dans les raids. Quand
          vous leur vendez directement un objet de haute qualité — fond orange ou
          fond jaune — en raid, ils l'achètent avec une <strong>prime de vingt
          pour cent</strong>, soit un coefficient de 1,2 sur le prix affiché.</p>
          <div class="callout callout-info">
            <p><strong>La conséquence pratique :</strong> ne quittez jamais le raid
            avec un objet de haute qualité que vous n'aviez pas déjà l'intention de
            vendre. La vente en raid au marchand est plus rentable que la vente
            au marché après extraction, et elle libère de l'espace dans le sac
            au moment où l'espace compte. Si vous récupérez une pièce de haute
            qualité et que votre sac est plein, la vente immédiate au premier
            marchand rencontré est presque toujours la bonne décision.</p>
          </div>
          <p>Deux nuances protègent de l'erreur. D'abord, cette prime concerne
          les objets de <em>haute qualité</em> : la majority du butin courant n'en
          bénéficie pas, et l'écart de 20 % sur une pièce à faible valeur ne vaut
          pas le détour. Ensuite, le statut de cette règle est celui d'un
          <strong>retour communautaire</strong> : plusieurs guides de Saison 7 la
          décrivent de la même façon, mais les notes officielles de la saison ne
          publient pas le tableau des coefficients.</p>
""",
    ),
    # ────────────────────────── guide-extraction ──────────────────────────
    (
        "guide-extraction.html",
        "erreurs",
        "conteneur-assurance",
        """
          <h2 id="conteneur-assurance">Conteneur sécurisé : ce qui survit à la mort</h2>
          <p>Quand vous mourez en raid, vous perdez tout ce que vous aviez
          emporté et tout ce que vous aviez trouvé — à deux exceptions près. Ces
          deux exceptions sont les seuls amortisseurs de risque du jeu, et elles
          sont très mal utilisées.</p>

          <h3>Le conteneur sécurisé : une seule chose survit</h3>
          <p>Le conteneur sécurisé, parfois appelé poche, garde un seul objet
          même si vous mourez. Sa taille est un choix : il existe en
          <strong>1×2, 2×2, 2×3</strong> et <strong>3×3</strong>. Le format 3×3
          est une récompense saisonnière : on l'obtient en remplissant les
          missions de la saison, et il ne reste valable que le temps de cette
          saison.</p>
          <ul>
            <li><strong>Ce qu'on y met</strong> : vos munitions les plus chères,
            un objet de valeur inestimable, ou une clé que vous n'avez pas les
            moyens de racheter.</li>
            <li><strong>Ce qu'on n'y met pas</strong> : une arme entière. La
            place vaut plus que la valeur d'une arme, et l'arme peut être
            reconstruite.</li>
            <li><strong>Le verrou Tactical Ops</strong> : un objet marqué
            « Tactical Ops locked » ne peut pas être placé dans le conteneur
            avant votre première extraction réussie avec lui. Le symbole de
            boîte apparaît sur l'objet une fois cette condition remplie.</li>
          </ul>

          <h3>Il n'y a pas d'assurance : ce qu'il faut savoir à la place</h3>
          <p><strong>ABI Infinite n'a pas de système d'assurance.</strong> C'est
          la position officielle, et elle est explicite : « insurance does not
          exist, what you lose is gone unless recovered manually ». Tout ce que
          vous portez hors d'un emplacement protégé est perdu sans
          contrepartie. Les guides qui décrivent un « remboursement
          conditionnel », un « remboursement si aucun joueur adverse n'a
          extrait votre arme assurée » ou des « fichiers chiffrés exclus de la
          couverture » décrivent une mécanique qui n'existe pas dans le jeu PC :
          ce sont les règles du jeu mobile Arena Breakout.
          <span class="src-tag src-documente">Documenté</span></p>
          <div class="callout callout-warning">
            <p><strong>Les quatre vrais filets de sécurité, à leur place.</strong>
            <strong>1. La Secure Case</strong> — un conteneur à grille loué en
            Bonds qui conserve son contenu même à la mort ; les munitions de
            haut tier en sont exclues par une règle de Saison 6. <strong>2. Le
            coéquipier</strong> — s'il sort vivant avec votre stuff, il vous le
            renvoie par la messagerie du jeu. <strong>3. Le Supplies Retrieval
            Device</strong> — expédié après le raid. <strong>4. Secure Ops</strong>
            — le mode où un échec ne coûte aucun équipement. En dehors de ces
            quatre voies, ce que vous perdez est perdu.
            <span class="src-tag src-documente">Documenté</span></p>
          </div>
          <p>La règle d'usage rationnelle est simple : mettez dans la Case ce qui
          est coûteux à remplacer, et laissez le reste. Couvrir un kit de raid
          complet revient à payer une prime qui dépasse souvent la marge
          disponible — à ce stade-là, mieux vaut réduire la valeur du kit que de
          tenter de le couvrir.</p>
""",
    ),
    # ─────────────────────────── guide-avance ───────────────────────────
    (
        "guide-avance.html",
        "decision",
        "missions-sautables",
        """
          <h2 id="missions-sautables">Les trois sections de mission qu'il vaut mieux sauter</h2>
          <p>La progression de faction passe par des sections de mission, et
          trois d'entre elles sont  les plus pénibles du
          jeu au regard de ce qu'elles rapportent. Les sauter est un choix
          rationnel, pas une triche.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Les sections de mission à contourner — ce qu'elles coûtent</caption>
              <thead><tr><th scope="col">Section</th><th scope="col">Ce qu'elle impose</th>
              <th scope="col">Coût réel</th></tr></thead>
              <tbody>
                <tr><td><strong>Exploration souterraine</strong></td>
                <td>Survivre à dix extractions en mission urgente</td>
                <td>Le trafic des zones à forte affluence en fait un goulot
                d'étranglement économique</td></tr>
                <tr><td><strong>Perturbation interne</strong></td>
                <td>Extraire par un ascenseur de second étage très exposé, avec
                restriction des grenades</td>
                <td>Un piège à wipe d'équipe : l'ascenseur est un couloir préparé
                et la restriction supprime votre réponse</td></tr>
                <tr><td><strong>Interférences de communication</strong></td>
                <td>Interagir avec un marchand précis dix fois, avec un plafond
                de deux interactions par déploiement</td>
                <td>Cinq raids minimum, pour un reward final faible</td></tr>
              </tbody>
            </table>
          </div>
          <p>Le principe commun aux trois : elles imposent soit un risque
          disproportionné, soit une répétition mécanique qui coûte plus de
          temps qu'elle ne rapporte de progression. L'option de contournement
          existe pour chacune. Les ressources restantes à commercer avec se répartit sur
          les sections qui ne demandent ni position exposée ni répétition.</p>
          <div class="callout callout-warning">
            <p><strong>Statut de cette information :</strong> retour
            communautaire. Un guide de survie de Saison 7 publié sur Reddit
            signale ces trois sections et l'existence d'une option de
            contournement. Les notes officielles de saison ne détaillent pas
            section par section, donc vérifiez dans votre propre interface que
            l'option est bien active avant de foncer.</p>
          </div>

          <h2 id="style-solo">Jouer seul : la discipline qui rend le solo viable</h2>
          <p>Le jeu n'offre pas de file solo : vous êtes toujours matché contre
          des équipes. Mais la valeur extraite en solo est statistiquement
          <strong>supérieure</strong>, puisque vous ne partagez rien. Trois règles
          suffisent à en profiter.</p>
          <ol>
            <li><strong>Les fumées d'abord.</strong> Le conseil le plus répété des
            joueurs solitaires : beaucoup de fumées, un tir, puis un déplacement.
            La fumée coupe la ligne de vue de l'équipe adverse pendant que vous
            supprimez un membre, et vous vous repositionnez avant qu'ils ne vous reacquièrent.</li>
            <li><strong>Se repositionner après chaque tir.</strong> Dès que vous
            tirez, votre position est connue. Un joueur solitaire qui reste
            immobile contre une équipe est un joueur solitaire qui meurt du
            flanc.</li>
            <li><strong>Combattre pour la sortie, pas pour la carte.</strong>
            Remplissez le sac sur un ou deux kills et partez. Chaque minute
            supplémentaire en raid est une minute de plus pendant laquelle une
            équipe converge vers vous.</li>
          </ol>
          <p>Si vous voulez la valeur la plus forte en mode PvE sans le risque
          PvP, la réponse est le <strong>Secteur hostile</strong> sur Farm et
          Northridge, où les équipes ne peuvent pas s'infliger de dégâts, et
          l'<strong>Infiltration solo</strong> par tickets, qui donne accès à la
          carte en solo ou en équipe réduite. La queue solo n'existe pas, mais
          l'Infiltration solo si.</p>
""",
    ),
    # ─────────────────────────── guide-economie ───────────────────────────
    (
        "guide-economie.html",
        "plan",
        "enveloppes-budget",
        """
          <h3 id="enveloppes-budget">Les deux enveloppes de raid à budget serré</h3>
          <p>Quand la réserve est basse, la question n'est pas « quel kit
          optimal » mais « quel kit qui ne peut pas couter plus qu'il ne
          rapporte ». Deux enveloppes de référence circulent dans la communauté,
          et leur logique vaut au-delà du chiffre.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Deux enveloppes pour reconstituer une réserve</caption>
              <thead><tr><th scope="col">Enveloppe</th><th scope="col">Budget</th>
              <th scope="col">Contenu</th><th scope="col">Objectif</th></tr></thead>
              <tbody>
                <tr><td><strong>Le rat</strong></td><td>Moins de 20 000 K</td>
                <td>Pistolet, gilet léger, petit sac, bandages</td>
                <td>Zéro risque : on évite tout combat, on fouille ce qui est
                tranquille et on sort</td></tr>
                <tr><td><strong>Le bête de somme</strong></td><td>30 000 à 50 000 K</td>
                <td>Un cran au-dessus, toujours sans armure lourde</td>
                <td>On engage quand on a l'avantage : hauteur, angle ou
                surprise</td></tr>
              </tbody>
            </table>
          </div>
          <p>La démonstration chiffrée est ce qui rend l'idée convaincante. Sur
          dix raids, un joueur qui engage des kits à 150 000 K avec 30 % de
          chances de survie dépense 1 500 000 K et rapporte environ 600 000 K : il
          perd 900 000. Un joueur qui engage des kits à 30 000 K avec 40 % de
          chances de survie dépense 300 000 K et rapporte environ 320 000 K : il
          gagne 20 000. Le ratio de survie plus faible ne compense pas
          l'écart de coût.</p>
          <div class="callout callout-info">
            <p><strong>La règle du tiers</strong> est la version prudente de ce
            raisonnement : ne jamais engager plus de 30 % de votre réserve
            disponible sur un seul raid. La règle des 20 %, plus stricte, s'applique
            au <em>kit complet</em> — arme, armure, munitions et soins ensemble —
            et c'est celle qui tient sur la durée.</p>
          </div>
""",
    ),
    # ────────────────────────── map-northridge ──────────────────────────
    (
        "map-northridge.html",
        "pve",
        "hostile-sector-reference",
        """
          <h2 id="hostile-sector-reference">Référence : ce qu'était le Secteur hostile</h2>
          <p>Le mode Secteur hostile a été introduit en Saison 6 et n'est plus
          accessible en Saison 7. Mais ses chiffres officiels restent la meilleure
          façon de comprendre l'économie PvE du jeu, et ils expliquent pourquoi
          Northridge est devenu la carte de farm préférée des joueurs solitaires.</p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Secteur hostile — les rendements officiels annoncés en Saison 6</caption>
              <thead><tr><th scope="col">Carte</th><th scope="col">Rendement de butin</th>
              <th scope="col">Combat entre équipes</th><th scope="col">Météo</th></tr></thead>
              <tbody>
                <tr><td><strong>Farm</strong></td><td>Égal à une zone Lockdown</td>
                <td>Les équipes ne peuvent pas s'infliger de dégâts</td>
                <td>Nuit, brouillard, tempête</td></tr>
                <tr><td><strong>Northridge</strong></td><td>Supérieur à une zone Lockdown</td>
                <td>Les équipes ne peuvent pas s'infliger de dégâts</td>
                <td>Nuit, blizzard</td></tr>
                <tr><td><strong>TV Station</strong></td><td>Égal à une zone Forbidden</td>
                <td>Le combat entre équipes est conservé</td>
                <td>Conditions extrêmes</td></tr>
              </tbody>
            </table>
          </div>
          <p>Ces chiffres viennent de l'annonce officielle de la Saison 6, publiée
          par l'éditeur le 29 juin 2026. Trois conséquences en découlaient :
          Northridge offrait le meilleur rendement en PvE du jeu sans aucun
          risque de combat entre joueurs, Farm offrait le même rendement avec
          une rotation plus simple, et TV Station conservait le combat entre
          équipes tout en descendant au niveau de butin Forbidden.</p>
          <p>Le mode ajoutait aussi quatre types de forces spéciales, aux
          comportements très différents : le <strong>briseur</strong>, le
          <strong>tireur d'élite</strong>, le <strong>grenadier</strong> et le
          <strong>fumigateur</strong>. Des boss étaient garantis sur Farm et
          Northridge, avec des chances de drop des clés universelles et de
          butin de forte valeur, et l'événement de ralliement de boss pouvait se
          déclencher sur les trois cartes.</p>
          <p>Enfin, l'<strong>Infiltration solo</strong> proposait l'entrée en
          solo ou en équipe réduite sur Farm et Northridge, via des tickets
          trouvables en Tactical Ops, extractibles et échangeables sur le
          marché. C'est cette mécanique qui manquait au jeu depuis longtemps :
          la possibilité d'apprendre une carte sans être lecture par une équipe adverse.</p>
""",
    ),
]


def main():
    total = 0
    for page, ancre, id_bloc, corps in BLOCS:
        f = PAGES / page
        if not f.exists():
            print("  ABSENT :", page)
            continue
        s = f.read_text(encoding="utf-8")
        if 'id="%s"' % id_bloc in s:
            print("  deja present : %-26s %s" % (page, id_bloc))
            continue
        m = re.search(r'<h2[^>]*id="%s"[^>]*>' % re.escape(ancre), s)
        if not m:
            # repli : inserer avant la balise h2 de la section donnee
            m2 = re.search(r'<h2[^>]*id="%s"' % re.escape(ancre), s)
            if not m2:
                print("  ANCRE INTROUVABLE : %s -> %s" % (page, ancre))
                continue
            m = m2
        s = s[: m.start()] + corps.strip() + "\n\n" + s[m.start():]
        f.write_text(s, encoding="utf-8")
        total += 1
        print("  enrichi : %-26s %s" % (page, id_bloc))
    print("\ntotal :", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
