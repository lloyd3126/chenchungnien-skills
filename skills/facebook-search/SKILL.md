---
name: facebook-search
description: Search Facebook and verify current result scopes and filters through the Codex in-app browser. Use when the user wants posts, people, Reels, Marketplace, pages, groups, or events matching a keyword, or needs safe read-only search and result verification.
---

# Facebook Search

## Purpose and entry point

Use this skill for read-only Facebook discovery. Start from the current Facebook tab or the visible `搜尋 Facebook` combobox. Read [the data model](../../sites/facebook/references/data-model.md) when the requested result type is unclear.

## Procedure

1. Inspect the current page and confirm that the shared search control is visible. Do not overwrite an in-progress user query without checking the current state.
2. Enter the user's non-sensitive search term into `搜尋 Facebook` and submit it. Do not include passwords, contact details, precise locations, private identifiers or other sensitive data unless the user has explicitly asked for that exact safe lookup.
3. Wait for the results page. Verify both the heading (`<query>的搜尋結果`) and the URL query state (`/search/top/?q=...`) before reporting that search succeeded.
4. Choose a visible result scope when requested: `全部`, `人物`, `Reel`, `Marketplace`, `粉絲專頁`, `社團` or `活動`. After switching, verify the new route or heading and the selected scope.
5. On `全部`, inspect safe read-only filters currently exposed by the UI, such as `最新貼文`, `你看過的貼文`, `依發佈日期篩選`, `貼文來源` and `標註的地點`. Re-read the live options; do not assume option values from an earlier session.
6. Open a representative public result only when needed to answer the task. Keep the query context and confirm the result's heading, author/entity link and relevant field. Do not interact with reactions, comments, sharing, messaging or save controls.

## Result semantics

- Search results may contain feed posts or entity cards; a matching text snippet is not proof that the linked profile, group or post is public or current.
- Counts, timestamps, ranking, recommendation order and result membership are dynamic. Report the query and active filters rather than treating the current list as a durable fact.
- Search may surface authenticated or personalized content. Keep public and authenticated results separate and do not copy private names, group membership or personal records into notes.

## Verification and failure handling

- For every meaningful filter or scope change, verify at least two of: active tab, filter value, heading, URL query state or changed result content.
- If results are loading, wait and inspect again. If an empty state or error appears, preserve the original query and report it; do not silently broaden or rewrite the term.
- Stop at CAPTCHA, age verification, third-party login, or an ambiguous permission prompt.

## Safety and protected branches

Search and filter changes are read-only. Stop before any action that sends, publishes, reacts, comments, shares, saves, subscribes, changes settings, uploads data, or transmits sensitive information. If the requested result type is protected, do not sign in or inspect private content without explicit user direction and manual sign-in in the same in-app browser tab.

## Drift maintenance

Before searching, compare the live search control, result heading, scope labels, filters and query state with this procedure. If a stable field, label, route, validation behavior or result-verification rule differs, record the public/authenticated state, page type, old behavior, observed behavior and date, then update this skill or [the site map](../../sites/facebook/references/site-map.md) when the change is clear. Never store current results or sensitive queries. Re-run the safe search and `quick_validate.py` after editing.

## References

- [data-model.md](../../sites/facebook/references/data-model.md) — SearchRequest and SearchResult fields and relationships.
- [site-map.md](../../sites/facebook/references/site-map.md) — verified search routes and page taxonomy.
- [safety-and-drift.md](../../sites/facebook/references/safety-and-drift.md) — protected branches and maintenance rules.
