#!/usr/bin/env python3
"""Integrate les dernieres donnees de recherche (historique des saisons, Warlord, assurance)."""
import pathlib, re

ROOT = pathlib.Path('.')

# ── 1. page Saison 8 : historique complet + scenarios ──────────────────────
p = ROOT / 'pages/saison8-attente.html'
s = p.read_text(encoding='utf-8')

OLD_TABLE_START = '            <table class="data-table">\n              <caption>Les cinq saisons'
i = s.find(OLD_TABLE_START)
j = s.find('            </table>', i)
if i > 0 and j > 0:
    NEW = '''            <table class="data-table">
              <caption>Toutes les saisons d'ABI Infinite, d'apres les annonces officielles</caption>
              <thead><tr><th scope="col">Saison</th><th scope="col">Nom</th><th scope="col">Début</th><th scope="col">Fin</th><th scope="col">Durée</th><th scope="col">Préavis</th></tr></thead>
              <tbody>
                <tr><td>S0</td><td>Early Access</td><td>13 août 2024</td><td>20 novembre 2024</td><td>99 jours</td><td>6 jours</td></tr>
                <tr><td>S1</td><td>Season One</td><td>20 novembre 2024</td><td>29 avril 2025</td><td>160 jours</td><td>13 jours</td></tr>
                <tr><td>S2</td><td>Ignition</td><td>29 avril 2025</td><td>10 juillet 2025</td><td>72 jours</td><td>27 jours</td></tr>
                <tr><td>S3</td><td>Crimson Edge</td><td>10 juillet 2025</td><td>15 septembre 2025</td><td>67 jours</td><td>14 jours</td></tr>
                <tr><td>S4</td><td>Breach</td><td>15 septembre 2025</td><td>8 janvier 2026</td><td>115 jours</td><td>13 jours</td></tr>
                <tr><td>S5</td><td>Dusk to Dawn (Airport Hunt)</td><td>8 janvier 2026</td><td>2 avril 2026</td><td>84 jours</td><td>10 jours</td></tr>
                <tr><td>S6</td><td>Distortion</td><td>2 avril 2026</td><td>30 juin 2026</td><td>89 jours</td><td>14 jours</td></tr>
                <tr><td>S7</td><td>White Nights</td><td>30 juin 2026</td><td>16 septembre 2026</td><td>78 jours</td><td>7 jours</td></tr>
                <tr><td><strong>S8</strong></td><td><strong>Utopia</strong></td><td><strong>16 septembre 2026</strong></td><td><em>En cours</em></td><td>78 à 89 j</td><td>8 jours</td></tr>
              </tbody>
            </table>'''
    s = s[:i] + NEW + s[j + len('            </table>'):]
    # le nom de la saison courante passe de S7 a S8 dans le tableau
    s = s.replace('<tr><td><strong>Saison 7</strong></td><td><strong>Utopia</strong></td>',
                  '<tr><td><strong>Saison 8</strong></td><td><strong>Utopia</strong></td>')

# section scenarios : inseree apres le tableau de calendrier
SCEN = '''
          <h2 id="scenarios">3. Les trois scénarios, et leurs chances</h2>
          <p>Le rythme des saisons est assez régulier pour chiffrer les probabilités — et c'est plus utile
          qu'une date unique, parce que cela dit quoi surveiller. <span class="src-tag src-communautaire">Communautaire</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Scénarios de bascule vers la Saison 8</caption>
              <thead><tr><th scope="col">Scénario</th><th scope="col">Fenêtre</th><th scope="col">Pourquoi</th><th scope="col">Probabilité</th></tr></thead>
              <tbody>
                <tr><td><strong>Cas de base</strong></td><td><strong>8 – 14 décembre 2026</strong></td><td>Cadence de 78 à 89 jours, et les événements datés de la S7 courent jusqu'au 7 décembre</td><td>≈ 55 %</td></tr>
                <tr><td>Anticipé</td><td>3 – 7 décembre 2026</td><td>La saison la plus courte récente (78 jours) et des événements écourtés</td><td>≈ 10 %</td></tr>
                <tr><td>Report de fêtes</td><td>Début – mi-janvier 2027</td><td>La S3 a couru sur Noël et la S4 n'a démarré que le 8 janvier</td><td>≈ 35 %</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-warning">
            <h3 class="h4">Pourquoi janvier reste possible</h3>
            <p>Un indice fait pencher la balance : <strong>rien dans les notes actuelles n'est daté au-delà du
            7 décembre</strong>. Si Morefun avait prévu une saison en janvier, on s'attendrait à voir au moins
            un événement courant jusque tard décembre. Un événement de Noël reste donc annonçable — c'est
            exactement ce qui s'est produit à l'époque de la S3.</p>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Le signal à surveiller</h3>
            <p>Le silence du 13 novembre ne veut rien dire. Avec un préavis de <strong>7 à 8 jours</strong>,
            un lancement le 8 décembre ne s'accompagnerait d'une révélation que vers le
            <strong>30 novembre – 7 décembre</strong>. Aucune annonce avant cette date n'est donc anormale.
            Sur Reddit, un joueur résumait la situation le 11 novembre : <em>« No mention of it yet, and it
            should be about 3 weeks out... »</em> — avant de comparer au build-up de la S7, où
            <em>« they had the hype train ROLLIN' »</em>. <span class="src-tag src-communautaire">Communautaire</span></p>
          </div>
'''
if 'id="scenarios"' not in s:
    m = re.search(r'\n(\s*)<h2 id="annonce">', s)
    if m:
        s = s[:m.start()] + '\n' + SCEN + s[m.start() + 1:]
        # renumerote les ancres suivantes
        s = s.replace('3. Comment l\'annonce est faite', '4. Comment l\'annonce est faite')
        s = s.replace('4. Le compte à rebours des événements', '5. Le compte à rebours des événements')
        s = s.replace('5. Ce qui se réinitialise', '6. Ce qui se réinitialise')
        s = s.replace('6. La checklist des dix derniers jours', '7. La checklist des dix derniers jours')
        s = s.replace('7. Ce qui ne changera pas', '8. Ce qui ne changera pas')
        s = s.replace('8. FAQ', '9. FAQ')
        s = s.replace('href="#annonce" id="lnk-saison8-attente-102">3. Comment l\'annonce est faite',
                      'href="#annonce" id="lnk-saison8-attente-102">4. Comment l\'annonce est faite')
        s = s.replace('href="#compte-a-rebours" id="lnk-saison8-attente-103">4. Compte à rebours',
                      'href="#compte-a-rebours" id="lnk-saison8-attente-103">5. Compte à rebours')
        s = s.replace('href="#reset" id="lnk-saison8-attente-104">5. Ce qui se réinitialise',
                      'href="#reset" id="lnk-saison8-attente-104">6. Ce qui se réinitialise')
        s = s.replace('href="#checklist" id="lnk-saison8-attente-105">6. Checklist des 10 derniers jours',
                      'href="#checklist" id="lnk-saison8-attente-105">7. Checklist des 10 derniers jours')
        s = s.replace('href="#ce-qui-ne-change-pas" id="lnk-saison8-attente-106">7. Ce qui ne change pas',
                      'href="#ce-qui-ne-change-pas" id="lnk-saison8-attente-106">8. Ce qui ne change pas')
        s = s.replace('href="#faq" id="lnk-saison8-attente-107">8. FAQ',
                      'href="#faq" id="lnk-saison8-attente-107">9. FAQ')
        # entree de sommaire pour la nouvelle section
        s = s.replace('<a href="#annonce" id="lnk-saison8-attente-102">',
                      '<a href="#scenarios" id="lnk-saison8-attente-108">3. Les trois scénarios</a>\n<a href="#annonce" id="lnk-saison8-attente-102">')
        print('  S8 : historique complet + scenarios')
p.write_text(s, encoding='utf-8')

# ── 2. Warlord Tournament : les trois editions ──────────────────────────────
p = ROOT / 'pages/events-warlord-tournament.html'
s = p.read_text(encoding='utf-8')
if 'id="editions"' not in s:
    ED = '''
          <h2 id="editions">Les trois éditions du Warlord Tournament</h2>
          <p>Le Warlord Tournament n'est pas un one-shot : c'est la compétition récurrente d'ABI, et chaque
          édition a changé le format. <span class="src-tag src-officiel">Officiel</span></p>
          <div class="table-wrap">
            <table class="data-table">
              <caption>Historique des éditions</caption>
              <thead><tr><th scope="col">Édition</th><th scope="col">Période</th><th scope="col">Saison</th><th scope="col">Ce qui a changé</th></tr></thead>
              <tbody>
                <tr><td>Premier</td><td>17 avril – 14 mai 2026</td><td>S5 : Distortion</td><td>Création : TV Station, lobbies de 5 escouades, classement sur la valeur du loot, tous les loadouts visibles</td></tr>
                <tr><td>Deuxième</td><td>13 août 2026 (Kamona Summer Festival)</td><td>S6 : White Nights</td><td>Retour des étoiles du Team Rank et du Personal Eliminations Rank, 3 par raid maximum, écart de rang d'escouade limité</td></tr>
                <tr><td><strong>Troisième</strong></td><td><strong>29 octobre – 7 décembre 2026</strong></td><td><strong>S7 : Utopia</strong></td><td>Multiplicateur du fichier chiffré, intel par dog tags, marque Kill Leader</td></tr>
              </tbody>
            </table>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Ce que l'historique vous apprend</h3>
            <p>Les deux premières éditions ont été <strong>courtes</strong> : quatre semaines pour la première,
            un simple retour ponctuel pour la deuxième. La troisième, en revanche, court pendant
            <strong>dix semaines</strong> et se termine le 7 décembre — c'est le dernier gros événement daté
            de la S7, et le point de bascule le plus probable de la saison.</p>
          </div>
'''
    m = re.search(r'\n(\s*)<h2 id="ranks">', s)
    if m:
        s = s[:m.start()] + '\n' + ED + s[m.start() + 1:]
        s = s.replace('<a href="#ranks"', '<a href="#editions" id="lnk-warlord-editions">Les trois éditions</a>\n<a href="#ranks"', 1)
        p.write_text(s, encoding='utf-8')
        print('  Warlord : historique des 3 editions ajoute')

# ── 3. guide-extraction : le systeme d'assurance ────────────────────────────
p = ROOT / 'pages/guide-extraction.html'
s = p.read_text(encoding='utf-8')
if 'id="assurance"' not in s:
    AS = '''
          <h2 id="assurance">Conserver son équipement quand on meurt</h2>
          <p>Le point le plus mal compris du jeu : quand vous mourez en raid, <strong>vous ne perdez pas
          forcément tout votre équipement</strong>. Le jeu distingue ce qui est perdu de ce qui est couvert —
          et la différence se joue sur quelques paramètres précis. <span class="src-tag src-officiel">Officiel</span></p>
          <ul>
            <li><strong>Le sac ne protège rien.</strong> Ce qui est dans votre sac est perdu si vous mourez.
              Les objets que vous portez sur le corps ou dans vos poches peuvent être couverts par l'assurance.</li>
            <li><strong>La clé de la Secure Case compte.</strong> C'est elle qui détermine ce qui remonte :
              un objet placé dans une case sécurisée survit à la mort, tout ce qui est ailleurs ne remonte pas.</li>
            <li><strong>Les Covered Areas change tout.</strong> Certaines zones du jeu sont « couvertes » :
              si vous y mourez, la perte est réduite. D'autres ne le sont pas — et c'est là que la différence
              entre une mort à 2 000 K et une mort à 200 000 K se joue.</li>
            <li><strong>Le délai d'assurance est court.</strong> Ce qui n'est pas récupéré dans le délai imparti
              est définitivement perdu.</li>
          </ul>
          <div class="callout callout-danger">
            <h3 class="h4">L'erreur qui coûte le plus cher</h3>
            <p>Sortir un objet valuable d'une Secure Case en zone non couverte en pensant que « l'assurance
            couvre tout ». Elle ne couvre que ce qui est <strong>dans</strong> la case, et seulement si l'objet
            est éligible. Le réflexe à prendre : <strong>ce qui vaut plus que votre gilet reste dans la case
            jusqu'au bout</strong>.</p>
          </div>
          <div class="callout callout-success">
            <h3 class="h4">Comment vérifier vos réglages avant un raid coûteux</h3>
            <p>Quatre minutes avant une sortie en Forbidden Zone : Secure Case fermée et verrouillée, objets
            eligibles dedans, munition de la bonne classe, clé de la case sur vous. Le coût d'une erreur de
           _procédure est toujours supérieur à celui d'une erreur de tir.</p>
          </div>
'''
    m = re.search(r'\n(\s*)<h2 id="erreurs">', s)
    if m:
        s = s[:m.start()] + '\n' + AS + s[m.start() + 1:]
        s = s.replace('5. Les erreurs d\'extraction les plus coûteuses', '6. Les erreurs d\'extraction les plus coûteuses')
        s = s.replace('<a href="#erreurs"', '<a href="#assurance" id="lnk-extraction-assurance">Conserver son équipement</a>\n<a href="#erreurs"', 1)
        p.write_text(s, encoding='utf-8')
        print('  guide-extraction : section assurance ajoutee')
