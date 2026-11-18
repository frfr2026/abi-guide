#!/usr/bin/env node
/**
 * ABI NEXUS — audit_images_browser.js
 *
 * Mesure les doublons d'images REELS (apres execution du JavaScript) :
 * pour chaque page chargee dans Chromium, on collecte les src de tous les
 * <img> rendus, puis on detecte les images qui apparaissent sur plusieurs
 * pages. C'est la seule mesure fiable : les cartes generees par JS a partir
 * des JSON ne sont pas visibles dans le HTML statique.
 *
 * Usage : node tools/audit_images_browser.js [baseUrl]
 */
const { chromium } = require('/home/user/node_modules/playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const BASE = process.argv[2] || 'http://127.0.0.1:8000';

// --- collecte des pages ---
const pagesDir = path.join(ROOT, 'pages');
const htmlFiles = fs.readdirSync(pagesDir).filter(f => f.endsWith('.html')).sort();
const targets = [
  { url: '/index.html', name: 'index.html' },
  { url: '/404.html', name: '404.html' },
  ...htmlFiles.map(f => ({ url: '/pages/' + f, name: 'pages/' + f })),
];

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox', '--disable-dev-shm-usage'] });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });

  const usage = new Map();      // src -> Set(pages)
  const broken = [];            // images non decodees
  let totalRefs = 0;

  for (const t of targets) {
        const page = await ctx.newPage();
    try {
      await page.goto(BASE + t.url, { waitUntil: 'networkidle', timeout: 45000 });
      // force le chargement des images lazy : on descend jusqu'en bas
      await page.evaluate(async () => {
        const prev = document.documentElement.style.scrollBehavior;
        document.documentElement.style.scrollBehavior = 'auto';
        const h = document.body.scrollHeight;
        for (let y = 0; y < h + window.innerHeight; y += Math.floor(window.innerHeight * 0.8)) {
          window.scrollTo({ top: y, behavior: 'instant' });
          await new Promise(r => setTimeout(r, 90));
        }
        window.scrollTo({ top: 0, behavior: 'instant' });
        document.documentElement.style.scrollBehavior = prev;
        await new Promise(r => setTimeout(r, 300));
      });
      await page.waitForTimeout(600);
      // attend que toutes les images soient decodees
      await page.evaluate(async () => {
        const imgs = Array.from(document.querySelectorAll('img'));
        const wait = (im) => new Promise(res => {
          if (im.complete && im.naturalWidth > 0) return res();
          im.addEventListener('load', res, { once: true });
          im.addEventListener('error', res, { once: true });
          setTimeout(res, 5000);
        });
        await Promise.all(imgs.map(wait));
      });
      await page.waitForTimeout(400);
      const res = await page.evaluate(async () => {
        const imgs = Array.from(document.querySelectorAll('img'));
        const out = [];
        for (const im of imgs) {
          const src = im.getAttribute('src') || '';
          const abs = im.src || '';
          let ok = false;
          try { ok = im.complete && im.naturalWidth > 0; } catch (e) { ok = false; }
          out.push({ src, abs, ok, w: im.naturalWidth || 0 });
        }
        return out;
      });
      for (const r of res) {
        if (!r.abs || r.abs.startsWith('data:')) continue;
        totalRefs++;
        // cle stable : chemin relatif a la racine du site
        let key;
        try { key = '/' + new URL(r.abs).pathname.replace(/^\//, ''); } catch (e) { key = r.abs; }
        if (!usage.has(key)) usage.set(key, new Set());
        usage.get(key).add(t.name);
        if (!r.ok) broken.push(t.name + ' -> ' + key);
      }
    } catch (e) {
      console.log('  ! ' + t.name + ' : ' + e.message.split('\n')[0]);
    }
    await page.close();
  }
  await browser.close();

  const dups = [...usage.entries()].filter(([, s]) => s.size > 1)
    .sort((a, b) => b[1].size - a[1].size);

  console.log('='.repeat(78));
  console.log('AUDIT IMAGES RENDUES (navigateur)');
  console.log('='.repeat(78));
  console.log('Pages auditees        : ' + targets.length);
  console.log('References d\'images   : ' + totalRefs);
  console.log('Images distinctes     : ' + usage.size);
  console.log('Images multi-pages    : ' + dups.length);
  console.log('Images non decodees   : ' + broken.length);
  console.log('');
  for (const [k, s] of dups) {
    console.log('  ' + k + '  [' + s.size + ']  ' + [...s].join(', '));
  }
  if (broken.length) {
    console.log('\nIMAGES NON DECODEES :');
    for (const b of [...new Set(broken)]) console.log('  ! ' + b);
  }
  fs.writeFileSync(path.join(ROOT, 'tools', '_audit_images.json'),
    JSON.stringify({ usage: Object.fromEntries([...usage].map(([k, v]) => [k, [...v]])), broken }, null, 1));
  process.exit(0);
})();
