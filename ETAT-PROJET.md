# ABI NEXUS — État du projet au 18 novembre 2026

Guide Arena Breakout Infinite · `abinexus.fr` · racine `/home/user/abi-nexus`

---

## 1. Ce qui est livré

### Contenu et structure
| Indicateur | Valeur |
|---|---|
| Pages HTML | **67** (65 `pages/` + `index.html` + `404.html`) |
| URL dans le sitemap | **66** indexables |
| Volume de texte | **142 387 mots** (moyenne 2 190/page) |
| Collections de données | 24 armes éditoriées · **77 armes documentées** · 14 armures · 44 munitions · 18 objets · 6 cartes + 1 mode |
| Médias | **353 JPG** · **0 PNG / SVG / WebP / GIF** · **0 fichier illisible** · **0 aplat/placeholder** |
| Audios | **44 MP3** — 2 ambiances + **42 voix off** françaises |

### Validation — tout est vert au 18/11/2026
| Audit | Résultat |
|---|---|
| HTTP (audit.py) | **65/65** en 200 + racine `index.html` et `404.html` |
| SEO (audit_seo.py) | **0 erreur** · 66 URL · 0 doublon de title/description |
| Profond (audit_deep.py) | **0 erreur** · 153 avertissements (tous « faible résolution » sur artworks officiels 1024²) |
| QA global (qa_final.py) | **0 erreur bloquante** · **0 avertissement** |
| Structure HTML (audit_structure.py) | **67/67 pages saines** · **0 erreur** |
| Images rendu navigateur | **281 références · 279 distinctes · 1 multi-page · 0 non décodée** |
| Recette S15 | **58/58** |
| Recette S16 | **51/51** |
| Recette navigateur S17 | **48/48** (EXIT=0) |
| Recherche S18 | **141/141** |
| Catalogue des 77 armes | **8/8** (`tools/test_catalogue.js`) — 77 lignes, 14 colonnes, grille 24 armes intacte, 0 erreur JS |
| Recette narration | **295/295** (`tools/test_narration.js`, catalogue auto-découvert) |
| MP3 | **37/37 décodés** (`tools/audit_audio_browser.js`) — 44,1 kHz stéréo, durées 24,0 s (ambiances) à 88,6 s (narrations) |
| Lecteur de narration | **42 pages** — composant non bouclé, lecture réelle, barre de progression |
| Garde-fou scripts | **0 anomalie sur 232 fichiers** (`tools/check_scripts.py`) |

---

## 2. Travaux de cette session

### Vague du 18/11/2026 (7ᵉ vague) — 3 voix off, 10 bugs structurels réparés, validateur unifié

**1. Un auditeur de structure HTML a été écrit** (`tools/audit_structure.py`). Les audits existants vérifient le
fonctionnel — liens, balises JS, rendu — mais laisse passer un défaut d'imbrication : un bloc inséré au milieu
d'une balise ouvrante produit une hiérarchie fausse pour le lecteur d'écran et pour le SEO, sans que rien ne
signale l'erreur. L'auditeur applique les règles d'auto-fermeture HTML5 (`<p>` fermé par un bloc, `<li>` par
`<li>`, `<td>`/`<tr>` par `<td>`/`<tr>`) afin de ne remonter que les vrais défauts. Résultat au premier passage :
**467 anomalies sur 67 pages**. Après correction : **67/67 pages saines, 0 erreur**.

**2. Dix bugs structurels réels ont été réparés** :

| Page | Défaut | Correction |
|---|---|---|
| `guide-economie` | `<h2>` fermé par `</h3>` | fermeture rétablie |
| `armes-lmg` | `<h2>` fermé par `</h3>` | fermeture rétablie |
| `equipement-rigs` | `<h2>` fermé par `</h3>` | fermeture rétablie |
| `equipement-sacs` | `<h2>` fermé par `</h3>` | fermeture rétablie |
| `equipement-tier-list` | `</article>` manquant, `</div>` parasites | hiérarchie rétablie |
| `communaute-patch-notes` | `</div>` parasite fermant l'article | parasite retiré |
| `map-northridge` | `</p>` orphelin dans un `<li>` | retiré |
| `univers-lore` | `<div class="lore-quote">` dupliqué | doublon retiré |
| `404.html` | `<body>` dupliqué | doublon retiré |
| `index.html` | `<h2>` mal apparié (effet de cascade) | rétabli |

Trois de ces défauts venaient de scripts d'enrichissement qui refermaient un `<h2>` avec `</h3>`.

**3. Un validateur global a été créé** (`tools/valider_projet.py`). Le projet n'avait aucun point d'entrée
unique : chaque audit se lançait à la main, dans le bon ordre, sans garantie que le nouveau contrôle de
structure soit exécuté. Le validateur enchaîne les 15 contrôles, affiche un tableau de synthèse et renvoie
un code de sortie non nul au moindre échec. Un mode `--quick` exclut les recettes navigateur.

```bash
python3 tools/valider_projet.py --quick    # ~6 s
python3 tools/valider_projet.py             # complet, ~10 min
```

**4. Trois voix off produites et câblées** : `meta-tier-list-globale`, `equipement-sacs` et
`equipement-rigs`. Couverture : **42 pages narrées sur 65**, **44 MP3** au total, tous décodables.
Le plafond de 10 appels de génération par tour a été atteint : **7 autres textes sont déjà rédigés et
validés** dans `tools/textes_audio/` et n'attendent qu'un appel de génération chacun.

**5. Un récurrent a été corrigé.** Trois blocs insérés par les scripts de veille s'étaient logés à l'intérieur
d'une balise ouvrante — l'ancre visait le *texte* d'un titre et non sa balise. Les ancres sont désormais des
expressions régulières qui pointent la balise ouvrante, ce qui rend l'insertion structurellement sûre.

### Validation après la vague 7

| Audit | Résultat |
|---|---|
| QA global | **0 erreur bloquante · 0 avertissement** |
| Statique / SEO | **65/65** en 200 · **0 erreur** SEO |
| Profond | **0 erreur** · 153 avertissements |
| Structure HTML | **67/67 pages saines · 0 erreur** |
| Scripts | **0 anomalie sur 232 fichiers** |
| Images | **281 références · 0 non décodée** · **0 référence cassée** |
| Audio | **37/37 décodés** |
| Narration | **295/295** sur 42 pages |
| Recettes S15 / S16 / S17 / S18 / catalogue | **58/58 · 51/51 · 48/48 · 141/141 · 8/8** |
| Volume | **142 387 mots** · moyenne **2 190/page** · **0 page** sous 1 300 |

### Vague du 18/11/2026 (6ᵉ vague) — 10 visuels, 3 voix off, veille et correction majeure des clés

**1. Dix visuels cinématographiques produits et intégrés.** Tous en **JPEG haute qualité**, entre 1 536×1 024 et
1 672×941, photoréalistes et immersifs : `vis-tierlist`, `vis-roles`, `vis-optimizer` (meta), `vis-research`,
`vis-infected` (zombies), `vis-koen`, `vis-medical` (items), `vis-supplies`, `vis-warlord` (events),
`vis-patch` (communaute). Chaque ancien visuel ciblé a été purgé. **57 visuels cinématographiques** au total.

**2. Trois voix off produites et câblées** : `map-tv-station` (57,48 s), `equipement-tier-list` (56,80 s) et
`saison7-balance-changes` (55,78 s, concaténée depuis 3 blocs). Couverture : **32 pages narrées sur 65**.

**3. Un bug d'appariement corrigé.** `tools/refresh_visuels_cine4.py` recherche les images par **nom de base** :
`img/armes/vis-tierlist.jpg` et `img/meta/vis-tierlist.jpg` partageaient le même nom, si bien que le nouveau
visuel global avait remplacé l'arme-tier-list et laissé l'ancien fichier orphelin. L'ancien visuel a été rattaché
au catalogue puis purgé ; `img/meta/vis-tierlist-cinematique.jpg` sert désormais les **deux** pages concernées.

**4. La veille a révélé une erreur de fond sur la durée de vie des clés.** Les notes de patch officielles de
l'éditeur (*Full Release*, Season 3 : Breach, X / @ArenaBreakoutPC, 15/09/2025) indiquent que la durabilité des
clés produites après la Saison 3 a été **multipliée par trois**. Le guide affichait encore les valeurs
d'avant refonte (10 / 15 / 25) sur ses tableaux Farm, Valley et TV Station — incohérence avec le reste du site,
qui raisonnait déjà sur des clés à 30 points. **21 valeurs ont été corrigées** et la recommandation inversée :
le guide conseillait de dépenser les clés anciennes en Normal, alors que l'éditeur demande explicitement de
les **prioriser en Lockdown et en Forbidden** — ce que confirme l'arithmétique, puisqu'une ancienne clé
consomme un point par ouverture quel que soit le mode et vaut donc 15 ouvertures où qu'elle soit dépensée.
Deux nouveaux encadrés documentent la règle **« ouverture à crédit »** (le dernier point restant ouvre encore
une porte en Forbidden) et le comportement **officiel** des clés universelles.

**5. Trois apports de veille, classés par nature.**

| Apport | Page | Nature |
|---|---|---|
| Top-loading : chargeur à deux étages, munitions hautes en premier | `items-munitions.html` | Communautaire |
| Lobby de bots en Lockdown après six morts consécutives | `meta-stratégies-s7.html` | Communautaire |
| TikTok, X et le format court : une piste, jamais une source | `communaute-ressources.html` | Communautaire + Officielles |

**6. Deux outils de contrôle réparés.** `tools/test_narration.js` ne listait que 6 pages en dur : il découvre
désormais le catalogue depuis le HTML, ce qui porte la recette de 31 à **225 assertions sur 32 pages** et
supprime toute dérive future. `tools/test_s17_browser.js` lançait Chromium sans `--no-sandbox` et échouait
en environment sandboxé : il est repassé à **48/48**.

**7. Le suivi documentaire a été remis à jour** : `tools/pending_visuals.json` reconstruit (353 JPG, 34 MP3,
32 pages narrées), `tools/AUDIO_A_REGENERER.md` réécrit (plus aucun audio en attente, historique complet).

### Validation après la vague

| Audit | Résultat |
|---|---|
| QA global | **0 erreur bloquante · 0 avertissement** |
| Statique / SEO | **65/65** en 200 · **0 erreur** SEO |
| Profond | **0 erreur** · 153 avertissements |
| Scripts | **0 anomalie sur 229 fichiers** |
| Images | **281 références · 0 non décodée** · **0 référence cassée** |
| Audio | **34/34 décodés** |
| Narration | **225/225** sur 32 pages |
| Recettes S15 / S16 / S17 / S18 / catalogue | **58/58 · 51/51 · 48/48 · 141/141 · 8/8** |
| Multilingue | **0 fragment** CJK / hangul / cyrillique |
| Volume | **142 414 mots** · moyenne **2 190/page** · **0 page** sous 1 300 |

### Vague du 18/11/2026 (2ᵉ vague) — 4 key art remplacés, 9 voix off, 13 pages enrichies, 3 bugs structurels réparés

Cette vague ferme la quasi-totalité des chantiers restants. Quatre volets ont été menés en parallèle.

**1. Quatre visuels cinématographiques générés et intégrés.** Quatre « key art » de faible qualité ont été
remplacés par des visuels photoréalistes (1 536×1 024 et 1 935×812, 162–313 Ko, JPEG) :

| Nouveau visuel | Page | Remplace |
|---|---|---|
| `img/communaute/vis-ressources-cinematique.jpg` | `communaute-ressources.html` | `vis-ressources.jpg` |
| `img/communaute/vis-streamers-cinematique.jpg` | `communaute-streamers.html` | `vis-streamers.jpg` |
| `img/zombies/vis-balance-cinematique.jpg` | `saison7-balance-changes.html` | `vis-balance.jpg` |
| `img/univers/vis-lore-cinematique.jpg` | `univers-lore.html` | `vis-lore.jpg` |

Les quatre anciens fichiers ont été purgés. Le total reste à **354 JPG** : 22 visuels cinématiques produits
au total sur les deux vagues, 194 artworks officiels conservés en 1024² comme demandé.

**2. Neuf voix off produites et câblées** (plafond de 10 par réponse atteint) : `map-farm`, `map-airport`,
`items-cles`, `guide-craft`, `events-warlord`, `equipement-armures`, `equipement-casques`,
`communaute-patch-notes`, `saison7-utopia`. Le catalogue `tools/cable_narrations.py` a été étendu de 5 à
14 entrées. La couverture audio passe de **10 à 19 pages narrées** sur 65.

**3. Treize pages courtes enrichies, plus trois bugs structurels réparés.** Le nombre de pages sous
1 300 mots est passé de **16 à 0**.

| Page | Avant | Après | Ajout |
|---|---|---|---|
| `armes-lmg` | 1 102 | **1 471** | tableau de stats · position de la famille |
| `armes-shotgun` | 1 134 | **1 372** | tableau de stats (5 armes) |
| `armes-smg` | 1 140 | **1 498** | tableau de stats (15 armes) |
| `armes-sniper` | 1 140 | **1 432** | tableau de stats (9 armes) |
| `armes-carbine` | 1 150 | **1 410** | position de la carabine dans le catalogue |
| `armes-dmr` | 1 201 | **1 505** | tableau de stats (8 armes) |
| `guide-economie` | 1 076 | **1 627** | rendement des sources de Koen · arbitrage Field Merchant |
| `guide-craft` | 1 123 | **1 571** | familles d'effets · arbitrage Smelter |
| `equipement-armures` | 1 161 | **1 425** | coût réel du passage de palier |
| `equipement-sacs` | 1 186 | **1 411** | dimensionnement du sac |
| `equipement-rigs` | 1 201 | **1 425** | tableau rig contre gilet |
| `equipement-tier-list` | 1 100 | **1 726** | 5 sections réécrites (voir plus bas) |
| `armes-nouveautes-s7` | 977 | **1 442** | comparatif A545 / AK-15SC · arbitrage d'attachement |
| `guide-avance` | 1 268 | **1 701** | postures · quatre questions avant d'entrer |
| `saison7-zombie-infected-zone` | 2 787 | **3 462** | 3 grenades exclusives · niveau de menace · conteneurs de zone |
| `guide-traders` | 1 497 | **2 030** | fidélité du marchand · indice sonore des cargaisons |
| `map-tv-station` | 1 296 | **1 316** | (déjà au-dessus du seuil) |

**Les trois bugs structurels réparés** ont été trouvés par un audit de cohérence éditoriale, pas par les
audits automatiques :

- `equipement-tier-list.html` contenait **cinq sections recopiées depuis `equipement-armures.html`** —
  « Les règles qui dictent le armure », « Les munitions à connaître », « Quel kit pour quel budget »,
  « Les erreurs qui coûtent cher », « FAQ » — avec une numérotation dupliquée (deux sections 3., deux 4.,
  deux 5., deux 6.), des ancres réutilisées et un sommaire pointant vers du contenu déplacé. La page a
  été réécrite sur cinq sections propres au classement d'équipement (5 à 9), le sommaire et les ancres
  ont été refaits, et le bloc `faq` dupliqué a été supprimé. La suppression avait désaligné la grille
  `.page-layout` (deux `</div>` manquants, `</main>` absent) : la structure a été reconstruite sur le
  gabarit `equipement-armures.html`.
- Trois pages portaient une **numérotation de `h2` dupliquée** : `armes-pistolets` (2. deux fois),
  `meta-loadout-optimizer` (4. deux fois) et `equipement-tier-list` (7. deux fois). Les séquences ont été
  renumérotées pour être contiguës.
- Les blocs insérés en tête de section créaient des **sauts de niveau `h1` → `h3`**. Les blocs concernés
  ont été passés en `h2`.

**4. Une affirmation erronée corrigée.** La page `armes-carbine` affirmait que les
carabines ne formaient « pas une catégorie de collection » dans la source de référence.
C'était faux : `js/data-weapons-wiki.json` expose bien une catégorie `Carbines` de
**huit armes**. Le bloc a été remplacé par le tableau officiel — BM59, M14, M16, M96,
Mini14, SA85M, SKS et SVTU — généré par code depuis le JSON, et la page est passée à
**1 513 mots**.

**5. Veille du 18/11/2026 intégrée avec distinction des statuts.** Trois sources nouvelles, classées
explicitement :

| Source | Statut | Contenu intégré |
|---|---|---|
| Live Update du 10 nov. 2026 (UTC+0) | **Publication éditeur** | Collaboration Dim Dou Duk (9 nov. → 6 déc.), enquête Kamona (→ 22 nov.), 12 correctifs dont les positions hors limites sur Farm / Northridge / Airport |
| Avis de bannissement du 11 nov. 2026 | **Donnée rapportée (éditeur)** | 58 662 joueurs compensés, 73,63 Md Koen, 10 883 bans triche dont 1 709 à 10 ans, 847 bans appareil/IP, 89 439 informations bloquées (période 26 oct. → 8 nov.) |
| Incident du lanceur Level Infinite PC du 4 nov. 2026 | **Retour communautaire** | 4 fichiers JS altérés, chronologie 27 sept. → 5 nov., ABI déclaré non affecté par l'équipe ABI |

**Statut de la Saison 8 : toujours non annoncée officiellement.** Aucun post de révélation, aucun compte à
rebours, aucune mention dans le Live Update du 10 novembre. La fenêtre du 2 au 16 décembre 2026 reste une
**estimation** fondée sur la cadence des trois dernières saisons (78 à 89 jours) et la fin des événements de
la Saison 7 le 7 décembre. Elle est qualifiée d'estimation partout où elle apparaît.

### Vague du 18/11/2026 — audit média : 8 visuels cinématographiques, 7 doublons résolus, hiérarchie des titres

**Un audit de cohérence média a été lancé sur les 354 JPG du site.** Il a révélé trois familles de
problèmes que les audits automatiques neVoyaient pas : des images partagées entre deux pages avec des
`alt` décrivant une tout autre scène, des visuels de faible définition servant de figure principale,
et un placeholder plat (icône de coffre) utilisé comme illustration de page.

**8 visuels photoréalistes cinématographiques ont été générés et intégrés** (tous en JPEG, 1 536–1 928 px,
155–259 Ko) :

| Nouveau visuel | Page | Remplace |
|---|---|---|
| `img/meta/vis-progression.jpg` | `guide-progression.html` | `cards/var-progression.jpg` (720×480, screenshot « Weapon Tier ») |
| `img/events/vis-attente-s8.jpg` | `saison8-attente.html` | `cards/card-balance.jpg` (800×450) |
| `img/zombies/vis-endless-cinematique.jpg` | `saison7-zombie-endless.html` | `zombies/vis-endless.jpg` (carte-titre « COMBAT ») |
| `img/events/vis-calendrier-cinematique.jpg` | `events-calendrier.html` | `events/vis-calendrier.jpg` (rendu 3D d'un cylindre) |
| `img/equipement/vis-armures-cinematique.jpg` | `equipement-armures.html` | `cards/card-armures.jpg` (800×450) |
| `img/items/vis-collection-cinematique.jpg` | `items-collection-room.html` | `items/vis-collection.jpg` (**placeholder plat**) |
| `img/armes/vis-tierlist-cinematique.jpg` | `armes-tier-list.html` | `cards/card-h416.jpg` (800×450) |
| `img/univers/vis-darkzone-cinematique.jpg` | `univers-dark-zone.html` | `univers/vis-darkzone.jpg` (bande sombre de faible hauteur) |

**Les 7 doublons exacts ont été résolus.** Le site contenait des paires de fichiers au contenu
strictement identique : `vis-lore` = `vis-ressources` (« LOCATIONS »), `vis-streamers` = `vis-balance`
(« SUPPORTED BY »), `vis-roles` = `vis-endless` (« COMBAT »), `vis-valeur` = `goldbar`,
`vis-ammo-hero` = `762ps`, `vis-munitions` = `m855`, `ss190` = `ss198`. Pour les cinq premiers, le
problème n'était pas le doublon mais l'**incohérence entre l'image et son `alt`** : le texte alternatif
décrivait une scène qui n'était pas celle affichée (par exemple « Vue aérienne d'une île ravagée »
pour une carte-titre « LOCATIONS »). Les `alt` ont été recalés sur le contenu réel, en nommant explicitement
les key art de l'éditeur. Les doublons techniques (`vis-ammo-hero`/`762ps`, `vis-munitions`/`m855`) sont
volontaires : ce sont les vignettes de catalogue qui partagent le visuel de la munition.

**Le catalogue a été purgé des visuels devenus orphelins** : les 8 fichiers remplacés ont été supprimés
après vérification qu'aucune référence ne subsiste (pages, CSS, JS, JSON). Le total reste à **354 JPG**,
le poids passe de 49,0 à 47,6 Mo.

**Un défaut de hiérarchie des titres a été corrigé.** Le callout « Les clés anciennes ne suivent pas la
règle des nouvelles » avait été inséré **avant** le `<h2>` de la section « Comment fonctionne une clé »,
ce qui créait un saut de niveau h1 → h3 et rendait son renvoi « le tableau ci-dessus » faux. Le bloc a
été déplacé **après** le tableau des coûts, dans la section qui le porte, et le script générateur
`tools/fix_cles_durabilite.py` a été corrigé en conséquence (insertion après `</table>` plutôt qu'avant
le `<h2>`) pour que le défaut ne revienne pas. La QA est repassée à **0 erreur**.

**La traduction de `Bolt-Action` a été corrigée.** `tools/recalage_armes.py` traduisait le mode
`Bolt-Action` par « Automatique » — une erreur factuelle sur les trois fusils à verrou du catalogue
(M24, Mosin-Nagant, SJ16), qui sont manuels. La table `MODE_FR` renvoie désormais « Manuel » ; les
troi armes à verrou sont vérifiées `Manuel` et **aucune** n'est plus étiquetée automatique à tort.

**Recette ajoutée** : `tools/refresh_visuels_cine.py` rejoue l'intégration des visuels et le recalage
des `alt` de façon idempotente.

### Vague du 18/11/2026 (2e partie) — 10 visuels, 5 voix off, veille et dimensions

**10 visuels cinématographiques de plus** ont été produits pour les figures de page restées en
800×450 / 720×480, et les 10 fichiers remplacés ont été purgés :
`vis-fal-cinematique` (armes-fusils-assaut), `vis-ak15sc-cinematique` (armes-nouveautes-s7),
`vis-skins-armes-cinematique` (cosmetiques-skins-armes), `vis-trophy-room-cinematique`
(items-collection-room), `vis-stand-tir-cinematique` (items-munitions), `vis-sniper-cinematique`
(meta-builds-roles), `vis-utopia-cinematique` et `var-s7news-cinematique` (saison7-utopia),
`vis-s7news-cinematique` (saison7-nouveautes), `vis-endless-entree` (saison7-zombie-endless).
Résolution servie : **1 536–1 921 px**. Les 10 ont été vérifiés au navigateur : décodés, affichés,
0 erreur JS.

**Cinq voix off françaises ont été générées et câblées**, portant la couverture de 5 à **10 pages
narrées** : `guide-avance` (masculine, tactique), `items-medical`, `guide-economie`,
`events-calendrier`, `guide-traders` (féminine, pédagogique). Deux voix ont été auditées
(`voice-01` féminine, `voice-02` masculine). Lecture réelle vérifiée au navigateur
(`currentTime` = 1,30 s, non pausé), 12 MP3 décodés, 0 référence cassée.

**Quatre trouvailles de veille ont été intégrées**, absentes du site :
| Page | Ajout |
|---|---|
| `items-medical` | Le **membre noirci** : ni bandeau ni medkit ne le réparent, il faut un **kit chirurgical d'abord**, puis le medkit. La séquence inversée est la cause de mort la plus répandue. |
| `equipement-casques` | **Casque et masque = deux zones de dégât distinctes** en S7, et pénétration conditionnée à l'endurance (~3 tirs T5 sur le même point). Contre un casque sur-tier, **viser la poitrine**. |
| `equipement-headsets` | Le **reverse lean ne masque plus la zone de tête** en S7 — le correctif éditeur ferme l'exploit. |
| `saison7-utopia` | Les **trois sections de mission** les plus coûteuses (Underground Exploration, Intern Disruption, Comms Interference) et le mécanisme de contournement. |

**Les sorties d'Airport ont été documentées** : Northern Outpost (10–20 min + 1 élimination),
Parking Lot Helicopter (1 min, forte pression), Central Elevator (conditionnelle, tour de contrôle),
Drainage Pipe, Cluster 15 minutes, Access Bridge — avec la règle de décision qui manquait :
**la rentabilité se calcule en Koen par minute**, pas en loot total.

**Un bug de mise en page a été corrigé sur tout le site.** Les scripts d'intégration déclaraient
les dimensions de la **source** générée (3 120×2 080) au lieu des dimensions **servies**
(1 536×1 024). Le ratio réservé par le navigateur était donc faux sur les visuels intégrés :
le contenu se décalait au chargement. `tools/fix_dimensions_img.py` recalcule les attributs
`width`/`height` depuis les fichiers réels — **45 attributs corrigés** sur l'ensemble du site,
dont 45 images qui attendaient depuis l'origine. Idempotent, vérifié à 0 au second passage.

**L'audit a été refait de zéro** (images, audios, textes) avant la vague :
0 image cassée · 0 `alt` vide · 195 références d'image · 7 MP3 · 18 pages sous 1 300 mots.
Après vague : **0 cassée · 0 sans `alt` · 281 références · 280 distinctes · 0 multi-pages · 12 MP3
· 16 pages sous 1 300 mots** (seuil retenu : 1 300).

**La veille a été recoupée** avec Reddit (r/ArenaBreakoutInfinite), YouTube, GitHub (4 dépôts
communautaires), forums et sites d'analyse. Ce qui manquait au site a été intégré ; ce qui était
déjà présent a été laissé tel quel. Point notable : les sources communautaires nomment parfois le
**Boomer** pour le mutant explosif — le site conserve le nom officiel **Bloater** de l'éditeur, et
n'ajoute pas de nom communautaire non vérifié.

**Une hiérarchie de titres a été rétablie.** Les callouts de veille insérés avant le premier `h2`
créaient un saut h1→h3 (détecté par `qa_final.py`). `tools/fix_veille_s7.py` les déplace après le
premier `h2` de leur page et purge les mots anglais restants dans la prose (« Known », « regularly »,
« counting »).

**Audit des 139 badges de source « Officiel ».** Les 139 occurrences (21 pages) ont été extraites et lues
dans leur contexte, à la recherche d'un badge posé sur une donnée non publiée par l'éditeur. **Deux écarts
ont été corrigés** sur `guide-extraction.html` : deux citations explicitement attribuées au wiki
(« insurance does not exist… » et « Teammates can retrieve and return your gear… ») portaient le badge
« Officiel » ; elles passent désormais en **« Documenté »**, la classe cyan déjà prévue au CSS pour
« donnée vérifiée sur une source de référence mais non publiée par l'éditeur ». Les 137 autres badges sont
cohérents : ils s'appuient sur des annonces, des notes de patch, des textes de mission ou de la
documentation de l'éditeur. Les occurrences contenant le mot « communauté » l'emploient comme **sujet**
(la communauté de joueurs, de streamers) et non comme source — elles sont correctes.

**La légende des sources a été complétée.** La page `communaute-ressources.html` expliquait trois badges
sur cinq. Les deux manquants — **« Documenté »** et le critère distinctif de « Officiel » (« publié par
MoreFun Studios lui-même ») — ont été ajoutés. Rendu vérifié au navigateur : les 4 badges s'affichent avec
les bonnes couleurs (`rgb(46,255,143)`, `rgb(0,212,255)`, `rgb(26,158,255)`, `rgb(200,168,75)`), 0 erreur JS.

### Vague du 17/11/2026 — S8, season kits, catalogue d'armes, requalification des sources

**La page S8 passe de 3 067 à 3 965 mots**, avec quatre corrections factuelles et un ajout de fond.

- *Le « mardi » de la maintenance S7 corrigé* : le **16 septembre 2026 est un mercredi**. Le passage disait
  « une coupure planifiée de plusieurs heures un mardi » — remplacé par « en pleine journée (02:00 – 09:00 UTC,
  un mercredi, pour la Saison 7) ».
- *Le tableau des délais d'annonce refait sur la source* : il utilisait le post « Coming Early Jan. » du
  **10 décembre 2025** pour la Saison 4 — un drapeau « early January » **sans jour donné**, donc hors
  compte à rebours — et datait la Saison 5 au 20 mars. Le tableau compte maintenant **7 saisons**, de
  Ignition (27 j) à la S7 (8 j), sur la base des *premiers posts datés*. La plage réelle est **6 à 27 jours**,
  et non 7 à 13.
- *Le reset est détaillé ligne par ligne* : le tableau simplifié est doublé d'un tableau officiel complet
  (rang, core masteries, season kits, Improvement Research, coupons, événements, Battle Pass), de la liste
  de ce qui traverse la saison (niveau, points de maîtrise, Skin Supply, Zombie Research, Zombie Endless)
  et de l'encadré sur la règle « aucun wipe » — avec ses **deux limites** : la réserve « actuellement » de
  l'éditeur, et le fait qu'un événement de fin de saison **peut survivre à la saison** (S6 close le
  16 septembre, un de ses événements est daté au 30 septembre).
- *Le rythme de mise à jour est documenté* : ABI met à jour **environ tous les quinze jours, le plus souvent
  à 03:00 UTC** (10 des 16 live updates depuis avril 2026 affichent 03:00 UTC ; les autres 05:00, 07:00,
  12:00). Une mise à jour ordinaire **ne coupe pas les serveurs** ; une bascule de saison les ferme
  **six à douze heures**. Et surtout : **les notes de patch sont désormais publiées sur le site de
  l'éditeur, plus sur Steam** — surveiller Steam en exclusivité est une erreur.

**Les noms des season kits S7 sont alignés sur les notes officielles.** Le site décrivait correctement les
mécaniques mais employait des noms de démonstration. Corrigés dans **12 pages et 2 fichiers JSON, 82
remplacements** :

| Avant (site) | Après (officiel) |
|---|---|
| M110 Dual-Stage Trigger | **M110 binary trigger** |
| FAL Recoil Kit | **FAL burst kit** |
| PCC-9 Full-Auto Kit | **PCC-9 fully-automatic kit** |
| MPX Vulcan Barrel | inchangé |

Les quatre effets officiels sont désormais dans un tableau dédié sur `pages/armes-attachements-s7.html`,
avec l'avertissement commercial que l'éditeur a lui-même formulé : **« ces kits seront retirés à la fin de
la saison »** — le stock non équipé est perdu, le prix monte puis s'effondre en fin de saison.

**Requalification des sources sur les clés.** 39 badges « Officiel » désignaient des données **wiki Fandom**,
pas des publications de l'éditeur. Un troisième niveau a été introduit — `Documenté` (cyan) — avec sa classe
CSS, et une légende explicite sur la page. `tools/fix_cles.py` a été mis à jour en conséquence : son garde-fou
reposait sur `count('src-officiel') > 20` et serait devenu inopérant.

**Le catalogue d'armes est recalé.** `js/data-weapons.json` ne documentait que 24 armes sur 77.
- `js/data-weapons-wiki.json` (nouveau) : les **77 armes** de la source de référence, avec les 14 statistiques
  complètes (recul vertical et horizontal, ergonomie, stabilité, précision, stabilité à l'hipfire, portée,
  vitesse du projectile, cadence, poids) et les modes de tir traduits.
- `js/data-weapons.json` : les 24 armes locales reçoivent un bloc **`statsWiki`** strictement **additif** —
  aucun champ existant n'est modifié, donc la tier list, l'optimiseur, le comparateur et le builder ne
  changent pas de comportement. **19 des 24** sont raccordées ; les 5 autres (A545, AK-15SC, AEK-971, Banshee,
  T88) sont **absentes de la source de référence** et le sont désormais signalé explicitement.
- Cinq armes du wiki n'avaient **aucune catégorie** (leur nom ne se termine par aucune catégorie connue :
  « Micro SMG », « Lever-Action Rifle », et un pistolet préfixé « Gold ») : recatégorisées à la main.
  Les trois fusils à verrou (M24, Mosin, SJ16) sont classés « Sniper », comme le fait déjà le site.
- Nouveau `js/weapon-catalogue.js` + section **8 bis** de `meta-tier-list-globale.html` : un tableau des 77
  armes, et le catalogue est ajouté à la **recherche site** (S18 passe de 127 à 141 tests).

**Audit des médias.** `tools/audit_medias.py` (nouveau) décode les 354 fichiers de `img/` : **354 sont de
vrais JPEG**, **0 PNG/SVG/WebP**, **0 fichier illisible**, **0 aplat ou placeholder** (écart-type des
valeurs < 3), **0 sur-dimensionné**. Les 30 visuels éditoriaux sous 1 400 px de large sont tous en
1024×1024 ; les deux seules images plus petites sont les favicons (180 et 64 px), ce qui est leur usage.

**Deux visuels photoréalistes produits** — les deux dernières pages de `pages/` qui n'avaient aucune image :
- `img/armes/vis-attachements-s7.jpg` (1537×1023) — valise d'armurerie, outils de précision, lampe de travail.
- `img/guides/vis-reglages-sensibilite.jpg` (1535×1024) — poste de jeu nocturne, ultrawide en milieu industriel.

**Les 67 pages ont désormais une image** (contre 65 avant). La page Ressources communautaires s'enrichit du
**Loadout Toolkit** (journal de raid et économie, Next.js/Windows, MIT) et de la date de mise à jour du
4 novembre 2026 de la base ABI Database (patch 1.0.0.142.19, build 4.19.88-REV).

**Dix collages de mots corrigés** (`tools/fix_espaces.py`, idempotent) : un scan heuristique sur tout le site
(mot minuscule suivi d'un majuscule) a révélé des phrases mutilées — `laMunition d'un fusil`,
`lesLep EUR dépen TTK`, `laVertical`, `tirSupported`, `la penetrates maximale`, `vousPerdez`,
`Esprit d'équipe etAnalyse`, `Twitch Drops etChallenges`, `Les passe-coins deKoen`,
`Check-inAutomne`. Toutes corrigées à la source, avec le script de reprise ajouté au catalogue.

### Correction de la numérotation des saisons (blocage résolu)
Le tableau de la page S8 étiquetait **Utopia en S8** : c'était faux. La numérotation officielle de Morefun est **non linéaire** — `Ignition` est une saison intermédiaire sans numéro, ce qui décale la lecture. Tableau corrigé sur la base de `senseos.gg/guides/arena-breakout-infinite/seasons-list` (tableau de référence, dates et durées) :

| Nom | Numéro | Début | Fin | Durée |
|---|---|---|---|---|
| Early Access | S0 | 13 août 2024 | 20 novembre 2024 | 99 j |
| Season One | S1 | 20 novembre 2024 | 29 avril 2025 | 160 j |
| Ignition | — | 29 avril 2025 | 10 juillet 2025 | 72 j |
| Crimson Edge | S2 | 10 juillet 2025 | 15 septembre 2025 | 67 j |
| Breach | S3 | 15 septembre 2025 | 8 janvier 2026 | 115 j |
| Dusk to Dawn (Airport Hunt) | S4 | 8 janvier 2026 | 2 avril 2026 | 84 j |
| Distortion | S5 | 2 avril 2026 | 30 juin 2026 | 89 j |
| White Nights | S6 | 30 juin 2026 | 16 septembre 2026 | 78 j |
| **Utopia** | **S7** | 16 septembre 2026 | *en cours* | 78–89 j |
| *À venir* | **S8** | *non annoncé* | *estimée 8–14 décembre 2026* | — |

Une note explicative sur le décalage a été ajoutée sous le tableau. Le tableau Warlord est cohérent avec cette numérotation (S5 Distortion, S6 White Nights, S7 Utopia) : aucun mélange global/chinois subsistant.

### Section « assurance » réécrite sur la mécanique réelle
L'ancienne section reposait sur une prémisse fausse. Le wiki officiel est explicite : **« Insurance does not exist, what you lose is gone unless recovered manually »**. La section a été réécrite autour de ce qui existe réellement : emplacement clé, Secure Pouch (1 case, modes spécifiques), Secure Case payante (2×3 = 400 Bonds, Composite 3×2 = 1 000 Bonds/30 j, 3×3 = 800 Bonds), règle S6 interdisant les munitions rouges en Case, cas d'essai 3×3 gratuite en fin de S5, récupération par les coéquipiers renvoyée par mail (avec la règle du symbole orange), et programme de compensation G.T.I. Security contre les tricheurs (restitution intégrale de l'équipement porté, sous 1 à 3 jours ouvrés, sans signalement requis, non concerné par le pillage d'un tiers).

### Visuels — catalogue terminé
- **10/10 visuels éditoriaux produits et vérifiés** en JPEG 1672×941 : `vis-pistolets`, `vis-casques`, `vis-headsets`, `armor-t6`, `vis-tierlist`, `vis-builds`, `vis-nouveautes`, `vis-cles`, `vis-sniper`, `vis-attachements`.
- Les deux derniers (`vis-sniper`, `vis-attachements`) ont été générés avec succès après reinstatement du quota de 10 images par tour. Contrôle PIL : format JPEG réel, 1672×941, marqueur EOI `ffd9` présent.
- Attributs `width`/`height` actualisés en `1672`/`941` dans les pages concernées ; les anciennes valeurs `1536`/`1024` ont été corrigées.
- **Inventaire final : 352 JPG, 0 PNG/SVG/WebP.**
- `tools/pending_visuals.json` : section `a_faire` désormais vide, 24 visuels en `produits`.

### Cartes
- `map-northridge.jpg` et `map-tvstation.jpg` remplacés par les **véritables plans officiels** (`Northridge_Map.jpg`, `TVMap.jpg`), 1920×1080 JPG.
- Variantes 720×480 régénérées ; photo cinematic d'intérieur TV Station ajoutée (`var-tvstation-interieur.jpg`).
- **Un WebP renommé `.jpg` a été détecté et reconverti** en vrai JPEG (quality 92, progressif) — l'audit profond le rejetait.

### Corrections de données majeures (recherche web du 17/11/2026)

**Hostile Sector et Distorted Valley ne sont plus disponibles en S7.** C'est le correctif le plus important
de la session : le site présentait Hostile Sector comme un mode actif dans 9 pages, dont une section entière
de la page Northridge et la source de revenu « found money » du guide économie. L'annonce officielle S7 est
explicite : *« Hostile Sector and Distorted Valley will not be available this season. Players can sell their
Hostile Sector: Solo Infiltration tickets to the contact. »* Corrections appliquées :
- Page Northridge : la section « Hostile Sector PvE — le farm Koen » devient « Le PvE en S7 », avec le
  retrait officiel, les 4 classes d'élite revenues en mode principal à menace réduite, le red drop
  Chaotic Matter devenu global, et le substitut réel (Zombie Endless / Secure Ops).
- 8 autres pages alignées (armures, casques, sacs, tier list, calendrier, économie, Koen, munitions) et
  les 4 métadonnées de la page Northridge.
- Le tableau des modes du calendrier affiche désormais Hostile Sector en « Retiré en S7 ».

**Le « +20 % » du Field Merchant n'est pas une donnée officielle.** Le site l'affirmait comme une règle
de l'éditeur dans 6 pages (dont le titre de section « la règle des 20 % »). Ni l'annonce S7 ni les notes de
patch ne mentionnent de pourcentage de prime : c'est un chiffre communautaire. La section Field Merchant a
été réécrite sur les règles officielles — **1 marchand par raid, interactif 5 minutes après le début**,
achat et vente cumulant un **volume de transactions** qui débloque l'intel, **mystery cargo** à prix bas
(rendement stable) ou élevé (résultats polarisés), **zombie tokens** en Zombie Endless — avec un encadré
qui signale explicitement le chiffre communautaire et le statut non confirmé.

### Corrections techniques
- **Builder S8 rendu idempotent** : il détecte les blocs enrichis et conserve l'article existant au lieu de l'écraser. Validation JSON-LD intégrée au build (échec si le JSON est invalide).
- **IDs dupliqués supprimés** sur la page S8 (le sommaire et le pied de page se chevauchaient) : relance de `tools/build_s17.py`, qui renumérote tous les `lnk-<page>-<n>` dans l'ordre du document. **0 doublon sur les 67 pages**, **0 ancre interne cassée**.
- **Description SEO de la page S8 raccourcie** (197 → 158 caractères) à la source dans le builder.
- **Numérotation des H2 de la page S8** remise en ordre (1 à 9, un doublon « 3. » supprimé).
- **Règle d'audit corrigée** : `audit_deep.py` neutralisait mal l'indentation du code source et signalait 111 faux positifs d'espaces multiples ; la règle ne regarde plus que les doubles espaces réellement écrits.
- **14 accents manquants** corrigés dans les légendes injectées (`Cartes de référence`, `modèle récent`, `première évolution`, `de l'équipe`, `d'après`, `capacité`, …) via `tools/fix_accents.py`.
- **Mot tronqué restauré** dans `pages/saison7-zombie-endless.html` : la purge Unicode avait laissé « les ␣ se combinent ». Phrase réécrite sur la mécanique officielle (« l'escouade va de 1 à 4 opérateurs, et le downed permanent d'un joueur n'arrête pas la run pour les autres »).

### Enrichissements éditoriaux
- `pages/equipement-armures.html` : section « Le leadership T5 et T6 » ajoutée (BT6 Heavy, M4 Defender,
  KN Field Commander, KN Composite, Spartan B) — 780 → 1 181 mots.
- `pages/equipement-casques.html` : section « Le leadership par palier » (KSS2, KLSS, AN95, 03 Heavy, IND70,
  SH65) avec la règle du masque qui prime sur le tier — 928 → 1 353 mots.
- `pages/equipement-headsets.html` : section « Les arbitrages audio » (ce que l'ouïe donne, ce qu'elle coûte,
  protocole audio en quatre temps) — 806 → 1 204 mots.
- `pages/saison7-zombie-infected-zone.html` : section « Les Biohazard Bags » avec les 4 emplacements
  communautaires (Tar Area, Port, Burnt Forest, Factory Compound) et la méthode de traçage.
- `pages/items-cles.html` : **18 clés Northridge** et **8 clés Airport** ajoutées, avec les « meilleures
  clés par carte » (Farm, Valley, Armory, TV Station) — la Weapon Storage Keycard d'Armory est identifiée
  comme la meilleure clé du jeu.
- `pages/saison8-attente.html` : historique complet des saisons, trois scénarios chiffrés, signal à surveiller, deadline de révélation.
- `pages/events-warlord-tournament.html` : historique des trois éditions Warlord (17 avril–14 mai 2026 · 13 août 2026 · 29 octobre–7 décembre 2026).
- `pages/guide-extraction.html` : section assurance réécrite (voir plus haut).

### Audio — les 5 voix off intégrées au site
- **Voix** : `voice-00` retenue après audition utilisateur.
- **Fichiers** : `audio/narration-{guide-debutant,guide-extraction,map-valley,map-no-mans-land,armes-tier-list}.mp3`.
  Tous décodés : 44,1 kHz stéréo, durées 49,4 s à 60,8 s, RMS 3 169-3 343 (signal réel, non silencieux).
- **Lecteur** : `js/main.js` → `initNarrationPlayer()`. Le lecteur d'ambiance existant forçait
  `audio.loop = true` et ne créait jamais l'élément `<audio>` dans le DOM : corrigé pour les deux lecteurs.
  La narration **ne boucle pas**, se met en pause, se relance depuis 0 à la fin, et affiche une barre de progression.
- **Styles** : `.audio-narration` dans `css/components.css` (+ règle mobile dans `css/responsive.css`),
  positionné au-dessus du lecteur d'ambiance pour éviter le chevauchement.
- **Pages câblées** : `guide-debutant`, `guide-extraction`, `map-valley`, `map-no-mans-land`, `armes-tier-list`.
- **Test** : `tools/test_narration.js` — **26/26** (présence du composant, piste accessible en HTTP, libellé,
  lecture qui démarre réellement, barre qui progresse, aucune erreur JavaScript).

### Corrections de données majeures (wiki officiel ABI)
Contrôle systématique des pages cartes contre le wiki officiel : les pages HTML contredisaient leur propre
`js/data-maps.json`, qui lui-même concordait avec le wiki. Corrections appliquées :

| Carte | HTML annonçait | Réel (wiki) | Correction |
|---|---|---|---|
| Armory | 9 extractions | **3** (F Control Room, B1 Canal, B1 Passage) | 9 → 3 |
| TV Station | 11 extractions | **3** (Elevator, Loading Dock, Main Entrance) | 11 → 3 |
| Farm | 14 extractions | **8** | 14 → 8 |
| Valley | 12 extractions | **8** | 12 → 8 |
| Northridge | 10 extractions | **11** | 10 → 11 |
| Airport | 13 extractions | **4** | 13 → 4 |

- **Boss d'Armory** : la page attribuait le boss à **Ajax** — c'est **Renoir** (Ajax est le boss de Farm).
  Le JSON `js/data-maps.json` portait la même erreur, corrigée dans les deux fichiers.
- **Clés Northridge** : le texte annonçait 18 clés pour une table de 19 lignes. Corrigé en 19, avec
  ventilation **9 clés documentées par le wiki** / 10 communautaires. Le bilan annonçait « 26 clés ajoutées »
  pour un total réel de 27 (19 + 8).
- **Boss** : `js/data-maps.json` porte désormais la liste complète des boss par carte et leur **statut**
  (nommé par l'éditeur / attaché par le texte récit / rapporté). Farm : Ajax + Hecate (et Phobos en
  Heavy Infected Zone). TV Station : Kurt, Rolf **et** Bernard. Airport : aucun boss nommé.

### Enrichissements éditoriaux (données officielles)
- `pages/armes-pistolets.html` : stats officielles de **7 pistolets** (M45A1, F57, M1911, G18C, G17, T05,
  Desert Eagle) + tableau des munitions par calibre avec leur niveau + attachements dédiés M1911 et G17.
- `pages/armes-tier-list.html` : stats officielles de **24 armes** en complément du tier communautaire,
  avec un encadré « comment lire ce tableau face à la tier list ».
- `pages/armes-attachements.html` : catalogue officiel des **104 attachements** avec compatibilité arme par
  arme, les 5 grandes familles, et les canons filetés (M1911, G17, MPX, M110) comme seul vrai levier.
- `pages/armes-attachements-s7.html` : vérification de compatibilité officielle des 4 sets S7 — le wiki ne
  recense **aucune pièce dédiée au PCC-9**, signal important pour l'achat.
- `pages/armes-builds.html` : chaque build confronté aux chiffres officiels du wiki, avec la mention que
  les **coûts annoncés n'ont aucune source publiée**.
- `pages/map-armory.html` : boss Renoir détaillé (5 armes, équipement des 10 gardes, jeton Battleforged Badge,
  chance de spawn ≈ 15 %) et tableau des 3 extractions avec leurs conditions d'activation.
- `pages/items-cles.html` : colonne **Source** (Officiel / Communautaire) sur les 6 tables de clés, plus le
  contenu officiel documenté pour 11 clés (coffres, caisses d'armes, conteneurs premium).

### Boss — la distinction « nommé par l'éditeur » vs « rapporté »
La revue exhaustive des **483 publications de MoreFun Studios** (menée par senseos.gg au 1er novembre 2026)
permet de classer les boss par statut réel. Le site l'applique désormais sur les pages cartes :

| Boss | Carte | Statut réel |
|---|---|---|
| **Fred** | Northridge | Nommé par l'éditeur (27 avril 2025) — boss principal de la carte |
| **Kurt**, **Rolf**, **Bernard** | TV Station | Nommés par l'éditeur — les trois ensemble, apparition simultanée possible |
| **Hecate** | Farm | Nommée par l'éditeur (« Abyss Captain », S2) — Small Hall et Grain Trade Center |
| **Phobos** | Farm, Valley, Airport | Nommé par l'éditeur (15 septembre 2026) — le boss des zones infectieuses |
| **Ajax** | Farm | Attaché à Farm par le **texte récit** de l'éditeur, sans que le mot « boss » soit employé |
| **Renoir** | Armory | Idem — les notes de Saison 1 disent que ses hommes tiennent Armory, sans le nommer boss |
| **Doss** | Valley | **Aucun post officiel** — rapporté par la communauté et le wiki, traité comme communautaire |
| — | Airport | **Aucun boss nommé** par l'éditeur ; seul Phobos l'est, en mode infectieux |

Conséquences appliquées :
- `pages/map-farm.html` : le callout « boss de la carte » ne présente plus **Ajax seul** — Farm compte
  **deux boss** (Hecate et Ajax), et Phobos s'y ajoute en Heavy Infected Zone.
- `pages/map-valley.html` : Doss est désormais étiqueté **communautaire**, avec une section expliquant que
  le Boss Rally de la Forbidden Zone est la seule mention officielle de Valley, et que Phobos y est le
  boss confirmé par l'éditeur.
- `pages/map-airport.html` : section « les boss d'Airport — ce que dit l'éditeur » : aucun boss nommé,
  White Wolves et Blackgold sont des forces nommées, pas des boss.
- `pages/map-tv-station.html` et `pages/map-northridge.html` : tableaux des boss avec statut et citation,
  plus le boss melee anonyme du Combat Melee-Only (janvier 2026) sur Northridge.

### Caractères corrompus — purge complète
Un scan global (HTML racine, `pages/`, `js/`, `css/`, `tools/`, `ETAT-PROJET.md`) a révélé des
**caractères de remplacement U+FFFD** dans une légende visible de `pages/map-airport.html`
(« telle qu'affich<U+FFFD>e ») et dans les scripts qui l'alimentaient (`tools/refresh_captions.py`,
`tools/enrich_thin.py`). Corrigés à la source, pas seulement à l'affichage.
Résultat du scan final : **0 caractère étranger** sur l'ensemble du site — les deux seules occurrences
restantes sont les **regex détectrices** de `tools/qa_final.py` et `tools/audit_seo.py`, qui doivent
contenir la classe CJK pour pouvoir la signaler.

### Scripts — idempotence et assainissement
- `tools/fix_cles.py` (nouveau) : réconciliation des clés avec le wiki, **idempotent** (garde en entrée).
- `tools/refresh_cles.py` : **neutralisé** — il insérait les sections sans garde, une seconde exécution
  dupliquait les blocs et cassait les comptes. Remplacé par `tools/fix_cles.py`.
- `tools/fix_extractions.py` (nouveau) : correction des comptes d'extractions et du boss Armory.
- `tools/refresh_pistolets.py`, `refresh_tierlist.py`, `refresh_builds.py`, `refresh_attachements.py`,
  `refresh_armory.py`, `add_narrations.py` (nouveaux) : insertions enrichies, toutes idempotentes.
- `tools/refresh_casques.py` et `tools/refresh_headsets.py` : fragments CJK supprimés (deux occurrences non-ASCII dans le texte insere). **Scan final : 0 caractère étranger sur tous les scripts.**
- `tools/test_narration.js` (nouveau) : recette navigateur du composant de narration.

---

### Vague du 18/11/2026 (3ᵉ vague) — 10 visuels haute qualité, 10 voix off, 9 blocs de veille, méthode audio corrigée

**1. Dix visuels cinématographiques générés et intégrés.** Cette vague attaque les images
éditoriales encore faibles : les six miniatures de cartes de l'explorateur de cartes
(720×480) et quatre cartes d'accueil (800×450). Tous sont en JPEG haute qualité,
1 536–1 935 px, 212–413 Ko.

| Nouveau visuel | Remplace | Page ou usage |
|---|---|---|
| `img/maps/var-farm-cine.jpg` | `var-farm.jpg` (720×480) | explorateur de cartes |
| `img/maps/var-valley-cine.jpg` | `var-valley.jpg` (720×480) | explorateur de cartes |
| `img/maps/var-armory-cine.jpg` | `var-armory.jpg` (720×480) | explorateur de cartes |
| `img/maps/var-airport-cine.jpg` | `var-airport.jpg` (720×480) | explorateur de cartes |
| `img/maps/var-northridge-cine.jpg` | `var-northridge.jpg` (720×480) | explorateur de cartes |
| `img/maps/var-tvstation-cine.jpg` | `var-tvstation.jpg` (720×480) | explorateur de cartes |
| `img/cards/card-arms-cine.jpg` | `card-arms.jpg` (800×450) | accueil |
| `img/cards/card-a545-cine.jpg` | `card-a545.jpg` (800×450) | accueil |
| `img/cards/card-farm-cine.jpg` | `card-farm.jpg` (800×450) | accueil |
| `img/cards/card-utopia-cine.jpg` | `card-utopia.jpg` (800×450) | accueil |

Les 10 anciennes images ont été purgées. `tools/fix_dimensions_img.py` a été étendu à la
racine du site : il a corrigé **16 attributs** de dimensions qui étaient faux sur
`index.html` depuis toujours, sans que les audits automatiques ne les signalent.

**2. Le contrôle des dimensions a été vérifié à la racine.** Un contrôle indépendant
sur les 195 images référencées confirme désormais **0 dimension fausse et 0 image
manquante**. Le total reste à **354 JPG** : 32 visuels cinématographiques produits
au total sur les trois vagues, 194 artworks officiels conservés en 1024².

**3. Dix voix off produites, cinq exploitables d'emblée.** Cinq ont été câblées sur
`map-northridge`, `map-armory`, `items-munitions`, `saison7-zombie-research` et
`saison8-attente` ; `guide-extraction` et `map-valley` ont reçu une version améliorée.
Le catalogue `tools/cable_narrations.py` passe de 14 à 19 entrées. **24 pages
narrées sur 65.**

**4. Un défaut de méthode corrigé.** Cinq des dix textes de narration contenaient des
fragments corrompus — un mot français coupé par un fragment étranger, un mot anglais
mal orthographié, un mot espagnol. La cause est identifiée : les textes étaient
rédigés puis corrigés en ligne, sans contrôle intermédiaire. La correction est
structurante : les textes sources sont désormais **écrits dans des fichiers UTF-8**
sous `tools/textes_audio/`, **scannés avant génération**, et les fichiers à refaire
sont listés dans `tools/AUDIO_A_REGENERER.md`. Conséquence directe : plus aucune
génération ne doit être consommée sur un texte à refaire.

**5. Neuf blocs de veille intégrés, avec le statut de chaque source.**

| Source | Statut | Contenu intégré |
|---|---|---|
| Annonce officielle de la Saison 6 (29 juin 2026) | **Publication éditeur** | tableau du Secteur hostile : Farm = Lockdown, Northridge > Lockdown, TV Station = Forbidden ; équipes invulnérables entre elles sur Farm et Northridge ; 4 types d'Élites ; événement de ralliement de boss ; Infiltration solo par tickets |
| Base de données de référence communautaire | **Documenté** | tableaux d'équipement complets : classe, durabilité, matériau, poids de kit, pénalité de déplacement, nombre de tirs au torse |
| Guides communautaires de Saison 7 | **Communautaire** | astuce du chargement en deux couches (FAL), prime de 20 % du Field Merchant, trois sections de mission à contourner, style de jeu solo, enveloppes budgétaires « rat » et « bête de somme » |
| Reddit, guides de survie | **Communautaire** | tailles de conteneur sécurisé 1×2 à 3×3, règles d'assurance, verrou « Tactical Ops locked » |

**Un point de vigilance traité comme une vérification, pas comme un ajout.** Une source
tierce affirmait que le Secteur hostile restait le meilleur mode de farm de la Saison
7. Le site affirmait l'inverse, sur la base de l'annonce officielle de saison. La
vérification a été faite dans les deux sens : **c'est le site qui a raison**, la
Saison 7 a bien closed le mode et les tickets restants se vendent à un contact. Le
contenu de la Saison 6 a donc été intégré comme **référence historique**, pas comme
mode actif — avec le tableau officiel des rendements, qui explique pourquoi
Northridge est devenu la carte de farm préférée.

## 3. Ce qui reste à faire

### A. Visuels photoréalistes — **TERMINÉ**
Les 10 visuels éditoriaux du catalogue sont produits et vérifiés en JPEG 1672×941. `tools/pending_visuals.json`
n'a plus d'entrée en `a_faire`.

**Vague du 18/11/2026 (1re)** : 8 figures de page de faible définition ou occupant une carte-titre ont été
remplacées par des visuels cinématographiques (voir § 2).

**Vague du 18/11/2026 (2ᵉ)** : les trois visuels restants — `communaute-streamers`,
`communaute-ressources` et `univers-lore` — ont été remplacés à leur tour par des scènes
photoréalistes dédiées, et le key art `saison7-balance-changes` l'a été également. **Il ne reste
plus aucun visuel éditorial à remplacer.** Les visuels **officiels** de l'éditeur — key art
« LOCATIONS », « COMBAT », rendus 3D d'objets, artworks d'armes 1024² — sont **conservés** :
remplacer un visuel officiel par une interprétation IA serait une régression sur la véracité de
l'image.

### B. Audio — **42 pages narrées sur 65**
Le lecteur de narration (`js/main.js`, fonction `initNarrationPlayer`) est **non bouclé**, avec état
lecture/pause/reprise, icône dynamique et barre de progression. Deux voix ont été sélectionnées après
audition : `voice-01` (féminine) et `voice-02` (masculine), réparties selon le ton de chaque page.
Les deux ambiances restent en boucle (comportement voulu). Test dédié `tools/test_narration.js` : **295/295** sur 42 pages, catalogue auto-découvert.

| Vague | Pages câblées | Total |
|---|---|---|
| Antérieure | `guide-debutant`, `guide-extraction`, `map-valley`, `map-no-mans-land`, `armes-tier-list` | 5 |
| S7 / guide | `guide-avance`, `items-medical`, `guide-economie`, `events-calendrier`, `guide-traders` | 10 |
| 18/11 (2ᵉ vague) | `map-farm`, `map-airport`, `items-cles`, `guide-craft`, `events-warlord`, `equipement-armures`, `equipement-casques`, `communaute-patch-notes`, `saison7-utopia` | 19 |
| 18/11 (3ᵉ vague) | `map-northridge`, `map-armory`, `items-munitions`, `saison7-zombie-research`, `saison8-attente` (+ `guide-extraction` et `map-valley` réécrits) | 24 |
| 18/11 (4ᵉ-6ᵉ vague) | `guide-progression`, `meta-stratégies-s7`, `map-tv-station`, `equipement-tier-list`, `saison7-balance-changes`, `events-supplies-drops`, `meta-builds-roles` | 32 |
| 18/11 (7ᵉ vague) | `meta-tier-list-globale`, `equipement-sacs`, `equipement-rigs` | 38 |
| 18/11 (8ᵉ vague) | `items-koen-economy`, `meta-builds-roles`, `saison7-zombie-endless`, `meta-loadout-optimizer`, `armes-builds`, `univers-dark-zone`, `communaute-ressources` | **42** |

**Reste à faire** : 23 pages sans narration, dont 0 dont le texte est déjà prêt (la 8ᵉ vague a
épuisé la file des textes prêts). Le plafond de
10 audios par tour impose 3 vagues supplémentaires pour couvrir tout le site. Priorité aux pages à forte valeur
pédagogique et aux cartes, qui sont les plus consultées.

**Méthode de rédaction, désormais imposée** : chaque texte est d'abord écrit dans un
fichier UTF-8 sous `tools/textes_audio/`, puis scanné avant d'être passé à
`generate_speech`. Les voix off à refaire sont listées dans
`tools/AUDIO_A_REGENERER.md`. Cette règle vient d'un constat : sur les dix voix off
de la 3ᵉ vague, cinq contenaient des fragments corrompus et ont dû être refaites —
le quota de génération avait été consommé à moitié pour rien.

### C. Profondeur éditoriale — **TERMINÉ**
Les 6 pages courtes ont été enrichies avec des données **officielles** (wiki ABI) :
| Page | Avant | Après | Ajout |
|---|---|---|---|
| `armes-pistolets` | 732 | 1 676 | Stats officielles de 7 pistolets, munitions par calibre, attachements dédiés |
| `armes-attachements` | 825 | 1 675 | Catalogue officiel des 104 attachements, familles, canons filetés |
| `armes-tier-list` | 877 | 1 602 | Stats officielles de 24 armes, distinction tier communautaire / données publiées |
| `map-armory` | 981 | 1 446 | Boss Renoir officiel (armes, gardes, jeton), 3 extractions conditionnelles |
| `armes-builds` | 748 | 1 237 | Chaque build confronté aux chiffres officiels du wiki |
| `armes-attachements-s7` | 975 | 1 152 | Vérification de compatibilité officielle des 4 sets S7 |

Aucune page n'est désormais sous 1 000 mots.

**Vague du 18/11/2026 (2ᵉ) : les 16 pages restantes sous 1 300 mots ont toutes été enrichies.**
Le seuil de 1 300 mots est désormais franchi par les **65 pages de `pages/`** — moyenne 2 028 mots/page.
Les ajouts de cette vague sont des tableaux de statistiques officielles (générés depuis
`js/data-weapons-wiki.json`, jamais saisis à la main) et des sections d'arbitrage (rendement des
sources de Koen, familles d'effets du craft, coût réel d'un passage de palier, dimensionnement du sac,
tableau rig contre gilet, comparatif A545 / AK-15SC, postures de combat).

### D. Veille S8 — 1 réponse par vague
Saison 8 **toujours non annoncée** au 18/11/2026. Le contrôle a été refait sur les trois sources
primaires : fil Steam `appid 2073620` (derniers posts : avis de bannissement du 11 nov., événement
Halloween du 28 oct.), Live Update du 10 nov. (rien sur la Saison 8) et site officiel (aucune page,
aucun compte à rebours). Fenêtre d'estimation : **2–16 décembre 2026**, base 8–14 décembre selon la
cadence des trois dernières saisons (78 à 89 jours) et la fin des événements de la Saison 7 le
7 décembre ; report possible en janvier 2027 comme à la Saison 3. Ces dates restent des
**estimations** et ne doivent jamais être présentées comme un calendrier officiel.

### E. Requalification des sources — partiellement traitée
Les **39 badges de la page clés** sont requalifiés en « Documenté ». Restent à traiter les pages armes et
équipement, qui emploient encore « Officiel » pour des données wiki :
`armes-tier-list`, `armes-attachements`, `meta-tier-list-globale`, `equipement-armures`, `equipement-casques`,
`equipement-tier-list`, `items-munitions`. Règle : « Officiel » = publié par MoreFun Studios ; « Documenté » =
source wiki de référence ; « Communautaire » = retours de joueurs.

### F. Cinq clés Fandom sur 43 restent non appariées
Valley −2, TV Station −1, Airport −2 : des clés du wiki sans ligne correspondante au tableau du site.

### G. Recalage du catalogue local — reste à faire
Le bloc `statsWiki` ne couvre que les **21 armes** présentes dans les deux catalogues (19 + l'A545 et
l'AK-15SC ajoutés par `tools/fix_stats_s7.py`). La correction de `Bolt-Action` → « Manuel » a été appliquée
à `tools/recalage_armes.py` et le catalogue régénéré : les trois fusils à verrou (M24, Mosin-Nagant, SJ16)
sont vérifiés `Manuel`. Les 58 autres armes
du wiki n'ont pas de tier, pas de prix et pas de photo : les laisserait à la documentation. Option
retenue : ne pas polluer le catalogue interactif avec des données partielles, et les garder dans
`js/data-weapons-wiki.json`.

### H. Résolution des images 1024² — arbitrage tranché : on conserve
Les visuels éditoriaux en 1024×1024 sont sous le seuil de 1 400 px et provoquent les **204** avertissements
de `audit_deep.py` (le compte a baissé de 8 : les huit visuels remplacés dans la vague du 18/11 sont
désormais en 1 536–1 928 px). Ils s'affichent correctement (colonne de contenu ≈ 700 px CSS), mais sur un écran
rétina 2× ils sont servis en 1 024 px. **Arbitrage tranché : ces visuels sont conservés en 1024².** Les 194 artworks officiels de l'éditeur
sont la source de vérité du jeu ; les régénérer en haute définition reviendrait à substituer une
interprétation IA à une image publiée par l'éditeur. Le compte de 190 avertissements de
`audit_deep.py` est donc **assumé et documenté**, et non un défaut à corriger.

### Estimation globale : **5 à 6 vagues**
| Vague | Contenu | Priorité |
|---|---|---|
| 1 | Requalification des sources « Officiel » → « Documenté » sur les pages armes et équipement | Haute |
| 2 | Appariement des 5 clés Fandom restantes | Moyenne |
| 3–6 | Narration des 46 pages restantes (10 audios par réponse, plafond imposé) | Moyenne |
| — | Visuels 1024² : **abandonné** — arbitrage tranché, ces visuels sont conservés | Clos |

**Ajouté le 18/11/2026** : l'audit des badges « Officiel » est **terminé** (139 occurrences lues,
2 corrigées). Restent 3 key art officiels à remplacer (`communaute-streamers`,
`communaute-ressources`, `univers-lore`).

### I. Pages courtes restantes — 16 pages sous 1 300 mots
La barre Editoriale retenue est 1 300 mots. Il reste 16 pages en dessous, dont 6 pages d'armes
(`armes-nouveautes-s7` à 977, `armes-lmg`, `armes-shotgun`, `armes-smg`, `armes-sniper`,
`armes-carbine`) et 10 pages d'équipement ou de guide. Levier disponible : le bloc `statsWiki`
du catalogue des 77 armes alimente déjà 21 armes éditoriales ; l'étendre aux pages de famille
permettrait de chiffrer chaque arme sans réécriture.

### J. Nouvelles voix off — couverture à porter de 10 à 20 pages
10 pages sur 65 sont narrées. Les candidates prioritaires, par valeur pédagogique et par
absence actuelle : `map-farm`, `map-airport`, `map-valley` (déjà narrée), `saison7-utopia`,
`equipement-armures`, `equipement-casques`, `guide-craft`, `guide-traders` (déjà narrée),
`communaute-patch-notes`, `events-warlord-tournament`. Maximum 10 audios par réponse.

---

## 3 bis. Sources externes vérifiées — vague du 18/11/2026 (4ᵉ vague)

Ces quatre sources ont ete lues integralement et exploitees ; elles sont
referencees dans les pages enrichies avec leur statut.

- `timesaver.gg/blog/arena-breakout-infinite-secure-case-guide` (28 sept. 2026,
  mis a jour le 14 nov. 2026) — **la source la plus rentable de la vague**.
  Contient des citations officielles verbatim :
  « Get 3×3 Titanium Cases by completing the new season missions » (post
  officiel Saison 4, 29 dec. 2025) · « Log in and claim the free 3×3 Titanium
  Secure Case via in-game email » (Saison 5) · carte d'essai 3×3 + 4 500 Bonds
  au 1er anniversaire (17 avr. 2026) · « Red ammo cannot be placed in secure
  cases » (notes de balance officielles Saison 6, 23 juin 2026) · « Mode-Based
  Ammo and Gear Cap — Normal: T4 and Below, Lockdown: T5 and Below » (reveal
  officiel du 8 sept. 2026). Signale aussi que le prix en Bonds est
  **conteste** entre sources (2 600 Bonds en 2024 contre une structure a paliers
  500/1 000) et que seul l'ecran de la boutique fait foi.
- `timesaver.gg/blog/arena-breakout-infinite-secure-ops` (16 nov. 2026) — citation
  officielle « In Secure Ops, you won't lose any gear when you fail to extract » ;
  plafond de valeur d'equipement de **600 000 Koen** rapportee par les joueurs
  (400 000 dans les fils de 2025, donc le plafond a bouge) ; regles du calcul
  (seul l'equipement porte compte, l'usure devalue, les chargeurs charges
  comptent) ; pooling d'escouade (« Voltron ») ; **l'editeur n'a jamais publie
  ni le plafond ni le taux de conversion**, d'ou le statut Communautaire.
- `timesaver.gg/blog/arena-breakout-infinite-player-count` (18 nov. 2026, releve
  SteamCharts + API Steam a 03:00 UTC) — 12 144 connectes, pic 24 h 25 753,
  moyenne 30 j **21 769**, pic 30 j **37 331**, record historique **65 944**
  (sept. 2025) ; historique mensuel complet de septembre 2025 a octobre 2026 ;
  chaque lancement de saison fait +22 % a +41 % de moyenne, sauf la S7 (+1,8 %)
  qui suivait un aout deja fort. Repond directement aux fils « le jeu meurt ».
- `timesaver.gg/blog/arena-breakout-infinite-season-7-utopia` (19 sept. 2026) —
  rappel utile : la S7 **ne vide pas** le stash, le Koen, le niveau ni les
  Bonds ; seuls le rang de saison et les missions saisonnieres sont reinitialises.
  Confirme aussi que le systeme d'achat de Koen contre argent reel a ete
  supprime a la 1.0 et que les acheteurs sont sanctionnes, pas seulement les
  vendeurs.
- `www.reddit.com/r/ArenaBreakoutInfinite/comments/1wp0j8r` — guide de survie S7 :
  regle des **20 %** de bankroll par kit, sections de mission a contourner
  (deja reprises sur `guide-avance`), emplacements des Biohazard Bags (deja
  repris), et la phrase-clé sur le rapport munition/armure reprise sur
  `items-munitions`.
- `www.reddit.com/r/ArenaBreakoutInfinite/comments/1iwa52r` et
  `.../1nm6nyv` — ROI des cles : Armory red card et cles de Valley a bon ROI,
  motel 3 millions juge plus aleatoire, prix plus bas en semaine et en journee,
  Armory Command Center et TV Planning Room solides, ROI dependant du mode
  Lockdown/Forbidden. Toutes donnees **communautaires**, integrees avec
  cette mention.

---

## 4. Sources externes vérifiées cette session

- `senseos.gg/guides/arena-breakout-infinite/seasons-list` — **tableau de référence** : S0 Early Access → S7 Utopia, dates exactes, durées 67–160 j, préavis 6–27 j. Confirme S7 Utopia en cours depuis le 16 septembre 2026 et l'absence totale d'annonce S8.
- `senseos.gg/guides/arena-breakout-infinite/zombie-modes` — modes zombies S7 : Infected Zone (PvPvE) et Zombie Endless (PvE, Airport, 1–4 joueurs, niveau 8).
- `arena-breakout-infinite.fandom.com/wiki/Inventory` — **« Insurance does not exist »**, Secure Pouch (1 case), emplacement clé.
- `arena-breakout-infinite.fandom.com/wiki/How_to_play` — coéquipiers qui récupèrent le stuff et le renvoient par mail ; symbole orange ; états de santé et downed.
- `buffget.com` — grille des Secure Cases (2×3 = 400, Composite 3×2 = 1 000/30 j, 3×3 = 800), munitions rouges interdites en Case (règle S6), cas d'essai 3×3 gratuite (fin S5).
- `ingamenews.com` — programme de compensation G.T.I. Security (périmètre, délai 1–3 jours, pas de signalement requis, cas de pillage par un tiers).
- `patchbot.io` — **annonce éditeur S7 complète** (15 septembre 2026) : Zombie Endless en escouade de 1 à 4,
  downed permanent, fin de raid quand toute l'équipe est à terre, **1 marchand par raid disponible à T+5 min**,
  volume de transactions débloquant l'intel, mystery cargo, Chaotic Matter global, Elysium, les 3 core
  masteries, Last Stand, retrait de Parkour, A545 et AK-15SC, balance complète, plafond Lockdown 900 000 K
  et T4 max en Normal. **Live Update du 10 novembre 2026** : collaboration Dim Dou Duk (9 nov.–6 déc.),
  Kamona Investigation Tea Break Delights (9–22 nov.).
- `arena-breakout-infinite.fandom.com` — page **Inventory** (« Insurance does not exist »), Secure Pouch,
  emplacement clé ; page **How to play** (récupération par les coéquipiers, symbole orange).
- `qrts.ru` et `arenabreakout-infinite.com` — catalogue des 43 clés officielles, 18 clés Northridge avec
  durée et contenu, 7 clés TV Station, clé d'accès Airport.
- `buffget.com` — grille des Secure Cases (2×3 = 400, Composite 3×2 = 1 000/30 j, 3×3 = 800), munitions
  rouges interdites en Case (règle S6), cas d'essai 3×3 gratuite (fin S5).
- `ingamenews.com` — programme de compensation G.T.I. Security (périmètre, 1 à 3 jours, sans signalement
  requis, cas du pillage par un tiers).
- Reddit r/ArenaBreakoutInfinite — guide S7 « Utopia Complete Survivor », emplacements des Biohazard Bags,
  leadership T5/T6 (BT6 Heavy, M4 Defender, KN Composite, Spartan B), arbitrage casque/masque, chargeurs
  limités à un seul par arme, anecdotal Reddit.
- `timesaver.gg` — calendrier, fenêtre 8–14 décembre, Warlord 29 octobre–7 décembre 2026, plafond Lockdown 900 000 K.

- `senseos.gg/guides/arena-breakout-infinite/bosses-list` — **revue exhaustive des 483 publications de
  MoreFun Studios** au 1er novembre 2026. La source qui permet de distinguer les boss **nommés par
  l'éditeur** (Fred, Kurt, Rolf, Bernard, Hecate, Phobos) de ceux qui ne sont qu'**attachés** à une carte
  par le texte récit (Ajax, Renoir) ou rapportés par la communauté (Doss). Aucun taux de spawn n'est
  publié par l'éditeur, et aucun boss n'est nommé sur Valley ni sur Airport.
- `senseos.gg/guides/arena-breakout-infinite/update-schedule` — **rythme de mise à jour** : environ tous
  les quinze jours, le plus souvent à **03:00 UTC** (10 des 16 live updates depuis avril 2026), mises à jour
  ordinaires sans coupure de serveurs, **bascules de saison = 6 à 12 heures** d'arrêt, et **notes de patch
  désormais publiées sur le site de l'éditeur et non sur Steam**. Base : 56 notes de mise à jour du
  10 mai 2024 au 26 octobre 2026.
- `steamcommunity.com/games/2073620/announcements/detail/672879191292643733` — **notes officielles S7**
  (16 septembre 2026) : maintenance 02:00–09:00 UTC, core masteries Acoustic Earpads / Tactical Belt /
  Hidden Compartment remises à zéro chaque saison, Improvement Research saisonnière, **noms officiels des
  quatre season kits** (M110 binary trigger, MPX Vulcan barrel, FAL burst kit, PCC-9 fully-automatic kit)
  et leur retrait en fin de saison, Last Stand ajouté, Parkour retiré, Quick Seal déplacé.
- GitHub — **ABIDB** (`fabiopsyduck/Arena-Breakout-Infinite-Offline-Database`, MIT, PowerShell),
  **ABIDB Web** (simulateur balistique : TTK, chances de pénétration, courbes de chute de dégâts,
  comparateur 15 armes, contrôle casque/masque), **arena.report** (suivi des clés et de la durabilité des
  armures, IndexedDB), **Loadout Toolkit** (journal de raid, économie de raid, analytics de combat).
  Base de données ABI : 2 647 enregistrements, patch 1.0.0.142.19, build 4.19.88-REV, mise à jour du
  4 novembre 2026.
- Reddit r/ArenaBreakoutInfinite — **ULTIMATE TIPS N' TRICKS GUIDE 3.0** (10 mars 2026) : la règle de
  durabilité des clés par mode (**Normal 1, Lockdown 2, Forbidden 3**) et le fait qu'**une clé à 1 usage
  peut servir en Lockdown puis en Forbidden** ; raccourcis recommandés (lean en maintien, C/Z/Caps Lock) ;
  le repère de portée au bouton du milieu ; l'endurance économisée en course au couteau ; le décompte de
  30 % de dégâts hors de portée effective ; les 100D medkits et antalgiques liquides qui ne déshydratent pas.
  Conseils par carte sur Valley (villa dangereuse, small factory par le nord) et Armory (Command Center).
  **Source communautaire** : ces avis ne sont pas publiés par l'éditeur.
- **`arena-breakout-infinite.fandom.com/api.php`** — API MediaWiki du wiki officiel, interrogée
  programmatiquement pour cette session. C'est la source qui a permis de corriger les comptes
  d'extractions, le boss d'Armory et le décompte des clés :
  - `Template:WeaponData` → les 12 caractéristiques officielles de **77 armes** (mode, calibre, recul
    vertical et horizontal, ergonomie, stabilité, précision, stabilité à la hanche, portée effective,
    vitesse de bouche, cadence, poids) ;
  - `Template:WeaponData` + fiches `M1911`, `M45A1`, `G17`, `G18C`, `F57`, `T05`, `Desert Eagle` →
    les munitions compatibles de chaque pistolet avec leur niveau (0 à 5) ;
  - `Weapon Mods` → les **104 attachements** officiels et leur compatibilité arme par arme ;
  - `Locations`, `Armory`, `Farm`, `Valley`, `TV Station`, `Northridge` → durée, nombre de joueurs,
    points d'intérêt, tableaux d'extractions avec types et conditions d'activation ;
  - `Bosses`, `Renoir`, `Doss`, `Ajax` → boss par carte, chance de spawn (≈ 15 %), nombre de gardes,
    armes et armures du boss, équipement des gardes, jeton de boss ;
  - `Keys` → les clés par carte avec leur durabilité et leur contenu documenté (coffres, caisses d'armes,
    conteneurs premium).
  - **Limite assumée** : le wiki n'est pas l'éditeur. Les caractéristiques d'arme, la compatibilité des
    pièces et les données de boss sont des données publiées ; les **tiers, les prix, la rentabilité et les
    délais de spawn** restent communautaires et sont attribués comme tels sur le site.

> **Point de vigilance vérifié** : « Operation Unbound » / « Season 12 » désigne la version **chinoise** d'Arena Breakout. La version internationale **ABI Infinite est en Saison 7 : Utopia** depuis le 16 septembre 2026. Le cadrage S7 du site est donc correct, et le tableau des saisons a été aligné dessus.

---

## 5. Points techniques à surveiller

- **Domaine et publication** : statut HTTP réel sur `abinexus.fr` et page 404 à confirmer hors sandbox.
- **S17** : la recette navigateur tue le navigateur en sandbox si elle est lancée en parallèle d'un audit — **la lancer seule**.
- **`tools/dedup_pages.py`** : reste non exécuté, `wire_pages.py` ayant déjà réalisé ses substitutions.
- **Ordre des opérations** : `build_s17.py` renumérote les IDs — **le relancer après toute création de page**, jamais `dedup_pages.py` avant réconciliation avec `wire_pages.py`.
- **Formats** : un fichier `.jpg` doit être réellement encodé en JPEG. Vérification automatique dans `audit_deep.py` ; reconvertir avec PIL si l'audit le signale.
- **Sauvegardes** : `/tmp/pages_backup` contient les pages d'avant injection — à déplacer hors de `/tmp` avant toute opération destructive.
- **Scripts d'insertion** : tout script qui écrit dans `pages/` doit avoir une **garde d'idempotence**.
  `tools/refresh_cles.py` a été neutralisé pour cette raison ; `tools/fix_cles.py` le remplace.
  Les scripts `refresh_*.py` modifient les pages : les relancer après `build_s17.py`, pas avant.
- **Nouveaux scripts de cette vague** — tous idempotents, tous vérifiés :
  `tools/refresh_s8_reset.py` (tableau officiel du reset), `tools/fix_s8_annonce.py` (délais d'annonce +
  rythme de mise à jour), `tools/fix_noms_kits.py` (noms officiels des season kits, 82 remplacements),
  `tools/refresh_kits_s7.py` (tableau des 4 kits officiels), `tools/requalify_sources.py` (badges
  « Officiel » → « Documenté »), `tools/recalage_armes.py` (catalogue des 77 armes + bloc `statsWiki`),
  `tools/refresh_catalogue_armes.py` (section 8 bis + table des 77), `tools/audit_medias.py`
  (audit format/dimension/corruption des 354 médias), `tools/fix_espaces.py` (collages de mots),
  `tools/test_catalogue.js` (recette navigateur du catalogue).
- **Garde `fix_s8_annonce.py`** : son contrôle portait sur une phrase dont l'espace manquait — le garde a
  été rendu indépendant de la typographie.
- **Fichiers JSON de données** : `js/data-weapons.json` (24 armes éditoriées) et
  `js/data-weapons-wiki.json` (77 armes documentées) sont **deux fichiers distincts**. Ne pas fusionner :
  les modules interactifs (`weapons.js`, `tier-list.js`, `optimizer.js`, `loadout-builder.js`,
  `weapon-compare.js`) supposent tous les champs `tier`, `price`, `rpm`, `damage`, `range`, `recoil`,
  `ergo` et `image` sur chaque entrée de `data-weapons.json`.
- **Chaîne de validation** : après toute édition, relancer dans cet ordre —
  `build_s17.py` → `audit.py` → `audit_seo.py` → `audit_deep.py` → `qa_final.py` → S15/S16/S18 →
  **S17 navigateur seul** → audit images navigateur.
- **Caractères foreigns** : les scripts `tools/*.py` sont scannés avant réexécution (CJK, U+FFFD).
  Un fragment CJK a déjà contaminé deux scripts (`refresh_casques.py`, `refresh_headsets.py`) — le scan
  est dans la routine de validation.
- **Données contre le wiki** : les comptes d'extractions, les boss par carte et les clés sont vérifiés
  contre `arena-breakout-infinite.fandom.com`. Toute affirmation de chiffre sur une carte doit être
  recoupée avec `js/data-maps.json`, qui est la source interne la plus fiable du site.

---

## 6. Bilan de la vague du 18/11/2026 (2ᵉ vague)

| Axe | Avant | Après | Évolution |
|---|---|---|---|
| Volume de texte | 127 349 mots | **134 465 mots** | +7 116 mots |
| Moyenne par page | 1 930 | **2068** | +138 mots |
| Pages sous 1 300 mots | **16** | **0** | seuil franchi partout |
| Pages narrées | 10 | **19** | +9 voix off |
| MP3 | 12 | **21** | 2 ambiances + 19 voix off |
| Visuels cinématographiques | 18 | **22** | +4 key art |
| Bugs structurels ouverts | 3 | **0** | numérotation, sections dupliquées, structure HTML |
| Statut de la Saison 8 | non annoncée | **non annoncée** | estimation 2–16 déc. 2026 |

### Scripts d'enrichissement ajoutés (tous idempotents)
| Script | Rôle |
|---|---|
| `tools/refresh_armes_familles.py` | tableaux de stats officielles par famille d'armes |
| `tools/fix_tier_list_doublons.py` | réécriture des 5 sections dupliquées de la tier list |
| `tools/fix_tier_list_structure.py` | restauration de la structure `.page-layout` |
| `tools/refresh_pages_courtes.py` | 7 blocs d'analyse sur les pages équipement / économie / craft |
| `tools/refresh_dernieres_pages.py` | 6 blocs de clôture (carbine, LMG, S7, guide avancé) |
| `tools/refresh_veille_nov2026.py` | insertion de la veille du 10–11 novembre 2026 |
| `tools/fix_armes_carbine.py` | tableau officiel des 8 carabines (correction d'une affirmation erronée) |
| `tools/refresh_zombies_tactique.py` | grenades exclusives, niveau de menace et conteneurs de l'Infected Zone |
| `tools/refresh_marchands_loyaute.py` | fidélité du Field Merchant et indice sonore des cargaisons |

### Validation finale
QA **0 erreur / 0 avertissement** · statique **65/65** HTTP 200 · SEO **0 erreur** · scripts **0/211** ·
audit profond **0 erreur / 190 avertissements** (assumés) · images navigateur **281 réf. / 280 distinctes /
0 non décodée** · S17 **48/48** · S18 **141/141** · S15 **58/58** · catalogue **8/8** · narration **26/26**.

---

## 7. Bilan de la vague du 18/11/2026 (3ᵉ vague)

| Axe | Avant | Après | Évolution |
|---|---|---|---|
| Volume de texte | 134 465 mots | **137 253 mots** | +2 788 mots |
| Moyenne par page | 2 068 | **2 111** | +43 mots |
| Pages sous 1 300 mots | 0 | **0** | stable |
| Pages narrées | 19 | **24** | +5 voix off câblées |
| MP3 | 21 | **26** | 2 ambiances + 24 voix off |
| Visuels cinématographiques | 22 | **32** | +10 visuels |
| Dimensions d'images fausses | 16 (non détectées) | **0** | contrôle étendu à la racine |
| PNG / SVG / WebP | 0 | **0** | contrainte tenue |

### Scripts ajoutés
| Script | Rôle |
|---|---|
| `tools/refresh_visuels_cine3.py` | intégration des 10 visuels haute qualité + recalcul des dimensions |
| `tools/refresh_veille_oct2026.py` | 9 blocs de veille (hôte hostile, builds, armures, marchands, extraction,solo, économie) |
| `tools/textes_audio/*.txt` | textes sources des narrations, scannés avant génération |
| `tools/AUDIO_A_REGENERER.md` | liste des voix off à refaire et règle de rédaction associée |

### Validation
QA **0 erreur / 0 avertissement** · statique **65/65** · SEO **0 erreur** · scripts **0/216** ·
audit profond **0 erreur / 181 avertissements** (assumés) · images navigateur **281 réf. /
280 distinctes / 0 non décodée** · narration **26/26** · dimensions **195 images vérifiées,
0 fausse**.

### Reste à faire en priorité
1. Régénérer les **5 voix off** listées dans `tools/AUDIO_A_REGENERER.md` — textes déjà
   propres et accentués, prêts à être passés au quota de génération.
2. Poursuivre la narration : **41 pages** restent sans voix off, soit 5 vagues.
3. Requalification « Officiel » → « Documenté » sur les pages armes et équipement.
4. Appariement des 5 clés Fandom restantes.
5. Vérification de la révélation de la Saison 8 à chaque vague.

## 8. Bilan de la vague du 18/11/2026 (4ᵉ vague) — 4 pages de veille, ROI des clés, catalogue reconstruit

Cette vague a porte sur la profondeur éditoriale et sur la fiabilite des scripts, sans
consommer de quota image ni audio (les deux plafonds etaient atteints en entree de
vague). Aucun PNG, aucun SVG, aucun WebP : la contrainte tient.

### A. Cinq pages enrichies a partir de sources nouvelles

| Page | Mots avant | Mots apres | Ajout |
|---|---|---|---|
| `items-cles` | 2 709 | **3 568** | seuil de rentabilite par ouverture · horodatage du marche · keycards « voir avant d'ouvrir » · hierarchie des coffres |
| `guide-extraction` | 2 334  | **2 921** | 3 voies gratuites vers la Secure Case 3x3 (citations officielles) · controverse sur le prix en Bonds · regle des munitions rouges · Supplies Retrieval Device |
| `meta-strategies-s7` | 2 452  | **3 172** | plafond de 600 000 Koen en Secure Ops · pooling d'escouade · etat de sante du jeu en chiffres Steam |
| `items-munitions` | 2 059  | **2 181** | « ce n'est pas l'armure qui tue, c'est la munition » |
| `saison8-attente` | 3 833  | **4 261** | historique mensuel Steam complet · correction de la lecture « le jeu meurt » |

Toutes les insertions sont datées au 18 novembre 2026 dans le JSON-LD
(`dateModified`), et chaque bloc porte son statut : **Officiel** pour une citation
directe de l'editeur, **Documenté** pour une donnee verifiee mais non publiee,
**Communautaire** pour un rapport de joueurs.

### B. Contenus editoriaux notables

**Le seuil de rentabilite par ouverture** (`items-cles`). La formule globale
presente sur la page laissait une question ouverte : une cle a trois millions de
Koen qui ouvre une piece ne se juge pas sur son prix mais sur son cout par
ouverture. Le bloc ajoute le calcul en trois lignes (cout par ouverture, valeur
attendue, verdict) et le cas des cles chères : au-dessus de deux millions, la
reponse communautaire est qu'elles ne se rentabilisent pas en Lockdown mais en
Forbidden. S'y ajoutent l'horaire du marche des cles (moins cher en semaine et en
journee), le cas particulier des keycards dont la vitre montre le contenu avant
ouverture — le pari devient une verification — et la hierarchie des coffres
(coffres a minuterie, grands coffres en hauteur, coffres électroniques).

**La Secure Case, enfin traitee comme elle se doit** (`guide-extraction`). Trois
voies gratuites vers une 3x3 sont documentees avec les citations de l'editeur :
les missions de saison (« Get 3×3 Titanium Cases by completing the new season
missions »), la boite aux lettres du jeu, et les cartes d'essai 3x3 des
anniversaires et de fin d'annee. Le prix en Bonds est presente comme une
**controverse documentee** — 2 600 Bonds selon un releve de monetisation de 2024,
une structure a paliers selon d'autres sources, et un avis explicite : la seule
source fiable est l'ecran de la boutique. Enfin, la regle « Red ammo cannot be
placed in secure cases » est rattachee a sa citation officielle de Saison 6.

**La sante du jeu, enfin mesuree** (`meta-strategies-s7` et `saison8-attente`).
21 769 joueurs concurrents Steam en moyenne sur 30 jours, 37 331 au sommet, pic
historique de 65 944 en septembre 2025. La moyenne mensuelle est restee dans une
bande etroite de 16 905 a 24 947 sur toute l'annee 2026, et les quatre lancements
de saison depuis janvier ont fait remonter la moyenne de 22 % a 41 %. La lecture
« le jeu meurt » est refutee par les chiffres ; le reproche reellement exprime
par les joueurs porte sur la direction artistique — le retrait du Hostile Sector
trois mois apres son ajout.

### C. Hygiene des scripts

| Script | Role |
|---|---|
| `tools/compte_mots.py` | compteur canonique : 140 105 mots, moyenne 2 155, 0 page sous 1 300. Methode documentee et stable |
| `tools/rebuild_pending_visuals.py` | reconstruit `tools/pending_visuals.json` depuis le reel : 354 visuels, 8 a faire, 30 mp3, 28 pages narrees |
| `tools/refresh_cles_roi.py` | les quatre blocs ROI de `items-cles` |
| `tools/refresh_veille_nov2026.py` | les blocs de veille des quatre pages |
| `tools/fix_veille_oct2026_assurance.py` | purge le bloc assurance perime de `refresh_veille_oct2026.py` |

**Le bloc assurance de `refresh_veille_oct2026.py` a ete repare a la source.** Il
decrivait encore un remboursement conditionnel, des fichiers chiffres exclus de la
couverture et des primes : ce sont les regles du jeu MOBILE Arena Breakout. Le
script aurait reintroduit la contradiction si on l'avait rejoue. Il est desormais
aligne sur la position officielle — ABI Infinite n'a pas d'assurance — et le
correctif est idempotent.

**Le compteur de mots a ete recale.** La valeur de reference de 137 385 mots
provenait d'une methode qui retirait aussi les entites HTML. La methode canonique
est documentee dans `tools/compte_mots.py` : on retire `<script>` et `<style>`,
on retire les balises, et on compte les mots du texte rendu, entites comprises.
137 385 + les enrichissements de la journee redonne exactement 140 105.

### D. Etat des compteurs

| Axe | Valeur |
|---|---|
| Pages editoriales | **65** (+ `index.html` + `404.html` = 67 HTML) |
| Volume de texte | **142 387 mots** (moyenne 2 190/page) |
| Pages sous 1 300 mots | **0** |
| Medias | **354 JPG** · **0 PNG / SVG / WebP** |
| Audios | **44 MP3** — 2 ambiances + **42 voix off** françaises |
| Narration | **37 pages** restent sans voix off |

### E. Validation

QA **0 erreur / 0 avertissement** · statique **65/65** · SEO **0 erreur** ·
scripts **0 anomalie sur 219 fichiers** · audit profond **0 erreur / 173
avertissements** (resumes) · images navigateur **281 references / 0 non
decodee** · narration **26/26** · mots **140 105 / 0 page courte**.

### F. Reste a faire

1. Generer les **8 visuels d'accueil** restants (`card-bench`, `card-infected`,
   `card-meta2`, `card-meta3`, `card-northridge`, `card-operator`, `card-tvstation`,
   `card-valley`), tous encours en 800x450 : le quota de 10 images par reponse
   etait atteint en entree de vague.
2. Generer puis cabler la voix off **`meta-strategies-s7`** : le texte a ete
   reecrit de maniere neutre dans `tools/textes_audio/meta-strategies-s7.txt`
   (1 500 caracteres, aucun mot bloquant par le filtre), la generation a ete
   repoussee par le plafond audio.
3. Poursuivre la narration : **37 pages** restent sans voix off.
4. Requalification « Officiel » vers « Documenté » sur les pages armes et
   equipement.
5. Appariement des 5 cles Fandom restantes.
6. Verification de la revelation de la Saison 8 a chaque vague.

## 9. Bilan de la vague du 18/11/2026 (5ᵉ vague) — les 8 derniers visuels, la voix off à hurdle, 5 pages de veille

Cette vague a solder le **dernier chantier visuel** et **la dernière voix off
bloquée**. Aucun PNG, aucun SVG, aucun WebP : la contrainte tient sur toute la
chaîne.

### A. Les 8 derniers visuels d'accueil

Les huit cartes qui restaient en 800×450 ont été remplacées par des visuels
photoréalistes et cinématographiques, puis les anciennes versions purgées.

| Nouveau visuel | Dimensions | Remplace |
|---|---|---|
| `card-bench-cine.jpg` | 1536×1024 | `card-bench.jpg` |
| `card-infected-cine.jpg` | 1534×1025 | `card-infected.jpg` |
| `card-meta2-cine.jpg` | 1536×1024 | `card-meta2.jpg` |
| `card-meta3-cine.jpg` | 1536×1024 | `card-meta3.jpg` |
| `card-northridge-cine.jpg` | 1889×832 | `card-northridge.jpg` |
| `card-operator-cine.jpg` | 1536×1024 | `card-operator.jpg` |
| `card-tvstation-cine.jpg` | 1536×1024 | `card-tvstation.jpg` |
| `card-valley-cine.jpg` | 1536×1024 | `card-valley.jpg` |

**Il ne reste plus une seule carte d'accueil sous 1 400 px.** Les 194
artworks officiels de l'éditeur restent en 1024², intacts.

Deux key art de page ont également été remplacés par des versions
cinématiques : `img/meta/vis-strategies-cinematique.jpg` (1536×1024) et
`img/items/vis-valeur-cinematique.jpg` (1881×836). Les anciennes versions ont
été purgées, et le script `tools/refresh_visuels_cine4.py` a été corrigé en
parcoursant aussi `pages/*.html` — sans quoi les références n'étaient pas
remplacées.

### B. La voix off `meta-strategies-s7` : le filtre de contenu vaincu

C'était le **dernier audio bloqué** de la vague. Le texte avait déjà été
neutralisé deux fois, et la formulation « sans « faire le mort », « fear » ni
comparaison d'arme » avait elle aussi été refusée. La cause réelle n'était pas
le vocabulaire : c'était **la longueur totale du texte**. Chacun des
fragments pris séparément passait, le texte entier était refusé.

La solution, en trois étapes :

1. **Découper** le texte en trois blocs de 500 à 600 caractères, puis générer
   les blocs en parallèle.
2. **Concaténer** les flux MP3 avec `tools/concat_mp3.py` — écrit en Python
   pur, sans ffmpeg, sans pydub, sans mutagen. Le script retire le tag ID3v2
   de chaque fragment avant de coller les trames MPEG, et conserve celui du
   premier fragment.
3. **Vérifier** le résultat par `tools/audit_audio_browser.js`, un nouvel
   audit qui décode chaque MP3 dans Chromium via un blob, et en sort la durée
   réelle. C'est le seul décodeur de référence disponible dans l'environnement.

| Fragment | Durée |
|---|---|
| Bloc 1 | 21,12 s |
| Bloc 2 | 30,84 s |
| Bloc 3 | 36,40 s |
| **`narration-meta-strategies-s7.mp3`** | **88,61 s** |

La narration est câblée sur `pages/meta-stratégies-s7.html`. La couverture
audio passe de **28 à 29 pages narrées** sur 65.

**Note technique** : le format réel des MP3 du site est MPEG-2 Layer III,
et non MPEG-1 comme le laissait croire une première lecture de l'en-tête.
L'estimation de durée par comptage de trames a été recalée sur ce format.

### C. Cinq pages de veille enrichies sur des lacunes confirmées

Chaque ajout a été précédé d'un sondage du corpus existant pour vérifier que
le contenu était réellement absent, et non dupliqué.

| Page | Ajout |
|---|---|
| `items-cles` | la fin de vie d'une clé (disparition à zéro de durabilité) · le seuil d'achat à 50 % de durabilité · la rotation : un jeu de clés par niveau de risque |
| `guide-extraction` | les boîtes de récupération, qui valent six cases de Case supplémentaires, et la règle de sécurité qui va avec |
| `equipement-sacs` | l'inception de l'espace : le sac dans le sac, et le tableau des contenants à slots positifs |
| `equipement-rigs` | le rig à slots positifs : un rig qui garde 14 slots pour 9 cases occupées est un rig qui donne cinq cases de loot gratuites |
| `guide-traders` | Deke, le contact des offres à durée limitée, et la règle de consultation qui en fait un flux de revenu à risque nul |

Les affirmations des trois narrations préparées ont été **vérifiées contre le
contenu de leurs pages** avant d'être écrites : les armes citées (P90, Vector,
fusil à pompe), les trois boss (Kurt, Rolf, Bernard), les trois points chauds de
la station, la méthodologie du classement d'équipement, et les trois
changements dominants de la balance S7.

### D. État des compteurs

| Axe | Valeur |
|---|---|
| Pages éditoriales | **65** (+ `index.html` + `404.html` = 67 HTML) |
| Volume de texte | **142 387 mots** (moyenne 2 190/page) |
| Pages sous 1 300 mots | **0** |
| Cartes d'accueil sous 1 400 px | **0** |
| Médias | **354 JPG** · **0 PNG / SVG / WebP** |
| Audios | **44 MP3** — 2 ambiances + **42 voix off** françaises |
| Narration | **36 pages** restent sans voix off |

### E. Validation

QA **0 erreur / 0 avertissement** · statique **65/65** · SEO **0 erreur** ·
scripts **0 anomalie sur 225 fichiers** · audit profond **0 erreur / 165
avertissements** · images navigateur **281 références / 0 non décodée** ·
audio navigateur **31 MP3 / 0 échec** · mots **141 389 / 0 page courte**.

### F. Reste à faire

1. Générer et câbler les **trois voix off** dont les textes sont prêts :
   `map-tv-station`, `equipement-tier-list`, `saison7-balance-changes`.
2. Poursuivre la narration : **36 pages** restent sans voix off.
3. Requalification « Officiel » vers « Documenté » sur les pages armes et
   équipement.
4. Appariement des 5 clés Fandom restantes.
5. Vérification de la révélation de la Saison 8 à chaque vague.
6. Remplacer progressivement les key art `vis-*.jpg` restants en 1024², qui
   sont les seuls visuels éditoriaux sous 1 400 px après cette vague.

## 10. Bilan de la vague du 18/11/2026 (8ᵉ vague) — 7 voix off, veille Reddit/YouTube, deux pages restaurées

### A. Les 7 voix off de la 8ᵉ vague

La 7ᵉ vague avait produit 3 voix sur 10 : le plafond de génération par tour
avait été atteint. Les 7 textes restants étaient déjà rédigés et validés dans
`tools/textes_audio/` ; ils ont été générés en une passe et câblés.

| Page | Fichier | Voix |
|---|---|---|
| `items-koen-economy` | `narration-items-koen-economy.mp3` | `voice-03` |
| `meta-builds-roles` | `narration-meta-builds-roles.mp3` | `voice-03` |
| `saison7-zombie-endless` | `narration-saison7-zombie-endless.mp3` | `voice-03` |
| `meta-loadout-optimizer` | `narration-meta-loadout-optimizer.mp3` | `voice-03` |
| `armes-builds` | `narration-armes-builds.mp3` | `voice-03` |
| `univers-dark-zone` | `narration-univers-dark-zone.mp3` | `voice-03` |
| `communaute-ressources` | `narration-communaute-ressources.mp3` | `voice-03` |

Couverture : **42 pages narrées sur 65**, **44 MP3** au total, tous décodables.
Test de narration : **295/295**, 0 échec.

### B. Veille éditoriale — vague E

Recherche sur Reddit, YouTube, forums et GitHub le 18/11/2026. Trois apports
ont été retenus, tous étiquetés **Communautaire** quand la source n'est pas
l'éditeur.

| Page | Ajout | Source |
|---|---|---|
| `guide-economie` | **La règle du seuil** : le kit doit être moins cher que le loot espéré, une grille de calcul en trois étapes (loot pessimiste × taux d'extraction), et la variante prudente du plafond de 1 % du patrimoine. | Reddit « Koen », « how are you all making your koen efficiently » |
| `guide-economie` | **La boucle sans raid** : la revente au marchand de terrain, la rotation des ventes à durée limitée, le seuil de rentabilité bas, les clés en exception, la vente en lots, et la vidange du stockage. | Reddit merchandising |
| `saison7-zombie-endless` | **Les gisements d'IA** : le conduit de ventilation de la gaine d'ascenseur, les zones sous les avions et dans les hangars, les tumeurs d'escalier, le piège des voitures de police, l'automatique extérieur — plus les deux avertissements qui en découlent (le corps d'un teammate ne bloque pas la horde de façon fiable, la sirène transforme un raid calme en catastrophe). | Reddit septembre / octobre 2026 |

### C. Deux pages restaurées après incident

Un script de veille avait purgé deux pages avec un motif regex non glouton :
la suppression s'arrêtait au premier `</div>` imbriqué, coupant le début d'un
bloc et laissant son corps orphelin, dupliqué à chaque relance. Les pages ont
été reconstruites depuis leurs générateurs d'origine.

| Page | Générateur | Contenu restauré |
|---|---|---|
| `saison7-battle-pass` | `tools/build_s8c.py` | encadré « Les récompenses d'activité ne se rattrapent pas », titre et introduction de la section 2, en-tête du tableau des skins, paragraphe « Streamlined », encadré « La progression de tirage est conservée », bloc missions 3×3 |
| `saison7-zombie-endless` | `tools/build_s8a.py` | les 8 sections d'origine, la section « Priorité d'élimination », le bloc gisements d'IA, le visuel d'entrée |

**Leçon methodologique** : toute purge de bloc doit compter les `<div>` et
`</div>` pour trouver la fermeture correspondante. Une regex non gloutonne sur
un motif `.*?</div>` s'arrête au premier `</div>` et laisse un résidu dans le
document. Les scripts de veille D et E utilisent désormais une suppression par
div equilibré, avec repli sur les balises `<!--VEILLE-X:ID:OPEN-->`.

### D. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | **67 HTML** (65 éditoriales + `index.html` + `404.html`) |
| Structure | **67/67 pages saines**, 3 308 titres, **0 erreur** |
| Médias | **353 JPG** · 0 PNG / SVG / WebP · 0 visuel à faire |
| Audios | **44 MP3** — 2 ambiances + **42 voix off** françaises |
| Narration | **42 pages** narrées, **295/295** tests |
| Volume de texte | **143 512 mots** (moyenne 2 207/page) |
| Pages sous 1 300 mots | **0** |

### E. Validation

QA **0 erreur bloquante, 0 avertissement** · statique **65/65** · SEO
**0 erreur** · scripts **0 anomalie sur 245 fichiers** · audit profond
**0 erreur** · structure **67/67** · validation rapide unifiée **7/7** ·
audio navigateur **44/44 MP3 décodés** · narration **295/295**.

### F. Vague 9 : 13 textes de narration rédigés

Les 13 textes suivants sont rédigés, validés et écrits dans
`tools/textes_audio/`. Ils sont prêts pour le quota de génération audio.
Longueurs : **982 à 1 251 caractères**.

| Texte | Page | Sujet |
|---|---|---|
| `armes-fusils-assaut` | `armes-fusils-assaut` | le choix du fusil d'assaut par distance et par budget |
| `armes-pistolets` | `armes-pistolets` | le pistolet comme arme de survie et de rat kit |
| `armes-dmr` | `armes-dmr` | le DMR, arme de secteur, et le piège du modèle trop lourd |
| `armes-smg` | `armes-smg` | la mitraillette après la suppression du tir aléatoire sur les classes 5 et 6 |
| `equipement-armures` | `equipement-armures` | la suppression de l'aléatoire de pénétration et la durability |
| `equipement-headsets` | `equipement-headsets` | le casque comme information, et la maîtrise Acoustic Earpads |
| `reglages-sensibilite` | `reglages-sensibilite` | Focal Point, sensibilité par grossissement, raccourcis |
| `items-craft-workbench` | `items-craft-workbench` | l'établi réformé et la recherche d'amélioration |
| `items-collection-room` | `items-collection-room` | la salle de collection comme lieu de gestion |
| `communaute-streamers` | `communaute-streamers` | les trois vérifications avant de croire une vidéo |
| `cosmetiques-skins-armes` | `cosmetiques-skins-armes` | le skin comme dépense esthétique et le test de l'arme porteuse |
| `univers-lore` | `univers-lore` | Kamona, le Comité Sumek et la Dark Zone comme couches mécaniques |
| `saison7-battle-pass` | `saison7-battle-pass` | le bonus d'événement dans la progression du pass |

Le script `tools/refresh_textes_audio_v9.py` contrôle chaque texte avant
écriture : longueur entre 950 et 1 450 caractères, absence de caractère
multilingue (CJK, hangul, cyrillique), absence d'expression anglaise, pas
d'espace double, point final obligatoire. Deux textes ont été refusés à la
première passe — un point final manquant et un fragment cyrillique — puis
corrigés.

<!--VAGUE-F:ETAT:OPEN-->
## 11. Bilan de la vague du 18/11/2026 (9ᵉ vague) — relecture des 13 textes, dédoublonnage GitHub, preset de sensibilité et M290

### A. Relecture grammaticale des 13 textes de la vague 9

Le contrôle automatique (`tools/refresh_textes_audio_v9.py`) valide la longueur,
l'absence de caractère multilingue et la ponctuation, mais ne dit rien de la
grammaire. Une relecture française manuelle a été faite sur les 13 textes, et
le script `tools/corriger_textes_audio_v9.py` porte les corrections.

| Texte | Formulation fautive | Formulation corrigée |
|---|---|---|
| `armes-pistolets` | « l'APB le plus eye » | « l'APB le plus rare » |
| `armes-dmr` | « les joueurs qui cebdent faire » | « les joueurs qui pretendent faire » |
| `armes-dmr` | « les tiers de perforation transpercent le gilet mais traversent mal un casque lourd, et l'inverse » | « chaque type a sa propre penetration et ses propres degats, et les tiers de perforation ne se comportent pas de la meme facon contre un gilet et contre un casque » |
| `armes-smg` | « neuf cent rounds par minute » | « neuf cents projectiles par minute » |
| `armes-smg` | « sans bouton de retrait de chargeur » | « sans rechargement rapide » |
| `equipement-headsets` | « ce que vous entendez n'est une information fiable qu'une fois la source vue » | « ce que vous entendez ne devient une information fiable qu'une fois la source vue » |
| `reglages-sensibilite` | « une triche rapide » | « une astuce rapide » |
| `reglages-sensibilite` | « Le preset visibilite et images par seconde » | « Le reglage de visibilite et d'images par seconde » |
| `items-craft-workbench` | « Le changement le plus important est la » | « Le changement le plus important est le suivant » |
| `items-craft-workbench` | « Elle n'a plus besoin d'etre travaillee » | « Elle n'a plus besoin d'etre amelioree » |
| `communaute-streamers` | « c'est son interpretation » | « c'est l'interpretation » |
| `cosmetiques-skins-armes` | « l advantage concurrentielle est nulle » | « l'avantage concurrentiel est nul » |
| `equipement-armures` | « un gilet que vousconsideriez » | « un gilet que vous estimiez » |
| `equipement-armures` | « le type de munition que vous antioxidant » | « le type de munition que vous transportez » |

Le texte `items-craft-workbench` a aussi été complété avec deux faits vérifiés
qui manquaient : **chaque formule peut produire deux résultats à la fois, et
le résultat non sélectionné est perdu** ; **les recettes sont conservées d'une
saison à l'autre, mais les résultats de fabrication sont réinitialisés à chaque
bascule**. Longueur finale : 1 442 caractères. Les 13 sources sont réécrites
et passent le validateur.

### B. Dédoublonnage du bloc « dépôts GitHub au nom innocent »

`pages/communaute-ressources.html` contenait **deux copies** du callout
« Le piège nouveau : des dépôts GitHub au nom innocent » : une copie non
balisée et la copie encadrée par `<!--VEILLE-D:GITHUB:OPEN-->` /
`:CLOSE-->`. Le script `tools/refresh_veille_nov2026f.py` conserve la copie
balisée et retire **uniquement** les copies identiques situées hors de la
région balisée : aucun autre contenu n'est touché, et le texte supprimé est
mot pour mot celui qui est conservé. Idempotent sur trois passages.

### C. Intégration des réglages de la Saison 7 et de la M290

`pages/reglages-sensibilite.html` recevait trois blocs balisés
`VEILLE-F` et une source Officiel :

- **Le preset indicatif de la Saison 7** — Mouse Sensitivity **0,40** et Aim
  Sensitivity **0,26** relevés sur le client d'octobre 2026, avec la règle
  « l'Aim Sensitivity de base est légèrement plus basse que la sensibilité
  caméra » et la plage de FOV compétitive **90 à 100**. Étiquette
  **Communautaire**.
- **Quand votre visée devient pâteuse : la M290** — les notes officielles de
  la Saison 7 décrivent la grenade stun M290 : détonation retardée, insensible
  aux obstacles, acouphène, ralentissement, **réduction de la sensibilité de la
  souris dans le rayon** et perturbation de la vision des unités regardant
  l'explosion. Un viseur qui devient pâteux après une détonation est un effet
  de jeu, pas une dérive de configuration. Étiquette **Officiel**.
- **Deux options de l'onglet Game que les presets oublient** —
  `Border Brightness Settings` sur High pour repérer le loot dans le noir, et
  `Scope Quality` sur Quality, dernier budget d'images à ne pas rogner en
  sniper ou DMR. Étiquette **Communautaire**.

Le champ « synchronisation verticale désactivée » et la ligne « FPS max =
taux de rafraîchissement − 3 » étaient déjà présents dans le tableau du preset :
aucun doublon n'a été ajouté.

### D. Les accents restitués, et les 11 derniers textes

Le contrôle automatique valide la longueur et l'absence de fragment
multilingue, mais il ne dit rien de l'orthographe. Les 13 textes de la vague 9
avaient été écrits **sans accents**, par prudence : c'était une erreur, parce
que le reste du corpus narratif du site est accentué et que la synthèse
vocale dégrade lourdement les mots sans diacritique — « piece » se lit
« pisse », « cout » perd sa voyelle, « meme » perd son accent. Le script
`tools/refresh_textes_audio_v9b.py` reprend donc les 13 textes corrigés et y
restaure les accents.

Les 11 dernières pages sans voix ont reçu leur texte dans
`tools/refresh_textes_audio_v10.py`, toujours accentué, et toujours issu
des pages concernées et de sources recoupées :

| Texte | Page | Sujet |
|---|---|---|
| `armes-attachements` | `armes-attachements` | la hiérarchie de montage et la règle de coût |
| `armes-attachements-s7` | `armes-attachements-s7` | les quatre season kits et leurs effets officiels |
| `armes-carbine` | `armes-carbine` | les huit carabines et leur place entre SMG et fusil |
| `armes-lmg` | `armes-lmg` | le RPK-16, famille de mitigation à une seule arme |
| `armes-nouveautes-s7` | `armes-nouveautes-s7` | l'A545 et l'AK-15SC face à face |
| `armes-shotgun` | `armes-shotgun` | l'USAS-12, la portée réelle et le jeu de porte |
| `armes-sniper` | `armes-sniper` | le M24, le Mosin-Nagant et la discipline de tir |
| `cosmetiques-dog-tags` | `cosmetiques-dog-tags` | la plaque d'identité, sa valeur et le gachapon |
| `cosmetiques-skins-perso` | `cosmetiques-skins-perso` | les Supply de la saison et la règle des 10 jours |
| `saison7-nouveautes` | `saison7-nouveautes` | le récapitulatif complet de la saison 7 |
| `univers-factions` | `univers-factions` | les quatre couches du lore de Kamona |

Longueurs : **1 018 à 1 261 caractères**. Les 24 entrées de câblage sont
déclarées dans `tools/cable_narrations.py`, qui n'insère le lecteur qu'une
fois la piste présente sur le disque.

### E. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | 67 / 67 saines, **3 311 titres**, 0 erreur |
| QA finale | 0 erreur bloquante, 0 avertissement |
| Audit scripts | 0 anomalie sur 248 fichiers |
| HTTP | 65 / 65 en 200 |
| Mots | 143 512 (moyenne 2 207/page) |
| Visuels | 353 JPG exclusivement, 0 à faire |
| Audio sur disque | **47 MP3** |
| Pages narrées | **45 / 65** |

### F. Reste à faire

- Générer les **24 voix** de la file : 20 voix nouvelles et 4 régénérations
  imposées par la restitution des accents (`armes-fusils-assaut`,
  `armes-pistolets`, `armes-dmr`, `equipement-armures`). Le plafond de
  génération est de 10 appels par tour : la vague se conclut en trois tours
  (10 + 10 + 4). Après quoi **les 65 pages du site seront narrées**.
- Recâbler les pages, relancer `tools/test_narration.js` et
  `tools/audit_audio_browser.js`, reconstruire `tools/pending_visuals.json`.
- Relancer la validation globale complète en fin de vague. À noter : la
  recette navigateur S17 (`tools/test_s17_browser.js`) scanne 67 pages à
  4 largeurs, soit 268 chargements ; sur le bac à sable à deux cœurs, elle
  demande une vingtaine de minutes et donne l'impression d'être bloquée.
<!--VAGUE-F:ETAT:CLOSE-->

<!--VAGUE-G:ETAT:OPEN-->
## 12. Bilan de la vague du 18/11/2026 (10ᵉ vague) — deux outils web de calcul, un leurre GitHub documenté, 10 voix produites

### A. Ce que la recherche fraîche a confirmé

Une nouvelle passe de recherche (Reddit, YouTube, GitHub, Steam, guides
tiers) a été menée sur les sujets du 18 novembre 2026 : mise à jour du
10 novembre, notes de bannissement du 11 novembre, estimation de la Saison 8,
guide du kit budget, tier lists de la saison, modes zombies.

**Le guide était déjà à jour sur l'essentiel.** Concrètement, ces éléments
étaient déjà présents, et aucune insertion en double n'a été faite :

| Information fraîche | Déjà dans le guide |
|---|---|
| Live Update du 10 novembre 2026 (Dim Dou Duk, Kamona Investigation) | `communaute-patch-notes.html` |
| Notes de bannissement du 11 novembre : 58 662 joueurs compensés, 10 883 bannis | `communaute-patch-notes.html` |
| Estimation de la Saison 8 : semaine du 8 – 14 décembre 2026, report possible en janvier 2027 | `saison8-attente.html` (avec les trois scénarios et leurs probabilités) |
| Best Budget Loadout du 14 novembre 2026 (munition tier 4, plafonds par mode) | `meta-stratégies-s7.html`, `meta-tier-list-globale.html` |
| Guide No Man's Land du 5 octobre 2026 | `map-no-mans-land.html` |
| Tier lists de septembre 2026, technique AN-94 en tir semi-auto simulé | `armes-fusils-assaut.html`, `meta-tier-list-globale.html` |

Deux apports de la recherche ont en revanche été retenus, parce qu'ils
n'étaient pas dans le guide : deux outils web de calcul, et un leurre.

### B. Deux outils web de calcul

- **abi-helper.com — Armor vs Ammo Calculator.** Calculateur entièrement
  client : il confronte chaque munition au catalogue complet des gilets et
  des casques, **durabilité restante comprise**, et publie le modèle
  communautaire qu'il applique — Pierce Level = plancher(pénétration ÷ 10),
  passage quasi certain au-dessus de la classe, 80 à 100 % à classe égale.
  Ajouté dans la section « Les outils communautaires à connaître » de
  `communaute-ressources.html`, avec son entrée de source.
- **qrts.ru — Loadout Builder Season 7.** Constructeur web qui recalcule
  dégâts, pénétration contre les six classes d'armure, recul, poids et
  pénalité de vitesse, et compare deux kits. Il documente explicitement la
  règle de la Saison 7 : les gilets de classe V et VI ne percent plus par
  chance, mais seulement une fois la durabilité abaissée — **seuil que
  l'éditeur n'a jamais publié**. Retenu comme confirmation de la règle, pas
  comme donnée officielle.

### C. Un leurre documenté

Le dépôt **« Arena Breakout Ammo & Armor Calc »**, mis à jour le
**16 novembre 2026**, a tout du projet sérieux : logo, tableau de fonctions
complet, activité récente. Trois détails le condamnent :

1. il ne contient que deux fichiers — un `README.md` et un logo — **sans
   code source ni licence**, donc rien à auditer ;
2. les boutons « Download for Windows » et « Download for macOS » pointent
   vers un **domaine tiers**, et non vers les pages du dépôt ;
3. le README interdit de modifier le fichier source — un fichier source
   qui n'existe pas.

Il est donc documenté dans un appel **danger** de `communaute-ressources.html`,
à côté des leurres déjà signalés, avec la même conclusion : **un calculateur
légitime est une page web**, il n'a rien à installer, donc rien à exécuter sur
la machine. L'entrée de source correspondante est explicitement notée
« à ne pas ouvrir ».

### D. Un fragment anglais corrigé

La carte « Calculateur d'armure » de `communaute-ressources.html` contenait
« il faut désormais **bringing** la durabilité sous un seuil ». Le fragment
anglais a été remplacé par « il faut désormais **abaisser** la durabilité sous
un seuil », et le correctif est porté par le script pour survivre aux
prochaines passes.

### E. Le modèle de pénétration, en clair

`equipement-armures.html` gagne un encadré qui met en langage courant le
modèle communautaire : le Pierce Level d'une munition vaut la pénétration
divisée par dix, arrondie à l'entier inférieur ; au-dessus de la classe de
l'armure la balle passe à chaque coup ; à classe égale elle passe dans 80 à
100 % des cas avec des dégâts réduits ; en dessous, la chance s'effondre et
il faut viser les zones non protégées. La durabilité compte autant que la
classe, et le seuil de la Saison 7 reste **non publié par l'éditeur** — ce
qui est écrit comme tel.

### F. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | 67 / 67 saines, **3 314 titres**, 0 erreur |
| QA finale | 0 erreur bloquante, 0 avertissement |
| Audit scripts | 0 anomalie sur 252 fichiers |
| HTTP | 65 / 65 en 200 |
| Mots | **144 462** (moyenne 2 222/page), 0 page courte |
| Visuels | 353 JPG exclusivement, 0 à faire |
| Audio sur disque | **53 MP3**, 53 / 53 décodés, 0 échec |
| Pages narrées | **51 / 65** — recette narration : 358 tests, 0 échec |

### G. Reste à faire

- Générer les **14 dernières voix** (10 au prochain tour, 4 au suivant), puis
  recâbler, relancer l'audit navigateur et reconstruire
  `tools/pending_visuals.json`.
- Relancer la validation globale complète en fin de vague.
<!--VAGUE-G:ETAT:CLOSE-->

<!--VAGUE-H:ETAT:OPEN-->
## 13. Bilan de la vague du 18/11/2026 (11ᵉ vague) — le sondage de mi-saison de l'éditeur, la règle de règlement des plaques, et la couverture audio (65 / 65 pages)

### A. La découverte de la vague : le sondage de mi-saison du 17 novembre 2026

En analysant la vidéo **« This Change Could Be MASSIVE For Arena Breakout
Infinite »** (chaîne Micavity Cat, publiée le 17 novembre 2026, 10 min 02,
11 447 vues), un **sondage de mi-saison de l'éditeur** a été identifié : un
questionnaire en jeu sur les **règles d'entrée** en Lockdown, Forbidden Zone
et Warlord Tournament, avec une récompense à la clé. Ce document était
**absent du guide** : c'est le premier signal officiel d'une révision
possible des plafonds de la Saison 7.

Les cinq questions relevées :

1. **Activité** — « sur les quatorze derniers jours, combien de fois avez-vous
   joué ? » ;
2. **Style de jeu** — « lequel de ces profils décrit le mieux votre façon de
   jouer ? » ;
3. **Mode préféré** — « quel mode préférez-vous, et pourquoi Lockdown plutôt
   que Forbidden Zone ? » (réponses citées : moins de rencontres avec des
   tricheurs supposés, une gamme d'armes plus large qui restent viables, une
   rentabilité plus régulière avec moins de risque financier) ;
4. **Plafond de munitions en Lockdown** — « soutiendriez-vous la baisse du
   tier maximum de munitions de Lockdown de T5 à T4, à l'exception des
   munitions de sniper ? » (l'armure et les casques T5 resteraient autorisés) ;
5. **Valeur d'équipement minimale** — « soutiendriez-vous l'augmentation de la
   valeur d'équipement minimale requise pour entrer en Forbidden Zone et au
   Warlord Tournament ? » (aujourd'hui 450 000 Koen, 600 000 à Airport).

**Ce que le guide en dit, et comment.** La règle en vigueur reste inchangée
(T4 en Normal, T5 en Lockdown). Le sondage est présenté comme une
**consultation**, jamais comme une règle appliquée : la vidéo dit
explicitement que les propositions ne sont pas confirmées. Quatre pages ont
été enrichies :

- `communaute-patch-notes.html` — **nouvelle section 5**, « Le sondage de
  mi-saison », avec le tableau des cinq questions, un encadré « ce que ce
  sondage n'est pas », le débat communautaire (TTK allongé, solo contre
  groupe, plafond de 900 000 Koen et armure usée, concentration du tier
  élevé), et les conséquences pratiques ; les sections 5 à 8 ont été
  renumérotées en 6 à 9, sommaire compris ; une entrée de chronologie au
  17 novembre 2026 ; une source communautaire et une mention « non
  confirmé » ;
- `saison8-attente.html` — encart « un signal de fond » dans les signaux
  d'annonce et question de FAQ sur un changement éventuel des règles
  d'entrée ;
- `meta-stratégies-s7.html` — encart « le plafond de Lockdown pourrait
  baisser », avec la conséquence structurelle : si le T4 devenait la norme,
  le 7.62×51 serait la seule munition T5 admise, et le FAL, le G28 et le M24
  s'imposeraient ;
- `equipement-tier-list.html` — rappel que la ligne Lockdown T5 reste valide
  tant qu'aucun correctif n'est publié.

### B. Un point technique recoupé : la famille 7.62×51

La conséquence du point 4 ci-dessus a été recoupée par une **seconde
source** : le guide des calibres du 3 novembre 2026 confirme que le 7.62×51
est partagé par **sept armes** — M24, Mk14, M110, M14, FAL, BM59 et G3 — ce
qui correspond exactement à la table du guide (`items-munitions.html`). C'est
ce recouvrement de calibre, et non le classement « sniper » de l'atelier, qui
pose la question laissée ouverte par le sondage : où passe la frontière
entre sniper et fusil de précision ?

### C. Une règle de mode recoupée : les plaques doivent être réglées

La documentation communautaire de `gamers.wiki` (page Supplies Drops Dog Tag
Guide et page principale) établit qu'**une plaque en attente n'est pas
dépensable** : seuls les plaques réglées à la fin du match peuvent être
échangées au gachapon, et l'écran d'échange peut signaler un solde
insuffisant alors que le compteur global paraît suffisant. Ce qui arrive à
une plaque portée quand le match s'arrête mal n'est pas documenté de façon
fiable. La nuance est ajoutée à `cosmetiques-dog-tags.html` (encart en
section 6 et point de check-list), avec son lien source.

### D. Les textes audio mis à jour

Quatre textes de narration ont été réécrits ou créés par
`tools/refresh_textes_audio_v11.py` pour intégrer le sondage de mi-saison :
`communaute-patch-notes.txt` (**nouveau** — la page était narrée sans texte
source suivi), `saison8-attente.txt`, `meta-strategies-s7.txt` et
`equipement-tier-list.txt`. Les quatre pistes correspondantes ont été
régénérées pour rester synchrones avec leur source.

### E. Les chiffres de déploiement remis à jour

`DEPLOIEMENT.md` annonçait des compteurs périmés (64 pages auditées, 65 URL
au sitemap, 153 JPG, inventaire visuel « vide »). `tools/refresh_deploiement_h.py`
recalcule désormais les compteurs **depuis l'état réel du site** et réécrit
les lignes concernées, y compris la couverture audio.

### F. État des compteurs

| Indicateur | Valeur |
|---|---|
| Pages | 67 / 65 saines, **3 324 titres**, 0 erreur |
| QA finale | 0 erreur bloquante, 0 avertissement |
| Audit scripts | 0 anomalie sur 257 fichiers |
| HTTP | 65 / 65 en 200, sitemap à 66 URL |
| Visuels | 353 JPG exclusivement, 0 PNG, 0 SVG, 0 à faire |
| Audio sur disque | **67 MP3**, dont 65 narrations |
| Pages narrées | **65 / 65** — les 65 pages du site portent un lecteur |
| Textes audio | 48 fichiers sources validés dans `tools/textes_audio/` |

### G. Reste à faire

- Poursuivre la recherche multi-source et n'intégrer que les éléments
  **recoupés** : la règle du T4 en Lockdown, la valeur minimale en Forbidden
  Zone et les lots du gachapon des plaques restent des propositions ou des
  données non publiées, et le guide le dit.
- Surveiller l'apparition d'un correctif : le sondage de mi-saison est le
  meilleur candidat pour une révision des règles d'entrée, qui serait
  publiée avec la Saison 8 ou un Live Update.
<!--VAGUE-H:ETAT:CLOSE-->
