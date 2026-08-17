---
name: globenewswire-rss
description: Locate and verify public GlobeNewswire RSS, ATOM, and JavaScript widget feeds through the Codex in-app browser. Use when the user wants feeds by subject, industry, location, or a release organization's visible RSS/ATOM links.
---

# GlobeNewswire RSS

## Purpose and entry point

Use this skill for public syndication feeds at `https://www.globenewswire.com/rss/list` or for a feed link visibly exposed on a GlobeNewswire release detail page. Use the current Codex in-app browser tab only; do not use curl, an API, an external browser, or guessed feed tokens.

## Feed directory workflow

1. Inspect the current tab, then open the visible footer `RSS Feeds` link or `/rss/list` in the same tab.
2. Verify the heading `GlobeNewswire RSS / XML News Release Feeds` and the visible tablist.
3. Choose the live grouping: `RSS by Subject`, `RSS by Industry`, or `RSS by Location`. In the exploration pass, `RSS by Subject` was selected and `Speciality Business News` was expanded; the other tab contents were visible as tabs but not confirmed after click.
4. Expand a visible group when needed and choose the exact visible format link: `RSS`, `ATOM`, or `Java Script`. Do not synthesize a URL containing `subjectcode`, `orgclass`, `feedTitle`, or a token; copy it from the visible first-party link.
5. Verify the opened feed's title/content type/entries or the browser's visible download state. Keep the feed URL and entries current; do not report that a feed is valid solely because its link label exists.
6. For a release-specific feed, open the visible `Subscribe via RSS` or `Subscribe via ATOM` link from the release page and verify the target. Route to `$globenewswire-release` when the user also needs release metadata.

## Format semantics

- `RSS` and `ATOM` are public syndication representations; their entries, timestamps, and ordering are dynamic.
- `Java Script` / `JSWidgetFeed` is a widget/script feed intended for embedding or programmatic presentation, not automatically an RSS or Atom document.
- Directory groupings describe the site's navigation taxonomy. They do not guarantee that every release has every feed or that a feed is complete.

## Safety and limits

- Reading a public feed is read-only. Do not subscribe a user account, save a browser feed, or transmit credentials.
- Do not follow private, tokenized, or unrelated external URLs merely because they appear in page markup. Use only the exact visible first-party feed link required by the request.
- Treat current entries, counts, dates, and availability as dynamic. Record the retrieval time when freshness matters.
- If a tab click, XML view, or download is blocked, inspect the same current tab and retry through the visible link once. Report `client-blocked`, `blocked`, `invalid`, or `unavailable` precisely; an empty automation response alone is not proof that the feed is empty.

## Drift maintenance

Compare the current RSS directory labels, tab state, group names, formats, routes, and feed content with this procedure. If a stable change is verified, update this skill or the site reference with the exact evidence and re-run the feed workflow plus the validator. Do not store current feed entries or tokenized URLs as durable knowledge.

## References

- [site-map.md](../../sites/globenewswire/references/site-map.md) — RSS directory evidence and route inventory.
- [data-model.md](../../sites/globenewswire/references/data-model.md) — Feed entity and relationships.
- [first-party-guidance.md](../../sites/globenewswire/references/first-party-guidance.md) — terminology and content limits.
