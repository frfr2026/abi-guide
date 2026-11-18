/* ════════════════════════════════════════════════════════════════
   ABI NEXUS — navigation.js : menu mobile, mega-menu, état actif
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

  const isMobile = () => window.innerWidth <= 768;

  function initNav() {
    const nav = $('.site-nav');
    const burger = $('.hamburger');
    const links = $('.nav-links');

    /* Ombre au scroll */
    document.addEventListener('scroll', () => {
      if (nav) nav.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });

    if (!burger || !links) return;

    /* ── Bouton menu mobile ─────────────────────────────────── */
    const setBurger = open => {
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      burger.innerHTML = open
        ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>';
    };

    const openPanel = open => {
      links.classList.toggle('open', open);
      setBurger(open);
    };

    burger.addEventListener('click', () => openPanel(!links.classList.contains('open')));

    /* ── Liens du menu ────────────────────────────────────────
       Sur mobile, un lien de premier niveau porteur d'un méga-menu
       déplie sa colonne au lieu de fermer le panneau : le clic est
       intercepté ici, le panneau reste donc ouvert et visible.
       Les liens de contenu (méga-colonne ou entrée directe) ferment
       le panneau comme attendu. */
    $$('.nav-links .nav-link, .nav-links .mega-col a', links).forEach(a => {
      const isTrigger = a.parentElement && a.parentElement.classList.contains('has-mega');

      if (isTrigger) {
        a.setAttribute('aria-expanded', 'false');
        a.addEventListener('click', e => {
          if (!isMobile()) return;          // sur desktop : navigation normale
          e.preventDefault();
          const open = a.parentElement.classList.toggle('open');
          a.setAttribute('aria-expanded', String(open));
        });
        return;
      }

      a.addEventListener('click', () => openPanel(false));
    });

    /* Fermeture au clavier (Échap) */
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && links.classList.contains('open')) {
        openPanel(false);
        burger.focus();
      }
    });

    /* Referme le panneau si la fenêtre repasse en mode large */
    window.addEventListener('resize', () => {
      if (!isMobile() && links.classList.contains('open')) openPanel(false);
    });

    /* ── Lien actif selon la page courante ───────────────────── */
    const current = window.location.pathname.split('/').pop() || 'index.html';
    $$('.nav-links .nav-link, .nav-links .mega-col a', links).forEach(a => {
      const href = a.getAttribute('href') || '';
      if (href.split('/').pop() === current) a.classList.add('active');
    });
  }

  document.addEventListener('DOMContentLoaded', initNav);
})();
