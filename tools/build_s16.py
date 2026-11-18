#!/usr/bin/env python3
"""ABI NEXUS — build_s16.py : refonte SEO/performance des <head>.

Pour chaque page (index.html + pages/*.html) :
  1. reecrit le bloc <head> avec un jeu de balises homogene
     (canonical, robots, Open Graph complet, Twitter Card, theme-color) ;
  2. genere un bloc JSON-LD @graph unique
     (Organization + WebSite + WebPage + BreadcrumbList + Article) ;
  3. ajoute width / height / decoding a chaque <img> (anti-CLS) ;
  4. rogne les titres (> 60 caracteres) et descriptions (> 160 caracteres) ;
  5. precharge l'image LCP de la page d'accueil.

Toutes les URL absolues sont derivees de tools/seo_config.py.

Usage : python3 tools/build_s16.py
"""
import pathlib, re, json, sys, html
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import seo_config as C  # noqa: E402

# ── Index des dimensions intrinseques des images ─────────────────
DIMS = {}
for p in (ROOT / 'img').rglob('*.jpg'):
    try:
        with Image.open(p) as im:
            DIMS[str(p.relative_to(ROOT))] = im.size
    except Exception:
        pass


def resolve_img(page_rel: str, src: str):
    """Chemin site-root d'une image referencee depuis une page.

    Accepte un chemin relatif ('../img/x.jpg') comme une URL absolue
    deja issue du site ('https://domaine/img/x.jpg') : le script est
    ainsi idempotent et peut etre relance sans degrade les balises.
    """
    if not src:
        return None
    base_site = C.SITE_URL.rstrip('/') + '/'
    if src.startswith(base_site):
        src = src[len(base_site):]
        base = pathlib.Path('.')
    elif src.startswith('http'):
        return None
    else:
        base = pathlib.Path(page_rel).parent
    try:
        return str((base / src).resolve().relative_to(ROOT.resolve()))
    except Exception:
        return None


def esc(s):
    return html.escape(str(s), quote=True)


def clean_text(s):
    """Nettoie une balise meta (entites HTML decodees, espaces reduits)."""
    return html.unescape(s or '').strip()


def clip(text, limit):
    """Rogne un texte sur une frontiere de mot, sans couper un mot."""
    text = clean_text(text)
    if len(text) <= limit:
        return text
    cut = text[:limit].rstrip()
    sp = cut.rfind(' ')
    if sp > limit * 0.6:
        cut = cut[:sp]
    return cut.rstrip(' ,;:.—-') + '…'


# ── Extraction de la hierarchie de fil d'Ariane depuis la page ────
def parse_breadcrumb(s):
    """Retourne [(nom, url)] du fil d'Ariane visible de la page."""
    m = re.search(r'<nav class="breadcrumb".*?</nav>', s, re.S)
    if not m:
        return []
    nav = m.group(0)
    items = []
    for href, label in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', nav):
        clean = re.sub(r'<[^>]+>', '', label).strip()
        if clean:
            items.append((clean, href))
    return items


# ── Reecriture complete du <head> ────────────────────────────────
def rebuild_head(s, page_rel):
    head_end = s.index('</head>')
    head = s[:head_end]
    body = s[head_end:]

    # --- donnees existantes ---
    title_m = re.search(r'<title>(.*?)</title>', head, re.S)
    title = clean_text(title_m.group(1)) if title_m else ''
    desc_m = re.search(r'<meta name="description" content="(.*?)"\s*/?>', head, re.S)
    desc = clean_text(desc_m.group(1)) if desc_m else ''
    og_title_m = re.search(r'<meta property="og:title" content="(.*?)"\s*/?>', head, re.S)
    og_title = clean_text(og_title_m.group(1)) if og_title_m else ''
    og_desc_m = re.search(r'<meta property="og:description" content="(.*?)"\s*/?>', head, re.S)
    og_desc = clean_text(og_desc_m.group(1)) if og_desc_m else ''
    og_img_m = re.search(r'<meta property="og:image" content="(.*?)"\s*/?>', head, re.S)
    og_img = clean_text(og_img_m.group(1)) if og_img_m else ''
    og_type_m = re.search(r'<meta property="og:type" content="(.*?)"\s*/?>', head, re.S)
    og_type = clean_text(og_type_m.group(1)) if og_type_m else 'article'

    # --- decoupe titre / marque ---
    # "Titre | ABI NEXUS" -> ("Titre", "ABI NEXUS", "|")
    suffix = ''
    sep = ' — '
    for cand in ('| ABI NEXUS', '— ABI NEXUS', '– ABI NEXUS'):
        if title.endswith(cand):
            title, suffix = title[:-len(cand)].strip(), 'ABI NEXUS'
            sep = ' | ' if cand.startswith('|') else ' — '
            break

    is_index = page_rel == C.ROOT_INDEX
    if is_index:
        # Titre dedie a la page d'accueil : lisible en entier dans
        # la ligne de resultat, sans troncature.
        title = 'ABI NEXUS — Guide Arena Breakout Infinite | Saison 7'
        suffix = ''
        sep = ''
    else:
        # Le titre complet (titre + marque) doit tenir dans 60 caracteres.
        room = 60 - len(sep + suffix) if suffix else 60
        title = clip(title, room)
    desc = clip(desc or og_desc, 160)

    canonical = C.page_url(page_rel)

    # --- image sociale ---
    img_rel = None
    if og_img:
        img_rel = resolve_img(page_rel, og_img)
    if is_index:
        img_rel = 'img/seo/og-accueil.jpg'
    # Une image sociale verticale est rognee par les plateformes :
    # on bascule sur une carte OG paysage dediee.
    if img_rel and img_rel in DIMS:
        w0, h0 = DIMS[img_rel]
        if not (1.5 <= (w0 / h0) <= 2.1):
            img_rel = None
    if not img_rel or img_rel not in DIMS:
        fallback = 'img/seo/og-accueil.jpg' if is_index else (
            'img/seo/og-outils.jpg' if ('meta' in page_rel or 'optimizer' in page_rel
                                        or 'strat' in page_rel or 'builds' in page_rel
                                        or 'tier-list' in page_rel) else 'img/seo/og-archives.jpg')
        img_rel = fallback
    iw, ih = DIMS[img_rel]
    img_abs = C.abs_url(img_rel)
    img_alt = "ABI NEXUS — guide Arena Breakout Infinite, Saison 7 : Utopia"

    # --- fil d'Ariane ---
    crumbs = parse_breadcrumb(s)

    # --- dates ---
    pub = '2026-09-16'
    mod = C.CONTENT_DATE
    old_ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
    for blk in old_ld:
        try:
            d = json.loads(blk)
        except Exception:
            continue
        if isinstance(d, dict):
            pub = d.get('datePublished', pub) or pub
            mod = d.get('dateModified', mod) or mod

    # --- JSON-LD @graph ---
    graph = []
    org_id = C.SITE_URL.rstrip('/') + '/#organization'
    web_id = C.SITE_URL.rstrip('/') + '/#website'
    page_id = canonical + '#webpage'
    art_id = canonical + '#article'
    bc_id = canonical + '#breadcrumb'

    graph.append({
        "@type": "Organization",
        "@id": org_id,
        "name": C.SITE_NAME,
        "url": C.SITE_URL.rstrip('/') + '/',
        "logo": {
            "@type": "ImageObject",
            "url": C.abs_url('img/ui/favicon-512.jpg'),
            "width": 512,
            "height": 512
        }
    })
    graph.append({
        "@type": "WebSite",
        "@id": web_id,
        "url": C.SITE_URL.rstrip('/') + '/',
        "name": C.SITE_LONG_NAME,
        "description": C.SITE_DESCRIPTION,
        "inLanguage": "fr-FR",
        "publisher": {"@id": org_id}
    })

    webpage = {
        "@type": "WebPage",
        "@id": page_id,
        "url": canonical,
        "name": title + (sep + suffix if suffix else ''),
        "description": desc,
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": web_id},
        "publisher": {"@id": org_id},
        "datePublished": pub,
        "dateModified": mod,
        "primaryImageOfPage": {"@type": "ImageObject", "url": img_abs, "width": iw, "height": ih}
    }
    if crumbs:
        webpage["breadcrumb"] = {"@id": bc_id}
    graph.append(webpage)

    if crumbs:
        elements = []
        for i, (name, href) in enumerate(crumbs, start=1):
            el = {"@type": "ListItem", "position": i, "name": name}
            if i < len(crumbs):
                target = href if href.startswith('http') else C.page_url(
                    ('pages/' + href) if not href.startswith('../') else href.replace('../', '', 1))
                el["item"] = target
            elements.append(el)
        graph.append({
            "@type": "BreadcrumbList",
            "@id": bc_id,
            "itemListElement": elements
        })

    article = {
        "@type": "Article" if og_type == 'article' else "WebPage",
        "@id": art_id,
        "headline": title,
        "description": desc,
        "image": [img_abs],
        "datePublished": pub,
        "dateModified": mod,
        "author": {"@id": org_id},
        "publisher": {"@id": org_id},
        "mainEntityOfPage": {"@id": page_id},
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": web_id}
    }
    if og_type == 'article':
        graph.append(article)

    if is_index:
        graph.append({
            "@type": "VideoGame",
            "name": C.GAME,
            "url": C.abs_url('index.html'),
            "gamePlatform": "PC",
            "applicationCategory": "Game",
            "operatingSystem": "Windows",
            "inLanguage": "fr-FR",
            "description": C.SITE_DESCRIPTION,
            "image": img_abs,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}
        })

    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, indent=2)

    # --- assemblage du <head> ---
    head_parts = []
    head_parts.append('<!DOCTYPE html>')
    head_parts.append('<html lang="fr" data-theme="dark">')
    head_parts.append('<head>')
    head_parts.append('  <meta charset="UTF-8">')
    head_parts.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    full_title = title + (sep + suffix if suffix else '')
    head_parts.append('  <title>' + esc(full_title) + '</title>')
    head_parts.append('  <meta name="description" content="' + esc(desc) + '">')
    head_parts.append('  <meta name="robots" content="' + C.ROBOTS + '">')
    head_parts.append('  <meta name="author" content="ABI NEXUS">')
    head_parts.append('  <meta name="language" content="French">')
    head_parts.append('  <meta name="theme-color" content="' + C.THEME_COLOR_DARK + '" media="(prefers-color-scheme: dark)">')
    head_parts.append('  <meta name="theme-color" content="' + C.THEME_COLOR_LIGHT + '" media="(prefers-color-scheme: light)">')
    head_parts.append('  <link rel="canonical" href="' + esc(canonical) + '">')
    head_parts.append('  <link rel="alternate" hreflang="fr" href="' + esc(canonical) + '">')
    head_parts.append('  <link rel="sitemap" type="application/xml" title="Sitemap ABI NEXUS" href="' + esc(C.abs_url('sitemap.xml')) + '">')
    head_parts.append('  <meta property="og:type" content="' + (og_type if og_type in ('article', 'website') else 'article') + '">')
    head_parts.append('  <meta property="og:site_name" content="' + esc(C.SITE_NAME) + '">')
    head_parts.append('  <meta property="og:locale" content="' + C.SITE_LOCALE + '">')
    head_parts.append('  <meta property="og:title" content="' + esc(og_title or (title + (sep + suffix if suffix else ''))) + '">')
    head_parts.append('  <meta property="og:description" content="' + esc(og_desc or desc) + '">')
    head_parts.append('  <meta property="og:url" content="' + esc(canonical) + '">')
    head_parts.append('  <meta property="og:image" content="' + esc(img_abs) + '">')
    head_parts.append('  <meta property="og:image:width" content="' + str(iw) + '">')
    head_parts.append('  <meta property="og:image:height" content="' + str(ih) + '">')
    head_parts.append('  <meta property="og:image:alt" content="' + esc(img_alt) + '">')
    head_parts.append('  <meta property="og:image:type" content="image/jpeg">')
    head_parts.append('  <meta name="twitter:card" content="summary_large_image">')
    head_parts.append('  <meta name="twitter:title" content="' + esc(og_title or (title + (sep + suffix if suffix else ''))) + '">')
    head_parts.append('  <meta name="twitter:description" content="' + esc(og_desc or desc) + '">')
    head_parts.append('  <meta name="twitter:image" content="' + esc(img_abs) + '">')
    head_parts.append('  <meta name="twitter:image:alt" content="' + esc(img_alt) + '">')
    head_parts.append('  <meta property="article:section" content="' + esc(
        (crumbs[0][0] if crumbs else 'ABI NEXUS')) + '">')
    head_parts.append('  <link rel="preconnect" href="https://fonts.googleapis.com">')
    head_parts.append('  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    head_parts.append('  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@400;500;600;700&family=Exo+2:wght@300;400;600&display=swap" rel="stylesheet">')
    # preload de l'image LCP (accueil uniquement)
    if is_index:
        head_parts.append('  <link rel="preload" as="image" href="img/hero/hero-accueil.jpg" fetchpriority="high">')
    head_parts.append('  <link rel="stylesheet" href="' + ('css' if is_index else '../css') + '/variables.css">')
    head_parts.append('  <link rel="stylesheet" href="' + ('css' if is_index else '../css') + '/main.css">')
    head_parts.append('  <link rel="stylesheet" href="' + ('css' if is_index else '../css') + '/animations.css">')
    head_parts.append('  <link rel="stylesheet" href="' + ('css' if is_index else '../css') + '/components.css">')
    head_parts.append('  <link rel="stylesheet" href="' + ('css' if is_index else '../css') + '/responsive.css">')
    head_parts.append('  <link rel="icon" type="image/jpeg" sizes="64x64" href="' + ('img' if is_index else '../img') + '/ui/favicon-64.jpg">')
    head_parts.append('  <link rel="apple-touch-icon" href="' + ('img' if is_index else '../img') + '/ui/favicon-180.jpg">')
    head_parts.append('  <link rel="manifest" href="' + ('manifest.json' if is_index else '../manifest.json') + '">')
    head_parts.append('  <script type="application/ld+json">')
    head_parts.append(ld)
    head_parts.append('  </script>')
    head_parts.append('</head>')

    new_head = "\n".join(head_parts)

    # on conserve le <body ...> eventuel depuis l'ancien head
    body_open = re.search(r'<body[^>]*>', body)
    if body_open:
        body = body_open.group(0) + body[body_open.end():]
    else:
        body = '<body>' + body

    # --- balises <img> : width / height / decoding ---
    def fix_img(m):
        tag = m.group(0)
        src_m = re.search(r'src="([^"]+)"', tag)
        if not src_m:
            return tag
        rel = resolve_img(page_rel, src_m.group(1))
        if not rel or rel not in DIMS:
            return tag
        w, h = DIMS[rel]
        if 'width=' not in tag:
            tag = tag.replace(' src=', ' width="%d" height="%d" src=' % (w, h), 1)
        if 'decoding=' not in tag:
            tag = tag.replace(' loading="lazy"', ' loading="lazy" decoding="async"', 1)
            if 'decoding=' not in tag:
                tag = tag.replace('<img ', '<img decoding="async" ', 1)
        return tag

    body = re.sub(r'<img[^>]*>', fix_img, body)

    return new_head + body


def main():
    targets = [ROOT / C.ROOT_INDEX] + sorted((ROOT / C.PAGES_DIR).glob('*.html'))
    changed = 0
    for f in targets:
        rel = str(f.relative_to(ROOT))
        s = f.read_text(encoding='utf-8')
        new = rebuild_head(s, rel)
        if new != s:
            f.write_text(new, encoding='utf-8')
            changed += 1
    print('S16 : %d pages réécrites sur %d' % (changed, len(targets)))


if __name__ == '__main__':
    main()
