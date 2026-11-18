/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — tests S16 (jsdom)
   Verifie le rendu apres refonte SEO : page 404, JSON-LD, absence
   d'erreur JavaScript sur l'ensemble des pages, fichiers racine.

   Usage : node tools/test_s16.js
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
  '.svg': 'image/svg+xml', '.webp': 'image/webp', '.ico': 'image/x-icon',
  '.xml': 'application/xml', '.txt': 'text/plain; charset=utf-8'
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
  vc.on('jsdomError', e => errors.push(e.message));
  vc.on('error', (...a) => errors.push(a.map(String).join(' ')));
  vc.on('warn', () => {}); vc.on('info', () => {}); vc.on('log', () => {});
  const dom = await JSDOM.fromURL('http://127.0.0.1:' + port + pagePath, {
    runScripts: 'dangerously', resources: 'usable', pretendToBeVisual: true, virtualConsole: vc,
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
      window.matchMedia = window.matchMedia || (() => ({
        matches: false, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {}
      }));
    }
  });
  await new Promise(r => setTimeout(r, waitMs || 1000));
  return { dom, window: dom.window, doc: dom.window.document, errors };
}

(async function main() {
  const port = await startServer();
  console.log('\n═══ ABI NEXUS — Tests S16 ═══\n');

  /* ── 1. Page 404 ────────────────────────────────────────────── */
  console.log('1. Page 404 (404.html)');
  {
    const { window, doc, errors } = await loadPage(port, '/404.html', 1400);
    ok('la page se rend sans erreur JavaScript', errors.length === 0, errors.join(' | '));
    ok('la navigation globale est presente', !!doc.querySelector('.site-nav .nav-links'));
    ok('le pied de page a 8 colonnes est present', doc.querySelectorAll('.footer-col').length >= 7,
      doc.querySelectorAll('.footer-col').length + ' colonnes');
    ok('le champ de recherche est injecte', !!doc.querySelector('.srch-input'));
    ok('le message d\'erreur est explicite', /n'existe pas|Secteur perdu/i.test(doc.body.textContent));
    ok('les raccourcis vers les sections sont presents', doc.querySelectorAll('.err-card').length === 8,
      doc.querySelectorAll('.err-card').length + ' cartes');
    ok('le lien vers l\'accueil est present', !!doc.querySelector('.err-actions a[href="index.html"]'));
    ok('la balise noindex est presente', /noindex/.test(doc.head.innerHTML));

    // la recherche fonctionne aussi sur la page 404
    const input = doc.querySelector('.srch-input');
    input.value = 'armure';
    input.dispatchEvent(new window.Event('input', { bubbles: true }));
    await new Promise(r => setTimeout(r, 500));
    const n = doc.querySelectorAll('.srch-panel .srch-item').length;
    ok('la recherche renvoie des résultats sur la page 404', n > 0, n + ' résultats');

    window.close();
  }

  /* ── 2. JSON-LD ─────────────────────────────────────────────── */
  console.log('\n2. Données structurées JSON-LD');
  {
    const pages = fs.readdirSync(path.join(ROOT, 'pages')).filter(f => f.endsWith('.html'));
    let valid = 0, withGraph = 0, withBc = 0, withArticle = 0;
    const problems = [];
    pages.concat(['../index.html']).forEach(f => {
      const p = f === '../index.html' ? path.join(ROOT, 'index.html') : path.join(ROOT, 'pages', f);
      const s = fs.readFileSync(p, 'utf8');
      const head = s.slice(0, s.indexOf('</head>'));
      const blocks = head.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g) || [];
      if (!blocks.length) { problems.push(f + ' : aucun bloc'); return; }
      blocks.forEach(b => {
        const json = b.replace(/<script[^>]*>/, '').replace(/<\/script>/, '');
        try {
          const d = JSON.parse(json);
          if (!d['@graph']) { problems.push(f + ' : pas de @graph'); return; }
          withGraph++;
          const types = d['@graph'].map(n => n['@type']);
          if (types.includes('BreadcrumbList')) withBc++;
          if (types.includes('Article')) withArticle++;
          const ids = new Set(d['@graph'].map(n => n['@id']).filter(Boolean));
          d['@graph'].forEach(n => {
            ['isPartOf', 'publisher', 'author', 'breadcrumb', 'mainEntityOfPage'].forEach(k => {
              const ref = n[k];
              if (ref && ref['@id'] && !ids.has(ref['@id'])) problems.push(f + ' : reference orpheline ' + ref['@id']);
            });
          });
          valid++;
        } catch (e) { problems.push(f + ' : JSON invalide ' + e.message); }
      });
    });
    ok('tous les blocs JSON-LD sont du JSON valide', valid === pages.length + 1, valid + '/' + (pages.length + 1));
    ok('tous les blocs utilisent @graph', withGraph === pages.length + 1, withGraph + '/' + (pages.length + 1));
    ok('toutes les pages hors accueil ont un BreadcrumbList', withBc === pages.length, withBc + '/' + pages.length);
    ok('les pages editoriales ont un Article', withArticle >= 55, withArticle + ' pages');
    ok('aucune reference JSON-LD orpheline', problems.length === 0, problems.slice(0, 3).join(' | '));
  }

  /* ── 3. Balises head sur l'ensemble du site ─────────────────── */
  console.log('\n3. Balises <head> sur toutes les pages du site');
  {
    const pages = fs.readdirSync(path.join(ROOT, 'pages')).filter(f => f.endsWith('.html'));
    const miss = [];
    pages.concat(['../index.html']).forEach(f => {
      const p = f === '../index.html' ? path.join(ROOT, 'index.html') : path.join(ROOT, 'pages', f);
      const s = fs.readFileSync(p, 'utf8');
      const head = s.slice(0, s.indexOf('</head>'));
      const need = [
        '<link rel="canonical"', 'name="robots"', 'property="og:image"',
        'property="og:image:width"', 'property="og:image:height"',
        'name="twitter:card" content="summary_large_image"',
        'name="theme-color"', '<link rel="alternate" hreflang="fr"'
      ];
      need.forEach(n => { if (!head.includes(n)) miss.push(f + ' → ' + n); });
    });
    ok('toutes les balises obligatoires sont presentes', miss.length === 0, miss.slice(0, 4).join(' | '));

    // toutes les images ont width/height
    let bad = 0;
    pages.concat(['../index.html']).forEach(f => {
      const p = f === '../index.html' ? path.join(ROOT, 'index.html') : path.join(ROOT, 'pages', f);
      const s = fs.readFileSync(p, 'utf8');
      (s.match(/<img[^>]*>/g) || []).forEach(tag => {
        if (!/width="/.test(tag) || !/height="/.test(tag)) bad++;
      });
    });
    ok('toutes les images declarent width et height (anti-CLS)', bad === 0, bad + ' images sans dimension');
  }

  /* ── 4. Fichiers racine ─────────────────────────────────────── */
  console.log('\n4. Fichiers racine servis en HTTP');
  {
    const checks = [
      ['/sitemap.xml', 'application/xml'],
      ['/robots.txt', 'text/plain'],
      ['/manifest.json', 'application/json'],
      ['/404.html', 'text/html']
    ];
    for (const [p, ct] of checks) {
      const r = await fetch('http://127.0.0.1:' + port + p);
      const body = await r.text();
      ok(p + ' renvoie 200', r.status === 200, 'status ' + r.status);
      ok(p + ' a un contenu non vide', body.length > 100, body.length + ' octets');
    }
    // sitemap : toutes les URL correspondent a des fichiers reels
    const sm = await (await fetch('http://127.0.0.1:' + port + '/sitemap.xml')).text();
    const locs = (sm.match(/<loc>(.*?)<\/loc>/g) || []).map(l => l.replace(/<\/?loc>/g, ''));
    const expectedUrls = fs.readdirSync(path.join(ROOT, 'pages')).filter(f => f.endsWith('.html')).length + 1;
    ok('le sitemap contient une URL par page indexable', locs.length === expectedUrls,
       locs.length + ' URL pour ' + expectedUrls + ' pages');
    const missing = locs.filter(u => !fs.existsSync(path.join(ROOT, u.replace('https://abinexus.fr/', ''))));
    ok('toutes les URL du sitemap pointent vers un fichier existant', missing.length === 0, missing.slice(0, 3).join(', '));
    const smNoComment = sm.replace(/<!--[\s\S]*?-->/g, '');
    ok('le sitemap ne contient pas priority ni changefreq', !/<priority>/.test(smNoComment) && !/<changefreq>/.test(smNoComment));
    ok('le sitemap contient un lastmod au format W3C', /<lastmod>\d{4}-\d{2}-\d{2}T[\d:]{8}\+01:00<\/lastmod>/.test(sm));

    const rb = await (await fetch('http://127.0.0.1:' + port + '/robots.txt')).text();
    ok('robots.txt reference le sitemap en URL absolue', /Sitemap: https:\/\//.test(rb));
    ok('robots.txt autorise Googlebot', /User-agent: Googlebot\nAllow: \//.test(rb));
    ok('robots.txt bloque les robots d\'entrainement IA', /User-agent: GPTBot\nDisallow: \//.test(rb));
    ok('robots.txt n\'utilise pas noindex comme directive', !/^(Disallow|Allow):.*noindex/m.test(rb));

    const mf = JSON.parse(await (await fetch('http://127.0.0.1:' + port + '/manifest.json')).text());
    ok('le manifeste declare 4 icones', mf.icons.length === 4);
    ok('le manifeste declare 4 raccourcis', mf.shortcuts.length === 4);
    ok('toutes les icones du manifeste sont des JPG', mf.icons.every(i => i.src.endsWith('.jpg')));
  }

  /* ── 5. Absence d'erreur JS sur un echantillon ─────────────── */
  console.log('\n5. Rendu JavaScript (échantillon de 8 pages)');
  {
    const sample = ['/index.html', '/pages/armes-tier-list.html', '/pages/meta-loadout-optimizer.html',
      '/pages/meta-stratégies-s7.html', '/pages/guide-debutant.html', '/pages/map-farm.html',
      '/pages/communaute-ressources.html', '/pages/saison7-utopia.html'];
    for (const p of sample) {
      const { window, errors } = await loadPage(port, p, 1300);
      ok(p + ' sans erreur JavaScript', errors.length === 0, errors.join(' | '));
      ok(p + ' injecte le module de recherche', !!window.document.querySelector('.srch-input'));
      window.close();
    }
  }

  server.close();
  console.log('\n═══ Résultat : ' + PASS + ' réussites, ' + FAIL + ' échecs ═══');
  if (failures.length) { console.log('\nÉchecs :'); failures.forEach(f => console.log('  · ' + f)); }
  process.exit(FAIL ? 1 : 0);
})().catch(e => { console.error(e); server.close(); process.exit(2); });
