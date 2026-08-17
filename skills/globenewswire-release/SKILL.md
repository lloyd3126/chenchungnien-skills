---
name: globenewswire-release
description: Inspect and verify a public GlobeNewswire press release in the Codex in-app browser. Use when the user has a release URL or search result and needs its title, publication time, source, body, tags, industry, links, or safe related-release navigation.
---

# GlobeNewswire Release

## Purpose and entry point

Use this skill for a public release detail page on `https://www.globenewswire.com/`. Start from a visible search/category result or a user-provided GlobeNewswire release URL in the current Codex in-app browser tab. Use `$globenewswire-search` when the release must first be found; use `$globenewswire-rss` when the user needs a feed rather than one release.

## Procedure

1. Inspect the current tab, then open the target release in that same tab. Prefer the exact visible first-party href; do not reconstruct a slug or release ID from memory.
2. Verify the page with at least two signals: the `/news-release/...html` route, the level-1 title, the publication time, or the visible `Source` organization.
3. Read the durable structure: headline, published time/timezone, source, body sections, release summary, company profile, tags, industry, company website, and visible language.
4. Preserve attribution. Separate issuer statements, quotations, forward-looking statements, company profile text, and the agent's own synthesis. Do not treat a distribution page as independent verification of a financial, legal, medical, or regulatory claim.
5. Inspect the public action area only as needed. The observed page exposed `Print`, `Download PDF`, `Subscribe via RSS`, `Subscribe via ATOM`, and a JavaScript widget link. Verify a target actually opens or downloads before claiming that it was retrieved.
6. Use the visible organization/tag links or adjacent-release links for follow-up. Route back to `$globenewswire-search` for broader discovery and `$globenewswire-rss` for feed work.

## Page and field semantics

- `Source` is the public organization attribution.
- The time shown next to the title is the site's published time; also record the observation time when freshness matters.
- `Release Summary`, body paragraphs, quotes, company profile, and `Forward-Looking Statements` are publisher-provided content and should retain attribution.
- `Tags` and `Industry` are site labels. They can route to public search results but do not prove that a release is complete or exclusive to that topic.
- `Print` and `Download PDF` are alternate representations of the release. `Subscribe via RSS` and `Subscribe via ATOM` expose public organization feeds when the visible link is available.
- `Follow` and share controls were visible but not used in exploration; treat them as potentially state-changing or representational and do not activate them without a separate user request and action-time confirmation when required.

## Freshness and verification

Re-open the release when the user needs current text, current links, current publication status, or current related releases. Do not save current release titles, prices, rankings, dates, counts, or body text as durable skill knowledge. If a PDF/feed is requested, verify the browser download/open result rather than trusting the link label alone.

## Safety and authentication

- Keep reading and navigation read-only by default. Do not publish, edit, follow, share, send, subscribe an account, register, or submit a form during discovery.
- Do not enter credentials or personal data into the Notified login/Reader branches. A visible CAPTCHA or authentication wall is a stop boundary.
- Treat external company websites, Notified pages, SEC links, and social links as separate destinations; follow only when the user asks and the action remains within the approved scope.

## Drift maintenance

Compare the current visible release layout, labels, action links, route pattern, and first-party explanations with this procedure before acting. If a stable field or route changes, complete the safe read with the live UI, capture the exact old/new behavior and evidence source, update this skill or the site reference, and re-run the affected workflow plus the validator. Keep dynamic publisher content out of the artifacts.

## References

- [site-map.md](../../sites/globenewswire/references/site-map.md) — release route pattern and page taxonomy.
- [data-model.md](../../sites/globenewswire/references/data-model.md) — release fields and entity relationships.
- [first-party-guidance.md](../../sites/globenewswire/references/first-party-guidance.md) — first-party terminology and publisher-claim limits.
