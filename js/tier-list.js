/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — tier-list.js (S15)
   Tier list interactive : on réordonne les armes à la souris, au
   clavier ou au tactile, et le classement est sauvegardé localement.
   POINT DE TRANSPARENCE : le classement affiché au chargement est un
   consensus communautaire (moyenne de plusieurs tier lists publiques
   recoupées en novembre 2026), jamais une classification officielle
   de l'éditeur.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const ROOT = document.querySelector('.tier-list-builder');
  if (!ROOT) return;

  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, m =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  const TIERS = ['S', 'A', 'B', 'C'];
  const STORE_KEY = 'abi-nexus-tier-list-v1';

  /* Consensus communautaire de départ : moyenne pondérée de plusieurs
     tier lists publiques (méthode "consensus moyen", listes récentes
     pondérées davantage). Recoupé le 17 novembre 2026. */
  const CONSENSUS = {
    a545: 'S', h416: 'S', ak12: 'S', u191: 'S', p90: 'S', m24: 'S',
    ak15sc: 'A', aek971: 'A', an94: 'A', fal: 'A', m110: 'A', mk14: 'A', sj16: 'A',
    m4a1: 'B', mpx: 'B', vss: 'B', usas12: 'B', rpk16: 'B', t88: 'B',
    pcc9: 'C', mosin: 'C', sks: 'C', banshee: 'C', vector: 'C'
  };

  const SOURCES = [
    { name: 'qrts.ru — tier list armes', type: 'Communautaire', date: 'nov. 2026', method: 'Consensus moyen de plusieurs listes publiques' },
    { name: 'gamer-choice.com — tier list 2026', type: 'Communautaire', date: 'nov. 2026', method: 'Retours communautaires et contenus vidéo pondérés' },
    { name: 'news.bittopup.com — tier list post-op Unbound', type: 'Communautaire', date: 'nov. 2026', method: 'Critères : pénétration, recul, mobilité, viabilité solo/équipe' }
  ];

  let WEAPONS = [];
  let state = null;   // { S: [ids], A: [...], B: [...], C: [...] }
  let custom = false;

  Promise.all([fetch('../js/data-weapons.json').then(r => r.json())]).then(([w]) => {
    WEAPONS = w.weapons || [];
    load();
    buildSelectors();
    render();
  }).catch(err => {
    console.error('[ABI NEXUS] tier-list', err);
    ROOT.innerHTML = '<div class="callout callout-danger"><h4>Données indisponibles</h4><p>Impossible de charger la liste des armes.</p></div>';
  });

  function defaultState() {
    const st = { S: [], A: [], B: [], C: [] };
    WEAPONS.forEach(w => {
      const t = CONSENSUS[w.id] || 'B';
      st[t].push(w.id);
    });
    return st;
  }

  function load() {
    try {
      const raw = localStorage.getItem(STORE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && parsed.S && parsed.A && parsed.B && parsed.C) {
          state = parsed;
          custom = true;
          return;
        }
      }
    } catch (e) { /* stockage indisponible */ }
    state = defaultState();
  }

  function save() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(state)); } catch (e) { /* ignoré */ }
  }

  function buildSelectors() {
    const status = ROOT.querySelector('#tlx-status');
    if (status) status.setAttribute('aria-live', 'polite');
    const cat = ROOT.querySelector('#tlx-cat');
    const cats = Array.from(new Set(WEAPONS.map(w => w.category))).sort();
    cat.innerHTML = '<option value="">Toutes les catégories</option>' +
      cats.map(c => '<option value="' + esc(c) + '">' + esc(c) + '</option>').join('');
    cat.addEventListener('change', render);

    const reset = ROOT.querySelector('#tlx-reset');
    if (reset) reset.addEventListener('click', () => {
      state = defaultState();
      custom = false;
      save();
      render();
      const badge = ROOT.querySelector('#tlx-status');
      if (badge) badge.textContent = 'Classement réinitialisé sur le consensus communautaire.';
    });

    const share = ROOT.querySelector('#tlx-share');
    if (share) share.addEventListener('click', () => {
      const lines = TIERS.map(t => t + ' : ' + (state[t] || []).map(id => {
        const w = WEAPONS.find(x => x.id === id);
        return w ? w.name : id;
      }).join(', ')).join('\n');
      const txt = 'ABI NEXUS — Tier list personnalisée (consensus communautaire du 17 nov. 2026)\n' + lines;
      const btn = share;
      const done = () => { btn.textContent = 'Copié ✓'; setTimeout(() => { btn.textContent = 'Copier le classement'; }, 1800); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(txt).then(done).catch(() => fallback());
      } else { fallback(); }
      function fallback() {
        const ta = document.createElement('textarea');
        ta.value = txt; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); done(); } catch (e) { btn.textContent = 'Copie impossible'; }
        document.body.removeChild(ta);
      }
    });
  }

  function render() {
    const cat = ROOT.querySelector('#tlx-cat').value;
    const board = ROOT.querySelector('.tlx-board');
    const visible = new Set(
      WEAPONS.filter(w => !cat || w.category === cat).map(w => w.id)
    );

    board.innerHTML = TIERS.map(t => {
      const items = (state[t] || []).filter(id => visible.has(id));
      const hidden = (state[t] || []).length - items.length;
      return '<div class="tlx-tier" data-tier="' + t + '">' +
        '<div class="tlx-tier-head">' +
          '<h4>Tier ' + t + '</h4>' +
          '<span class="tlx-count">' + items.length + ' arme' + (items.length > 1 ? 's' : '') + (hidden ? ' (+' + hidden + ' hors filtre)' : '') + '</span>' +
        '</div>' +
        '<div class="tlx-drop" data-tier="' + t + '" role="list" aria-label="Tier ' + t + '">' +
          items.map(id => {
            const w = WEAPONS.find(x => x.id === id);
            if (!w) return '';
            return '<span class="tlx-chip" draggable="true" data-id="' + esc(w.id) + '" tabindex="0" role="listitem" aria-label="' + esc(w.name + ', tier ' + w.tier + '. Touche Espace pour descendre d\'un cran.') + '" title="' + esc(w.name + ' — ' + w.category) + '">' +
              '<span class="tlx-grip" aria-hidden="true">⠿</span>' +
              '<span>' + esc(w.name) + '</span>' +
              '<span class="tlx-tier-badge">' + esc(w.tier) + '</span>' +
            '</span>';
          }).join('') +
        '</div>' +
      '</div>';
    }).join('');

    bindDnD(board);

    const badge = ROOT.querySelector('#tlx-status');
    if (badge) {
      badge.textContent = custom
        ? 'Classement personnalisé, enregistré dans ce navigateur.'
        : 'Classement initial issu du consensus communautaire (nov. 2026).';
    }
  }

  /* ── Glisser-déposer + clavier ───────────────────────────────── */
  function bindDnD(board) {
    let dragged = null;

    board.querySelectorAll('.tlx-chip').forEach(chip => {
      chip.addEventListener('dragstart', e => {
        dragged = chip;
        chip.classList.add('dragging');
        try { e.dataTransfer.setData('text/plain', chip.dataset.id); e.dataTransfer.effectAllowed = 'move'; } catch (err) { /* ignoré */ }
      });
      chip.addEventListener('dragend', () => {
        chip.classList.remove('dragging');
        dragged = null;
      });
      /* clavier : Espace sélectionne, flèches montent / descendent */
      chip.addEventListener('keydown', e => {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          const id = chip.dataset.id;
          const tier = chip.closest('.tlx-drop').dataset.tier;
          const idx = TIERS.indexOf(tier);
          if (idx > -1 && idx < TIERS.length - 1) {
            move(id, TIERS[idx + 1], true);
          }
        }
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
          e.preventDefault();
          const drop = chip.closest('.tlx-drop');
          const chips = Array.from(drop.querySelectorAll('.tlx-chip'));
          const i = chips.indexOf(chip);
          const j = e.key === 'ArrowLeft' ? i - 1 : i + 1;
          if (chips[j]) {
            if (e.key === 'ArrowLeft') drop.insertBefore(chip, chips[j]);
            else drop.insertBefore(chips[j], chip);
            chip.focus();
            commit();
          }
        }
      });
    });

    board.querySelectorAll('.tlx-drop').forEach(drop => {
      drop.addEventListener('dragover', e => { e.preventDefault(); drop.classList.add('dragover'); });
      drop.addEventListener('dragleave', () => drop.classList.remove('dragover'));
      drop.addEventListener('drop', e => {
        e.preventDefault();
        drop.classList.remove('dragover');
        const id = (e.dataTransfer && e.dataTransfer.getData('text/plain')) || (dragged && dragged.dataset.id);
        if (id) move(id, drop.dataset.tier, true);
      });
    });
  }

  /* Déplace une arme dans un tier et enregistre le classement. */
  function move(id, destTier, focusAfter) {
    const from = TIERS.find(t => (state[t] || []).indexOf(id) !== -1);
    if (!from) return;
    state[from] = state[from].filter(x => x !== id);
    if (!state[destTier]) state[destTier] = [];
    state[destTier].push(id);
    custom = true;
    save();
    render();
    if (focusAfter) {
      const chip = ROOT.querySelector('.tlx-chip[data-id="' + id + '"]');
      if (chip) chip.focus();
    }
  }

  /* Source de la méthode — affichée pour que l'utilisateur sache
     d'où viennent les classes et ce qu'elles valent. */
  function renderSources() {
    const box = ROOT.querySelector('.tlx-sources');
    if (!box) return;
    box.innerHTML =
      '<h4>Origine du classement et méthode</h4>' +
      '<ul>' + SOURCES.map(s =>
        '<li><strong>' + esc(s.name) + '</strong> — ' + esc(s.type) + ', relevé le ' + esc(s.date) + '. Méthode : ' + esc(s.method) + '.</li>'
      ).join('') + '</ul>' +
      '<p class="tlx-note">Aucune de ces sources n’est l’éditeur : ce sont des classements communautaires. Le consensus moyen pondère davantage les listes les plus récentes. Vos modifications restent locales à votre navigateur et ne modifient pas la base du site.</p>';
  }

  document.addEventListener('DOMContentLoaded', renderSources);
  if (document.readyState !== 'loading') renderSources();

  window.ABITierList = { render, getState: () => state };
})();
