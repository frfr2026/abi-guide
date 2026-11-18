# -*- coding: utf-8 -*-
"""Outil interne — application d'accents francais sur un contenu HTML.

Le contenu S12 a ete redige en ASCII puis accentue par ce script, qui utilise
un dictionnaire de mots non ambigus et des regles de contexte pour les mots
ambigus (a/a, ou/ou, des/des, la/la).
"""
import re
import sys

# ── Mots dont l'accent est toujours requis dans ce corpus ─────────────
DICT = {
    "abimee": "abîmée", "aeronautiques": "aéronautiques", "aeroport": "aéroport",
    "allies": "alliés", "ambusculee": "embusquée", "annees": "années",
    "antiaerienne": "antiaérienne", "antiaeriennes": "antiaériennes",
    "apparait": "apparaît", "appelee": "appelée", "approchee": "approchée",
    "apres": "après", "armee": "armée", "arretes": "arrêtés", "arret": "arrêt",
    "avancee": "avancée", "aupres": "auprès", "autorite": "autorité",
    "batiments": "bâtiments", "batit": "bâtit", "blindee": "blindée",
    "caracteristiques": "caractéristiques", "chaine": "chaîne",
    "cite": "cité", "cle": "clé", "cles": "clés", "coherente": "cohérente",
    "comite": "comité", "communaute": "communauté", "communiquee": "communiquée",
    "concrete": "concrète", "confirmee": "confirmée", "confirmees": "confirmées",
    "consequence": "conséquence", "consequences": "conséquences",
    "considerables": "considérables", "conteste": "contesté",
    "controle": "contrôle", "cote": "côte", "cree": "crée", "crees": "créés",
    "datee": "datée", "decide": "décidé", 
    "declaration": "déclaration", "declaree": "déclarée", "declarees": "déclarées",
    "decor": "décor", "decoratif": "décoratif", "dediee": "dédiée",
    "defend": "défend", "defense": "défense", "definitions": "définitions",
    "deja": "déjà", "deliberement": "délibérément", "densite": "densité",
    "depend": "dépend", "deplace": "déplacé", "deployees": "déployées",
    "depose": "déposé", "depot": "dépôt", "depots": "dépôts",
    "derniere": "dernière", "designe": "désigné", "desorientee": "désorientée",
    "detail": "détail", "deuxieme": "deuxième",
    "developpement": "développement", "developpements": "développements",
     "diffusee": "diffusée", "dignite": "dignité",
    "disputee": "disputée", "donnee": "donnée",
    "donnees": "données", "donnes": "donnés", "ecart": "écart",
    "echanges": "échanges", "echantillons": "échantillons", "echappe": "échappe",
    "echelle": "échelle", "eclat": "éclat", "economiques": "économiques",
    "ecrase": "écrase", "ecrasement": "écrasement", 
    "editeur": "éditeur", "egal": "égal", "egale": "égale", "elevee": "élevée",
    "elimination": "élimination", "elite": "élite", "emeute": "émeute",
    "ennee": "enneigée", "enqueteur": "enquêteur", "entites": "entités",
"episode": "épisode", "epuration": "épuration",
    "equipe": "équipe", "equipes": "équipes", "equipement": "équipement",
    "etat": "état", "etage": "étage", "etaient": "étaient", "etait": "était",
    "ete": "été", "etes": "êtes", "etranger": "étranger", "etrangeres": "étrangères",
    "etre": "être", "evacue": "évacué", "evenement": "événement",
    "evenements": "événements", "eviter": "éviter", "expliques": "expliqués",
    "exposee": "exposée", "facon": "façon", "floues": "flouées",
    "frontiere": "frontière", "generateur": "générateur", "geographie": "géographie",
    "geographiquement": "géographiquement", "gerer": "gérer", "hostilites": "hostilités",
    "hotel": "hôtel", "hypothese": "hypothèse", "identite": "identité",
    "ideologique": "idéologique", "ile": "île", "iles": "îles",
    "incube": "incubé", "independance": "indépendance", "independant": "indépendant",
    "infectee": "infectée", "infectees": "infectées", "infectes": "infectés",
    "intensite": "intensité", "interestait": "intéressait",
    "interference": "interférence", "interieur": "intérieur", "intitule": "intitulé",
    "liberation": "libération", "locality": "localité", "majeur": "majeur",
    "majorite": "majorité", "material": "matériel", "materiel": "matériel",
    "mediation": "médiation", "mediatise": "médiatise", "medie": "médie",
    "meme": "même", "mentionne": "mentionné", "meridionales": "méridionales",
    "metaphore": "métaphore", "methode": "méthode", "militarise": "militarisé",
    "militarisees": "militarisées", "miniere": "minière", "monetisation": "monétisation",
    "montree": "montrée", "muette": "muet", "mystere": "mystère",
    "mysteres": "mystères", "noeud": "nœud", "nomme": "nommé",
    "operateurs": "opérateurs", "operation": "opération",
    "operationnelle": "opérationnelle", "opportunite": "opportunité",
    "ordonnes": "ordonnés", "organise": "organisé",
    "parrainee": "parrainée", "penetration": "pénétration", "piece": "pièce",
    "plutot": "plutôt", "pole": "pôle", "possede": "possède",
    "precisement": "précisément", "predit": "prédit", 
    "priorite": "priorité", "privees": "privées", "reactif": "réactif",
    "realisee": "réalisée", "recit": "récit", "recompense": "récompense",
    "recoupees": "recoupées", "recovers": "récupère",
    "recuperations": "récupérations", "recupere": "récupéré",
    "recuperer": "récupérer",  "redirigee": "redirigée",
    "reel": "réel", "region": "région", "regions": "régions",
    "regle": "règle", "regressions": "régressions", "renovation": "rénovation",
    "renovee": "rénovée", "reperes": "repères", "repetee": "répétée",
    "republique": "république", "reputation": "réputation",
    "requisionne": "réquisitionne", "requisitionne": "réquisitionné",
    "reseau": "réseau", "reseaux": "réseaux", "residence": "résidence",
    "resolue": "résolue", "resolus": "résolus", "resultat": "résultat",
    "resume": "résumé", "reunions": "réunions", "reussi": "réussi",
    "reussie": "réussie", "revele": "révèle", "revelee": "révélée",
    "role": "rôle", "sacrifice": "sacrifice", "serie": "série",
    "securiser": "sécuriser", "securite": "sécurité", "situees": "situées",
    "situes": "situés", "special": "spécial", "specialistes": "spécialistes",
    "steriles": "stériles", "strategique": "stratégique",
    "strategiquement": "stratégiquement", "suggere": "suggère",
    "superieurs": "supérieurs", "supplementaires": "supplémentaires",
    "synthese": "synthèse", "systeme": "système", "systemes": "systèmes",
    "theatre": "théâtre", "theorie": "théorie", "theories": "théories",
    "tranchee": "tranchée", "tresors": "trésors", "troisieme": "troisième",
    "unite": "unité", "vallee": "vallée", "veritables": "véritables",
    "videos": "vidéos", "abolition": "abolition", "acceleration": "accélération",
    "extraction": "extraction", "forteresse": "forteresse", "generation": "génération",
    "operation": "opération", "operations": "opérations", "protection": "protection",
    "repetition": "répétition", "selection": "sélection", "situation": "situation",
    "decision": "décision", "precision": "précision", "ration": "ration",
    "larvee": "larvée", "documente": "documenté", "rappelee": "rappelée",
    "arretee": "arrêtée", "fortifie": "fortifié", "fortifiee": "fortifiée",
    "modernise": "modernisé", "declare": "déclare", "proteger": "protéger",
    "prospere": "prospère", "complete": "complète", "eleve": "élevé",
    "abandonne": "abandonné", "abandonnes": "abandonnés", "facilite": "facilite",
    "deja": "déjà", "interets": "intérêts", "evenements": "événements",
    "evasion": "évasion", "eviter": "éviter", "enquete": "enquête",
    "acces": "accès", "interieur": "intérieur",
    "deuxieme": "deuxième", "denier": "dénier", "traite": "traité",
    "enquetes": "enquêtes", "equipe": "équipe", "equipes": "équipes",
    "interroger": "interroger", "tactique": "tactique", "ennemi": "ennemi",
    "ennemis": "ennemis", "verifiable": "vérifiable", "verifiables": "vérifiables",
}

# Mots a ne surtout pas toucher (anglais des references, noms propres)
PROTECT = [
    "Any", "The", "Story", "Kamona", "Arena", "Breakout", "Infinite", "Ops", "Tac",
    "Covert", "Utopia", "Elysium", "Documentary", "Season", "Dusk", "Dawn", "White",
    "Nights", "Airport", "Hunt", "Red", "Smoke", "The Key", "Rat", "Dogtag", "Golden",
    "Opportunity", "No Man's Land", "First Season Documentary", "Summit", "Secure",
    "Gear", "No Fear", "Ignition", "Disconcert", "Uncharted", "Awaken", "Outcast",
    "All", "Contract", "Mission", "Official", "Overview", "Dark", "Zone", "Blackout",
    "Peacemaker", "Cleaners", "Arachne", "Apostle", "Gungnir", "Toland", "Ark",
    "Legend", "Shot", "Edge", "War", "Blue", "Lines", "Player", "Unknown", "Now",
    "In", "On", "At", "To", "It", "Is", "No", "One", "Up", "Out", "And", "For",
    "With", "From", "This", "That", "What", "When", "Where", "Who", "Why", "How",
    "Champion", "Legends", "Fall", "Rise", "Stars", "Echoes", "Legacy", "Title",
    "Reborn", "Phoenix", "Vanguard", "Strike", "Steel", "Iron", "Wolf", "Wolves",
    "Blackgold", "Colom", "Tevilla", "Sumek", "Mad Dogs", "Antonio", "Renoir",
    "Ajax", "Hecate", "Obol", "Viper", "Fred", "Porrero", "Derwin", "Rodriquez",
    "Stephen", "Mihalio", "Edelweiss", "Evita", "Elite", "Boss", "Token", "Tokeng",
    "Supply", "Drops", "Warlord", "Tournament", "Resident", "Evil", "Global",
    "Player", "Value", "Type", "Ammo", "Chart", "Red", "Drops", "Mr", "Smelter",
    "Collection", "Room", "Lunar", "Soil", "Sample", "Chaotic", "Matter", "Distorted",
    "Night", "Owl", "Detective", "Agency", "Lab", "Gold", "Bar", "Dark", "Chocolate",
    "Salvage", "Cargo", "Secret", "Document", "Special", "Forces", "Fumigators",
    "Grenadiers", "Breachers", "Mastery", "Transcend", "Hostile", "Sector",
]

# Corrections de contexte (avant le dictionnaire)
PHRASES = [
    ("l'Armery", "l'Armory"),
    ("carrying des echantillons", "transportant des échantillons"),
    ("comme des forceurs", "comme des mandataires"),
    ("desressingeurs", "des mandataires"),
    ("valeur narrative + idofficielle", "valeur narrative et officielle"),
    ("Valeur narrative +idofficielle", "valeur narrative et officielle"),
    ("qui recovers des documents", "qui récupère des documents"),
    ("action collective Documented", "action collective documentée"),
    ("leurs AFFaires", "leurs affaires"),
    ("les grandes puissances commutent les operateurs locaux",
     "les grandes puissances emploient les opérateurs locaux"),
    ("un programme de recherche militaire ou corporate",
     "un programme de recherche militaire ou industriel"),
    ("Un poor en loot", "Un pauvre en loot"),
    ("le marche noir", "le marché noir"),
    ("de marche noir", "de marché noir"),
    ("marche noir", "marché noir"),
    ("son recit (RPK-16 a tambour", "son récit (RPK-16 à tambour"),
    ("la ou se concentrent", "là où se concentrent"),
    ("n'a pas explose", "n'a pas explosé"),
    ("des officiers choisit de partir", "des officiers choisissent de partir"),
    ("prise de guerre decisive", "prise de guerre décisive"),
    ("de Kamona dispose de deux cuirass", "de Kamona disposait de deux cuirassés"),
    (" refuse de couler", " a refusé de couler"),
    ("qui a garde sa dignity", "qui a gardé sa dignité"),
    ("le lieu ou la metaphore", "le lieu où la métaphore"),
    ("ne s'arrete pas", "ne s’arrête pas"),
    ("c'est la que se joue", "c’est là que se joue"),
    ("Pour proteger ses vols", "Pour protéger ses vols"),
    ("et enqueter sur", "et enquêter sur"),
    ("et redirige la derniere batterie", "et redirige la dernière batterie"),
    ("Renoir Brady est accuse", "Renoir Brady est accusé"),
    ("est le nom donne au territory", "est le nom donné au territoire"),
    ("n'y est presente", "n’y est présente"),
    ("celui-la", "celui-là"),
    ("ce jour-la", "ce jour-là"),
    ("la contacte par radio", "la contacte par radio"),
    ("l'ecret de l'avion", "le secret de l’avion"),
    ("Le detail est lit pour", "Le détail est lu pour"),
    ("au capital transporte", "au capital transporté"),
    ("a explicitement indique", "a explicitement indiqué"),
    ("aux installations situes sous", "aux installations situées sous"),
    ("Le Comite requisitionne ensuite", "Le Comité réquisitionne ensuite"),
    ("est|deliberement", "est délibérément"),
    ("comme having incubé sous", "qui aurait incubé sous"),
    ("comme having incub sous", "qui aurait incubé sous"),
    ("ne le mentionne dans les", "ne le mentionne pas dans les"),
    ("presente dans les theories communautaires", "présent dans les théories communautaires"),
    ("La regle qui resume", "La règle qui résume"),
    ("l'equipement decide de l'issue", "l’équipement décide de l’issue"),
    ("aurait possede la", "aurait possédé la"),
    ("l'Operation Blackout", "l’Operation Blackout"),
    ("Signal Interference", "Signal Interference"),
    ("Kamona Liberation Army", "Kamona Liberation Army"),
    ("Marulos Liberation Army", "Marulos Liberation Army"),
    ("Liberation Army", "Liberation Army"),
    ("n'a pas", "n’a pas"), ("n'a jamais", "n’a jamais"),
    ("n'ayant", "n’ayant"), ("n'est", "n’est"), ("n'y", "n’y"),
    ("c'est", "c’est"), ("qu'il", "qu’il"), ("d'Oh", "d’Oh"),
    ("l'interface", "l’interface"),
]



# "a" verbe avoir : a proteger les occurrences
KEEP_A = [
    "n’a pas", "n’a jamais", "a ete", "a été", "qui a garde", "a gardé",
    "Le studio a explicitement", "Qui a fabrique", "a avoir", "a l’air",
    "Le Polaris a refusé", "a réussi", "a échoué", "a gagné", "a perdu",
    "Il a", "Elle a", "On a", "qui a", "n’a", "l’a", "d’a", "qu’a", "s’a",
    "c’a", "j’a", "m’a", "t’a", "L’a", "N’a", "D’a", "C’a", "S’a", "J’a",
]


def _text_segments(text):
    """Decoupe en segments (balise, texte). On n'accentue que le texte."""
    return re.split(r'(<[^>]+>)', text)


PROTECT_WORDS = [
    "Signal Interference",
    "Kamona Liberation Army",
    "Marulos Liberation Army",
    "Operation Blackout",
    "Operation Peacemaker",
    "Story of Kamona",
]


VERB_A_PATTERNS = [
    r"(?<![A-Za-zÀ-ÿ])n[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])l[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])d[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])qu[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])s[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])c[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])j[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])m[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])t[\u2019']a(?![A-Za-zÀ-ÿ])",
    r"(?<![A-Za-zÀ-ÿ])a(?= ete\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= garde\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= explicitement\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= fabrique\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= refuse\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= refusé\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= reussi\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= reussi\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= echoue\b)",
    r"(?<![A-Za-zÀ-ÿ])a(?= gagne\b)",
]


def _restore_case(orig: str, acc: str) -> str:
    if orig.isupper():
        return acc.upper()
    if orig[:1].isupper():
        return acc[:1].upper() + acc[1:]
    return acc


def _accentuate_text(seg: str) -> str:
    # 1. Corrections de contexte
    for a, b in PHRASES:
        seg = seg.replace(a, b)
    # 2. Protection des "a" verbaux
    for pat in VERB_A_PATTERNS:
        seg = re.sub(pat, lambda m: m.group(0)[:-1] + "\x02", seg)
    # 3. "ou" adverbe -> "ou"
    for a, b in [("ou deux puissances", "où deux puissances"),
                 ("ou une action collective", "où une action collective"),
                 ("ou subsistent", "où subsistent"),
                 ("ou le conflit se poursuit", "où le conflit se poursuit"),
                 ("ou le jeu relie", "où le jeu relie"),
                 ("ou l’on meurt", "où l’on meurt"),
                 ("ou la neige", "où la neige"),
                 ("ou vous etes", "où vous êtes"),
                 ("ou a un site", "où à un site")]:
        seg = seg.replace(a, b)
    # 3b. Protection des noms propres
    prot = []
    for w in PROTECT_WORDS:
        if w in seg:
            prot.append(w)
            seg = seg.replace(w, "\x03%d\x03" % (len(prot) - 1))
    # 4. Dictionnaire (insensible a la casse)
    for w, acc in DICT.items():
        seg = re.sub(r"(?<![A-Za-zÀ-ÿ])" + w + r"(?![A-Za-zÀ-ÿ])",
                     lambda m, a=acc: _restore_case(m.group(0), a), seg, flags=re.I)
    # 5. "a" preposition + restauration
    seg = re.sub(r"(?<![A-Za-zÀ-ÿ])a(?![A-Za-zÀ-ÿ])", "à", seg)
    seg = seg.replace("\x02", "a")
    # 5b. Restauration des noms propres
    for i, w in enumerate(prot):
        seg = seg.replace("\x03%d\x03" % i, w)
    # 6. Apostrophes typographiques
    for a, b in [("l'", "l’"), ("d'", "d’"), ("qu'", "qu’"), ("n'", "n’"),
                 ("s'", "s’"), ("c'", "c’"), ("j'", "j’"), ("m'", "m’"),
                 ("t'", "t’"), ("L'", "L’"), ("N'", "N’"), ("D'", "D’"),
                 ("C'", "C’"), ("S'", "S’"), ("J'", "J’"), ("M'", "M’"),
                 ("T'", "T’"), ("Qu'", "Qu’")]:
        seg = seg.replace(a, b)
    return seg


def accentuate(text: str) -> str:
    parts = _text_segments(text)
    out = []
    for i, part in enumerate(parts):
        if part.startswith("<"):
            out.append(part)
        else:
            out.append(_accentuate_text(part))
    return "".join(out)


if __name__ == "__main__":
    p = sys.argv[1]
    import pathlib
    f = pathlib.Path(p)
    s = f.read_text(encoding="utf-8")
    f.write_text(accentuate(s), encoding="utf-8")
    print("Accentue :", p)
