#!/usr/bin/env python3
"""Appariement intelligent site <-> wiki ABI, avec score de confiance."""
import json, re, pathlib, difflib

ROOT = pathlib.Path('.')

TYPE_SUFFIX = {
    'assault rifle': ['Assault Rifle'],
    'marksman rifle': ['Marksman Rifle', 'DMR'],
    'smg': ['Micro SMG', 'SMG'],
    'sniper rifle': ['Sniper Rifle'],
    'shotgun': ['Shotgun'],
    'pistol': ['Pistol'],
    'lmg': ['Light Machine Gun'],
    'carbine': ['Carbine'],
}


def normalize(s):
    s = s.lower().replace('&', ' and ')
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r"['’]", '', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    return s


def match(entity, idx_norm):
    """idx_norm : {cle normalisee -> titre wiki}. Retourne (titre, score)."""
    name = entity['name']
    cat = (entity.get('category') or '').lower()
    base = normalize(name)

    # 1. nom exact
    if base in idx_norm:
        return idx_norm[base], 1.0
    # 2. nom + suffixe de type
    for suf in TYPE_SUFFIX.get(cat, []):
        k = normalize('%s %s' % (name, suf))
        if k in idx_norm:
            return idx_norm[k], 0.98
        k2 = normalize('%s %s' % (name.replace('-', '').replace('.', ''), suf))
        if k2 in idx_norm:
            return idx_norm[k2], 0.96
    # 3. variante sans ponctuation
    for variant in (name.replace('-', ''), name.replace('.', ''), name.replace(' ', '')):
        k = normalize(variant)
        if k in idx_norm:
            return idx_norm[k], 0.95
    # 4. prefixe : le nom du site est le debut du titre wiki
    pref = sorted((len(k), idx_norm[k]) for k in idx_norm if k.startswith(base))
    if pref:
        return pref[0][1], 0.9
    # 5. similarite
    close = difflib.get_close_matches(base, list(idx_norm.keys()), n=1, cutoff=0.8)
    if close:
        return idx_norm[close[0]], 0.7
    # 6. nom du fichier image actuel
    stem = normalize(pathlib.Path(entity.get('image', '')).stem)
    if stem in idx_norm:
        return idx_norm[stem], 0.85
    for k in sorted(idx_norm):
        if stem and (k.startswith(stem) or stem.startswith(k)):
            return idx_norm[k], 0.78
    return None, 0.0


if __name__ == '__main__':
    idx_norm = json.load(open('tools/_wiki_index.json'))['index']
    ents = []
    for jf, key in (('js/data-weapons.json', 'weapons'),
                    ('js/data-items.json', 'items'),
                    ('js/data-armors.json', 'armors')):
        d = json.loads((ROOT / jf).read_text(encoding='utf-8'))
        for e in d.get(key, []):
            ents.append({'src': key, 'name': e['name'], 'id': e['id'],
                         'category': e.get('category', ''),
                         'image': e.get('image', '')})
    res, miss = [], []
    for e in ents:
        title, score = match(e, idx_norm)
        if title:
            res.append({**e, 'wiki': title, 'score': round(score, 2)})
        else:
            miss.append(e)
    print('Correspondances : %d / %d' % (len(res), len(ents)))
    for r in res:
        flag = '' if r['score'] >= 0.85 else '   <- a verifier'
        print('  %-9s %-26s -> %-44s (%.2f)%s'
              % (r['src'][:9], r['name'][:26], r['wiki'][:44], r['score'], flag))
    print('\nNON TROUVES : %d' % len(miss))
    for m in miss:
        print('  %-9s %s' % (m['src'][:9], m['name']))
    json.dump(res, open('tools/_wiki_matches.json', 'w'), ensure_ascii=False, indent=1)
