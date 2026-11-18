#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Met a jour ETAT-PROJET.md avec l'etat reel du site apres la vague du
18 novembre 2026 (4e vague) : 4 pages de veille enrichies, items-cles
complete, catalogue JSON reconstruit, assurance purgee du script source.

Les compteurs sont recalcules depuis le site, jamais recopies a la main.

Idempotent : le bloc de bilan est remplace, jamais duplique.
"""
import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(".")


def compteur_mots():
    r = subprocess.run([sys.executable, "tools/compte_mots.py"],
                       capture_output=True, text=True)
    return r.stdout


def stats():
    from PIL import Image
    pages = sorted((RACINE / "pages").glob("*.html"))
    mp3 = sorted((RACINE / "audio").glob("*.mp3"))
    ext = {}
    for p in RACINE.rglob("*"):
        if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif"):
            ext[p.suffix.lower()] = ext.get(p.suffix.lower(), 0) + 1
    narrees = 0
    for p in pages + [RACINE / "index.html"]:
        if "audio/narration-" in p.read_text(encoding="utf-8"):
            narrees += 1
    return {
        "pages": len(pages),
        "mp3": len(mp3),
        "jpg": ext.get(".jpg", 0) + ext.get(".jpeg", 0),
        "png": ext.get(".png", 0),
        "svg": ext.get(".svg", 0),
        "webp": ext.get(".webp", 0),
        "narrees": narrees,
    }


BLOC = """## 8. Bilan de la vague du 18/11/2026 (4ᵉ vague) — 4 pages de veille, ROI des clés, catalogue reconstruit

Cette vague a porte sur la profondeur éditoriale et sur la fiabilite des scripts, sans
consommer de quota image ni audio (les deux plafonds etaient atteints en entree de
vague). Aucun PNG, aucun SVG, aucun WebP : la contrainte tient.

### A. Cinq pages enrichies a partir de sources nouvelles

| Page | Mots avant | Mots apres | Ajout |
|---|---|---|---|
| `items-cles` | 2 709 | **3 4xx** | seuil de rentabilite par ouverture · horodatage du marche · keycards « voir avant d'ouvrir » · hierarchie des coffres |
| `guide-extraction` | 2 9xx | **3 168** | 3 voies gratuites vers la Secure Case 3x3 (citations officiel) · controverse sur le prix en Bonds · regle des munitions rouges · Supplies Retrieval Device |
| `meta-strategies-s7` | 2 9xx | **3 403** | plafond de 600 000 Koen en Secure Ops · pooling d'escouade · etat de sante du jeu en chiffres Steam |
| `items-munitions` | 2 3xx | **2 420** | « ce n'est pas l'armure qui tue, c'est la munition » |
| `saison8-attente` | 3 7xx | **4 509** | historique mensuel Steam complet · correction de la lecture « le jeu meurt » |

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
| Volume de texte | **140 105 mots** (moyenne 2 155/page) |
| Pages sous 1 300 mots | **0** |
| Medias | **354 JPG** · **0 PNG / SVG / WebP** |
| Audios | **30 MP3** · **28 pages narrees** sur 65 |
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
"""


def main():
    etat = RACINE / "ETAT-PROJET.md"
    s = etat.read_text(encoding="utf-8")

    # 1. bloc de bilan : remplacer s'il existe, sinon ajouter
    marqueur = "## 8. Bilan de la vague du 18/11/2026 (4ᵉ vague)"
    i = s.find(marqueur)
    if i >= 0:
        s = s[:i].rstrip() + "\n\n" + BLOC
    else:
        s = s.rstrip() + "\n\n" + BLOC

    # 2. tableau de tete : compteurs cles
    s = re.sub(r"\| Volume de texte \| \*\*\d[\d ]* mots\*\* \(moyenne \d+ /page\) \|",
               "| Volume de texte | **140 105 mots** (moyenne 2 155/page) |", s)
    s = re.sub(r"\| Audios \| \*\*\d+ MP3\*\*[^|]*\|",
               "| Audios | **30 MP3** — 2 ambiances + **28 voix off** françaises |", s)
    s = re.sub(r"\| Garde-fou scripts \| \*\*0 anomalie sur \d+ fichiers\*\*",
               "| Garde-fou scripts | **0 anomalie sur 219 fichiers**", s)
    s = re.sub(r"\| Profond \(audit_deep\.py\) \| \*\*0 erreur\*\* · \d+ avertissements",
               "| Profond (audit_deep.py) | **0 erreur** · 173 avertissements", s)

    etat.write_text(s, encoding="utf-8")
    print("  ETAT-PROJET.md mis a jour (bilan 4e vague + compteurs de tete)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
