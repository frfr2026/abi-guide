#!/usr/bin/env python3
"""Enrichit les pages armes/equipement les plus courtes avec des sections editoriales."""
import pathlib, re

ROOT = pathlib.Path('.')

# ---------------------------------------------------------------- donnees
PAGES = {
 'pages/armes-fusils-assaut.html': dict(
   cat='Fusils d\'assaut', anchor='role',
   role='fusil d\'assaut',
   intro="""Le fusil d'assaut est l'arme qui gagne les fights que personne ne voulait gagner. Fourchette de portée 30-100 m, c'est la classe la plus polyvalente du jeu : elle tient face à un SMG qui pousse, elle tient face à un DMR qui tient la distance, et elle ne perd jamais toute une partie parce qu'un seul&nbsp;projeté l'a touchée.""",
   munis=[("5.45×39mm BS (T5)","A545, U191, AEK","Pénétration maximale en 5.45, le meilleur compromis cadence/récupération pour l'A545."),
         ("5.56×45mm AP (T5)","H416, M4A1, AK-12","Le standard du jeu en 2026 : il traverse les gilets T5 et fait tomber les T6 à la tête."),
         ("7.62×39mm BP (T4)","AK-12, AKS-74N","Rendement au Koen imbattable, un excellent compromis pour les runs de farm."),
         ("5.8×42mm BP (T5)","PKM, VAL","Munition de précision, indispensable au sniper en Mode Étendu."),
         ("7.62×51mm M80 (T5)","FAL, G28","La plus punchy du jeu, mais très lourde et très coûteuse.")],
   errs=["<strong>Changer de canon pour « plus de dégâts »</strong> : le gain de dégâts est marginal, la perte de contrôle est immédiate. Le canon long est un choix de portée, pas de puissance.",
         "<strong>Partir en munitions T5 sans budget</strong> : la différence de coût entre une T3 correcte et une T5 se récupère sur deux ou trois raids ratés.",
         "<strong>Oublier le suppresseur sur les armes à haut recul</strong> : il ne réduit pas les dégâts, il réduit la dispersion — c'est exactement ce qui manque en CQB serré.",
         "<strong>Reculer au lieu d'avancer</strong> : le recul vertical d'un fusil d'assaut se corrige en tirant dans la cible, pas en reculant."],
   faq=[("Quel fusil d'assaut choisir en S7&nbsp;?","Le <strong>A545</strong> pour sa cadence et son recul presque vertical, le <strong>H416</strong> pour sa polyvalence, l'<strong>AK-12</strong> pour le budget. Le <strong>AK-15SC</strong> est le nouveau pick 7.62×39 de la saison."),
         ("Fusil d'assaut ou SMG ?","L'arme se choisit par <strong>distance de combat</strong>, pas par Taste. En dessous de 20 m, un SMG gagne. Au-delà de 50 m, seul un fusil d'assaut tient le tir."),
         ("La 5.45 vaut-elle la 5.56&nbsp;?","En S7, oui sur l'A545 et l'U191, grâce à la cadence et à la maîtrise du recul. Mais la 5.56 reste plus universelle et plus facile à« qui perce » les gilets lourds."),
         ("Quel canon choisir&nbsp;?","Court pour l'intérieur et la mobilité, long pour la portée et la précision à la longue distance. Le canon ne change pas la classe de dégâts, il change votre fenêtre de tir.")],
   budget=[("Budget serré","70 000 – 110 000 K","AK-12 ou AKS-74N en T4, armure T3-T4","Farm de	Key et extraction sûre"),
           ("Budget moyen","150 000 – 250 000 K","H416 modéré, gilet T4","Raids Lockdownolan"),
           ("Budget large","300 000 K et plus","A545 ou U191, gilet T5, optique","Farm de rouge etanjou PvP")],
 ),
 'pages/armes-carbine.html': dict(
   cat='Carabines', anchor='role',
   role='carabine',
   intro="""La carabine est le compromis qui a survécu à tous les changements de saison : la maniabilité d'une arme de poing, laMunition d'un fusil, le tout dans un format qui passe sous une porte. C'est l'arme des joueurs qui veulent une seule arme pour toute la partie.""",
   munis=[("5.56×45mm AP (T5)","AK-12, AKS-74U","Le cœur de la classe : précision et pénétration sans exploser le budget."),
         ("7.62×39mm BP (T4)","SKS, AKS-74N","Idéale en farm, moins en duel contre armure T5."),
         ("9×39mm SP-6 (T4)","VSS, Vintorez","La munition subsonique : silencieuse, et trajectoire difficile à suivre."),
         ("5.45×39mm PP (T3)","Banshee, AKS-74U","Rendement maximal pour le train de vie quotidien.")],
   errs=["<strong>Partir en 5.56 sansfonds pour la munition</strong> : une carbine qui claque à chaque tir est une carbine inutilisable.",
         "<strong>Ignorer la différence entre 9×39 et 9×19</strong> : ce ne sont pas les mêmes munitions, et le choix change complètement le TTK.",
         "<strong>Choisir un canon long sur une carabine</strong> : vous perdez la seule avantage de la classe.",
         "<strong>Oublier le grip vertical</strong> : sur une carabine courte, c'est lui qui rend le tir contrôlable."],
   faq=[("Carabine ou fusil d'assaut&nbsp;?","La carabine est plus maniable et plus économe, mais perd en portée et en dégâts bruts. Sur les petites cartes (Farm, TV Station), elle gagne souvent."),
         ("Pourquoi le SKS est si rentable&nbsp;?","Prix d'entrée bas, 7.62×39 très efficace en T4, et un profil de recul qu'on peut apprendre en trois heures."),
         ("Les carabines valent-elles un kit en Lockdown&nbsp;?","Oui, mais avec une armure T5 et une munition T5. En dessous, vous restez en Normal."),
         ("C'est quoi la différence entre 9×19 et 9×39&nbsp;?","La 9×19 est une arme de poing. La 9×39 est une munition de fusil&nbsp;: beaucoup plus puissante, et c'est elle qu'utilise la VSS.")],
   budget=[("Farming","60 000 – 90 000 K","SKS en 7.62×39 BP, sac léger","Extractions Farm et Armory"),
           ("Polyvalence","110 000 – 200 000 K","AK-12 modérée, gilet T4","Un seul kit pour tout le jeu"),
           ("Discret","150 000 – 300 000 K","VSS, 9×39 SP-6, casque léger","Approches discrètes")],
 ),
 'pages/armes-dmr.html': dict(
   cat='DMR', anchor='role',
   role='DMR',
   intro="""Un DMR est un fusil de précision qu'on accepte de tirer en semi-automatique. Le compromis est net : vous perdez la mitraillette, vous gagnez la capacité de tuer à travers une fenêtre, un porche, un toit. C'est l'arme de la ligne de vue longue sur les cartes ouvertes.""",
   munis=[("7.62×51mm M80 (T5)","M110, SVDS","La montée en puissance maximale d'un DMR : un tir Supported suffit à percer un T5."),
         ("7.62×54mm LPS (T4)","Mosin-Nagant, M24","Dégâts enormously élevés, mais la balle LPS perd de la vitesse en fin de course."),
         ("8.8×24mm (T5)","M24 (variante)","Munition de précision, la meilleure contre les armures lourdes si votre build l'autorise."),
         ("5.56×45mm AP (T5)","SVD, G28","Plus légère, plus maniable, moins de dégâts par tir mais un recoil plus facile à tenir.")],
   errs=["<strong>Tirer en rafale avec un DMR</strong> : la courbe de recul est complètement différente, chaque tir compte.",
         "<strong>Oublier le bipied ou le support</strong> : à 200 m, sans appui, le premier tir est un hasard.",
         "<strong>Choisir du 7.62×54 LPS contre un T6</strong> : le LPS perd sa vitesse, il faut toucher la zone de tête ou une partie non protégée.",
         "<strong>Se placer dans un champ de tir dégagé</strong> : un DMR qui n'a pas d'angle de tir n'est qu'une arme.views grosse."],
   faq=[("Quel DMR est le meilleur&nbsp;?","Le <strong>SVDS</strong> et le <strong>M110</strong> dominent la catégorie longue. Le <strong>SVD</strong> est plus maniable, le <strong>M24</strong> est le roi du one-shot."),
         ("DMR ou sniper&nbsp;?","Si votre équipe vous pousse vers l'avant et que vous tirez souvent, prenez un DMR. Si vous tenez une position, prenez un sniper."),
        ("Quel оптиique&nbsp;?","Un 2x pour rester mobile, un 4x pour le mid-range, un 8x pour le one-shot longue distance. Le grossissement coûte cher en temps de visée."),
        ("Le DMR vaut-il son prix&nbsp;?","Il n'a de valeur que si vous savez le placer. Un M110 entre les mains d'un joueur qui ne bouge pas vaut trois fois un A545 entre les mains d'un joueur qui court.")],
   budget=[("Budget serré","80 000 – 140 000 K","Mosin-Nagant, 7.62×54 LPS","Sniper solo, terrain découvert"),
           ("Équipier","150 000 – 280 000 K","SVDS ou M110, 7.62×51 M80","Appui longue distance en escouade"),
           ("Longue distance","250 000 K et plus","M24, optique 8x","Postes de tir longue distance")],
 ),
 'pages/armes-sniper.html': dict(
   cat='Sniper', anchor='role',
   role='sniper',
   intro="""Le sniper n'est pas une arme de combat, c'est une arme de position. Tout se joue avant le tir : l'angle, le support, la ligne de vue. LeocularScope est le composant le plus cher et le plus déterminant du kit, et c'est lui — pas le canon — qui décide si votre tir compte.""",
   munis=[("8.8×24mm (T5)","M24, Mosin-Nagant (haut niveau)","La pénétration maximale : le tir soutenu en pleine tête traverse."),
         ("7.62×54mm LPS (T4)","Mosin, M24","Classique, très létal, mais la vitesse chute sur la distance."),
         ("7.62×51mm M80 (T5)","M110, SVDS","Plus contrôlable que le 7.62×54, avec moins de STOP."),
         (".338 LM (T6)","CheyTac M200","Le haut du panier : dégâts et de pénétration, avec une seule balle sans toucher le")],
   errs=["<strong>Tirer en position debout</strong> : le premier tir est perdu, le second est médiocre. La Opticscompte autant que l'arme.",
         "<strong>Exposer sa position</strong> : le flash ou le son de la détente trahit. Un sniper audible est un sniper mort.",
         "<strong>Oublier le bipied ou le sac de stabilisation</strong> : la dispersion ouverte vous fait rater ce que le canon ne pardonne pas.",
         "<strong>Choisir la 7.62×54 contre une armure T6</strong> : la LPS ne perce plus à distance."],
   faq=[("Quel sniper pour commencer&nbsp;?","Le <strong>M24</strong> est le plus pardonnant : recul gérable, optique lisible, et un one-shot régulier. Le Mosin est plus fort mais plus exigeant."),
         ("Faut-il un support&nbsp;?","Toujours. Un sniper sans support perd sa précision à chaque tir."),
         ("Les snipers sont-ils rentables&nbsp;?","En solo, oui si vous savez jouer les cartes ouvertes. En escouade, vous êtes souvent plus utile en DMR."),
        ("Comment зеркалить un tir&nbsp;?","La compensation de recul d'arme règle laVertical, le support règle l'horizontal. Il faut les deux.")],
   budget=[("Débutant","120 000 – 200 000 K","M24, lunette 4x, bipied","Tirs d'appui sur un toit"),
           ("Confirmé","250 000 – 450 000 K","CheyTac ou M24 haut niveau","One-shot en T5-T6"),
           ("Équipier","300 000 – 600 000 K","8x stabilized, support lourd","Position de verrouillage")],
 ),
 'pages/armes-smg.html': dict(
   cat='SMG', anchor='role',
   role='SMG',
   intro="""Une mitraillette, c'est une arme qui refuse deelk. 900 ou 1 200 tours/minute, elle transforme un duel à 15 m en une question de celui qui a le premier réflexe. Sa force est aussi sa faiblesse : au-delà de 30 m, vous tirez dans le vide.""",
   munis=[("9×19mm Dum-Dum (T2-T3)","MP5, Vector 9mm","La munition anti-armure par les jambes : la moins chère de tout le jeu."),
         (".45 ACP AP (T4)","Vector .45, PCC9","La plus punchy des pistols-calibres, avec un recul que le bloc-magasin tient."),
         ("9×39mm SP-6 (T4)","VSS","Subsonique et précise : la meilleure en approche discrète."),
         ("5.8×42mm BP (T5)","P90","La seule capable de casser une armure T5 en CQB.")],
   errs=["<strong>Sprayer à 60 m</strong> : un SMG à longue distance est un bruit de fond coûteux.",
         "<strong>Charger la 9×19 standard en PvP haut niveau</strong> : la Dum-Dum ou l'AP, c'est la différence entre tuer et presque tuer.",
         "<strong>Ignorer le magasin étendu</strong> : vous coupez 30 % de vos rechargements pour un poids dérisoire.",
         "<strong>Spray sans reculer</strong> : le seul correctif du SMG, c'est le buffer."],
   faq=[("Quel SMG choisir&nbsp;?","Le <strong>P90</strong> pour la cadence et la pénétration, le <strong>Vector .45</strong> pour le STOP, le <strong>MP5</strong> pour l'apprentissage, la <strong>VSS</strong> pour le furtif."),
         ("Le SMG vaut-il contre une armure T5&nbsp;?","Seulement avec la bonne munition : Dum-Dum sur les jambes, ou le P90 en 5.8×42."),
         ("P90 ou MPX&nbsp;?","Le P90 est plus rapide et plus perforant ; le MPX est plus stable et plus facile à maîtriser."),
        ("MPX + Vulcan Barrel&nbsp;?","Le kit S7 transforme le MPX en arme anti-armure de jambes. C'est le build le plus rentable de la classe en farm.")],
   budget=[("Apprentissage","50 000 – 80 000 K","MP5 en 9×19 Dum-Dum","Progresser sans risquer"),
           ("Rentable","80 000 – 150 000 K","Vector .45 ou MPX Vulcan","Farm de Koen et de clés"),
           ("Haut niveau","200 000 – 350 000 K","P90, 5.8×42 BP","CQB contre armure T5")],
 ),
 'pages/armes-shotgun.html': dict(
   cat='Fusils à pompe', anchor='role',
   role='fusil à pompe',
   intro="""Le fusil à pompe n'a pas derapport de dégâts par balle qui vaille le coup : il en a sept. À bout portant, dans un couloir, une cartouche de buckshot décide du sort. C'est l'arme la plus terrifiante et la plus fragile du jeu — celle qui gagne d'un coup et perd d'un seul tir raté.""",
   munis=[("12×70mm buckshot (T2)","M870, Saiga-12","Le gros du damage, mais seulement à moins de 10 m."),
         ("12×70mm slug (T3)","M870, KS23","Une seule balle en plomb : la seule qui traverse une armure."),
         ("8×70mm buckshot (T2)","SKS shotgun","Moins dense, mais meilleure penetration relative."),
         ("12×70mm VS AP (T4)","KS23","Le nouveau projectile S7 : la percée contre l'armure change tout.")],
   errs=["<strong>Tirer à plus de 15 m</strong> : le tir devient un jet de plombs qui rate 90 % du temps.",
         "<strong>Charger du buckshot contre une armure T5&nbsp;?</strong> ça perfore pas. Passez au slug ou au VS AP.",
         "<strong>Recycler l'arme comme un SMG</strong> : chaque rechargement manuel est une seconde de mort.",
         "<strong>Oublier le frein de bouche</strong> : il ne fait pas de bruit, il resserre le faisceau."],
   faq=[("Le fusil à pompe est-il rentable&nbsp;?","En CQB strict, oui, et il est quasi gratuit. En dehors, non."),
         ("Quel calibre choisir&nbsp;?","Le 12×70mm, sans hésiter : le 12×70 VS AP de la S7 a changé la classe face aux armures."),
         ("Un fusil à pompe en escouade&nbsp;?","Oui, en rôle de bouche de porte. Ne comptez pas sur lui pour le mid-range."),
         ("Buckshot ou slug&nbsp;?","Buckshot pour la zone de mort, slug pour percer. En CQB pur, le buckshot gagne ; contre un T5, le slug s'impose.")],
   budget=[("Entrée","40 000 – 70 000 K","M870 en buckshot","Indoor pur"),
           ("Contre armure","90 000 – 180 000 K","KS23 en VS AP","Contre T4-T5"),
           ("Spécialiste","150 000 – 300 000 K","Slug + frein + optique","Traque de niveaux")],
 ),
 'pages/armes-lmg.html': dict(
   cat='Mitrailleuses (LMG)', anchor='role',
   role='mitrailleuse',
   intro="""Une LMG, c'est un furnish HCV : elle ne vise pas une personne, elle couvre une zone. Ce n'est pas une arme qu'on tire depuis l'épaule pendant un raid — c'est une arme qu'on installe sur un point d'appui et qu'on oublie le temps de couvrir le couloir.""",
   munis=[("7.62×51mm M80 (T5)","PKM, MG3","Le standard de la suppression : perforation et portée."),
         ("8.8×24mm (T5)","M249","La pénétration maximale, mais un coût et un poids qui interdisent lonomade."),
         ("5.56×45mm AP (T5)","RPD, MG3 (variante)","Moins de portée, bien moins de poids, exploitable en mobilité."),
         ("7.62×39mm BP (T4)","RPK-16","Le compromis : ce n'est pas une LMG, mais elle en joue le rôle.")],
   errs=["<strong>Porter une LMG en raid solo</strong> : le poids détruit votre mobilité et votre temps de réanimation.",
         "<strong>Tirer en marchant</strong> : la dispersion rend le tir improductif. Elle se pose, ou elle ne sert à rien.",
         "<strong>Oublier la ceinture de munitions</strong> : sans elle, vous avez huit secondes de tir.",
         "<strong>Choisir le 5.56 pour « être mobile »</strong> : à 150 m, ce n'est plus une LMG, c'est un fusil raté."],
   faq=[("Une LMG vaut-elle le coup&nbsp;?","En escouade, sur un point de contention, oui. En solo, non."),
         ("PKM ou M249&nbsp;?","Le PKM pour le 7.62 accessible, le M249 pour la puissance brute et les endurance courtes."),
         ("Quel canon&nbsp;?","Long pour le tir à distance, court pour rester mobile. La LMG ne se porte pas : elle se pose."),
        ("Comment l'utiliser&nbsp;?","Installez-vous, tirez sur le couloir, et comptez sur vos vapeurs — le vrai danger, c'est le flank.")],
   budget=[("Équipier","200 000 – 350 000 K","PKM, 7.62×51 M80","Suppression de groupe"),
           ("Point fixe","300 000 – 500 000 K","M249, 8.8×24","Verrouillage de couloir"),
           ("Tir mobile","120 000 – 220 000 K","RPD ou RPK-16","Appui en déplacement")],
 ),
 'pages/equipement-rigs.html': dict(
   cat='Rigs', anchor='role',
   role='rig',
   intro="""Un rig, c'est un gilet sans protection : uniquement des poches. Il ne vous sauve pas, il vous permet de porter. La question n'est jamais « quel rig est le meilleur », mais « quel rig correspond à ce que je ramasse et à ce que je veux garder en cas de mort ».""",
   errs=["<strong>Choisir un rig par son prix</strong> : un rig cher sans bonne répartition de poches est un rig inutile.",
         "<strong>Ignorer le coût de l'équipement total</strong> : le rig s'ajoute au plafond de 900 000 K du Lockdown.",
         "<strong>Porter un sac lourd en raid Lockdown</strong> : au-delà d'un seuil, le poids transforme un duel en course-pours.",
         "<strong>Mettre les munitions dans les poches du torse</strong> : la troncature de la visée s'en ressent."],
   faq=[("Quel rig pour la S7&nbsp;?","Un rig de type chest-rig modulaire, avec une range séparée et des poches compatibles avec vos munitions."),
          ("Rig ou sac&nbsp;?","Le rig pour l'accès rapide en combat, le sac pour le volume. Les meilleurs raid runs combinent les deux."),
          ("Combien coûte un kit complet&nbsp;?","En Lockdown, la valeur totale de l'équipement est plafonnée à <strong>900 000 Koen</strong>. Un rig mal choisi peut vous faire dépasser et bloquer le raid."),
          ("Le rig vaut-il le coup&nbsp;?","Oui, parce qu'il augmente ce que vous pouvez <em>emporter</em>. Sans lui, vous laissez la valeur au sol.")],
   budget=[("Léger","20 000 – 45 000 K","Rig minimal, 4 poches","Raid court, une arme"),
           ("Standard","45 000 – 90 000 K","Rig modulaire complet","Raid Lockdown classique"),
           ("Chargeur","90 000 – 150 000 K","Rig lourd + rangement munitions","Raid long, squad")],
   munis=[("Poche verticale","Cartouches 5.56 / 7.62","Accès immédiat, dosseret rapide"),
          ("Poche horizontale","Chargeurs 30 rounds","Moins rapide, mais plus compacte"),
          ("Rangement molle","Bocales, clés, outils","Garde les petits objets du bruit du métal")],
 ),
 'pages/equipement-sacs.html': dict(
   cat='Sacs', anchor='role',
   role='sac',
   intro="""Le sac est le seul objet qui transforme une run en profit. Un rig vous donne l'accès, le sac vous donne le volume. Et le sac a un prix invisible : chaque tranche de volume supplémentaire coûte de la mobilité, donc des secondes pour réagir.""",
   errs=["<strong>Prendre le plus grand sac disponible</strong> : un sac surchargé vous ralentit dans les rotations, et la rotation perdue vaut plus que le loot non ramassé.",
         "<strong>Remplir au point de non-retour</strong> : au-delà d'un certain poids, vous perdez plus de temps à l'extraction que ce que vous gagnez.",
         "<strong>Oublier le coût total de l'équipement</strong> : 900 000 K en Lockdown, le sac est le premier poste à faireraulic.",
         "<strong>Choisir un sac sans knowing la durée du raid</strong> : en Infected Zone, le sac est un handicap."],
   faq=[("Quel sac pour la S7&nbsp;?","Un sac de capacité moyenne en raid standard, un grand sac seulement quand vous avez une mission de loot précise."),
          ("Comment savoir si je suis trop chargé&nbsp;?","Sur l'indicateur de charge : au-delà d'un seuil, l'extraction devient lente et risquée."),
          ("Sac ou rig, lequel primero&nbsp;?","Le sac. Le rig est un plus, le sac est la base."),
          ("Le sac compte-t-il dans le plafond d'équipement&nbsp;?","Oui : les 900 000 K du Lockdown incluent tout l'équipement, sac compris.")],
   budget=[("Discret","15 000 – 40 000 K","Petit sac, une arme","Recon et fuite"),
           ("Équipier","40 000 – 90 000 K","Sac moyen, deux armes","Raid standard"),
           ("Chargeur","90 000 – 160 000 K","Grand sac + rig lourd","Mission de loot dédiée")],
   munis=[("Volume","Nombre de cases","Plus de volume = moins de mobilité"),
          ("Accès","Type d'ouverture","Rapide en combat, lente en rangé"),
          ("Charge","Poids supporté","Le vrai coût caché du sac")],
 ),
 'pages/equipement-tier-list.html': dict(
   cat='Tier list équipement', anchor='role',
   role='armure',
   intro="""Le classement des protections se joue sur deux axes, et les confondre est l'erreur la plus coûteuse du jeu : <strong>la classe de protection</strong> (combien de dégâts encaissés) et le <strong>niveau de pénétration</strong> (est-ce que ça traverse). Un gilet T6 médiocre perd contre une T4 bien choisie.""",
   errs=["<strong>Partir en T6 sans budget de munitions</strong> : le T6 ne sert que contre des munitions de haut niveau.",
         "<strong>Confondre protection et pénétration</strong> : ce sont deux chiffres distincts sur chaque armure.",
         "<strong>Ignorer le plafond de mode</strong> : Normal = T4 max, Lockdown = T5 max, Forbidden = T6. Le T6 est refusé en Normal.",
         "<strong>Dépasser le plafond de 900 000 K</strong> : le raid ne démarre pas tant qu'un objet n'est pas retiré."],
   faq=[("Quel tier viser&nbsp;?","Le <strong>T4</strong> en Normal, le <strong>T5</strong> en Lockdown : c'est là que se situe l'optimisation coût/efficacité."),
          ("T5 ou T6&nbsp;?","Le T6 est réservé au Forbidden et aux raids où vous savez que vous rencontrerez du T6."),
          ("Le casque compte-t-il&nbsp;?","Oui, pour les tirs à la tête — et la S7 a <strong>renforcé la récompense des headshots</strong>, ce qui rend le casque plus prioritaire qu'avant."),
          ("Comment figer un kit&nbsp;?","Le <a href='meta-loadout-optimizer.html'>Loadout Optimizer</a> applique les plafonds par mode et signale les dépassements.")],
   budget=[("Normal","80 000 – 180 000 K","Gilet T3-T4, casque T3","Le ratio rendement/sécurité maximal"),
           ("Lockdown","200 000 – 400 000 K","Gilet T4-T5, casque T4","Le kit de la majorité des joueurs"),
           ("Forbidden","450 000 – 900 000 K","Gilet T5-T6, casque T5","Réservé aux raids à très fort enjeu")],
   munis=[("Protection","Niveau 1 à 6","Cela décide combien de dégâts vous encaissez"),
          ("Pénétration","Niveau 1 à 6","Détermine si votre balle traverse la protection"),
          ("Zone couverte","Torse, tête, jambes","La tête est la zone la plus rentable à protéger en S7")],
 ),
}

# ---------------------------------------------------------------- gabarit
def build(cfg, idx):
    rows_muni = '\n'.join(
        '                <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>' % (m[0], m[1], m[2])
        for m in cfg['munis'])
    rows_err = '\n'.join('            <li>%s</li>' % e for e in cfg['errs'])
    rows_faq = '\n'.join(
        '          <h3 class="h4">%s</h3>\n          <p>%s</p>' % (q[0], q[1]) for q in cfg['faq'])
    rows_bud = '\n'.join(
        '                <tr><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>' % b
        for b in cfg['budget'])

    return '''
          <h2 id="regles">3. Les règles qui dictent le %s</h2>
          <p>%s</p>
          <ul class="zone-list">
            <li><strong>Plafonds par mode</strong> : Normal = T4 maximum, Lockdown = T5 maximum, Forbidden = T6. Le choix du mode décide de votre tier avant même votre budget.</li>
            <li><strong>Plafond de valeur</strong> : 900 000 K d'équipement en Lockdown. Au-delà, le raid refuse de démarrer.</li>
            <li><strong>RNG de pénétration supprimée</strong> : depuis la S7, la bonne munition traverse presque toujours. comptez sur votre munition, pas sur la chance.</li>
            <li><strong>TTK allongé, headshots récompensés</strong> : la précision compte davantage qu'en S6. Le premier tir placé vaut plus qu'une rafale.</li>
          </ul>

          <h2 id="munitions">4. Les munitions à connaître</h2>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Calibres de référence — %s</caption>
              <thead><tr><th scope="col">Munition</th><th scope="col">Armes</th><th scope="col">Ce qu'elle change</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>

          <h2 id="budget">5. Quel kit pour quel budget</h2>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Trois enveloppes pour trois usages</caption>
              <thead><tr><th scope="col">Profil</th><th scope="col">Budget</th><th scope="col">Configuration</th><th scope="col">Usage</th></tr></thead>
              <tbody>
%s
              </tbody>
            </table>
          </div>

          <h2 id="erreurs">6. Les erreurs qui coûtent cher</h2>
          <ul>
%s
          </ul>

          <h2 id="faq">7. FAQ</h2>
%s
''' % (cfg['role'], cfg['intro'], cfg['cat'], rows_muni, rows_bud, rows_err, rows_faq)


def main():
    for path, cfg in PAGES.items():
        p = ROOT / path
        s = p.read_text(encoding='utf-8')
        if 'id="faq"' in s:
            print('  %-34s deja enrichi' % path)
            continue
        end = s.find('        </article>')
        if end < 0:
            print('  ! %s : article introuvable' % path); continue
        s = s[:end] + build(cfg, 0) + '        ' + s[end:]

        # sommaire : ajoute les nouvelles entrees avant la fermeture de l'aside
        anchors = [('regles', '3. Les règles qui dictent le choix'),
                   ('munitions', '4. Les munitions'),
                   ('budget', '5. Quel kit pour quel budget'),
                   ('erreurs', '6. Les erreurs coûteuses'),
                   ('faq', '7. FAQ')]
        m = re.search(r'(<aside class="toc".*?)(</aside>)', s, re.S)
        if m:
            add = ''
            for a, lab in anchors:
                if 'href="#%s"' % a not in s:
                    add += '\n<a href="#%s" id="lnk-%s-%d">%s</a>' % (a, p.stem, 200 + len(add), lab)
            s = s[:m.end(1)] + add + s[m.end(1):]
        p.write_text(s, encoding='utf-8')
        print('  %-34s +5 sections' % path)


if __name__ == '__main__':
    main()
