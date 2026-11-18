#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - textes de narration, vague 9b : memes textes que la vague 9,
avec les accents restores.

Les 13 textes de la vague 9 avaient ete ecrits sans accents, par prudence.
Mais le reste du corpus narratif du site est accentue, et le rendu synthesized
de ces 13 textes serait degrade : "piece" lu comme "pisse", "cout" sans
tilde, "meme" sans circonflexe. Ce script reprend les textes corriges de
tools/refresh_textes_audio_v9.py et y restitue les accents.

Meme controle que la vague 9 : longueur entre 950 et 1 450 caracteres,
aucun fragment multilingue (CJK, kana, hangul, cyrillique), aucune
expression anglaise, pas d'espace double, point final obligatoire.

Idempotent : ecrase les sources de la vague 9, qui sont remplacees.
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

TEXTES["armes-fusils-assaut"] = """Le fusil d'assaut est l'arme la plus polyvalente d'Arena Breakout Infinite, et celle que le jeu attend le plus souvent chez vous. En Saison 7, six modèles se partagent le haut du classement : l'A545, qui signe le meilleur rapport entre cadence et recul maîtrisé, le H416, refuge des budgets serrés, l'U191, l'arme la plus lourde du lot, l'AK-12, l'AK-15SC et l'AN-94. Le critère de choix n'est jamais la puissance brute, mais la distance à laquelle vous comptez tuer. Une arme de combat rapproché se juge sur sa cadence et son maniement ; une arme de cartouche se juge sur sa portée et la qualité de son viseur. La règle d'or tient en une phrase : le fusil d'assaut doit correspondre au niveau de risque de la zone que vous jouez. En Normal, une carabine à soixante pour cent de sa valeur vaut mieux qu'un fusil à prix plein que vous perdrez à la première rencontre. Retenez enfin que le prix d'une arme n'est qu'une partie du coût : s'y ajoutent l'optique, le canon et les munitions, et c'est cette somme qui décide de votre survie. Le meilleur fusil d'assaut n'est pas celui qui tue le plus, c'est celui que vous pouvez remplacer sans y laisser votre économie."""

TEXTES["armes-pistolets"] = """Le pistolet occupe une place à part dans Arena Breakout Infinite, et beaucoup de joueurs sous-estiment son rôle. Il n'est jamais votre arme de combat principale : c'est votre arme de survie, celle qui reste dans votre poche quand votre fusil est vide. Trois modèles reviennent sur Kamona : le Makarov, le TT-33 et l'APB. Le Makarov est le plus discret, le TT-33 le plus répandu, l'APB le plus rare. Un pistolet sert avant tout à ce que le jeu appelle un rat kit : entrer avec le strict minimum, garder une arme de secours, et sortir avant d'être vu. Sa valeur stratégique tient à une propriété que les autres armes n'ont pas : il ne vous coûte presque rien à perdre. Sur le plan des munitions, la règle est simple : la munition de pistolet n'est jamais chère, mais sa pénétration est faible, et une balle qui ne traverse pas une classe quatre est une balle perdue. Utilisez-le donc contre ce qu'il tue vite, et gardez vos munitions de qualité pour les cas où elles comptent vraiment."""

TEXTES["armes-dmr"] = """Le DMR occupe l'espace entre le fusil de précision et le fusil d'assaut : il ne vise pas une cible unique, il tient un secteur. C'est l'arme du joueur qui veut dominer une pièce à distance tout en gardant une issue de secours. Sa caractéristique distinctive est la distance de travail : là où le fusil d'assaut se bat jusqu'à trente mètres et où le sniper vise à deux cents, le DMR reste compétent de cinquante à cent cinquante mètres. Le choix de l'arme se fait sur deux axes : la précision du tir et la capacité à encaisser un échange rapproché. Un DMR trop lourd devient un pilon dans le corps à corps, et le jeu vous punit de cette erreur. La munition est le vrai sujet : chaque type a sa propre pénétration et ses propres dégâts, et les tiers de perforation ne se comportent pas de la même façon contre un gilet et contre un casque. Enfin, le DMR est souvent mal conseillé par les joueurs qui prétendent faire du tout-terrain : un modèle lourd à prix plein sur une carte où l'on tire à quinze mètres est un excellent moyen de perdre son budget en une seule sortie."""

TEXTES["armes-smg"] = """La mitraillette est l'arme des distances courtes, et son aveuglement a changé en Saison 7. Elle a longtemps été consultée comme le choix du pauvre, celui qui n'a pas les moyens d'un fusil d'assaut ; depuis la suppression du tir aléatoire sur les instances de classe cinq et six, elle est devenue une option de premier ordre contre les zones infectées. Sa force est la cadence, sa faiblesse est tout ce qui vient avec : le recul cumulatif, la précision qui s'effondre au-delà de trente mètres, et la consommation de munitions. Une mitraillette se construit donc autour d'une seule question : à quelle distance maximale vous tirez le plus souvent ? En dessous de vingt mètres, une cadence de neuf cents projectiles par minute transforme la pièce en zone de contrôle. Au-delà de quarante, elle devient un gaspillage. Les munitions font le reste du travail : les projectiles de faible percussion se comportent de façon prévisible à courte portée mais ne percent pas le gilet, il faut donc choisir son type en connaissance de cause. Enfin, la discipline de dégagement compte autant que l'arme : une mitraillette sans rechargement rapide est une arme qui vous achève à elle seule."""

TEXTES["equipement-armures"] = """Le gilet est l'équipement qui décide de votre temps de survie dans un combat, et son choix mérite plus de soin que celui de l'arme. La Saison 7 a changé la donne sur un point central : la pénétration d'arme contre les instances de classe cinq et six n'est plus aléatoire. Elle ne s'obtient plus par chance de tir, elle se provoque en abaissant la durabilité de l'armure sous un seuil donné. Conséquence directe : une armure de haute classe mal entretenue ne vous protège plus, et un coup bien placé peut percer un gilet que vous estimiez comme une garantie. Cela rebat les cartes de la protection : ce qui compte n'est plus seulement la classe, mais l'état de l'équipement et le type de munition que vous transportez. La règle de terrain est la suivante : ne sortez jamais une armure dont vous ne connaissez pas la durabilité restante, parce que la valeur de ce que vous portez sur le torso se mesure au moment du coup, pas au moment de l'achat. Et le second réflexe, en équipe, reste le même : la protection d'un membre de l'équipe ne vaut que s'il tire en même temps que vous."""

TEXTES["equipement-headsets"] = """Le casque audio ne change aucune statistique, et pourtant c'est l'un des équipements les plus discutés d'Arena Breakout Infinite. Il change une chose : le moment où vous apprenez qu'un ennemi existe. Et en jeu d'extraction, une information arrivée deux secondes trop tard vaut exactement zéro. Le mécanisme est simple. Chaque source de bruit dans la zone produit un son que le jeu module selon l'équipement que vous portez. Un casque lourd qui couvre les oreilles coupe une partie du spectre : vous entendez moins, mais les bruits graves passent. La Saison 7 a corrigé ce travers avec la maîtrise principale Acoustic Earpads, qui réduit l'effet de blocage des casques et rend cette option viable. Le conseil de terrain est donc le suivant : choisissez votre casque selon la carte et non selon le catalogue. Dans une zone ouverte et silencieuse, la captation large est un avantage net. Dans un lieu métallique où tout résonne, un casque directionnel vous fera entendre un pas derrière un mur. Et dans les deux cas, la règle reste la même : ce que vous entendez ne devient une information fiable qu'une fois la source vue."""

TEXTES["reglages-sensibilite"] = """Les réglages d'Arena Breakout Infinite sont le premier levier de performance, et le plus souvent mal réglé. Le point de départ est le Focal Point, c'est-à-dire l'origine de l'axe de visée. Déplacé trop haut, il fait grimper la sensibilité et votre viseur part à chaque mouvement de poignet. Placé trop bas, il colle le réticule au sol et gêne les corrections. La règle simple est de le poser au niveau de votre main, à hauteur du milieu du viseur, et de ne plus y toucher ensuite. La sensibilité, elle, se règle par grossissement et jamais globalement : une visée à deux fois demande une correction plus fine qu'une visée à une fois, et c'est exactement ce que les réglages par zoom permettent de faire. Le réglage de visibilité et d'images par seconde arbitre entre lisibilité et fluidité ; sur un écran correct, choisir la lisibilité coûte peu et fait gagner beaucoup en situation de combat. Enfin, les raccourcis sont sous-exploités : un inventaire à une touche, une astuce rapide et une commande de permutation permettent de changer de position en une fraction de seconde, ce qui vaut bien plus qu'une souris plus sensible."""

TEXTES["items-craft-workbench"] = """L'établi est le cœur de la progression hors raid d'Arena Breakout Infinite, et la Saison 7 l'a entièrement rechargé. Le changement le plus important est le suivant : une formule déblocée arrive désormais à son niveau maximal. Elle n'a plus besoin d'être améliorée pour atteindre son plafond, ce qui transforme des semaines de farm acharné en quelques minutes de manipulation. Le second changement concerne les matériaux : les besoins de la plupart des recettes ont été revus à la baisse, et beaucoup d'objets annexes ont reçu un usage. La conséquence pratique est directe : la liste des objets à afficher au marché s'allonge, et un poste d'objets jusqu'alors sans intérêt devient une source de revenus. La nouvelle mécanique de recherche d'amélioration ajoute une couche : les plans d'amélioration se trouvent dans les boîtes à documents, les vêtements et les tiroirs. Chaque formule peut produire deux résultats à la fois, et celui que vous ne sélectionnez pas est perdu : les résultats non choisis sont perdus définitivement. Les recettes sont conservées d'une saison à l'autre, mais les résultats de fabrication sont réinitialisés à chaque bascule. Le conseil de méthode est le suivant : ne fabriquez jamais ce que vous pouvez acheter moins cher au marché. Fabriquer n'est intéressant que si le coût des matériaux est nettement inférieur au prix de vente, ce qui est rarement le cas des armes complètes, et souvent le cas des composants."""

TEXTES["communaute-streamers"] = """Les streamers sont l'une des sources d'information les plus regardées de la communauté, et l'une des plus mal comprises. Une vidéo de gameplay montre ce qu'un tableau de chiffres ne montre jamais : la gestuelle, le déplacement, la façon dont un joueur se place dans une pièce avant d'y entrer. Mais une vidéo montre aussi les choix de son auteur, qui ne correspondent pas forcément à la règle exacte du jeu. La méthode qui fonctionne tient en trois vérifications. D'abord, la date : une vidéo antérieure à la mise à jour de la Saison 7 décrit un monde qui n'existe plus, en particulier sur les règles de territoire, sur les clés et sur le rechargement de l'arme. Ensuite, la source de l'information : quand un streamer annonce une règle, ce n'est pas la règle, c'est l'interprétation, et il peut se tromper. Enfin, le recoupement : une information ne devient fiable qu'après avoir été retrouvée dans une source officielle ou dans une base de données maintenue par la communauté. La règle la plus utile que vous tirerez de ces vidéos est négative : elles montrent quoi ne pas faire. Voir un raid raté, voir un joueur se faire tuer en entrant dans une pièce, voir une erreur de rechargement, cela s'apprend en une minute et se paie en plusieurs raids."""

TEXTES["cosmetiques-skins-armes"] = """Les skins d'armes sont, dans Arena Breakout Infinite, le premier poste de dépense purement esthétique, et c'est précisément ce qui en fait un choix difficile. Le prix d'un skin peut atteindre plusieurs centaines de milliers de Koen, et l'avantage concurrentiel est nul : deux joueurs avec la même arme et le même rechargement se battent à armes égales. Le premier filtre est donc la question que le catalogue officiel pose lui-même : allez-vous réellement équiper cette arme ? Un skin appliqué à une carabine que vous ne sortez jamais est un achat mort, et l'argent est bien mieux placé ailleurs. Le second filtre est la rareté perçue. Un set de plusieurs armes cohérentes vaut mieux qu'une pièce unique, parce qu'il donne l'impression d'un ensemble plutôt que d'un objet posé sur une arme qu'on ne regarde qu'en boutique. Enfin, la dynamique de la saison compte : un skin de la saison en cours sera remplacé, un skin d'une saison ancienne reste dans votre collection indéfiniment. La question la plus simple reste la meilleure : est-ce que cette arme sort de votre stash, oui ou non ? Dans le doute, gardez votre Koen."""

TEXTES["univers-lore"] = """Kamona est l'état principal de la franchise Arena Breakout, et son histoire se lit dans ses couches successives de conflit. La guerre Nord-Sud y a laissé des vestiges qui ne sont pas seulement historiques mais mécaniques : les zones à risque élevé ne sont pas un réglage de difficulté arbitraire, ce sont des territoires dont l'histoire explique la dangerosité. Le Comité Sumek, qui a mis fin publiquement aux hostilités, n'en a pas résolu les causes ; c'est précisément ce qui rend la situation post-armistice instable. La Dark Zone, l'espace où subsistent les opérations Tac Ops, en est la conséquence directe. La Saison 7 ajoute Utopia et sa couche de contamination, qui vient redéfinir ce que signifie le risque sur la carte. L'intérêt de ce récit est qu'il n'est pas décoratif : chaque couche d'histoire correspond à une règle de jeu. L'économie, les clés, les restrictions de territoire, les factions qui contrôlent certaines zones : tout cela découle de cette histoire. Comprendre pourquoi Valley est plus risquée que la ferme ne change pas la manière de jouer, mais cela change la manière de raisonner quand on doit choisir entre deux raids."""

TEXTES["items-collection-room"] = """La salle de collection est le musée personnel du joueur dans Arena Breakout Infinite, et depuis la Saison 7 elle a changé de nature. Ce n'était plus un simple musée d'objets : c'est devenu un lieu de gestion active, avec une limite de niveau augmentée et une capacité de rangement des objets rouges portée à neuf cent quatre-vingt-dix-neuf emplacements. Les objets rouges, ces drops rares dont la valeur se compte en centaines de milliers de Koen, y occupent une place à part entière. Deux points de vigilance méritent d'être signalés. Le premier concerne le repérage : le point rouge qui signale les nouveaux dog tags est désormais restreint à l'étagère des dog tags. Il n'est plus reporté sur l'écran principal de la Trophy Room ni dans l'entrée du lobby, ce qui supprime une source d'information gratuite pour les autres joueurs. Le second concerne la conservation : un objet rouge stocké ne rapporte rien, et la place qu'il occupe vous prive d'une place pour un objet qui, lui, se vend. La collection ne se défend pas toute seule : elle a besoin d'un arbitrage régulier, exactement comme le reste du stash."""

TEXTES["saison7-battle-pass"] = """Le pass de saison de la Saison 7 fonctionne sur le modèle classique, avec une piste gratuite et une piste premium, mais il a changé sur un point qui mérite d'être souligné : les récompenses de progression des missions d'activité incluent désormais un bonus issu des événements à durée limitée. Concrètement, vos événements de saison font monter votre palier de pass plus vite. La stratégie qui en découle est simple : priorisez les événements temporaires plutôt que les quêtes hebdomadaires, parce que leur progression de palier ne disparaît pas au changement de semaine. Le passe gratuit annonce littéralement des millions de Koen, ce qui en fait la source de revenu la plus stable du jeu si vous le collectez. La piste premium ajoute des skins et de l'accès au Battle Pass Store, et le coût est de cinq cents Bonds pour l'amélioration instantanée. Attention enfin au point que les joueurs oublient souvent : les récompenses d'étoile sont réinitialisées chaque lundi à cinq heures UTC et les récompenses non réclamées ne sont pas rééditées. Les quêtes de la ligne zombies de quarante missions suivent la même logique. Ce que le pass ne contient pas, ce sont les armes de la saison : elles se gagnent en jeu."""


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
    print("\n  %d textes accentues ecrits" % len(TEXTES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
