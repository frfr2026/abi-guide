#!/usr/bin/env python3
"""Garde-fou de caracteres etrangers pour l'ensemble du projet.

Trois controles, avec des cibles distinctes :

  1. CJK / U+FFFD sur TOUS les fichiers (HTML, JS, CSS, JSON, Python, MD).
     Seules exceptions : les fichiers de detection eux-memes (audit_seo.py,
     qa_final.py), qui contiennent volontairement la classe CJK pour pouvoir la
     signaler, et ce script, qui en cite des exemples dans sa docstring.

  2. "Mots colles" (minuscule suivi d'un majuscule) sur la PROSE des pages
     HTML et sur les chaines de caracteres Python. En JavaScript et en JSON-LD
     ce controle est inutile : le camelCase des identifiants et des cles
     produit des faux positifs massifs.

  3. Deux signatures non ambigues :
       - un tiret bas au milieu d'un mot ("les_OPERATORs") ;
       - une liste de collages fautifs connus, ajoutees au fil des revisions.

Usage : python3 tools/check_scripts.py
Code de sortie 1 si une anomalie est trouvee.
"""
import pathlib, re, sys

ROOT = pathlib.Path('.')
ALL = sorted(
    list(ROOT.glob('*.html')) + list(ROOT.glob('*.md')) +
    list(ROOT.glob('pages/*.html')) +
    list(ROOT.glob('js/*.js')) + list(ROOT.glob('js/*.json')) +
    list(ROOT.glob('css/*.css')) +
    list(ROOT.glob('tools/*.py')) + list(ROOT.glob('tools/*.js'))
)

# Fichiers qui contiennent la classe CJK par design (detecteurs).
CJK_ALLOW = {'audit_seo.py', 'qa_final.py', 'check_scripts.py'}

# Scripts dont les chaines "avant correction" sont volontairement garblees :
# ce sont les motifs que le script cherche pour les remplacer.
MOT_COLLE_ALLOW = {'fix_espaces.py', 'fix_s8_annonce.py'}

CJK = re.compile(r'[\u3000-\u303f\u4e00-\u9fff\ufffd]')
COLLE = re.compile(r'\b[a-zà-ÿ]{3,}[A-ZÉ][a-zà-ÿ]{2,}\b')
# Signature non ambigue : un mot francais ne contient jamais de tiret bas.
# Seule la forme minuscule + underscore + MAJUSCULE est un bug :
# "les_OPERATORs". Les pseudos ("aminem_ghost", "off_kuka358") et les
# valeurs ("in_regular") sont legitimes et ne declenchent rien.
TIRET_BAS = re.compile(r'\b[a-zà-ÿ]{2,}_[A-Z][A-Za-z0-9à-ÿ]+\b')

# Fautes de collage observees sur le site, ajoutees au fil des revisions.
COLLEES = ['àugaliser', 'àgaliser', 'ànuler', 'éperer', 'àxiter']

# Mots legitimes qui collent deux majuscules (noms propres, sigles, code).
OK = {
    'localStorage', 'sessionStorage', 'macOS', 'MoreFun', 'Koen', 'Kamona',
    'Ultimate', 'Never', 'Dark', 'Light', 'Solo', 'Cloud', 'Flash', 'Boss',
    'Loot', 'Item', 'Items', 'Next', 'Day', 'One', 'Two', 'New', 'Up', 'Push',
    'Fail', 'Win', 'Lose', 'Hold', 'Lock', 'Half', 'High', 'Low', 'Best',
    'Game', 'Plan', 'Hunter', 'Breaker', 'Zombie', 'Warlord', 'Utopia',
    'Crimson', 'Breach', 'Dusk', 'Distortion', 'White', 'Infinite', 'Arena',
    'Breakout', 'Outbreak', 'Mother', 'Winter', 'Summer', 'Spring', 'Autumn',
    'Fall', 'Snow', 'Ice', 'Fire', 'Water', 'Wind', 'Earth', 'Storm', 'Steel',
    'Rust', 'Iron', 'Blood', 'Honey', 'Good', 'Mad', 'Key', 'Analysis',
    'Challenges', 'Vertical', 'Supported', 'Munition', 'Semi', 'Full',
    'Burst', 'Automatic', 'Bolt', 'Action', 'Pump', 'Round', 'Assault',
    'Rifle', 'Micro', 'SMG', 'Pistol', 'Carbine', 'Machine', 'Gun', 'Shotgun',
    'Sniper', 'Marksman', 'Heavy', 'Submachine', 'DMR', 'LMG', 'AK', 'SKS',
    'S12K', 'Vector', 'Mosin', 'Nagant', 'Operator', 'Normal', 'Mutant',
    'Reaper', 'Ambusher', 'Bloater', 'Breacher', 'Phobos', 'Cornered', 'Beast',
}

problems = []
for f in ALL:
    s = f.read_text(encoding='utf-8')

    # ── 1. CJK / U+FFFD partout ──
    if f.name not in CJK_ALLOW:
        for m in CJK.finditer(s):
            a = max(0, m.start() - 45)
            problems.append((f.name, 'CJK/U+FFFD', repr(s[a:m.start() + 45])))

    # ── 2 et 3 : prose des pages HTML ──
    if f.suffix == '.html':
        txt = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', s, flags=re.S | re.I)
        txt = re.sub(r'<[^>]+>', ' ', txt)
        for m in COLLE.finditer(txt):
            if m.group(0) not in OK:
                a = max(0, m.start() - 35)
                problems.append((f.name, 'mot colle', repr(txt[a:m.end() + 35])))
        for m in TIRET_BAS.finditer(txt):
            a = max(0, m.start() - 35)
            problems.append((f.name, 'tiret bas', repr(txt[a:m.end() + 35])))
        for w in COLLEES:
            for m in re.finditer(re.escape(w), txt, re.I):
                a = max(0, m.start() - 35)
                problems.append((f.name, 'collage connu', repr(txt[a:m.end() + 35])))

    # ── 2 : chaines de caracteres Python ──
    elif f.suffix == '.py' and f.name not in CJK_ALLOW and f.name not in MOT_COLLE_ALLOW:
        # Chaine comptee comme de la prose francaise : au moins cinq mots,
        # et aucun caractere de balisage ni de code.
        for m in re.finditer(r"'([^'\n]{16,})'", s):
            lit = m.group(1)
            if any(c in lit for c in '<>{}()[]="\\%'):
                continue
            if len(lit.split()) < 5:
                continue
            for w in COLLE.finditer(lit):
                if w.group(0) not in OK:
                    problems.append((f.name, 'mot colle', repr(lit[:90])))
            for w in COLLEES:
                if w in lit.lower():
                    problems.append((f.name, 'collage connu', repr(lit[:90])))

if problems:
    print('ANOMALIES : %d' % len(problems))
    for name, kind, ctx in problems[:60]:
        print('  %-28s %-14s %s' % (name, kind, ctx))
    if len(problems) > 60:
        print('  ... et %d de plus' % (len(problems) - 60))
    sys.exit(1)

print('Scan complet : 0 anomalie sur %d fichiers' % len(ALL))
