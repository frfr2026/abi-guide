#!/usr/bin/env python3
"""Script historique d'insertion des cles Northridge et Airport.

ATTENTION : ce script est NEUTRALISE. Son contenu datait de sources
secondaires (qrts.ru, arenabreakout-infinite.com, topuplive) et inserait
les sections sans aucune garde : une seconde execution dupliquait les
sections et le decompte des cles devenait faux.

Il est remplace par tools/fix_cles.py, qui :
  - est idempotent (garde en entree) ;
  - attribue chaque cle au wiki officiel ou a une base communautaire ;
  - complete le contenu officiel des cles documentees ;
  - corrige le decompte Northridge (19 cles, dont 9 officielles).

Pour regenerer l'etat actuel de pages/items-cles.html, relancer :
    python3 tools/fix_cles.py

Ne pas relancer tools/refresh_cles.py : il reproduirait le bug de doublon.
"""
import pathlib
import sys

MSG = """
================================================================
tools/refresh_cles.py est neutralise.

Use instead :
    python3 tools/fix_cles.py

Reason : this script inserted sections without an idempotence guard, so a
second run duplicated the Northridge and Airport blocks and broke the key
counts. The replacement attributes each key to the official wiki or to a
community source, and is safe to re-run.
================================================================
"""

if '--help' in sys.argv or '-h' in sys.argv:
    print(MSG)
    raise SystemExit(0)

print(MSG)
raise SystemExit(1)
