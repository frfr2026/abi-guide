#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - reparation finale de pages/guide-economie.html.

Apres la suppression des fragments orphelins, deux fermetures </div> sans
ouverture subsistent : elles fermaient les blocs SEUIL supprimes. Ce script
supprime toute la zone comprise entre la fin de la section Field Merchants et
le debut du bloc SEUIL canonique, puis verifie l'equilibre des div.

Idempotent.
"""
import pathlib
import re
import sys

PAGE = pathlib.Path("pages/guide-economie.html")
TITRE = "La règle du seuil : votre kit doit être plus petit que votre loot espéré"
SIGNE = "Concrètement&nbsp;: si vous estimez"


def main():
    s = PAGE.read_text(encoding="utf-8")

    idx_titre = s.find(TITRE)
    if idx_titre == -1:
        print("  [!!] bloc SEUIL introuvable")
        return 1
    d_bloc = s.rfind('<div class="callout callout-warning">', 0, idx_titre)
    if d_bloc == -1:
        print("  [!!] ouverture du bloc SEUIL introuvable")
        return 1

    # premier fragment orphelin avant le bloc canonique
    premier = None
    for m in re.finditer(re.escape(SIGNE), s):
        if m.start() < d_bloc:
            premier = m.start()
            break
    if premier is None:
        print("  aucun fragment orphelin : rien a faire")
        return 0

    # remonter a la fin de la liste HTML qui precede
    fin_liste = s.rfind("</ul>\n", 0, premier)
    if fin_liste == -1:
        print("  [!!] fin de liste introuvable")
        return 1
    fin_liste += len("</ul>\n")

    zone = s[fin_liste:d_bloc]
    print("  zone a nettoyer : %d caracteres" % len(zone))
    if zone.count("<div") != zone.count("</div>"):
        print("  (zone desequilibree : %d <div / %d </div)"
              % (zone.count("<div"), zone.count("</div>")))

    s = s[:fin_liste] + "\n" + s[d_bloc:]

    ouv = len(re.findall(r"<div\b", s))
    fer = len(re.findall(r"</div>", s))
    print("  balises div : %d ouvertes / %d fermees" % (ouv, fer))
    if ouv != fer:
        print("  [!!] toujours desequilibre")
        return 1

    for cle in (TITRE, "Le piège du loot brut", "sortir vivant.</p>", SIGNE):
        n = s.count(cle)
        print("  %-52s %d" % (cle[:50], n))
        if n != 1:
            print("  [!!] occurrence inattendue")
            return 1

    PAGE.write_text(s, encoding="utf-8")
    print("  page ecrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
