(() => {
  const STORAGE_KEY = "olione-lang";
  const strings = {
    it: {
      "meta.title":
        "Olione | Olio extravergine del Sebino · Predore · Lago d'Iseo",
      "meta.description":
        "Olione è olio extravergine di oliva del Sebino, da Predore sul Lago d'Iseo. Bottiglia da 0,5 l dal produttore Carlo Duci, con spedizione in tutta Italia.",
      "meta.ogTitle": "Olione | Olio extravergine del Sebino",
      "meta.ogDescription":
        "Olio extravergine di oliva del Sebino, da Predore sul Lago d'Iseo. Dal produttore, bottiglia 0,5 l, spedizione in Italia.",
      "skip": "Vai al contenuto",
      "nav.label": "Principale",
      "nav.grove": "L'uliveto",
      "nav.harvest": "La raccolta",
      "nav.mill": "Al frantoio",
      "nav.products": "I nostri prodotti",
      "nav.contact": "Contatti",
      "nav.menu": "Menu",
      "lang.label": "Lingua",
      "hero.label": "Home page",
      "hero.alt": "Predore sul Lago d'Iseo, sponda bergamasca del Sebino",
      "hero.place": "Predore · Lago d'Iseo",
      "hero.kicker": "Olio extravergine dal produttore",
      "hero.ctaProducts": "I nostri prodotti",
      "hero.ctaOrder": "Ordina",
      "hero.scroll": "Scorri",
      "grove.eyebrow": "L'uliveto",
      "grove.title": "Tra lago e pietra",
      "grove.p1":
        "Coltiviamo olive su terrazzamenti sostenuti da antichi muri in pietra, affacciati sul Lago d'Iseo, nel comune di Predore: circa un centinaio di piante, di circa cinquant'anni.",
      "grove.p2":
        "Qui il microclima del Sebino — il Lago d'Iseo — accompagna la crescita degli olivi: luce, pendenza e cura quotidiana del territorio danno carattere al frutto e, di stagione in stagione, all'olio.",
      "grove.alt": "Reti da raccolta stese nell'uliveto di Predore sul Lago d'Iseo",
      "grove.caption": "Predore - Il nostro Uliveto",
      "strip.label": "Promessa di marca",
      "strip.text": "Prodotto dalla cura del nostro territorio",
      "harvest.eyebrow": "La raccolta",
      "harvest.title": "Ottobre, ogni sera al frantoio",
      "harvest.p1":
        "Raccogliamo le olive nelle prime settimane di ottobre, quando il frutto è ancora fresco e pieno di aroma.",
      "harvest.p2":
        "Dopo la raccolta, ogni sera, le portiamo al frantoio per la frangitura e l'estrazione dell'olio: tempi brevi, per custodire la qualità dell'extravergine.",
      "harvest.altWork": "Raccolta delle olive a Predore: reti, cassette e abbacco in uliveto",
      "harvest.altCrates": "Cassette di olive appena raccolte sull'uliveto terrazzato di Predore",
      "mill.eyebrow": "Al frantoio",
      "mill.title": "Dalle olive all'olio",
      "mill.lead":
        "Un percorso meccanico, senza intermedi chimici: dalla pulizia del frutto fino alla filtrazione, ogni passaggio prepara un extravergine limpido e riconoscibile.",
      "mill.alt": "Olio extravergine appena estratto al frantoio",
      "mill.step1": "Pulizia e lavaggio",
      "mill.step2": "Frangitura",
      "mill.step3": "Gramolatura",
      "mill.step4": "Estrazione",
      "mill.step5": "Separazione e filtrazione",
      "products.eyebrow": "I nostri prodotti",
      "products.title": "Olio extravergine di oliva di qualità superiore",
      "products.p1":
        "Olione è un olio extravergine di oliva italiano di categoria superiore, ottenuto direttamente dalle olive e unicamente mediante procedimenti meccanici.",
      "products.slowfood":
        'Il nostro olio è segnalato dalla “Guida agli Extra Vergini” di <a href="https://www.slowfoodeditore.it/it/guide-slow/guida-agli-extravergini-2026-1162.html" target="_blank" rel="noopener noreferrer"><strong>Slow Food Editore</strong></a>.',
      "products.p2":
        "In bottiglia da 0,5 l, pensata per la tavola: un olio del Sebino di piccola misura, legato ai terrazzamenti di Predore e alla campagna di raccolta dell'anno.",
      "products.p3":
        "Lo produciamo noi e lo spediamo in tutta Italia. Scrivici per ordinare la bottiglia della campagna in corso.",
      "products.cta": "Ordina Olione",
      "products.alt":
        "Bottiglia Olione di olio extravergine di oliva italiano",
      "contact.eyebrow": "Contatti",
      "contact.title": "Ordina dal produttore",
      "contact.intro":
        "Per ordinare Olione da Carlo Duci, sapere la disponibilità della campagna o organizzare un ritiro: siamo a Predore, sul Lago d'Iseo, e spediamo in tutta Italia.",
      "contact.email": "Email",
      "contact.phone": "Telefono",
      "contact.social": "Social",
      "contact.address": "Indirizzo",
      "form.subject": "Richiesta Olione dal sito",
      "form.name": "Nome",
      "form.email": "Email",
      "form.message": "Messaggio",
      "form.placeholder": "Es. vorrei ordinare 2 bottiglie da 0,5 l",
      "form.submit": "Invia richiesta",
      "form.sending": "Invio in corso…",
      "form.success": "Richiesta inviata. Ti risponderemo al più presto.",
      "form.error":
        "Invio non riuscito. Riprova o scrivi a olioevopredore@gmail.com.",
      "form.offline":
        "Connessione non disponibile. Riprova o usa email/telefono.",
      "footer.place": "Predore · Bergamo · Lago d'Iseo",
      "footer.line": "Olio extravergine di oliva · Spedizione in Italia",
      "footer.copyright": "Carlo Duci · Olivicoltura",
      "legal.kind": "impresa individuale agricola",
      "legal.seat": "Sede",
      "legal.register": "Registro Imprese di Bergamo",
    },
    en: {
      "meta.title":
        "Olione | Extra virgin olive oil from Lake Iseo · Predore, Bergamo",
      "meta.description":
        "Olione is extra virgin olive oil from the Sebino, produced in Predore on Lake Iseo. 0.5 l bottle from grower Carlo Duci, shipped throughout Italy.",
      "meta.ogTitle": "Olione | Extra virgin olive oil from Lake Iseo",
      "meta.ogDescription":
        "Extra virgin olive oil from the Sebino, Predore on Lake Iseo. From the producer, 0.5 l bottle, shipped in Italy.",
      "skip": "Skip to content",
      "nav.label": "Primary",
      "nav.grove": "The grove",
      "nav.harvest": "Harvest",
      "nav.mill": "The mill",
      "nav.products": "Our products",
      "nav.contact": "Contact",
      "nav.menu": "Menu",
      "lang.label": "Language",
      "hero.label": "Home",
      "hero.alt": "Predore on Lake Iseo, Bergamo shore of the Sebino",
      "hero.place": "Predore · Lake Iseo",
      "hero.kicker": "Extra virgin olive oil from the producer",
      "hero.ctaProducts": "Our products",
      "hero.ctaOrder": "Order",
      "hero.scroll": "Scroll",
      "grove.eyebrow": "The grove",
      "grove.title": "Between lake and stone",
      "grove.p1":
        "We grow olives on terraces held by old stone walls, overlooking Lake Iseo, in Predore: about one hundred trees, around fifty years old.",
      "grove.p2":
        "Here the Sebino microclimate — Lake Iseo — accompanies the olives: light, slope and daily care of the land give character to the fruit and, season after season, to the oil.",
      "grove.alt": "Harvest nets laid out in the Predore olive grove on Lake Iseo",
      "grove.caption": "Predore - Our olive grove",
      "strip.label": "Brand promise",
      "strip.text": "Made through the care of our land",
      "harvest.eyebrow": "Harvest",
      "harvest.title": "October, to the mill every evening",
      "harvest.p1":
        "We pick the olives in the first weeks of October, when the fruit is still fresh and full of aroma.",
      "harvest.p2":
        "After harvest, each evening, we take them to the mill for crushing and extraction: short times, to protect extra virgin quality.",
      "harvest.altWork": "Olive harvest in Predore: nets, crates and pole harvester in the grove",
      "harvest.altCrates": "Crates of freshly picked olives on the terraced grove in Predore",
      "mill.eyebrow": "The mill",
      "mill.title": "From olives to oil",
      "mill.lead":
        "A mechanical process, with no chemical intermediaries: from washing the fruit to filtration, each step prepares a clear, recognisable extra virgin oil.",
      "mill.alt": "Extra virgin olive oil just extracted at the mill",
      "mill.step1": "Cleaning and washing",
      "mill.step2": "Crushing",
      "mill.step3": "Malaxing",
      "mill.step4": "Extraction",
      "mill.step5": "Separation and filtration",
      "products.eyebrow": "Our products",
      "products.title": "Superior-category extra virgin olive oil",
      "products.p1":
        "Olione is Italian extra virgin olive oil of superior category, obtained directly from olives and solely by mechanical means.",
      "products.slowfood":
        'Our oil is listed in <a href="https://www.slowfoodeditore.it/it/guide-slow/guida-agli-extravergini-2026-1162.html" target="_blank" rel="noopener noreferrer"><strong>Slow Food Editore</strong></a>’s “Guida agli Extra Vergini”.',
      "products.p2":
        "In a 0.5 l bottle, made for the table: a small-batch Sebino oil, tied to Predore’s terraces and to that year’s harvest.",
      "products.p3":
        "We produce it ourselves and ship throughout Italy. Write to us to order this season’s bottle.",
      "products.cta": "Order Olione",
      "products.alt":
        "Olione bottle of Italian extra virgin olive oil",
      "contact.eyebrow": "Contact",
      "contact.title": "Order from the producer",
      "contact.intro":
        "To order Olione from Carlo Duci, check this season’s availability or arrange a pickup: we are in Predore, on Lake Iseo, and we ship throughout Italy.",
      "contact.email": "Email",
      "contact.phone": "Phone",
      "contact.social": "Social",
      "contact.address": "Address",
      "form.subject": "Olione enquiry from the website",
      "form.name": "Name",
      "form.email": "Email",
      "form.message": "Message",
      "form.placeholder": "E.g. I would like to order 2 bottles of 0.5 l",
      "form.submit": "Send request",
      "form.sending": "Sending…",
      "form.success": "Request sent. We will get back to you shortly.",
      "form.error":
        "Could not send. Please try again or write to olioevopredore@gmail.com.",
      "form.offline":
        "No connection. Please try again, or use email or phone.",
      "footer.place": "Predore · Bergamo · Lake Iseo",
      "footer.line": "Extra virgin olive oil · Shipping in Italy",
      "footer.copyright": "Carlo Duci · Olive growing",
      "legal.kind": "sole agricultural proprietor",
      "legal.seat": "Registered office",
      "legal.register": "Bergamo Company Register",
    },
  };

  const t = (lang, key) =>
    (strings[lang] && strings[lang][key]) || strings.it[key] || key;

  const readLang = () => {
    const params = new URLSearchParams(window.location.search);
    const fromUrl = params.get("lang");
    if (fromUrl === "en" || fromUrl === "it") return fromUrl;
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored === "en" || stored === "it") return stored;
    } catch {
      /* ignore */
    }
    return "it";
  };

  const setUrlLang = (lang) => {
    const url = new URL(window.location.href);
    if (lang === "it") url.searchParams.delete("lang");
    else url.searchParams.set("lang", lang);
    history.replaceState({}, "", url);
  };

  const setMeta = (selector, attr, value) => {
    const el = document.querySelector(selector);
    if (el) el.setAttribute(attr, value);
  };

  const apply = (lang) => {
    document.documentElement.lang = lang;
    document.documentElement.dataset.lang = lang;
    document.title = t(lang, "meta.title");
    setMeta('meta[name="description"]', "content", t(lang, "meta.description"));
    setMeta('meta[property="og:title"]', "content", t(lang, "meta.ogTitle"));
    setMeta(
      'meta[property="og:description"]',
      "content",
      t(lang, "meta.ogDescription")
    );
    setMeta('meta[property="og:locale"]', "content", lang === "en" ? "en_GB" : "it_IT");
    setMeta('meta[name="twitter:title"]', "content", t(lang, "meta.ogTitle"));
    setMeta(
      'meta[name="twitter:description"]',
      "content",
      t(lang, "meta.ogDescription")
    );

    document.querySelectorAll("[data-i18n]").forEach((el) => {
      el.textContent = t(lang, el.getAttribute("data-i18n"));
    });
    document.querySelectorAll("[data-i18n-html]").forEach((el) => {
      el.innerHTML = t(lang, el.getAttribute("data-i18n-html"));
    });
    document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
      el.setAttribute(
        "placeholder",
        t(lang, el.getAttribute("data-i18n-placeholder"))
      );
    });
    document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
      el.setAttribute(
        "aria-label",
        t(lang, el.getAttribute("data-i18n-aria"))
      );
    });
    document.querySelectorAll("[data-i18n-alt]").forEach((el) => {
      el.setAttribute("alt", t(lang, el.getAttribute("data-i18n-alt")));
    });

    const subject = document.querySelector('input[name="_subject"]');
    if (subject) subject.value = t(lang, "form.subject");

    document.querySelectorAll("[data-lang-switch]").forEach((el) => {
      const active = el.getAttribute("data-lang-switch") === lang;
      el.setAttribute("aria-current", active ? "true" : "false");
      el.classList.toggle("is-active", active);
    });

    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch {
      /* ignore */
    }
  };

  const init = () => {
    apply(readLang());
    document.querySelectorAll("[data-lang-switch]").forEach((el) => {
      el.addEventListener("click", (event) => {
        event.preventDefault();
        const lang = el.getAttribute("data-lang-switch");
        if (lang !== "it" && lang !== "en") return;
        setUrlLang(lang);
        apply(lang);
      });
    });
  };

  window.OlioneI18n = { t, apply, readLang, init };
})();
