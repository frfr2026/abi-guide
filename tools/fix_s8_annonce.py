#!/usr/bin/env python3
"""Corrige et complete la section "Comment l'annonce est-elle faite" de la page S8.

Deux corrections factuelles et un ajout, d'apres la revue des publications de
MoreFun reprise par SenseOS (seasons-list, update-schedule) :

  1. Le tableau des delais utilisait le post "Coming Early Jan." du 10 decembre
     2025 pour la Saison 4 et datait la Saison 5 au 20 mars. Or le *premier post
     date* de la Saison 4 est du 29 decembre 2025 (10 jours), le 10 decembre
     n'etait qu'un drapeau "early January" sans jour precis ; et le premier post
     date de la Saison 5 est du 19 mars 2026 (14 jours).
  2. La plage reelle va de 6 a 27 jours (Ignition : 2 avril puis 29 avril 2025,
     27 jours), et non 7 a 13.
  3. Ajout du rythme de mise a jour lui-meme : ABI met a jour environ tous les
     quinze jours, le plus souvent a 03:00 UTC, et ces mises a jour ordinaires ne
     coupent pas les serveurs. Surtout : les notes de patch sont desormais
     publiees sur le site de l'editeur, et non plus sur Steam.

Idempotent.
"""
import pathlib, re

P = pathlib.Path('pages/saison8-attente.html')
s = P.read_text(encoding='utf-8')

# Garde d'idempotence : si le tableau corrige est deja en place, on sort.
if 'Ignition (Saison 1)' in s and 'quinze jours' in s and 'premier post <em>dat' in s:
    print('deja corrige')
    raise SystemExit(0)

OLD_TABLE = '''                <tr><td>Saison 4</td><td>10 d\u00e9cembre 2025 (\u00ab Coming Early Jan. \u00bb)</td><td>8 janvier 2026</td><td>29 jours</td></tr>
                <tr><td>Saison 5</td><td>20 mars 2026</td><td>2 avril 2026</td><td>13 jours</td></tr>
                <tr><td>Saison 6</td><td>23 juin 2026</td><td>30 juin 2026</td><td>7 jours</td></tr>
                <tr><td>Saison 7</td><td>8 septembre 2026</td><td>16 septembre 2026</td><td>8 jours</td></tr>'''

NEW_TABLE = '''                <tr><td>Ignition (Saison 1)</td><td>2 avril 2025</td><td>29 avril 2025</td><td>27 jours</td></tr>
                <tr><td>Saison 2</td><td>26 juin 2025</td><td>10 juillet 2025</td><td>14 jours</td></tr>
                <tr><td>Saison 3</td><td>2 septembre 2025</td><td>15 septembre 2025</td><td>13 jours</td></tr>
                <tr><td>Saison 4</td><td>29 d\u00e9cembre 2025</td><td>8 janvier 2026</td><td>10 jours</td></tr>
                <tr><td>Saison 5</td><td>19 mars 2026</td><td>2 avril 2026</td><td>14 jours</td></tr>
                <tr><td>Saison 6</td><td>23 juin 2026</td><td>30 juin 2026</td><td>7 jours</td></tr>
                <tr><td>Saison 7</td><td>8 septembre 2026</td><td>16 septembre 2026</td><td>8 jours</td></tr>'''

assert OLD_TABLE in s, 'tableau des delais introuvable'
s = s.replace(OLD_TABLE, NEW_TABLE, 1)

OLD_CAP = '<caption>Le d\u00e9lai entre le premier signal officiel et le lancement</caption>'
NEW_CAP = '<caption>Le d\u00e9lai entre le premier post <em>dat\u00e9</em> et le lancement</caption>'
assert OLD_CAP in s
s = s.replace(OLD_CAP, NEW_CAP, 1)

OLD_P = '''          <p>Concr\u00e8tement : \u00e0 partir de la mi-novembre, le premier post \u00ab reveal \u00bb est attendu, et le
          lancement suit g\u00e9n\u00e9ralement <strong>une \u00e0 deux semaines</strong> plus tard. C'est le moment de
          surveiller l'onglet <strong>Actualit\u00e9s</strong> du jeu et les annonces Steam de l'app 2073620.
          <span class="src-tag src-officiel">Officiel</span></p>'''

NEW_P = '''          <p>Concr\u00e8tement : \u00e0 partir de la mi-novembre, le premier post \u00ab reveal \u00bb est attendu, et le
          lancement suit g\u00e9n\u00e9ralement <strong>une \u00e0 deux semaines</strong> plus tard \u2014 mais la plage
          historique va de <strong>6 \u00e0 27 jours</strong>, et les deux derni\u00e8res saisons n'ont annonc\u00e9
          que <strong>7 et 8 jours</strong> \u00e0 l'avance. Plus le pr\u00e9avis est court, moins vous avez de temps
          pour pr\u00e9parer votre kit de fin de saison.</p>
          <p>Un pr\u00e9cision de vocabulaire : le 10 d\u00e9cembre 2025, MoreFun avait publi\u00e9 un \u00ab Coming Early Jan. \u00bb
          pour la Saison 4 <em>sans donner de jour</em>. Ce n'\u00e9tait pas le premier post dat\u00e9 \u2014 celui-l\u00e0 est
          du 29 d\u00e9cembre, dix jours avant le lancement. Un drapeau sans date ne compte pas dans le compte
          \u00e0 rebours : c'est le post qui donne la date qui compte.
          <span class="src-tag src-officiel">Officiel</span></p>

          <h3 class="h4">L\u2019endroit exact o\u00f9 guetter \u2014 et \u00e0 quelle heure</h3>
          <p>Deux erreurs de surveillance costent cher, et les deux sont fr\u00e9quentes.</p>
          <ul>
            <li><strong>Les notes de patch sont d\u00e9sormais sur le site de l\u2019\u00e9diteur, plus sur Steam.</strong> Steam reste le canal des grandes annonces de saison, mais les notes de mise \u00e0 jour ordinaires sont publi\u00e9es sur le site officiel de MoreFun. Ne regardez pas Steam en exclusivit\u00e9.</li>
            <li><strong>Le rythme estEnviron tous les quinze jours, le plus souvent \u00e0 03:00 UTC.</strong> Sur les seize mises \u00e0 jour en direct depuis avril 2026, quatorze affichent une heure et dix de celles-ci sont \u00e0 03:00 UTC ; les autres \u00e0 05:00, 07:00 ou 12:00. Une reprise \u00e0 03:00 UTC un mardi ou un jeudi est donc le rendez-vous \u00e0 mettre dans votre agenda.</li>
            <li><strong>Et surtout, distinguez mise \u00e0 jour et bascule de saison.</strong> Une mise \u00e0 jour ordinaire ne coupe g\u00e9n\u00e9ralement pas les serveurs : le jeu red\u00e9marre et se patche. Une bascule de saison, elle, ferme les serveurs <strong>six \u00e0 douze heures</strong>. Si votre jeu est indisponible au milieu de la journ\u00e9e et qu\u2019une note d\u00e9taill\u00e9e accompagne le red\u00e9marrage, c\u2019est qu\u2019une saison se pr\u00e9pare.</li>
          </ul>
          <p class="small text-muted">Source : revue des publications de MoreFun (56 notes de mise \u00e0 jour, du 10 mai 2024 au 26 octobre 2026) et calendrier des saisons.</p>'''

assert OLD_P in s, 'paragraphe de conclusion introuvable'
s = s.replace(OLD_P, NEW_P, 1)

P.write_text(s, encoding='utf-8')
print('pages/saison8-attente.html : delais corriges + section surveillance ajoutee')
