/* ABI NEXUS — Loadout Optimizer (Saison 7 : Utopia)
   Données : js/data-builds.json, js/data-weapons.json, js/data-armors.json, js/data-ammo.json
   Prix : Koen, valeurs indicatives. Le prix des munitions est donné par cartouche. */
(function () {
  'use strict';

  const TIERS = ['S', 'A', 'B', 'C'];
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  const fmt = n => (typeof n === 'number' ? n.toLocaleString('fr-FR') + ' K' : '—');

  /* ── Coeur de calcul (testable, sans DOM) ─────────────────────── */
  const Core = {
    /* Score d'une arme pour un rôle donné. Le coût est pondéré négativement. */
    scoreWeapon(w, role) {
      let s = 0;
      const tIdx = TIERS.indexOf(w.tier);
      s += (4 - (tIdx < 0 ? 3 : tIdx)) * 12;                  // tier
      s += Math.min(w.rpm, 900) / 900 * 26 * role.rpmBias;    // cadence
      s += Math.min(w.range, 130) / 130 * 26 * role.rangeBias; // portée
      s += Math.max(0, (w.ergo - 30) / 40) * 14;               // ergonomie
      s += Math.min(w.damage, 45) / 45 * 10;                   // dégâts de base
      s -= (w.price / 60000) * (1 - role.rpmBias * 0.3);       // pénalité de coût
      return s;
    },

    /* Arme du rôle la mieux notée dont le prix laisse de la place au reste du kit.
       available = part du budget restante que l'on accepte de consacrer à l'arme. */
    pickWeapon(weapons, role, cap, available) {
      const pool = weapons
        .filter(w => role.categories.indexOf(w.category) !== -1)
        .map(w => ({ w, s: Core.scoreWeapon(w, role) }))
        .sort((a, b) => b.s - a.s);
      if (!pool.length) return null;
      const affordable = pool.filter(x => x.w.price <= available);
      if (affordable.length) return affordable[0].w;
      // aucune arme affordable : on prend la moins chère du pool
      return pool.slice().sort((a, b) => a.w.price - b.w.price)[0].w;
    },

    /* Munition : meilleure pénétration autorisée par le plafond du mode. */
    pickAmmo(ammo, caliber, cap, maxUnitPrice) {
      const pool = ammo
        .filter(a => a.caliber === caliber && a.tier <= cap)
        .sort((a, b) => b.tier - a.tier || b.penetration - a.penetration);
      if (!pool.length) return null;
      const affordable = pool.filter(a => a.price <= maxUnitPrice);
      return (affordable[0] || pool[pool.length - 1]);
    },

    /* Gilet : on vise le tier maximal du mode (T4 en Normal, T5 en Lockdown, T6 en Forbidden),
       puis on dégrade d'un cran tant que le prix dépasse l'enveloppe budgetaire. */
    pickArmor(armors, cap, envelope) {
      const pool = armors.filter(a => a.tier <= cap);
      if (!pool.length) return null;
      for (let t = cap; t >= 1; t--) {
        const tierPool = pool.filter(a => a.tier === t)
          .sort((a, b) => b.durability - a.durability || b.ergo - a.ergo);
        if (!tierPool.length) continue;
        const affordable = tierPool.find(a => a.price <= envelope);
        if (affordable) return affordable;
        // aucun de ce tier n'entre dans l'enveloppe : on mémorise le moins cher pour plus tard
        if (t === cap) var fallback = tierPool[0];
      }
      return typeof fallback !== 'undefined' ? fallback : pool.slice().sort((a, b) => a.price - b.price)[0];
    },

    /* Calcule un kit complet. */
    build(data, modeId, roleId, budget) {
      const mode = data.modes.find(m => m.id === modeId) || data.modes[0];
      const role = data.roles.find(r => r.id === roleId) || data.roles[0];
      const cap = mode.tierCap;
      const gear = data.gear[mode.id];
      const rounds = role.id === 'support' ? data.ammoBudget.roundsHeavy : data.ammoBudget.rounds;

      const fixed = gear.helmet.price + gear.rig.price + gear.backpack.price
        + gear.headset.price + gear.medical.price;

      // Répartition de l'enveloppe disponible : 60 % arme, 25 % gilet, reste en munitions.
      const avail = Math.max(0, budget - fixed);
      const weapon = Core.pickWeapon(data.weapons, role, cap, avail * 0.6);
      if (!weapon) return null;

      const rest = Math.max(0, budget - fixed - weapon.price);
      const armor = Core.pickArmor(data.armors, cap, avail * 0.25);
      const ammo = Core.pickAmmo(data.ammo, weapon.caliber, cap, (rest * 0.8) / rounds);

      const ammoCost = ammo ? Math.round(ammo.price * rounds) : 0;
      const lines = [
        { k: 'Arme', n: weapon.name, v: weapon.price, note: weapon.caliber + ' · ' + weapon.rpm + ' RPM · ' + weapon.range + ' m · tier ' + weapon.tier },
        { k: 'Munitions', n: ammo ? ammo.name + ' ×' + rounds : '—', v: ammoCost, note: ammo ? 'PL ' + ammo.pierceLevel + ' · pénétration ' + ammo.penetration + ' · ' + ammo.damage + ' dégâts chair' : '' },
        { k: 'Gilet', n: armor ? armor.name : '—', v: armor ? armor.price : 0, note: armor ? 'T' + armor.tier + ' · ' + armor.material + ' · ' + armor.weight + ' kg · −' + armor.speedPenalty + ' % vitesse · ' + armor.ergo + ' ergonomie' : '' },
        { k: 'Casque', n: gear.helmet.name, v: gear.helmet.price, note: gear.helmet.note },
        { k: 'Rig', n: gear.rig.name, v: gear.rig.price, note: gear.rig.note },
        { k: 'Sac', n: gear.backpack.name, v: gear.backpack.price, note: gear.backpack.note },
        { k: 'Audio', n: gear.headset.name, v: gear.headset.price, note: gear.headset.note },
        { k: 'Médical', n: gear.medical.name, v: gear.medical.price, note: gear.medical.note }
      ];
      const total = lines.reduce((s, l) => s + (l.v || 0), 0);
      const ratio = total / budget;

      let verdict, vclass;
      if (ratio > 1.15) { verdict = 'Kit surdimensionné : vous risquez plus que votre raid ne rapporte.'; vclass = 'danger'; }
      else if (ratio > 0.95) { verdict = 'Kit au maximum de votre budget : correct, sans marge de manoeuvre.'; vclass = 'warning'; }
      else if (ratio < 0.45) { verdict = 'Kit très léger : excellent pour apprendre, dangereux en Lockdown face à des kits T5.'; vclass = 'success'; }
      else { verdict = 'Kit équilibré : le meilleur rapport risque / gain pour ce budget.'; vclass = 'success'; }

      const warnings = [];
      if (weapon.tier === 'S' && cap <= 4) warnings.push('Arme de tier S : son prix n\'a de sens qu\'à partir du Lockdown.');
      if (ammo && ammo.tier < cap) warnings.push('Munition PL ' + ammo.pierceLevel + ' alors que le mode autorise jusqu\'à PL ' + cap + ' : prévoyez de monter d\'un cran si votre cible est équipée.');
      if (armor && armor.tier < cap) warnings.push('Gilet T' + armor.tier + ' en mode ' + mode.label + ' : les adversaires peuvent porter du T' + cap + '.');
      if (role.id === 'sniper' && mode.id === 'normal') warnings.push('Un sniper en primaire est une mauvaise idée en Normal : la majorité des duels se joue à moins de 30 m.');
      if (role.id === 'cqb' && mode.id === 'forbidden') warnings.push('Un CQB en Forbidden : le loot y vaut 5 à 10 fois plus qu\'une mort.');
      if (role.id === 'loot' && weapon.tier === 'S') warnings.push('Arme de tier S en rôle Lointier : elle coûte plus qu\'elle ne rapporte si vous mourez.');
      if (ammo && ammo.pierceLevel >= 5 && mode.id === 'normal') warnings.push('Munition premium (PL ' + ammo.pierceLevel + ') sélectionnée en Normal : elle est inutilisée contre la classe 4.');

      const summary = [
        'BUILD ' + role.name.toUpperCase() + ' — ' + mode.label + ' (T' + cap + ' max)',
        'Arme      : ' + weapon.name + ' (' + weapon.caliber + ', ' + weapon.rpm + ' RPM, ' + weapon.range + ' m) — ' + fmt(weapon.price),
        'Munitions : ' + (ammo ? ammo.name + ' PL' + ammo.pierceLevel + ' ×' + rounds + ' (' + ammo.price + ' K/cartouche)' : '—'),
        'Gilet     : ' + (armor ? armor.name + ' T' + armor.tier + ' (' + armor.material + ')' : '—') + (armor ? ' — ' + fmt(armor.price) : ''),
        'Casque    : ' + gear.helmet.name + ' — ' + fmt(gear.helmet.price),
        'Rig       : ' + gear.rig.name + ' — ' + fmt(gear.rig.price),
        'Sac       : ' + gear.backpack.name + ' — ' + fmt(gear.backpack.price),
        'Audio     : ' + gear.headset.name + ' — ' + fmt(gear.headset.price),
        'Médical   : ' + gear.medical.name + ' — ' + fmt(gear.medical.price),
        'TOTAL     : ' + fmt(total) + ' (' + Math.round(ratio * 100) + ' % du budget)'
      ].join('\n');

      return { mode, role, cap, rounds, weapon, ammo, armor, gear, lines, total, ratio, verdict, vclass, warnings, summary };
    }
  };

  if (typeof window !== 'undefined') window.ABIOptimizerCore = Core;

  /* ── Interface ─────────────────────────────────────────────────── */
  const ROOT = typeof document !== 'undefined' ? document.querySelector('.optimizer') : null;
  if (!ROOT) return;

  let DATA = null;

  Promise.all([
    fetch('../js/data-builds.json').then(r => r.json()),
    fetch('../js/data-weapons.json').then(r => r.json()),
    fetch('../js/data-armors.json').then(r => r.json()),
    fetch('../js/data-ammo.json').then(r => r.json())
  ]).then(([builds, weapons, armors, ammo]) => {
    DATA = {
      modes: builds.modes,
      roles: builds.roles,
      gear: builds.gear,
      budgets: builds.budgets,
      ammoBudget: builds.ammoBudget,
      weapons: Array.isArray(weapons) ? weapons : (weapons.weapons || []),
      armors: Array.isArray(armors) ? armors : (armors.armors || []),
      ammo: Array.isArray(ammo) ? ammo : (ammo.ammo || [])
    };
    initUI();
    compute();
  }).catch(err => {
    console.error('[ABI NEXUS] optimizer', err);
    const out = ROOT.querySelector('.opt-result');
    if (out) out.innerHTML = '<div class="callout callout-danger"><h4>Données indisponibles</h4><p>Les fiches de référence n\'ont pas pu être chargées. Rechargez la page.</p></div>';
  });

  function initUI() {
    const resLive = ROOT.querySelector('.opt-result');
    if (resLive) resLive.setAttribute('aria-live', 'polite');
    const modeSel = ROOT.querySelector('#opt-mode');
    const roleSel = ROOT.querySelector('#opt-role');
    const budget = ROOT.querySelector('#opt-budget');
    const budgetOut = ROOT.querySelector('#opt-budget-val');

    modeSel.innerHTML = DATA.modes.map(m => '<option value="' + m.id + '">' + esc(m.label) + ' — T' + m.tierCap + ' max</option>').join('');
    roleSel.innerHTML = DATA.roles.map(r => '<option value="' + r.id + '">' + esc(r.name) + ' — tier ' + esc(r.tier) + '</option>').join('');

    // Chaque mode a sa propre enveloppe budgetaire : on la charge a chaque changement de mode.
    const sync = () => { budgetOut.textContent = Number(budget.value).toLocaleString('fr-FR') + ' K'; };
    const applyBudget = (modeId) => {
      const key = (DATA.budgets && DATA.budgets[modeId]) ? modeId : DATA.modes[0].id;
      const b = (DATA.budgets && DATA.budgets[key]) || null;
      if (!b) return;
      budget.min = b.min;
      budget.max = b.max;
      budget.step = 10000;
      budget.value = b.default;
      sync();
    };
    sync();
    applyBudget(modeSel.value);
    modeSel.addEventListener('change', () => { applyBudget(modeSel.value); compute(); });
    roleSel.addEventListener('change', compute);
    budget.addEventListener('input', sync);
    budget.addEventListener('change', compute);
    const btn = ROOT.querySelector('#opt-copy');
    if (btn) btn.addEventListener('click', copyBuild);
  }

  function compute() {
    const modeSel = ROOT.querySelector('#opt-mode');
    const roleSel = ROOT.querySelector('#opt-role');
    let budget = Number(ROOT.querySelector('#opt-budget').value);
    if (!budget || !isFinite(budget)) {
      const b = (DATA.budgets && DATA.budgets[modeSel.value]) || null;
      budget = b ? b.default : 350000;
    }
    const res = Core.build(DATA, modeSel.value, roleSel.value, budget);
    const out = ROOT.querySelector('.opt-result');
    if (!res) {
      out.innerHTML = '<div class="callout callout-warning"><h4>Aucune arme compatible</h4><p>Ce rôle n\'a pas d\'arme dans la base de référence pour ce mode.</p></div>';
      return;
    }
    const ratio = res.ratio;
    out.innerHTML =
      '<div class="opt-head">' +
        '<div>' +
          '<span class="opt-role">' + esc(res.role.icon) + ' ' + esc(res.role.name) + '</span>' +
          '<span class="opt-mode">' + esc(res.mode.label) + ' · plafond T' + res.cap + ' · ' + res.rounds + ' cartouches</span>' +
        '</div>' +
        '<div class="opt-total"><span class="v">' + fmt(res.total) + '</span><span class="k">Coût total du kit</span></div>' +
      '</div>' +
      '<div class="opt-meter"><div class="opt-meter-fill ' + (ratio > 1 ? 'over' : ratio > 0.95 ? 'warn' : 'ok') + '" style="width:' + Math.min(100, ratio * 100).toFixed(0) + '%"></div><span class="opt-meter-label">' + Math.round(ratio * 100) + ' % du budget</span></div>' +
      '<div class="opt-lines">' +
        res.lines.map(l =>
          '<div class="opt-line">' +
            '<span class="opt-line-k">' + esc(l.k) + '</span>' +
            '<span class="opt-line-n">' + esc(l.n) + (l.note ? '<em>' + esc(l.note) + '</em>' : '') + '</span>' +
            '<span class="opt-line-v">' + fmt(l.v) + '</span>' +
          '</div>').join('') +
      '</div>' +
      '<div class="callout callout-' + res.vclass + '"><h4>Verdict</h4><p>' + esc(res.verdict) + '</p></div>' +
      (res.warnings.length
        ? '<div class="callout callout-warning"><h4>Points de vigilance</h4><ul>' + res.warnings.map(w => '<li>' + esc(w) + '</li>').join('') + '</ul></div>'
        : '') +
      '<div class="callout callout-success"><h4>Conseil du rôle</h4><p>' + esc(res.role.tip) + '</p></div>';

    ROOT.querySelector('.opt-summary').textContent = res.summary;
  }

  function copyBuild() {
    const txt = ROOT.querySelector('.opt-summary').textContent;
    const btn = ROOT.querySelector('#opt-copy');
    const done = () => { btn.textContent = 'Copié ✓'; setTimeout(() => { btn.textContent = 'Copier le build'; }, 1800); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(done).catch(() => fallback());
    } else { fallback(); }
    function fallback() {
      const ta = document.createElement('textarea');
      ta.value = txt; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch (e) { btn.textContent = 'Copie impossible'; }
      document.body.removeChild(ta);
    }
  }
})();
