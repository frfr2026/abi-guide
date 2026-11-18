#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - vague H : le sondage de mi-saison de l'editeur (17 novembre 2026).

Recherche du 18/11/2026 sur YouTube et les guides de season 7.

Constat : le guide ne parlait pas du sondage de mi-saison que MoreFun a ouvert
en jeu sur les regles d'entree de Lockdown, Forbidden Zone et du Warlord
Tournament. Ce document est le premier signal officiel d'une revision possible
des plafonds de la Saison 7.

1) pages/communaute-patch-notes.html
   - nouvelle section 5 : le sondage, ses cinq questions, ce qu'il n'est pas ;
   - renumerotation des sections 5 a 8 en 6 a 9, sommaire compris ;
   - entree de chronologie au 17 novembre 2026 ;
   - source communautaire (capture video du sondage) et mention "non confirme".

2) pages/saison8-attente.html
   - encart "signal de fond" dans les signaux d'annonce ;
   - question de FAQ sur un changement eventuel des regles d'entree.

3) pages/meta-strategies-s7.html
   - encart : le plafond Lockdown pourrait baisser, ce qu'il faut en faire.

4) pages/equipement-tier-list.html
   - rappel : la ligne Lockdown T5 reste valide, mais elle est en discussion.

Chaque bloc insere est encadre par un marqueur : relancer le script remplace
le contenu encadre au lieu de le dupliquer.

Idempotent.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGES = RACINE / "pages"


def inserer_balise(s, ancre, bloc):
    """Insere ou remplace un bloc balise juste avant l'ancre donnee."""
    nom = bloc.split("-->")[0].strip()
    marqueur_open = nom
    marqueur_close = nom.replace(":OPEN", ":CLOSE") + "-->"

    i = s.find(marqueur_open)
    if i != -1:
        j = s.find(marqueur_close, i)
        if j == -1:
            print("  [KO] marqueur de fin absent :", marqueur_open)
            return s, 1
        fin = j + len(marqueur_close)
        while s[fin:fin + 3] == "-->":
            fin += 3
        s = s[:i] + bloc + s[fin:]
        return s, 0

    k = s.find(ancre)
    if k == -1:
        print("  [KO] ancre introuvable :", ancre[:70])
        return s, 1
    s = s[:k] + bloc + "\n" + s[k:]
    return s, 0


# ==========================================================================
# 1. communaute-patch-notes.html
# ==========================================================================

SECTION_SONDAGE = """<!--VEILLE-H:SONDAGE:OPEN-->
<h2 id="sondage">5. Le sondage de mi-saison : l'éditeur demande son avis sur les règles d'entrée</h2>
          <p>En novembre 2026, MoreFun a mis en jeu un <strong>questionnaire court sur les règles d'entrée</strong> en Lockdown, en Forbidden Zone et au Warlord Tournament. Le sondage prend quatre à cinq minutes et s'accompagne d'une récompense. C'est une <strong>consultation</strong> : aucune des propositions qu'il présente n'est une règle appliquée, et aucune date n'accompagne le document. <span class="src-tag src-officiel">Officiel</span></p>

          <div class="table-wrap">
            <table class="data-table">
              <caption>Les cinq questions du sondage de mi-saison, et ce qu'elles remettraient en cause</caption>
              <thead><tr><th scope="col">Question posée</th><th scope="col">Ce qu'elle mesure</th><th scope="col">Ce qu'elle changerait si elle était retenue</th></tr></thead>
              <tbody>
                <tr><td><strong>Activité</strong> — « sur les quatorze derniers jours, combien de fois avez-vous joué ? »</td><td>La practice réelle de la base, tout simplement.</td><td>Rien : c'est un indicateur de taille d'audience.</td></tr>
                <tr><td><strong>Style de jeu</strong> — « lequel de ces profils décrit le mieux votre façon de jouer ? »</td><td>Un profil type (agressif, variable selon la situation).</td><td>Rien : c'est un indicateur de comportement.</td></tr>
                <tr><td><strong>Mode préféré</strong> — « quel mode préférez-vous, et pourquoi Lockdown plutôt que Forbidden Zone ? »</td><td>Les raisons réelles du choix : moins de rencontres avec des tricheurs supposés, une gamme d'armes plus large qui restent viables, ou une rentabilité plus régulière avec moins de risque financier.</td><td>La hiérarchie des modes : si « moins de tricheurs » domine, l'éditeur a un problème de concurrence à traiter, pas un problème de réglage.</td></tr>
                <tr><td><strong>Plafond de munitions en Lockdown</strong> — «Soutiendriez-vous la baisse du tier maximum de munitions en Lockdown de T5 à T4, à l'exception des munitions de sniper ? »</td><td>L'appétence pour un Lockdown sans T5.</td><td>L'armure et les casques T5 resteraient autorisés ; <strong>T4 deviendrait le plafond des munitions</strong> pour tout le reste, et les calibres de sniper conserveraient T5.</td></tr>
                <tr><td><strong>Valeur d'équipement minimale</strong> — « soutiendriez-vous l'augmentation de la valeur d'équipement minimale requise pour entrer en Forbidden Zone et au Warlord Tournament ? »</td><td>L'appétence pour un accès plus cher aux modes à risque élevé.</td><td>Les seuils actuels — 450 000 Koen en Forbidden Zone, 600 000 à Airport — remonteraient. La communauté demande ce relèvement depuis un an.</td></tr>
              </tbody>
            </table>
          </div>

          <div class="callout callout-warning">
            <h3 class="h4">Ce que ce sondage n'est pas</h3>
            <p>Ce n'est <strong>pas</strong> une note de patch, <strong>pas</strong> une annonce de règles et <strong>pas</strong> une date de bascule. La phrase qui compte vient de l'analyse de la vidéo qui a capté le questionnaire : <em>« These proposals are not confirmed changes. »</em> Les règles en vigueur restent celles de la Saison 7 — <strong>T4 et moins en Normal, T5 et moins en Lockdown</strong>. Toute page qui présente déjà le « Lockdown en T4 » comme une règle applicable se trompe. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>Un point de méthode : le questionnaire est bien une communication de l'éditeur, mais il n'a fait l'objet d'aucune publication officielle consultable sur le fil Steam ni sur le site de MoreFun. Il est connu par les captures d'écran et la vidéo de la communauté. <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

          <div class="callout callout-info">
            <h3 class="h4">Ce que la communauté a répondu : deux camps, et une vraie question de classement</h3>
            <p>La question du plafond de munitions a soulevé plus de trois cents commentaires. Le camp du <strong>T4</strong> argues que les combats dureraient plus longtemps, que l'écart de niveau entre un solo et un groupe T5 se refermerait, et que les armes « à munitions bon marché » ne domineraient plus. Le camp du <strong>statu quo</strong> répond que le <strong>temps de mise à mort s'allongerait</strong> — ce qui est défavorable au joueur solo face à un groupe complet — que le plafond de 900 000 Koen pousse déjà vers l'armure usée, et que le retrait du T5 ferait baisser le loot récupéré. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>Le point technique le plus intéressant est le troisième : le <strong>7.62×51</strong> est partagé par le M24, le Mk14, le M110, le M14, le FAL, le BM59 et le G3. Si l'exception « sniper » s'appliquait à la munition et non à la <em>catégorie d'arme</em>, le FAL et le G3 — rangés dans l'atelier parmi les fusils d'assaut — resteraient les machines T5 les plus familiales du jeu, en automatique. D'où la question ouverte : où passe la frontière entre « sniper » et « fusil de précision » ? La communauté distingue les snipers (Mosin, M24, SJ-06) des armes de précision semi-automatiques ; l'éditeur n'a rien tranché. <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>

          <div class="callout callout-success">
            <h3 class="h4">Ce que cela change pour vous, aujourd'hui</h3>
            <p>Trois consequences concretes. D'abord, <strong>n'achetez pas de munitions T5 en gros pour Lockdown</strong> : elles sont autorisées aujourd'hui et peuvent ne plus l'être. Ensuite, gardez vos <strong>kits modulaires</strong> — une armure T5 et des munitions T4 permettent de s'adapter au plafond nouveau sans refaire un achat. Enfin, si vous pariez sur un Lockdown « sans T5 », vous ne touchez aucune exception sniper : gardez une arme de ce calibre en réserve, c'est elle qui ferait la différence si l'exception sniper passe. <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
<!--VEILLE-H:SONDAGE:CLOSE-->"""

SOURCE_VIDEO = """<!--VEILLE-H:SRC-SONDAGE:OPEN-->
            <li><span class="src-name">Micavity Cat — « This Change Could Be MASSIVE For Arena Breakout Infinite »</span> — vidéo du 17 novembre 2026 (10 min 02, 11 447 vues au moment de la consultation) : capture et lecture du sondage de mi-saison de MoreFun sur les règles d'entrée en Lockdown, Forbidden Zone et Warlord Tournament, et discussion des arguments de la communauté dans les commentaires. <a href="https://www.youtube.com/watch?v=6Lq5cas71fQ" target="_blank" rel="noopener" id="lnk-communaute-patch-notes-157">youtube.com<span class="sr-only"> (nouvel onglet)</span></a></li>
<!--VEILLE-H:SRC-SONDAGE:CLOSE-->"""

MENTION_NON_CONFIRME = """<!--VEILLE-H:NON-CONFIRME:OPEN-->
            <li>Les deux propositions du <strong>sondage de mi-saison du 17 novembre 2026</strong> — baisse du plafond de munitions en Lockdown à T4 (exception pour les calibres de sniper) et relèvement de la valeur d'équipement minimale en Forbidden Zone et au Warlord Tournament — sont des <strong>propositions en consultation</strong>, pas des règles en vigueur. Rien n'est daté, rien n'est appliqué ; le seuil de 450 000 Koen reste la règle en vigueur.</li>
<!--VEILLE-H:NON-CONFIRME:CLOSE-->"""

CHRONO_SONDAGE = """<!--VEILLE-H:CHRONO-SONDAGE:OPEN-->
            <li><span class="up-date">17 nov. 2026</span><span class="up-body"><strong>Sondage de mi-saison sur les règles d'entrée</strong><p>MoreFun consulte la communauté sur le plafond de munitions en Lockdown (T5 vers T4, exception pour les calibres de sniper) et sur la valeur d'équipement minimale requise en Forbidden Zone et au Warlord Tournament. Consultation avec récompense, sans date ni règle appliquée.</p></span></li>
<!--VEILLE-H:CHRONO-SONDAGE:CLOSE-->"""


def maj_patch_notes():
    chemin = PAGES / "communaute-patch-notes.html"
    s = chemin.read_text(encoding="utf-8")
    erreurs = 0

    # 1. renumerotation des sections 5 a 8 -> 6 a 9 (titres et sommaire)
    renum = [
        ('<h2 id="sources">8. Sources</h2>', '<h2 id="sources">9. Sources</h2>'),
        ('<h2 id="historique">7. Chronologie des mises à jour de la Saison 7</h2>',
         '<h2 id="historique">8. Chronologie des mises à jour de la Saison 7</h2>'),
        ('<h2 id="lire">6. Méthode : lire une note de patch en dix minutes</h2>',
         '<h2 id="lire">7. Méthode : lire une note de patch en dix minutes</h2>'),
        ('<h2 id="securite">5. Les rapports de sécurité : le suivi que personne ne lit</h2>',
         '<h2 id="securite">6. Les rapports de sécurité : le suivi que personne ne lit</h2>'),
        ('>8. Sources</a>', '>9. Sources</a>'),
        ('>7. Chronologie des mises à jour</a>', '>8. Chronologie des mises à jour</a>'),
        ('>6. Lire une note en dix minutes</a>', '>7. Lire une note en dix minutes</a>'),
        ('>5. Les rapports de sécurité</a>', '>6. Les rapports de sécurité</a>'),
    ]
    for avant, apres in renum:
        if apres in s:
            continue
        if avant not in s:
            print("  [KO] renumerotation introuvable :", avant[:60])
            erreurs += 1
            continue
        s = s.replace(avant, apres, 1)

    # 2. entree de sommaire vers la nouvelle section 5
    toc_avant = '<a href="#live" id="lnk-communaute-patch-notes-115">4. Le format des Live Updates</a>'
    toc_apres = (toc_avant + '\n'
                 '          <a href="#sondage" id="lnk-communaute-patch-notes-158">5. Le sondage de mi-saison</a>')
    if 'href="#sondage"' not in s:
        if toc_avant not in s:
            print("  [KO] ancre du sommaire introuvable")
            erreurs += 1
        else:
            s = s.replace(toc_avant, toc_apres, 1)
    else:
        print("  [OK] sommaire deja a jour")

    # 3. section nouvelle
    s, e = inserer_balise(
        s,
        '<h2 id="securite">6. Les rapports de sécurité : le suivi que personne ne lit</h2>',
        SECTION_SONDAGE)
    erreurs += e

    # 4. source communautaire
    s, e = inserer_balise(s, '<h3>Non confirmé</h3>\n          <ul class="src-list">', SOURCE_VIDEO)
    erreurs += e

    # 5. mention non confirme
    s, e = inserer_balise(s, '<h3>Non confirmé</h3>\n          <ul class="src-list">', MENTION_NON_CONFIRME)
    erreurs += e

    # 6. chronologie
    s, e = inserer_balise(s, '<figure class="page-figure">\n            <img width="1536" height="1024" src="../img/communaute/market-tracking.jpg"',
                          CHRONO_SONDAGE)
    erreurs += e

    if erreurs:
        print("  [KO] %d anomalie(s) sur communaute-patch-notes.html" % erreurs)
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] communaute-patch-notes.html : section 5, chronologie, sources")
    return 0


# ==========================================================================
# 2. saison8-attente.html
# ==========================================================================

ENCART_S8 = """<!--VEILLE-H:S8-SIGNAL:OPEN-->
          <div class="callout callout-info">
            <h3 class="h4">Un signal de fond : le sondage de mi-saison</h3>
            <p>Le 17 novembre 2026, MoreFun a ouvert un <strong>sondage sur les règles d'entrée</strong> en Lockdown, Forbidden Zone et Warlord Tournament : baisse possible du plafond de munitions en Lockdown (T5 vers T4, exception pour les calibres de sniper) et relèvement possible de la valeur d'équipement minimale en Forbidden Zone et au Warlord. Ce n'est <strong>pas</strong> une annonce de règles : c'est une consultation, sans date et sans application immédiate. Mais un éditeur qui interroge sa communauté sur ses plafonds d'entrée en pleine saison prépare très probablement une révision pour la suite. <span class="src-tag src-officiel">Officiel</span></p>
            <p>Comment en tenir compte : les règles décrites dans ce guide — <strong>T4 en Normal, T5 en Lockdown</strong>, 150 000 à 900 000 de valeur d'équipement en Lockdown, 450 000 en Forbidden Zone — restent celles en vigueur tant qu'une note de patch n'a pas dit le contraire. <a href="communaute-patch-notes.html#sondage" id="lnk-saison8-attente-143">Le détail des cinq questions</a> est repris dans la page des patch notes.</p>
          </div>
<!--VEILLE-H:S8-SIGNAL:CLOSE-->"""

FAQ_S8 = """<!--VEILLE-H:S8-FAQ:OPEN-->
          <h3 class="h4">Les règles d'entrée vont-elles changer&nbsp;?</h3>
          <p>Rien n'est confirmé. Le seul indice disponible est le <strong>sondage de mi-saison du 17 novembre 2026</strong> : MoreFun y demande l'avis de la communauté sur une baisse du plafond de munitions en Lockdown — de T5 vers T4, exception pour les calibres de sniper — et sur une hausse de la valeur d'équipement minimale en Forbidden Zone et au Warlord Tournament. Aucun correctif n'accompagne le questionnaire, aucune date n'est donnée, et l'éditeur n'a rien publié sur ses canaux officiels à ce sujet. Tant que la note de patch n'est pas là, les règles du guide sont les règles du jeu. <span class="src-tag src-communautaire">Communautaire</span></p>
<!--VEILLE-H:S8-FAQ:CLOSE-->"""


def maj_saison8():
    chemin = PAGES / "saison8-attente.html"
    s = chemin.read_text(encoding="utf-8")
    erreurs = 0

    s, e = inserer_balise(s, '<h2 id="compte-a-rebours">6. Le compte à rebours des événements de la S7</h2>', ENCART_S8)
    erreurs += e

    s, e = inserer_balise(s, '<h3 class="h4">Où suivre l\'annonce&nbsp;?</h3>', FAQ_S8)
    erreurs += e

    if erreurs:
        print("  [KO] %d anomalie(s) sur saison8-attente.html" % erreurs)
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] saison8-attente.html : encart signal et question de FAQ")
    return 0


# ==========================================================================
# 3. meta-strategies-s7.html
# ==========================================================================

ENCART_META = """<!--VEILLE-H:META-PLAFOND:OPEN-->
          <div class="callout callout-warning">
            <h3 class="h4">Le plafond de Lockdown pourrait baisser : ce qu'il faut en faire</h3>
            <p>Le 17 novembre 2026, MoreFun a ouvert un sondage de mi-saison sur les règles d'entrée. L'une des questions porte sur la <strong>baisse du plafond de munitions en Lockdown de T5 à T4</strong>, avec une exception pour les munitions de sniper ; l'armure et les casques T5 resteraient autorisés. Ce n'est <strong>pas une règle en vigueur</strong> : rien n'est daté, rien n'est appliqué, et le T5 reste autorisé en Lockdown aujourd'hui. <span class="src-tag src-officiel">Officiel</span></p>
            <p>Pourquoi cela vous concerne même sans attendre la confirmation : le débat porte sur la structure du tier, pas sur un détail. Si le T4 devenait la norme en Lockdown, le <strong>7.62×51</strong> serait la seule munition T5 admise — et donc le FAL, le G28 et le M24 s'imposeraient, le FAL en automatique capable de tenir le T5 à faible cadence. C'est précisément le risque que la communauté signale : la concentration du tier élevé sur un petit nombre d'armes au lieu d'un vrai équilibre. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>La règle de conduite est simple : <strong>n'achetez pas de munitions T5 en gros pour Lockdown</strong>, gardez vos kits modulaires, et traitez le T4 comme la valeur sûre. Le T5 est autorisé aujourd'hui ; il pourrait ne plus l'être au prochain correctif ou à la Saison 8. <a href="communaute-patch-notes.html#sondage" id="lnk-meta-strat-gies-s7-148">Le détail du sondage</a> est dans la page des patch notes.</p>
          </div>
<!--VEILLE-H:META-PLAFOND:CLOSE-->"""


def maj_meta():
    chemin = PAGES / "meta-stratégies-s7.html"
    s = chemin.read_text(encoding="utf-8")
    s, e = inserer_balise(
        s,
        '<h3 class="h4">Le jeu meurt-il ? Non — et les chiffres le disent</h3>',
        ENCART_META)
    if e:
        print("  [KO] anomalie sur meta-strategies-s7.html")
        return e
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] meta-strategies-s7.html : encart sur le plafond Lockdown")
    return 0


# ==========================================================================
# 4. equipement-tier-list.html
# ==========================================================================

ENCART_TIER = """<!--VEILLE-H:TIER-PLAFOND:OPEN-->
          <div class="callout callout-warning">
            <h3 class="h4">Le T5 de Lockdown est en discussion</h3>
            <p>La ligne <strong>Lockdown — T5</strong> de ce tableau est la règle <strong>en vigueur</strong>. Depuis le 17 novembre 2026, MoreFun consulte la communauté sur une baisse du plafond de munitions en Lockdown à T4, exception pour les calibres de sniper, l'armure T5 restant autorisée. Consultation en cours, <strong>aucun changement appliqué</strong> : tant qu'aucune note de patch n'est publiée, ce tableau est valide et un build T5 est toujours légal en Lockdown. <a href="communaute-patch-notes.html#sondage" id="lnk-equipement-tier-list-140">Détail du sondage</a>. <span class="src-tag src-officiel">Officiel</span></p>
          </div>
<!--VEILLE-H:TIER-PLAFOND:CLOSE-->"""


def maj_tier_list():
    chemin = PAGES / "equipement-tier-list.html"
    s = chemin.read_text(encoding="utf-8")
    s, e = inserer_balise(
        s,
        '<div class="callout callout-success"><h3 class="h4">Le mot de la fin</h3>',
        ENCART_TIER)
    if e:
        print("  [KO] anomalie sur equipement-tier-list.html")
        return e
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] equipement-tier-list.html : rappel sur le plafond Lockdown")
    return 0



# ==========================================================================
# 5. cosmetiques-dog-tags.html
# ==========================================================================

ENCART_REGLEMENT = """<!--VEILLE-H:DOGTAG-REGLEMENT:OPEN-->
          <div class="callout callout-info">
            <h3 class="h4">Les plaques doivent être réglées avant d'être dépensées</h3>
            <p>Une plaque ramassée pendant le match n'est pas immédiatement dépensable. Selon la documentation communautaire du mode, seules les plaques <strong>réglées</strong> — validées à la fin du match — peuvent être échangées au gachapon : les plaques <strong>en attente</strong> ne sont pas comptées dans le solde dépensable, et l'écran d'échange peut afficher un avertissement de solde insuffisant alors que le compteur global paraît suffisant. <span class="src-tag src-communautaire">Communautaire</span></p>
            <p>La conséquence pratique tient en une phrase : <strong>attendez la fin du match</strong> avant d'ouvrir le gachapon, et vérifiez le solde réglé — pas le total affiché — avant de lancer un tirage. Ce que devient une plaque portée quand le match s'arrête mal (mort, déconnexion, abandon) n'est pas documenté de façon fiable : les sources disponibles ne tranchent pas entre perte, conservation et mise en attente. <span class="src-tag src-communautaire">Communautaire</span> <a href="https://gamers.wiki/en/games/arena-breakout-infinite/guides/arena-breakout-infinite-supplies-drops-dog-tag-guide" target="_blank" rel="noopener" id="lnk-cosmetiques-dog-tags-141">gamers.wiki<span class="sr-only"> (nouvel onglet)</span></a></p>
          </div>
<!--VEILLE-H:DOGTAG-REGLEMENT:CLOSE-->"""

CHECKLIST_REGLEMENT = """<!--VEILLE-H:DOGTAG-CHECK:OPEN-->
            <li>En Supplies Drops, attendez la <strong>régularisation</strong> de fin de match avant d'ouvrir le gachapon : une plaque encore en attente n'est pas dépensable.</li>
<!--VEILLE-H:DOGTAG-CHECK:CLOSE-->"""


def maj_dog_tags():
    chemin = PAGES / "cosmetiques-dog-tags.html"
    s = chemin.read_text(encoding="utf-8")
    s, e = inserer_balise(s, '<h2 id="strategie">7. Stratégie : ramasser ou vendre ?</h2>', ENCART_REGLEMENT)
    erreurs = e
    s, e = inserer_balise(s, '<li>Vendez au contact avant le reset de saison si vous n\'êtes pas collectionneur.</li>', CHECKLIST_REGLEMENT)
    erreurs += e
    if erreurs:
        print("  [KO] %d anomalie(s) sur cosmetiques-dog-tags.html" % erreurs)
        return erreurs
    chemin.write_text(s, encoding="utf-8")
    print("  [OK] cosmetiques-dog-tags.html : reglement des plaques")
    return 0


def main():
    ecarts = (maj_patch_notes() + maj_saison8() + maj_meta() + maj_tier_list()
              + maj_dog_tags())
    if ecarts:
        print("\n  %d anomalie(s)" % ecarts)
        return 1
    print("\n  vague H appliquee")
    return 0


if __name__ == "__main__":
    sys.exit(main())
