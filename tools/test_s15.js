/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — tests S15 (jsdom)
   Vérifie que les cinq modules interactifs se montent réellement
   dans les pages, que les calculs sont cohérents et qu'aucune
   erreur JavaScript n'est levée.

   Usage : node tools/test_s15.js
   ════════════════════════════════════════════════════════════════ */
'use strict';

const http = require('http');
const fs = require('fs');
const path = require('path');
const { JSDOM, VirtualConsole } = require('jsdom');

const ROOT = path.resolve(__dirname, '..');
const MIME = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png',
  '.svg': 'image/svg+xml', '.webp': 'image/webp', '.ico': 'image/x-icon'
};

let PASS = 0, FAIL = 0;
const failures = [];

function ok(label, cond, extra) {
  if (cond) { PASS++; console.log('  ✓ ' + label); }
  else { FAIL++; failures.push(label + (extra ? ' → ' + extra : '')); console.log('  ✗ ' + label + (extra ? ' → ' + extra : '')); }
}

const server = http.createServer((req, res) => {
  let rel = decodeURIComponent(req.url.split('?')[0]);
  if (rel === '/') rel = '/index.html';
  const file = path.join(ROOT, rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    res.writeHead(404); res.end('not found'); return;
  }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});

function startServer() {
  return new Promise(resolve => server.listen(0, '127.0.0.1', () => resolve(server.address().port)));
}

async function loadPage(port, pagePath, waitMs) {
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => errors.push(e.message + (e.detail ? ' :: ' + e.detail : '')));
  vc.on('error', (...a) => errors.push(a.map(String).join(' ')));
  vc.on('warn', () => {});
  vc.on('info', () => {});
  vc.on('log', () => {});

  const dom = await JSDOM.fromURL('http://127.0.0.1:' + port + pagePath, {
    runScripts: 'dangerously',
    resources: 'usable',
    pretendToBeVisual: true,
    virtualConsole: vc,
    beforeParse(window) {
      window.fetch = (input, init) => {
        const u = typeof input === 'string' ? new URL(input, window.location.href) : input;
        return fetch(u, init);
      };
      window.IntersectionObserver = class {
        constructor(cb) { this.cb = cb; }
        observe(el) { this.cb([{ isIntersecting: true, target: el, intersectionRatio: 1 }], this); }
        unobserve() {} disconnect() {} takeRecords() { return []; }
      };
      window.matchMedia = window.matchMedia || function () {
        return { matches: false, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} };
      };
    }
  });
  await new Promise(r => setTimeout(r, waitMs || 1200));
  return { dom, window: dom.window, doc: dom.window.document, errors };
}

/* ───────────────────────────────────────────────────────────── */
(async function main() {
  const port = await startServer();
  console.log('\n═══ ABI NEXUS — Tests S15 ═══\n');

  /* ── 1. Recherche globale ─────────────────────────────────── */
  console.log('1. Recherche globale (js/search.js)');
  {
    const { window, doc, errors } = await loadPage(port, '/index.html', 1500);
    const input = doc.querySelector('.srch-input');
    ok('champ de recherche injecté dans la navigation', !!input);
    ok('panneau de résultats présent', !!doc.querySelector('.srch-panel'));

    input.value = 'a545';
    input.dispatchEvent(new window.Event('input', { bubbles: true }));
    await new Promise(r => setTimeout(r, 400));
    const items = doc.querySelectorAll('.srch-panel .srch-item');
    ok('la saisie "a545" renvoie des résultats', items.length > 0, items.length + ' résultats');
    ok('A545 est trouvé', Array.from(items).some(i => i.textContent.indexOf('A545') !== -1));

    input.value = 'zzzzzzintrouvable';
    input.dispatchEvent(new window.Event('input', { bubbles: true }));
    await new Promise(r => setTimeout(r, 400));
    ok('une requête sans correspondance affiche un message', !!doc.querySelector('.srch-empty'));

    input.value = 'm4a1';
    input.dispatchEvent(new window.Event('input', { bubbles: true }));
    await new Promise(r => setTimeout(r, 400));
    ok('la recherche ignore la casse et les accents (M4A1)', Array.from(doc.querySelectorAll('.srch-item')).some(i => i.textContent.indexOf('M4A1') !== -1));

    const pageLinks = Array.from(doc.querySelectorAll('.srch-panel .srch-item')).map(a => a.getAttribute('href'));
    ok('les résultats pointent vers des URL relatives valides', pageLinks.every(h => h && !h.startsWith('http')), pageLinks.slice(0, 3).join(', '));

    ok('aucune erreur JavaScript sur index.html', errors.length === 0, errors.join(' | '));
    window.close();
  }

  /* ── 2. Constructeur de loadout ───────────────────────────── */
  console.log('\n2. Constructeur de kit (js/loadout-builder.js)');
  {
    const { window, doc, errors } = await loadPage(port, '/pages/meta-loadout-optimizer.html', 1800);
    const root = doc.querySelector('.loadout-builder');
    ok('bloc constructeur présent sur la page', !!root);
    ok('le mode est alimenté', doc.querySelector('#lb-mode').options.length === 3, doc.querySelector('#lb-mode').options.length + ' options');
    ok('les armes sont listées', doc.querySelector('#lb-weapon').options.length === 25, doc.querySelector('#lb-weapon').options.length + ' options');
    ok('les gilets sont listés', doc.querySelector('#lb-armor').options.length === 15, doc.querySelector('#lb-armor').options.length + ' options');

    // Sélection A545 + munition + gilet BT101
    const w = doc.querySelector('#lb-weapon');
    w.value = 'a545'; w.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 300));
    ok('la sélection d’une arme charge les munitions du calibre', doc.querySelector('#lb-ammo').options.length > 1);

    const m = doc.querySelector('#lb-ammo');
    m.value = m.options[1].value; m.dispatchEvent(new window.Event('change', { bubbles: true }));
    const a = doc.querySelector('#lb-armor');
    a.value = 'bt101'; a.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 400));

    const out = doc.querySelector('.lb-out');
    ok('le résultat est calculé', out.innerHTML.indexOf('lb-summary') !== -1);
    const costText = out.querySelector('.lb-cell .lb-v').textContent;
    ok('un coût total est affiché', /\d/.test(costText), costText);

    // Recalcul manuel du coût attendu
    const weapons = JSON.parse(fs.readFileSync(path.join(ROOT, 'js/data-weapons.json'), 'utf8')).weapons;
    const armors = JSON.parse(fs.readFileSync(path.join(ROOT, 'js/data-armors.json'), 'utf8')).armors;
    const ammo = JSON.parse(fs.readFileSync(path.join(ROOT, 'js/data-ammo.json'), 'utf8')).ammo;
    const builds = JSON.parse(fs.readFileSync(path.join(ROOT, 'js/data-builds.json'), 'utf8'));
    const weapon = weapons.find(x => x.id === 'a545');
    const armor = armors.find(x => x.id === 'bt101');
    const mun = ammo.find(x => x.id === m.options[1].value);
    const gear = builds.gear.normal;
    const expected = weapon.price + armor.price + mun.price * 120
      + gear.helmet.price + gear.rig.price + gear.backpack.price + gear.headset.price + gear.medical.price;
    const shown = parseFloat(costText.replace(/[^\d]/g, '')) * 1000;
    ok('le coût affiché correspond au calcul attendu', Math.abs(shown - expected) < 1500,
      'affiché ' + shown + ' vs attendu ' + expected);

    // Le gilet T6 en mode Normal doit déclencher un avertissement
    ok('une incompatibilité de tier est signalée', out.innerHTML.indexOf('Points de vigilance') !== -1);
    ok('la masse du kit est calculée', /\d+\.\d kg/.test(out.innerHTML), (out.innerHTML.match(/[\d.]+ kg/) || [''])[0]);
    ok('la mobilité est calculée', out.innerHTML.indexOf('Mobilité') !== -1);

    // Basculer en Forbidden : l'avertissement T6 doit disparaître
    const mode = doc.querySelector('#lb-mode');
    mode.value = 'forbidden'; mode.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 400));
    const a2 = doc.querySelector('#lb-armor');
    a2.value = 'bt101'; a2.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 400));
    ok('le mode Forbidden est pris en compte', Number(doc.querySelector('#lb-budget').max) === 3500000, 'max=' + doc.querySelector('#lb-budget').max);

    ok('aucune erreur JavaScript sur la page optimizer', errors.length === 0, errors.join(' | '));
    window.close();
  }

  /* ── 3. Comparateur d'armes ───────────────────────────────── */
  console.log('\n3. Comparateur d’armes (js/weapon-compare.js)');
  {
    const { window, doc, errors } = await loadPage(port, '/pages/armes-tier-list.html', 1800);
    ok('bloc comparateur présent', !!doc.querySelector('.weapon-compare'));
    const sa = doc.querySelector('#wc-a'), sb = doc.querySelector('#wc-b');
    ok('les deux listes sont alimentées', sa.options.length === 24 && sb.options.length === 24, sa.options.length + '/' + sb.options.length);

    sa.value = 'a545'; sa.dispatchEvent(new window.Event('change', { bubbles: true }));
    sb.value = 'vector'; sb.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 300));

    const rows = doc.querySelectorAll('.wc-table tbody tr');
    ok('le tableau comparatif est rendu', rows.length === 6, rows.length + ' lignes');
    ok('les munitions compatibles sont indiquées', doc.querySelector('.lb-kit').textContent.indexOf('PL') !== -1);
    ok('un rapport coût / performance est calculé', doc.querySelector('.wc-out').textContent.indexOf('rapport') !== -1);

    // Vector .45 a le RPM le plus élevé : il doit être marqué meilleur
    const rpmRow = Array.from(rows).find(r => r.textContent.indexOf('Cadence') !== -1);
    const cells = rpmRow.querySelectorAll('td');
    ok('la meilleure cadence est mise en évidence', cells[2].className.indexOf('best') !== -1, 'classe=' + cells[2].className);

    // Échange
    doc.querySelector('#wc-swap').dispatchEvent(new window.Event('click', { bubbles: true }));
    await new Promise(r => setTimeout(r, 200));
    ok('le bouton d’échange inverse les deux armes', doc.querySelector('#wc-a').value === 'vector' && doc.querySelector('#wc-b').value === 'a545');

    ok('aucune erreur JavaScript sur la page tier list', errors.length === 0, errors.join(' | '));
    window.close();
  }

  /* ── 4. Tier list interactive ─────────────────────────────── */
  console.log('\n4. Tier list interactive (js/tier-list.js)');
  {
    const { window, doc, errors } = await loadPage(port, '/pages/armes-tier-list.html', 1800);
    const board = doc.querySelector('.tlx-board');
    ok('le plateau de tier list est rendu', !!board);
    const chips = doc.querySelectorAll('.tlx-chip');
    ok('les 24 armes sont réparties en puces', chips.length === 24, chips.length + ' puces');
    const tiers = doc.querySelectorAll('.tlx-tier');
    ok('quatre tiers sont affichés', tiers.length === 4);

    // Le consensus doit être réparti sur les quatre tiers
    const counts = Array.from(tiers).map(t => t.querySelectorAll('.tlx-chip').length);
    ok('chaque tier contient au moins une arme', counts.every(c => c > 0), counts.join('/'));

    // Source affichée
    const src = doc.querySelector('.tlx-sources').textContent;
    ok('les sources communautaires sont citées', src.indexOf('qrts.ru') !== -1 && src.indexOf('Communautaire') !== -1);
    ok('la mention « non officiel » est présente', /n\s*.{0,3}est l\s*.{0,3}éditeur|jamais une classification officielle/i.test(doc.querySelector('.tlx-sources').textContent));

    // Clavier : Espace fait descendre la puce d'un tier
    const firstChip = doc.querySelector('.tlx-drop[data-tier="S"] .tlx-chip');
    const before = doc.querySelectorAll('.tlx-drop[data-tier="S"] .tlx-chip').length;
    firstChip.dispatchEvent(new window.KeyboardEvent('keydown', { key: ' ', bubbles: true }));
    await new Promise(r => setTimeout(r, 300));
    const after = doc.querySelectorAll('.tlx-drop[data-tier="S"] .tlx-chip').length;
    ok('la touche Espace fait descendre l’arme d’un tier', after === before - 1, before + ' → ' + after);

    // Persistance locale
    const stored = window.localStorage.getItem('abi-nexus-tier-list-v1');
    ok('le classement personnalisé est enregistré', !!stored && stored.length > 10);
    const parsed = JSON.parse(stored || '{}');
    ok('les quatre tiers sont persistés', ['S', 'A', 'B', 'C'].every(t => Array.isArray(parsed[t])));

    // Réinitialisation
    doc.querySelector('#tlx-reset').dispatchEvent(new window.Event('click', { bubbles: true }));
    await new Promise(r => setTimeout(r, 300));
    ok('la réinitialisation restaure le consensus', doc.querySelectorAll('.tlx-chip').length === 24);

    ok('aucune erreur JavaScript sur la tier list', errors.length === 0, errors.join(' | '));
    window.close();
  }

  /* ── 5. Explorateur de cartes ─────────────────────────────── */
  console.log('\n5. Explorateur de cartes (js/map-explorer.js)');
  {
    const { window, doc, errors } = await loadPage(port, '/pages/meta-stratégies-s7.html', 1800);
    ok('bloc explorateur présent', !!doc.querySelector('.map-explorer'));
    let cards = doc.querySelectorAll('.mx-card');
    ok('les 6 cartes reelles sont affichees', cards.length === 6, cards.length + ' cartes');
    ok('le compteur de cartes est renseigne', /6 cartes/.test(doc.querySelector('#mx-count').textContent));

    // Filtre infectées
    const inf = doc.querySelector('#mx-infected');
    inf.value = 'oui'; inf.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 250));
    cards = doc.querySelectorAll('.mx-card');
    ok('le filtre « infectees » reduit la liste', cards.length === 3, cards.length + ' cartes');
    ok('Farm est dans les cartes infectées', Array.from(cards).some(c => c.textContent.indexOf('Farm') !== -1));

    // Filtre mode
    const mod = doc.querySelector('#mx-mode');
    mod.value = 'Zombie Endless'; mod.dispatchEvent(new window.Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 250));
    cards = doc.querySelectorAll('.mx-card');
    ok('le filtre par mode Zombie Endless isole Airport', cards.length === 1 && cards[0].textContent.indexOf('Airport') !== -1, cards.length + ' carte(s)');

    // Réinitialisation
    doc.querySelector('#mx-reset').dispatchEvent(new window.Event('click', { bubbles: true }));
    await new Promise(r => setTimeout(r, 250));
    ok('la reinitialisation restaure les 6 cartes', doc.querySelectorAll('.mx-card').length === 6);

    // Chaque carte renvoie vers sa fiche
    const hrefs = Array.from(doc.querySelectorAll('.mx-card a.btn')).map(a => a.getAttribute('href'));
    ok('chaque carte pointe vers sa fiche', hrefs.length === 6 && hrefs.every(h => /^map-[a-z\-]+\.html$/.test(h)), hrefs.join(','));

    ok('aucune erreur JavaScript sur la page stratégies', errors.length === 0, errors.join(' | '));
    window.close();
  }

  /* ── 6. Intégration globale ───────────────────────────────── */
  console.log('\n6. Intégration globale');
  {
    const pages = fs.readdirSync(path.join(ROOT, 'pages')).filter(f => f.endsWith('.html'));
    let withSearch = 0;
    pages.forEach(f => {
      const s = fs.readFileSync(path.join(ROOT, 'pages', f), 'utf8');
      if (s.indexOf('js/search.js') !== -1) withSearch++;
    });
    ok('toutes les pages chargent le module de recherche',
       withSearch === pages.length, withSearch + '/' + pages.length);
    const idx = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
    ok('index.html charge le module de recherche', idx.indexOf('js/search.js') !== -1);

    // Aucune page ne doit référencer un module S15 inexistant
    const mods = ['search.js', 'loadout-builder.js', 'weapon-compare.js', 'map-explorer.js', 'tier-list.js'];
    let missing = [];
    pages.concat(['../index.html']).forEach(f => {
      const p = f === '../index.html' ? path.join(ROOT, 'index.html') : path.join(ROOT, 'pages', f);
      const s = fs.readFileSync(p, 'utf8');
      mods.forEach(m => {
        if (s.indexOf(m) !== -1 && !fs.existsSync(path.join(ROOT, 'js', m))) missing.push(f + ' → ' + m);
      });
    });
    ok('aucun module référencé n’est manquant', missing.length === 0, missing.join(', '));

    // Les assets S15 existent bien
    ['img/interactive/loadout-bench.jpg', 'img/interactive/weapon-compare.jpg', 'img/interactive/map-planning.jpg',
     'img/interactive/tier-board.jpg', 'img/interactive/search-intel.jpg', 'img/interactive/ammo-penetration.jpg']
      .forEach(f => ok('asset présent : ' + f, fs.existsSync(path.join(ROOT, f))));
  }

  server.close();
  console.log('\n═══ Résultat : ' + PASS + ' réussites, ' + FAIL + ' échecs ═══');
  if (failures.length) {
    console.log('\nÉchecs :');
    failures.forEach(f => console.log('  · ' + f));
  }
  process.exit(FAIL ? 1 : 0);
})().catch(e => { console.error(e); server.close(); process.exit(2); });
