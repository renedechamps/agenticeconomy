# Claude Code brief — Monthly Digest section

**Goal:** add a "Monthly Digest" section under the Resources menu on agenticeconomy.dev. Ship issue N°1 (April 2026) live with a hub + issue page, PDF download, and LinkedIn article link. Match the existing site's visual language (navy `#04060e` + emerald `#34d399` + amber `#f59e0b`, Inter typography).

---

## 1. URL structure

Mirror the `/blog/` pattern (hub at root of folder, issues nested):

- Hub: `AgenticEconomy/03-Web/digest/index.html` → public URL `/digest/`
- Issue 1: `AgenticEconomy/03-Web/digest/001-april-2026.html` → public URL `/digest/001-april-2026`

Canonical path for cross-links: `agenticeconomy.dev/digest` (hub), `agenticeconomy.dev/digest/001-april-2026` (issue).

## 2. Navigation change

In every page that carries the global nav (grep for `<button class="nav-item nav-dropdown-trigger">Resources`), add **Monthly Digest** as the FIRST entry of the Resources dropdown, above Glossary:

```html
<div class="dropdown-panel">
  <a href="/digest/">Monthly Digest</a>
  <a href="agentic-economy-glossary.html">Glossary</a>
  <a href="agentic-economy-quiz.html">Quiz</a>
  <a href="agentic-economy-infographic.html">Infographic</a>
  <a href="ask-agentic-economy.html">Ask the Corpus</a>
</div>
```

Also update the footer Resources column (around line 1252 of `index.html` and its siblings) to include the same link in the same position.

## 3. Assets to host

Create `AgenticEconomy/03-Web/digest/assets/` and copy the following from `AgenticEconomy/03-Social/`. **Rename** to drop the `v7.3` / `v2` version suffixes — public URLs stay clean, we bump in-repo but not publicly:

| Source (03-Social) | Destination (03-Web/digest/assets) |
|---|---|
| `AE-Digest-01-April-2026-v7.3.pdf` | `AE-Digest-01-April-2026.pdf` |
| `AE-Digest-cover-01-April-2026-v2.png` | `AE-Digest-01-cover.png` (1280×720, social/OG) |
| `AE-Digest-cover-01-April-2026-v2-2x.png` | `AE-Digest-01-cover-2x.png` (2560×1440, retina) |
| `AE-Digest-01-figure-timeline-v3.png` | `AE-Digest-01-figure-timeline.png` |

Do **not** commit the SVG sources — keep those in `03-Social/` where the build scripts live.

## 4. Hub page — `digest/index.html`

Purpose: one-glance index of all issues. For N°1, only one card appears; the template must accept more without a rewrite.

**Layout (top to bottom):**

1. Global nav (copy from `index.html`).
2. **Masthead** — navy background, title "**Monthly Digest**" (H1), dek *"Agentic commerce, distilled. Monthly. No filler."*, emerald rule beneath.
3. **About the digest card** — 2–3 sentences:
   > A monthly read-out on the agentic-commerce stack — protocols, firms, academic papers, policy. Built on the public corpus (57 entries, coded across eight dimensions, free to cite). For operators, investors, and policy teams shaping agentic commerce.
4. **Subscribe CTA** — single button: **"Subscribe on LinkedIn →"** pointing to the LinkedIn Newsletter URL (placeholder: `https://www.linkedin.com/newsletters/<TK-subscribe-url>` — René to fill in after LinkedIn Article publishes). Secondary link: "Or read the archive below."
5. **Issues grid** — array of `<IssueCard>` (see §4.1). Reverse chronological, newest first. N°1 is the only entry today.
6. Footer (copy from `index.html`).

### 4.1 IssueCard component

Each card is a clickable tile, ~260px tall on desktop, stacking on mobile.

```
┌──────────────────────────────────────────────────┐
│ [cover image, 16:9, fills card top half]         │
├──────────────────────────────────────────────────┤
│ № 01 · APRIL 2026                 (emerald tag) │
│ A2A hits 1.0 — why the trust layer is the       │
│ story of the quarter                    (H3)    │
│                                                  │
│ From slideware to plumbing — how identity,      │
│ delegation, and neutral governance all moved    │
│ in the same month.               (dek, muted)   │
│                                                  │
│ Read issue →      Download PDF ↓   LinkedIn ↗  │
└──────────────────────────────────────────────────┘
```

- Cover image = `AE-Digest-01-cover.png`, `srcset` with 2x for retina.
- "Read issue" → `/digest/001-april-2026`
- "Download PDF" → `/digest/assets/AE-Digest-01-April-2026.pdf` (attr `download`)
- "LinkedIn" → `<TK-linkedin-article-url>` (René fills in after publishing)

Data-driven: read issue metadata from an array at the top of the file (id, number, date, title, dek, cover, pdf, linkedin, slug) so adding N°2 is a one-line append.

## 5. Issue page — `digest/001-april-2026.html`

Purpose: canonical web copy of the issue. Primary CTA = download PDF. Secondary = LinkedIn article.

**Layout:**

1. Global nav.
2. **Cover band** — `AE-Digest-01-cover-2x.png` full-bleed, max-height 520px, letterboxed on navy.
3. **Title block** — eyebrow "AGENTIC ECONOMY DIGEST · № 01 · APRIL 2026" (emerald), H1 the issue title, dek in amber italic, audience line in muted slate, byline with ORCID.
4. **Action bar** — sticky on scroll: [Download PDF] [Read on LinkedIn] [Copy link].
5. **Body** — render the markdown at `AgenticEconomy/03-Social/AE-Digest-01-LinkedIn-paste-v7.3.md` as HTML. Match the PDF styling where reasonable (emerald H2 underline, Watch-next callouts with left border, amber figure captions). Embed `AE-Digest-01-figure-timeline.png` where the source references it.
6. **Independence disclosure box** (emerald left border, pale-green background):
   > Independent research · No institutional funding · No industry sponsorship · CC BY-SA 4.0 · ORCID 0009-0007-1033-6519
7. **Next issue teaser** — "Coming in May: recurring scoreboard on last month's calls, plus Paper 5 (KYA) preprint link."
8. Footer.

### 5.1 Markdown → HTML conversion

Use the existing site's Markdown pipeline if one exists; otherwise render statically with a minimal Python script using `markdown` + `markdown.extensions.extra` and inline the result into the HTML shell. Commit the rendered HTML, not a runtime renderer.

## 6. SEO + schema

Both pages get standard meta + OpenGraph + Twitter card:

- `<title>` — "Monthly Digest — AgenticEconomy.dev" (hub) / "A2A hits 1.0 — Agentic Economy Digest N°1 (April 2026)" (issue).
- `<meta name="description">` — 155-char summary.
- OG image = `AE-Digest-01-cover.png` (absolute URL).
- `og:type` = `article` for the issue page, `website` for the hub.

Issue page embeds JSON-LD:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "A2A hits 1.0 — why the trust layer is the story of the quarter",
  "datePublished": "2026-04-22",
  "author": {
    "@type": "Person",
    "name": "René Dechamps Otamendi",
    "identifier": "https://orcid.org/0009-0007-1033-6519"
  },
  "publisher": {
    "@type": "Organization",
    "name": "AgenticEconomy.dev",
    "url": "https://agenticeconomy.dev"
  },
  "license": "https://creativecommons.org/licenses/by-sa/4.0/",
  "isPartOf": {
    "@type": "PublicationIssue",
    "issueNumber": "1",
    "datePublished": "2026-04-22"
  }
}
```

## 7. Sitemap + RSS

- Add `/digest/` and `/digest/001-april-2026` to `sitemap.xml` if one exists.
- Add a feed at `/digest/feed.xml` (Atom or RSS 2.0, 20 items). N°1 is the only entry. Hub page links to it via `<link rel="alternate" type="application/rss+xml" href="/digest/feed.xml">`.

## 8. Acceptance criteria

- `/digest/` loads, shows one IssueCard (N°1), Subscribe CTA, and footer.
- `/digest/001-april-2026` loads, displays cover + full issue body + timeline figure + download button that serves the PDF.
- Resources dropdown on every page now shows "Monthly Digest" as the first item.
- Footer Resources column updated likewise.
- Lighthouse ≥ 95 on performance, accessibility, SEO for both new pages.
- Mobile: cover band legible at 420px, IssueCard stacks vertically.
- No 404s on the PDF, cover, or figure asset URLs.
- `sitemap.xml` and `feed.xml` validate.

## 9. Out of scope (do NOT do)

- Email opt-in / backend subscribe form. LinkedIn is the only subscribe channel for now.
- Comments, reactions, analytics beyond what the site already has.
- Regenerating the PDF or cover — the files in `03-Social/` are locked.
- N°2 scaffolding. The data model must support it, but no placeholder issue.

## 10. Once shipped, ping back with

- The two canonical URLs.
- A screenshot of each page at desktop + mobile widths.
- The LinkedIn Article URL placeholder replaced, or flagged as `<TK>` for René to fill in after publishing.

---

**Assets recap (source of truth in `AgenticEconomy/03-Social/`):**

- `AE-Digest-01-April-2026-v7.3.pdf` — final canonical PDF, 10pp, 516 KB.
- `AE-Digest-cover-01-April-2026-v2.png` / `-v2-2x.png` — cover, 1280×720 / 2560×1440.
- `AE-Digest-01-figure-timeline-v3.png` — Figure 1.
- `AE-Digest-01-LinkedIn-paste-v7.3.md` — body copy source (1,312 words).

— René Dechamps Otamendi · AgenticEconomy.dev
