#!/usr/bin/env python3
"""Configuration SEO d'ABI NEXUS — source unique de vérité (S16).

Le fichier est consommé par :
  • tools/build_s16.py     — réécriture des <head> de toutes les pages
  • tools/build_sitemap.py — génération de sitemap.xml
  • tools/build_robots.py  — génération de robots.txt
  • tools/audit_seo.py     — contrôle de conformité

IMPORTANT — À REMPLIR AVANT MISE EN PRODUCTION
---------------------------------------------
SITE_URL est le nom de domaine public du site. Tant qu'il n'est pas
défini sur le domaine réel, les URL absolues (canonical, og:image,
sitemap, robots.txt) restent des URL d'exemple. Après changement,
relancer :

    python3 tools/build_s16.py && python3 tools/build_sitemap.py && \\
    python3 tools/build_robots.py && python3 tools/audit_seo.py
"""

# ── Domaine public ───────────────────────────────────────────────
# TODO(SEO) : remplacer par le domaine réel avant mise en ligne.
SITE_URL = "https://abinexus.fr"

# ── Identité du site ─────────────────────────────────────────────
SITE_NAME = "ABI NEXUS"
SITE_LONG_NAME = "ABI NEXUS — Guide Ultime Arena Breakout Infinite"
SITE_DESCRIPTION = (
    "Le guide de reference francais d'Arena Breakout Infinite : "
    "Saison 7 Utopia, armes, armures, munitions, cartes, economie, "
    "strategies, tier lists et outils interactifs."
)
SITE_LOCALE = "fr_FR"
THEME_COLOR_DARK = "#0a0b0e"
THEME_COLOR_LIGHT = "#f4f5f7"
GAME = "Arena Breakout Infinite"
SEASON = "Saison 7 : Utopia"
PATCH = "1.0.0.142.19"
CONTENT_DATE = "2026-11-17"

# ── Balises robots ───────────────────────────────────────────────
# max-image-preview:large autorise les aperçus d'images en pleine
# largeur dans les resultats Google (recommandation 2026).
# max-snippet:-1 autorise un extrait de texte illimite.
ROBOTS = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"

# ── Politiques robots (fichier robots.txt) ───────────────────────
# Google ignore crawl-delay (clarifie en fevrier 2026) : on ne le
# declare pas pour le robot principal. En revanche, les crawlers
# IA sont traites separement : le site reste lisible par les moteurs
# de recherche classiques, mais son contenu n'est pas exploite pour
# l'entrainement de modeles.
AI_TRAINING_BOTS = [
    "GPTBot",           # OpenAI — entrainement
    "CCBot",            # Common Crawl — entrainement
    "ClaudeBot",        # Anthropic — entrainement
    "Google-Extended",  # Google — entrainement / grounding Gemini
    "Applebot-Extended",# Apple — entrainement
    "Bytespider",       # ByteDance — entrainement
    "Meta-ExternalAgent", # Meta — entrainement
]
# PerplexityBot et Googlebot restent autorises : ces robots citent
# et indexent le site, ils ne l'entrainent pas.
AI_CITATION_BOTS = ["PerplexityBot", "Googlebot", "Bingbot"]

# ── Arborescence ─────────────────────────────────────────────────
PAGES_DIR = "pages"
ROOT_INDEX = "index.html"

# Fichiers exclus du sitemap (pages d'erreur, pages non indexables)
SITEMAP_EXCLUDE = {"404.html"}

# ── Cartes Open Graph dediees (1200x630) ─────────────────────────
OG_CARDS = {
    "og-accueil":  "img/seo/og-accueil.jpg",
    "og-outils":   "img/seo/og-outils.jpg",
    "og-archives": "img/seo/og-archives.jpg",
}

# ── Utilitaires ──────────────────────────────────────────────────
def abs_url(path: str) -> str:
    """Transforme un chemin relatif du site en URL absolue."""
    if not path:
        return ""
    if path.startswith("http://") or path.startswith("https://"):
        return path
    return SITE_URL.rstrip("/") + "/" + path.lstrip("/")


def page_url(relative: str) -> str:
    """URL absolue d'une page du site (chemin relatif a la racine)."""
    return abs_url(relative)
