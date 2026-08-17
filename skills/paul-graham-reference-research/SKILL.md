---
name: paul-graham-reference-research
description: Explore and verify public Paul Graham books, Arc, Bel, Lisp, Spam, Responses, FAQs, RAQs, Quotes, RSS, Bio, and Email pages through the Codex in-app browser. Use when the user asks for a Paul Graham reference page, project resource, book metadata, FAQ route, quote lookup, biography, feed explanation, or contact guidance.
---

# Paul Graham References

## Purpose and entry point

Use this skill for non-Essay reference and project pages on `https://paulgraham.com/`. Start from the already-open Codex in-app browser tab, or return to the site's visible home navigation. Do not use Chrome, an external browser, web search, a CLI, an API, a scraper, or stored session data. Read [the site map](../../sites/paul-graham/references/site-map.md) and [the interaction rules](../../sites/paul-graham/references/interaction-rules.md) before following an unfamiliar branch.

## Route by intent

- Book list or book metadata → `/books.html` → visible book card → a detail page such as `/hackpaint.html`.
- Arc resources → `/arc.html`; follow visible internal child pages or record external Forum, Tutorial, or installation links without opening them unless requested.
- Bel language resources → `/bel.html`; follow the visible guide, source, or examples link when the user asks to read it. Treat CDN query parameters as ephemeral and do not persist them.
- Lisp history, code, links, quotes, or FAQ → `/lisp.html` → the visible topic page.
- Spam research or FAQ → `/antispam.html` → the visible article, FAQ, research, resource, archive, or link page.
- Responses → `/kedrosky.html` → the visible response page.
- Frequently asked questions → `/faq.html` → the requested FAQ family (`gfaq.html`, `pfaq.html`, `startupfaq.html`, `arcfaq.html`, `lispfaq1.html`, `vwfaq.html`, `spamfaq.html`, or `ffbfaq.html`).
- Rarely asked questions → `/raq.html`; read the long-form page and follow only visible same-site links.
- Quotes → `/quo.html`; read current entries and sources; do not assume a search or filter exists.
- RSS explanation → `/rss.html`; distinguish the page's explanation from the external feed, which was not explored in this skill.
- Biography → `/bio.html`; verify the current visible biography and image/source note.
- Contact guidance → `/info.html`; report the instructions only. Never send an email on the user's behalf.

## Procedure

1. Inspect the current tab, URL, title, visible entry labels, and authentication state. This site was observed as public; do not request credentials or inspect session storage.
2. Open the narrowest hub route using a visible same-site link or the route map. Confirm the hub title and the requested section before following one representative child link.
3. For a detail page, record the stable fields visible in the page: title, description, date/year, publisher/pages/ISBN when present, internal links, and external link labels. Do not copy current quotes, counts, timestamps, tokenized URLs, or live availability into reusable instructions.
4. Treat external destinations as separate sites. Stop before Amazon purchase, Y Combinator application, social posting, forum interaction, email, or any other side effect. If the user explicitly asks to inspect an external destination, clarify that it is outside this site's package before switching scope.
5. Verify at least two signals after each navigation: current URL, title/image alt, visible section label, first content block, and the destination's link purpose.

## Page and field semantics

- Books is a three-card hub for On Lisp, ANSI Common Lisp, and Hackers & Painters. A detail page can contain cover art, description, bibliographic metadata, reviews, and outbound publisher/buy links.
- Arc, Bel, Lisp, Spam, and Responses are topic/project hubs. Their child lists are navigation maps, not proof that every child route is available or current.
- FAQ is a family hub; RAQ is a long-form Q&A page; Quotes is a list of quote/source entries. None showed a site search, filter, or submit control in the observed public state.
- RSS is a first-party explanation page that points to an external scraped feed; do not report the feed's current contents without separately opening and verifying it.
- Bio and Email are informational pages. Email guidance is not permission to reveal private contact data or send messages.

## Verification and freshness

Re-open the target page for every request. Verify the page title and the requested section or field in the current UI. Current project resources, FAQ answers, Quotes, external link availability, dates, and CDN parameters can change. If the page is long, use the visible title and targeted DOM text, then report the exact route rather than copying the whole page.

If a browser control reports `ERR_BLOCKED_BY_CLIENT`, timeout, empty automation output, or screenshot failure, inspect the same current tab and retry the exact route once. Preserve earlier visual/download evidence and record a later control error separately; never turn a control error into a claim that the resource is empty.

## Safety and limits

- Keep exploration read-only. Do not buy, apply, post, comment, subscribe, send email, or operate external social/forum destinations.
- Do not download and execute unknown files. Text/image resources may be read only when reached by the visible page and requested by the user.
- Do not guess routes or enumerate the whole archive. Use the hub's visible links and one representative child page.

## Drift maintenance

Before acting, compare the current hub, route, labels, controls, permissions, and first-party explanations with this procedure and the linked references. If a stable difference appears, use the current UI safely, record the public variant, old and new behavior, evidence, and date, then patch the owning artifact only when the change is clear and stable. Re-run the affected read workflow and `quick_validate.py`; report broad or ambiguous changes as maintenance gaps.

## References

- [site-map.md](../../sites/paul-graham/references/site-map.md) — route families, visible labels, page types, and inventory evidence.
- [data-model.md](../../sites/paul-graham/references/data-model.md) — Book, ProjectHub, ReferencePage, and ExternalResource fields.
- [interaction-rules.md](../../sites/paul-graham/references/interaction-rules.md) — safe interactions, external boundaries, and evidence handling.
- [agent-usability.md](../../sites/paul-graham/references/agent-usability.md) — routing simulations for representative future requests.
