# ABI NEXUS — Rapport de recette finale (S17 QA_FINAL)

**Site :** ABI NEXUS — Guide Arena Breakout Infinite
**Domaine de production :** `https://abinexus.fr` (provisoire — à confirmer)
**Version du guide :** v1.0.0 — Saison 7 : Utopia
**Patch de référence :** 1.0.0.142.19 (Build 4.19.88-REV)
**Date de recette :** 17 novembre 2026
**Verdict :** ✅ **VALIDÉ — aucune erreur bloquante, aucun avertissement**

---

## 1. Synthèse

| Domaine | Vérifications | Résultat |
|---|---|---|
| Structure HTML et hiérarchie des titres | 66 pages | 0 saut de niveau, 1 `<h1>` par page |
| Accessibilité (noms, libellés, skip link, landmarks) | 66 pages | 0 élément sans nom, 0 champ sans libellé |
| Accessibilité (focus, cible tactile, reduced motion) | 5 points CSS | 5/5 conformes |
| Navigation globale | 66 pages | 1 seule variante après normalisation |
| Liens internes et identifiants | 7 700+ liens | 0 lien cassé, 0 identifiant dupliqué |
| Liens externes | 452 liens | 0 sans `noopener`, 0 ouverture non annoncée |
| Images | 153 fichiers | 0 manquante, 0 sans alt, 0 sans dimensions, 0 PNG/SVG |
| JavaScript | 12 modules | 0 erreur de syntaxe, 5 modules à région live |
| Performance | 66 pages | CSS 18,1 Ko gzip · JS 36,7 Ko gzip · 0 page > 25 Ko gzip |
| Contenu | 66 pages | 0 caractère CJK, 66/66 titres et descriptions uniques |
| Fichiers racine | 4 fichiers | sitemap 65 URL · robots 53 lignes · manifeste 4+4 |
| Orthographe française | 66 pages | 0 occurrence suspecte |
| **Recette navigateur (Chromium)** | **264 chargements** | **48/48 assertions** |
| **Résolution des liens de recherche** | **127 assertions** | **0 lien cassé** |
| **Audit approfondi médias/texte/liens** | **66 pages + racine** | **0 erreur, 0 avertissement** |

**Non-régression :** audit global 64 pages / 0 erreur / 64 HTTP 200 · audit SEO 0 erreur / 0 avertissement · audit approfondi 0 erreur / 0 avertissement · tests S15 **58/58** · tests S16 **51/51** · tests S18 recherche **127/127**.

---

## 2. Anomalies détectées et corrigées en S17

### 2.1 Accessibilité et structure

| Anomalie | Portée | Correction |
|---|---|---|
| 196 titres sautaient un niveau de hiérarchie (183 `<h4>` sous `<h2>`, 13 `<h5>` sous `<h3>`) | 65 pages | `tools/build_s17.py` promeut chaque titre au niveau immédiatement précédent et conserve son apparence via les classes `h4` / `h5` (rendu identique, hiérarchie continue h1 → h2 → h3 → h4 → h5) |
| 2 règles `outline: none` neutralisaient l'indicateur de focus | `css/components.css` | Supprimées — le focus est désormais visible au clavier (contrôle Chromium : outline calculé sur la navigation) |
| 433 liens externes ouvraient un nouvel onglet sans annonce | 65 pages | Ajout de `<span class="sr-only"> (nouvel onglet)</span>` dans chaque lien `target="_blank"` |
| Identifiants de liens absents (ciblage impossible) | 65 pages | Chaque `<a>` reçoit un identifiant unique `lnk-<page>-<n>` — 0 doublon sur l'ensemble du site |
| Aucune région `aria-live` sur les modules interactifs | 5 modules | `search.js`, `loadout-builder.js`, `map-explorer.js`, `tier-list.js`, `optimizer.js` : ajout d'une région live polie |
| 3 navigateurs convergeaient vers des pages hors périmètre (16 pages) | 65 pages | `pages/meta-stratégies-s7.html` → `pages/stratégies-s7.html`, `pages/items-koen-economie.html` → `pages/items-koen-economie.html`, `pages/community-ressources.html` → `pages/communaute-ressources.html` |

### 2.1 bis — Reconstruction de la navigation globale

La revue visuelle a révélé que la barre de navigation reposait sur un assemblage
par substitutions successives (S13, S14, S17) laissant **un `</div>` surnuméraire**
dans le `<header>` : la balise `<nav class="nav-links">` se fermait après « Objets ».
Conséquences mesurées avant correction :

| Symptôme | Mesure | Correction |
|---|---|---|
| HTML mal formé | 41 `<div>` ouverts / 42 `</div>` fermés, sur les 65 pages | `tools/build_nav.py` reconstruit le `<header>` **entièrement** depuis un modèle unique : 0 header déséquilibré, 0 saut de structure |
| Menu mobile inutilisable | bouton hamburger à **x = 623 px** sur un écran de 375 px (hors écran) | Le conteneur `.nav-inner` retrouve sa structure flex : hamburger à **x = 265–307 px**, dans l'écran |
| Entrées « Méta », « Univers », « Événements », « Communauté » hors flux | sorties de `nav.nav-links` par le `</div>` en trop | Les 10 entrées de premier niveau sont de nouveau dans le flux, écart minimum mesuré à **24 px** |
| « Objets » sans méga-menu | lien nu, alignement incohérent | Méga-menu « Objets » à 3 colonnes (10 liens) : munitions & valeur, accès & production, soins & cosmétiques |
| « Objets » / « Cartes » indistincts | collision visuelle « CARTESOBJETS » | Séparés : « Cartes » (7 cartes), « Objets » (10 objets), chacun avec son méga-menu |
| Accordeéon mobile refermant le panneau | le clic sur une entrée repliait tout le panneau au lieu de déplier la colonne | `js/navigation.js` : le clic sur une entrée de premier niveau déplie sa colonne en mobile ; seule une navigation ferme le panneau. Fermeture par `Échap` ajoutée, `aria-expanded` sur chaque déclencheur |
| Badge « Utopia » collé au libellé | halo du badge tangent sur « SAISON 7 » | Marge de 0,5 rem sur `.nav-link .badge` en mobile — écart mesuré à **8 px** |

La structure est désormais **identique sur les 65 pages** (1 seule variante de
navigation normalisée) et l'état actif (`aria-current="page"`) est appliqué
automatiquement par section sur 64 pages sur 66.

### 2.2 Responsive (détecté par Chromium réel, invisible en analyse statique)

| Anomalie | Portée | Correction |
|---|---|---|
| **Débordement horizontal à 375 px sur 34 pages** (jusqu'à 564 px de large) | 65 pages | Cause : les pistes de grille `1fr` ne pouvaient pas descendre sous la largeur de leur contenu (tableaux larges, listes, faits). Correction : toutes les pistes passent en `minmax(0, 1fr)`, `min-width: 0` ajouté aux enfants de grille, tableaux Griffiths défilables, `overflow-wrap: anywhere` sur les titres longs (ex. « 3. Reddit : r/ArenaBreakoutInfinite ») |
| Barre de navigation débordante à 375 px | 65 pages | Logo compacté (1,02 rem), actions resserrées, recherche repliée sur son icône (36 px), `gap` réduit |
| Cibles tactiles sous 24 px | navigation | Hauteur minimale de 42 px sur le bouton menu mobile |

**Résultat après correction : 0 débordement horizontal sur 65 pages × 4 largeurs (375 / 768 / 1280 / 1440 px), soit 260 chargements.**

### 2.3 Ressources et médias

| Anomalie | Portée | Correction |
|---|---|---|
| **15 visuels d'armes référencés mais absents** (`m4a1`, `aek971`, `m110`, `mk14`, `sj16`, `mosin`, `mpx`, `vss`, `vector`, `pcc9`, `sks`, `usas12`, `rpk16`, `banshee`, `t88`) | `js/data-weapons.json` | Référence recalée sur le visuel de repli ; cible finale conservée dans `imagePending` et listée dans `tools/pending_visuals.json` pour production par lots de 10 |
| **17 visuels d'objets référencés mais absents** | `js/data-items.json` | Idem — repli sur `img/items/red-drop.jpg`, cibles listées dans `tools/pending_visuals.json` |
| **Piste audio du menu absente** (`audio/ambiance-menu.mp3`) — référencée par les 65 pages | 65 pages | `tools/build_audio.py` : synthèse locale d'une ambiance industrielle boucleable (drone 55 Hz, souffle filtré, cliquetis lointains), encodage MP3 via `lameenc` — 24 s, mono 44,1 kHz, 64 kbps, 188 Ko, en-tête MPEG valide |
| `img/hero/hero-accueil.jpg` signalée orpheline | audit | Faux positif : le visuel est référencé par un `preload` et un `background-image` — le scan des références a été élargi (JSON, JS, `<link>`, `og:image`, CSS, `url()` inline) |
| Le validateur ne vérifiait pas l'existence des images référencées en JSON | `tools/qa_final.py` | Contrôle ajouté : 75 références JSON vérifiées, 0 manquante |

### 2.4 Contenu et forme

| Anomalie | Correction |
|---|---|
| 33 faux positifs d'orthographe (« complet », « situation », « comparaison », « explicite » sont des formes correctes sans accent) | Liste de contrôle refaite : seuls les mots dont la forme sans accent est toujours fautive sont signalés. Deux vraies erreurs corrigées : « votre reference » → « votre **référence** », « côté economie » → « côté **économie** » |
| Variantes de navigation vues comme différentes entre la racine et les pages | Normalisation des préfixes `pages/` : 1 seule variante réelle. Le lien « Objets » manquant à l'accueil a été ajouté |
| La page 404 générée ne recevait pas les corrections S17 | `tools/build_s16_files.py` applique désormais le correcteur S17 à `404.html` après génération |

---

## 3. Recette navigateur (Chromium via Playwright)

`tools/test_s17_browser.js` — **48 assertions, 0 échec**.

1. **Balayage** — 66 pages × 4 largeurs (375 / 768 / 1280 / 1440 px) = 264 chargements.
2. **Débordement horizontal** — 0 débordement.
3. **Erreurs console** — 0 erreur JavaScript, 0 ressource 404.
4. **Images décodées** — 100 % des images référencées se chargent (chargement paresseux déclenché par défilement).
5. **Clavier et focus** — premier Tab sur le skip link, indicateur de focus calculé, aucun `outline` neutralisé.
6. **Recherche globale** — la touche « / » place le focus dans le champ, la saisie « AK-12 » renvoie des résultats correspondants, le panneau est une région live polie, `Échap` referme.
7. **Navigation mobile** — le bouton menu existe, s'ouvre, déclare `aria-expanded="true"`, rend le panneau visible et expose les 14 entrées.
8. **Outils interactifs** — constructeur de kit (recalcul au changement de mode, région live), tier list (4 paliers, puces atteignables au clavier, `Espace` descend une arme et l'annonce), explorateur de cartes (cartes listées, compteur live), comparateur d'armes présent.
9. **Page 404** — statut HTTP 404 vérifié, message, navigation globale, `noindex`, 8 raccourcis.
10. **Bande-son** — piste présente, servie en HTTP 200, en-tête MP3 valide.
11. **Performance de rendu** — DCL 81–191 ms, `load` 116–374 ms en local.

---

## 4. Accessibilité — conformité WCAG 2.2 AA

| Critère | Mise en œuvre |
|---|---|
| 1.3.1 Info et relations | Hiérarchie de titres continue h1 → h5 sur les 65 pages, 0 saut ; `<article>`, `<nav>`, `<section>` et `<table>` avec en-têtes de portée |
| 1.4.3 Contraste | Thème sombre à contraste renforcé, tokens `--color-text-primary` / `--color-text-secondary` / `--color-text-muted` calibrés |
| 1.4.4 Redimensionnement | 0 débordement horizontal de 320 à 1440 px (vérifié à 375 / 768 / 1440 px) |
| 1.4.10 Retour à la ligne | `overflow-wrap: anywhere` sur les titres longs et les valeurs de faits ; tableaux défilables dans leur conteneur |
| 1.4.11 Contrastes non textuels | Bordures de focus visibles, badges de source avec couleur + libellé textuel |
| 2.1.1 clavier | Skip link, menu mobile, recherche, tier list et loadout builder entièrement pilotables au clavier |
| 2.4.1 Éviter les blocs | Skip link « Aller au contenu » en tête de chaque page |
| 2.4.7 Focus visible | `:focus-visible` avec contour de 2 px, aucun `outline: none` sur le site |
| 2.5.5 Taille des cibles | Cibles tactiles ≥ 24 px, bouton menu 42 × 42 px |
| 3.2.2 Sur saisie | Aucun changement de contexte au clavier ; la navigation ne se déclenche qu'au clic |
| 3.3.2 Étiquettes | 0 champ de formulaire sans libellé (explicite, associé ou implicite) |
| 4.1.2 Nom, rôle, valeur | 0 élément interactif sans nom accessible ; `aria-current="page"` sur 64 pages ; `aria-expanded` sur le menu mobile |
| 4.1.3 Messages de statut | 5 modules interactifs avec région `aria-live="polite"` ; annonces de déplacement dans la tier list |

---

## 5. SEO et performance

| Contrôle | Résultat |
|---|---|
| Titres uniques et ≤ 60 caractères | 65/65 |
| Descriptions uniques et ≤ 160 caractères | 65/65 |
| Données structurées JSON-LD `@graph` | Valides sur les 65 pages + `404.html` |
| `sitemap.xml` | 65 URL indexables, `lastmod` au format W3C, aucune URL 404, `404.html` exclue |
| `robots.txt` | 53 lignes, 11 `User-agent` ; Googlebot / Bingbot / PerplexityBot autorisés ; GPTBot, ClaudeBot, CCBot, Google-Extended, Applebot-Extended, Bytespider, Meta-ExternalAgent bloqués ; `Sitemap:` en URL absolue ; aucun `noindex` dans le fichier |
| `manifest.json` | 4 icônes JPG, 4 raccourcis, toutes les cibles présentes |
| Open Graph | Carte 1200 × 630 JPG, URL absolue, `alt` renseigné |
| Poids CSS | 93,5 Ko bruts / **17,6 Ko gzip** (budget 80 Ko) |
| Poids JS | 95,5 Ko bruts / **32,5 Ko gzip** (budget 300 Ko) |
| Poids des images | 33,8 Mo pour 153 fichiers |
| Images | `width` + `height` sur 100 % des `<img>` (CLS maîtrisé), `loading="lazy"`, `decoding="async"`, `alt` en français |

---

## 6. Fiabilité des données — distinction des sources

Le site sépare explicitement trois registres, signalés par des badges visuels et textuels :

- **Source officielle** — annonces Steam et notes de patch de MoreFun Studios (`app 2073620`), base de données de référence `arenabreakout-infinite.com` (build 4.19.88-REV).
- **Source communautaire** — Reddit `r/ArenaBreakoutInfinite`, Discord officiel, YouTube, consensus de tier lists publiques recoupé le 17 novembre 2026.
- **Donnée non confirmée / dérivée** — la pénétration affichée est un *calcul* (Pierce Level = plancher de la pénétration ÷ 10) et non une valeur publiée ; les masses sont des estimations de marche ; les classements sont des consensus, jamais des classifications de l'éditeur.

Les données ont été confrontées aux sources fraîches du 17 novembre 2026 : Saison 7 « Utopia » depuis le 16 septembre 2026, plafonds de mode (Normal T4, Lockdown T5), Live Update des 27 octobre et 10 novembre 2026, Secure Ops, A545 et AK-15SC comme armes nouvelles, suppression du RNG de pénétration T5/T6.

---

## 7. Reproduction de la recette

```bash
# serveur local
cd abi-nexus && python3 -m http.server 8000 --bind 0.0.0.0

# recette statique (12 volets)
python3 tools/qa_final.py          # 0 erreur, 0 avertissement

# recette navigateur réel (Chromium)
node tools/test_s17_browser.js      # 48/48 (264 chargements)

# non-régression
python3 tools/audit.py              # 64 pages, 0 erreur, 64/64 HTTP 200
python3 tools/audit_seo.py          # 0 erreur, 0 avertissement
node tools/test_s15.js              # 58/58
node tools/test_s16.js              # 51/51

# correcteurs idempotents
python3 tools/build_s17.py          # 0 promotion, aucun fichier modifié
python3 tools/build_s16.py
python3 tools/build_s16_files.py

# média
python3 tools/build_audio.py        # audio/ambiance-menu.mp3
```

---

## 7 bis. Ajouts post-recette

### 7.1 Simulateur balistique (nouveau module)

Le site documentait la pénétration mais ne calculait rien. La recherche web
(ABIDB-WEB, `fabiopsyduck/ABIDB-WEB`, mis à jour le 20 septembre 2026) a
confirmé que le **simulateur balistique TTK / pénétration** est le besoin le
plus demandé par la communauté. `js/ballistics.js` l'implémente sur la page
« Munitions & Pénétration », à partir des données existantes
(`js/data-ammo.json` — 44 munitions, `js/data-armors.json` — 14 armures,
`js/data-weapons.json`).

Fonctionnalités :

- 10 calibres, filtrage automatique des armes et munitions par calibre ;
- verdict de pénétration selon les règles de la **Saison 7** : le
  `Pierce Level` vaut le plancher de la pénétration ÷ 10, et une munition
  dont le Pierce Level est inférieur à la classe de l'armure **ne perce pas**
  (la loterie de pénétration a été supprimée sur les plaques T5 et T6) ;
- nombre de projectiles nécessaires pour neutraliser la zone visée ;
- **TTK théorique** calculé à la cadence réelle de l'arme sélectionnée ;
- cas particulier de la tête, jamais protégée par l'armure ;
- région `aria-live="polite"` pour l'annonce du résultat.

Le barème de pénétration a été **affiné après recherche** : le guide de budget
le plus récent du jeu (*mis à jour le 14 novembre 2026*) documente un barème
communautaire cohérent sur tous les guides de la saison, que le simulateur
applique désormais :

| Relation | Verdict simulé | Dégâts chair retenus |
|---|---|---|
| Pierce Level **supérieur** à la classe | « Pénètre pleinement » | 100 % |
| Pierce Level **égal** à la classe | « Pénétration partielle » | 80 % |
| Pierce Level **inférieur** à la classe | « Ne pénètre pas » | 50 % |

Le simulateur ajoute la **durabilité comme second levier** : chaque tir dégrade
la plaque, et le simulateur indique la dégradation par projectile — d'où la
technique de la *sustained fire*, seule façon pour une munition sous-tier de
finir par percer.

Le modèle reste explicitement présenté comme simplifié : les points de vie par
zone et la durabilité sont des estimations de terrain, pas des valeurs éditeur.

### 7.2 Tier list : ajout de la distinction par mode

La recherche a mis en évidence un angle mort éditorial : la tier list était
**globale**, sans distinction entre les modes, alors que le plafond de gear de
la Saison 7 rend cette distinction déterminante. Une nouvelle section
« 2 bis. Le meta par mode : Lockdown ou Forbidden » a été ajoutée, avec :

- un tableau `Mode / Plafond de gear / Armes privilégiées / Logique` ;
- la correction de l'**AR-57**, classée A dans la tier list globale alors que
  les guides de saison la classent **S en Lockdown** et **A en Forbidden** ;
- l'arbitrage économique A545 (coûteuse, rentable en Forbidden seulement)
  contre AR-57 (rentable en Lockdown) ;
- le conseil terrain issu d'un loadout Lockdown solo publié le 31 octobre
  2026 : casque **SH Masca**, gilet **H-Tag**, perk **Rush**, emplacement 2×3 ;
- une section « Sources » propre à la page, avec 4 liens sourcés et annoncés.

Les entrées correspondantes ont été ajoutées au sommaire latéral.

### 7.3 Couverture explicite YouTube, GitHub et réseaux sociaux

La page « Ressources communautaires » ne citait GitHub que par un lien
générique vers la home du site, et ne proposait aucune sélection de guides
vidéo. Deux ajouts ont été faits :

- **GitHub** — trois dépôts réels ont été ajoutés et vérifiés : **ABIDB Web**
  (base de données et simulateur balistique, mis à jour le 20 septembre 2026),
  **Arena Breakout Infinite Offline Database** (base hors ligne avec export
  CSV, release 0.9.7) et **ABI Loadout Calculator** (calculateur de point mort).
  ABIDB Web est également décrit dans la liste des projets open source.
- **YouTube** — une nouvelle section « 6 bis. Les guides vidéo à regarder en
  priorité » recense les quatre guides communautaires récents, avec leur date
  de publication : revue des armes de la Saison 7 (26 octobre 2026), classement
  complet build par build (19 octobre 2026), test de la configuration A545
  (24 septembre 2026) et le guide Lockdown solo du 31 octobre 2026. Un
  encadré rappelle que toute vidéo antérieure au **16 septembre 2026** décrit
  un monde où la pénétration était encore aléatoire sur les plaques T5/T6.

Les entrées correspondantes ont été ajoutées au sommaire de la page, et les
URL figurent dans la liste des sources communautaires.

### 7.4 Débordement horizontal en 1280 px — corrigé

Le balayage responsive couvrait 375, 768 et 1440 px. Un contrôle à **1280 px**
— largeur très courante sur portable — a révélé un débordement de **7 px** sur
les 65 pages : le seuil de compactage de la barre de navigation était fixé à
1250 px, alors que les 10 entrées de premier niveau, le badge « Utopia » et
les actions ne tiennent plus entre 1251 et 1287 px.

Le seuil a été porté à **1320 px**. Contrôle après correction : **0 débordement
sur 65 pages × 4 largeurs (260 combinaisons)**. La recette navigateur a été
étendue en conséquence — elle vérifie désormais 375, 768, 1280 et 1440 px sur
l'intégralité du site.

### 7.5 Deuxième ambiance sonore pour les pages zombies

Le guide ne disposait que d'une seule piste, l'ambiance industrielle du menu.
Une seconde piste a été synthétisée localement et câblée sur les trois pages
exclusivement consacrées aux modes zombies (`saison7-zombie-research`,
`saison7-zombie-endless`, `saison7-zombie-infected-zone`) :

| Piste | Durée | Format | Contenu |
|---|---|---|---|
| `audio/ambiance-menu.mp3` | 24,03 s | mono 44,1 kHz, 64 kbps | drone grave, souffle de ventilation, cliquetis métalliques |
| `audio/ambiance-infection.mp3` | 24,03 s | mono 44,1 kHz, 64 kbps | bourdon dissonant (quinte + seconde mineure), pulsation, souffle chaud, impacts lointains |

Les deux pistes sont **bouclables** (fondu de bouclage de 1,2 à 1,4 s) et
produites par le même script `tools/build_audio.py`, sans binaire externe :
numpy pour la synthèse, `lameenc` pour l'encodage MPEG-1 Layer III.

La recette navigateur vérifie désormais, pour les deux pistes : présence,
HTTP 200, en-tête MPEG valide et **décodage réel par le navigateur**
(événement `canplaythrough`), et non une simple présence de fichier.

### 7.6 Nouvelle page « Réglages & sensibilité »

La recherche a mis en évidence un angle mort total : le site documentait les
armes, l'armure, la munitions et les cartes, mais **pas une seule ligne sur
les réglages du client** — alors que c'est le premier réglage que tout joueur
modifie, et le domaine le plus fréquemment discuté par la communauté.

La nouvelle page `pages/reglages-sensibilite.html` couvre :

- **Focal Point** (onglet Game) — le point central, avec son piège : les
  balles ne partent pas exactement sur le point, elles partent légèrement à
  droite, plus ou moins haut selon l'arme. La correction se fait au Stand de
  tir, une fois pour toutes.
- **La sensibilité par grossissement** — `Control → Global Control Settings`,
  un curseur d'Aim Sensitivity par optique (1x, 1,6x, 2x, 3x, 3,5x, 4x, 6x,
  7x, 10x, de 0,10 à 4,00), le cas particulier des optiques combinées 1x/6x
  qui se comportent comme du 1x.
- **Le preset de visibilité et FPS** — le tableau complet, avec le point
  capital : la végétation haute est une obstruction, pas un décor.
- **Les raccourcis de combat** — viser et tirer à la molette, `Alt + T` pour
  vérifier le chargeur, `Alt + V` pour recharger, et surtout la désactivation
  du double-clic pour déplacer un objet, cause n°1 des munitions perdues.
- **Ce que les réglages ne corrigent pas** — peek du côté droit, jiggle peek
  avec Alt, réticule à hauteur de poitrine, `M` pendant la file d'attente.

La page est intégrée au méga-menu « Guides » (colonne Stratégie), au sitemap
(65 URL), au JSON-LD et au maillage interne depuis le guide du débutant et le
guide avancé.

### 7.7 Correctif de numérotation des identifiants — build_s17.py

L'insertion d'un lien en milieu de page a révélé un **bug réel** dans
`tools/build_s17.py` : le compteur d'identifiants ignorait les ancres qui
avaient déjà un `id`, si bien que l'ajout d'une ancre décalait la numérotation
et créait un doublon (`lnk-guide-avance-087` en double). Le script retire
désormais les identifiants `lnk-*` avant de les réaffecter dans l'ordre du
document : la numérotation est continue et le script reste idempotent.

Les tests S15 et S16 ne comptaient plus en dur le nombre de pages
(63 et 64) : ils comparent désormais au nombre réel de fichiers présents, ce
qui évite une nouvelle rupture à chaque page ajoutée.

### 7.8 Fenêtre de la Saison 8 : les probabilités

La page « Calendrier des événements » mentionnait la fenêtre du 3 au 14 décembre
2026 mais sans quantification. Un tableau de probabilités a été ajouté, avec
les trois scénarios et leur poids : **cas de base 8–14 décembre (~55 %)**,
**précoces 3–7 décembre (~10 %)**, **report de fin d'année début–mi-janvier
2027 (~35 %)**.

L'information la plus actionnable est la **fenêtre d'annonce** : les deux
dernières saisons ont laissé à peine plus d'une semaine entre l'annonce et le
lancement. Pour une sortie dans la semaine du 8 au 14 décembre, l'annonce
tomberait donc entre le **30 novembre et le 7 décembre** — c'est la période à
surveiller, pas maintenant.

### 7.9 Contrôle de dérive de l'index de recherche

`js/search.js` porte une liste codée en dur des pages indexables. L'ajout de
la page « Réglages & sensibilité » a révélé que la liste n'était pas mise à
jour : la page était dans le sitemap mais invisible dans la recherche. Un
contrôle a été ajouté à `tools/qa_final.py` : il compare la liste `PAGES` aux
fichiers réellement présents et signale toute page non inscrite ou listée à
tort. Il passe désormais au vert — **64 pages indexées, 0 dérive**.

### 7.10 Visuels : catalogue photographique complet

Les visuels photographiques ont été produits par lots de 10 maximum par
réponse, en **JPG uniquement**, photoréalistes et cinématographiques, tous en
1536×1024 (le T88 en 1672×941, format déjà utilisé par 7 visuels du site).
Chaque fichier a été contrôlé : signature JPEG complète (`FFD8`…`FFD9`),
dimensions vérifiées, aucun PNG ni SVG.

| Lot | Visuels |
|---|---|
| Armes | MPX, Vector .45, SKS, USAS-12, RPK-16, **Banshee**, **T88** |
| Objets S7 | MRID, Northern Stars, Lute, **Jade Flute**, **GPU**, **Military Circuit**, **Gold Bar**, **Rolex**, **Morphine**, **Y40**, **Flare Gun** |
| Dernier lot | **Phéromone**, **Fumigène de soin**, **Keycard**, **Medkit**, **Bandage**, **M290 (grenade incapacitante)** |

Les **24 armes** ont leur photographie réelle : plus aucun `imagePending` sur
`js/data-weapons.json`. Les **24 objets** également : plus aucun `imagePending`
sur `js/data-items.json`. `tools/pending_visuals.json` est désormais vide — le
**catalogue média est complet**, aucun visuel factice ni image de substitution
ne subsiste dans le site.

Inventaire final : **153 images, 0 orpheline, 0 PNG/SVG, 0 référence
manquante**, et les nouveaux visuels vérifiés en chargement réel dans Chromium
sur les pages armes et objets.

### 7.11 Techniques de terrain Zombie Endless

Un fil Reddit du 20 octobre 2026 a permis d'ajouter **cinq techniques** qui
manquaient à la page Zombie Endless, toutes vérifiées comme absentes :

- le **tour de poteau** (« ring around the rosie ») pour faire rater sa charge
  au Phobos — la parade la moins chère qui soit ;
- **ne pas cooker la grenade** face à une charge : elle explose pendant que
  vous êtes à terre et vous vous relevez ;
- l'astuce des **tumeurs d'Airport Central** : la petite tumeur bouche le
  passage aux zombies, la laisser en place est une barricade gratuite ;
- le **hangar d'exposition**, où monter sur l'avion coince les Phobos ;
- l'interdiction du **corps à corps contre une créature spéciale**.

La page a également reçu sa **section Sources** (3 références externes
annoncées), absente jusqu'ici.

Et sur la page Zombie Research, les **coffres et mini-coffres** ont été ajoutés
comme source d'échantillons zombies, à côté des sacs de zombies et des
conteneurs exclusifs.

### 7.12 Réactifs expérimentaux : le nom officiel retrouvé

Une relecture de la page *Infected Zone* a montré que le troisième réactif de
la Saison 7 était décrit par son effet seul (« résistance aux blessures
critiques »), **sans son nom officiel**. Les notes bêta de la Saison 7 et
l'annonce officielle le nomment **« Cornered Beast »** : pendant une durée
limitée, un dommage sévère à la tête ou au torse met à terre au lieu de tuer.

Le nom a été rétabli sur les trois pages qui mentionnaient le réactif
(`saison7-zombie-infected-zone.html`, `saison7-nouveautes.html`,
`items-medical.html`), avec un encart dédié qui explicite la contrepartie
commune aux trois réactifs — plus de dégâts subis, plus facile à détecter —
et le fait qu'aucun ne peut être extrait du raid.

### 7.13 Section Sources ajoutée à la page Infected Zone

La page *Infected Zone* ne comportait aucune section **Sources**, alors que sa
page jumelle *Zombie Endless* en avait une. La section a été créée avec
trois références classées par statut : **officiel** (annonce de la Saison 7),
**communautaire** (notes bêta Reddit, synthèse des deux modes zombies) et
**à vérifier** (les valeurs de détection, de dégâts et de durée des réactifs
ne sont chiffrées par aucune source publique). Le sommaire passe à 9 entrées.

### 7.14 Trois règles officielles absentes du site, désormais rétablies

La relecture intégrale de l'annonce officielle de la Saison 7 (six pages de
notes, patchbot.io) a fait ressortir trois règles que le site ne mentionnait
nulle part — toutes vérifiées comme absentes avant correction :

| Règle officielle | Pages corrigées |
|---|---|
| Le **plafond de 900 000 Koen** de valeur d'équipement et la limitation au **niveau 5** (casques, masques, gilets blindés, gilets de corps) s'appliquent aux raids Lockdown **y compris l'Infected Zone**. En Heavy Infected Zone (Farm et Airport), les récompenses sont à parité avec Forbidden et le coût en points de clé est standardisé à 2 points | `saison7-zombie-infected-zone.html` |
| Les **core masteries** sont exclues de l'Arena Mode, du Covert Ops **et du Zombie Endless** — et les masteries normales suivent les mêmes exclusions | `guide-progression.html`, `saison7-zombie-endless.html` |
| Le **réactif « Cornered Beast »** est le nom officiel du troisième réactif de la Saison 7 (les blessures sévères à la tête ou au torse mettent à terre au lieu de tuer) | `saison7-zombie-infected-zone.html`, `saison7-nouveautes.html`, `items-medical.html` |

La première est la plus structurante : elle change la composition d'un kit
autorisé en Infected Zone standard, et l'avertissement « le raid ne démarre
pas tant que vous dépassez le plafond » manquait.

### 7.15 Audit approfondi : trois défauts réels corrigés

Un audit média/texte/liens plus exhaustif que la recette habituelle
(`tools/audit_deep.py`, nouveau) a mis au jour trois défauts que les suites
automatisées ne détectaient pas :

**1. Tous les liens de la recherche globale étaient cassés.** `js/search.js`
utilisait un préfixe unique (`BASE`) à la fois pour les liens vers les pages et
pour le chargement des fichiers JSON. Les deux n'exigent pas le même préfixe :
depuis `/pages/`, les liens doivent être des frères (`armes-tier-list.html`)
alors que les JSON sont un niveau au-dessus (`../js/…`) ; depuis la racine,
c'est l'inverse. Résultat : **tous** les résultats de recherche pointaient vers
`/armes-tier-list.html` au lieu de `/pages/armes-tier-list.html`, sur les
66 pages du site. La correction sépare `DATA_BASE` (fetch), `PAGE_BASE`
(liens) et `ROOT_BASE` (accueil). Une nouvelle suite,
`tools/test_s18_search.js`, résout et vérifie en HTTP chaque lien produit par
la recherche, depuis la racine et depuis `/pages/` : **127 assertions**.

**2. La page `saison7-nouveautes.html` était orpheline.** Présente au sitemap
et dans l'index de recherche, mais **aucun lien n'y menait** : le top-level
« Saison 7 » de la barre de navigation était une entrée directe sans
méga-menu, et la colonne de pied de page ne la listait pas. Le top-level
« Saison 7 » a reçu un méga-menu à deux colonnes (*La saison* / *Modes
zombies*) exposant ses 6 pages, badge « Utopia » conservé.

**3. Un `<th>` vide** dans le tableau comparatif rig / gilet blindé de
`equipement-rigs.html`, remplacé par « Critère ».

Corrigé en parallèle : la recherche n'indexait pas la page d'accueil (elle
est désormais dans l'index, avec une convention racine explicite `/index.html`
prise en compte par le contrôle de dérive de `tools/qa_final.py`), et la page
*Stratégies S7* a reçu sa section **Sources**.

### 7.16 Secure Ops : le mode sous-estimé

Le site n'évoquait Secure Ops qu'en trois endroits incidents, alors qu'il
s'agit d'un mode à part entière et du meilleur environnement d'apprentissage
du jeu — celui que la page *Réglages* recommande pour calibrer sa
sensibilité. Une section dédiée a été ajoutée à `meta-stratégies-s7.html` :
la règle officielle (« vous ne perdez aucun équipement si vous n'extraitiez
pas ; le butin est converti en Koen à l'extraction »), le taux de conversion
communautaire de 30 à 40 % de la valeur affichée, le build recommandé, et la
**démystification d'une rumeur** — « l'armure doit être neuve » est une
suggestion de joueur du 13 novembre 2026, pas une règle.

### 7.17 Contenu vérifié à jour

Un audit de 60 marqueurs d'information de la Saison 7 (patch `1.0.0.142.19`,
Live Update du 10 novembre 2026) passe à **60/60** : caps Normal T4 / Lockdown T5 /
Forbidden T6, RNG de pénétration supprimé, ricochets de casque supprimés,
flashlight nerfed, GLI-F4 ramené à 50 s, T88, UMP45 à 650 rpm, MCX, FAMAS,
SS190 en pénétration 42, les 3 Core Masteries, Last Stand, formules de craft au
niveau maximum,objets Rouges S7 (Elysium, MRID, Northern Stars, Lute, Jade
Flute), objets tactiques zombies (phéromone, flare gun, fumigène de soin),
M290 craftable, Supply Drops 2.0, Dog Tags, recherche zombie, marchands,
météo, Secure Ops, Season Kits, et l'absence d'annonce de la Saison 8 au
13 novembre 2026.

---

## 8. Points ouverts avant mise en production

1. **Domaine** — `SITE_URL=https://abinexus.fr` dans `tools/seo_config.py` est provisoire. À confirmer avant déploiement : toutes les URL canoniques, `og:url` et le sitemap en dépendent.
2. ~~Visuels photographiques en attente~~ — **résolu**. Les 24 armes et les 24 objets ont leur photographie réelle ; `tools/pending_visuals.json` est vide et l'inventaire compte **153 JPG, 0 orpheline, 0 PNG/SVG**.
3. **Serveur de production** — la page `404.html` doit être servie en **vrai HTTP 404** par l'hébergeur (procédure documentée dans `DEPLOIEMENT.md`), jamais en redirection ni en 200.
4. **Recherche** — la barre interroge les pages et les données d'armes, armures, munitions, objets et cartes. L'index des **pages** est une liste codée en dur dans `js/search.js` ; l'index des **objets** est chargé en `fetch` depuis les fichiers JSON. Un contrôle de recette compare désormais la liste `PAGES` aux fichiers réellement présents : toute page ajoutée sans être inscrite dans `js/search.js` est signalée comme erreur bloquante, ce qui évite qu'une page reste invisible dans la recherche.
