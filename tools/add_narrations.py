#!/usr/bin/env python3
"""Ajoute le composant de narration audio aux pages concernees.

Le lecteur existant (audio-player) joue une ambiance en boucle. La narration
est un document long : elle ne doit pas boucler, elle doit avoir un etat
lecture / pause / termine, et un resume de position.

Composant : <div class="audio-narration" data-track="..." data-label="...">
"""
import pathlib, re

# ── 1. JavaScript : initialisation du lecteur de narration ────────────────
JS = pathlib.Path('js/main.js')
js = JS.read_text(encoding='utf-8')

ANCHOR = '''  /* ── 10. Parallaxe légère du hero ───────────────────────── */'''

NEW_JS = '''  /* ── 9 bis. Lecteur de narration (voix off, non bouclé) ──── */
  function initNarrationPlayer() {
    const player = $('.audio-narration');
    if (!player) return;
    const audio = $('audio', player) || document.createElement('audio');
    const track = player.dataset.track || '';
    const btn = $('button', player);
    const label = $('.audio-label', player);
    const bar = $('.audio-bar-fill', player);
    if (track) { audio.src = track; audio.preload = 'none'; }
    audio.volume = 0.9;

    const setIcon = () => {
      if (audio.ended) {
        btn.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
        btn.setAttribute('aria-label', 'Rejouer la narration');
        if (label) label.textContent = 'Rejouer la narration';
        return;
      }
      btn.innerHTML = audio.paused
        ? '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
      btn.setAttribute('aria-label', audio.paused ? 'Ecouter la narration' : 'Mettre la narration en pause');
    };

    btn.addEventListener('click', () => {
      if (!track) return;
      if (audio.ended) { audio.currentTime = 0; }
      audio.paused ? audio.play().catch(() => {}) : audio.pause();
      setIcon();
    });

    audio.addEventListener('play', setIcon);
    audio.addEventListener('pause', setIcon);
    audio.addEventListener('ended', setIcon);
    audio.addEventListener('timeupdate', () => {
      if (!bar || !audio.duration || !isFinite(audio.duration)) return;
      bar.style.width = (audio.currentTime / audio.duration * 100) + '%';
    });

    if (label && player.dataset.label) label.textContent = player.dataset.label;
    setIcon();
  }

  /* ── 10. Parallaxe légère du hero ───────────────────────── */'''

assert ANCHOR in js, 'ancre JS introuvable'
js = js.replace(ANCHOR, NEW_JS, 1)

# branche l'initialisation
CALL = "  initAudioPlayer();"
if CALL in js:
    js = js.replace(CALL, CALL + "\n    initNarrationPlayer();", 1)
else:
    # fallback : on insere apres l'appel a initAudioPlayer ailleurs
    m = re.search(r'\n(\s*)initAudioPlayer\(\);', js)
    if m:
        js = js[:m.end()] + "\n%sinitNarrationPlayer();" % m.group(1) + js[m.end():]
    else:
        raise SystemExit('appel initAudioPlayer introuvable')

JS.write_text(js, encoding='utf-8')
print('js/main.js : lecteur de narration ajoute')

# ── 2. CSS ────────────────────────────────────────────────────────────────
CSS = pathlib.Path('css/components.css')
css = CSS.read_text(encoding='utf-8')

CSS_ANCHOR = '/* ── Callout / alerte ─────────────────────────────────────── */'

NEW_CSS = '''/* ── Narration audio (voix off) ─────────────────────────── */
.audio-narration {
  position: fixed; right: var(--space-lg); bottom: var(--space-lg);
  z-index: var(--z-audio);
  display: flex; align-items: center; gap: var(--space-sm);
  background: rgba(17,19,24,.94); backdrop-filter: blur(10px);
  border: 1px solid var(--color-border); border-radius: 999px;
  padding: var(--space-xs) var(--space-md) var(--space-xs) var(--space-xs);
  box-shadow: var(--shadow-card); overflow: hidden;
}
.audio-narration button {
  width: 40px; height: 40px; border-radius: 50%; border: none; flex: 0 0 auto;
  background: var(--color-accent-gold); color: #0A0C0F;
  display: grid; place-items: center; transition: transform var(--transition-fast);
}
.audio-narration button:hover { transform: scale(1.08); }
.audio-narration button svg { width: 18px; height: 18px; }
.audio-narration .audio-label {
  font-family: var(--font-data); font-size: var(--fs-xs); letter-spacing: .1em;
  text-transform: uppercase; color: var(--color-text-secondary); white-space: nowrap;
}
.audio-narration .audio-bar {
  width: 90px; height: 3px; border-radius: 2px; flex: 0 0 auto;
  background: rgba(255,255,255,.12); overflow: hidden;
}
.audio-narration .audio-bar-fill {
  display: block; width: 0; height: 100%;
  background: var(--color-accent-gold); transition: width .2s linear;
}

''' + CSS_ANCHOR

assert CSS_ANCHOR in css, 'ancre CSS introuvable'
css = css.replace(CSS_ANCHOR, NEW_CSS, 1)
CSS.write_text(css, encoding='utf-8')
print('css/components.css : style du lecteur de narration ajoute')

# responsive : sur petit ecran, le libelle disparait
RESP = pathlib.Path('css/responsive.css')
r = RESP.read_text(encoding='utf-8')
if '.audio-narration' not in r:
    anchor = '  .audio-player .audio-label { display: none; }'
    if anchor in r:
        r = r.replace(anchor, anchor + '''
  .audio-narration { right: var(--space-md); bottom: var(--space-md); }
  .audio-narration .audio-label { display: none; }
  .audio-narration .audio-bar { width: 56px; }''')
        RESP.write_text(r, encoding='utf-8')
        print('css/responsive.css : regle mobile ajoutee')
    else:
        print('ATTENTION : ancre responsive introuvable')

# ── 3. Insertion du composant dans les pages ──────────────────────────────
PAGES = [
    ('pages/guide-debutant.html', 'narration-guide-debutant.mp3', 'Guide debutant'),
    ('pages/guide-extraction.html', 'narration-guide-extraction.mp3', 'Guide extraction'),
    ('pages/map-valley.html', 'narration-map-valley.mp3', 'Guide Valley'),
    ('pages/map-no-mans-land.html', 'narration-map-no-mans-land.mp3', 'Guide No Man\'s Land'),
    ('pages/armes-tier-list.html', 'narration-armes-tier-list.mp3', 'Tier list armes'),
]

for f, track, label in PAGES:
    p = pathlib.Path(f)
    s = p.read_text(encoding='utf-8')
    if 'audio-narration' in s:
        print('deja present :', f)
        continue
    # on insere avant le lecteur d'ambiance existant (ou avant le back-to-top)
    depth = '../' if f.startswith('pages/') else ''
    html = ('  <div class="audio-narration" data-track="%saudio/%s" data-label="Narration : %s">\n'
            '    <button aria-label="Ecouter la narration"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>\n'
            '    <span class="audio-label">Narration</span>\n'
            '    <span class="audio-bar"><span class="audio-bar-fill"></span></span>\n'
            '  </div>\n') % (depth, track, label)
    m = re.search(r'  <div class="audio-player"', s)
    if m:
        s = s[:m.start()] + html + s[m.start():]
    else:
        m = re.search(r'  <button class="back-to-top"', s)
        if not m:
            raise SystemExit('point d insertion introuvable dans ' + f)
        s = s[:m.start()] + html + s[m.start():]
    p.write_text(s, encoding='utf-8')
    print('composant insere :', f)
