/* Verification visuelle : les deux nouveaux visuels s'affichent correctement
 * dans leur page, avec le bon texte alternatif et les bonnes dimensions. */
const { chromium } = require('playwright');
const BASE = process.env.BASE || 'http://127.0.0.1:8765';

const CAS = [
  ['/pages/armes-attachements-s7.html', 'img/armes/vis-attachements-s7.jpg'],
  ['/pages/reglages-sensibilite.html', 'img/guides/vis-reglages-sensibilite.jpg'],
  ['/pages/meta-tier-list-globale.html', null]
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });

  for (const [url, img] of CAS) {
    await page.goto(BASE + url, { waitUntil: 'networkidle' });
    await page.waitForTimeout(500);
    if (img) {
      const info = await page.evaluate(sel => {
        const el = document.querySelector('img[src*="' + sel + '"]');
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return { src: el.getAttribute('src'), alt: el.alt,
                 w: el.naturalWidth, h: el.naturalHeight,
                 visible: r.width > 0 && r.height > 0 };
      }, img.split('/').pop());
      console.log(url);
      console.log('   ' + JSON.stringify(info));
    } else {
      const rows = await page.$$eval('#catalogue-77-body tr', r => r.length);
      console.log(url + ' -> ' + rows + ' lignes de catalogue');
    }
  }
  await browser.close();
})();
