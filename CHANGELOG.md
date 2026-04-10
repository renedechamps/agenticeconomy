# Changelog

All notable changes to agenticeconomy.dev.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Versioning: [SemVer](https://semver.org/).

## [3.0.0] — 2026-04-10

**Full pivot from v1 → v3.** This release replaces the previous 11-operations deployment with a research-hub focused on the agentic economy: definitions, peer-reviewed papers, protocols, glossary, and a public API. Zero frameworks, zero build tools, zero tracking. Licensed CC BY-SA 4.0.

### Scope of the pivot

v1 was an operations-and-services site. v3 is a research corpus and reference hub. This is not an incremental update — the information architecture, content model, and audience are different. Every page has been rewritten from the Spec-Rebuild-Web-v3 specification.

### Added

#### Content
- **51 canonical definitions** under `/definition/` covering the six-category taxonomy (A: Agent-Assisted Human Commerce, B: Agent-as-Workforce, C_cr: Autonomous A2A Crypto, C_s: Autonomous A2A Non-Crypto, D: Analytical/Regulatory, E: Infrastructure/Standards), each with Source Context & Analysis, sidebar metadata (ID, category, cite), prev/next navigation, and related definitions.
- **30 glossary term pages** under `/term/` with Q&A content rendered as FAQPage structured data for rich results.
- **17 main hub pages** rewritten from scratch with full meta + JSON-LD coverage:
  `index.html`, `about-agentic-economy.html`, `agentic-economy-101.html`, `agentic-economy-definitions.html`, `agentic-economy-glossary.html`, `agentic-economy-protocols.html`, `agentic-economy-timeline.html`, `agentic-economy-research.html`, `agentic-economy-infographic.html`, `agentic-economy-quiz.html`, `ask-agentic-economy.html`, `compare.html`, `embed-demo.html`, `field-reports.html`, `sandbox.html`, `validators.html`, `404.html`.
- **Three peer-reviewed Zenodo papers** referenced with canonical DOIs throughout:
  - Commerce Readiness Index (CRI) — `10.5281/zenodo.19208083`
  - Taxonomy of the Agentic Economy — `10.5281/zenodo.19208278`
  - The Oracle Problem in Agent Commerce — `10.5281/zenodo.19208440`
- **Public JSON API** under `/api/`: `definitions.json`, `protocols.json`, `glossary.json`, `meta.json` + browsable index.
- **Embeddable widget** (`embed.js`) and demo page.

#### SEO (Section 5 of the spec — ~70% of the build effort)
- **Full meta tag template** on every page: `<title>`, `meta description`, canonical, `theme-color`, `color-scheme`, full Open Graph (`og:title`, `og:description`, `og:url`, `og:type`, `og:image`, `og:site_name`, `og:locale`), Twitter Card (`twitter:card`, `twitter:site`, `twitter:creator`, `twitter:title`, `twitter:description`, `twitter:image`), `article:*` for content pages.
- **JSON-LD structured data** per page type:
  - Sitewide: `Organization` (with `@id` anchor), `WebSite` (with `SearchAction` for sitelinks search box).
  - Home: `WebPage` + `CollectionPage` + `ItemList`.
  - Definition pages (×51): `DefinedTerm` inside `DefinedTermSet` + `ScholarlyArticle` + `BreadcrumbList`.
  - Glossary pages (×30): `FAQPage` + `DefinedTerm` + `BreadcrumbList`.
  - Research page: `CollectionPage` with `mainEntity` → 3 `ScholarlyArticle` entries with full DOI + author schema.
  - Timeline: `ItemList` with five eras.
  - Protocols: `ItemList` with 17 protocols.
  - About: `AboutPage` + `Person` schema for Rene Dechamps Otamendi.
  - API: `WebApplication` + `Dataset`.
  - Global `BreadcrumbList` on all non-root pages.
- **sitemap.xml** — 100 URLs with `priority`, `changefreq`, `lastmod`.
- **robots.txt** — explicitly allows 16 LLM/AI crawlers: `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `CCBot`, `Bytespider`, `anthropic-ai`, `FacebookBot`, `Applebot-Extended`, `Omgilibot`, `DuckAssistBot`, `Amazonbot`, `YouBot`, `cohere-ai`, `Diffbot`, `ImagesiftBot`, plus the Big 4 search engines.
- **llms.txt + llms-full.txt** (emerging standard by Anthropic for LLM-facing site summaries). `llms-full.txt` is a 44 KB markdown export of the full corpus grouped by taxonomy category — ready for LLM ingestion.
- **feed.xml** — RSS 2.0 feed with 5 items for the major research outputs.
- **\_headers** — Cloudflare Pages headers: CSP, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`, HSTS with `preload`, per-file-type cache-control (static assets 1y immutable, HTML no-cache), `Access-Control-Allow-Origin: *` for `/api/*`.
- **\_redirects** — apex canonicalization for `.info` and `.us` and `www.*` → `agenticeconomy.dev`, clean-URL rewrites (strip `.html`), legacy v1 paths → closest v3 equivalent, `contrarian-take` → `410 Gone` (defense-in-depth, see below).
- **E-E-A-T signals** throughout: author bylines with ORCID, affiliation (BotNode — The Lab: Where Theory Meets Code), peer-reviewed citations with DOIs, explicit dates, CC BY-SA 4.0 licensing, source code references.

#### Infrastructure
- Internal link checker (`03-Web-Tooling/link-check.js`) — verified 3602 internal links across 101 HTML files: **0 broken**.
- Generators under `03-Web-Tooling/`: `generate-definitions-v3.js`, `generate-glossary-v3.js`, `update-main-pages.js`, `generate-seo-files.js`, `shared-template.js`.

### Changed

- **Information architecture** rebuilt around the taxonomy + research corpus model. Navigation: Start Here · Research▾ (Papers, Definitions, Glossary, Protocols, Timeline) · Resources▾ (API, Embed, Compare, Sandbox, Field Reports) · About.
- **Dark theme** consolidated as the only theme.
- **URLs are clean** (no `.html` suffix). Redirects handle legacy links.
- **Canonical domain** is `agenticeconomy.dev`. `.info`, `.us`, and `www.*` redirect to apex.

### Removed

- **All v1 "11 operations" content** and its information architecture.
- **Analytics and tracking** — zero third-party scripts, zero cookies.
- **Build tooling dependencies** — no webpack, no Next.js, no React, no npm runtime. Content is generated by Node scripts but the deployed site is static HTML.

### Security

- **Contrarian Take is NOT published in this release.** The draft has been moved to a sibling `03-Web-Drafts/` directory outside the deploy root. Additionally, `/agentic-economy-contrarian-take` returns `410 Gone` via `_redirects` as defense-in-depth. Do not re-publish without explicit approval.
- CSP in `_headers` restricts scripts to `self` + `cdnjs.cloudflare.com` (for MathJax on research pages).
- HSTS with `includeSubDomains` and `preload`.

### Known limitations (to address in follow-up releases)

- **ORCID not yet injected into Person/Organization JSON-LD.** The author now has ORCID `0009-0007-1033-6519`; will be added in v3.0.1.
- **Ask chatbot (`ask-agentic-economy.html`) is UI-only** — the Gemini backend Worker is not deployed yet (awaiting API key).
- **`og:image` references** point to `/social-card.png` which needs to be generated (1200×630 PNG).

### Stats

- 127 files tracked in this release
- 61,661 lines added
- 101 HTML pages
- 3,602 internal links verified

### Contributors

- Rene Dechamps Otamendi ([ORCID 0009-0007-1033-6519](https://orcid.org/0009-0007-1033-6519)) — author, curator, sole contributor
- Build assisted by Claude (Anthropic)
