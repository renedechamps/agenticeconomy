# renedechamps.com — Pivot Audit (BotNode → AgenticEconomy.dev)

**Author of audit:** Claude · 2026-05-07
**Site audited:** `https://renedechamps.com` (homepage + `/about/`)
**Pivot policy reference:** memory `feedback_signature_identity.md` — *"René signs as AgenticEconomy.dev, NOT BotNode; BotNode is experimental only."*
**Companion memory:** `reference_botnode_api.md` — *"botnode.io is the live VMP-1.0 platform with 55+ endpoints; NOT a Mac Mini service."* — i.e. BotNode is real, but it is **one experimental implementation of the AgenticEconomy.dev research stack**, not the magnum opus.

---

## 0. TL;DR

The personal site currently treats **BotNode as the climax of the career arc** and AgenticEconomy.dev as a footnote (one mention, near the end of the About page, framed as the place where "the research" lives). The pivot inverts that hierarchy:

- **AgenticEconomy.dev** = the public-facing identity. Independent research hub. Author of (now) five papers. Open-access, CC BY-SA, ORCID-anchored. This is where the body of work lives and where credibility is built.
- **BotNode** = one experimental implementation of the framework defined by the papers. Reference build of VMP-1.0. Useful, real, demonstrable — but **not the headline**. It's Chapter~12, not the whole book.

There are roughly **18 substantive copy changes** across two pages, plus an **architectural rebalance** of the personal narrative on `/about/`. None of the historical chapters (OX2, Mind Your Group, BBVA, etc.) need to change.

**Severity legend** below:
- **P0 — Breaks credibility now.** Fix before any new outreach.
- **P1 — Quietly damaging.** Fix this week.
- **P2 — Stylistic.** Fix on next general site refresh.

---

## 1. The pivot in one paragraph (for René to internalize before editing)

> Until late 2025, BotNode was the headline because the papers didn't exist yet and the live platform was the only proof of work. Since March 2026 that has inverted: four papers are on Zenodo (and now on arXiv), Paper 5 is shipped (May 2026), Paper 6 is in concept, and there is a documented research series, a multilingual editorial catalogue, an independence disclosure, and a commercial offering grounded in the framework. BotNode is now the **reference implementation** of one corner of that framework — the C12 entry in Paper 4's corpus of fifty-one definitions. The personal site needs to tell the same story the rest of the catalogue already tells: René is the **author of the AgenticEconomy.dev research series**, the experimental builder of BotNode, and a serial entrepreneur whose seventh construction is the research hub itself.

---

## 2. Page-by-page audit

### 2.1  Homepage `/` — six fixes

#### F-01 · "Now Building / Built · Live: BotNode™" card  **(P0)**

**Current copy** (homepage, "Now Building" section):

> **Built · Live**
> **BotNode™**
> I built the missing piece. Verification before payment. Quantitative reputation. Machine-native currency. Open source. Three academic papers with permanent DOIs back the architecture. Live at botnode.io.

**Why it breaks now.** Frames BotNode as *the* missing piece and the papers as *backing the architecture*. Reality is the inverse: the papers **define** the architecture (six primitives, settlement neutrality, oracle problem, definitional taxonomy, KYA conformance); BotNode is one reference implementation that probes the same architecture from the inside. With Paper 5 published, the "three papers" line is also factually stale.

**Proposed replacement copy:**

> **Now Building**
> **AgenticEconomy.dev**
> Independent research hub on the engineering and economic foundations of agent commerce. Five open-access papers (March–May 2026) on reputation, taxonomy, the Oracle Problem, definitional convergence, and Know Your Agent. CC BY-SA 4.0. ORCID 0009-0007-1033-6519. Live at **agenticeconomy.dev**.
>
> **Reference build · BotNode™**
> One experimental implementation of the framework. Verification before payment, quantitative reputation, machine-native currency. Open-source protocol, proprietary grid. Used as the C12 case study in Paper 4. Live at **botnode.io**.

Two cards instead of one; AgenticEconomy.dev is the larger card, BotNode the smaller. Both real, both linked, hierarchy explicit.

---

#### F-02 · Page `<title>` and meta description  **(P1)**

**Current title:** `René Dechamps Otamendi | Serial Entrepreneur and Builder`

That's fine but undersells the current chapter. Suggest:

> `René Dechamps Otamendi | AgenticEconomy.dev · Serial Builder, Independent Researcher`

Meta description (suggested, ~155 chars):

> `Serial entrepreneur (7 companies, 1 exit) and independent researcher behind AgenticEconomy.dev — five open-access papers on agent commerce. Belgian-Spanish.`

---

#### F-03 · Hero line "Same pattern. Bigger pieces."  **(P2)**

Keep. This still works.

Optional micro-edit to the subline:

> Current: *"Belgian-Spanish · Serial builder · 7 companies · 1 exit"*
> Suggested: *"Belgian-Spanish · Serial builder · 7 companies · 1 exit · Now: AgenticEconomy.dev"*

Adds the current chapter without breaking the rhythm.

---

#### F-04 · The "Writing > Selected Writing" list  **(P1)**

The 2026 entry currently reads:

> **2026 — I Built the Missing Piece of the Agent Economy** — *agentic economy*

This is the personal-essay version of the BotNode origin story. It should stay (it's a real piece of writing and tells a true story) but it should not be the **only** 2026 entry. With five papers and a Field Report shipped, the list is misrepresenting the year.

**Proposed Writing additions (newest at top):**

| Year | Title | Tag |
|------|-------|-----|
| 2026 | Paper 5 — Know Your Agent: Six Primitives for Identity, Authority, and Liability | research |
| 2026 | Paper 4 — Fifty-One Maps, No Territory (diagnostic of the field) | research |
| 2026 | Field Report N°1 — A Policymaker's Guide to the Agentic Economy (EU) | policy |
| 2026 | Trilogy — CRI / Two Economies / The Oracle Problem | research |
| 2026 | I Built the Missing Piece of the Agent Economy *(personal essay)* | agentic economy |
| 2013 | The Lego Entrepreneur vs.\ the Playmobil Entrepreneur | entrepreneurship |
| 2009 | NextStage Predicts Gender and Age | data science |
| 2007 | NeuroMarketing, Web Analytics & Ethics | privacy & ethics |
| 2007 | Four Gurus For You (4G4U) | web analytics |
| 2006 | Web Analytics Journey Index (WAJ) | web analytics |
| 2020 | My Early Days on the Internet and the Sale of My First Digital Agency | entrepreneurship |

Each new 2026 entry links to the canonical hub page on agenticeconomy.dev (`/papers/paper-5-kya`, `/paper-4-maps`, `/papers/`, `/field-reports/eu-001`, etc.). The personal essay stays at `renedechamps.com/i-built-the-missing-piece-…` but is no longer **alone** in 2026.

---

#### F-05 · The "Now Building" / "Before That" framing  **(P0)**

Right now the homepage architecture is:

```
Now Building
  └── Built · Live · BotNode™

Before That · Other Constructions
  └── OX2  ·  Mind Your Group  ·  Neo@Ogilvy  ·  BBVA
```

After pivot:

```
Now Building
  ├── AgenticEconomy.dev  (research hub, 5 papers, public-facing identity)
  └── BotNode™            (reference build, experimental)

Before That · Other Constructions
  └── OX2  ·  Mind Your Group  ·  Neo@Ogilvy  ·  BBVA
```

That's the structural change. Visual implementation: keep the existing card system but make the "Now Building" column hold **two** cards, with AgenticEconomy.dev visually dominant (larger, top) and BotNode subordinate (smaller, below or adjacent).

---

#### F-06 · Footer / colophon  **(P2)**

If the homepage carries a footer with social links and the canonical author block, ensure:

- ORCID 0009-0007-1033-6519 is hyperlinked.
- An `agenticeconomy.dev` link appears alongside `botnode.io` (not after it; same line or before).
- License note (e.g. "Personal site CC BY 4.0; research at agenticeconomy.dev under CC BY-SA 4.0") is added if not present.

---

### 2.2  About page `/about/` — six fixes

The About page is a long-form personal narrative organized into 14 chapters. Most of it does **not** need to change — chapters 01–11 are the personal history (kitchen, Lego, candy stand, Geneva, drama school, OX2, exit, NextStage, Mind Your Group, BBVA, divorce). Leave them as is.

The pivot work is concentrated in **Chapters 12, 13 and 14**.

#### F-07 · Chapter 12 title and framing  **(P0)**

**Current:**

> **Chapter 12 — BotNode™: The Trust Layer for the Agentic Web**

This positions BotNode as the climactic construction. After pivot, the chapter should pivot one level up — the **construction** that matters is the research hub plus the experimental platform together, not BotNode alone.

**Proposed new title:**

> **Chapter 12 — The Seventh Construction: AgenticEconomy.dev**

**Proposed new opening** (replacing the first paragraph of current Chapter 12):

> What I built is not an AI tool. Not a payment platform. Not a startup. It is a research hub and a reference build, designed together so that one publishes what the other proves.
>
> AgenticEconomy.dev is the public side: five open-access papers between March and May 2026, an independence disclosure, a CC BY-SA license, an ORCID, a Zenodo community, and an editorial cadence I built to outlive any single piece of work.
>
> BotNode is the experimental side: a live grid for autonomous agents — escrow, schema validation, CRI reputation, settlement receipts before payment release — used inside the research to probe the architecture from the inside. It is one of fifty-one definitions of the agentic economy I catalogued in Paper 4 (entry C12, settlement-neutral). It is the only one I happen to be running.

Then the rest of the current Chapter 12 (the "three pieces were needed" deep dive on Verification, Reputation, Currency, and the $TCK / Law V / CRI / Biological Overhead passages) can stay — but reframed as **"how BotNode probes the framework"** rather than **"BotNode is the framework"**.

A small but symbolic edit: the BotNode taglines ("BotNode is the trust layer," "BotNode is building the roads") are great as historical quotes but should now appear inside quotation marks with light past-tense framing — *"At the time I was writing the Bluepaper, I summarized it as: the entire AI industry is building faster horses. BotNode is building the roads."* Reads as a moment in the narrative, not a current marketing claim.

---

#### F-08 · The "three papers" count  **(P0)**

Inside Chapter 12 there's the line:

> *"Three academic papers back the architecture — published with permanent DOIs: a multi-factor reputation system with Sybil resistance analysis, a taxonomy of 50+ definitions of the Agentic Economy across 8 protocols, and a formal analysis of why automated quality verification is mathematically impossible."*

Stale. After Paper 4 (April) and Paper 5 (May) this should read:

> *"Five academic papers back the architecture, all open-access on Zenodo with permanent DOIs: the trilogy on reputation (CRI), taxonomy (Two Economies), and verification (The Oracle Problem) in March; a diagnostic of the field (Fifty-One Maps, No Territory) in April; and a six-primitive framework for Know Your Agent in May. Forty-plus pages each, peer-style methodology, every claim independently citable."*

Update the supporting clause ("39 pages, 62 references, five Nobel laureates cited") to match the new count.

---

#### F-09 · The single mention of AgenticEconomy.dev  **(P0)**

Currently the site mentions AgenticEconomy.dev exactly once, deep inside Chapter 12:

> *"The research is at agenticeconomy.dev/research/."*

That's it. Buried, almost throwaway. After pivot, AgenticEconomy.dev should appear:

1. In the homepage "Now Building" card (F-01).
2. In the homepage hero subtitle (F-03 optional).
3. In the About page Chapter 12 retitled (F-07).
4. In the closing paragraph of the About page (new sentence; see F-11 below).
5. In the footer / colophon (F-06).
6. As the destination for Paper 4 and Paper 5 entries in the Writing list (F-04).

Six locations, not one. The rule: any reader who lands on any internal page should encounter the agenticeconomy.dev URL within one scroll.

---

#### F-10 · Chapter 13 — "The Next Construction"  **(P1)**

Current Chapter 13:

> **Chapter 13 — The Next Construction**
> *Since November 2025, I've been building something else — quietly, in parallel. It sits at the intersection of three worlds I know well — each from a different angle, each with scars. It is the most personal thing I have ever built. The technology is only part of it. The rest is harder to name and belongs to a different kind of telling.*
>
> *For now: the pieces are in place. The construction isn't ready to be seen. When it is, it will speak for itself.*

This currently reads like a teaser for something **after** BotNode — but the BotNode framing in Chapter 12 was already framed as the climax. So Chapter 13 doesn't quite have a job.

**Two options:**

- **Option A (recommended).** Repurpose Chapter 13 as the chapter where AgenticEconomy.dev gets named explicitly as the seventh construction, complementing the BotNode build of Chapter 12. Move the "something quietly, in parallel" teaser to a new Chapter 14 or fold it into the closing. Title: *"Chapter 13 — The Research Hub: AgenticEconomy.dev"*.
- **Option B.** Leave Chapter 13 as a deliberate teaser, but add a one-line preface: *"This is not BotNode. BotNode is alive and documented at botnode.io. This is the thing that comes after."*

Either way: keep the tease alive, but stop the reader assuming the climax is BotNode.

---

#### F-11 · Closing — Chapter 14 "The Method, After the Story"  **(P1)**

The final chapter currently closes with the Lego metaphor and "if your sister tells you to spend the money — tell her you can't. You need the pieces for the next one." Good. Don't touch the cadence.

But add **one sentence** before that closing, positioned just after the "Look at what's missing. Feel which pieces belong together. Build the thing." beat:

> *And when the thing you build is also a piece of work for the rest of the field — publish it open, sign it with your ORCID, and let it outlive any single company.*

That line links the construction method to AgenticEconomy.dev without saying "AgenticEconomy.dev." It's a values statement: open-access, citable, durable. The reader who's reached Chapter 14 will know where to look.

---

#### F-12 · "29 skills ready at launch / Protocol open source / Grid proprietary"  **(P2)**

Inside Chapter 12, BotNode-specific operational facts. Two issues:

- *"29 skills"* — verify against current `botnode.io` state. The number may have moved. If the live count is different, update; if not, leave but date it ("at v1.0 launch, March 2026").
- *"Protocol open source. Grid proprietary."* — confirm this is still the licensing posture for BotNode. If yes, leave. If the platform pivoted to fully open or fully closed, update.

This isn't a pivot issue per se — it's just "fact-check before the next site deploy."

---

### 2.3  Linked essay  `/i-built-the-missing-piece-…/`  **(needs separate audit)**

When I tried to load the article URL directly, it redirected to the homepage — I couldn't read the body. The article is still listed under Writing and presumably linked from the homepage. Two possibilities:

1. The article exists at a slightly different slug than the one I guessed. Verify and re-audit. Most likely needs the same Chapter-12 treatment: keep the personal-essay framing intact, but in the **closing or addendum**, add a one-paragraph "what changed since I wrote this": *"This essay was written in early 2026, before the research hub crystallized. The work it described — BotNode — is alive at botnode.io. The framework it implements is now documented across five papers at agenticeconomy.dev."*
2. The article was removed or hidden. If so: no action needed, but flag the broken link from the Writing list on the homepage.

**Action item for René:** confirm the article URL, then redo this audit row.

---

### 2.4  Other internal pages — likely fine, worth checking

I only navigated to the homepage and the about page in this audit. The following might exist and should be sampled:

- `/contact/` — email, social, ensure agenticeconomy.dev is the primary professional handle.
- `/lego-entrepreneur/` or `/playmobil-entrepreneur/` (the 2013 essay) — likely fine; pre-dates the pivot.
- `/web-analytics-journey-index/` (the 2006 essay) — historical, leave alone.
- Any `/research/` or `/papers/` redirect — should 301 to `agenticeconomy.dev/papers/` if it exists; if not, ignore.

Not blocking. Sample on next pass.

---

## 3. Find-and-replace table (concrete strings)

For Claude Code or whoever is editing the templates:

| Where | Find | Replace |
|---|---|---|
| Homepage hero subtitle | `Belgian-Spanish · Serial builder · 7 companies · 1 exit` | `Belgian-Spanish · Serial builder · 7 companies · 1 exit · Now: AgenticEconomy.dev` |
| Homepage "Now Building" card | `Built · Live` heading + `BotNode™` + body para | Two cards: `AgenticEconomy.dev` (research hub, 5 papers) primary; `BotNode™` (reference build) secondary. Body copy in §2.1 F-01. |
| Homepage Writing list | `2026 — I Built the Missing Piece of the Agent Economy` as the only 2026 entry | Add Papers 1–5, Field Report N°1; keep personal essay as one of six 2026 entries. See §2.1 F-04 table. |
| Homepage `<title>` | `René Dechamps Otamendi \| Serial Entrepreneur and Builder` | `René Dechamps Otamendi \| AgenticEconomy.dev · Serial Builder, Independent Researcher` |
| Homepage meta description | (current, whatever it is) | `Serial entrepreneur (7 companies, 1 exit) and independent researcher behind AgenticEconomy.dev — five open-access papers on agent commerce. Belgian-Spanish.` |
| About Ch.12 title | `Chapter 12 — BotNode™: The Trust Layer for the Agentic Web` | `Chapter 12 — The Seventh Construction: AgenticEconomy.dev` |
| About Ch.12 opening | `What I built is not an AI tool. Not a payment platform. Infrastructure — the missing layer ...` (full first paragraph) | Replacement paragraph in §2.2 F-07 above. |
| About Ch.12 "Three academic papers ..." | `Three academic papers back the architecture — published with permanent DOIs: a multi-factor reputation system ..., a taxonomy ..., and a formal analysis ...` | `Five academic papers back the architecture, all open-access on Zenodo with permanent DOIs: the trilogy on reputation, taxonomy and verification in March; a diagnostic of the field in April; and a six-primitive framework for Know Your Agent in May.` |
| About Ch.12 paper-count clause | `39 pages, 62 references, five Nobel laureates cited` | Update to reflect cumulative count across five papers, or simply drop the specific page-count line. |
| About Ch.12 closing line | `We are not being replaced — we are being promoted from operators to founders ...` | Keep verbatim — this is good personal-essay closing. |
| About Ch.13 title | `Chapter 13 — The Next Construction` | Per Option A: `Chapter 13 — The Research Hub: AgenticEconomy.dev` (with new body — see §2.2 F-10) |
| About Ch.14 — before "Look at what's missing" line | (no insertion) | Add new sentence: `And when the thing you build is also a piece of work for the rest of the field — publish it open, sign it with your ORCID, and let it outlive any single company.` |
| Footer (if present) | `botnode.io` link only | `agenticeconomy.dev` link first, `botnode.io` link second; ORCID hyperlinked. |

---

## 4. New content to commission (Claude Code / writing pass)

These are net-new pieces that don't exist on the site yet:

1. **A `/research/` redirect or landing page** on `renedechamps.com` that 301-forwards to `agenticeconomy.dev/papers/`. Cheap, semantic, helps anyone who lands on the site looking for the research.
2. **A small "Five Papers, Free to Cite" callout box** somewhere on the homepage (could be in the Writing section, could be a sidebar): list of the five papers with DOIs. The trilogy + Paper 4 + Paper 5. Each linked to its hub page.
3. **An updated headshot caption or one-liner** for the hero — currently the site is mostly text. If there's a hero photo, the caption should now read something like *"René Dechamps Otamendi · AgenticEconomy.dev"* rather than just the name. (Cosmetic; P2.)

---

## 5. SEO and structured-data pass (separate, P2)

If the site uses JSON-LD `Person` or `ProfilePage` schema:

- Ensure `Person.identifier` includes the ORCID URI.
- Ensure `Person.affiliation` lists `AgenticEconomy.dev`.
- Ensure `Person.knowsAbout` lists the five paper topics (reputation systems, multi-agent systems, agent commerce, settlement neutrality, Know Your Agent, definitional analysis).
- Ensure `Person.author` lists the five papers as `ScholarlyArticle` entries with DOIs (or `sameAs` URIs pointing at Zenodo).

This is a separate sweep; out of scope for the copy edits above. Mention it to Claude Code when the next web-fixes brief is built.

---

## 6. What NOT to change

Belt-and-suspenders list — these are good as they are and should not be touched:

- The hero "Same pattern. Bigger pieces." line. Strong.
- The "7 / 13 / 17 / 20 / 27 / 32" age-anchored timeline of early constructions on the homepage. Iconic, doesn't need updates.
- Chapters 01–11 of the About page (kitchen, Lego, candy stand, Geneva, drama school, OX2 founding, exit, NextStage, Mind Your Group, BBVA, divorce). These are the personal history. Out of scope for the pivot.
- The 7 values block (No Ego, Honesty & Transparency, Accountability, Customer Focus, Resilience, Excellence, Passion). These crystallized at OX2 and stand.
- The Eurovision 1993, Death of a Salesman, beer-tray-at-the-bar anecdotes. Brand-defining colour.
- Existing testimonials from Avinash Kaushik, Jim Sterne, Eric Peterson, Stéphane Hamel, Blair Reeves, Oliver Schiffers, etc. These are about past constructions and are fine.
- The "Lego apart, take the pieces, next construction" metaphor as the closing of Chapter 14.

---

## 7. Priority sequence (one weekend of editing)

| Order | Item | Severity | Effort |
|---|---|---|---|
| 1 | F-01 Homepage "Now Building" card → two cards (AE.dev primary, BotNode secondary) | P0 | 30 min copy + 30 min layout |
| 2 | F-07 About Ch.12 retitled and re-opened | P0 | 45 min copy |
| 3 | F-08 "Three papers" → "Five papers" everywhere | P0 | 15 min find-and-replace |
| 4 | F-09 Make sure agenticeconomy.dev appears on every internal page within one scroll | P0 | 30 min |
| 5 | F-04 Writing list — add Papers 1–5 + Field Report N°1, demote personal essay to one entry of six | P1 | 30 min |
| 6 | F-10 Chapter 13 retitled (Option A) | P1 | 30 min copy |
| 7 | F-11 Closing addition in Chapter 14 | P1 | 5 min copy |
| 8 | F-02 `<title>` + meta description | P1 | 5 min |
| 9 | F-06 Footer / colophon adjusted | P2 | 15 min |
| 10 | F-12 BotNode operational facts (skill count, licensing) fact-check | P2 | 15 min verify |
| 11 | F-03 Hero subtitle micro-edit | P2 | 2 min |
| 12 | Section §4 new-content items (research redirect, papers callout, hero caption) | P2 | 1–2 hours |
| 13 | Section §5 SEO / JSON-LD | P2 | separate sweep |

Total estimated time for P0+P1: **~4 hours of careful copy work**. P2 layer is another **~3 hours**.

---

## 8. Sample DM / LinkedIn post once the pivot is done

For when the edits ship and you want to announce the new framing without making it sound like a relaunch:

> *I rebuilt my site to match the work. AgenticEconomy.dev — independent research hub, five open-access papers on agent commerce — is now the front page. BotNode, the experimental reference build I keep talking about, is one corner of that work. Same person, sharper picture.*
>
> `agenticeconomy.dev` · `renedechamps.com`

Short, no fanfare, signals exactly the inversion this audit is about.

---

## 9. What I could not audit (caveats)

- The article at `/i-built-the-missing-piece-…/` redirected to home; could not read body. Action item: verify URL and re-audit. (§2.3)
- No internal pages beyond home + about were sampled. `/contact/`, individual blog post URLs, and any `/research` or `/papers` slugs need a P2-level pass.
- I could not see whether the site has any structured data (JSON-LD). The SEO section (§5) is a recommendation based on the standard `Person` schema used by other AgenticEconomy.dev properties; verify before applying.
- The actual hero image / headshot (if any) on the homepage is not described here. If there's a tagline overlay on it, update that too — `AgenticEconomy.dev` should appear next to the name.

---

## 10. Provenance and sources for this audit

- Site read: `https://renedechamps.com/` and `https://renedechamps.com/about/`, fetched 2026-05-07 via Claude in Chrome.
- Pivot policy: memory `feedback_signature_identity.md` (2026-04-21 entry).
- Paper count and titles: memories `reference_research_papers.md`, `project_paper_4_status.md`, `project_paper_dates.md`, and current state of `/AgenticEconomy/01-Papers/`.
- BotNode positioning: memory `reference_botnode_api.md` (BotNode = live VMP-1.0 platform, one experimental implementation).

---

*Audit v1 · 2026-05-07 · `/AgenticEconomy/03-Web/renedechamps-com-pivot-audit.md`*
