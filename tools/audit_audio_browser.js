// Audit audio : decodage reel et duree de chaque MP3 du site.
// Le navigateur est le seul decodeur de reference disponible dans la
// chaine d'outils (ni ffmpeg, ni pydub, ni mutagen dans l'environnement),
// et c'est lui qui sert la piste a l'internaute.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const AUDIO = path.resolve(__dirname, '..', 'audio');

(async () => {
  const fichiers = fs.readdirSync(AUDIO)
    .filter(f => f.endsWith('.mp3'))
    .sort();

  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  let ok = 0, fail = 0;
  const T = (c, m) => { c ? (ok++, console.log('  ✓', m)) : (fail++, console.log('  ✗', m)); };

  console.log(`\nAudit audio — ${fichiers.length} fichiers MP3\n`);

  for (const f of fichiers) {
    // Chromium refuse le protocole file:// pour les medias : on passe le
    // contenu en base64 et on construit un blob URL dans la page.
    const b64 = fs.readFileSync(path.join(AUDIO, f)).toString('base64');
    const r = await p.evaluate(async (data) => {
      const bin = atob(data);
      const buf = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) buf[i] = bin.charCodeAt(i);
      const url = URL.createObjectURL(new Blob([buf], { type: 'audio/mpeg' }));
      return await new Promise((resolve) => {
        const a = new Audio();
        a.preload = 'metadata';
        const done = (v) => { URL.revokeObjectURL(url); resolve(v); };
        a.addEventListener('loadedmetadata', () => done({ dur: a.duration, ok: true }));
        a.addEventListener('error', () => done({ ok: false, err: String(a.error && a.error.code) }));
        setTimeout(() => done({ ok: false, err: 'timeout' }), 8000);
        a.src = url;
      });
    }, b64);
    if (r.ok && isFinite(r.dur) && r.dur > 0.5) {
      ok++;
      console.log(`  ✓ ${f.padEnd(42)} ${r.dur.toFixed(2)} s`);
    } else {
      fail++;
      console.log(`  ✗ ${f.padEnd(42)} NON DECODE (${r.err || 'duree invalide'})`);
    }
  }

  console.log(`\n  Decodes : ${ok} | Echecs : ${fail}`);
  await b.close();
  process.exit(fail ? 1 : 0);
})();
