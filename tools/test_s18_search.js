const { chromium } = require('/home/user/node_modules/playwright');

/**
 * ABI NEXUS — test_s18_search.js
 * Verifie que CHAQUE resultat de la recherche globale resout vers une
 * page reellement servie (HTTP 200), depuis la racine ET depuis pages/.
 * Le bug historique : search.js utilisait un prefixe unique pour les
 * liens de pages et le chargement des JSON, ce qui cassait tous les
 * resultats depuis l'accueil comme depuis les pages du guide.
 */
const BASE = process.argv[2] || 'http://127.0.0.1:8000';
let pass = 0, fail = 0;
const failures = [];
function ok(label, cond, detail) {
  if (cond) { pass++; console.log('  ✓ ' + label); }
  else { fail++; failures.push(label + (detail ? ' — ' + detail : '')); console.log('  ✗ ' + label + (detail ? ' — ' + detail : '')); }
}

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage();

  const ORIGINS = [
    { url: BASE + '/index.html', label: 'racine' },
    { url: BASE + '/pages/guide-debutant.html', label: 'pages/' }
  ];
  const QUERIES = ['ak', 'm4', 'munitions', 'saison 7', 'zombie', 'armure', 'guide'];

  let total = 0;
  for (const o of ORIGINS) {
    await p.goto(o.url, { waitUntil: 'networkidle' });
    for (const q of QUERIES) {
      await p.fill('.srch-input', q);
      await p.waitForTimeout(900);
      const hrefs = await p.$$eval('.srch-item', as => as.map(a => a.getAttribute('href')));
      if (!hrefs.length) continue;
      // resolution en URL absolue + verification HTTP
      const abs = await p.evaluate(hs => hs.map(h => new URL(h, location.href).href), hrefs);
      for (const u of abs) {
        total++;
        const r = await p.request.get(u);
        if (r.status() === 200) pass++;
        else { fail++; failures.push('HTTP ' + r.status() + ' sur ' + u); console.log('  ✗ HTTP ' + r.status() + ' sur ' + u); }
      }
    }
  }
  ok(`${total} resultats de recherche resolus en HTTP 200 (racine + pages/)`, fail === 0);

  // l'accueil doit etre findable
  await p.goto(BASE + '/pages/guide-debutant.html', { waitUntil: 'networkidle' });
  await p.fill('.srch-input', 'accueil');
  await p.waitForTimeout(900);
  const home = await p.$$eval('.srch-item', as => as.map(a => a.getAttribute('href')));
  ok('la page d\'accueil est indexee dans la recherche', home.some(h => /index\.html$/.test(h)), home.join(','));

  // navigation clavier + focus
  await p.keyboard.press('Escape');
  await p.waitForTimeout(300);
  const hidden = await p.evaluate(() => {
    const el = document.querySelector('.srch-panel');
    return el ? getComputedStyle(el).display === 'none' || el.hidden : false;
  });
  ok('Echap ferme le panneau de recherche', hidden);

  await b.close();
  console.log('\n═══ Résultat : ' + pass + ' réussites, ' + fail + ' échecs ═══');
  process.exit(fail ? 1 : 0);
})();
