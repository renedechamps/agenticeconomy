# Claude Code Brief — Commercial Contact Page

**File to edit:** `about-agentic-economy.html` (section `<!-- Section 6: Contact -->`, currently around line 1096)
**Related files:** `_redirects`, possibly new `netlify/functions/contact.js` (or Netlify Forms — see below)
**Priority:** High. Ships alongside Digest #1 launch (2026-04-21).
**Why this exists:** Digest #1 ends with a commercial CTA pointing people here. Right now the form is friendly but revenue-invisible — no commercial intent signal, no routing, no delivery. This brief turns it into the top of a commercial funnel.

---

## Goal

Convert the contact page from "polite inquiry form" into a "money-driven intake form" that:

1. **Signals commercial availability** without making the page feel like a sales landing.
2. **Segments incoming requests** so high-intent leads surface immediately.
3. **Delivers every submission to two inboxes** so René never misses one.

Tone stays operator, not corporate. This is not a lead-gen funnel with qualifying quizzes. It is a cleaner intake form that *mentions* the commercial options exist.

---

## Required changes

### 1. Dropdown — replace options

Current options (remove all of them):
- Research Inquiry
- Contribute a definition or protocol
- Press & Speaking
- Other

New options (in this exact order — commercial first, contribution last):

```html
<option value="Advisory retainer">Advisory retainer (monthly)</option>
<option value="Commissioned research">Commissioned research</option>
<option value="Research inquiry / press">Research inquiry / press</option>
<option value="Contribute a definition or protocol">Contribute a definition or protocol</option>
<option value="Other">Other</option>
```

Ordering is deliberate — the first thing a reader sees is the commercial option. Do not reorder alphabetically. Do not add Speaking or Advisor-equity options (those come in Q3).

### 2. Short commercial intro above the form

Just above `<h2>Get in Touch</h2>`, add a tight intro paragraph. Match the existing operator-voice register used elsewhere on the site. Proposed copy (lightly edit for voice consistency if needed):

> I take **three advisory engagements per quarter** with operators, investors, and policy teams building in agentic commerce. Standing monthly retainer, deep on taxonomy, protocol selection, and regulatory positioning. Also open to commissioned research. For press, contributions, or anything else, the same form works.

Style: no bullet list, one paragraph. Keep it under 60 words. Bold only on the "three advisory engagements per quarter" fragment.

### 3. Anchor linkability

The Digest links to `agenticeconomy.dev/about-agentic-economy#contact`. Verify the contact `<section>` has `id="contact"`. If not, add it.

### 4. Remove placeholder names in inputs

Replace `placeholder="Jane Smith"` and `placeholder="jane@example.com"` with something less American-generic — e.g. `placeholder="Name"` and `placeholder="email@domain.com"`. Minor, but this is a European-based researcher's page.

### 5. (Optional, nice-to-have) Subtle "Current availability" line

Below the dropdown, small muted text: *"Current availability: Q3 2026."*
Only if it fits visually — do not disrupt the form flow. Skip if unclear.

---

## Email delivery — the critical part

The form currently posts to `/api/contact`. **There is no backend.** Submissions go nowhere. This must be fixed.

### Recipients (both, every submission)

- **Primary:** `rene@renedechamps.com` — To:
- **Copy:** `renator@gmail.com` — Cc:

Both addresses must receive every submission. Do not use BCC for `renator@gmail.com` — use Cc so René can reply-all from either inbox and keep a visible paper trail.

### Recommended implementation — Netlify Forms

This site is on Netlify (`_redirects` and `_headers` confirm). The cleanest path is **Netlify Forms** — zero backend code, built-in spam filtering, email notifications.

Steps:

1. Add `data-netlify="true"` and `name="contact"` to the `<form>` element.
2. Add a hidden honeypot field (already exists as `bot-field` — confirm it's wired correctly: the form tag needs `netlify-honeypot="bot-field"`).
3. Remove `action="/api/contact"` — Netlify intercepts the POST at the edge.
4. In Netlify dashboard (or via `netlify.toml`), configure form notifications to send to **both** `rene@renedechamps.com` and `renator@gmail.com`.
5. Netlify Forms free tier = 100 submissions/month. Fine for now. If we outgrow it, switch to a Netlify Function.

**Alternative if Netlify Forms has any constraint (e.g. subject-based routing needed later):** write `netlify/functions/contact.js` that receives the POST and sends email via Resend, Postmark, or SendGrid to both recipients. But do not over-engineer this now — Netlify Forms first.

### Email subject line format

When the notification email is generated, the subject should include the selected dropdown value so René can triage on his phone without opening:

```
[AgenticEconomy.dev] {Subject dropdown value} — {Sender name}
```

Example: `[AgenticEconomy.dev] Advisory retainer — Priya Shah`

### Auto-reply to sender

Add a simple auto-reply so senders know the message landed. Keep it honest and human:

> Thanks — this landed in my inbox. I reply to every message personally, usually within 2 business days. If it's commercial (advisory, research), I triage first.
> — René

Sent from `rene@renedechamps.com`. Plain text, no HTML styling.

---

## Testing checklist

Before closing the PR:

- [ ] Submit the form with each dropdown value — 5 submissions total.
- [ ] Confirm both `rene@renedechamps.com` and `renator@gmail.com` received all 5.
- [ ] Confirm subject line format is correct.
- [ ] Confirm sender received the auto-reply.
- [ ] Click `agenticeconomy.dev/about-agentic-economy#contact` from a fresh tab — anchor must scroll to the contact section.
- [ ] Test the honeypot: fill `bot-field` in DevTools — Netlify should reject.
- [ ] Check mobile layout — the new intro paragraph should not break the form card.

---

## Out of scope — do not do

- Do not add Speaking, Podcast, Event, or Advisor-equity options to the dropdown.
- Do not add a Calendly embed or calendar booking widget.
- Do not add tier pricing ("Starting at €X/month") anywhere on the page.
- Do not add testimonials or client logos.
- Do not remove the Contribution or Other options — those still matter.

This brief is narrow on purpose. Commercial options on the dropdown will evolve as the business model does; we will revisit in Q3.

---

## Deliverables

1. Updated `about-agentic-economy.html` with new dropdown, intro paragraph, and anchor id.
2. Netlify Forms wiring (form attributes + notification config).
3. Auto-reply configured.
4. Short PR description confirming all test checkboxes pass, plus a screenshot of one test notification email arriving in both inboxes.

---

**Questions or ambiguity?** Default to the operator-voice, minimalist aesthetic already established on the rest of the site. When in doubt, fewer words.
