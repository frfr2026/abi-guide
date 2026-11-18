#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - suppression des fragments orphelins de la vague E.

Meme cause que sur guide-economie : la purge regex non gloutonne s'est arretee
au premier </div>, laissant le corps du bloc SEUIL / IA hors de son div, puis
duplique a chaque relance.

Ce script est generique : pour chaque page concernee, il repere le bloc
canonique (celui qui suit l'ouverture du callout portant le titre attendu) et
supprime tous les fragments du meme contenu situes ailleurs dans la page.

Idempotent.
"""
import pathlib
import re
import sys

# (page, titre du bloc, signature d'un paragraphe de son corps)
CAS = [
    (
        "pages/guide-economie.html",
        "La règle du seuil : votre kit doit être plus petit que votre loot espéré",
        "Concrètement&nbsp;: si vous estimez",
    ),
    (
        "pages/saison7-zombie-endless.html",
        "Les gisements d'IA du mode Endless",
        "Deux avertissements qui découlent de cette lecture",
    ),
]


def debut_bloc(s, titre):
    """Retourne (debut, fin) du bloc canonique ou (None, None)."""
    i = s.find(titre)
    if i == -1:
        return None, None
    d = s.rfind('<div class="callout', 0, i)
    if d == -1:
        return None, None
    prof = 0
    for m in re.finditer(r"<div\b|</div>", s[d:]):
        if m.group(0) == "</div>":
            prof -= 1
            if prof == 0:
                return d, d + m.end()
        else:
            prof += 1
    return None, None


def fragments_orphelins(s, signature):
    """Positions des fragments de corps situés hors du bloc canonique."""
    out = []
    for m in re.finditer(re.escape(signature), s):
        p = s.rfind("<p", 0, m.start())
        if p == -1:
            continue
        fin_p = s.find("</p>", m.start())
        if fin_p == -1:
            continue
        fin_p += len("</p>")
        suite = s[fin_p:fin_p + 40]
        fin = fin_p
        if suite.lstrip().startswith("</div>"):
            fin = fin_p + suite.index("</div>") + len("</div>")
        out.append((p, fin))
    return out


def traiter(page, titre, signature):
    chemin = pathlib.Path(page)
    s = chemin.read_text(encoding="utf-8")

    d_bloc, f_bloc = debut_bloc(s, titre)
    if d_bloc is None:
        print("  [!!] %s : bloc canonique introuvable" % page)
        return False

    frags = fragments_orphelins(s, signature)
    supprimes = 0
    for debut, fin in reversed(frags):
        if d_bloc <= debut < f_bloc:
            continue  # fragment legitement dans le bloc canonique
        s = s[:debut] + s[fin:]
        supprimes += 1

    if supprimes:
        print("  %s : %d fragment(s) orphelin(s) supprime(s)" % (page, supprimes))

    ouv = len(re.findall(r"<div\b", s))
    fer = len(re.findall(r"</div>", s))
    if ouv != fer:
        # des </div> orphelines subsistent : nettoyer la zone entre la liste
        # precedente et le bloc canonique
        premier = None
        for m in re.finditer(re.escape(signature), s):
            if m.start() < d_bloc:
                premier = m.start()
                break
        if premier is not None:
            fin_liste = s.rfind("</ul>\n", 0, premier)
            if fin_liste != -1:
                fin_liste += len("</ul>\n")
                zone = s[fin_liste:d_bloc]
                if zone.count("</div>") > zone.count("<div"):
                    print("  %s : %d </div> orpheline(s) retirees"
                          % (page, zone.count("</div>") - zone.count("<div")))
                    s = s[:fin_liste] + "\n" + s[d_bloc:]
                    d_bloc, f_bloc = debut_bloc(s, titre)

    ouv = len(re.findall(r"<div\b", s))
    fer = len(re.findall(r"</div>", s))
    if ouv != fer:
        print("  [!!] %s : div equilibrees ? %d / %d" % (page, ouv, fer))
        return False

    n = s.count(signature)
    if n != 1:
        print("  [!!] %s : signature presente %d fois" % (page, n))
        return False

    chemin.write_text(s, encoding="utf-8")
    print("  %s : OK (%d div equilibrees)" % (page, ouv))
    return True


def main():
    for page, titre, signature in CAS:
        if not traiter(page, titre, signature):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
