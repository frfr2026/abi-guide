#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - reparation de pages/guide-economie.html.

La vague E avait un motif de purge regex qui, par non-gloutonnerie, s'arretait
au premier </div> : le callout "Le piege du loot brut" (ajoute par
tools/refresh_pages_courtes.py) a ete ampute de quatre paragraphes qui se
retrouvaient dans le callout "La regle du seuil".

Ce script :
  1. retire les residus du paragraphes de la vague E ;
  2. retablit le callout d'origine, mot pour mot ;
  3. retire le bloc VEILLE-E:SEUIL, dont la purge sera refaite proprement.

Idempotent.
"""
import pathlib
import re

PAGE = pathlib.Path("pages/guide-economie.html")

# --- fragments a nettoyer (residus de la purge defaillante) -----------------
RESIDUS = [
    """            <p>Concrètement&nbsp;: si vous estimez sortir <strong>600 000 K</strong> d'un raid et
            que votre taux d'extraction est de 40 %, votre recette espérée est de 240 000 K.
            Votre kit doit donc coûter nettement moins que ça — munitions et consommables
            compris. Enter 600 000 K de kit pour viser 600 000 K de loot, c'est un raid
            déjà perdu d'avance&nbsp;: il suffit d'un seul raid raté pour l'emporter.</p>
            <p>Une variante encore plus prudente circule sur les Reddit economics&nbsp;: ne jamais
            engager plus de <strong>1 % de votre patrimoine total</strong> dans un raid. Avec
            20 millions de liquidités, cela fait 200 000 K de kit maximum&nbsp;; avec 10 millions,
            100 000 K. Ce plafond est brutal mais il protège&nbsp;: c'est le seul qui rende
            l'économie <em>stable</em> même quand le taux d'extraction s'effondre.</p>
            <p class="small text-muted">Sources&nbsp;: fils Reddit «&nbsp;Koen&nbsp;» et «&nbsp;how are you all
            making your koen efficiently&nbsp;», discussions sur le taux d'extraction et le
            seuil de rentabilité — <strong>Communautaire</strong>. Le plafond officiel de
            900 000 K en Lockdown reste la seule règle <strong>Officielle</strong> applicable.</p>
""",
]

# --- callout d'origine (tools/refresh_pages_courtes.py) ---------------------
ORIGINAL = """          <div class="callout callout-warning">
            <p><strong>Le piège du loot brut.</strong> Comparer deux sources au montant
            total est une erreur de méthode : un raid à 900 000 K de loot qui se termine
            par une mort en pleine rue rapporte zéro, contre une mission de trading à
            100 000 K qui rapporte cent pour cent. Le calcul honnête est toujours
            <em>valeur espérée</em> : loot moyen multiplié par la probabilité de
            sortir vivant.</p>
          </div>
"""

# signature du bloc original, pour detecter sa presence
SIGNE = "Le piège du loot brut"


def retirer_div_equilibre(s, debut):
    i = debut
    prof = 0
    for m in re.finditer(r"<div\b|</div>", s[debut:]):
        if m.group(0) == "</div>":
            prof -= 1
            if prof == 0:
                return s[:debut] + s[debut + m.end():]
        else:
            prof += 1
    return s


def main():
    s = PAGE.read_text(encoding="utf-8")

    # 1. retirer les residus
    for r in RESIDUS:
        if r in s:
            s = s.replace(r, "")
            print("  residu retire")

    # 2. retablir le callout d'origine s'il a disparu ou est abime
    if SIGNE not in s:
        anc = "          <div class=\"callout callout-warning\">\n            <p><strong>Le piège du loot brut.</strong>"
        # on cherche l'emplacement : juste avant la fermeture du tableau de rendement
        m = re.search(r"( *</tbody>\n *</table>\n *</div>\n)", s)
        if m:
            s = s[:m.end()] + ORIGINAL + s[m.end():]
            print("  callout 'piege du loot brut' retabli")
        else:
            print("  [!!] ancre de retablissement introuvable")
            return 1
    else:
        # present mais amputé : on verifie la presence du dernier paragraphe
        if "sortir vivant.</p>" not in s:
            h = s.find(SIGNE)
            d = s.rfind('<div class="callout', 0, h)
            if d != -1:
                s = retirer_div_equilibre(s, d)
                m = re.search(r"( *</tbody>\n *</table>\n *</div>\n)", s)
                if m:
                    s = s[:m.end()] + ORIGINAL + s[m.end():]
                    print("  callout 'piege du loot brut' reconstruit")

    # 3. retirer le bloc VEILLE-E:SEUIL (il sera reinsert par la vague E)
    o = "<!--VEILLE-E:SEUIL:OPEN-->"
    f = "<!--VEILLE-E:SEUIL:CLOSE-->"
    i = s.find(o)
    if i != -1:
        j = s.find(f)
        if j != -1:
            s = s[:i] + s[j + len(f):]
            print("  bloc VEILLE-E:SEUIL retire (reinsertion apres reparation)")

    PAGE.write_text(s, encoding="utf-8")
    print("  page ecrite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
