#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - textes de narration, vague 10 : les 11 dernieres pages sans voix.

Contenu issu des pages concernees (pages/*.html) et des sources deja
recoupees : notes de mise a jour de la Saison 7 (16 septembre 2026),
catalogue de reference du guide communautaire, fiches de la base de donnees
de missions.

Meme controle que les vagues 9 et 9b : longueur entre 950 et 1 450
caracteres, aucun fragment multilingue (CJK, kana, hangul, cyrillique),
aucune expression anglaise, pas d'espace double, point final obligatoire.
"""
import pathlib
import re
import sys

DEST = pathlib.Path("tools/textes_audio")

MIN_LEN = 950
MAX_LEN = 1450

MOTIF_UNICODE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]")

INTERDITS = [
    " the ", " and ", " with ", " your ", " from ", " this ", " that ",
    " have ", " will ", " about ", " which ", " there ", " their ", " you ",
]

TEXTES = {}

TEXTES["armes-attachements"] = """Les attachements sont le second budget de votre kit, après l'arme elle-même, et c'est là que la plupart des joueurs se trompent. Plus de mille deux cents pièces sont recensées, mais une poignée compte vraiment. L'ordre de montage n'est pas une préférence esthétique, c'est une hiérarchie de gains : d'abord le recul vertical, donc un compensateur ou une bouche qui l'atténue, parce que c'est la statistique numéro un ; ensuite le recul horizontal, avec une poignée inclinée ou verticale, car c'est là que l'angle des gerbes se brise ; puis l'ergonomie, qui se mesure au temps de rechargement et à la vitesse d'épaulement ; et seulement ensuite la portée, avec un canon rallongé, si la carte l'exige. Le canon et la crosse viennent en dernier, sauf si une pièce saisonnière change les règles. La règle de coût suit la même logique : un bon montage coûte une fois et demie à deux fois le prix de l'arme, un excellent montage deux à trois fois ; au-delà de quatre fois, achetez une autre arme. Enfin, retenez que ces pièces se démontent et se revendent : une erreur d'achat se paie en munitions manquées."""

TEXTES["armes-attachements-s7"] = """La Saison 7 introduit le premier jeu d'attachements saisonniers de l'histoire d'Arena Breakout Infinite : quatre pièces exclusives, sur quatre armes précises. Ce sont des season kits, c'est-à-dire des pièces expérimentales démontables, et non des objets de collection qu'on admire dans un coffre. Les noms officiels, ceux que l'éditeur a publiés dans ses notes de mise à jour du seize septembre deux mille vingt-six, sont quatre : le kit entièrement automatique du PCC-9, qui rend cette arme capable de tirer en rafale continue ; le déclencheur binaire du M110, qui fait partir deux projectiles par pression de détente et donne à ce fusil de précision une puissance de dégâts immédiate ; le canon Vulcan du MPX, qui ouvre à la mitraillette des options de munitions à chair ; et le kit rafale du FAL, qui fait passer sa puissance de feu de moyenne-faible à élevée, au prix d'une cadence légèrement réduite. Deux erreurs coûtent cher ici. La première est de les acheter comme des pièces de collection : leur effet est mécanique, il se perd au démontage. La seconde est de les croire permanents : l'éditeur a précisé que ces kits seraient retirés à la fin de la saison. Vérifiez enfin la compatibilité de chaque pièce avec l'arme visée avant de conclure au marché."""

TEXTES["armes-carbine"] = """Entre la mitraillette et le fusil d'assaut, la carbine occupe une place à part : cadence modérée, portée moyenne à longue, tir fait pour tenir un axe plutôt que pour l'emporter. Huit carabines sont recensées dans le catalogue de référence, de la SVTU à deux cents coups par minute jusqu'à la M16 à six cent soixante, et leurs portées s'échelonnent de cinquante-quatre mètres pour la SA85M à soixante-treize pour la M16. Ce tableau raconte une chose simple : il n'existe pas une carabine, il existe des carabines, et le choix se fait par le budget et par la distance. Le SKS, trois cents coups par minute en sept virgule soixante-deux fois trente-neuf, reste le ticket d'entrée le plus rentable du jeu ; la M14 Carbine et la M16 montent d'un cran en puissance et en prix. Les règles qui dictent la carabine sont celles de la Saison 7 : la bonne munition l'emporte presque toujours, le minimum tier trois, tier quatre ou cinq pour les modes haut de gamme, et un plafond par mode, normal, lock-down et forbidden. Retenez ceci : une carabine à soixante pour cent de sa valeur vaut mieux qu'un fusil à prix plein perdu à la première rencontre."""

TEXTES["armes-lmg"] = """La famille de la mitigation lourde ne compte qu'une seule arme documentée dans le catalogue de référence : le RPK-16. Ce n'est pas un angle mort du catalogue, c'est une information en soi : une famille à une seule arme ne s'achète pas, elle se loue, pour une situation précise. Le RPK-16 est classé A-tier, partage sa munition cinq virgule quarante-cinq avec l'A545 et l'AK-12, et sa synergie logistique est donc parfaite : un seul type de munition à emporter pour trois armes. Sa portée utile se situe autour de cinquante-trois mètres, ce qui le place entre le MPX, plus cadent mais bien plus court, et l'U191, de même cadence mais plus lourd à manier. En suppression, sur Valley et sur Northridge, un fusil qui arrose ferme protège vos rotations de loot et termine les pushes. Mais en solo, la même arme devient un piège à bruit : elle vous signale à tout le monde. En duo ou en trio, elle devient un mur. Son argument principal reste le chargeur : cent projectiles, c'est de la suppression, pas du tir de précision."""

TEXTES["armes-nouveautes-s7"] = """La Saison 7 a introduit deux armes nouvelles, et elles occupent les deux extrêmes du catalogue. L'A545 est le roi du meta : cadence élevée, recul maîtrisé, portée effective augmentée par les correctifs de la saison, et elle s'impose aussi bien en duel qu'en suppression. L'AK-15SC, à l'inverse, est la terreur du combat rapproché : plus lourde, plus lente à manier, mais redoutable dans les pièces étroites et contre un ennemi qui surgit à cinq mètres. À ces deux armes s'ajoutent les quatre attachements saisonniers, qui transforment d'autres armes existantes : le PCC-9 qui gagne le tir entièrement automatique, le M110 qui gagne le déclencheur binaire, le MPX qui gagne le canon Vulcan, et le FAL qui gagne le kit rafale. Le contexte de l'équilibrage explique ces ajouts : les portées effectives ont été allongées, les headshots renforcés, le temps de mise à mort global allongé, et le hasard de pénétration des instances de classe cinq et six a été supprimé. Une seule conclusion à en tirer : ne verrouillez pas votre build au premier jour. Les changements arrivent, et votre configuration de lancement sera caduque avant la fin de la saison."""

TEXTES["armes-shotgun"] = """Le fusil à pompe tient une place à part dans le catalogue de la Saison 7 : l'USAS-12 est le seul shotgun du catalogue actuel, automatique, en douze gauge, avec deux cent soixante-quinze coups par minute et des dégâts instantanés à bout portant. Sa portée utile, en revanche, est courte : la règle du jeu est que la portée réelle du fusil à pompe se compte en une dizaine de mètres. Sa valeur tient donc à la surprise, pas à la distance. Le contexte de la saison le rend pertinent : en Normal, le plafond de l'équipement est de tier quatre, la cible est plus molle, et le buckshot écrase les mutants de la zone infectée. Mais il faut adapter son kit au lobby, et non à son ego : le plafond monte en lock-down, puis en forbidden. La discipline de jeu, c'est la porte : on pousse un angle, on tire dans l'embrasure, on recule. Pour le budget, la règle est simple : avec un canon et une optique corrects, le fusil à pompe coûte moins cher qu'une carabine et livre plus de dégâts au contact. Ce qu'il ne faut pas faire, c'est l'acheter pour tenir un combat à distance : personne ne l'a conçu pour cela."""

TEXTES["armes-sniper"] = """Le sniper gagne le jeu avant le premier click : c'est un problème de placement, de patience et de lecture, pas de puissance de feu. Deux bottes dominent la famille. Le M24, classé S-tier, est l'apex du bolt-action : avec les headshots renforcés de la Saison 7, un tir placé termine la majorité des opérateurs en une seule balle. Le Mosin-Nagant, classé C-tier, reste la botte budget la plus rentable, du premier wipe jusqu'au kilomètre final. Sa précision se joue sur trois points : la munition d'abord, car en neuf cinquante-quatre R il faut toujours vérifier la pénétration, et depuis la Saison 7 le hasard a été retiré, un tir bien planifié perce ; l'optique ensuite, avec un grossissement long qui sert à lire la cible à distance ; l'ancrage enfin, la position stable, le support, et l'angle de tir dégagé. Sur le terrain, le sniper se déplace en silence, s'installe, attend, et tire une fois. Le support n'est pas un luxe : c'est ce qui transforme une arme à plusieurs centaines de milliers de Koen en un tir qui ne part pas de travers."""

TEXTES["cosmetiques-dog-tags"] = """La plaque d'identité est le plus petit objet de loot d'Arena Breakout Infinite, et l'un des plus lourds en conséquences : elle dit qui vous a tué, avec quelle arme, et elle vaut de cinq cents Koen au rang rookie jusqu'à soixante-dix mille Koen au rang forbidden ou warlord. Elle pèse cent dix grammes et occupe un emplacement minuscule, ce qui la rend facile à laisser passer, et c'est bien tort. Elle ne sert pas qu'à orner l'étagère : elle solde certaines extractions, elle remplit l'étagère de plaques de votre Trophy Room, elle alimente le gachapon du mode Supplies Drops, elle valide des objectifs de mission, et elle se revend. La Saison 7 a ajouté ce qui manquait : des animations d'inspection et cinq animations d'interaction, qui transforment un objet de loot en objet que l'on regarde. Un piège subsiste : les bots de faible niveau portent aussi des plaques. Seuls un niveau trente ou un rang élevé prouvent qu'un joueur est humain. Reste la décision finale, vendre ou garder : gardez ce que vous visez au gachapon, vendez le reste avant la réinitialisation de saison."""

TEXTES["cosmetiques-skins-perso"] = """Les cosmétiques de personnage ne donnent aucun avantage : ni statistiques, ni avantage concurrentiel, ni rien qui se mesure en combat. Ils donnent autre chose, dans un jeu d'extraction où tout le monde se voit : une identité reconnaissable. La Saison 7 en propose trois Supply, lancés le seize septembre deux mille vingt-six, sur une fenêtre qui court jusqu'au vingt-neuf décembre : l'Emerald Arachnid, centré sur le personnage Emerald Web Arachne et ses skins d'armes, le Toxic Edge, centré sur le couteau Venomfang Tactical Karambit, et la Hazmat Suit, centrée sur la tenue. Les règles de dépense sont simples et documentées. Le premier tirage est gratuit sur chaque Supply : c'est l'échantillon avant l'investissement. Un seul Supply à la fois, car diluer sur deux bassins divise vos chances d'avoir le set complet. Et comparez toujours les passes achetées en Koen avec les Skin Supply Coupons, qui s'obtiennent gratuitement en mission. Le seul raccourci vraiment rentable est la complétion : posséder à la fois le personnage et le couteau débloque le fond d'écran Endless Weave. Enfin, retenez la règle de l'éditeur : ni le Koen ni la puissance de combat ne se vendent jamais."""

TEXTES["saison7-nouveautes"] = """Le seize septembre deux mille vingt-six, la Saison 7 Utopia a ouvert, et une saison change plus de choses qu'il n'y paraît. Côté combat : portées effectives augmentées, headshots renforcés, temps de mise à mort global allongé, ricochets supprimés, hasard de pénétration des instances de classe cinq et six retiré, torche portante moins énergivore. Côté zombies : six mutants, deux modes dédiés, l'Infected Zone en PvPvE et le Zombie Endless en PvE, plus No Man's Land, la Zombie Research et quarante missions. Côté équipement : l'A545 et l'AK-15SC, quatre season kits, et la grenade stun M290 désormais craftable à l'établi. Côté économie : les formules arrivent à leur niveau maximum dès le déblocage, les besoins en matériaux sont revus à la baisse, et les objets divers ont reçu de nouveaux usages. Côté loot : de nouveaux objets, de nouveaux collectibles rouges, et une salle de collection qui change de nature. Et les mécaniques : le nouveau système de recherche et de craft, le marchand en raid, les événements de saison. Retenez l'essentiel : le build du premier jour est un piège, et le pass ne contient aucune arme."""

TEXTES["univers-factions"] = """Le lore de Kamona repose sur quatre couches, et les comprendre évite de perdre un raid sur la mauvaise faction. Première couche : deux puissances étrangères se disputent l'île, Tevilla au nord, Colom au sud, chacune avec son unité d'élite. Deuxième couche : deux armées locales régulières, le MNST, front du Nord, et le CDIS, armée du Sud, plus une force dissidente, la Kamona Liberation Army, et un groupe qui refuse de choisir, EDELWEISS. Troisième couche : les entreprises militaires privées, au premier rang desquelles Blackgold Universal, bien équipée, disciplinée, et toujours du mauvais côté de l'armistice, avec sa troupe d'élite, l'Abyss Squad. Quatrième couche : les acteurs non belligérants, le Comité Sumek et le Kamona Investigation Bureau, et surtout les organisations criminelles, la Famille Antonio, les Mad Dogs et les Mutins du Polaris, qui vivent du chaos. Vous, vous incarnez un PMC indépendant : la couche qui arrive une fois que tout le monde est installé. Enfin, la règle de lecture : un boss vous apprend toujours à qui il appartient. Et trois dossiers restent non confirmés, la corporation Toland, les Cleaners et la figure Arachne, les projets Gungnir et Apostle : traitez-les comme des théories."""


def controler(slug, texte):
    erreurs = []
    n = len(texte)
    if n < MIN_LEN:
        erreurs.append("trop court (%d < %d)" % (n, MIN_LEN))
    if n > MAX_LEN:
        erreurs.append("trop long (%d > %d)" % (n, MAX_LEN))
    mult = MOTIF_UNICODE.findall(texte)
    if mult:
        erreurs.append("caractere multilingue %s" % sorted(set(mult)))
    for mot in INTERDITS:
        if mot in texte.lower():
            erreurs.append("expression anglaise %r" % mot)
    if re.search(r"\s{2,}", texte):
        erreurs.append("espace double")
    if texte != texte.strip():
        erreurs.append("espaces en bord")
    if not texte.endswith("."):
        erreurs.append("pas de point final")
    return erreurs


def main():
    echecs = 0
    for slug, texte in sorted(TEXTES.items()):
        erreurs = controler(slug, texte)
        if erreurs:
            print("  [KO] %s : %s" % (slug, " ; ".join(erreurs)))
            echecs += 1
            continue
        f = DEST / ("%s.txt" % slug)
        f.write_text(texte, encoding="utf-8")
        print("  [OK] %-28s %d caracteres" % (slug, len(texte)))
    if echecs:
        print("\n  %d texte(s) refuse(s)" % echecs)
        return 1
    print("\n  %d textes ecrits" % len(TEXTES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
