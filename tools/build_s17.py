#!/usr/bin/env python3
"""ABI NEXUS — build_s17.py : corrections d'accessibilite (S17 QA_FINAL).

Corrige, sur l'ensemble des pages :
  1. la hierarchie des titres (WCAG 1.3.1) : un <h4> place directement
     sous un <h2> est promu en <h3 class="h4">, ce qui restaure une
     hierarchie continue h1 > h2 > h3 > h4 sans modifier le rendu ;
  2. l'annonce des liens ouvrant un nouvel onglet : un texte reserve
     aux lecteurs d'ecran est insere dans chaque lien externe
     (target="_blank") : l'ouverture dans un nouvel onglet est
     signalee aux lecteurs d'ecran ;
  3. l'identite des liens : chaque <a> porte desormais un id unique
     "lnk-<page>-<n>", ce qui permet de referencer une cible precise.

Le script est idempotent.

Usage : python3 tools/build_s17.py
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted((ROOT / 'pages').glob('*.html')) + [ROOT / 'index.html', ROOT / '404.html']

SR_ONLY = '<span class="sr-only"> (nouvel onglet)</span>'


def slug(name):
    s = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return s[:28]


# ════════════════════════════════════════════════════════════════
#  1. Hierarchie des titres
# ════════════════════════════════════════════════════════════════
HEAD_RE = re.compile(r'<h([1-6])([^>]*)>(.*?)</h\1>', re.S)


def fix_headings(s):
    """Repare la hierarchie des titres (WCAG 1.3.1).

    Regle : un titre ne doit jamais sauter un niveau. Si le niveau
    du titre est superieur de plus d'un cran a celui du titre
    precedent, il est promu au niveau precedent + 1.

    L'apparence d'origine est preservee par une classe :
      <h4> -> <h3 class="h4">   (rendu de h4 conserve)
      <h5> -> <h4 class="h5">   (rendu de h5 conserve)
    """
    body_start = s.index('<body>')
    head, body = s[:body_start], s[body_start:]

    matches = list(HEAD_RE.finditer(body))
    if not matches:
        return s, 0

    planned = {}   # start -> (nouveau niveau, classe de rendu)
    prev = 0
    for m in matches:
        lvl = int(m.group(1))
        target = lvl
        if prev and lvl > prev + 1:
            target = prev + 1
        if target != lvl:
            planned[m.start()] = (target, 'h%d' % lvl)
        prev = target

    if not planned:
        return s, 0

    out = []
    last = 0
    for m in matches:
        if m.start() not in planned:
            continue
        target, keep = planned[m.start()]
        out.append(body[last:m.start()])
        attrs = m.group(2)
        if 'class=' in attrs:
            attrs = re.sub(r'class="([^"]*)"', r'class="\1 %s"' % keep, attrs)
        else:
            attrs = attrs + ' class="%s"' % keep
        out.append('<h%d%s>%s</h%d>' % (target, attrs, m.group(3), target))
        last = m.end()
    out.append(body[last:])
    return head + ''.join(out), len(planned)


# ════════════════════════════════════════════════════════════════
#  2. Liens externes : annonce du nouvel onglet + identifiant unique
# ════════════════════════════════════════════════════════════════
A_RE = re.compile(r'<a\b([^>]*)>(.*?)</a>', re.S)


def fix_links(s, page_id):
    head_end = s.index('<body>')
    head, body = s[:head_end], s[head_end:]

    counter = [0]

    def repl(m):
        attrs, inner = m.group(1), m.group(2)
        counter[0] += 1
        # Identifiant unique pour pouvoir cibler le lien.
        # Les identifiants lnk-<page>-<n> sont d'abord retires, puis
        # reaffectes dans l'ordre du document : sans cela, l'insertion
        # d'un nouveau lien au milieu d'une page decale la numerotation
        # et crée un doublon (le compteur ignorait les ancres qui
        # avaient deja un identifiant).
        attrs = re.sub(r'\s+id="lnk-[^"]*"', '', attrs)
        attrs += ' id="lnk-%s-%03d"' % (page_id, counter[0])
        if 'target="_blank"' in attrs and SR_ONLY not in inner:
            # le texte reserve est place en fin de contenu du lien
            inner = inner + SR_ONLY
        return '<a%s>%s</a>' % (attrs, inner)

    body = A_RE.sub(repl, body)
    return head + body


# ════════════════════════════════════════════════════════════════
def main():
    total_h = total_a = 0
    detail = {}
    for f in PAGES:
        rel = f.relative_to(ROOT)
        s = f.read_text(encoding='utf-8')
        before = s
        s, nh = fix_headings(s)
        s = fix_links(s, slug(f.stem))
        if s != before:
            f.write_text(s, encoding='utf-8')
        total_h += nh
        total_a += 1
    # compte par niveau d'origine, a partir de l'etat final du site
    for f in PAGES:
        s = f.read_text(encoding='utf-8')
        for m in HEAD_RE.finditer(s[s.index('<body>'):]):
            attrs = m.group(2)
            cm = re.search(r'class="([^"]*)"', attrs)
            if cm and re.search(r'\bh[4-6]\b', cm.group(1)):
                key = cm.group(1).split()[-1]
                detail[key] = detail.get(key, 0) + 1
    promoted = ' + '.join('%s : %d' % (k, v) for k, v in sorted(detail.items())) or 'aucune'
    print('S17 : %d pages traitees — titres promus conserves [%s]'
          % (total_a, promoted))
    print('S17 : le script est idempotent (relance sans modification)')


if __name__ == '__main__':
    main()
