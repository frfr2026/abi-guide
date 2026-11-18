/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — weapon-compare.js (S15)
   Comparateur côte à côte de deux armes : statistiques brutes du
   jeu, prix, compatibilité des munitions et rapport coût/performance.
   Aucune valeur n'est inventée : tout provient de data-weapons.json.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const ROOT = document.querySelector('.weapon-compare');
  if (!ROOT) return;

  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, m =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
  const kf = n => (typeof n === 'number' ? Math.round(n).toLocaleString('fr-FR') + ' K' : '—');

  let WEAPONS = [];
  let AMMO = [];
  let a = null, b = null;

  const STATS = [
    { k: 'rpm', label: 'Cadence', unit: ' RPM', max: 900, better: 'high' },
    { k: 'damage', label: 'Dégâts', unit: '', max: 45, better: 'high' },
    { k: 'range', label: 'Portée', unit: ' m', max: 130, better: 'high' },
    { k: 'recoil', label: 'Recul', unit: '', max: 100, better: 'low' },
    { k: 'ergo', label: 'Ergonomie', unit: '', max: 100, better: 'high' },
    { k: 'price', label: 'Prix', unit: '', max: 600000, better: 'low', money: true }
  ];

  Promise.all([
    fetch('../js/data-weapons.json').then(r => r.json()),
    fetch('../js/data-ammo.json').then(r => r.json())
  ]).then(([w, am]) => {
    WEAPONS = (w.weapons || []).slice().sort((x, y) => x.price - y.price);
    AMMO = am.ammo || [];
    const selA = ROOT.querySelector('#wc-a');
    const selB = ROOT.querySelector('#wc-b');
    const opts = WEAPONS.map(x =>
      '<option value="' + x.id + '">' + esc(x.name) + ' — ' + esc(x.category) + ' · ' + kf(x.price) + '</option>').join('');
    selA.innerHTML = opts;
    selB.innerHTML = opts;
    selA.value = 'a545';
    selB.value = 'h416';
    a = WEAPONS.find(x => x.id === selA.value) || WEAPONS[0];
    b = WEAPONS.find(x => x.id === selB.value) || WEAPONS[1] || WEAPONS[0];
    selA.addEventListener('change', () => { a = WEAPONS.find(x => x.id === selA.value); render(); });
    selB.addEventListener('change', () => { b = WEAPONS.find(x => x.id === selB.value); render(); });
    const swap = ROOT.querySelector('#wc-swap');
    if (swap) swap.addEventListener('click', () => {
      const t = selA.value; selA.value = selB.value; selB.value = t;
      const tmp = a; a = b; b = tmp;
      render();
    });
    render();
  }).catch(err => {
    console.error('[ABI NEXUS] weapon-compare', err);
    ROOT.innerHTML = '<div class="callout callout-danger"><h4>Données indisponibles</h4><p>Impossible de charger la liste des armes.</p></div>';
  });

  function render() {
    if (!a || !b) return;
    const out = ROOT.querySelector('.wc-out');
    const rows = STATS.map(s => {
      const va = a[s.k], vb = b[s.k];
      let best = '', worst = '';
      if (va !== vb) {
        const aBetter = s.better === 'high' ? va > vb : va < vb;
        best = (aBetter ? 'a' : 'b');
        worst = (aBetter ? 'b' : 'a');
      }
      const fa = s.money ? kf(va) : va + s.unit;
      const fb = s.money ? kf(vb) : vb + s.unit;
      const pctA = Math.max(4, Math.min(100, (va / s.max) * 100));
      const pctB = Math.max(4, Math.min(100, (vb / s.max) * 100));
      return '<tr>' +
        '<td>' + esc(s.label) + '</td>' +
        '<td class="' + (best === 'a' ? 'best' : worst === 'a' ? 'worst' : '') + '">' + esc(fa) +
          '<div class="wc-bar"><i style="width:' + pctA.toFixed(0) + '%"></i></div></td>' +
        '<td class="' + (best === 'b' ? 'best' : worst === 'b' ? 'worst' : '') + '">' + esc(fb) +
          '<div class="wc-bar"><i style="width:' + pctB.toFixed(0) + '%"></i></div></td>' +
      '</tr>';
    }).join('');

    /* Munitions compatibles */
    const amA = AMMO.filter(x => x.caliber === a.caliber);
    const amB = AMMO.filter(x => x.caliber === b.caliber);
    const bestAmmo = list => list.slice().sort((x, y) => y.tier - x.tier || y.penetration - x.penetration)[0];

    /* Rapport coût / performance : un indicateur simple et explicite.
       Dégâts théoriques par seconde, corrigé d'un facteur d'ergonomie. */
    function dps(w) {
      const rpm = Math.min(w.rpm, 900);
      return Math.round((rpm / 60) * w.damage * (0.6 + w.ergo / 250));
    }
    const dA = dps(a), dB = dps(b);
    const vA = Math.round(dA / Math.max(1, a.price / 1000));
    const vB = Math.round(dB / Math.max(1, b.price / 1000));

    const winner = (vA === vB) ? null : (vA > vB ? a : b);

    out.innerHTML =
      '<div class="wc-table-wrap"><table class="wc-table">' +
        '<thead><tr><th>Statistique</th><th>' + esc(a.name) + '</th><th>' + esc(b.name) + '</th></tr></thead>' +
        '<tbody>' + rows + '</tbody>' +
      '</table></div>' +
      '<div class="lb-summary" style="margin-top:1rem">' +
        '<div class="lb-cell"><div class="lb-v">' + esc(a.tier) + '</div><div class="lb-k">Tier ' + esc(a.name) + '</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + esc(b.tier) + '</div><div class="lb-k">Tier ' + esc(b.name) + '</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + dA + '</div><div class="lb-k">DPS estimé ' + esc(a.name) + '</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + dB + '</div><div class="lb-k">DPS estimé ' + esc(b.name) + '</div></div>' +
      '</div>' +
      '<div class="lb-summary" style="margin-top:.5rem">' +
        '<div class="lb-cell"><div class="lb-v">' + vA + '</div><div class="lb-k">DPS / 1 K ' + esc(a.name) + '</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + vB + '</div><div class="lb-k">DPS / 1 K ' + esc(b.name) + '</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + amA.length + '</div><div class="lb-k">Munitions ' + esc(a.name) + '</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + amB.length + '</div><div class="lb-k">Munitions ' + esc(b.name) + '</div></div>' +
      '</div>' +
      '<ul class="lb-kit" style="margin-top:1rem">' +
        '<li><span>Calibre</span><span>' + esc(a.caliber) + '</span><span>' + esc(b.caliber) + '</span></li>' +
        '<li><span>Meilleure munition</span><span>' + esc(bestAmmo(amA) ? bestAmmo(amA).name + ' (PL ' + bestAmmo(amA).pierceLevel + ')' : '—') + '</span><span>' + esc(bestAmmo(amB) ? bestAmmo(amB).name + ' (PL ' + bestAmmo(amB).pierceLevel + ')' : '—') + '</span></li>' +
        '<li><span>Saison</span><span>' + esc(a.season || '—') + '</span><span>' + esc(b.season || '—') + '</span></li>' +
      '</ul>' +
      (winner
        ? '<div class="callout callout-success"><h4>Rapport coût / performance</h4><p>Sur cet indicateur, <strong>' + esc(winner.name) + '</strong> offre le meilleur rapport (' +
          (winner === a ? vA : vB) + ' DPS par 1 000 K contre ' + (winner === a ? vB : vA) + '). ' +
          'Ce calcul est un estimateur simplifié construit à partir des statistiques de la base locale ; il ne remplace pas le test en jeu.</p></div>'
        : '<div class="callout"><h4>Rapport coût / performance</h4><p>Les deux armes obtiennent le même indice sur cet estimateur simplifié.</p></div>') +
      '<p class="wc-note">Statistiques, prix et munitions issus de la base locale du site (patch 1.0.0.142.19, mise à jour 17 novembre 2026). Le DPS estimé est un calcul dérivé, pas une valeur publiée par l’éditeur.</p>';
  }

  window.ABIWeaponCompare = { render };
})();
