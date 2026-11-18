#!/usr/bin/env python3
"""Reecrit la section "assurance" de guide-extraction avec les regles verifiees du wiki officiel."""
import pathlib, re

P = pathlib.Path('pages/guide-extraction.html')
s = P.read_text(encoding='utf-8')

start = s.find('          <h2 id="assurance">')
if start < 0:
    raise SystemExit('section assurance introuvable')
end = s.find('          <h2 id="erreurs">', start)
if end < 0:
    raise SystemExit('section erreurs introuvable')

NEW = '''          <h2 id="assurance">Ce que vous perdez vraiment quand vous mourez</h2>
          <p>C'est la question que tout le monde pose et que presque personne ne pose correctement. La
          réponse courte : <strong>il n'y a pas d'assurance dans ABI Infinite</strong>. Ce que vous perdez
          est perdu — sauf ce qui est placé dans un emplacement protégé, ou ce qu'un coéquipier vous
          rapporte. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Ce qui survit à une mort</caption>
              <thead><tr><th scope="col">Emplacement</th><th scope="col">Ce qui survit</th><th scope="col">Condition</th></tr></thead>
              <tbody>
                <tr><td><strong>Emplacement clé</strong></td><td>Vos cartes d'accès</td><td>Toujours protégé, même si vous mourez</td></tr>
                <tr><td><strong>Secure Pouch</strong> (1 case)</td><td>1 objet</td><td>Seulement dans les modes qui le proposent</td></tr>
                <tr><td><strong>Secure Case</strong> (grille payante)</td><td>6 à 9 cases</td><td>Contenu de la grille uniquement</td></tr>
                <tr><td><strong>Corps de l'adversaire</strong></td><td>Tout son kit</td><td>Accessible uniquement si vous survivez assez longtemps</td></tr>
                <tr><td><strong>Recours des coéquipiers</strong></td><td>Votre stuff, renvoyé par mail</td><td>Un coéquipier doit survivre et sortir</td></tr>
                <tr><td><strong>Rig et sac</strong></td><td><em>Rien</em></td><td>Tout ce qui n'est pas protégé est perdu définitivement</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-danger">
            <h3 class="h4">L'erreur qui coûte le plus cher</h3>
            <p>Beaucoup de guides — y compris d'anciennes versions de celui-ci — parlent d'une « assurance »
            qui rendrait l'équipement couvert. <strong>Cette mécanique n'existe pas dans le jeu actuel</strong> :
            le wiki officiel est explicite, « insurance does not exist, what you lose is gone unless recovered
            manually ». Tout ce que vous mettiez en dehors d'un emplacement protégé est perdu sans
            contrepartie. <span class="src-tag src-officiel">Officiel</span></p>
          </div>

          <h3 class="h4">La Secure Case : ce que les Bonds achètent vraiment</h3>
          <p>La Secure Case est le seul « achat de survie » du jeu. C'est un petit conteneur à grille que
          vous louez en Bonds, et qui conserve son contenu même si vous mourez. Ce que vous n'y mettez pas
          ne vous protège pas. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Secure Cases disponibles</caption>
              <thead><tr><th scope="col">Format</th><th scope="col">Cases</th><th scope="col">Coût</th><th scope="col">À retenir</th></tr></thead>
              <tbody>
                <tr><td>2×3</td><td>6</td><td>400 Bonds</td><td>Le format d'entrée, suffisant pour un lot de documents et d'injecteurs</td></tr>
                <tr><td>3×2 (Composite Case)</td><td>6</td><td>1 000 Bonds / 30 jours</td><td>Abonnement à renouveler : l'abonnement expire même si vous ne mourez jamais</td></tr>
                <tr><td>3×3</td><td>9</td><td>800 Bonds</td><td>Persiste au wipe, mais ne vaut que si vous le remplissez</td></tr>
              </tbody>
            </table>
          </div>
          <ul>
            <li><strong>La Case elle-même ne se perd pas</strong> à la mort — seule la subscription expire, au
              bout de sa durée.</li>
            <li><strong>Règle de la Saison 6</strong> : les munitions rouges ne peuvent pas être placées dans
              une Secure Case.</li>
            <li><strong>Depuis la Saison 5</strong>, une carte d'essai 3×3 gratuite est distribuée en
              récompense de fin de saison — vérifiez votre boîte aux lettres.</li>
            <li><strong>Ce qui mérite la Case</strong> : documents, objets de quête, injecteurs, clés si vous
              n'avez pas le Key Chain, et le loot compact à forte valeur. Ce qui ne la mérite pas : les
              munitions en vrac et l'armure que vous porterez de toute façon.</li>
            <li><strong>Le seuil de rentabilité</strong> est arithmétique, pas émotionnel : six cases bien
              pleines battent neuf cases vides. Comptez vos morts réels sur dix raids avant d'acheter.</li>
          </ul>

          <h3 class="h4">La récupération par les coéquipiers : le vrai filet de sécurité</h3>
          <p>Le wiki le formule sans ambiguïté : <em>« Teammates can retrieve and return your gear if they
          survive, which will be sent back to you via in-game mail. »</em> Autrement dit, si un coéquipier
          sort vivant avec votre stuff, il vous le renvoie par la messagerie du jeu. C'est gratuit, et c'est
          souvent plus rentable qu'une Case. <span class="src-tag src-officiel">Officiel</span></p>
          <p>Une nuance importante : les objets marqués d'un <strong>symbole orange</strong> appartiennent à
          vos coéquipiers — si vous extrayez avec eux, vous ne pouvez pas les garder. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="callout callout-success">
            <h3 class="h4">Le protocole d'équipe en quatre lignes</h3>
            <p>1. Emplacement clé : vos cartes, toujours. 2. Secure Pouch : votre objet le plus cher.
            3. Coéquipier vivant = stuff renvoyé par mail. 4. Rig et sac : ce que vous acceptez de perdre
            aujourd'hui pour ne pas avoir à choisir en pleine mort.</p>
          </div>

          <h3 class="h4">Le programme de compensation des tricheurs</h3>
          <p>Il existe une seule forme de « remboursement » dans le jeu, et elle est targeting les
          tricheurs : le <strong>programme de compensation de G.T.I. Security</strong>. Si vous êtes tué par
          un joueur qui reçoit ensuite un bannissement définitif, vous récupérez <strong>l'intégralité</strong>
          de l'équipement porté au moment de la mort — armes primaires et secondaires avec leurs
          attachements, casque, casque audio, gilet et protection, sac et chest rig. Le tout est renvoyé par
          la messagerie du jeu, généralement sous un à trois jours ouvrés. <span class="src-tag src-communautaire">Communautaire</span></p>
          <ul>
            <li><strong>Vous n'avez rien à faire.</strong> Le système vous identifie automatiquement comme
              victime ; un signalement n'est pas nécessaire, il est simplement encouragé.</li>
            <li><strong>Cela fonctionne même si un autre joueur a déjà pillé votre corps</strong>, et même si
              votre coéquipier a récupéré votre stuff.</li>
            <li><strong>Les objets de votre Secure Case ne sont pas concernés</strong> — ils ne sont pas
              perdus, ils sont conservés.</li>
          </ul>
          <div class="callout callout-warning">
            <h3 class="h4">Ce que ce programme ne change pas</h3>
            <p>Il ne rend pas le jeu moins risqué : il rend le jeu <strong>plus juste</strong>. La différence
            entre « j'ai perdu 300 000 K à un tricheur » et « j'ai perdu 300 000 K à un bon joueur » est
            importante, mais elle ne réduit ni le prix de votre kit ni le nombre de morts que vous prenez.</p>
          </div>

'''

s = s[:start] + NEW + s[end:]
P.write_text(s, encoding='utf-8')
print('section assurance reecrite (%d caracteres)' % len(NEW))
