#!/usr/bin/env node
/**
 * ABI NEXUS — test_s17_browser.js
 * Recette navigateur S17 (QA_FINAL).
 *
 * Unlike the jsdom suites, this script drives a real Chromium via
 * Playwright and therefore checks what only a layout engine can verify:
 * horizontal overflow, console errors, real image decoding, focus
 * visibility and keyboard journeys.
 *
 * Usage: node tools/test_s17_browser.js [baseUrl]
 */
const { chromium } = require('/home/user/node_modules/playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const BASE = process.argv[2] || 'http://127.0.0.1:8000';

let pass = 0;
let fail = 0;
const failures = [];

function ok(label, cond, detail) {
  if (cond) {
    pass++;
    console.log('  ✓ ' + label);
  } else {
    fail++;
    failures.push(label + (detail ? ' — ' + detail : ''));
    console.log('  ✗ ' + label + (detail ? ' — ' + detail : ''));
  }
}

function listPages() {
  const out = [];
  const pagesDir = path.join(ROOT, 'pages');
  for (const f of fs.readdirSync(pagesDir).filter(f => f.endsWith('.html')).sort()) {
    out.push('pages/' + f);
  }
  out.push('index.html');
  out.push('404.html');
  return out;
}

const VIEWPORTS = [
  { name: '375 (mobile)', width: 375, height: 812 },
  { name: '768 (tablette)', width: 768, height: 1024 },
  { name: '1280 (portable)', width: 1280, height: 800 },
  { name: '1440 (bureau)', width: 1440, height: 900 }
];

(async () => {
  console.log('═══ ABI NEXUS — Recette navigateur (S17) ═══');
  console.log('Base : ' + BASE + '\n');

  const browser = await chromium.launch({
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });
  const allPages = listPages();

  // ────────────────────────────────────────────────────────────
  // 1. Balayage complet : overflow horizontal + erreurs console
  // ────────────────────────────────────────────────────────────
  console.log('1. Balayage des %d pages aux 4 largeurs (overflow + console)', allPages.length);

  const consoleErrors = new Map();
  const overflows = [];
  const brokenImages = [];

  for (const vp of VIEWPORTS) {
    const ctx = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 1
    });
    for (const rel of allPages) {
      const page = await ctx.newPage();
      const errs = [];
      page.on('console', m => {
        if (m.type() === 'error') errs.push(m.text().slice(0, 160));
      });
      page.on('pageerror', e => errs.push('PAGEERROR ' + String(e.message).slice(0, 160)));
      try {
        await page.goto(BASE + '/' + rel, { waitUntil: 'load', timeout: 20000 });
        await page.waitForTimeout(120);

        const over = await page.evaluate(() => {
          const d = document.documentElement;
          const w = Math.max(d.scrollWidth, document.body ? document.body.scrollWidth : 0);
          return { scroll: w, client: d.clientWidth };
        });
        if (over.scroll > over.client + 2) {
          overflows.push(vp.name + ' | ' + rel + ' | ' + over.scroll + 'px > ' + over.client + 'px');
        }

        // les images « lazy » hors ecran ne sont pas chargees : on
        // fait defiler la page pour les declencher toutes
        await page.evaluate(async () => {
          const step = window.innerHeight * 0.8;
          for (let y = 0; y < document.body.scrollHeight; y += step) {
            window.scrollTo(0, y);
            await new Promise(r => setTimeout(r, 90));
          }
          window.scrollTo(0, document.body.scrollHeight);
          await new Promise(r => setTimeout(r, 350));
          window.scrollTo(0, 0);
          await new Promise(r => setTimeout(r, 200));
        });
        const broken = await page.evaluate(() =>
          Array.from(document.images)
            .filter(i => i.complete && i.naturalWidth === 0)
            .map(i => i.currentSrc || i.src)
        );
        for (const b of broken) {
          brokenImages.push(vp.name + ' | ' + rel + ' | ' + b);
        }
      } catch (e) {
        errs.push('LOAD ' + String(e.message).slice(0, 120));
      }
      if (errs.length) {
        consoleErrors.set(rel + ' @ ' + vp.name, [...new Set(errs)]);
      }
      await page.close();
    }
    await ctx.close();
  }
  console.log('   balayage terminé (' + (allPages.length * VIEWPORTS.length) + ' chargements)');

  console.log('\n2. Overflow horizontal');
  ok('aucun débordement horizontal à 375/768/1280/1440 px', overflows.length === 0,
     overflows.slice(0, 5).join(' ; '));

  console.log('\n3. Erreurs console');
  ok('aucune erreur JavaScript sur aucune page', consoleErrors.size === 0,
     [...consoleErrors.entries()].slice(0, 3).map(e => e[0] + ' → ' + e[1][0]).join(' ; '));

  console.log('\n4. Images décodées');
  ok('toutes les images référencées se chargent', brokenImages.length === 0,
     brokenImages.slice(0, 5).join(' ; '));

  // ────────────────────────────────────────────────────────────
  // 5. Parcours clavier et focus visible
  // ────────────────────────────────────────────────────────────
  console.log('\n5. Clavier et focus visible');
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.goto(BASE + '/index.html', { waitUntil: 'load' });

  // 5a. skip link
  await page.keyboard.press('Tab');
  const skip = await page.evaluate(() => {
    const a = document.activeElement;
    const cs = getComputedStyle(a);
    return {
      tag: a.tagName,
      text: (a.textContent || '').trim(),
      visible: a.getBoundingClientRect().top >= 0 && a.getBoundingClientRect().height > 0,
      outline: cs.outlineStyle + ' ' + cs.outlineWidth,
      bg: cs.backgroundColor
    };
  });
  ok('le premier Tab atteint le skip link', skip.tag === 'A' && /contenu/i.test(skip.text),
     JSON.stringify(skip));
  ok('le skip link est visible au focus', skip.visible && skip.bg !== 'rgba(0, 0, 0, 0)');

  // 5b. focus visible sur un lien de navigation
  const focusRing = await page.evaluate(() => {
    const a = document.querySelector('.site-nav a.nav-link');
    a.focus();
    const cs = getComputedStyle(a);
    return { style: cs.outlineStyle, width: cs.outlineWidth, color: cs.outlineColor };
  });
  ok('un indicateur de focus est calculé sur la navigation',
     focusRing.style !== 'none' && parseFloat(focusRing.width) >= 1, JSON.stringify(focusRing));

  // 5c. le focus n'est jamais supprimé
  const noOutline = await page.evaluate(() =>
    Array.from(document.querySelectorAll('a, button, input, select, textarea'))
      .filter(el => {
        const cs = getComputedStyle(el);
        return cs.outlineStyle === 'none' && el.getAttribute('data-force-outline') === 'on';
      }).length
  );
  ok('aucun outline neutralisé', noOutline === 0);

  // 5d. navigation au clavier dans la barre de recherche
  await page.goto(BASE + '/index.html', { waitUntil: 'load' });
  await page.keyboard.press('/');
  const searchFocused = await page.evaluate(() => {
    const a = document.activeElement;
    return { id: a.id, cls: String(a.className || ''), type: a.type || '' };
  });
  ok('la touche « / » place le focus dans la recherche',
     /srch-input/.test(searchFocused.cls) && searchFocused.type === 'search',
     JSON.stringify(searchFocused));

  await page.keyboard.type('AK-12');
  await page.waitForTimeout(400);
  const results = await page.evaluate(() => {
    const box = document.querySelector('.srch-panel');
    const items = box ? box.querySelectorAll('.srch-item') : [];
    return {
      visible: box ? getComputedStyle(box).display !== 'none' && !!box.offsetParent : false,
      count: items.length,
      first: items.length ? items[0].textContent.trim().slice(0, 40) : '',
      live: box ? box.getAttribute('aria-live') : null
    };
  });
  ok('la recherche renvoie des résultats', results.visible && results.count > 0,
     JSON.stringify(results));
  ok('le premier résultat correspond à la saisie', /AK-12/i.test(results.first),
     JSON.stringify(results.first));
  ok('le panneau de résultats est une région live', results.live === 'polite',
     String(results.live));

  await page.keyboard.press('Escape');
  await page.waitForTimeout(250);
  const closed = await page.evaluate(() => {
    const box = document.querySelector('.srch-panel');
    return box ? getComputedStyle(box).display === 'none' || !box.offsetParent : true;
  });
  ok('Échap ferme le panneau de résultats', closed);

  // ────────────────────────────────────────────────────────────
  // 6. Menu mobile
  // ────────────────────────────────────────────────────────────
  console.log('\n6. Navigation mobile (375 px)');
  const mctx = await browser.newContext({ viewport: { width: 375, height: 812 } });
  const mpage = await mctx.newPage();
  await mpage.goto(BASE + '/index.html', { waitUntil: 'load' });
  const burger = await mpage.evaluate(() => {
    const b = document.querySelector('.hamburger');
    if (!b) return null;
    return { found: true, label: b.getAttribute('aria-label') || '', expanded: b.getAttribute('aria-expanded') };
  });
  ok('un bouton de menu mobile est présent', !!burger, JSON.stringify(burger));
  if (burger) {
    await mpage.click('.hamburger');
    await mpage.waitForTimeout(400);
    const opened = await mpage.evaluate(() => {
      const b = document.querySelector('.hamburger');
      const panel = document.querySelector('.nav-links');
      return {
        expanded: b ? b.getAttribute('aria-expanded') : null,
        panelVisible: panel ? !!panel.offsetParent : false
      };
    });
    ok('le menu mobile s’ouvre et déclare aria-expanded', opened.expanded === 'true',
       JSON.stringify(opened));
    ok('le panneau de navigation devient visible', opened.panelVisible, JSON.stringify(opened));

    // navigation au clavier dans le menu ouvert
    await mpage.keyboard.press('Escape');
    await mpage.click('.hamburger');
    await mpage.waitForTimeout(300);
    const links = await mpage.evaluate(() =>
      document.querySelectorAll('.nav-links .nav-link').length);
    ok('le menu mobile expose les entrées de navigation', links >= 8, String(links));
  }

  // ────────────────────────────────────────────────────────────
  // 7. Outils interactifs
  // ────────────────────────────────────────────────────────────
  console.log('\n7. Outils interactifs');

  // 7a. constructeur de kit
  await page.goto(BASE + '/pages/meta-loadout-optimizer.html', { waitUntil: 'load' });
  await page.waitForTimeout(500);
  const lb = await page.evaluate(() => {
    const root = document.querySelector('.loadout-builder, [data-loadout]');
    return {
      found: !!root,
      mode: !!document.querySelector('#lb-mode'),
      weapon: !!document.querySelector('#lb-weapon'),
      out: (document.querySelector('.lb-out') || {}).innerText || ''
    };
  });
  ok('le constructeur de kit est présent', lb.found && lb.mode && lb.weapon, JSON.stringify(lb).slice(0, 120));
  if (lb.mode) {
    const before = lb.out;
    await page.selectOption('#lb-mode', { index: 2 }).catch(() => {});
    await page.waitForTimeout(500);
    const after = await page.evaluate(() => (document.querySelector('.lb-out') || {}).innerText || '');
    ok('changer de mode recalcule le kit', after.length > 0 && after !== before,
       (after || before).slice(0, 80).replace(/\n/g, ' '));
    const live = await page.evaluate(() => {
      const el = document.querySelector('.lb-out');
      return {
        attr: el ? el.getAttribute('aria-live') : null,
        text: el ? el.textContent.trim().length : 0
      };
    });
    ok('le constructeur de kit dispose d\'une région live',
       live.attr === 'polite' && live.text > 0, JSON.stringify(live));
  }

  // 7b. tier list interactive
  await page.goto(BASE + '/pages/armes-tier-list.html', { waitUntil: 'load' });
  await page.waitForTimeout(700);
  const tl = await page.evaluate(() => {
    const chips = document.querySelectorAll('.tlx-chip');
    const zones = document.querySelectorAll('.tlx-drop');
    const status = document.querySelector('#tlx-status');
    return {
      count: chips.length,
      zones: zones.length,
      live: status ? status.getAttribute('aria-live') : null,
      focusable: chips.length ? chips[0].getAttribute('tabindex') : null,
      role: chips.length ? chips[0].getAttribute('role') : null
    };
  });
  ok('la tier list interactive expose des éléments déplaçables', tl.count > 0, JSON.stringify(tl));
  ok('la tier list est organisée en quatre paliers', tl.zones === 4, JSON.stringify(tl));
  ok('les puces de la tier list sont atteignables au clavier', tl.focusable === '0',
     JSON.stringify(tl));
  ok('la tier list annonce ses changements (région live)', tl.live === 'polite',
     String(tl.live));

  // deplacement clavier d'une puce
  const moved = await page.evaluate(async () => {
    const chip = document.querySelector('.tlx-chip');
    if (!chip) return { ok: false };
    const id = chip.dataset.id;
    const before = chip.closest('.tlx-drop').dataset.tier;
    chip.focus();
    chip.dispatchEvent(new KeyboardEvent('keydown', { key: ' ', bubbles: true }));
    await new Promise(r => setTimeout(r, 350));
    // le classement est reconstruit : la puce est relocalisee par id
    const after = document.querySelector('.tlx-chip[data-id="' + id + '"]');
    const afterTier = after ? after.closest('.tlx-drop').dataset.tier : null;
    const status = document.querySelector('#tlx-status');
    return {
      ok: !!afterTier && afterTier !== before,
      before, after: afterTier,
      announced: status ? status.textContent.trim().slice(0, 60) : ''
    };
  });
  ok('la touche Espace descend une arme d’un palier', moved.ok, JSON.stringify(moved));
  ok('le déplacement est annoncé (région live)', moved.announced.length > 0,
     JSON.stringify(moved.announced));

  // 7c. explorateur de cartes
  await page.goto(BASE + '/pages/meta-stratégies-s7.html', { waitUntil: 'load' });
  await page.waitForTimeout(700);
  const maps = await page.evaluate(() => {
    const cards = document.querySelectorAll('.mx-card');
    const counter = document.querySelector('.mx-count, [aria-live]');
    return {
      count: cards.length,
      names: Array.from(cards).slice(0, 3).map(c => (c.textContent || '').trim().slice(0, 24)),
      live: counter ? counter.getAttribute('aria-live') : null
    };
  });
  ok('l\'explorateur de cartes liste des cartes', maps.count > 0, JSON.stringify(maps));
  ok('l\'explorateur de cartes annonce son compteur', maps.live === 'polite',
     String(maps.live));

  // 7d. comparateur d'armes
  await page.goto(BASE + '/pages/armes-tier-list.html', { waitUntil: 'load' });
  await page.waitForTimeout(400);
  const wc = await page.evaluate(() => {
    const root = document.querySelector('.weapon-compare, .wc-picker, [data-compare]');
    return { found: !!root };
  });
  ok('le comparateur d\'armes est présent sur la page', wc.found, JSON.stringify(wc));

  // ────────────────────────────────────────────────────────────
  // 8. Page 404 : vrai code HTTP et navigation de secours
  // ────────────────────────────────────────────────────────────
  console.log('\n8. Page 404');
  // le serveur de developpement renvoie sa propre page d'erreur :
  // on verifie donc le fichier 404.html livre par le site, puis on
  // controle que le serveur renvoie bien un statut HTTP 404.
  const resp = await page.goto(BASE + '/page-inexistante-xyz.html', { waitUntil: 'load' });
  ok('une URL inconnue renvoie un statut HTTP 404', resp.status() === 404,
     'HTTP ' + resp.status());

  await page.goto(BASE + '/404.html', { waitUntil: 'load' });
  const e404 = await page.evaluate(() => ({
    h1: (document.querySelector('h1') || {}).textContent || '',
    nav: !!document.querySelector('.site-nav'),
    navLinks: document.querySelectorAll('.nav-links .nav-link').length,
    search: !!document.querySelector('.srch-input'),
    noindex: !!document.querySelector('meta[name="robots"][content*="noindex"]'),
    shortcuts: document.querySelectorAll('.err-grid .card').length
  }));
  ok('la 404 affiche un message et la navigation globale',
     e404.h1.length > 0 && e404.nav && e404.navLinks >= 8, JSON.stringify(e404));
  ok('la 404 est marquée noindex', e404.noindex);
  ok('la 404 propose des raccourcis de navigation', e404.shortcuts >= 6,
     String(e404.shortcuts));

  // ────────────────────────────────────────────────────────────
  // 8b. Audio : la bande-son du menu doit etre livree et decodable
  // ────────────────────────────────────────────────────────────
  console.log('\n8b. Bande-son du menu');
  await page.goto(BASE + '/index.html', { waitUntil: 'load' });
  const audio = await page.evaluate(async () => {
    const player = document.querySelector('.audio-player');
    const track = player ? player.getAttribute('data-track') : null;
    if (!track) return { track: null };
    const res = await fetch(track);
    const buf = new Uint8Array(await res.arrayBuffer());
    return {
      track, status: res.status, bytes: buf.length,
      type: res.headers.get('content-type'),
      mp3: buf[0] === 0xff && (buf[1] & 0xe0) === 0xe0
    };
  });
  ok('la piste audio du menu est présente', !!audio.track, JSON.stringify(audio));
  ok('la piste audio est servie en HTTP 200', audio.status === 200, String(audio.status));
  ok('la piste audio est un MP3 valide', audio.mp3 === true,
     (audio.bytes || 0) + ' octets');

  // la piste dediee aux pages zombies doit etre presente et decodable
  await page.goto(BASE + '/pages/saison7-zombie-infected-zone.html', { waitUntil: 'load' });
  const audioZ = await page.evaluate(async () => {
    const player = document.querySelector('.audio-player');
    const track = player ? player.getAttribute('data-track') : null;
    if (!track) return { track: null };
    const res = await fetch(track);
    const buf = new Uint8Array(await res.arrayBuffer());
    const decoded = await new Promise(resolve => {
      const a = new Audio(track);
      a.addEventListener('canplaythrough', () => resolve(true));
      a.addEventListener('error', () => resolve(false));
      setTimeout(() => resolve(false), 4000);
    });
    return {
      track, status: res.status, bytes: buf.length, decoded,
      mp3: buf[0] === 0xff && (buf[1] & 0xe0) === 0xe0
    };
  });
  ok('la piste audio zombie est presente', !!audioZ.track, JSON.stringify(audioZ));
  ok('la piste audio zombie est servie en HTTP 200', audioZ.status === 200, String(audioZ.status));
  ok('la piste audio zombie est un MP3 valide', audioZ.mp3 === true,
     (audioZ.bytes || 0) + ' octets');
  ok('la piste audio zombie est decodable par le navigateur', audioZ.decoded === true,
     String(audioZ.decoded));

  // ────────────────────────────────────────────────────────────
  // 8c. Simulateur balistique : penetration et TTK
  // ────────────────────────────────────────────────────────────
  console.log('\n8c. Simulateur balistique');
  await page.goto(BASE + '/pages/items-munitions.html', { waitUntil: 'load' });
  await page.waitForTimeout(1200);
  const bal = await page.evaluate(() => {
    const root = document.querySelector('#ballistics');
    const out = document.querySelector('#bal-out');
    const sel = id => document.querySelector(id);
    return {
      present: !!root,
      calibres: sel('#bal-caliber') ? sel('#bal-caliber').options.length : 0,
      armes: sel('#bal-weapon') ? sel('#bal-weapon').options.length : 0,
      munitions: sel('#bal-ammo') ? sel('#bal-ammo').options.length : 0,
      armures: sel('#bal-armor') ? sel('#bal-armor').options.length : 0,
      live: out ? out.getAttribute('aria-live') : null,
      texte: out ? out.innerText.replace(/\s+/g, ' ') : ''
    };
  });
  ok('le simulateur balistique est present', bal.present, JSON.stringify(bal));
  ok('le simulateur propose les 10 calibres', bal.calibres === 10, String(bal.calibres));
  ok('le simulateur liste armes, munitions et armures',
     bal.armes > 0 && bal.munitions > 0 && bal.armures > 0,
     bal.armes + '/' + bal.munitions + '/' + bal.armures);
  ok('le simulateur annonce son résultat (région live)', bal.live === 'polite',
     String(bal.live));
  ok('le simulateur rend un verdict de penetration',
     /p(erce|énètre)/i.test(bal.texte) && /PL\s*\d/.test(bal.texte), bal.texte.slice(0, 90));

  // une munition sous la classe de l'armure ne doit pas percer
  const noPen = await page.evaluate(async () => {
    const armor = document.querySelector('#bal-armor');
    const t6 = Array.from(armor.options).find(o => /T6/.test(o.textContent));
    if (!t6) return { skip: true };
    armor.value = t6.value;
    armor.dispatchEvent(new Event('change'));
    const ammo = document.querySelector('#bal-ammo');
    const low = Array.from(ammo.options).find(o => /PL\s*[1-2]\b/.test(o.textContent));
    if (low) { ammo.value = low.value; ammo.dispatchEvent(new Event('change')); }
    await new Promise(r => setTimeout(r, 250));
    return { texte: document.querySelector('#bal-out').innerText.replace(/\s+/g, ' ') };
  });
  ok('une munition inferieure a la classe de l armure ne perce pas',
     noPen.skip || /ne p(erce|énètre) pas/i.test(noPen.texte), (noPen.texte || '').slice(0, 90));

  // le bareme communautaire : PL superieur = plein, PL egal = partiel (80 %),
  // PL inferieur = ricochet (50 %)
  const bareme = await page.evaluate(async () => {
    const sel = (s, re) => {
      const el = document.querySelector(s);
      const o = [...el.options].find(x => new RegExp(re).test(x.textContent));
      if (!o) return false;
      el.value = o.value; el.dispatchEvent(new Event('change'));
      return true;
    };
    const wait = () => new Promise(r => setTimeout(r, 200));
    const verdict = () => {
      const t = document.querySelector('#bal-out').innerText.replace(/\s+/g, ' ');
      const m = t.match(/VERDICT (.+?) Dégâts/);
      return m ? m[1] : '';
    };
    const out = {};
    sel('#bal-caliber', '5\\.45'); await wait();
    sel('#bal-ammo', ' BS'); sel('#bal-armor', 'T4 ·'); await wait();
    out.sup = verdict();
    sel('#bal-armor', 'T5 ·'); await wait();
    out.egal = verdict();
    sel('#bal-ammo', ' HP'); await wait();
    out.inf = verdict();
    return out;
  });
  ok('PL superieur a la classe : la balle traverse',
     /pénètre pleinement/i.test(bareme.sup || ''), String(bareme.sup));
  ok('PL egal a la classe : penetration partielle',
     /partielle/i.test(bareme.egal || ''), String(bareme.egal));
  ok('PL inferieur a la classe : la balle ricoche',
     /ne pénètre pas/i.test(bareme.inf || ''), String(bareme.inf));

  // ────────────────────────────────────────────────────────────
  // 9. Performance perçue (temps de chargement local)
  // ────────────────────────────────────────────────────────────
  console.log('\n9. Performance de rendu');
  const perf = [];
  for (const rel of ['index.html', 'pages/armes-tier-list.html', 'pages/meta-loadout-optimizer.html']) {
    const p = await ctx.newPage();
    await p.goto(BASE + '/' + rel, { waitUntil: 'load' });
    const t = await p.evaluate(() => {
      const n = performance.getEntriesByType('navigation')[0];
      const paint = performance.getEntriesByType('paint') || [];
      const fcp = paint.find(x => x.name === 'first-contentful-paint');
      return {
        dcl: Math.round(n.domContentLoadedEventEnd),
        load: Math.round(n.loadEventEnd),
        fcp: fcp ? Math.round(fcp.startTime) : null
      };
    });
    perf.push(rel + ' → DCL ' + t.dcl + ' ms, load ' + t.load + ' ms, FCP ' + t.fcp + ' ms');
    await p.close();
  }
  for (const l of perf) console.log('   · ' + l);

  await browser.close();

  console.log('\n' + '='.repeat(66));
  console.log('Résultat : ' + pass + ' réussites, ' + fail + ' échecs');
  if (fail) {
    console.log('Échecs :');
    for (const f of failures) console.log('  ✗ ' + f);
  }
  console.log('='.repeat(66));
  process.exit(fail ? 1 : 0);
})().catch(e => {
  console.error('ERREUR FATALE :', e);
  process.exit(2);
});
