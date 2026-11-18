/* ══════════════════════════════════════════════════════════════════════
   ABI NEXUS — ballistics.js : simulateur de pénétration et de TTK

   Ce module complète la page « Munitions & Pénétration » d'un outil
   interactif : choisir une arme, une munition et une armure, et lire
   le verdict — la munition perce-t-elle la plaque ? combien de balles
   pour neutralityner ? le TTK en est-il de combien ?

   Les règles appliquées sont celles de la Saison 7 « Utopia » :
     · Pierce Level = plancher(Pénétration ÷ 10)
     · une munition de Pierce Level lower que la classe de l'armure
       ne perce PAS (la « loterie » de pénétration a été supprimée
       en S7 sur les armures T5 et T6 : plus de chance aléatoire)
     · les dégâts de chair ne sont affectés qu'à la zone touchée :
       le torse est protégé, la tête ne l'est pas
     · chaque tir retire de la durabilité à l'armure, ce qui peut
       ouvrir une brèche dans la plaque à plus longue portée

   Sources : js/data-ammo.json et js/data-armors.json (patch 1.0.0.142.19).
   ══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g,
        m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));

  const root = $('#ballistics');
  if (!root) return;

  const ammoData = $('#ballistics-ammo');
  const armorData = $('#ballistics-armors');
  const weaponData = $('#ballistics-weapons');
  if (!ammoData || !armorData || !weaponData) return;

  let AMMO = [], ARMORS = [], WEAPONS = [];

  /* Les armes notent leurs calibres « 5.45×39 PP (T3) » (avec la munition),
     les munitions « 5.45×39mm ». On normalise pour pouvoir apparier. */
  const normCal = s => String(s || '')
    .replace(/\s*\(.*?\)\s*$/, '')      // retire « (T3) »
    .replace(/mm$/, '')
    .replace(/\s+/g, '')
    .toLowerCase();

  /* La munition « 5.45×39 BP » correspond au calibre « 5.45×39 » */
  const caliberOfAmmoName = s => {
    const m = String(s || '').match(/^([\d.]+[×x][\d.]+)/);
    return m ? m[1] : '';
  };

  /* ── Chargement des données ──────────────────────────────────────── */
  Promise.all([
    fetch(ammoData.dataset.src).then(r => r.json()),
    fetch(armorData.dataset.src).then(r => r.json()),
    fetch(weaponData.dataset.src).then(r => r.json())
  ]).then(([a, b, w]) => {
    AMMO = a.ammo || [];
    ARMORS = b.armors || [];
    WEAPONS = w.weapons || [];
    build();
  }).catch(err => {
    console.error('[ABI NEXUS] ballistics.js', err);
    root.innerHTML = '<div class="callout callout-danger"><p>Données balistiques indisponibles.</p></div>';
  });

  /* ── Rendu ───────────────────────────────────────────────────────── */
  function build() {
    const calLabel = {};
    const byCal = {};
    AMMO.forEach(x => {
      const key = normCal(x.caliber);
      (byCal[key] = byCal[key] || []).push(x);
      calLabel[key] = x.caliber;
    });

    const caliberSel = $('#bal-caliber', root);
    const weaponSel  = $('#bal-weapon', root);
    const ammoSel    = $('#bal-ammo', root);
    const armorSel   = $('#bal-armor', root);
    const zoneSel    = $('#bal-zone', root);
    const out        = $('#bal-out', root);

    /* Une arme correspond a un calibre si l'une de ses munitions commence
       par le calibre de la munition (comparaison normalisee). */
    const weaponsFor = cal => WEAPONS.filter(x =>
      x.ammo && x.ammo.some(a => {
        const name = caliberOfAmmoName(a);
        return name && normCal(name) === normCal(cal);
      }));


    function fillAmmo(cal) {
      const list = byCal[cal] || [];
      ammoSel.innerHTML = list.map(a =>
        '<option value="' + esc(a.id) + '">' + esc(a.name) +
        ' — PL ' + a.pierceLevel + ' · pén. ' + a.penetration +
        ' · ' + a.damage + ' chair</option>').join('');
    }

    function fillWeapons(cal) {
      const list = weaponsFor(cal);
      weaponSel.innerHTML = list.map(w =>
        '<option value="' + esc(w.id) + '">' + esc(w.name) +
        ' — ' + w.rpm + ' rpm · ' + w.damage + ' dégâts</option>').join('');
    }

    function fillArmors() {
      armorSel.innerHTML = ARMORS.map(x =>
        '<option value="' + esc(x.id) + '">' + esc(x.name) +
        ' — T' + x.tier + ' · ' + esc(x.material || '') + '</option>').join('');
    }

    function syncCaliber() {
      const w = WEAPONS.find(x => x.id === weaponSel.value);
      let cal = '';
      if (w && w.ammo && w.ammo[0]) cal = normCal(caliberOfAmmoName(w.ammo[0]));
      if (!byCal[cal]) cal = Object.keys(byCal)[0] || '';
      caliberSel.value = cal;
      fillAmmo(cal);
      fillWeapons(cal);
      render();
    }

    function render() {
      const ammo = AMMO.find(x => x.id === ammoSel.value) || AMMO[0];
      const armor = ARMORS.find(x => x.id === armorSel.value) || ARMORS[0];
      const weapon = WEAPONS.find(x => x.id === weaponSel.value) || WEAPONS[0];
      const zone = zoneSel.value;
      if (!ammo || !armor || !weapon) return;

      const pl = Math.floor(ammo.penetration / 10);
      const protectedZone = zone === 'torse' &&
                            armor.zones && armor.zones.length > 0;

      /* Règle de pénétration communautaire (testée, cohérente sur tous les
         guides de Saison 7) :
           · Pierce Level SUPÉRIEUR à la classe de l'armure -> la balle
             traverse et inflige la totalité des dégâts chair ;
           · Pierce Level ÉGAL à la classe -> pénétration partielle,
             environ 80 % des dégâts chair ;
           · Pierce Level INFÉRIEUR -> la balle ricoche, environ 50 %
             des dégâts chair, et la plaque encaisse les dégâts d'armure.
         La durabilité joue indépendamment : insistent sur la même plaque,
         on finit par percer même avec une munition sous-tier. */
      let ratio = 1, verdict = 'Pénètre pleinement';
      if (protectedZone) {
        if (pl > armor.tier) {
          ratio = 1; verdict = 'Pénètre pleinement';
        } else if (pl === armor.tier) {
          ratio = 0.8; verdict = 'Pénétration partielle';
        } else {
          ratio = 0.5; verdict = 'Ne pénètre pas';
        }
      } else {
        verdict = 'Zone non protégée';
      }

      /* Dégâts effectifs : chair, puis contribution de l'armure. */
      let dmg = Math.round(ammo.damage * ratio);
      let note = '';
      if (!protectedZone) {
        note = 'Aucune plaque ne couvre cette zone : la full flesh damage s\'applique.';
      } else if (ratio === 1) {
        note = 'Pierce Level supérieur à la classe : la balle traverse la plaque.';
      } else if (ratio === 0.8) {
        note = 'Pierce Level égal à la classe : pénétration partielle, environ 80 % des dégâts chair.';
      } else {
        note = 'Pierce Level inférieur à la classe : la balle ricoche, environ 50 % des dégâts chair.';
      }

      /* L'armure encaisse aussi : la munition dégrade la plaque, ce qui
         finit par ouvrir une brèche même avec une munition sous-tier. */
      const plateHit = protectedZone;
      const perShotArmor = plateHit ? ammo.armorDamage : 0;
      const breachAfter = perShotArmor > 0 && armor.durability
        ? Math.ceil(armor.durability / perShotArmor)
        : null;

      /* PV de la zone — valeurs de terrain issues des fiches armure */
      const HP = { tete: 35, torse: 85, ventre: 60, dos: 85, bras: 40, jambes: 65 };
      const hp = HP[zone] || 85;
      const shots = Math.max(1, Math.ceil(hp / dmg));

      /* TTK : cadence de l'arme */
      const rpm = weapon.rpm || 600;
      const msBetween = 60000 / rpm;
      const ttk = ((shots - 1) * msBetween) / 1000;

      /* Tête : aucune armure ne couvre la tête dans ce modèle */
      const headDmg = ammo.damage;
      const headShots = Math.max(1, Math.ceil(35 / headDmg));

      const verdictClass = ratio === 1 ? 'success'
        : (ratio === 0.8 ? 'warning' : (protectedZone ? 'danger' : 'info'));

      out.innerHTML =
        '<div class="facts">' +
          fact('Munition', ammo.name) +
          fact('Pénétration', ammo.penetration + ' → PL ' + pl) +
          fact('Classe armure', 'T' + armor.tier + ' · ' + armor.name) +
          fact('Verdict', verdict) +
        '</div>' +
        '<div class="callout callout-' + verdictClass + '">' +
          '<p><strong>' + verdict + '.</strong> ' + esc(note) + '</p>' +
          '<p>Dégâts effectifs sur la zone : <strong>' + dmg + '</strong>' +
          ' · <strong>' + shots + '</strong> projectile' + (shots > 1 ? 's' : '') +
          ' pour neutraliser ' + esc(zone) + ' (' + hp + ' PV).</p>' +
          '<p>TTK théorique à la cadence de ' + esc(weapon.name) + ' (' + rpm + ' rpm) : ' +
          '<strong>' + ttk.toFixed(2) + ' s</strong>' +
          ' · <strong>' + headShots + '</strong> projectile' + (headShots > 1 ? 's' : '') +
          ' à la tête (' + headDmg + ' dégâts chair).</p>' +
          (breachAfter ? '<p>La plaque encaisse <strong>' + perShotArmor +
            '</strong> points de durabilité par tir : à force de frapper la ' +
            'même zone, elle s\'use et finit par céder — c\'est ce qui permet ' +
            'à une munition sous-tier de finir par percer.</p>' : '') +
        '</div>' +
        '<p class="small text-muted">Modèle simplifié : les points de vie par zone et ' +
        'la durability sont des estimations de terrain, pas des valeurs éditeur. ' +
        'Le TTK réel dépend de la distance, de la précision et des attributs de l\'opposant.</p>';
    }

    function fact(k, v) {
      return '<div class="fact"><span class="fact-label">' + esc(k) +
             '</span><span class="fact-value">' + esc(v) + '</span></div>';
    }

    /* Options initiales */
    fillArmors();
    const firstWeapon = WEAPONS[0];
    let firstCal = '';
    if (firstWeapon && firstWeapon.ammo && firstWeapon.ammo[0]) {
      firstCal = normCal(caliberOfAmmoName(firstWeapon.ammo[0]));
    }
    if (!byCal[firstCal]) firstCal = Object.keys(byCal)[0] || '';
    caliberSel.innerHTML = Object.keys(byCal).map(c =>
      '<option value="' + esc(c) + '">' + esc(calLabel[c] || c) + '</option>').join('');
    caliberSel.value = firstCal;
    fillAmmo(firstCal);
    fillWeapons(firstCal);
    weaponSel.value = firstWeapon ? firstWeapon.id : '';
    armorSel.value = ARMORS[0] ? ARMORS[0].id : '';

    caliberSel.addEventListener('change', () => {
      fillAmmo(caliberSel.value);
      fillWeapons(caliberSel.value);
      render();
    });
    weaponSel.addEventListener('change', syncCaliber);
    ammoSel.addEventListener('change', render);
    armorSel.addEventListener('change', render);
    zoneSel.addEventListener('change', render);

    render();
  }
})();
