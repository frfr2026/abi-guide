/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — main.js : logique globale du site
   Thème, animations au scroll, compteurs, progression, audio,
   sommaire, retour en haut, recherche de base.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

  /* ── 1. Thème Dark / Light (persisté) ───────────────────── */
  const THEME_KEY = 'abi-nexus-theme';
  function initTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved) document.documentElement.setAttribute('data-theme', saved);
    $$('[data-theme-toggle]').forEach(btn => {
      btn.addEventListener('click', () => {
        const cur = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
        const next = cur === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem(THEME_KEY, next);
      });
    });
  }

  /* ── 2. Barre de progression de lecture ─────────────────── */
  function initProgressBar() {
    const bar = $('.progress-bar');
    if (!bar) return;
    const onScroll = () => {
      const h = document.documentElement;
      const max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── 3. Animations au scroll (Intersection Observer) ────── */
  function initReveal() {
    const els = $$('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    if (!('IntersectionObserver' in window)) {
      els.forEach(el => el.classList.add('visible'));
      return;
    }
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(el => io.observe(el));
  }

  /* ── 4. Compteurs animés ────────────────────────────────── */
  function animateCount(el) {
    const target = parseInt(el.dataset.count, 10) || 0;
    const dur = 1600, start = performance.now();
    const step = now => {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('fr-FR');
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }
  function initCounters() {
    const els = $$('[data-count]');
    if (!('IntersectionObserver' in window)) { els.forEach(animateCount); return; }
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { animateCount(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.4 });
    els.forEach(el => io.observe(el));
  }

  /* ── 5. Barres de stats animées ─────────────────────────── */
  function initStatBars() {
    const bars = $$('.stat-bar-fill[data-value]');
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.width = e.target.dataset.value + '%';
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.3 });
    bars.forEach(b => io.observe(b));
  }

  /* ── 6. Onglets ─────────────────────────────────────────── */
  function initTabs() {
    $$('.tabs').forEach(tabs => {
      const btns = $$('.tab-btn', tabs);
      const panels = $$('.tab-panel', tabs.parentElement);
      btns.forEach(btn => {
        btn.addEventListener('click', () => {
          btns.forEach(b => b.classList.remove('active'));
          panels.forEach(p => p.classList.remove('active'));
          btn.classList.add('active');
          const panel = $('#' + btn.dataset.tab, tabs.parentElement);
          if (panel) panel.classList.add('active');
        });
      });
    });
  }

  /* ── 7. Sommaire sticky (scrollspy) ─────────────────────── */
  function initToc() {
    const tocLinks = $$('.toc a');
    if (!tocLinks.length) return;
    const sections = tocLinks
      .map(a => $(a.getAttribute('href')))
      .filter(Boolean);
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          tocLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    sections.forEach(s => io.observe(s));
  }

  /* ── 8. Retour en haut ──────────────────────────────────── */
  function initBackToTop() {
    const btn = $('.back-to-top');
    if (!btn) return;
    document.addEventListener('scroll', () => {
      btn.classList.toggle('visible', window.scrollY > 600);
    }, { passive: true });
    btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ── 9. Audio player (ambiances MP3 par page) ───────────── */
  function initAudioPlayer() {
    const player = $('.audio-player');
    if (!player) return;
    let audio = $('audio', player);
    if (!audio) {
      audio = document.createElement('audio');
      audio.hidden = true;
      player.appendChild(audio);
    }
    const track = player.dataset.track || '';
    const btn = $('button', player);
    const vol = $('input[type="range"]', player);
    const label = $('.audio-label', player);
    if (track) { audio.src = track; audio.loop = true; }
    audio.volume = 0.5;
    const setIcon = () => {
      btn.innerHTML = audio.paused
        ? '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
    };
    btn.addEventListener('click', () => {
      if (!track) return;
      audio.paused ? audio.play().catch(() => {}) : audio.pause();
      setIcon();
    });
    audio.addEventListener('play', setIcon);
    audio.addEventListener('pause', setIcon);
    if (vol) vol.addEventListener('input', () => { audio.volume = parseFloat(vol.value); });
    if (label && player.dataset.label) label.textContent = player.dataset.label;
    setIcon();
  }

  /* ── 9 bis. Lecteur de narration (voix off, non bouclé) ──── */
  function initNarrationPlayer() {
    const player = $('.audio-narration');
    if (!player) return;
    let audio = $('audio', player);
    if (!audio) {
      audio = document.createElement('audio');
      audio.hidden = true;
      player.appendChild(audio);
    }
    const track = player.dataset.track || '';
    const btn = $('button', player);
    const label = $('.audio-label', player);
    const bar = $('.audio-bar-fill', player);
    if (track) { audio.src = track; audio.preload = 'none'; }
    audio.volume = 0.9;

    const setIcon = () => {
      if (audio.ended) {
        btn.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
        btn.setAttribute('aria-label', 'Rejouer la narration');
        if (label) label.textContent = 'Rejouer la narration';
        return;
      }
      btn.innerHTML = audio.paused
        ? '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
      btn.setAttribute('aria-label', audio.paused ? 'Ecouter la narration' : 'Mettre la narration en pause');
    };

    btn.addEventListener('click', () => {
      if (!track) return;
      if (audio.ended) { audio.currentTime = 0; }
      audio.paused ? audio.play().catch(() => {}) : audio.pause();
      setIcon();
    });

    audio.addEventListener('play', setIcon);
    audio.addEventListener('pause', setIcon);
    audio.addEventListener('ended', setIcon);
    audio.addEventListener('timeupdate', () => {
      if (!bar || !audio.duration || !isFinite(audio.duration)) return;
      bar.style.width = (audio.currentTime / audio.duration * 100) + '%';
    });

    if (label && player.dataset.label) label.textContent = player.dataset.label;
    setIcon();
  }

  /* ── 10. Parallaxe légère du hero ───────────────────────── */
  function initHeroParallax() {
    const bg = $('.hero-bg');
    if (!bg || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    document.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (y < window.innerHeight) bg.style.transform = `scale(1.05) translateY(${y * 0.18}px)`;
    }, { passive: true });
  }

  /* ── 11. Année dynamique + date de mise à jour ──────────── */
  function initDates() {
    $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
    $$('[data-updated]').forEach(el => {
      el.textContent = new Date().toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
    });
  }

  /* ── Initialisation ─────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initProgressBar();
    initReveal();
    initCounters();
    initStatBars();
    initTabs();
    initToc();
    initBackToTop();
    initAudioPlayer();
    initNarrationPlayer();
    initHeroParallax();
    initDates();
  });
})();
