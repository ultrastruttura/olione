(() => {
  document.documentElement.classList.add("js");

  if (window.OlioneI18n) window.OlioneI18n.init();

  const copy = (key) => {
    const lang =
      (window.OlioneI18n && document.documentElement.dataset.lang) || "it";
    return window.OlioneI18n ? window.OlioneI18n.t(lang, key) : key;
  };

  const header = document.querySelector("[data-header]");
  const hero = document.querySelector(".hero");
  const toggle = document.querySelector("[data-nav-toggle]");
  const mobileNav = document.querySelector("[data-mobile-nav]");
  const year = document.querySelector("[data-year]");

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  const setMenuOpen = (open) => {
    if (!toggle || !mobileNav || !header) return;
    toggle.setAttribute("aria-expanded", String(open));
    mobileNav.hidden = !open;
    header.classList.toggle("is-open", open);
    document.body.classList.toggle("nav-open", open);
  };

  const onScroll = () => {
    if (!header) return;
    // Stay transparent over the hero; solid only after leaving the photo.
    const pastHero = hero
      ? hero.getBoundingClientRect().bottom <= header.offsetHeight
      : window.scrollY > 24;
    header.classList.toggle("is-scrolled", pastHero);
  };

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);

  if (toggle && mobileNav) {
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      setMenuOpen(!open);
    });

    mobileNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setMenuOpen(false));
    });

    window.addEventListener("keydown", (event) => {
      if (event.key === "Escape") setMenuOpen(false);
    });

    window.addEventListener(
      "resize",
      () => {
        if (window.matchMedia("(min-width: 860px)").matches) {
          setMenuOpen(false);
        }
      },
      { passive: true }
    );
  }

  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.16, rootMargin: "0px 0px -6% 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-in"));
  }

  const contactForm = document.querySelector("[data-contact-form]");
  const contactStatus = document.querySelector("[data-contact-status]");
  if (contactForm && contactStatus) {
    const setStatus = (message, state) => {
      contactStatus.hidden = !message;
      contactStatus.textContent = message;
      contactStatus.dataset.state = state || "";
    };

    contactForm.addEventListener("submit", async (event) => {
      event.preventDefault();

      const submitBtn = contactForm.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = true;
      setStatus(copy("form.sending"), "pending");

      try {
        const response = await fetch(contactForm.action, {
          method: "POST",
          body: new FormData(contactForm),
          headers: { Accept: "application/json" },
        });

        if (response.ok) {
          contactForm.reset();
          setStatus(copy("form.success"), "success");
        } else {
          setStatus(copy("form.error"), "error");
        }
      } catch {
        setStatus(copy("form.offline"), "error");
      } finally {
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  }
})();
