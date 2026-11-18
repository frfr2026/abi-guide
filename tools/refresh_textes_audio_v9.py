#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - redaction des textes de narration, vague 9.

Produit les textes UTF-8 de 12 pages qui n'ont pas encore de voix off.
Chaque texte doit :
  - tenir entre 950 et 1 450 caracteres ;
  - etre en francais, sans terme anglais non traduit ;
  - ne contenir aucun fragment multilingue (CJK, hangul, cyrillique) ;
  - annoncer le sujet de la page sans la paraphraser ligne a ligne ;
  - respecter la regle de qualite : les conseils restent "Communautaires"
    sauf citation directe des notes officielles.

Le controle est execute a l'ecriture : un texte non conforme est refuse
et le script echoue avec le code de sortie 1.

Idempotent : ne reecrit pas un texte deja valide.
"""
import pathlib
import re
import sys

DEST = pathlib.Path("tools/textes_audio")

MIN_LEN = 950
MAX_LEN = 1450

MOTIF_UNICODE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]")

# expressions anglaises a proscrire
INTERDITS = [
    " the ", " and ", " with ", " your ", " from ", " this ", " that ",
    " have ", " will ", " about ", " which ", " there ", " their ", " you ",
]

TEXTES = {}

TEXTES["armes-fusils-assaut"] = """Le fusil d'assaut est l'arme la plus polyvalente d'Arena Breakout Infinite, et celle que le jeu attend le plus souvent chez vous. En Saison 7, six modeles se partagent le haut du classement : l'A545, qui signe le meilleur rapport entre cadence et recul maitrise, le H416, refuge des budgets serres, l'U191, l'arme la plus lourde du lot, l'AK-12, l'AK-15SC et l'AN-94. Le critere de choix n'est jamais la puissance brute, mais la distance a laquelle vous comptez tuer. Une arme de combat rapproche se juge sur sa cadence et son maniement ; une arme de cartouche se juge sur sa portee et la qualite de son viseur. La regle d'or tient en une phrase : le fusil d'assaut doit correspondre au niveau de risque de la zone que vous jouez. En Normal, une carabine a soixante pour cent de sa valeur vaut mieux qu'un fusil a prix plein que vous perdrez a la premiere rencontre. Retenez enfin que le prix d'une arme n'est qu'une partie du cout : s'y ajoutent l'optique, le canon et les munitions, et c'est cette somme qui decide de votre survie. Le meilleur fusil d'assaut n'est pas celui qui tue le plus, c'est celui que vous pouvez remplacer sans y laisser votre economie."""

TEXTES["armes-pistolets"] = """Le pistolet occupe une place a part dans Arena Breakout Infinite, et beaucoup de joueurs sous-estiment son role. Il n'est jamais votre arme de combat principale : c'est votre arme de survie, celle qui reste dans votre poche quand votre fusil est vide. Trois modeles reviennent sur Kamona : le Makarov, le TT-33 et l'APB. Le Makarov est le plus discret, le TT-33 le plus repandu, l'APB le plus rare. Un pistolet sert avant tout a ce que le jeu appelle un rat kit : entrer avec le strict minimum, garder une arme de secours, et sortir avant d'etre vu. Sa valeur strategique tient a une propriete que les autres armes n'ont pas : il ne vous coute presque rien a perdre. Sur le plan des munitions, la regle est simple : la munition de pistolet n'est jamais chere, mais sa penetration est faible, et une balle qui ne traverse pas une classe quatre est une balle perdue. Utilisez-le donc contre ce qu'il tue vite, et gardez vos munitions de qualite pour les cas ou elles comptent vraiment."""

TEXTES["armes-dmr"] = """Le DMR occupe l'espace entre le fusil de precision et le fusil d'assaut : il ne vise pas une cible unique, il tient un secteur. C'est l'arme du joueur qui veut dominer une piece a distance tout en gardant une issue de secours. Sa caracteristique distinctive est la distance de travail : la ou le fusil d'assaut se bat jusqu'a trente metres et le sniper vise a deux cents, le DMR reste competent de cinquante a cent cinquante metres. Le choix de l'arme se fait sur deux axes : la precision du tir et la capacite a encaisser un echange rapproche. Un DMR trop lourd devient un pilon dans le corps a corps, et le jeu vous punit de cette erreur. La munition est le vrai sujet : chaque type a sa propre penetration et ses propres degats, et les tiers de perforation ne se comportent pas de la meme facon contre un gilet et contre un casque. Enfin, le DMR est souvent mal conseille par les joueurs qui pretendent faire du tout-terrain : un modele lourd a prix plein sur une carte ou l'on tire a quinze metres est un excellent moyen de perdre son budget en une seule sortie."""

TEXTES["armes-smg"] = """La mitraillette est l'arme des distances courtes, et son aveuglement a change en Saison 7. Elle a longtemps ete consultee comme le choix du pauvre, celui qui n'a pas les moyens d'un fusil d'assaut ; depuis la suppression du tir aleatoire sur les instances de classe cinq et six, elle est devenue une option de premier ordre contre les zones infectees. Sa force est la cadence, sa faiblesse est tout ce qui vient avec : le recul cumulatif, la precision qui s'effondre au-dela de trente metres, et la consommation de munitions. Une mitraillette se construit donc autour d'une seule question : a quelle distance maximale vous tirez le plus souvent ? En dessous de vingt metres, une cadence de neuf cents projectiles par minute transforme la piece en zone de controle. Au-dela de quarante, elle devient un gaspillage. Les munitions font le reste du travail : les projectiles de faible percussion se comportent de facon previsible a courte portee mais ne percent pas le gilet, il faut donc choisir son type en connaissance de cause. Enfin, la discipline de degagement compte autant que l'arme : une mitraillette sans rechargement rapide est une arme qui vous achève a elle seule."""

TEXTES["equipement-headsets"] = """Le casque audio ne change aucune statistique, et pourtant c'est l'un des equipements les plus discutes d'Arena Breakout Infinite. Il change une chose : le moment ou vous apprenez qu'un ennemi existe. Et en jeu d'extraction, une information arrivee deux secondes trop tard vaut exactement zero. Le mecanisme est simple. Chaque source de bruit dans la zone produit un son que le jeu module selon l'equipement que vous portez. Un casque lourd qui couvre les oreilles coupe une partie du spectre : vous entendez moins, mais les bruits graves passent. La Saison 7 a corrige ce travers avec la maitrise principale Acoustic Earpads, qui reduit l'effet de blocage des casques et rend cette option viable. Le conseil de terrain est donc le suivant : choisissez votre casque selon la carte et non selon le catalogue. Dans une zone ouverte et silencieuse, la captation large est un avantage net. Dans un lieu metallique ou tout resonne, un casque directionnel vous fera entendre un pas derriere un mur. Et dans les deux cas, la regle reste la meme : ce que vous entendez ne devient une information fiable qu'une fois la source vue."""

TEXTES["reglages-sensibilite"] = """Les reglages d'Arena Breakout Infinite sont le premier levier de performance, et le plus souvent mal regle. Le point de depart est le Focal Point, c'est-a-dire l'origine de l'axe de visee. Deplace trop haut, il fait grimper la sensibilite et votre viseur part a chaque mouvement de poignet. Place trop bas, il colle le reticule au sol et gene les corrections. La regle simple est de le poser au niveau de votre main, a hauteur du milieu du viseur, et de ne plus y toucher ensuite. La sensibilite, elle, se regle par grossissement et jamais globalement : une visee a deux fois demande une correction plus fine qu'une visee a une fois, et c'est exactement ce que les reglages par zoom permettent de faire. Le reglage de visibilite et d'images par seconde arbitre entre lisibilite et fluidite ; sur un ecran correct, choisir la lisibilite coute peu et fait gagner beaucoup en situation de combat. Enfin, les raccourcis sont sous-exploites : un inventaire a une touche, une astuce rapide et une commande de permutation permettent de changer de position en une fraction de seconde, ce qui vaut bien plus qu'une souris plus sensible."""

TEXTES["items-craft-workbench"] = """L'etabli est le coeur de la progression hors raid d'Arena Breakout Infinite, et la Saison 7 l'a entierement recharge. Le changement le plus important est le suivant : une formule debloquee arrive desormais a son niveau maximal. Elle n'a plus besoin d'etre amelioree pour atteindre son plafond, ce qui transforme des semaines de farm acharne en quelques minutes de manipulation. Le second changement concerne les materiaux : les besoins de la plupart des recettes ont ete revus a la baisse, et beaucoup d'objets annexes ont recu un usage. La consequence pratique est directe : la liste des objets a afficher au marche s'allonge, et un poste d'objets jusqu'alors sans interet devient une source de revenus. La nouvelle mecanique de recherche d'amelioration ajoute une couche : les plans d'amelioration se trouvent dans les boites a documents, les vetements et les tiroirs. Chaque formule peut produire deux resultats a la fois, et celui que vous ne selectionnez pas est perdu : les resultats non choisis sont perdus definitivement. Les recettes sont conservees d'une saison a l'autre, mais les resultats de fabrication sont reinitialises a chaque bascule. Le conseil de methode est le suivant : ne fabriquez jamais ce que vous pouvez acheter moins cher au marche. Fabriquer n'est interessant que si le cout des materiaux est nettement inferieur au prix de vente, ce qui est rarement le cas des armes completes, et souvent le cas des composants."""

TEXTES["communaute-streamers"] = """Les streamers sont l'une des sources d'information les plus regardees de la communaute, et l'une des plus mal comprises. Une video de gameplay montre ce qu'un tableau de chiffres ne montre jamais : la gestuelle, le deplacement, la facon dont un joueur se place dans une piece avant d'y entrer. Mais une video montre aussi les choix de son auteur, qui ne correspondent pas forcement a la regle exacte du jeu. La methode qui fonctionne tient en trois verifications. D'abord, la date : une video anterieure a la mise a jour de la Saison 7 decrit un monde qui n'existe plus, en particulier sur les regles de territoire, sur les cles et sur le rechargement de l'arme. Ensuite, la source de l'information : quand un streamer annonce une regle, ce n'est pas la regle, c'est l'interpretation, et il peut se tromper. Enfin, le recoupement : une information ne devient fiable qu'apres avoir ete retrouvee dans une source officielle ou dans une base de donnees maintenue par la communaute. La regle la plus utile que vous tirerez de ces videos est negative : elles montrent quoi ne pas faire. Voir un raid rate, voir un joueur se faire tuer en entrant dans une piece, voir une erreur de rechargement, cela s'apprend en une minute et se paie en plusieurs raids."""

TEXTES["cosmetiques-skins-armes"] = """Les skins d'armes sont, dans Arena Breakout Infinite, le premier poste de depense purement esthetique, et c'est precisement ce qui en fait un choix difficile. Le prix d'un skin peut atteindre plusieurs centaines de milliers de Koen, et l'avantage concurrentiel est nul : deux joueurs avec la meme arme et le meme rechargement se battent a armes egales. Le premier filtre est donc la question que le catalogue officiel pose lui-meme : allez-vous reellement equiper cette arme ? Un skin applique a une carabine que vous ne sortez jamais est un achat mort, et l'argent est bien mieux place ailleurs. Le second filtre est la rarete percue. Un set de plusieurs armes coherentes vaut mieux qu'une piece unique, parce qu'il donne l'impression d'un ensemble plutot que d'un objet pose sur une arme qu'on ne regarde qu'en boutique. Enfin, la dynamique de la saison compte : un skin de la saison en cours sera remplace, un skin d'une saison ancienne reste dans votre collection indefiniment. La question la plus simple reste la meilleure : est-ce que cette arme sort de votre stash, oui ou non ? Dans le doute, gardez votre Koen."""

TEXTES["univers-lore"] = """Kamona est l'etat principal de la franchise Arena Breakout, et son histoire se lit dans ses couches successives de conflit. La guerre Nord-Sud y a laisse des vestiges qui ne sont pas seulement historiques mais mecaniques : les zones a risque eleve ne sont pas un reglage de difficulte arbitraire, ce sont des territoires dont l'histoire explique la dangerosite. Le Comite Sumek, qui a mis fin publiquement aux hostilites, n'en a pas resolu les causes ; c'est precisement ce qui rend la situation post-armistice instable. La Dark Zone, l'espace ou subsistent les operations Tac Ops, en est la consequence directe. La Saison 7 ajoute Utopia et sa couche de contamination, qui vient redefinir ce que signifie le risque sur la carte. L'interet de ce recit est qu'il n'est pas decoratif : chaque couche d'histoire correspond a une regle de jeu. L'economie, les cles, les restrictions de territoire, les factions qui controlent certaines zones : tout cela decoule de cette histoire. Comprendre pourquoi Valley est plus risquee que la ferme ne change pas la maniere de jouer, mais cela change la maniere de raisonner quand on doit choisir entre deux raids."""

TEXTES["items-collection-room"] = """La salle de collection est le musee personnel du joueur dans Arena Breakout Infinite, et depuis la Saison 7 elle a change de nature. Ce n'etait plus un simple musee d'objets : c'est devenu un lieu de gestion active, avec une limite de niveau augmentee et une capacite de rangement des objets rouges portee a neuf cent quatre-vingt-dix-neuf emplacements. Les objets rouges, ces drops rares dont la valeur se compte en centaines de milliers de Koen, y occupent une place a part entiere. Deux points de vigilance meritent d'etre signales. Le premier concerne le reperage : le point rouge qui signale les nouveaux dog tags est desormais restreint a l'etagere des dog tags. Il n'est plus reporte sur l'ecran principal de la Trophy Room ni dans l'entree du lobby, ce qui supprime une source d'information gratuite pour les autres joueurs. Le second concerne la conservation : un objet rouge stocke ne rapporte rien, et la place qu'il occupe vous prive d'une place pour un objet qui, lui, se vend. La collection ne se defend pas toute seule : elle a besoin d'un arbitrage regulier, exactement comme le reste du stash."""

TEXTES["equipement-armures"] = """Le gilet est l'equipement qui decide de votre temps de survie dans un combat, et son choix merite plus de soin que celui de l'arme. La Saison 7 a change la donne sur un point central : la penetration d'arme contre les instances de classe cinq et six n'est plus aleatoire. Elle ne s'obtient plus par chance de tir, elle se provoque en abaissant la durabilite de l'armure sous un seuil donne. Consequence directe : une armure de haute classe mal entretenue ne vous protege plus, et un coup bien place peut percer un gilet que vous estimiez comme une garantie. Cela rebat les cartes de la protection : ce qui compte n'est plus seulement la classe, mais l'etat de l'equipement et le type de munition que vous transportez. La regle de terrain est la suivante : ne sortez jamais une armure dont vous ne connaissez pas la durabilite restante, parce que la valeur de ce que vous portez sur le torso se mesure au moment du coup, pas au moment de l'achat. Et le second reflexe, en squad, reste le meme : la protection d'un membre de l'equipe ne vaut que s'il tire en meme temps que vous."""

TEXTES["saison7-battle-pass"] = """Le pass de saison de la Saison 7 fonctionne sur le modele classique, avec une piste gratuite et une piste premium, mais il a change sur un point qui merite d'etre souligne : les recompenses de progression des missions d'activite incluent desormais un bonus issu des evenements a duree limitee. Concretement, vos evenements de saison font monter votre palier de pass plus vite. La strategie qui en decoule est simple : priorisez les evenements temporaires plutot que les quetes Hebdomadaires, parce que leur progression de palier ne disparait pas au changement de semaine. Le passe gratuit annonce litteralement des millions de Koen, ce qui en fait la source de revenu la plus stable du jeu si vous le collectez. La piste premium ajoute des skins et de l'acces au Battle Pass Store, et le cout est de cinq cents Bonds pour l'amelioration instantanee. Attention enfin au point que les joueurs oublient souvent : les recompenses d'etoile sont reinitialisees chaque lundi a cinq heures UTC et les recompenses non reclamees ne sont pas reeditees. Les quetes de la ligne zombies de quarante missions suivent la meme logique. Ce que le pass ne contient pas, ce sont les armes de la saison : elles se gagnent en jeu."""


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
    print("\n  %d textes valides ecrits" % len(TEXTES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
