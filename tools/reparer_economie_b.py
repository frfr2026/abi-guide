#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - reparation definitive de pages/guide-economie.html.

Degat : la purge regex de la vague E (motif non glouton) s'est arretee au
premier </div>, celui du <div class="table-wrap"> du bloc SEUIL. Le debut du
bloc a donc ete supprime et son corps est reste orphelin dans la page, puis
duplique a chaque relance.

Ce script :
  1. repere le bloc canonique "La regle du seuil" (celui qui commence par un
     <div class="callout callout-warning"> suivi du <h3>) ;
  2. supprime tous les fragments orphelins du meme contenu qui trainaient
     ailleurs dans la page ;
  3. verifie l'equilibre des balises div.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/guide-economie.html")

TITRE = "La règle du seuil : votre kit doit être plus petit que votre loot espéré"
SIGNE_ORPHELIN = "Concrètement&nbsp;: si vous estimez"


def blocs_orphelins(s):
    """Renvoie les (debut, fin) des fragments de corps SEUIL hors de son bloc.

    Un fragment orphelin est une suite de paragraphes du bloc SEUIL qui n'est
    pas precedee de la balise ouvrante du callout.
    """
    fragments = []
    for m in re.finditer(re.escape(SIGNE_ORPHELIN), s):
        pos = m.start()
        # remonter au debut du fragment : le <p> qui le precede
        d = s.rfind("<p>", 0, pos)
        if d == -1:
            continue
        # trouver la fin : le </p> du paragraphe source, puis le </div> orphelin
        fin_p = s.find("</p>", pos)
        if fin_p == -1:
            continue
        fin_p += len("</p>")
        # un </div> orphelin suit eventuellement
        suite = s[fin_p:fin_p + 40]
        if suite.lstrip().startswith("</div>"):
            fin = fin_p + suite.index("</div>") + len("</div>")
        else:
            fin = fin_p
        fragments.append((d, fin))
    return fragments


def main():
    s = PAGE.read_text(encoding="utf-8")

    # 1. le bloc canonique commence par l'ouverture du callout juste avant le titre
    idx_titre = s.find(TITRE)
    if idx_titre == -1:
        print("  [!!] bloc SEUIL introuvable")
        return 1
    d_bloc = s.rfind('<div class="callout callout-warning">', 0, idx_titre)
    if d_bloc == -1:
        print("  [!!] ouverture du bloc SEUIL introuvable")
        return 1

    # 2. tous les fragments qui ne sont pas dans [d_bloc, fin_bloc]
    #    on supprime d'abord les fragments situes AVANT le bloc canonique
    fragments = blocs_orphelins(s)
    supprimes = 0
    for debut, fin in reversed(fragments):
        if d_bloc <= debut:
            continue  # fragment deja dans le bloc canonique
        # verifier que le fragment n'est pas immediatement dans le bloc canonique
        s = s[:debut] + s[fin:]
        supprimes += 1
    if supprimes:
        print("  %d fragment(s) orphelin(s) supprime(s)" % supprimes)

    # 3. verifier l'equilibre div
    ouv = len(re.findall(r"<div\b", s))
    fer = len(re.findall(r"</div>", s))
    if ouv != fer:
        print("  [!!] balises div desequilibrees : %d ouvertes / %d fermees" % (ouv, fer))
        return 1
    print("  balises div equilibrees : %d" % ouv)

    # 4. verifier la presence des elements attendus
    for cle in (TITRE, "Le piège du loot brut", "sortir vivant.</p>"):
        if s.count(cle) != 1:
            print("  [!!] occurrence inattendue pour %r : %d" % (cle[:40], s.count(cle)))
            return 1
    print("  unicite verifiee : bloc SEUIL, piege du loot brut, paragraphe final")

    PAGE.write_text(s, encoding="utf-8")
    print("  page ecrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
