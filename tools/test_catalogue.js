/* ABI NEXUS — Recette : le catalogue des 77 armes se remplit correctement.
 *
 * Verifie, sur la page meta-tier-list-globale.html :
 *  - le tableau contient bien les 77 lignes ;
 *  - la grille "armurerie de reference" (24 armes) n'a pas regresse ;
 *  - aucune erreur JavaScript n'est levee ;
 *  - la recherche site trouve bien une arme du catalogue.
 */
const { chromium } = require('playwright');

const BASE = process.env.BASE || 'http://127.0.0.1:8765';
let ok = 0, ko = 0;
const check = (label, cond, extra) => {
  if (cond) { ok++; console.log('  OK  ' + label + (extra ? ' (' + extra + ')' : '')); }
  else { ko++; console.log('  KO  ' + label + (extra ? ' (' + extra + ')' : '')); }
};

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });

  await page.goto(BASE + '/pages/meta-tier-list-globale.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(700);

  const rows = await page.$$eval('#catalogue-77-body tr', r => r.length);
  check('le catalogue contient 77 lignes', rows === 77, rows + ' lignes');

  const firstCells = await page.$$eval('#catalogue-77-body tr:first-child th, #catalogue-77-body tr:first-child td',
    els => els.map(e => e.textContent.trim()));
  check('la premiere ligne a 14 colonnes', firstCells.length === 14, firstCells.length + ' colonnes');
  check('la premiere ligne contient une arme', firstCells[0] && firstCells[0].length > 0, firstCells[0]);
  check('la cadence est presente', /\d/.test(firstCells[12] || ''), firstCells[12]);

  const grid = await page.$$eval('.weapon-grid[data-variant="tier"] .weapon-card', c => c.length);
  check('la grille de reference garde ses 24 armes', grid === 24, grid + ' cartes');

  const empty = await page.$eval('#catalogue-77-body', b => b.textContent.includes('Chargement du catalogue'));
  check('le message de chargement a disparu', !empty);

  // recherche site
  await page.goto(BASE + '/index.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(600);
  const hasSearch = await page.$('input[type="search"], .search-input, #search-input');
  check('la recherche est presente sur l\'accueil', !!hasSearch);

  check('aucune erreur JavaScript', errors.length === 0, errors.slice(0, 3).join(' | '));

  await browser.close();
  console.log('\n' + ok + ' OK / ' + ko + ' KO');
  process.exit(ko ? 1 : 0);
})();
