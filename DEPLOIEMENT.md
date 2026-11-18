# ABI NEXUS — Guide de déploiement

Ce document décrit les opérations à réaliser **avant** la mise en ligne
du guide. Tout est reproductible : chaque fichier racine est généré par
un script du dossier `tools/`.

---

## 1. Définir le domaine public

Toutes les URL absolues du site (canonical, Open Graph, `sitemap.xml`,
`robots.txt`) sont dérivées d'une constante unique.

1. Ouvrir `tools/seo_config.py`
2. Remplacer :

```python
SITE_URL = "https://abinexus.fr"
```

par le domaine réel, sans barre oblique finale :

```python
SITE_URL = "https://votre-domaine.fr"
```

3. Régénérer les fichiers :

```bash
python3 tools/build_s16.py          # 65 pages : <head> SEO
python3 tools/build_s16_files.py    # sitemap.xml, robots.txt, 404.html, manifest.json
python3 tools/audit_seo.py          # contrôle de conformité
```

Le script `build_s16.py` est **idempotent** : il peut être relancé
autant de fois que nécessaire sans dégrader les balises.

> ⚠️ Tant que `SITE_URL` n'est pas défini sur le domaine réel, les URL
> absolues restent des URL d'exemple. Les URL **internes** (liens,
> navigation, assets) restent valables sur n'importe quel hébergeur.

---

## 2. Serveur HTTP — renvoyer un vrai 404

Une page 404 servie en HTTP 200 est un « soft 404 » : les moteurs de
recherche l'indexent comme une page normale. Le serveur doit renvoyer
le code **404** tout en affichant `404.html`.

### nginx

```nginx
server {
    listen 80;
    server_name votre-domaine.fr;
    root /var/www/abinexus;
    index index.html;

    error_page 404 /404.html;

    # Compression : indispensable pour tenir les budgets de performance
    gzip on;
    gzip_types text/css application/javascript application/json image/svg+xml;
    gzip_min_length 512;

    # Cache des assets versionnes
    location ~* ^/(img|css|js)/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location = /sitemap.xml { add_header Cache-Control "public, max-age=3600"; }
    location = /robots.txt  { add_header Cache-Control "public, max-age=3600"; }

    # Le dossier tools/ n'est pas publie
    location /tools/ { deny all; }
}
```

### Apache (`.htaccess` à la racine du site)

```apache
ErrorDocument 404 /404.html

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpeg "access plus 30 days"
  ExpiresByType text/css "access plus 30 days"
  ExpiresByType application/javascript "access plus 30 days"
</IfModule>

<FilesMatch "^(sitemap\.xml|robots\.txt)$">
  Header set Cache-Control "public, max-age=3600"
</FilesMatch>
```

### Netlify / Vercel / Cloudflare Pages

Ajouter un fichier `_redirects` (Netlify) :

```
/*  /404.html  404
```

ou `vercel.json` (Vercel) :

```json
{ "cleanUrls": true, "trailingSlash": false }
```

---

## 3. Référencement

1. **Google Search Console** — ajouter le domaine, puis
   *Search Console → Sitemaps* → saisir `sitemap.xml`.
   Le fichier est déjà déclaré dans `robots.txt`, ce qui suffit pour la
   découverte automatique.
2. **Bing Webmaster Tools** — importer `sitemap.xml` de la même façon.
3. **Valider les données structurées** :
   * Google Rich Results Test — <https://search.google.com/test/rich-results>
   * Validateur schema.org — <https://validator.schema.org>
   Les pages à tester en priorité : l'accueil, une page de catégorie
   (armes), une fiche de carte, une page événementielle.
4. **Contrôle du rendu** — dans l'URL Inspection, vérifier que le
   style est bien appliqué : `robots.txt` ne bloque ni `/css` ni `/js`.

---

## 4. Contrôles de non-régression

```bash
python3 tools/qa_final.py         # 12 volets statiques S17 — 0 erreur, 0 avertissement
node    tools/test_s17_browser.js # recette Chromium réel — 48/48 (264 chargements)
python3 tools/audit.py            # audit global : 65 pages, liens, images, CJK, HTTP (65/65 en 200)
python3 tools/audit_seo.py        # audit SEO / performance
node tools/test_s15.js            # 58 assertions — modules interactifs S15
node tools/test_s16.js            # 51 assertions — SEO, JSON-LD, 404, fichiers racine
```

Les deux audits doivent sortir sur **« AUCUNE erreur »**.

Le rapport complet de la recette finale est dans **`RECETTE_S17.md`**.

### Avant la mise en ligne

1. **Domaine** — `SITE_URL` dans `tools/seo_config.py` doit pointer sur le
   domaine définitif (valeur actuelle : `https://abinexus.fr`, provisoire).
   Relancer ensuite `python3 tools/build_s16.py` puis
   `python3 tools/build_s16_files.py` pour régénérer les URL canoniques,
   `og:url` et le `sitemap.xml`.
2. **Vrai 404** — la section 2 de ce document doit être appliquée par
   l'hébergeur : `404.html` doit répondre en HTTP 404, jamais en 200
   (soft 404) ni en redirection.
3. **Bande-son** — deux pistes à ne pas exclure du déploiement :
   `audio/ambiance-menu.mp3` (24 s, 188 Ko), référencée par les 63 pages
   standard, et `audio/ambiance-infection.mp3` (24 s, 188 Ko), référencée par
   les 3 pages zombies.
4. **Couverture audio** — **65 pages sur 65** portent un lecteur de narration
   (`audio/narration-*.mp3`) ; le câblage est fait par
   `tools/cable_narrations.py`, qui n'insère le lecteur que si la piste est
   présente sur le disque. Les textes sources validés sont dans
   `tools/textes_audio/`.
5. **Catalogue média complet** — aucun visuel n'est en attente :
   `tools/pending_visuals.json` ne liste plus rien à produire. Les **24 armes** et
   les **24 objets** ont leur photographie réelle, pour un inventaire de
   **353 JPG, 0 PNG, 0 SVG, 0 image orpheline et 0 référence manquante**. Le repli visuel du site reste
   en place dans le code comme filet de sécurité, mais aucune carte du site
   ne l'affiche aujourd'hui — ce qui est conforme à la ligne éditoriale.

---

## 5. Choix stratégiques à connaître

### Crawlers IA
`robots.txt` autorise Googlebot, Bingbot et PerplexityBot (indexation
et citation) et bloque GPTBot, ClaudeBot, CCBot, Google-Extended,
Applebot-Extended, Bytespider et Meta-ExternalAgent (entraînement de
modèles). Le choix est centralisé dans `tools/seo_config.py`
(`AI_TRAINING_BOTS` / `AI_CITATION_BOTS`) : inversez les deux listes et
relancez `build_s16_files.py` pour le modifier.

Attention : `Google-Extended` contrôle l'entraînement **et**
l'ancrage dans Gemini. Le bloquer n'affecte **pas** le classement
Google Search ni les AI Overviews, qui dépendent de Googlebot.

### `sitemap.xml`
Ni `<priority>` ni `<changefreq>` : Google déclare explicitement
ignorer ces deux balises depuis des années. Seul `<lastmod>` est utile,
et uniquement s'il reflète une modification réelle — il est ici généré
à partir de la date de modification effective du fichier.

### Page 404
`404.html` est en `noindex, follow` : elle reste atteignable et
répertoriée comme lien de secours, mais n'entre pas dans l'index. Elle
n'est pas listée dans `sitemap.xml`.

---

## 6. Inventaire des fichiers racine

| Fichier | Rôle |
|---|---|
| `index.html` | page d'accueil |
| `404.html` | page d'erreur personnalisée (navigation globale conservée) |
| `sitemap.xml` | 66 URL indexables, `lastmod` au format W3C |
| `robots.txt` | règles d'exploration + politique crawlers IA |
| `manifest.json` | manifeste PWA (icônes JPG, 4 raccourcis) |
| `DEPLOIEMENT.md` | ce document |
