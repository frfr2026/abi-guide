#!/usr/bin/env python3
"""Injection des blocs de donnees officielles dans les pages cartes.

Les blocs sont generes par tools/enrich_maps.py puis inseres avant le
sommaire (aside.toc) de chaque page, avec mise a jour du sommaire.
"""
import re, pathlib, sys, importlib.util

ROOT = pathlib.Path('.')
spec = importlib.util.spec_from_file_location('em', ROOT / 'tools' / 'enrich_maps.py')
em = importlib.util.module_from_spec(spec)
spec.loader.exec_module(em)

PAGES = em.PAGES


def insert_before_toc(raw, blocks):
    """Insere les blocs dans l'article (avant </article>), sinon avant le sommaire."""
    i = raw.find('</article>')
    if i >= 0:
        return raw[:i] + '\n' + blocks + '\n        ' + raw[i:]
    i = raw.find('<aside class="toc"')
    if i < 0:
        return None
    return raw[:i] + blocks + '\n' + raw[i:]


def update_toc(raw, new_links):
    """Ajoute les liens de sommaire correspondants aux nouveaux blocs."""
    for anchor, label in new_links:
        if 'href="#%s"' % anchor in raw:
            continue
        # insere avant la fermeture du sommaire
        m = re.search(r'(<aside class="toc".*?)(</aside>)', raw, re.S)
        if not m:
            continue
        add = '\n<a href="#%s">%s</a>' % (anchor, label)
        raw = raw[:m.end(1)] + add + raw[m.end(1):]
    return raw


if __name__ == '__main__':
    for page, (slug, name) in PAGES.items():
        p = ROOT / 'pages' / page
        raw = p.read_text(encoding='utf-8')
        blocks, desc, info = em.build_sections(slug, name)
        if 'id="zones"' not in raw:
            raw2 = insert_before_toc(raw, blocks)
            if raw2 is None:
                print('  ! %s : sommaire introuvable' % page)
                continue
            # met a jour le sommaire
            links = []
            for anchor, label in (('zones', 'Zones officielles'),
                                   ('extractions-officielles', 'Extractions officielles'),
                                   ('cles', 'Clés de la carte'),
                                   ('cartes-interactives', 'Cartes interactives')):
                if 'id="%s"' % anchor in blocks:
                    links.append((anchor, label))
            raw2 = update_toc(raw2, links)
            p.write_text(raw2, encoding='utf-8')
            print('  %-26s +%d blocs, +%d liens sommaire' % (page, blocks.count('<h2'), len(links)))
        else:
            print('  %-26s deja enrichi' % page)
