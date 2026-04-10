# agenticeconomy.dev — web fixes brief for Claude Code

**Date:** 2026-04-10
**Author:** René Dechamps Otamendi (AgenticEconomy.dev)
**Scope:** 17 issues across the agenticeconomy.dev static site
**Target:** Claude Code running locally in `mnt/OpenClaw/AgenticEconomy/03-Web/`
**Deploy target:** Netlify (detected via `_redirects` and `_headers` files)

---

## 0. Read this first — context you need before touching anything

You are working on **agenticeconomy.dev**, a static research hub on the agentic economy. The owner, René Dechamps Otamendi, publishes preprints on Zenodo and curates a corpus of 51 published definitions of the "agentic economy." The site is the public face of that research. It must look and feel **academic, sober, confident, contrarian** — not a SaaS landing page.

### Source of truth
- **Canonical corpus JSON:** `01-Papers/corpus/definitions-corpus.json` (schema v1.2, 51 entries, all 8 coded dimensions). **Never hand-edit individual fiches to add content that should come from the JSON.** If you need to change something on all fiches, update the JSON and re-run `build_fiches.js` at `/sessions/cool-amazing-wozniak/build_fiches.js` (parent-session scratch dir). If that script is not available in your environment, tell René and do not improvise.
- **Fiches live at:** `03-Web/definition/agentic-economy-def-*.html` (51 canonical + 33 redirect stubs that preserve legacy slugs — do NOT delete the stubs).
- **Owner identity:**
  - Name: *René Dechamps Otamendi*
  - ORCID: `0009-0007-1033-6519`
  - Personal site: `https://renedechamps.com`
  - Signs as: **AgenticEconomy.dev** (NOT BotNode — see §13)

### Hard constraints — do not break these
1. **Do not change any paper titles** except the one explicitly listed in §8. All other paper titles on `agentic-economy-research.html` stay exactly as they are.
2. **Do not break existing URLs.** The redirect stubs in `definition/` exist to preserve SEO on legacy slugs (`google-e1.html`, `visa-a5.html`, etc.). Leave them alone.
3. **Do not delete files.** If something is obsolete, move it to `03-Web/_archive/` and flag it in your PR description.
4. **Do not add tracking, analytics, cookies, or third-party scripts** other than Google Fonts (already in use). The footer line "Zero cookies. Not even Belgian ones." is load-bearing and must remain true.
5. **Preserve the dark theme and the design tokens** in `:root { --bg-deep, --accent: #34d399, --font-display: Syne, ... }`. If a new component needs styling, reuse those tokens — do not introduce new palette colors.
6. **Never market BotNode as open source in general.** BotNode is a research/experimentation ground with proprietary components. See §13.

### Priorities — address in this order
- **P0:** §1 (hero), §2 (Preprints label), §8 (first paper title), §9 (menu hover), §12 (about/profile)
- **P1:** §3 (legal pages), §4 (favicon), §5 (101 page), §6 (tech-name links), §7 (top menu), §15 (contact form)
- **P2:** §10 (infographic), §11 (BotNode positioning), §13 (remove BotNode from profile), §14 (vertical voids), §16 (global polish)

Work sequentially, committing after each section so the PR log reads cleanly. One branch per priority level is fine.

---

## 1. [P0] Hero animation — ship a live data-graph

**Current state:** `index.html`, hero section around line ~940 — the animation is static and feels lifeless.

**What to build:**
A subtle **network graph** animation in the hero, with nodes drifting slowly and edges forming/breaking between them. Each node represents one of the 51 definitions. Node color = category color (A=`#3b82f6`, B=`#a78bfa`, Ccr=`#f59e0b`, Cs=`#34d399`, D=`#f87171`, E=`#22d3ee`). Nodes cluster loosely by category but edges sometimes connect across clusters (representing cross-references from the JSON).

**Requirements:**
- Pure SVG or Canvas, no external libraries. Size < 15 KB inlined.
- `prefers-reduced-motion: reduce` stops the animation and shows a static snapshot.
- No more than 60fps target; throttle to 30fps if battery API is low.
- Node positions and edges are generated at load time from `definitions-corpus.json` — fetch it from `./corpus/definitions-corpus.json` (you will need to copy the canonical JSON to `03-Web/corpus/definitions-corpus.json` as part of this task; do NOT inline all 51 entries in the HTML).
- Edges use `e.cross_references[].id` pairs from the JSON. Fade opacity between 0.1 and 0.4.
- Background is `--bg-deep`. No bright accents — this is ambient, not a game.
- Behind the headline text: the animation sits in a layer with `opacity: 0.35`, pointer-events: none, so the headline and CTA remain readable.

**Acceptance criteria:**
- Lighthouse Performance score on `index.html` stays ≥ 90 on mobile.
- No layout shift (CLS = 0) during animation load.
- Works in Safari, Chrome, Firefox. Degrades gracefully in old browsers (static SVG fallback).
- Tested with `prefers-reduced-motion: reduce` — animation stops immediately.

**Files to edit:** `index.html`, new file `corpus/definitions-corpus.json` (copy from `01-Papers/corpus/definitions-corpus.json`).

---

## 2. [P0] "Peer-reviewed papers" → "Preprints"

**Why:** These papers are preprints on Zenodo, not peer-reviewed publications. The current label is inaccurate and damages credibility with actual academics reading the site.

**Find and replace across the whole site:**
- `Peer-reviewed papers` → `Preprints`
- `peer-reviewed papers` → `preprints`
- `Peer-reviewed research` → `Preprint research`
- `peer-reviewed` (standalone adjective describing the papers) → `preprint`

**Known occurrences (verified):**
- `index.html` lines 7, 16, 29 (meta descriptions), 944 (hero subtext), 1054 (stat label)
- `agentic-economy-research.html` lines 7, 16, 29, 69

**Check also:**
- `llms.txt`, `llms-full.txt`, `feed.xml`, `sitemap.xml` — if any of these mention "peer-reviewed" in the context of the papers, fix them too.
- `_archive/` if it exists — leave archived content alone.

**Do NOT replace "peer-reviewed" when it appears in academic-context descriptions that are accurate** (e.g. if a fiche's analytical note discusses peer-reviewed literature generally — that's fine). Only change labels that describe René's own papers.

**Acceptance criteria:** `grep -ri "peer-reviewed" 03-Web/ | grep -v "_archive"` returns zero matches about René's papers.

---

## 3. [P1] Privacy, Terms, Licensing — new pages, structure from botnode.io

**Why:** The site lacks privacy/terms/licensing pages entirely. Legal exposure and SEO penalty.

**Approach (decided):** Copy the **architecture and section structure** from `botnode.io` but **rewrite the text from scratch** for agenticeconomy.dev. Do not copy text verbatim — AE.dev has a different profile (research hub, open corpus, CC BY-SA 4.0, no accounts, no product).

**Pages to create:**
- `03-Web/privacy.html`
- `03-Web/terms.html`
- `03-Web/licensing.html`

**Each page:**
- Uses the same nav/footer/CSS design system as the rest of the site.
- Uses the `.container` layout from existing pages.
- Has a breadcrumb: Home / Legal / [page name].
- Has a "Last updated" date in the header.
- Has a short TOC if the page has >5 sections.

**Content requirements per page:**

### `privacy.html`
- Cover: what data is collected (spoiler: essentially nothing — the site is static, no accounts, no analytics, no cookies), what logs Netlify keeps by default, how to contact René.
- Explicit statement: no tracking pixels, no third-party cookies, no advertising, no user profiling.
- One section on Google Fonts (used via `fonts.googleapis.com`) with a link to Google's privacy policy and a note that IPs may be logged by Google per that policy.

### `terms.html`
- Cover: site is provided "as is" for research and educational purposes, CC BY-SA 4.0 for the corpus, no warranty, jurisdiction (René — **please confirm: Spain or Belgium?** Currently assume Spain; Claude Code: use a placeholder `[JURISDICTION TBD]` and flag it in your PR).
- The corpus content is curated research; users are free to reuse under CC BY-SA 4.0 with attribution.
- No commercial guarantees. No liability for decisions made based on the content.

### `licensing.html`
- Lists the license for each asset class:
  - **Corpus & analytical notes:** CC BY-SA 4.0
  - **Papers (preprints):** CC BY 4.0 (as published on Zenodo) — include the Zenodo DOIs
  - **Site code (HTML/CSS/JS):** MIT (if you confirm; if not, state "All rights reserved" as placeholder)
  - **BotNode VMP-1.0 specification:** BotNode is a separate project with mixed licensing (see §11 and §13); do not claim it is open source here.
- Includes BibTeX-ready citation for the corpus and each preprint.
- Explicit "How to cite" section with ORCID.

**Footer:** After creating these pages, add links in the footer of ALL pages under a new column "Legal" with: Privacy, Terms, Licensing.

**Files to edit:** Create the 3 new pages. Update the footer in **every** `.html` file that shares the site footer. Use `sed` or a template extraction if possible; do not hand-edit each file independently.

**Acceptance criteria:** The three pages render correctly, are linked from the footer of every page, pass HTML validation, and contain zero placeholder `TODO` markers other than the flagged `[JURISDICTION TBD]`.

---

## 4. [P1] Restore favicon

**Current state:** `<link rel="icon">` tags exist on some pages but the actual `favicon.ico` is missing from `03-Web/`.

**What to do:**
1. Check whether `agentic-economy-two-economies.svg` in `03-Web/` can be used as the favicon source.
2. Generate a full favicon set from that SVG:
   - `favicon.ico` (16×16, 32×32, 48×48 multi-res)
   - `favicon.svg` (vector, already exists as the logo)
   - `apple-touch-icon.png` (180×180)
   - `icon-192.png`, `icon-512.png` (for manifest)
3. Add a `manifest.webmanifest` with basic PWA metadata (name: "Agentic Economy", theme color: `#04060e`, background: `#04060e`).
4. Update the `<head>` section of every HTML page to reference the full set:
   ```html
   <link rel="icon" href="/favicon.svg" type="image/svg+xml">
   <link rel="icon" href="/favicon.ico" sizes="any">
   <link rel="apple-touch-icon" href="/apple-touch-icon.png">
   <link rel="manifest" href="/manifest.webmanifest">
   ```
5. If the existing SVG doesn't render well at 16×16, generate a simplified version (just the AE mark, no text) for the small sizes.

**Tools:** Use ImageMagick or `sharp` if available. If neither is available in your environment, generate the PNGs via an inline SVG-to-PNG conversion tool and tell René which you used.

**Acceptance criteria:** Favicon visible in browser tab on `index.html` after a local serve.

---

## 5. [P1] Page 101 — fix empty space, broken link, tech-name links

**File:** `agentic-economy-101.html`

### 5.1 Too much vertical empty space
The page has large gaps between sections. Audit:
- Reduce `margin-top`/`margin-bottom` on section separators.
- Collapse any placeholder `<div style="height: ...">` spacers.
- Tighten hero padding if it's above 5rem.
- The goal is a content-dense single-scroll 101 guide, not a marketing landing page.

### 5.2 "Read Two Economies, Not One" link is broken
Find the CTA that says "Read Two Economies, Not One" (or similar) and fix the `href`. It should point to the Paper 1 entry on `agentic-economy-research.html#paper-1` (or the exact anchor Claude Code finds for the first paper).

### 5.3 "Biggest names in tech" section — link each name to its fiche
There is a section listing tech companies that have published definitions (Microsoft, Google, Stripe, OpenAI, Visa, Mastercard, etc.). Each name should be a link to the corresponding fiche.

Use the canonical JSON to find the right slug for each name. Examples (verify with the JSON):
- Microsoft → `definition/agentic-economy-def-microsoft-research-a1.html`
- Stripe/OpenAI → `definition/agentic-economy-def-stripe-openai-a2.html`
- Google/Shopify/Walmart → `definition/agentic-economy-def-google-shopify-walmart-a3.html`
- Google/Mastercard/PayPal → `definition/agentic-economy-def-google-mastercard-paypal-a4.html`
- Visa → `definition/agentic-economy-def-visa-a5.html`
- Mastercard → `definition/agentic-economy-def-mastercard-a6.html`
- IBM → `definition/agentic-economy-def-ibm-a8.html`
- Salesforce → `definition/agentic-economy-def-salesforce-a9.html`
- JPMorgan → `definition/agentic-economy-def-jpmorgan-a10.html`
- Google A2A → `definition/agentic-economy-def-google-e1.html`
- Anthropic → `definition/agentic-economy-def-anthropic-e2.html`

If the section names tech companies not in the corpus, leave them as plain text.

**Acceptance criteria:** No broken links on `agentic-economy-101.html`, vertical spacing feels tight, every mentioned tech company with a corpus entry is a link.

---

## 6. [P1] Top menu — Research must lead to papers directly

**Current state:** The `Research ▾` dropdown shows Papers / 51 Definitions / Timeline / Protocol Matrix. Clicking "Research" as a top-level item does nothing (it just opens the dropdown).

**Change:** Make the top-level "Research" clickable — it should navigate to `agentic-economy-research.html` (the papers page). The dropdown still opens on hover for the sub-items.

**Pattern:**
```html
<div class="nav-group">
  <a href="agentic-economy-research.html" class="nav-group-link">Research ▾</a>
  <div class="dropdown">
    <a href="agentic-economy-research.html">Papers</a>
    <a href="agentic-economy-definitions.html">51 Definitions</a>
    <a href="agentic-economy-timeline.html">Timeline</a>
    <a href="agentic-economy-protocols.html">Protocol Matrix</a>
  </div>
</div>
```

Apply the same pattern to "Resources ▾" if it makes sense (it may not — decide based on whether there is a single obvious landing page for Resources).

**Files to edit:** Every HTML file with the site nav (search for `<nav class="site-nav">`).

**Acceptance criteria:** Clicking "Research" in the top menu navigates to the papers page. Dropdown still works on hover.

---

## 7. [P1] Same as §6 — already folded in

(Retained as placeholder so priority list numbering matches the original brief. See §6.)

---

## 8. [P0] First paper title — exact string replacement

**Current state:** `agentic-economy-research.html` line 832:
```
The Agentic Economy: A Taxonomy of 51 Definitions
```

**Change to exactly:**
```
Two Economies, Not One - A Taxonomy of the Agentic Economy and the Case for Settlement Neutrality
```

**Where to apply:**
- `agentic-economy-research.html` line 832 (the `<h2 class="paper-title">`)
- Any BibTeX entry on the same page (e.g. line 926 `title = {The Agentic Economy: A Taxonomy of 51 Definitions}`) → update to match.
- Meta description on that page if it mentions the old title.
- The `<title>` tag if it mentions the old title.
- Any `citation-label` with "Paper 1: The Taxonomy of 51 Definitions" → change to "Paper 1: Two Economies, Not One".

**CRITICAL:** Do not change the titles of Paper 2 ("Commerce Readiness Index for Agentic Economy Protocols") or Paper 3 ("The Oracle Problem in Agent-to-Agent Commerce"). **ONLY Paper 1.**

**Acceptance criteria:** `grep -r "Taxonomy of 51 Definitions" 03-Web/` returns zero matches in user-facing content. The new title appears consistently everywhere Paper 1 is referenced.

---

## 9. [P0] Menu level-2 collapses too fast

**Problem:** The `Research ▾` and `Resources ▾` dropdowns disappear the moment the mouse leaves the trigger, before the user can reach the sub-items.

**Root cause (likely):** The dropdown CSS uses `:hover` on the trigger only, with no hover-bridge and no delay.

**Fix:** Add a `transition-delay` on the hide side and a transparent bridge element between the trigger and the dropdown.

**Pattern:**
```css
.nav-group > .dropdown {
  display: none;
  /* existing styles */
}
.nav-group:hover > .dropdown,
.nav-group:focus-within > .dropdown {
  display: block;
}
/* Invisible bridge so the mouse can move from trigger to dropdown without leaving the hover region */
.nav-group > .dropdown::before {
  content: '';
  position: absolute;
  top: -12px;   /* height of the gap */
  left: 0;
  right: 0;
  height: 12px;
}
```

Also consider a small `transition` on `opacity` and `visibility` so the dropdown fades rather than snaps, which buys the user a few milliseconds of forgiveness.

**Acceptance criteria:** User can move mouse from "Research" to "51 Definitions" (sub-item) without the dropdown closing. Tested on Chrome, Firefox, Safari.

**Files to edit:** The shared CSS block in every page (or, if you refactor to an external stylesheet in §16, do it there once).

---

## 10. [P2] Infographic — rework `agentic-economy-infographic.html`

**Current state:** The infographic doesn't render well and doesn't land visually.

**Scope (decided):** Rework the whole page. The new visual approach is **TBD** — René will decide after you diagnose.

**First pass (investigation + proposal):**
1. Open `agentic-economy-infographic.html` and identify specifically what is broken:
   - Is it a layout issue (SVG not responsive)?
   - A data issue (numbers out of date vs. the corpus)?
   - A typography issue (font loading race)?
   - A "looks cheap" issue (generic bar charts, no visual hierarchy)?
2. Write a short diagnosis (max 200 words) as a comment block at the top of the file.
3. Propose **3 alternative visual approaches** as inline `<section class="proposal">` blocks that René can scroll through. Each proposal includes:
   - A one-line description of the visual metaphor.
   - A rough SVG mockup (can be low-fidelity).
   - The data source (canonical JSON fields used).
4. **DO NOT ship a final infographic yet.** Wait for René to pick one of the three proposals. Open a draft PR with the proposals as the deliverable.

**Design constraints for whichever approach is picked:**
- Uses `definitions-corpus.json` as the data source.
- Respects the design tokens (dark bg, `#34d399` accent).
- SVG or Canvas — no bitmap images.
- Annotated (every number is labeled), academic (no emoji, no cheesy gradients).
- Works at 375px mobile width.

**Acceptance criteria:** PR opened with 3 proposals + diagnosis. No final shipping decision without René's input.

---

## 11. [P2] BotNode is not entirely open source

**Current state:** Some pages market BotNode as open source. This is wrong — BotNode has proprietary components.

**Action:**
1. Grep for "BotNode" and "open source" within the same page:
   ```bash
   grep -rn "BotNode" 03-Web/ | grep -v "_archive"
   ```
2. For each hit, rewrite the surrounding copy. The correct framing is:
   > "BotNode is an experimental implementation ground for the ideas in this research. Parts of the VMP-1.0 specification are open (see [licensing](licensing.html)); the implementation itself contains proprietary components."
3. Where a page currently says something like "open source project BotNode" → change to "experimental project BotNode".
4. On the Paper 4 context (fiche `agentic-economy-def-botnode-vmp-10-c12.html`): the tone there should remain restrained and academic — BotNode is one entry in a 51-entry corpus, not a marketing opportunity. If the fiche's analytical note currently reads promotionally, leave it alone (it is generated from the canonical JSON and the voice is deliberately understated).

**Acceptance criteria:** No page implies that BotNode-as-a-whole is open source. The licensing page (§3) is the canonical source for what is and isn't open.

---

## 12. [P0] Profile / about page — "founder and researcher at AgenticEconomy.dev"

**File:** `about-agentic-economy.html`

**Changes:**

### 12.1 Bio line
Current: likely says "founder of BotNode" or similar.
New: exactly
> **René Dechamps Otamendi** — founder and researcher at AgenticEconomy.dev.

### 12.2 Add personal website link
Add a link to `https://renedechamps.com` in the profile's link list (near the ORCID link, LinkedIn, etc.).

### 12.3 Remove BotNode link from profile
Whatever link to `botnode.io` or `botnode.dev` currently appears in the profile → **remove it**. BotNode is experimentation, not the public identity. See also §13 which is a sharper version of this same rule applied site-wide.

### 12.4 ORCID anchor
Ensure the ORCID `0009-0007-1033-6519` is present and formatted as a link:
```html
<a href="https://orcid.org/0009-0007-1033-6519" rel="noopener">ORCID 0009-0007-1033-6519</a>
```

### 12.5 Publisher attribution in schema.org
Ensure the JSON-LD `Person` block on the about page uses:
```json
{
  "@type": "Person",
  "@id": "https://renedechamps.com/#person",
  "name": "René Dechamps Otamendi",
  "identifier": "https://orcid.org/0009-0007-1033-6519",
  "url": "https://renedechamps.com",
  "jobTitle": "Founder and researcher",
  "worksFor": { "@type": "Organization", "@id": "https://agenticeconomy.dev/#organization" }
}
```

**Acceptance criteria:** Bio matches the exact line above. Personal website link present. Zero references to BotNode on this page.

---

## 13. [P2] Remove BotNode from anywhere it appears as part of René's public identity

**Rule:** BotNode is the experimental ground; the public identity is AgenticEconomy.dev. BotNode should only appear in the site when it is necessary — i.e., on the single fiche `agentic-economy-def-botnode-vmp-10-c12.html` (which is a legitimate corpus entry) and nowhere else as a link from "me."

**Action:**
1. Grep for `botnode.io`, `botnode.dev`, `BotNode` across the whole site.
2. Classify each hit:
   - **Keep:** occurrences inside the BotNode/VMP-1.0 fiche (auto-generated, leave alone).
   - **Keep (reworded):** references in copy that describe the project factually as part of the corpus analysis.
   - **Remove:** any link from René's profile, bio, footer, sitemap, or "about" pages to botnode.io/.dev.
3. On `agentic-economy-research.html` and `index.html`, if BotNode appears as a "see also" or "our implementation" sidebar, remove or rework.
4. In `_headers`, `_redirects`, `sitemap.xml`, `llms.txt` — remove any BotNode-related canonicalization.

**Acceptance criteria:** `grep -ri "botnode" 03-Web/ | grep -v "_archive" | grep -v "botnode-vmp-10-c12"` returns ≤ 3 hits, and every remaining hit is a deliberate corpus-factual reference, not a profile link.

---

## 14. [P2] Vertical voids — global audit

**Problem:** Multiple pages have excessive vertical whitespace that makes them feel empty.

**Pages to audit (verified suspects from René):** `agentic-economy-101.html` (also covered in §5), `agentic-economy-research.html`, `index.html`, `agentic-economy-definitions.html`, `about-agentic-economy.html`.

**Method:**
1. For each page, take a screenshot at 1200×Full and at 375×Full.
2. Identify any stretch of ≥ 200 px of empty dark background between content blocks.
3. Tighten by:
   - Reducing section `padding` from e.g. `6rem 0` to `3.5rem 0` where appropriate.
   - Removing empty `<br>` tags.
   - Collapsing double `<hr>` or spacer divs.
   - Reducing hero min-height from `100vh` to `auto` with padding on pages where the hero is not a "landing" experience.
4. Keep the `index.html` hero at generous height — that page is the landing and can breathe. For all other pages, density over air.

**Acceptance criteria:** No single stretch of >200 px empty background between blocks on any audited page. Content feels dense without being cramped.

---

## 15. [P1] Contact form — no mailto, must send email

**Current state:** The contact section likely uses `mailto:` or doesn't exist.

**Decision (Netlify detected):** Use **Netlify Forms**. It is native to the deploy platform, free, requires zero backend code, and the setup is a single HTML attribute.

**Implementation:**

1. On the contact section (likely on `about-agentic-economy.html` or a new `contact.html`), add a form like:
   ```html
   <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="contact-form">
     <input type="hidden" name="form-name" value="contact">
     <p class="hidden-field"><label>Don't fill this out if you're human: <input name="bot-field"></label></p>

     <label for="name">Your name</label>
     <input id="name" type="text" name="name" required>

     <label for="email">Your email</label>
     <input id="email" type="email" name="email" required>

     <label for="subject">Subject</label>
     <input id="subject" type="text" name="subject">

     <label for="message">Message</label>
     <textarea id="message" name="message" rows="6" required></textarea>

     <button type="submit">Send</button>
   </form>
   ```

2. Style the form with the existing design tokens (dark bg inputs, accent border on focus, `Outfit` font).

3. In Netlify's dashboard, set up an email notification to René's address for new submissions. **Do NOT hardcode the email address in the HTML** — let Netlify handle routing.

4. Add a thank-you page `thanks.html` that the form redirects to on success:
   ```html
   <form action="/thanks" ...>
   ```

5. Remove any existing `mailto:` links and replace with a link to the contact form.

**Acceptance criteria:** Form exists, is styled, submits successfully to Netlify, shows a thank-you page. No `mailto:` in any user-facing CTA.

**Files:** Create `contact.html` (or section in about), create `thanks.html`, update any `mailto:` occurrences in existing files.

---

## 16. [P2] Global polish — consolidate shared CSS

**Observation:** Every fiche and every page inlines ~150 lines of identical CSS. This is a maintenance nightmare and the reason small tweaks explode into 100-file edits.

**Action (only if time permits, P2):**
1. Extract the shared CSS into `03-Web/style.css`.
2. Each HTML page imports it with a single `<link rel="stylesheet" href="/style.css">`.
3. Page-specific overrides stay inline.

**Caveat:** Do this **after** all other fixes land. It is a separate PR and deserves careful testing — one wrong selector and every page breaks.

**Acceptance criteria:** If done, all pages render identically before/after. No visual regression.

---

## Validation — run these before opening the PR

From the repository root:

```bash
# 1. No broken internal links
for f in 03-Web/*.html; do
  grep -oP 'href="(?!http|mailto|#)[^"]+"' "$f" | while read link; do
    path=$(echo "$link" | sed 's/href="//;s/"$//')
    target="03-Web/$path"
    if [ ! -f "$target" ]; then
      echo "BROKEN in $f: $link"
    fi
  done
done

# 2. No "peer-reviewed" leftovers in user-facing content
grep -rni "peer-reviewed" 03-Web/ | grep -v "_archive"

# 3. No "Taxonomy of 51 Definitions" leftovers
grep -rn "Taxonomy of 51 Definitions" 03-Web/

# 4. No mailto: in user-facing content
grep -rn "mailto:" 03-Web/ | grep -v "_archive"

# 5. No BotNode profile leakage
grep -ri "botnode" 03-Web/ | grep -v "_archive" | grep -v "botnode-vmp-10-c12"

# 6. Favicon present
ls 03-Web/favicon.ico 03-Web/favicon.svg 03-Web/apple-touch-icon.png

# 7. Legal pages present
ls 03-Web/privacy.html 03-Web/terms.html 03-Web/licensing.html

# 8. HTML validates (if validator available)
# html5validator --root 03-Web/ --show-warnings

# 9. No empty-space regressions (manual — screenshot diff)
```

---

## PR structure

Open one PR per priority group:

- **PR 1 — P0:** §1 hero, §2 preprints label, §8 first paper title, §9 menu hover, §12 profile
- **PR 2 — P1:** §3 legal pages, §4 favicon, §5 101 page, §6-7 top menu, §15 contact form
- **PR 3 — P2:** §10 infographic (proposals only), §11 BotNode positioning, §13 BotNode profile removal, §14 vertical voids, §16 CSS consolidation

Each PR description must include:
- What sections it covers (by number from this brief)
- Any decisions taken that are not 1:1 with the brief
- Any TODOs left for René (e.g. `[JURISDICTION TBD]` on terms.html)
- Screenshots of before/after for visual changes
- The validation commands from above with their output

---

## Questions Claude Code should flag back to René (do NOT guess — ask)

1. **Terms jurisdiction** (§3): Spain or Belgium? Leave `[JURISDICTION TBD]` until René answers.
2. **Site code license** (§3): MIT or All Rights Reserved? Default to "All Rights Reserved" until confirmed.
3. **Infographic direction** (§10): after you ship the 3 proposals, which one?
4. **Netlify dashboard access** (§15): René needs to wire the form notification email. Claude Code cannot do this from the repo.
5. **Archive directory** (generic): if `03-Web/_archive/` does not exist yet, create it before moving anything.

---

## Out of scope for this brief

These are **not** part of this web fixes brief and should NOT be touched:
- The Paper 4 annex content (managed via `definitions-corpus.json` + `build_fiches.js` in the parent working directory).
- The canonical JSON corpus — do not hand-edit.
- The 51 fiches — they are auto-generated; changes must go through the JSON.
- Zenodo metadata, arXiv submissions, preprint PDFs.
- BotNode's own site (`botnode.io`). That is a separate codebase.
- Any mention of pending migrations (Gemma 4, Mac Mini services, etc.).

---

**End of brief.** If anything is unclear, stop and ask René before improvising. The priority order exists for a reason — P0 items block the credibility of the site and must land first.
