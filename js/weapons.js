/* ABI NEXUS — Affichage dynamique des données d'armes (S7 Utopia) */
(function () {
  'use strict';

  const GRID = document.querySelector('.weapon-grid');
  const TIER_OUT = document.querySelector('.tier-list-output');
  if (!GRID && !TIER_OUT) return;

  const TIER_RANK = { S: 0, A: 1, B: 2, C: 3, D: 4 };
  const fmtPrice = n => (typeof n === 'number' ? n.toLocaleString('fr-FR') + ' K' : '—');
  const esc = s => String(s).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  fetch('../js/data-weapons.json')
    .then(r => r.json())
    .then(data => {
      const weapons = Array.isArray(data) ? data : (data.weapons || []);
      weapons.sort((a, b) => (TIER_RANK[a.tier] ?? 9) - (TIER_RANK[b.tier] ?? 9) || b.rpm - a.rpm);

      if (GRID) renderGrid(GRID, weapons);
      if (TIER_OUT) renderTierList(TIER_OUT, weapons);
    })
    .catch(err => {
      console.error('[ABI NEXUS] Impossible de charger data-weapons.json', err);
      if (GRID) GRID.innerHTML = '<div class="callout callout-danger"><p>Données temporairement indisponibles. Réessayez plus tard.</p></div>';
    });

  function weaponCard(w, variant) {
    // variant 'tier' : le tier list global utilise une declenchee dediee de
    // chaque arme, afin qu'aucune image ne serve sur deux pages du site.
    const img = (variant === 'tier' && w.imageVariant) ? w.imageVariant : (w.image || '../img/hero/hero-armes.jpg');
    return `
    <article class="card weapon-card">
      <div class="card-media">
        <img src="${esc(img)}" alt="${esc(w.name)}" loading="lazy" onerror="this.onerror=null;this.src='../img/hero/hero-armes.jpg'">
        <span class="tier-badge tier-${String(w.tier).toLowerCase()}">${esc(w.tier)}</span>
        <h3 class="weapon-name">${esc(w.name)}${w.isNew ? ' <span class="badge badge-s7">S7</span>' : ''}</h3>
      </div>
      <div class="card-body">
        <p class="small text-muted" style="margin:0">${esc(w.caliber)} · ${esc(w.category)}</p>
        <div class="weapon-stats">
          <div class="weapon-stat"><div class="v">${w.rpm}</div><div class="k">RPM</div></div>
          <div class="weapon-stat"><div class="v">${w.damage}</div><div class="k">Dégâts</div></div>
          <div class="weapon-stat"><div class="v">${w.range}</div><div class="k">Portée</div></div>
          <div class="weapon-stat"><div class="v">${w.recoil}</div><div class="k">Recul</div></div>
          <div class="weapon-stat"><div class="v">${w.ergo}</div><div class="k">Ergonomie</div></div>
          <div class="weapon-stat"><div class="v">${fmtPrice(w.price)}</div><div class="k">Prix</div></div>
        </div>
        <p class="card-text">${esc(w.description)}</p>
        <div class="card-meta">${(w.ammo || []).map(a => `<span class="chip">${esc(a)}</span>`).join('')}</div>
      </div>
    </article>`;
  }

  function renderGrid(grid, weapons) {
    const cat = grid.dataset.category;
    const tier = grid.dataset.tier;
    const variant = grid.dataset.variant || 'default';
    let list = weapons.filter(w => (!cat || w.category === cat) && (!tier || w.tier === tier));
    if (!list.length) {
      grid.innerHTML = '<p class="text-muted">Aucune arme dans ce segment pour le moment.</p>';
      return;
    }
    grid.innerHTML = list.map(w => weaponCard(w, variant)).join('');
  }

  function renderTierList(out, weapons) {
    const groups = {};
    weapons.forEach(w => { (groups[w.tier] = groups[w.tier] || []).push(w); });
    const titles = {
      S: 'Tier S — Apex Meta',
      A: 'Tier A — Pertinence réelle',
      B: 'Tier B — Jouable, situationnel',
      C: 'Tier C — Budget / niche',
      D: 'Tier D — À éviter'
    };
    out.innerHTML = ['S', 'A', 'B', 'C', 'D']
      .filter(t => groups[t] && groups[t].length)
      .map(t => `
        <div class="tier-group">
          <div class="tier-group-head"><span class="tier-badge tier-${t.toLowerCase()}">${t}</span><h3>${titles[t]}</h3></div>
          <div class="grid grid--2">
            ${groups[t].map(w => `
              <div class="tier-row">
                <span class="tier-badge tier-${t.toLowerCase()}">${t}</span>
                <span class="tier-name">${esc(w.name)}${w.isNew ? ' <span class="badge badge-s7">S7</span>' : ''}</span>
                <span class="tier-reason">${esc(w.description)}</span>
              </div>`).join('')}
          </div>
        </div>`).join('');
  }
})();
