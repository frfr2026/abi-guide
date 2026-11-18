const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Découvre automatiquement toutes les pages Html câblées avec une narration.
// Le catalogue ne peut plus être obsolète : la source de vérité est le HTML.
const ROOT = path.resolve(__dirname, '..');
const PAGES_DIR = path.join(ROOT, 'pages');

function decouvrir() {
  const trouvees = [];
  for (const f of fs.readdirSync(PAGES_DIR).filter(n => n.endsWith('.html')).sort()) {
    const src = fs.readFileSync(path.join(PAGES_DIR, f), 'utf8');
    const m = src.match(/class="audio-narration"[^>]*data-track="([^"]+)"/);
    if (m) trouvees.push({ slug: f.replace(/\.html$/, ''), track: m[1] });
  }
  return trouvees;
}

(async () => {
  const pages = decouvrir();
  console.log(`Pages narrées détectées : ${pages.length}`);
  if (!pages.length) { console.log('Résultat : 0 réussites, 1 échec'); process.exit(1); }

  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });

  let ok = 0, fail = 0;
  const T = (c, m) => { c ? (ok++, console.log('  ✓', m)) : (fail++, console.log('  ✗', m)); };

  for (const { slug, track: attendu } of pages) {
    await p.goto(`http://127.0.0.1:8000/pages/${slug}.html`, { waitUntil: 'load' });
    const has = await p.locator('.audio-narration').count();
    T(has === 1, `${slug} : composant narration présent`);
    if (!has) continue;

    const track = await p.locator('.audio-narration').getAttribute('data-track');
    T(track === attendu, `${slug} : piste attendue (${attendu})`);
    const okTrack = await p.evaluate(async (t) => (await fetch(t)).ok, track);
    T(okTrack, `${slug} : piste ${track} accessible en HTTP`);

    const lbl = await p.locator('.audio-narration .audio-label').textContent();
    T(/Narration/i.test(lbl || ''), `${slug} : libellé "${lbl}"`);

    const played = await p.evaluate(async () => {
      const pl = document.querySelector('.audio-narration');
      pl.querySelector('button').click();
      await new Promise(r => setTimeout(r, 1200));
      const a = pl.querySelector('audio');
      return { paused: a.paused, t: a.currentTime, dur: a.duration };
    });
    T(!played.paused && played.t > 0,
      `${slug} : lecture démarrée (t=${played.t.toFixed(2)}s / ${played.dur ? played.dur.toFixed(1) : '?'}s)`);
    T(!played.dur || played.dur > 1, `${slug} : durée ${played.dur ? played.dur.toFixed(1) : '?'}s`);

    const w = await p.evaluate(() => {
      const el = document.querySelector('.audio-narration .audio-bar-fill');
      return el ? el.style.width : '';
    });
    T(parseFloat(w) > 0, `${slug} : barre de progression à ${w}`);

    await p.evaluate(() => {
      const pl = document.querySelector('.audio-narration');
      pl.querySelector('button').click();
    });
  }

  T(errs.length === 0, 'aucune erreur JavaScript : ' + (errs.slice(0, 3).join(' | ') || 'rien'));
  console.log(`\nRésultat : ${ok} réussites, ${fail} échecs`);
  await b.close();
  process.exit(fail ? 1 : 0);
})();
