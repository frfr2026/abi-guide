#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABI NEXUS - audit de structure HTML.

Detecte les imbrications invalides que les audits fonctionnels ne voient pas :
un bloc insere au milieu d'une balise ouvrante (titre, paragraphe) peut laisser
la page valide pour le navigateur tout en produisant une hierarchie fausse
pour le lecteur d'ecran et pour le SEO.

Les regles d'auto-fermeture HTML5 sont appliquees (<p> ferme par un element de
bloc, <li> par <li>, <td>/<tr> par <td>/<tr>) afin que seuls les vrais
defauts soient signales.

Controles :
  1. balisage equilibre, avec detection des balises de fermeture orphelines
  2. aucun element de bloc a l'interieur d'un titre ou d'un paragraphe
  3. aucun <li> directement dans un <li>

Sortie : 0 erreur = structure saine.
"""
import pathlib
import sys
from html.parser import HTMLParser

RACINE = pathlib.Path(".")

TITRES = {"h1", "h2", "h3", "h4", "h5", "h6"}
INTERDITS = TITRES | {
    "p", "button", "label", "legend", "dt", "summary", "caption",
    "code", "kbd", "samp", "output",
}
BLOCS = {
    "address", "article", "aside", "blockquote", "details", "dialog", "div",
    "dl", "fieldset", "figure", "footer", "form", "header", "hr", "li",
    "main", "nav", "ol", "pre", "section", "table", "ul",
} | TITRES | {"p"}
VIDE = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# elements dont la balise de fin est optionnelle en HTML5
IMPLICITES = {"p", "li", "dt", "dd", "td", "th", "tr", "thead", "tbody",
              "tfoot", "option", "rt", "rp", "optgroup"}


class Verificateur(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pile = []
        self.erreurs = []
        self.titres = 0

    # ------------------------------------------------------------------
    def _fermer_implicite(self, tag):
        """Applique les regles d'auto-fermeture HTML5."""
        if tag in BLOCS and self.pile and self.pile[-1][0] == "p":
            self.pile.pop()
        if tag == "li" and self.pile and self.pile[-1][0] == "li":
            self.pile.pop()
        if tag in ("dt", "dd"):
            while self.pile and self.pile[-1][0] in ("dt", "dd"):
                self.pile.pop()
        if tag in ("td", "th"):
            while self.pile and self.pile[-1][0] in ("td", "th"):
                self.pile.pop()
        if tag == "tr":
            while self.pile and self.pile[-1][0] in ("td", "th", "tr"):
                self.pile.pop()
        if tag in ("thead", "tbody", "tfoot"):
            while self.pile and self.pile[-1][0] in ("td", "th", "tr",
                                                     "thead", "tbody", "tfoot"):
                self.pile.pop()
        if tag == "option" and self.pile and self.pile[-1][0] == "option":
            self.pile.pop()

    # ------------------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        ligne = self.getpos()[0]
        self._fermer_implicite(tag)

        if tag in TITRES:
            self.titres += 1

        if tag in BLOCS:
            for t, l in self.pile:
                if t in INTERDITS:
                    self.erreurs.append(
                        f"L{ligne} : <{tag}> a l'interieur de <{t}> (L{l}) "
                        f"- element de bloc dans un conteneur en ligne")
                    break

        if tag == "li" and self.pile and self.pile[-1][0] == "li":
            self.erreurs.append(
                f"L{ligne} : <li> directement dans <li> (L{self.pile[-1][1]})")

        if tag not in VIDE:
            self.pile.append((tag, ligne))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        ligne = self.getpos()[0]
        if tag in VIDE:
            return
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i][0] == tag:
                if i != len(self.pile) - 1:
                    ouvertes = self.pile[i + 1:]
                    # les elements implicites sont toleres
                    durs = [x for x in ouvertes if x[0] not in IMPLICITES]
                    if durs:
                        detail = ", ".join(f"<{t}>" for t, _ in durs)
                        self.erreurs.append(
                            f"L{ligne} : </{tag}> alors que {detail} "
                            f"est/sont encore ouverte(s)")
                del self.pile[i:]
                return
        self.erreurs.append(f"L{ligne} : </{tag}> sans ouverture")


def auditer(fichier):
    v = Verificateur()
    v.feed(fichier.read_text(encoding="utf-8"))
    v.close()
    for tag, ligne in v.pile:
        v.erreurs.append(f"L{ligne} : <{tag}> jamais fermee")
    return v.erreurs, v.titres


def main():
    fichiers = sorted(RACINE.glob("pages/*.html")) + [RACINE / "index.html", RACINE / "404.html"]
    total = 0
    pages_ok = 0
    titres = 0
    for f in fichiers:
        if not f.exists():
            continue
        errs, n = auditer(f)
        titres += n
        if errs:
            total += len(errs)
            print(f"\n  {f.relative_to(RACINE)}")
            for e in errs[:10]:
                print(f"    - {e}")
            if len(errs) > 10:
                print(f"    ... et {len(errs) - 10} autres")
        else:
            pages_ok += 1
    print("=" * 68)
    print(f"AUDIT STRUCTURE : {len(fichiers)} fichiers | {pages_ok} pages saines | "
          f"{titres} titres | {total} erreur(s)")
    print("=" * 68)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
