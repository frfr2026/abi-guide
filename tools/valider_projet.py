#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - validation globale du projet.

Lance l'ensemble des controles et affiche un tableau de synthese.
Le code de sortie vaut 1 si un seul controle echoue.

    python3 tools/valider_projet.py           # complet (browser inclus, ~10 min)
    python3 tools/valider_projet.py --quick   # sans les recette navigateur (~1 min)
"""
import pathlib
import re
import subprocess
import sys
import time

RACINE = pathlib.Path(__file__).resolve().parent.parent

CONTROLES = [
    # (libelle, commande, detecteur de succes, rapide)
    ("QA global", [sys.executable, "tools/qa_final.py"], r"AUCUNE erreur bloquante", True),
    ("Audit statique", [sys.executable, "tools/audit.py"], r"AUCUNE erreur", True),
    ("Audit SEO", [sys.executable, "tools/audit_seo.py"], r"AUCUNE erreur", True),
    ("Audit profond", [sys.executable, "tools/audit_deep.py"], r"ERREURS : 0", True),
    ("Structure HTML", [sys.executable, "tools/audit_structure.py"], r"0 erreur\(s\)", True),
    ("Scripts", [sys.executable, "tools/check_scripts.py"], r"0 anomalie", True),
    ("Mots", [sys.executable, "tools/compte_mots.py"], r"Sous 1 300 mots\s*:\s*0", True),
    ("Images (navigateur)", ["node", "tools/audit_images_browser.js"], r"Images non decodees\s*:\s*0", False),
    ("Audio (navigateur)", ["node", "tools/audit_audio_browser.js"], r"Echecs\s*:\s*0", False),
    ("Narration", ["node", "tools/test_narration.js"], r"0 échecs", False),
    ("Recette S15", ["node", "tools/test_s15.js"], r"0 échecs", False),
    ("Recette S16", ["node", "tools/test_s16.js"], r"0 échecs", False),
    ("Recette navigateur S17", ["node", "tools/test_s17_browser.js"], r"0 échecs", False),
    ("Recherche S18", ["node", "tools/test_s18_search.js"], r"0 échecs", False),
    ("Catalogue armes", ["node", "tools/test_catalogue.js"], r"0 KO", False),
]


def detail(sortie, motif):
    """Extrait la ligne qui porte le detail du controle."""
    for ligne in sortie.splitlines():
        if re.search(motif, ligne):
            return re.sub(r"\s+", " ", ligne).strip()
    return sortie.strip().splitlines()[-1][:80] if sortie.strip() else ""


def main():
    quick = "--quick" in sys.argv
    print("=" * 78)
    print(f"ABI NEXUS - VALIDATION GLOBALE{' (mode rapide)' if quick else ''}")
    print("=" * 78)

    resultats = []
    for libelle, cmd, motif, rapide in CONTROLES:
        if quick and not rapide:
            resultats.append((libelle, "SKIP", "mode rapide"))
            continue
        debut = time.time()
        try:
            p = subprocess.run(cmd, cwd=RACINE, capture_output=True, text=True, timeout=2400)
            sortie = p.stdout + p.stderr
            ok = re.search(motif, sortie) is not None
            detail_l = detail(sortie, motif)
            duree = time.time() - debut
            resultats.append((libelle, "OK" if ok else "ECHEC", f"{detail_l}  [{duree:.1f}s]"))
        except subprocess.TimeoutExpired:
            resultats.append((libelle, "ECHEC", "delai depasse"))
        except Exception as e:  # pragma: no cover
            resultats.append((libelle, "ECHEC", str(e)[:70]))

    print()
    echecs = 0
    for libelle, etat, d in resultats:
        if etat == "ECHEC":
            echecs += 1
        marque = {"OK": "OK   ", "ECHEC": "ECHEC", "SKIP": "SKIP "}[etat]
        print(f"  [{marque}] {libelle:26s} {d}")

    print("=" * 78)
    total = len([r for r in resultats if r[1] != "SKIP"])
    print(f"  {total - echecs}/{total} controles au vert"
          + (f" ({echecs} en echec)" if echecs else ""))
    print("=" * 78)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
