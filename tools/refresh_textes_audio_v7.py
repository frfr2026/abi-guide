#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABI NEXUS - redaction des 10 textes de narration de la vague 7.

Controles appliques avant ecriture :
  - longueur <= 1500 caracteres (le filtre de generation refuse au-dela)
  - aucun caractere CJK / kana / hangul / cyrillique
  - aucun mot du lexique qui declenche le refus du filtre
"""
import pathlib
import re
import sys

DEST = pathlib.Path("tools/textes_audio")
DEST.mkdir(parents=True, exist_ok=True)

INTERDITS = ["faire le mort", "tuer ", "fear", "headshot", "mise à mort"]
MOTIF_UNICODE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]")

TEXTES = {}

TEXTES["meta-tier-list-globale"] = (
    "La tier list globale de la Saison 7 classe soixante-dix-sept armes documentées en quatre "
    "catégories, de S à C. Elle commence par une règle d'honnêteté : un classement n'a de valeur "
    "que si l'on sait à quelle question il répond. Un tier list global est rassurant, mais il "
    "décrit une situation moyenne, celle où l'on ne sait pas encore contre qui l'on va se "
    "battre. Pour la plupart des joueurs, deux réponses suffisent : le H416 et l'A545 couvrent à la "
    "fois le combat rapproché et la portée moyenne. Pour l'efficacité en Koen, l'AK-12 s'impose. "
    "En combat intérieur, la P90 ou la PCC9 équipée de son kit automatique occupent le devant de la "
    "scène. Ce que la communauté formule le mieux tient en une phrase : la meilleure arme est celle "
    "avec laquelle vous touchez vos tirs. Une AK-74N bien maîtrisée vaut mieux qu'une A545 mal "
    "maîtrisée. Le classement par mode corrige la moyenne : en Lockdown le plafond d'armure "
    "descend au niveau 5, en Forbidden il disparaît, et le tier list global sous-estime l'AR-57. "
    "Les season kits, eux, expirent en fin de saison : traiter un kit comme une base permanente "
    "serait une erreur de budget."
)

TEXTES["equipement-sacs"] = (
    "Le sac ne protège pas : il détermine ce que vous pouvez rapporter. La règle de "
    "dimensionnement est arithmétique, pas empirique. Additionnez le volume de ce que vous comptez "
    "réellement rapporter, puis choisissez la taille immédiatement supérieure. Un sac surdimensionné "
    "n'améliore rien : il rend la fouille plus lente, l'extraction plus visible et la mort plus "
    "coûteuse. Le bon sac contient exactement ce que votre plan prévoit, plus une marge d'un objet. "
    "Le second réflexe est l'imbrication : un sac placé dans un autre sac, un rig dans un sac, "
    "occupent des cases qui ne seraient pas utilisées autrement, c'est de l'espace gratuit. "
    "L'erreur classique est l'inverse, un sac trop grand pour le contenu prévu. Attention au "
    "plafond de valeur d'équipement : en Lockdown la limite de neuf cent mille Koen inclut ce que "
    "vous portez, et un sac plein peut vous en faire franchir la porte. La question finale est "
    "simple : sac ou rig d'abord. Le rig organise l'accès rapide, le sac maximise le volume."
)

TEXTES["equipement-rigs"] = (
    "Rig ou gilet : la confusion la plus répandue porte sur la fonction. Un gilet protège, un rig "
    "transporte. Les deux occupent des emplacements différents et répondent à des besoins "
    "différents. L'erreur la plus coûteuse consiste à sacrifier la protection du torse pour gagner "
    "de la place de portage, alors que le torse est la zone qui reçoit le plus de balles en "
    "général. L'ordre d'achat rationnel est donc toujours le même : d'abord un torse correct, "
    "ensuite un rig de taille adaptée, et seulement ensuite l'optimisation du portage. La règle du "
    "rig positif compte les slots qu'un rig offre, puis les cases qu'il occupe. Un rig qui garde "
    "quatorze slots pour neuf cases occupées vous donne cinq cases de loot gratis, l'équivalent "
    "d'un sac entier, sans le poids. Un rig bien choisi se remplit de ce qui a le meilleur rapport "
    "valeur par case : attachements, munitions, médicaux, et casque quand le format le permet. La "
    "Tactical Belt, mastery cœur de la Saison 7, ajoute des slots de ceinture."
)

TEXTES["items-koen-economy"] = (
    "L'économie de Kamona repose sur une seule arithmétique : le coût de votre kit face à la "
    "valeur de ce que vous sortez. Un kit à quatre-vingt mille ou cent mille Koen est le cœur "
    "d'une économie saine. Une extraction à deux cent soixante-dix mille Koen couvre alors "
    "plusieurs morts. Un budget serré n'est pas une insulte tactique : c'est ce qui permet de "
    "jouer cinquante raids par semaine au lieu de trois. La règle que répète la communauté tient "
    "en une phrase : ne dépensez jamais plus de vingt pour cent de votre stash total dans une "
    "sortie. Avec cinq cent mille Koen en réserve, votre arme, votre armure, vos munitions et "
    "votre médical ne doivent pas dépasser cent mille Koen. Le reste de l'économie en découle. À la "
    "revente, deux repères comptent : posez légèrement sous le prix le plus bas pour vendre vite, "
    "entre le plancher et le prix moyen pour maximiser. Et vendez en lots les objets de faible "
    "valeur. Après le combat, les conteneurs restent et les joueurs sont partis : c'est là que se "
    "fait la marge."
)

TEXTES["meta-builds-roles"] = (
    "Un build n'est pas une liste d'objets : c'est une fonction, ce que vous faites pendant les "
    "douze minutes du raid. Chaque objet doit servir cette fonction. Si un emplacement ne sert pas "
    "le rôle, c'est de l'argent dans un sac qui ralentit votre course. Cinq rôles structurent le "
    "jeu. L'assaut, en catégorie S, tient le rôle central : cadence, portée moyenne et armure "
    "intermédiaire. Le sniper, en A, privilégie la précision longue distance et accepte de perdre "
    "en mobilité. Le combat rapproché, en A, mise sur la cadence et la maniabilité. Le lointier, "
    "en A, optimise le tir à distance et la discrétion. Le soutien, en A, porte les soins et les "
    "slots supplémentaires. En Saison 7, la classe d'armure est plafonnée par la difficulté : "
    "chaque build existe donc en version Normal, plafonnée au niveau 4, et Lockdown, plafonnée au "
    "niveau 5. Le build reste le même, seul l'équipement change. C'est exactement ce que calcule "
    "l'optimiseur de loadout. Chaque build existe en deux variantes : une version minimale qui "
    "reste sous le plafond de valeur, et une version complète qui assume le risque."
)

TEXTES["saison7-zombie-endless"] = (
    "Le Zombie Endless est le mode PvE de la saison. Vous ne risquez pas votre stash : le jeu vous "
    "attribue une classe au départ et un loadout initial correspondant. L'entrée coûte des Koen, "
    "sans limite de nombre de parties. Le principe tient en une phrase : survivre, pas extraire. "
    "Le niveau de menace monte continûment au fil de la raid : plus de mutants, plus forts. Quand "
    "tout l'effectif est tombé, ou quand l'équipe choisit d'extraire activement, la raid se "
    "termine. Chaque seconde survécue rapporte du Merit. Si un opérateur tombe, il passe en état "
    "downed permanent pour le reste de la raid : pas de réapparition, pas de réanimation. C'est la "
    "règle la plus dure du jeu, et elle change tout le plan. En solo, la priorité va à la distance "
    "et aux angles morts. En squad, la couverture compte davantage que la précision. Les "
    "techniques de terrain les plus citées consistent à rester en mouvement, à ne jamais "
    "s'arrêter dans un couloir, et à toujours garder une ligne de repli. Un marchand apparaît en "
    "Endless : c'est le seul endroit du mode où de l'équipement s'échange contre des Koen."
)

TEXTES["meta-loadout-optimizer"] = (
    "L'optimiseur de loadout répond à une question précise : quel kit maximisez-vous pour un mode, "
    "un rôle et un budget donnés. Vous choisissez un mode, qui fixe le plafond de tier et donc "
    "l'équipement possible, un rôle, qui pondère cadence, portée et catégorie d'arme, et un "
    "budget. L'outil sélectionne l'arme, la munition, le gilet et l'équipement annexe, calcule le "
    "coût total et signale les incohérences. Le constructeur de kit libre fait l'inverse : vous "
    "installez chaque pièce vous-même et l'outil mesure ce que vaut le résultat. Coût, masse, "
    "mobilité, cadence, contrôle du recul et compatibilité de tier sont recalculés à chaque "
    "changement. Ce que l'outil ne fait pas, c'est prédire le marché. Les prix viennent des bases "
    "de référence du site et fluctuent chaque semaine. Utilisez l'optimiseur pour structurer votre "
    "kit, jamais pour valider un achat : la décision d'investissement suit plutôt le calibre que "
    "l'arme exacte, puisque le 5.56 couvre treize armes et le 9×19 en couvre douze."
)

TEXTES["armes-builds"] = (
    "Cinq builds résument la Saison 7. L'A545, surnommé Utopia, est le build à tout faire : cadence "
    "élevée, recul vertical maîtrisé, et un prix qui reste dans les limites de la plupart des "
    "budgets de Lockdown. L'AK-12, surnommé Laser Budget, est l'arme du stash maigre : un budget "
    "minimal qui reste une arme de raid crédible. La Vector 45, surnommée Infected Clear, vise les "
    "hordes : cadence haute, portée courte, armure délibérément légère, le prix à payer en "
    "protection étant compensé par la vitesse. Le M24, surnommé Tribunal, répond à la précision "
    "longue distance. Le FAL, surnommé Forbidden Tribunal, revient en Saison 7 grâce à un kit de "
    "recul saisonnier appliqué au gunsmith. Avec lui revient une astuce de chargement applicable à "
    "toute arme à chargeur détaché : les munitions hautes sont placées en haut du chargeur, les "
    "munitions bon marché en dessous. C'est la munition chambrée qui détermine la classe de "
    "pénétration au moment du tir. La limite est évidente : dès que la cible change de calibre, ou "
    "qu'un rechargement survient au milieu d'un échange, l'avantage disparaît."
)

TEXTES["univers-dark-zone"] = (
    "La Dark Zone est le territoire de l'après-armistice : l'espace de Kamona où la guerre "
    "Nord-Sud n'a jamais vraiment cessé, mais où elle s'est transformée en conflit larvaire. Elle "
    "naît de l'intervention du Comité Sumek, qui met fin publiquement aux hostilités sans en "
    "résoudre les causes. Le jeu traduit la Dark Zone par trois paliers de risque officiels : "
    "Normal, Lockdown et Forbidden. Ce ne sont pas des zones de la carte : ce sont des règles de "
    "raid appliquées aux mêmes cartes. Le mode ne change pas votre loot, il change qui se trouve "
    "dans la zone avec vous. Trois origines officielles sont identifiées, dont les opérations Tac "
    "Ops, qui ont laissé derrière elles des résidus de conflit. Utopia ajoute une nouvelle couche "
    "à cet ensemble, et les questions ouvertes restent nombreuses : qui possède les échantillons "
    "d'Utopia, et dans quel but les factions se disputent-elles les indices. Les lois non écrites "
    "sont connues de tous : on ne fait pas confiance aux inconnus, et on ne montre pas ce que l'on "
    " transporte."
)

TEXTES["communaute-ressources"] = (
    "La quasi-totalité des problèmes de la communauté ne viennent pas du jeu, mais d'un faux lien. "
    "Les serveurs Discord clonés, les pages de codes de giveaway, les sites de Koen à bas prix sont "
    "des vecteurs de phishing à ciel ouvert. La règle d'or tient en une phrase : ne jamais suivre "
    "un lien trouvé par un moteur de recherche. Le seul point d'entrée de confiance est l'invitation "
    "publiée par l'éditeur dans ses propres annonces Steam. Le Discord officiel organise le "
    "matchmaking par région, avec un serveur par continent et des salons dédiés à la recherche "
    "d'équipe. Reddit, et en particulier le fil consacré à Arena Breakout Infinite, reste la "
    "meilleure source de retours d'expérience, à condition de vérifier la date des fils. Les bases "
    "de données communautaires permettent de lire la règle exacte d'un objet. GitHub abrite des "
    "outils utiles, calculateurs balistiques et gestionnaires de clés, mais aussi des dépôts à ne "
    "pas ouvrir. Les guides vidéo montrent la gestuelle et le déplacement, mais une vidéo "
    "antérieure à la mise à jour du 16 septembre 2026 décrit un monde qui n'existe plus. Le format "
    "court reste une piste et jamais une source."
)


def main():
    echecs = 0
    for slug, texte in TEXTES.items():
        texte = " ".join(texte.split())
        problemes = []
        if len(texte) > 1500:
            problemes.append(f"longueur {len(texte)} > 1500")
        m = MOTIF_UNICODE.findall(texte)
        if m:
            problemes.append(f"multilingue {set(m)}")
        bas = texte.lower()
        for mot in INTERDITS:
            if mot in bas:
                problemes.append(f"lexique bloquant '{mot.strip()}'")
        if problemes:
            echecs += 1
            print(f"  [!!] {slug} : {' ; '.join(problemes)}")
            continue
        (DEST / f"{slug}.txt").write_text(texte + "\n", encoding="utf-8")
        print(f"  [ok] {slug:28s} {len(texte):4d} caracteres")
    print(f"\n  {len(TEXTES) - echecs}/{len(TEXTES)} textes valides")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
