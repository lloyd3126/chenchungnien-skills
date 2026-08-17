---
name: pokecabook-site-search
description: Search the public PokecaBook website through the Codex in-app browser. Use when the user wants to find PokecaBook articles, deck posts, tournament results, card lists, rules, or columns by keyword, inspect search results, or paginate a live site search.
---

# PokecaBook Site Search

## Purpose and entry point

Use this skill for the public keyword search at `https://pokecabook.com/`. Start from the current PokecaBook tab when one exists; otherwise open the homepage in the Codex in-app browser. Read [search-results.md](references/search-results.md) for the observed form and result semantics, and [the site map](../../sites/pokecabook/references/site-map.md) when routing is unclear.

Do not use an external browser, web search, API, scraper, cookies, local storage, or saved session data.

## Procedure

1. Inspect the current tab and record the visible URL and title. Keep the existing tab and public session.
2. Use the visible search field labelled `サイト内を検索`. The observed public form uses `name="s"` and submits to the site root.
3. Submit a safe keyword search. If the visible submit control is unreliable, use one same-origin navigation derived from the observed form: `https://pokecabook.com/?s=<URL-encoded keyword>`. Do not invent hidden parameters or call an API.
4. Wait for the result page and verify at least two of: title, main heading, URL query, result-card titles/categories, or pagination. An empty result is a valid result; do not silently broaden the query.
5. For more results, use the visible pagination. Preserve the keyword and verify the page number in the URL or visible pagination before reporting results.
6. Open a result only when the user needs article-level facts. Hand the resulting detail URL to `$pokecabook-content-research` for structured article, deck, tournament, card-list, or rule extraction.

## Safety and freshness

- Treat titles, dates, counts, ranking positions, and result ordering as live data. Fetch them again for every user task.
- Do not publish comments, send inquiries, follow social links, or perform account-changing actions.
- External X, LINE, Pokémon deck-code, and other outbound links are not part of a normal site-search task; stop and ask before following an external action or scope.
- If the browser shows a CAPTCHA, safety interstitial, login request, or ambiguous third-party page, record the boundary and stop that branch.

## Verification

Report the exact keyword, route, page number, observed heading/title, and whether results were present. Keep evidence separated: current-tab visual, current-tab DOM/interaction, and browser-control errors are different evidence types.

## Drift maintenance

Before using this procedure, compare the live search form, action, field name, result heading, and pagination with this skill. If a stable label or route changes, complete the safe public search using the live UI, update this skill or its reference, and rerun the affected search plus the skill validator. Do not write current result values into the skill.

## References

- [search-results.md](references/search-results.md) — observed search form, query route, pagination, and verification rules.
- [site-map.md](../../sites/pokecabook/references/site-map.md) — public site inventory and known route limitations.
