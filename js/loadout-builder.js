/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — loadout-builder.js (S15)
   Constructeur de kit libre : vous choisissez chaque pièce,
   l'outil calcule le coût, la masse, la mobilité, la cadence,
   le contrôle du recul et la compatibilité tier / munitions.
   Données : js/data-weapons.json, data-armors.json, data-ammo.json,
             data-builds.json.
   Le calcul de pénétration est une ESTIMATION communautaire
   (PL = floor(pénétration / 10)), pas une donnée officielle.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const ROOT = document.querySelector('.loadout-builder');
  if (!ROOT) return;

  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, m =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
  const kf = n => (typeof n === 'number' ? Math.round(n).toLocaleString('fr-FR') + ' K' : '—');

  /* Poids de référence (kg) — estimations de marche issues de la
     communauté, cohérentes avec les valeurs de data-armors.json. */
  const WEIGHT = {
    weapon: 3.4,      // arme de base
    sniper: 4.6,
    smg: 2.6,
    lmg: 6.8,
    shotgun: 3.9,
    pistol: 1.1,
    helmet: 1.6,
    rig: 2.2,
    backpack: 1.8,
    headset: 0.4,
    medical: 0.9,
    ammoPerRound: 0.024,   // ~24 g la cartouche (chargeur compris)
    magPerRound: 0.031     // ~31 g la cartouche chargée
  };

  const ATTACH = {
    optic: { name: 'Optique', price: 45000, weight: 0.3, note: 'Réticule, grossissement, viseur thermique' },
    suppressor: { name: 'Silencieux', price: 78000, weight: 0.5, note: 'Réduit la signature sonore ; incompatibilité possible selon le calibre' },
    grip: { name: 'Poignée verticale', price: 22000, weight: 0.2, note: 'Contrôle du recul en CQB' },
    stock: { name: 'Crosse', price: 34000, weight: 0.4, note: 'Stabilise le tir, allonge la cadence' },
    mag: { name: 'Chargeur étendu', price: 26000, weight: 0.3, note: 'Plus de munitions par recharge' }
  };

  const ATTACH_ORDER = ['optic', 'suppressor', 'grip', 'stock', 'mag'];

  let D = null;
  let state = {
    mode: 'normal',
    budget: 450000,
    weapon: null,
    armor: null,
    ammo: null,
    rounds: 120,
    attach: { optic: false, suppressor: false, grip: false, stock: false, mag: false }
  };

  /* ── Chargement ─────────────────────────────────────────────── */
  Promise.all([
    fetch('../js/data-weapons.json').then(r => r.json()),
    fetch('../js/data-armors.json').then(r => r.json()),
    fetch('../js/data-ammo.json').then(r => r.json()),
    fetch('../js/data-builds.json').then(r => r.json())
  ]).then(([weapons, armors, ammo, builds]) => {
    D = {
      weapons: weapons.weapons || [],
      armors: armors.armors || [],
      ammo: ammo.ammo || [],
      modes: builds.modes,
      gear: builds.gear,
      budgets: builds.budgets,
      ammoBudget: builds.ammoBudget
    };
    initUI();
    resetPicks();
    compute();
  }).catch(err => {
    console.error('[ABI NEXUS] loadout-builder', err);
    ROOT.innerHTML = '<div class="callout callout-danger"><h4>Données indisponibles</h4><p>Impossible de charger les fiches de référence. Rechargez la page.</p></div>';
  });

  /* ── Interface ───────────────────────────────────────────────── */
  function initUI() {
    // Les resultats sont recalcules en direct : la region est annoncee
    // aux lecteurs d'ecran (WCAG 4.1.3 Status Messages).
    const outLive = ROOT.querySelector('.lb-out');
    if (outLive) outLive.setAttribute('aria-live', 'polite');
    const modeSel = ROOT.querySelector('#lb-mode');
    const budget = ROOT.querySelector('#lb-budget');
    const budgetOut = ROOT.querySelector('#lb-budget-val');
    const rounds = ROOT.querySelector('#lb-rounds');

    modeSel.innerHTML = D.modes.map(m =>
      '<option value="' + m.id + '">' + esc(m.label) + ' — plafond T' + m.tierCap + '</option>').join('');

    function syncBudget() {
      budgetOut.textContent = Number(budget.value).toLocaleString('fr-FR') + ' K';
    }
    function applyBudget(modeId) {
      const b = (D.budgets && D.budgets[modeId]) || D.budgets[D.modes[0].id];
      budget.min = b.min; budget.max = b.max; budget.step = 10000; budget.value = b.default;
      syncBudget();
    }
    syncBudget();
    applyBudget(modeSel.value);

    modeSel.addEventListener('change', () => { state.mode = modeSel.value; applyBudget(modeSel.value); resetPicks(); compute(); });
    budget.addEventListener('input', syncBudget);
    budget.addEventListener('change', compute);
    rounds.addEventListener('input', () => {
      state.rounds = Number(rounds.value);
      ROOT.querySelector('#lb-rounds-val').textContent = state.rounds + ' cartouches';
      compute();
    });

    ROOT.querySelector('#lb-reset').addEventListener('click', () => { resetPicks(); compute(); });
    const codeBtn = ROOT.querySelector('#lb-code-toggle');
    if (codeBtn) codeBtn.addEventListener('click', () => {
      const pre = ROOT.querySelector('.lb-code');
      pre.classList.toggle('show');
      codeBtn.textContent = pre.classList.contains('show') ? 'Masquer le récapitulatif' : 'Afficher le récapitulatif';
    });

    // Sélecteurs
    const wSel = ROOT.querySelector('#lb-weapon');
    wSel.innerHTML = '<option value="">— Choisir une arme —</option>' +
      D.weapons.slice().sort((a, b) => a.price - b.price).map(w =>
        '<option value="' + w.id + '">' + esc(w.name) + ' — ' + kf(w.price) + ' · ' + esc(w.caliber) + '</option>').join('');
    wSel.addEventListener('change', () => {
      state.weapon = D.weapons.find(w => w.id === wSel.value) || null;
      if (state.weapon) {
        const pool = D.ammo.filter(a => a.caliber === state.weapon.caliber);
        if (pool.length && (!state.ammo || !pool.some(a => a.id === state.ammo.id))) {
          state.ammo = pool.slice().sort((a, b) => b.tier - a.tier)[0];
        }
      }
      ROOT.querySelector('#lb-ammo').innerHTML = ammoOptions();
      compute();
    });

    const aSel = ROOT.querySelector('#lb-armor');
    aSel.innerHTML = '<option value="">— Choisir un gilet —</option>' +
      D.armors.slice().sort((a, b) => b.tier - a.tier || a.price - b.price).map(a =>
        '<option value="' + a.id + '">T' + a.tier + ' — ' + esc(a.name) + ' (' + esc(a.material) + ') — ' + kf(a.price) + '</option>').join('');
    aSel.addEventListener('change', () => {
      state.armor = D.armors.find(x => x.id === aSel.value) || null;
      compute();
    });

    const mSel = ROOT.querySelector('#lb-ammo');
    mSel.addEventListener('change', () => {
      state.ammo = D.ammo.find(a => a.id === mSel.value) || null;
      compute();
    });

    ROOT.querySelectorAll('.lb-attach input[type="checkbox"]').forEach(cb => {
      cb.addEventListener('change', () => { state.attach[cb.dataset.attach] = cb.checked; compute(); });
    });
  }

  function ammoOptions() {
    const caliber = state.weapon ? state.weapon.caliber : null;
    const pool = caliber ? D.ammo.filter(a => a.caliber === caliber) : [];
    if (!pool.length) {
      return '<option value="">— Aucune munition compatible —</option>';
    }
    return '<option value="">— Choisir une munition —</option>' +
      pool.slice().sort((a, b) => b.tier - a.tier || b.penetration - a.penetration).map(a =>
        '<option value="' + a.id + '"' + (state.ammo && state.ammo.id === a.id ? ' selected' : '') + '>' +
        esc(a.name) + ' — T' + a.tier + ' · PL ' + a.pierceLevel + ' · ' + a.penetration + ' pén. · ' + kf(a.price) + '/cartouche</option>').join('');
  }

  function resetPicks() {
    state.weapon = null;
    state.armor = null;
    state.ammo = null;
    state.attach = { optic: false, suppressor: false, grip: false, stock: false, mag: false };
    ROOT.querySelector('#lb-weapon').value = '';
    ROOT.querySelector('#lb-armor').value = '';
    ROOT.querySelector('#lb-ammo').innerHTML = '<option value="">— Choisir une munition —</option>';
    ROOT.querySelectorAll('.lb-attach input[type="checkbox"]').forEach(cb => { cb.checked = false; });
  }

  /* ── Calcul ──────────────────────────────────────────────────── */
  function compute() {
    if (!D) return;
    const mode = D.modes.find(m => m.id === state.mode) || D.modes[0];
    const cap = mode.tierCap;
    const gear = D.gear[mode.id];
    const rounds = state.rounds;

    /* Coût */
    let cost = 0;
    const lines = [];
    if (state.weapon) {
      cost += state.weapon.price;
      lines.push({ k: 'Arme', n: state.weapon.name, v: state.weapon.price, note: state.weapon.caliber + ' · ' + state.weapon.rpm + ' RPM' });
    }
    if (state.ammo) {
      const unit = state.ammo.price * (state.attach.mag ? 1.12 : 1);
      const c = Math.round(unit * rounds);
      cost += c;
      lines.push({ k: 'Munitions', n: state.ammo.name + ' ×' + rounds, v: c, note: 'PL ' + state.ammo.pierceLevel + ' · pénétration ' + state.ammo.penetration + ' · ' + state.ammo.damage + ' dégâts chair' });
    }
    if (state.armor) {
      cost += state.armor.price;
      lines.push({ k: 'Gilet', n: state.armor.name + ' (T' + state.armor.tier + ')', v: state.armor.price, note: state.armor.material + ' · ' + state.armor.durability + ' durabilité' });
    }
    if (gear) {
      ['helmet', 'rig', 'backpack', 'headset', 'medical'].forEach(k => {
        const g = gear[k];
        if (!g) return;
        cost += g.price;
        lines.push({ k: ({ helmet: 'Casque', rig: 'Rig', backpack: 'Sac', headset: 'Audio', medical: 'Médical' })[k], n: g.name, v: g.price, note: g.note });
      });
    }
    ATTACH_ORDER.forEach(k => {
      if (!state.attach[k]) return;
      cost += ATTACH[k].price;
      lines.push({ k: 'Attachement', n: ATTACH[k].name, v: ATTACH[k].price, note: ATTACH[k].note });
    });

    /* Masse */
    let weight = 0;
    if (state.weapon) {
      const cat = state.weapon.category || '';
      let base = WEIGHT.weapon;
      if (/Sniper/.test(cat)) base = WEIGHT.sniper;
      else if (/SMG/.test(cat)) base = WEIGHT.smg;
      else if (/LMG|Mitraille/.test(cat)) base = WEIGHT.lmg;
      else if (/Shotgun|Fusil à pompe/i.test(cat)) base = WEIGHT.shotgun;
      else if (/Pistolet/.test(cat)) base = WEIGHT.pistol;
      weight += base;
    }
    if (state.ammo) weight += rounds * (state.attach.mag ? WEIGHT.magPerRound : WEIGHT.ammoPerRound);
    if (state.armor) weight += state.armor.weight;
    if (gear) {
      weight += WEIGHT.helmet + WEIGHT.rig + WEIGHT.backpack + WEIGHT.headset + WEIGHT.medical;
    }
    ATTACH_ORDER.forEach(k => { if (state.attach[k]) weight += ATTACH[k].weight; });

    /* Mobilité : pénalité de vitesse cumulée (gilet + masse + ergonomie) */
    const speedPenalty = state.armor ? state.armor.speedPenalty : 0;
    const massPenalty = Math.max(0, (weight - 10)) * 1.6;
    const mobility = Math.max(0, Math.min(100, 100 - speedPenalty - massPenalty));

    /* Cadence / recul */
    const rpm = state.weapon ? state.weapon.rpm : 0;
    let recoilControl = state.weapon ? Math.max(0, Math.min(100, state.weapon.ergo - (state.weapon.recoil - 40) * 0.9)) : 0;
    if (state.attach.grip) recoilControl = Math.min(100, recoilControl + 12);
    if (state.attach.stock) recoilControl = Math.min(100, recoilControl + 6);

    /* Compatibilité tier */
    const issues = [];
    if (state.weapon && state.weapon.tier === 'S' && cap <= 4) {
      issues.push('Arme de tier S alors que le mode ' + mode.label + ' plafonne à T' + cap + ' : son prix n’a de sens qu’à partir du Lockdown.');
    }
    if (state.armor && state.armor.tier < cap) {
      issues.push('Gilet T' + state.armor.tier + ' alors que le mode autorise T' + cap + ' : les adversaires peuvent porter du T' + cap + '.');
    }
    if (state.ammo && state.ammo.tier < cap) {
      issues.push('Munition T' + state.ammo.tier + ' (PL ' + state.ammo.pierceLevel + ') alors que le mode autorise T' + cap + ' : prévoyez un cran de plus face à une cible équipée.');
    }
    if (state.ammo && state.ammo.tier > cap) {
      issues.push('Munition T' + state.ammo.tier + ' non autorisée en ' + mode.label + ' (plafond T' + cap + ').');
    }
    if (!state.weapon) issues.push('Aucune arme sélectionnée : le coût et la masse affichés ne sont que partiels.');
    if (!state.ammo && state.weapon) issues.push('Aucune munition sélectionnée : le kit ne peut pas tirer.');
    if (state.attach.suppressor && state.weapon && /Sniper|Shotgun|Fusil à pompe/i.test(state.weapon.category || '')) {
      issues.push('Silencieux peu adapté à ' + state.weapon.name + ' : vérifiez la compatibilité réelle dans le jeu avant de l’équiper.');
    }

    /* Estimation de pénétration — méthode communautaire, non officielle */
    const penRows = [];
    if (state.ammo && state.armor) {
      const pl = Math.floor(state.ammo.penetration / 10); // formule communautaire non publiée par l'éditeur
      const armorTier = state.armor.tier;
      const always = pl > armorTier;
      const margin = pl - armorTier;
      penRows.push({
        label: state.armor.name,
        pct: Math.max(4, Math.min(100, (pl / 6) * 100)),
        right: 'PL ' + pl + ' vs T' + armorTier,
        good: always,
        note: always
          ? 'Pénétration systématique (estimation).'
          : 'Pénétration partielle : ' + (margin <= 0 ? 'ne traverse pas la plaque' : 'peut ne pas traverser') + ' (estimation).'
      });
    }

    const ratio = cost / state.budget;
    const ratioClass = ratio > 1 ? 'bad' : ratio > 0.95 ? '' : 'good';

    /* Rendu */
    const out = ROOT.querySelector('.lb-out');
    out.innerHTML =
      '<div class="lb-summary">' +
        '<div class="lb-cell"><div class="lb-v ' + ratioClass + '">' + Math.round(cost / 1000).toLocaleString('fr-FR') + ' K</div><div class="lb-k">Coût total</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + Math.round(ratio * 100) + ' %</div><div class="lb-k">Du budget</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + weight.toFixed(1) + ' kg</div><div class="lb-k">Masse</div></div>' +
        '<div class="lb-cell"><div class="lb-v ' + (mobility >= 70 ? 'good' : mobility >= 50 ? '' : 'bad') + '">' + Math.round(mobility) + '</div><div class="lb-k">Mobilité /100</div></div>' +
      '</div>' +
      '<div class="lb-summary">' +
        '<div class="lb-cell"><div class="lb-v">' + (rpm || '—') + '</div><div class="lb-k">Cadence RPM</div></div>' +
        '<div class="lb-cell"><div class="lb-v ' + (recoilControl >= 60 ? 'good' : recoilControl >= 40 ? '' : 'bad') + '">' + (state.weapon ? Math.round(recoilControl) : '—') + '</div><div class="lb-k">Contrôle du recul</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + (state.ammo ? state.ammo.pierceLevel : '—') + '</div><div class="lb-k">Pierce Level</div></div>' +
        '<div class="lb-cell"><div class="lb-v">' + (state.armor ? 'T' + state.armor.tier : '—') + '</div><div class="lb-k">Tier gilet</div></div>' +
      '</div>' +
      (penRows.length
        ? '<div><h4 class="lb-h4">Estimation de pénétration</h4><div class="lb-pen">' +
          penRows.map(r =>
            '<div class="lb-pen-row"><span>' + esc(r.label) + '</span>' +
            '<span class="lb-pen-track"><i class="lb-pen-fill' + (r.good ? ' always' : '') + '" style="width:' + r.pct.toFixed(0) + '%"></i></span>' +
            '<span>' + esc(r.right) + '</span></div>' +
            '<p class="lb-sub">' + esc(r.note) + '</p>').join('') +
          '</div><p class="lb-note">Méthode communautaire (PL = floor(pénétration / 10)). Estimation, non publiée par l’éditeur.</p></div>'
        : '') +
      '<div><h4 class="lb-h4">Détail du kit</h4><ul class="lb-kit">' +
        (lines.length
          ? lines.map(l => '<li><span>' + esc(l.k) + '</span><span>' + esc(l.n) + '</span><span>' + kf(l.v) + '</span></li>').join('')
          : '<li><span colspan="3" class="text-muted">Sélectionnez une arme pour démarrer.</span></li>') +
      '</ul></div>' +
      (issues.length
        ? '<div class="callout callout-warning"><h4>Points de vigilance</h4><ul>' + issues.map(i => '<li>' + esc(i) + '</li>').join('') + '</ul></div>'
        : '<div class="callout callout-success"><h4>Kit cohérent</h4><p>Aucune incompatibilité détectée avec le plafond du mode.</p></div>') +
      '<pre class="lb-code">' + esc(buildText(mode, lines, cost, weight, mobility, ratio)) + '</pre>';

    /* récapitulatif texte */
    const pre = ROOT.querySelector('.lb-code');
    if (pre) pre.textContent = buildText(mode, lines, cost, weight, mobility, ratio);
  }

  function buildText(mode, lines, cost, weight, mobility, ratio) {
    return [
      'LOADOUT — ' + mode.label + ' (plafond T' + mode.tierCap + ')',
      ...lines.map(l => (l.k + '        ').slice(0, 10) + ' : ' + l.n + ' — ' + kf(l.v)),
      'TOTAL     : ' + kf(cost) + ' (' + Math.round(ratio * 100) + ' % du budget)',
      'MASSE     : ' + weight.toFixed(1) + ' kg · Mobilité ' + Math.round(mobility) + '/100'
    ].join('\n');
  }

  window.ABILoadoutBuilder = { compute, getState: () => state };
})();
