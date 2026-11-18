#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - corrections de coherence site.

Trois problemes traites en une passe, de facon idempotente :

  1. module de recherche : toute page doit charger js/search.js, sinon la
     barre de recherche (raccourci / ou Ctrl+K) est muette ;
  2. page 404 : un bloc skip-link + progress-bar etait duplique avant la
     balise <body>, ce qui produisait deux liens d'identifiant identique
     (lnk-404-001) et un contenu hors body ;
  3. build_s16_files.py : sa generation du 404 recombinait deux fois le
     skip-link et le progress-bar, ce qui reproduisait le defaut.

Idempotent : relancer le script sur un site deja corrige ne change rien.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted((ROOT / "pages").glob("*.html")) + [ROOT / "index.html", ROOT / "404.html"]

SCRIPT_PAGE = '  <script src="../js/search.js" defer></script>\n'
SCRIPT_RACINE = '  <script src="js/search.js" defer></script>\n'


def corriger_scripts(fichier):
    s = fichier.read_text(encoding="utf-8")
    avant = s
    if "js/search.js" in s:
        return False

    prefixe = "js/" if fichier.parent == ROOT else "../js/"
    balise = SCRIPT_RACINE if prefixe == "js/" else SCRIPT_PAGE
    anc = '  <script src="%smain.js" defer></script>\n' % prefixe
    if anc not in s:
        print("  [!!] ancre main.js introuvable dans %s" % fichier.name)
        return None
    s = s.replace(anc, anc + balise, 1)
    fichier.write_text(s, encoding="utf-8")
    return s != avant


def corriger_404():
    f = ROOT / "404.html"
    s = f.read_text(encoding="utf-8")
    avant = s

    # retire le bloc orphelin situe entre </head> et <body>
    i = s.index("</head>")
    j = s.index("<body")
    entre = s[i + len("</head>"):j]
    if entre.strip():
        s = s[:i + len("</head>")] + "\n" + s[j:]
        print("  404 : bloc hors body supprime")

    # garantit un seul bloc skip-link + progress-bar dans le body
    bloc = re.search(
        r'(  <a class="skip-link" href="#contenu"[^>]*>Aller au contenu</a>\n'
        r'  <div class="progress-bar" aria-hidden="true"></div>\n)+', s)
    if bloc and bloc.group(0).count("skip-link") > 1:
        unique = ('  <a class="skip-link" href="#contenu">Aller au contenu</a>\n'
                  '  <div class="progress-bar" aria-hidden="true"></div>\n')
        s = s[:bloc.start()] + unique + s[bloc.end():]
        print("  404 : bloc skip-link dedoublonne")

    if s != avant:
        f.write_text(s, encoding="utf-8")
        return True
    return False


def corriger_generateur():
    f = ROOT / "tools" / "build_s16_files.py"
    s = f.read_text(encoding="utf-8")
    avant = s

    # le skip-link et le progress-bar ne doivent pas etre ajoutes deux fois :
    # site_header reprend deja la sequence d'ouverture du body de index.html
    vieux = """    out = (header + '<body>\\n'
           + '  <a class="skip-link" href="#contenu">Aller au contenu</a>\\n'
           + '  <div class="progress-bar" aria-hidden="true"></div>\\n\\n'
           + site_header + '\\n\\n'"""
    neuf = """    # site_header contient deja la sequence d'ouverture du body (skip-link,
    # progress-bar puis <body>) reprise de index.html : on ne la duplique pas.
    out = (header + site_header + '\\n\\n'"""
    if vieux in s:
        s = s.replace(vieux, neuf)
        print("  build_s16_files.py : duplication skip-link corrigee")
    if s != avant:
        f.write_text(s, encoding="utf-8")
        return True
    return False


def main():
    modifies = 0
    for f in PAGES:
        r = corriger_scripts(f)
        if r is None:
            return 1
        if r:
            modifies += 1
            print("  %s : js/search.js ajoute" % f.name)
    print("  %d page(s) corrigee(s) pour le module de recherche" % modifies)

    if corriger_404():
        print("  404.html corrige")
    if corriger_generateur():
        print("  build_s16_files.py corrige")
    return 0


if __name__ == "__main__":
    sys.exit(main())
