/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — search.js : recherche globale du site (S15)
   Indexe les pages statiques et les données JSON (armes, cartes,
   armures, objets, munitions). Raccourcis : "/" ou Ctrl+K.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

  const esc = s => String(s == null ? '' : s)
    .replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));

  const RECENT_KEY = 'abi-nexus-recent-searches';
  const RECENT_MAX = 6;

  /* ── Index des pages statiques ─────────────────────────────── */
  const PAGES = [
    ['/index.html', 'Accueil ABI NEXUS', 'Saison 7 Utopia, armes, tactiques, outils interactifs, économie'],
    ['guide-debutant.html', 'Guide du débutant', 'Premiers pas, niveaux, zones, extraction'],
    ['guide-avance.html', 'Guide avancé', 'Mécaniques fines, PvP, optimisation'],
    ['reglages-sensibilite.html', 'Réglages & sensibilité', 'Visibilité, FPS, Focal Point, sensibilité par grossissement'],
    ['guide-progression.html', 'Progression', 'XP, niveaux, déblocages, paliers'],
    ['guide-extraction.html', 'Extraction', 'Sorties, timers, règles de survie'],
    ['guide-economie.html', 'Économie Koen', 'Prix, marché, Contacts, arbitrages'],
    ['guide-craft.html', 'Craft & Workbench', 'Fabrication, recettes, matériaux'],
    ['guide-traders.html', 'Marchands', 'Contacts, trocs, inventaire marchand'],
    ['armes-fusils-assaut.html', 'Fusils d’assaut', 'M4A1, AK-15SC, A545, AN94, U191'],
    ['armes-carbine.html', 'Carabines', 'AK12, AEK-971, SKS, F2000, VSS'],
    ['armes-dmr.html', 'DMR', 'M110, MK14, SVD, RPK-16'],
    ['armes-sniper.html', 'Snipers', 'M24, Mosin, M700, Banshee'],
    ['armes-smg.html', 'SMG', 'MPX, P90, Vector .45, PCC9'],
    ['armes-lmg.html', 'LMG', 'RPK-16, MG3, M249, KORD'],
    ['armes-shotgun.html', 'Shotguns', 'USAS-12, MP-133, M870, KS-12'],
    ['armes-pistolets.html', 'Pistolets', 'G17, Desert Eagle, Vector .45, M9'],
    ['armes-tier-list.html', 'Tier List des armes', 'Classement complet S7, patch 1.0.0.142.19'],
    ['armes-builds.html', 'Meilleurs builds', 'Configurations d’armes testées et validées'],
    ['armes-nouveautes-s7.html', 'Nouveautés armes S7', 'A545, AK-15SC, attachements S7'],
    ['armes-attachements.html', 'Attachements', 'Optiques, canons, poignées, chargeurs'],
    ['armes-attachements-s7.html', 'Attachements S7', 'Nouveaux optiques, grips et fore-ends'],
    ['equipement-armures.html', 'Armures T1–T6', 'Gilets, matériaux, zones, durabilité'],
    ['equipement-casques.html', 'Casques', 'Classes, visières, protection auditive'],
    ['equipement-headsets.html', 'Headsets', 'Audio, portée d’écoute, situations de mort'],
    ['equipement-rigs.html', 'Rigs', 'Harnais, emplacements, poids'],
    ['equipement-sacs.html', 'Sacs à dos', 'Capacité, emplacements 2x2 / 3x3'],
    ['equipement-tier-list.html', 'Tier List équipement', 'Classement armures et casques'],
    ['items-valeur.html', 'Loot rouge', 'Elysium, Northern Stars, Lunar Soil Sample'],
    ['items-munitions.html', 'Munitions', 'Pénétration, classe d’armure, dégâts de chair'],
    ['items-medical.html', 'Objets médicaux', 'Bandages, chirurgies, stimulants, antidotes'],
    ['items-cles.html', 'Clés', 'Keycards, clés de pièces, clés de boss'],
    ['items-collection-room.html', 'Collection Room', 'Limites, Red Drops, stockage'],
    ['items-craft-workbench.html', 'Craft & Workbench', 'Formules, matériaux, temps de recherche'],
    ['items-koen-economy.html', 'Koen & économie', 'Sources de revenus, arbitrages marchands'],
    ['map-farm.html', 'Farm', 'Heavy Infected Zone, 8 extractions, 11 zones'],
    ['map-valley.html', 'Valley', 'Infected Zone, portée longue, 8 extractions, 11 zones'],
    ['map-northridge.html', 'Northridge', 'Altitude, neige, 11 extractions, 16 zones'],
    ['map-armory.html', 'Armory', 'Top loot, 3 extractions, 7 zones'],
    ['map-tv-station.html', 'TV Station', 'Bâtiments clos, 3 extractions, 6 zones'],
    ['map-airport.html', 'Airport', '4 extractions, 9 zones, 9 clés'],
    ['map-no-mans-land.html', 'No Man’s Land', 'Mode PvE à tickets, rotation Farm / Valley / TV Station'],
    ['saison7-utopia.html', 'Saison 7 : Utopia', 'Hub de la saison, nouveautés'],
    ['saison8-attente.html', 'Saison 8 : ce qui arrive', 'Calendrier des saisons, fin de l’Utopia, checklist'],
    ['saison7-nouveautes.html', 'Nouveautés S7', 'Résumé des ajouts de la saison'],
    ['saison7-balance-changes.html', 'Balance changes S7', 'Ricochet supprimé, portées, classes'],
    ['saison7-battle-pass.html', 'Battle Pass S7', 'Pistes, vignettes, coupons'],
    ['saison7-zombie-infected-zone.html', 'Infected Zone', 'Mutants, boss, zombies'],
    ['saison7-zombie-endless.html', 'Zombie Endless', 'Merit, classement, 3 000 000 Koen'],
    ['saison7-zombie-research.html', 'Zombie Research', 'Échantillons, progression, récompenses'],
    ['meta-loadout-optimizer.html', 'Loadout Optimizer', 'Calculateur de kit selon le budget'],
    ['meta-builds-roles.html', 'Builds par rôle', 'Polyvalent, sniper, CQB, PMG'],
    ['meta-stratégies-s7.html', 'Stratégies S7', 'Routes, gestion du son, gestion du risque'],
    ['meta-tier-list-globale.html', 'Tier List globale', 'Toutes catégories, consensus communautaire'],
    ['univers-lore.html', 'Histoire de Kamona', 'Guerre Nord-Sud, Utopia, mystères'],
    ['univers-factions.html', 'Factions de Kamona', 'Tevilla, Colom, PMC, personnages'],
    ['univers-dark-zone.html', 'La Dark Zone', 'Tac Ops, Covert Ops, règles non écrites'],
    ['events-calendrier.html', 'Calendrier des événements', 'Toutes les échéances S7'],
    ['events-supplies-drops.html', 'Supply Drops 2.0', 'Caisse à 5 niveaux, Smelter, terminaux'],
    ['events-warlord-tournament.html', 'Warlord Tournament III', 'Rangs, scoring, fichier chiffré'],
    ['communaute-ressources.html', 'Ressources communautaires', 'Discord, Reddit, bases de données, GitHub'],
    ['communaute-streamers.html', 'Streamers & créateurs', 'Twitch, événements sponsorisés, drops'],
    ['communaute-patch-notes.html', 'Patch notes', 'Notes officielles, live updates, sécurité'],
    ['cosmetiques-dog-tags.html', 'Dog Tags', 'Plaques d’identité personnalisées'],
    ['cosmetiques-skins-armes.html', 'Skins d’armes', 'Camo, ornaments,paintjobs'],
    ['cosmetiques-skins-perso.html', 'Skins de personnage', 'Tenues, visages, emotes']
  ];

  /* ── Chargement des données JSON ───────────────────────────── */
  /* Deux préfixes distincts sont nécessaires :
     - DATA_BASE pointe vers le dossier /js/  (racine du site)
     - PAGE_BASE pointe vers le dossier /pages/ (les pages du guide)
     Depuis une page du guide, les deux racines sont au même niveau mais
     dans des dossiers différents : confondre les deux produisait des
     liens de résultats de recherche cassés. */
  const IN_PAGES = location.pathname.indexOf('/pages/') !== -1;
  const DATA_BASE = IN_PAGES ? '../' : '';
  const PAGE_BASE = IN_PAGES ? '' : 'pages/';
  const ROOT_BASE = IN_PAGES ? '../' : '';

  const DATA_SOURCES = [
    { file: 'data-weapons.json', key: 'weapons', group: 'Armes', render: w => ({
      title: w.name,
      sub: `${w.category} · ${w.caliber} · tier ${w.tier} · ${Math.round((w.price || 0) / 1000).toLocaleString('fr-FR')} K${w.isNew ? ' · nouveau S7' : ''}`,
      href: PAGE_BASE + 'armes-tier-list.html'
    })},
    { file: 'data-weapons-wiki.json', key: 'weapons', group: 'Armes (catalogue)', render: w => ({
      title: w.name,
      sub: `${w.category} · ${w.caliber} · cadence ${w.stats && w.stats.cadence} · recul V ${w.stats && w.stats.reculVertical} · documenté (wiki)`,
      href: PAGE_BASE + 'meta-tier-list-globale.html#catalogue-77'
    })},
    { file: 'data-maps.json', key: 'maps', group: 'Cartes', render: m => ({
      title: m.name,
      sub: `${m.difficulty} · ${m.extractions} extractions${m.infected ? ' · infectée' : ''}`,
      href: PAGE_BASE + 'map-' + m.id + '.html'
    })},
    { file: 'data-maps.json', key: 'modes', group: 'Modes', render: m => ({
      title: m.name,
      sub: `${m.subtitle} · ${m.rotation.join(', ')} · ${m.entry}`,
      href: PAGE_BASE + 'map-no-mans-land.html'
    })},
    { file: 'data-armors.json', key: 'armors', group: 'Équipement', render: a => ({
      title: a.name,
      sub: `T${a.tier} · ${a.material} · ${a.zones.join(', ')} · ${a.durability} durabilité`,
      href: PAGE_BASE + 'equipement-armures.html'
    })},
    { file: 'data-items.json', key: 'items', group: 'Objets', render: i => ({
      title: i.name,
      sub: `${i.category} · ${Math.round((i.price || 0) / 1000).toLocaleString('fr-FR')} K${i.isNew ? ' · nouveau S7' : ''}`,
      href: PAGE_BASE + 'items-valeur.html'
    })},
    { file: 'data-ammo.json', key: 'ammo', group: 'Munitions', render: a => ({
      title: a.name,
      sub: `${a.caliber} · classe T${a.tier} · pénétration ${a.penetration} · ${a.damage} dégâts de chair`,
      href: PAGE_BASE + 'items-munitions.html'
    })}
  ];

  let INDEX = [];
  let READY = false;

  function norm(s) {
    return String(s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }

  function buildIndex() {
    INDEX = [];
    PAGES.forEach(p => INDEX.push({
      group: 'Pages', title: p[1], sub: p[2],
      href: p[0].charAt(0) === '/' ? ROOT_BASE + p[0].slice(1) : PAGE_BASE + p[0],
      hay: norm(p[1] + ' ' + p[2] + ' ' + p[0].replace('.html', '').replace(/-/g, ' '))
    }));
    Promise.all(DATA_SOURCES.map(src =>
      fetch(DATA_BASE + 'js/' + src.file)
        .then(r => r.ok ? r.json() : null)
        .then(d => d && d[src.key] ? d[src.key] : [])
        .catch(() => [])
    )).then(lists => {
      lists.forEach((list, i) => {
        const src = DATA_SOURCES[i];
        list.forEach(item => {
          const r = src.render(item);
          INDEX.push({
            group: src.group, title: r.title, sub: r.sub, href: r.href,
            hay: norm(r.title + ' ' + r.sub + ' ' + src.group)
          });
        });
      });
      READY = true;
    });
  }

  /* ── Historique ────────────────────────────────────────────── */
  function getRecent() {
    try { return JSON.parse(localStorage.getItem(RECENT_KEY) || '[]'); }
    catch (e) { return []; }
  }
  function pushRecent(q) {
    try {
      const list = getRecent().filter(x => x !== q);
      list.unshift(q);
      localStorage.setItem(RECENT_KEY, JSON.stringify(list.slice(0, RECENT_MAX)));
    } catch (e) { /* stockage indisponible */ }
  }

  /* ── Interface ─────────────────────────────────────────────── */
  function buildUI() {
    const actions = $('.nav-actions');
    if (!actions || $('.srch')) return;

    const wrap = document.createElement('div');
    wrap.className = 'srch';
    wrap.innerHTML =
      '<input class="srch-input" type="search" placeholder="Rechercher…" aria-label="Recherche globale" autocomplete="off" spellcheck="false">' +
      '<svg class="srch-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>' +
      '<span class="srch-kbd">/</span>' +
      '<div class="srch-panel" role="region" aria-label="Résultats de recherche" aria-live="polite"></div>';

    const btn = $('.nav-icon-btn[data-theme-toggle]', actions);
    actions.insertBefore(wrap, btn || actions.firstChild);

    const input = $('.srch-input', wrap);
    const panel = $('.srch-panel', wrap);
    let sel = -1;
    let items = [];

    function close() { panel.classList.remove('open'); sel = -1; }

    function render(list, emptyMsg) {
      if (!list.length) {
        panel.innerHTML = '<div class="srch-empty">' + esc(emptyMsg || 'Aucun résultat.') + '</div>';
        items = [];
        return;
      }
      items = list;
      const groups = [];
      list.forEach(it => {
        let g = groups.find(x => x.name === it.group);
        if (!g) { g = { name: it.group, rows: [] }; groups.push(g); }
        g.rows.push(it);
      });
      panel.innerHTML = groups.map(g =>
        '<div class="srch-group">' + esc(g.name) + '</div>' +
        g.rows.map((it, i) =>
          '<a class="srch-item" href="' + esc(it.href) + '">' +
          '<span>' + highlight(it.title, lastQuery) + '</span>' +
          (it.sub ? '<small>' + esc(it.sub) + '</small>' : '') +
          '</a>'
        ).join('')
      ).join('');
      sel = -1;
    }

    function highlight(text, q) {
      if (!q) return esc(text);
      const i = norm(text).indexOf(norm(q));
      if (i < 0) return esc(text);
      return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length));
    }

    function search(q) {
      lastQuery = q;
      if (!q || q.length < 2) {
        const recent = getRecent();
        if (recent.length) {
          render(recent.map(r => ({ group: 'Recherches récentes', title: r, sub: '', href: '#', recent: true })),
            'Tapez au moins 2 caractères.');
        } else {
          panel.innerHTML = '<div class="srch-empty">Tapez au moins 2 caractères.<br><small>Armes, cartes, armures, objets, munitions, pages.</small></div>';
          items = [];
        }
        return;
      }
      const nq = norm(q);
      const hits = INDEX
        .filter(it => it.hay.indexOf(nq) !== -1)
        .sort((a, b) => {
          const ai = norm(a.title).indexOf(nq);
          const bi = norm(b.title).indexOf(nq);
          if (ai !== bi) return (ai < 0 ? 99 : ai) - (bi < 0 ? 99 : bi);
          return a.title.length - b.title.length;
        })
        .slice(0, 40);
      render(hits, 'Aucun résultat pour « ' + q + ' ».');
    }

    let lastQuery = '';

    input.addEventListener('focus', () => { search(input.value.trim()); panel.classList.add('open'); });
    input.addEventListener('input', () => { search(input.value.trim()); panel.classList.add('open'); });
    input.addEventListener('keydown', e => {
      if (e.key === 'Escape') { close(); input.blur(); return; }
      if (e.key === 'Enter') {
        const cur = items.filter(i => !i.recent)[sel];
        if (cur) { pushRecent(input.value.trim()); window.location.href = cur.href; }
        else if (items[sel] && items[sel].recent) { input.value = items[sel].title; search(items[sel].title); }
        return;
      }
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        if (!items.length) return;
        e.preventDefault();
        sel += (e.key === 'ArrowDown' ? 1 : -1);
        if (sel < 0) sel = items.length - 1;
        if (sel >= items.length) sel = 0;
        $$('.srch-item', panel).forEach((el, i) => el.classList.toggle('sel', i === sel));
        const el = $$('.srch-item', panel)[sel];
        if (el && el.scrollIntoView) el.scrollIntoView({ block: 'nearest' });
      }
    });

    panel.addEventListener('click', e => {
      const a = e.target.closest('.srch-item');
      if (!a) return;
      if (a.getAttribute('href') === '#') {
        input.value = a.textContent.trim();
        search(input.value.trim());
        e.preventDefault();
      } else {
        pushRecent(input.value.trim());
      }
    });

    document.addEventListener('click', e => {
      if (!wrap.contains(e.target)) close();
    });

    document.addEventListener('keydown', e => {
      const tag = (e.target.tagName || '').toLowerCase();
      const typing = tag === 'input' || tag === 'textarea' || e.target.isContentEditable;
      if ((e.key === '/' && !typing) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k')) {
        e.preventDefault();
        input.focus();
        input.select();
      }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    buildUI();
    buildIndex();
  });
})();
