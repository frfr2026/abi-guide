/* ABI NEXUS — Catalogue complet des 77 armes documentées
 *
 * Remplit le tableau de la section "8 bis" de meta-tier-list-globale.html a
 * partir de js/data-weapons-wiki.json. Le fichier est la seule source de
 * verite : aucune valeur n'est ecrite en dur ici.
 *
 * Source : wiki ABI de reference (Fandom). Donnee documentee, non publiee par
 * l'editeur. Chaque cellule porte le niveau de source dans son titre.
 */
(function () {
  'use strict';

  const BODY = document.querySelector('#catalogue-77-body');
  const TABLE = document.querySelector('#catalogue-77-table');
  if (!BODY) return;

  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g,
    m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  fetch('../js/data-weapons-wiki.json')
    .then(r => r.json())
    .then(data => {
      const list = (data && data.weapons) || [];
      if (!list.length) throw new Error('catalogue vide');

      const CAT_ORDER = {
        "Fusil d'assaut": 0, 'DMR': 1, 'Sniper': 2, 'Carabine': 3,
        'SMG': 4, 'Shotgun': 5, 'LMG': 6, 'Pistolet': 7
      };
      const sorted = list.slice().sort((a, b) =>
        (CAT_ORDER[a.category] ?? 99) - (CAT_ORDER[b.category] ?? 99) ||
        a.name.localeCompare(b.name, 'fr'));

      const rows = sorted.map(w => {
        const t = w.stats || {};
        const cell = (v, tip) => `<td${tip ? ` title="${esc(tip)}"` : ''}>${esc(v)}</td>`;
        return '<tr>' +
          `<th scope="row" title="${esc(w.nomComplet || w.name)}">${esc(w.name)}</th>` +
          cell(w.category) +
          cell(w.caliber) +
          cell((w.modes || []).join(' · ')) +
          cell(t.reculVertical, 'Recul vertical : plus la valeur est haute, plus le tir monte.') +
          cell(t.reculHorizontal, 'Recul horizontal : plus la valeur est haute, plus la balle part sur le cote.') +
          cell(t.ergonomie) +
          cell(t.stabilite) +
          cell(t.precision) +
          cell(t.stabiliteHipfire, 'Stabilite a l\'hipfire : la capacite a tenir le tir sans viser.') +
          cell(t.portee, 'Distance a laquelle l\'arme reste efficace.') +
          cell(t.vitesseProjectile, 'Vitesse du projectile en metres par seconde.') +
          cell(t.cadence, 'Cadence de tir en tours par minute.') +
          cell(w.poids + ' kg') +
          '</tr>';
      }).join('');

      BODY.innerHTML = rows;

      if (TABLE) {
        const cap = TABLE.querySelector('caption');
        if (cap) cap.innerHTML =
          `Les ${sorted.length} armes document&eacute;es &mdash; ` +
          `<span class="src-tag src-documente">Document&eacute;</span>`;
      }
    })
    .catch(err => {
      console.error('[ABI NEXUS] weapon-catalogue', err);
      BODY.innerHTML = '<tr><td colspan="14" class="text-muted">' +
        'Catalogue indisponible pour le moment. R&eacute;essayez plus tard.</td></tr>';
    });
})();
