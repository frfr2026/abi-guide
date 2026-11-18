/* ABI NEXUS — Affichage dynamique des données d'armures (S7 Utopia) */
(function () {
  'use strict';
  const GRID = document.querySelector('.armor-grid');
  const TIER_OUT = document.querySelector('.armor-tier-output');
  if (!GRID && !TIER_OUT) return;

  const RANK = { S: 0, A: 1, B: 2, C: 3, D: 4 };
  const fmtPrice = n => (typeof n === 'number' ? n.toLocaleString('fr-FR') + ' K' : '—');
  const esc = s => String(s).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  fetch('../js/data-armors.json')
    .then(r => r.json())
    .then(data => {
      const armors = Array.isArray(data) ? data : (data.armors || []);
      armors.sort((a, b) => b.tier - a.tier);
      if (GRID) renderGrid(GRID, armors);
      if (TIER_OUT) renderTier(TIER_OUT, armors);
    })
    .catch(err => {
      console.error('[ABI NEXUS] data-armors.json', err);
      if (GRID) GRID.innerHTML = '<div class="callout callout-danger"><p>Données temporairement indisponibles.</p></div>';
    });

  function armorCard(a) {
    const img = a.image || '../img/armures/armor-t6.jpg';
    return `
    <article class="card armor-card">
      <div class="card-media">
        <img src="${esc(img)}" alt="${esc(a.name)}" loading="lazy" onerror="this.onerror=null;this.src='../img/hero/hero-armures.jpg'">
        <span class="armor-level">${esc(a.tier)}</span>
        <h3 class="weapon-name">${esc(a.name)}</h3>
      </div>
      <div class="card-body">
        <p class="small text-muted" style="margin:0">${esc(a.material)} · Vendeur : ${esc(a.trader)}</p>
        <div class="weapon-stats">
          <div class="weapon-stat"><div class="v">${a.durability}</div><div class="k">Durabilité</div></div>
          <div class="weapon-stat"><div class="v">${a.weight} kg</div><div class="k">Poids</div></div>
          <div class="weapon-stat"><div class="v">${a.speedPenalty}%</div><div class="k">Vitesse −</div></div>
          <div class="weapon-stat"><div class="v">${a.ergo}</div><div class="k">Ergonomie</div></div>
          <div class="weapon-stat"><div class="v">T${esc(a.tier)}</div><div class="k">Tier</div></div>
          <div class="weapon-stat"><div class="v">${fmtPrice(a.price)}</div><div class="k">Prix</div></div>
        </div>
        <div class="bar-row durability-bar"><div class="durability-fill" style="width:${Math.min(100, a.durability / 1.5)}%"></div></div>
        <p class="card-text">${esc(a.description)}</p>
        <div class="card-meta">${(a.zones || []).map(z => `<span class="chip">${esc(z)}</span>`).join('')}</div>
      </div>
    </article>`;
  }

  function renderGrid(grid, armors) {
    const tier = grid.dataset.tier;
    let list = armors.filter(a => !tier || String(a.tier) === String(tier));
    if (!list.length) { grid.innerHTML = '<p class="text-muted">Aucune armure dans ce segment.</p>'; return; }
    grid.innerHTML = list.map(armorCard).join('');
  }

  function renderTier(out, armors) {
    const groups = {};
    armors.forEach(a => { (groups[a.tierList] = groups[a.tierList] || []).push(a); });
    const titles = { S: 'S — Protection ultime', A: 'A — Excellent compromis', B: 'B — Correct / budget', C: 'C — Bas de gamme', D: 'D — À éviter' };
    out.innerHTML = ['S', 'A', 'B', 'C', 'D']
      .filter(t => groups[t] && groups[t].length)
      .map(t => `
        <div class="tier-group">
          <div class="tier-group-head"><span class="tier-badge tier-${t.toLowerCase()}">${t}</span><h3>${titles[t]}</h3></div>
          <div class="grid grid--2">
            ${groups[t].map(a => `
              <div class="tier-row">
                <span class="tier-badge tier-${t.toLowerCase()}">${t}</span>
                <span class="tier-name">${esc(a.name)} <span class="small text-muted">T${esc(a.tier)}</span></span>
                <span class="tier-reason">${esc(a.description)}</span>
              </div>`).join('')}
          </div>
        </div>`).join('');
  }
})();
