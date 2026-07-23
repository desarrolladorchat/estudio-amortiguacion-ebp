(() => {
  "use strict";

  const SOURCE = "MANUAL_TECNICO_ESTUDIOS_AMORTIGUACION.md";
  const documentNode = document.getElementById("manualDocument");
  const tocNode = document.getElementById("manualToc");
  const searchInput = document.getElementById("manualSearch");
  const searchStatus = document.getElementById("searchStatus");
  const sidebar = document.getElementById("manualSidebar");
  const toggleToc = document.getElementById("toggleToc");
  const closeToc = document.getElementById("closeToc");
  const backToTop = document.getElementById("backToTop");
  let matches = [];
  let currentMatch = -1;

  function slugify(value) {
    return value
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
  }

  function sanitizeRenderedHtml(html) {
    const template = document.createElement("template");
    template.innerHTML = html;
    template.content.querySelectorAll("script, iframe, object, embed, form, style").forEach((node) => node.remove());
    template.content.querySelectorAll("*").forEach((node) => {
      [...node.attributes].forEach((attribute) => {
        const name = attribute.name.toLowerCase();
        const value = attribute.value.trim().toLowerCase();
        if (name.startsWith("on") || ((name === "href" || name === "src") && value.startsWith("javascript:"))) {
          node.removeAttribute(attribute.name);
        }
      });
    });
    return template.innerHTML;
  }

  function renderFallback(markdown) {
    const escaped = markdown
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    return `<div class="error-card"><strong>No se pudo iniciar el procesador Markdown.</strong><p>Se muestra el archivo en formato de texto.</p></div><pre><code>${escaped}</code></pre>`;
  }

  function decorateHeadings() {
    const used = new Map();
    documentNode.querySelectorAll("h1, h2, h3, h4").forEach((heading) => {
      const base = slugify(heading.textContent) || "seccion";
      const count = used.get(base) || 0;
      used.set(base, count + 1);
      heading.id = count ? `${base}-${count + 1}` : base;
      if (heading.matches("h2, h3")) {
        const anchor = document.createElement("a");
        anchor.className = "heading-anchor";
        anchor.href = `#${heading.id}`;
        anchor.setAttribute("aria-label", `Enlace a ${heading.textContent}`);
        anchor.textContent = "#";
        heading.append(anchor);
      }
    });
  }

  function decorateLinks() {
    documentNode.querySelectorAll("a[href]").forEach((link) => {
      try {
        const url = new URL(link.href, location.href);
        if (url.origin !== location.origin) {
          link.target = "_blank";
          link.rel = "noopener";
        }
      } catch {
        // The browser keeps the original relative link.
      }
    });
  }

  function buildToc() {
    const headings = [...documentNode.querySelectorAll("h2, h3")];
    const list = document.createElement("ul");
    headings.forEach((heading) => {
      const item = document.createElement("li");
      item.className = `level-${heading.tagName.slice(1)}`;
      const link = document.createElement("a");
      link.href = `#${heading.id}`;
      link.textContent = heading.childNodes[0]?.textContent?.trim() || heading.textContent.replace(/#$/, "").trim();
      link.addEventListener("click", () => closeSidebar());
      item.append(link);
      list.append(item);
    });
    tocNode.replaceChildren(list);
    observeSections(headings);
  }

  function observeSections(headings) {
    const tocLinks = new Map(
      [...tocNode.querySelectorAll("a")].map((link) => [link.getAttribute("href").slice(1), link])
    );
    const observer = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      tocNode.querySelectorAll("a.active").forEach((link) => link.classList.remove("active"));
      const active = tocLinks.get(visible.target.id);
      if (active) {
        active.classList.add("active");
        active.scrollIntoView({ block: "nearest" });
      }
    }, { rootMargin: "-82px 0px -72% 0px", threshold: [0, 1] });
    headings.forEach((heading) => observer.observe(heading));
  }

  function clearSearchMarks() {
    documentNode.querySelectorAll("mark.manual-match").forEach((mark) => {
      mark.replaceWith(document.createTextNode(mark.textContent));
    });
    documentNode.normalize();
    matches = [];
    currentMatch = -1;
  }

  function markSearch(query) {
    clearSearchMarks();
    const term = query.trim();
    if (term.length < 2) {
      searchStatus.textContent = "";
      return;
    }
    const normalizedTerm = term.toLocaleLowerCase("es");
    const walker = document.createTreeWalker(documentNode, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        if (node.parentElement.closest("code, pre, script, style, mark")) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    nodes.forEach((node) => {
      const text = node.nodeValue;
      const lower = text.toLocaleLowerCase("es");
      let start = 0;
      let index = lower.indexOf(normalizedTerm, start);
      if (index < 0) return;
      const fragment = document.createDocumentFragment();
      while (index >= 0) {
        fragment.append(document.createTextNode(text.slice(start, index)));
        const mark = document.createElement("mark");
        mark.className = "manual-match";
        mark.textContent = text.slice(index, index + term.length);
        fragment.append(mark);
        matches.push(mark);
        start = index + term.length;
        index = lower.indexOf(normalizedTerm, start);
      }
      fragment.append(document.createTextNode(text.slice(start)));
      node.replaceWith(fragment);
    });
    searchStatus.textContent = matches.length ? `${matches.length} coincidencia${matches.length === 1 ? "" : "s"}` : "Sin coincidencias";
    if (matches.length) selectMatch(0);
  }

  function selectMatch(index) {
    if (!matches.length) return;
    matches.forEach((match) => match.classList.remove("current"));
    currentMatch = (index + matches.length) % matches.length;
    matches[currentMatch].classList.add("current");
    matches[currentMatch].scrollIntoView({ behavior: "smooth", block: "center" });
    searchStatus.textContent = `${currentMatch + 1} de ${matches.length}`;
  }

  function openSidebar() {
    sidebar.classList.add("open");
    toggleToc.setAttribute("aria-expanded", "true");
  }

  function closeSidebar() {
    sidebar.classList.remove("open");
    toggleToc.setAttribute("aria-expanded", "false");
  }

  async function typesetMath() {
    if (!window.MathJax?.typesetPromise) return;
    try {
      await window.MathJax.typesetPromise([documentNode]);
    } catch (error) {
      console.warn("MathJax no pudo procesar algunas fórmulas.", error);
    }
  }

  async function loadManual() {
    try {
      const response = await fetch(SOURCE, { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const markdown = await response.text();
      const html = window.marked?.parse
        ? window.marked.parse(markdown, { gfm: true, breaks: false })
        : renderFallback(markdown);
      documentNode.innerHTML = sanitizeRenderedHtml(html);
      decorateHeadings();
      decorateLinks();
      buildToc();
      await typesetMath();
      if (location.hash) {
        requestAnimationFrame(() => document.getElementById(location.hash.slice(1))?.scrollIntoView());
      }
    } catch (error) {
      documentNode.innerHTML = `<div class="error-card"><strong>No fue posible cargar el manual.</strong><p>${error.message}</p><p><a href="${SOURCE}">Abrir el archivo Markdown directamente</a>.</p></div>`;
      tocNode.innerHTML = "<p class=\"loading-small\">Índice no disponible.</p>";
    }
  }

  let searchTimer;
  searchInput.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => markSearch(searchInput.value), 180);
  });
  searchInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && matches.length) {
      event.preventDefault();
      selectMatch(currentMatch + (event.shiftKey ? -1 : 1));
    }
    if (event.key === "Escape") {
      searchInput.value = "";
      clearSearchMarks();
      searchStatus.textContent = "";
    }
  });
  toggleToc.addEventListener("click", () => sidebar.classList.contains("open") ? closeSidebar() : openSidebar());
  closeToc.addEventListener("click", closeSidebar);
  document.getElementById("printManual").addEventListener("click", () => window.print());
  backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  window.addEventListener("scroll", () => backToTop.classList.toggle("visible", scrollY > 700), { passive: true });

  loadManual();
})();
