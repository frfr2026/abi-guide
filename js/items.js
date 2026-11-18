/* ABI NEXUS — Affichage dynamique des données d'objets (S7 Utopia) */
(function () {
  'use strict';
  const GRID = document.querySelector('.items-grid');
  const LIST = document.querySelector('.items-list');
  if (!GRID && !LIST) return;

  const RARITY_LABEL = {
    red: 'Red Tier', purple: 'Purple', blue: 'Blue', green: 'Green', white: 'White'
  };
  const fmt = n => (typeof n === 'number' ? n.toLocaleString('fr-FR') + ' K' : '—');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  fetch('../js/data-items.json')
    .then(r => r.json())
    .then(data => {
      const items = Array.isArray(data) ? data : (data.items || []);
      const order = { red: 0, purple: 1, blue: 2, green: 3, white: 4 };
      items.sort((a, b) => (order[a.rarity] ?? 9) - (order[b.rarity] ?? 9) || (b.price || 0) - (a.price || 0));
      if (GRID) GRID.innerHTML = items.map(card).join('');
      if (LIST) renderList(LIST, items);
    })
    .catch(err => {
      console.error('[ABI NEXUS] data-items.json', err);
      const msg = '<div class="callout callout-danger"><p>Données temporairement indisponibles.</p></div>';
      if (GRID) GRID.innerHTML = msg;
      if (LIST) LIST.innerHTML = msg;
    });

  function card(it) {
    const img = it.image || '../img/items/red-drop.jpg';
    return `
    <article class="card item-card">
      <div class="card-media">
        <img src="${esc(img)}" alt="${esc(it.name)}" loading="lazy" onerror="this.onerror=null;this.src='../img/items/red-drop.jpg'">
        <span class="rarity-badge rarity-${esc(it.rarity)}">${esc(RARITY_LABEL[it.rarity] || it.rarity)}</span>
        ${it.isNew ? '<span class="badge badge-s7 item-new">Nouveau</span>' : ''}
        <h3 class="weapon-name">${esc(it.name)}</h3>
      </div>
      <div class="card-body">
        <p class="small text-muted" style="margin:0 0 .4rem">${esc(it.category)}${it.season ? ' · Saison ' + esc(it.season) : ''}</p>
        <div class="weapon-stats">
          <div class="weapon-stat"><div class="v">${fmt(it.price)}</div><div class="k">Valeur Koen</div></div>
          <div class="weapon-stat"><div class="v">${esc(it.rarity)}</div><div class="k">Rareté</div></div>
        </div>
        <p class="card-text">${esc(it.description)}</p>
      </div>
    </article>`;
  }

  function renderList(root, items) {
    const cat = root.dataset.category;
    const list = items.filter(i => !cat || i.category === cat);
    root.innerHTML = `
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Objet</th><th>Rareté</th><th>Catégorie</th><th>Valeur (Koen)</th><th>Saison</th></tr></thead>
          <tbody>
            ${list.map(i => `<tr>
              <td><strong>${esc(i.name)}</strong>${i.isNew ? ' <span class="badge badge-s7">Nouveau</span>' : ''}</td>
              <td><span class="rarity-badge rarity-${esc(i.rarity)}">${esc(RARITY_LABEL[i.rarity] || i.rarity)}</span></td>
              <td>${esc(i.category)}</td>
              <td>${typeof i.price === 'number' ? i.price.toLocaleString('fr-FR') : '—'}</td>
              <td>${esc(i.season || '—')}</td>
            </tr>`).join('')}
          </tbody>
        </table>
      </div>`;
  }
})();
