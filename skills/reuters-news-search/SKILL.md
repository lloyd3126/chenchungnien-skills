---
name: reuters-news-search
description: Search and filter current Reuters articles through the Codex in-app browser. Use when the user asks for Reuters site search, articles matching keywords, section or date filters, or result sorting.
---

# Reuters News Search

## Purpose and entry point

Use the current Reuters tab and the public search UI. Read [../../sites/reuters/AGENTS.md](../../sites/reuters/AGENTS.md) first; load [form-controls.md](../../sites/reuters/references/form-controls.md) for exact controls and [first-party-guidance.md](../../sites/reuters/references/first-party-guidance.md) for source and freshness rules.

## Procedure

1. Verify the current tab is Reuters and record the current URL, title, and visible auth state.
2. Click `Open search bar`, then locate the `Search Reuters` searchbox. Fill only the user-requested query or a harmless representative query.
3. Click `Search` or press Enter. Verify the URL contains `/site-search/`, the query parameter, and the heading `Search results for “…”`.
4. Apply `Section`, `Date range`, and `Sort by` only when requested. After each change, verify the selected label, URL state, heading/result state, and a representative result; do not rely on the URL alone.
5. For each requested result, capture title, visible category, displayed time, article URL, and any `Exclusive` or `ANALYSIS` label. Open an article only when the task needs detail and hand off to `$reuters-article-research`.
6. Report observation time, query, filters, sorting, result scope, and any loading/empty/gated state. Re-fetch dynamic results for the final answer.

## Controls

- Section options observed: `All`, `World`, `Business`, `Legal`, `Markets`, `Breakingviews`, `Technology`, `Sustainability`, `Science`, `Sports`, and `Lifestyle`.
- Date options observed: `Any time`, `Past 24 hours`, `Past week`, `Past month`, and `Past year`.
- Sort options observed: `Newest`, `Oldest`, and `Relevance`.
- `Clear search text` clears the query; verify whether a new submit is required before reading results.

## Safety and limits

Search is read-only, but do not click `Save`, `Share`, `Follow`, `Subscribe`, or account controls while collecting results. Do not bypass registration, paywalls, CAPTCHA, or access gates. Do not write current result counts, headlines, rankings, or times into this skill.

## Drift maintenance

Compare the live search UI, labels, route parameters, selected controls, result semantics, and first-party explanations before acting. If a stable difference is safely verified, update this skill or the owning site reference, re-run the search workflow and the validator, and keep public/authenticated variants separate. Treat dynamic results as retrieval inputs, not documentation facts.

## References

- [site-map.md](../../sites/reuters/references/site-map.md) — search route and public page taxonomy.
- [form-controls.md](../../sites/reuters/references/form-controls.md) — query, filter, and sort semantics.
- [first-party-guidance.md](../../sites/reuters/references/first-party-guidance.md) — provenance, freshness, and access boundaries.
