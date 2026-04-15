# Changelog

All notable changes to agenticeconomy.dev.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Versioning: [SemVer](https://semver.org/).

## [3.1.1] — 2026-04-15

**Real 1200×630 PNG social card.** Proper raster `og:image` so X, LinkedIn, Discord, Slack, iMessage and Google Business Profile show a clean branded preview instead of the SVG placeholder.

### Added

- **`/og-image.png`** (1200×630, 50 KB) — dark-navy gradient matching the v3 theme with emerald (`#34d399`) accents. Renders the brand "AgenticEconomy.dev", the tagline "The Agentic Economy — Definitions, preprints, and protocols for agent-mediated commerce.", and the credibility stats row: **51 definitions · 3 preprints · 30 glossary terms · CC BY-SA**. Legible at thumbnail size (300×157). Generated deterministically by a new tooling script (`03-Web-Tooling/generate-og-image.py`, pure Pillow — no external deps).
- **`og:image:type`** meta tag (`image/png`) on all pages.
- **`og:image:alt` + `twitter:image:alt`** descriptive alt text on every page — accessibility improvement + extra keyword signal for social preview indexers.
- **Per-post `ogImageAlt` override** in `generate-blog.js` — the blog post now exposes a post-specific image alt derived from its `heroAlt` field, instead of inheriting the site-wide alt.

### Changed

- `SITE.ogImage` → `https://agenticeconomy.dev/og-image.png` (was `/agentic-economy-two-economies.svg`, which several social platforms refused to render as a card preview because SVG is not in their supported og:image content-type allowlist).
- `headMeta()` in `shared-template.js` now accepts `opts.ogImageAlt` and falls back to `SITE.ogImageAlt` — matches the existing pattern for `ogImage`.
- Every main, definition, glossary, and blog listing page regenerated (146 HTML files) to pick up the new og:image + alt + content-type tags.

### Unchanged (by design)

- The blog post at `/blog/what-is-the-agentic-economy/` still uses its own 1200×630 hero PNG as `og:image` — post-specific social cards are a best practice and the hero is already the correct dimensions.
- `Organization.logo` in JSON-LD still points to the existing brand SVG (separate identity from the social card; logo ≠ og:image).

### Stats

- 1 new asset: `og-image.png` (1200×630, 50 KB)
- 146 HTML files regenerated · 4,329 internal links verified · 0 real broken
- No content changes, no schema changes, no new pages

### Not yet in this release

- **Post 2** ("Why Agent Reputation Is Harder Than You Think") — held for v3.2.0.
- **Post 3** ("You Can't Verify Quality With an LLM") — held for v3.3.0.
- **Ask chatbot Gemini backend** — still awaiting API key.

---

## [3.1.0] — 2026-04-15

**Blog section launch + ORCID injection.** First blog post goes live as a companion explainer to the Taxonomy paper. Author identity is now fully wired in structured data across the site.

### Added

#### Blog section (new)
- **`/blog/` — Blog listing page** with `Blog` JSON-LD (links to all posts), hero intro, "Coming next" card pointing to the RSS feed.
- **Post 1: [What Is the Agentic Economy? Five Categories, Two Fault Lines](https://agenticeconomy.dev/blog/what-is-the-agentic-economy/)** — 1,087-word paper explainer (5 min read) for the Taxonomy paper (DOI 10.5281/zenodo.19208278). Includes:
  - Full `BlogPosting` JSON-LD with author Person (ORCID, affiliation, sameAs), publisher Organization, citation → ScholarlyArticle, license CC BY-SA 4.0, wordCount, articleSection, keywords.
  - `BreadcrumbList` JSON-LD (Home → Blog → post).
  - Google Scholar citation meta tags (`citation_title`, `citation_author`, `citation_publication_date`, `citation_doi`, `citation_public_url`).
  - Article-specific OG/Twitter meta + `article:section`, `article:tag` per tag, `article:author`.
  - Hero image (`agentic-economy-five-categories-taxonomy.png`, 262 KB) with proper `og:image` references.
  - Auto-generated Table of Contents from `<h2>` headings.
  - Reading time estimate (based on 220 wpm).
  - Share buttons (X/Twitter, LinkedIn, email, copy-link) — all URL-intent based, no third-party scripts, no tracking.
  - Author bio card with ORCID badge, affiliation, avatar, and bio-links to About / Papers / personal site.
  - "Read next" related-links grid (4 cards: paper, 51 definitions, protocol matrix, Settlement Neutrality glossary term).
  - Prev/Next post navigation (hidden when no siblings — will appear when posts 2 & 3 ship).
- **Blog images directory** at `/blog/images/` with immutable cache headers inherited from existing `/*.png` rule.

#### ORCID + author identity
- **ORCID `0009-0007-1033-6519`** injected into:
  - `SITE.authorOrcid`, `SITE.authorOrcidUrl`, `SITE.orgSameAs`, `SITE.authorSameAs` in `shared-template.js`.
  - `Organization.sameAs` across every page.
  - New `personJsonLd()` helper exports full Person schema: name, url, identifier (PropertyValue with ORCID propertyID), jobTitle, affiliation (BotNode — The Lab), sameAs (renedechamps.com + ORCID + GitHub + LinkedIn + Zenodo community).
  - `BlogPosting.author` in Post 1.
- **Author affiliation**: "BotNode — The Lab: Where Theory Meets Code" now surfaced in Person schema.

#### Navigation
- **Top-level `Blog` link** added to primary nav between `Resources▾` and `About` on all 101 pages.
- **`Blog` link** added to the "Project" column in the site footer on all pages.

### Changed

- `SITE.modifiedDate` bumped to `2026-04-15`.
- `feed.xml` now leads with the blog post (with `<author>` and `<category>` per tag) before the original v3-launch items.
- `sitemap.xml` grew from 100 → 102 URLs (+ `/blog/` and `/blog/what-is-the-agentic-economy/`, both `priority=0.8`).
- `llms.txt` gained a `## Blog` section linking to the listing and every post.
- `llms-full.txt` grew by ~5 KB — Post 1 full text is embedded as markdown under a `## Blog` heading for LLM ingestion.

### Stats

- 146 HTML files (was 101) — 3 new blog files + 42 regenerated definition/term/main pages with updated nav
- 4,329 internal links verified · 0 broken
- 102 URLs in sitemap
- Post 1 wordCount: 1,087 · reading time: 5 min

### Not yet in this release

- **Post 2** ("Why Agent Reputation Is Harder Than You Think") and **Post 3** ("You Can't Verify Quality With an LLM") — held for subsequent releases.
- **og:image social card PNG** (1200×630) — still references the SVG placeholder; needs a proper raster card for X/LinkedIn/Discord unfurls.
- **Ask chatbot Gemini backend** — still awaiting API key.

---

## [3.0.0] — 2026-04-10

**Full pivot from v1 → v3.** This release replaces the previous 11-operations deployment with a research-hub focused on the agentic economy: definitions, preprints, protocols, glossary, and a public API. Zero frameworks, zero build tools, zero tracking. Licensed CC BY-SA 4.0.

### Scope of the pivot

v1 was an operations-and-services site. v3 is a research corpus and reference hub. This is not an incremental update — the information architecture, content model, and audience are different. Every page has been rewritten from the Spec-Rebuild-Web-v3 specification.

### Added

#### Content
- **51 canonical definitions** under `/definition/` covering the six-category taxonomy (A: Agent-Assisted Human Commerce, B: Agent-as-Workforce, C_cr: Autonomous A2A Crypto, C_s: Autonomous A2A Non-Crypto, D: Analytical/Regulatory, E: Infrastructure/Standards), each with Source Context & Analysis, sidebar metadata (ID, category, cite), prev/next navigation, and related definitions.
- **30 glossary term pages** under `/term/` with Q&A content rendered as FAQPage structured data for rich results.
- **17 main hub pages** rewritten from scratch with full meta + JSON-LD coverage:
  `index.html`, `about-agentic-economy.html`, `agentic-economy-101.html`, `agentic-economy-definitions.html`, `agentic-economy-glossary.html`, `agentic-economy-protocols.html`, `agentic-economy-timeline.html`, `agentic-economy-research.html`, `agentic-economy-infographic.html`, `agentic-economy-quiz.html`, `ask-agentic-economy.html`, `compare.html`, `embed-demo.html`, `field-reports.html`, `sandbox.html`, `validators.html`, `404.html`.
- **Three Zenodo preprints** referenced with canonical DOIs throughout:
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
- **E-E-A-T signals** throughout: author bylines with ORCID, affiliation (AgenticEconomy.dev), preprint citations with DOIs, explicit dates, CC BY-SA 4.0 licensing, source code references.

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
