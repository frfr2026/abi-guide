/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — map-explorer.js (S15)
   Explorateur de cartes : filtres (difficulté, infection, mode),
   parcours d'apprentissage et points d'intérêt.
   Données : js/data-maps.json + repères communautaires datés.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const ROOT = document.querySelector('.map-explorer');
  if (!ROOT) return;

  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, m =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  /* Repères communautaires : consensus de plusieurs guides et retours
     de forum, recoupés en novembre 2026. Ce ne sont PAS des données
     officielles de l'éditeur. */
  const COMMUNITY = {
    farm: {
      level: 1,
      role: "Carte d'apprentissage",
      why: "Champs ouverts et zones lisibles : on repère ses repères avant de connaître les autres cartes. 14 extractions, la plus large de la rotation.",
      routes: [
        ['Entrée sud', 'Zone de loot de départ, sans risque' ],
        ['Granges nord', 'Valeur moyenne, bonne couverture'],
        ['Fossé Est', 'Fuite rapide en cas de perte']
      ],
      warns: ['Infestée en S7 : les zones Heavy sont hostile même au niveau 30.']
    },
    valley: {
      level: 2,
      role: 'Longue distance',
      why: "Portée longue et lignes de vue dégagées : la carte où l'on apprend à poser ses distances. 12 extractions.",
      routes: [
        ['Colline nord', 'Angle long, contrôle du flux'],
        ['Poste de garde', 'Zone de loot secondaire'],
        ['Lit de rivière', 'Traversée rapide mais exposée']
      ],
      warns: ['Zone Standards infectée : les IA modifiées tournent dans les points de loot.']
    },
    airport: {
      level: 3,
      role: 'Rendement élevé',
      why: "Taux de drop les plus élevés du jeu selon les guides communautaires, mais 13 extractions seulement : chaque sortie compte.",
      routes: [
        ['Terminal', 'Valeur maximale, très exposée'],
        ['Piste', 'Traversée rapide, couverture rare'],
        ['Hangar Est', 'Loot secondaire moins contesté']
      ],
      warns: ['Heavy Infected Zone en S7 : le rapport risque / gain change complètement.', 'Zone Zombie Endless : mode PvE à tickets, pas un raid classique.']
    },
    northridge: {
      level: 3,
      role: 'Survie difficile',
      why: "Relief, neige et visibilité réduite : 10 extractions. On y va une fois l'arsenal et le budget maîtrisés.",
      routes: [
        ['Refuge', 'Point de regroupement chaud'],
        ['Crête est', 'Vue longue, vent' ],
        ['Campement', 'Loot moyen, risque de mule']
      ],
      warns: ['La neige réduit la portée de tir : les DMR y perdent leur avantage.']
    },
    armory: {
      level: 4,
      role: 'Haut risque',
      why: "Meilleur loot du jeu, mais aussi le taux de mort le plus élevé. 9 extractions seulement.",
      routes: [
        ['Salle principale', 'Cœur du loot, zone mortelle'],
        ['Couloir sud', 'Raccourci vers une sortie'],
        ['Quai', 'Valeur correcte, plus de sorties']
      ],
      warns: ['Arme de tier S conseillée : le ratio valeur / mort ne tient pas avec un kit léger.']
    },
    tvstation: {
      level: 4,
      role: 'Entraînement PvP',
      why: "Bâtiments clos, 11 extractions. Excellent pour apprendre le combat rapproché une fois l'extraction maîtrisée.",
      routes: [
        ['Étage bas', 'Angle mort, CQB'],
        ['Plateau télé', 'Vue longue sur le plateau'],
        ['Sortie service', 'Peu utilisée, donc disputée']
      ],
      warns: ['Ce n’est pas une carte de départ : les duels s’y tranchent en moins de 30 mètres.', ]
    },
    nomansland: {
      level: 5,
      role: 'PvE à tickets',
      why: "8 extractions, mode PvE par tickets : on paie une entrée pour tuer des zombies et accumuler de la valeur.",
      routes: [
        ['Campement', 'Départ des vagues'],
        ['Fossé', 'Loot de zombies'],
        ['Point d’extraction', 'Départ rapide']
      ],
      warns: ['Le but n’est pas de looter de la valeur : c’est le score de vagues qui compte.']
    }
  };

  let MAPS = [];

  Promise.all([
    fetch('../js/data-maps.json').then(r => r.json())
  ]).then(([m]) => {
    MAPS = m.maps || [];
    buildFilters();
    render();
  }).catch(err => {
    console.error('[ABI NEXUS] map-explorer', err);
    ROOT.innerHTML = '<div class="callout callout-danger"><h4>Données indisponibles</h4><p>Impossible de charger les fiches de carte.</p></div>';
  });

  let filters = { diff: '', infected: '', mode: '', level: '' };

  function buildFilters() {
    const counter = ROOT.querySelector('#mx-count');
    if (counter) counter.setAttribute('aria-live', 'polite');
    const diffs = Array.from(new Set(MAPS.map(m => m.difficulty)));
    const modes = Array.from(new Set(MAPS.flatMap(m => m.modes || [])));

    const d = ROOT.querySelector('#mx-diff');
    const inf = ROOT.querySelector('#mx-infected');
    const mod = ROOT.querySelector('#mx-mode');
    const lvl = ROOT.querySelector('#mx-level');

    d.innerHTML = '<option value="">Toutes difficultés</option>' + diffs.map(x => '<option value="' + esc(x) + '">' + esc(x) + '</option>').join('');
    inf.innerHTML = '<option value="">Toutes</option><option value="oui">Infectées</option><option value="non">Non infectées</option>';
    mod.innerHTML = '<option value="">Tous modes</option>' + modes.map(x => '<option value="' + esc(x) + '">' + esc(x) + '</option>').join('');
    lvl.innerHTML = '<option value="">Tous niveaux</option>' +
      '<option value="1">Niveau 1 — Apprentissage</option>' +
      '<option value="2">Niveau 2 — Consolidation</option>' +
      '<option value="3">Niveau 3 — Spécialisation</option>' +
      '<option value="4">Niveau 4 — Confirmé</option>' +
      '<option value="5">Niveau 5 — Expert</option>';

    d.addEventListener('change', () => { filters.diff = d.value; render(); });
    inf.addEventListener('change', () => { filters.infected = inf.value; render(); });
    mod.addEventListener('change', () => { filters.mode = mod.value; render(); });
    lvl.addEventListener('change', () => { filters.level = lvl.value; render(); });

    const reset = ROOT.querySelector('#mx-reset');
    if (reset) reset.addEventListener('click', () => {
      d.value = ''; inf.value = ''; mod.value = ''; lvl.value = '';
      filters = { diff: '', infected: '', mode: '', level: '' };
      render();
    });
  }

  function render() {
    const list = ROOT.querySelector('.mx-list');
    const filtered = MAPS.filter(m => {
      if (filters.diff && m.difficulty !== filters.diff) return false;
      if (filters.infected === 'oui' && !m.infected) return false;
      if (filters.infected === 'non' && m.infected) return false;
      if (filters.mode && (m.modes || []).indexOf(filters.mode) === -1) return false;
      const cm = COMMUNITY[m.id];
      if (filters.level && (!cm || String(cm.level) !== filters.level)) return false;
      return true;
    }).sort((x, y) => {
      const lx = (COMMUNITY[x.id] ? COMMUNITY[x.id].level : 9);
      const ly = (COMMUNITY[y.id] ? COMMUNITY[y.id].level : 9);
      return lx - ly || y.extractions - x.extractions;
    });

    const count = ROOT.querySelector('#mx-count');
    if (count) count.textContent = filtered.length + ' carte' + (filtered.length > 1 ? 's' : '') + ' affichée' + (filtered.length > 1 ? 's' : '');

    if (!filtered.length) {
      list.innerHTML = '<div class="callout"><p>Aucune carte ne correspond à ces filtres.</p></div>';
      return;
    }

    list.innerHTML = filtered.map(m => {
      const cm = COMMUNITY[m.id] || { level: '—', role: '—', why: m.description, routes: [], warns: [] };
      // Variante dediee : chaque carte garde un visuel distinct de celui
      // de sa page detail, afin qu'aucune image ne serve a deux pages.
      const EXPLORER_IMG = {
        farm: '../img/maps/var-farm-cine.jpg',
        valley: '../img/maps/var-valley-cine.jpg',
        airport: '../img/maps/var-airport-cine.jpg',
        northridge: '../img/maps/var-northridge-cine.jpg',
        armory: '../img/maps/var-armory-cine.jpg',
        tvstation: '../img/maps/var-tvstation-cine.jpg'
      };
      const img = EXPLORER_IMG[m.id] || m.image || '../img/maps/map-farm.jpg';
      return '<article class="mx-card">' +
        '<div class="mx-media"><img src="' + esc(img) + '" alt="Vue de la carte ' + esc(m.name) + '" loading="lazy" onerror="this.onerror=null;this.src=\'../img/hero/hero-cartes.jpg\'"></div>' +
        '<h4>' + esc(m.name) + '</h4>' +
        '<div class="mx-meta">' + esc(m.difficulty) + ' · ' + m.extractions + ' extractions · ' + (m.infected ? 'infectée' : 'non infectée') + '</div>' +
        '<p>' + esc(cm.why) + '</p>' +
        '<div class="mx-tags">' +
          (m.modes || []).map(x => '<span class="chip">' + esc(x) + '</span>').join('') +
          '<span class="chip chip-gold">Apprentissage ' + esc(cm.level) + '</span>' +
        '</div>' +
        (cm.routes && cm.routes.length
          ? '<div style="margin-top:.6rem">' +
            cm.routes.map(r => '<div class="mx-spot"><span class="mx-ico">▸</span><span><b>' + esc(r[0]) + '</b> — ' + esc(r[1]) + '</span></div>').join('') +
            '</div>'
          : '') +
        (cm.warns && cm.warns.length
          ? '<div class="callout callout-warning" style="margin:.6rem 0 0"><ul>' + cm.warns.map(w => '<li>' + esc(w) + '</li>').join('') + '</ul></div>'
          : '') +
        '<div style="margin-top:.6rem"><a class="btn btn-outline btn-sm" href="' + esc(m.page || ('map-' + m.id + '.html')) + '">Fiche ' + esc(m.name) + '</a></div>' +
      '</article>';
    }).join('');
  }

  window.ABIMapExplorer = { render };
})();
