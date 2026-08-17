---
name: pr-newswire-search
description: Search and filter public PR Newswire content in the Codex in-app browser. Use when the user asks for a press release, organization, product, or resource by keyword, or wants to verify a search result without logging in or publishing.
---

# PR Newswire Search

## Purpose and entry point

Use this skill for public keyword discovery. Start from the user's current PR Newswire tab, or the visible PR Newswire logo/home route if the tab is already on the same site. Use only the Codex in-app browser and keep the operation read-only.

Read [the site package](../../sites/pr-newswire/AGENTS.md), [the interaction guide](../../sites/pr-newswire/references/interaction-guide.md), and [the data model](../../sites/pr-newswire/references/data-model.md) when routing or field semantics are unclear.

## Search workflow

1. Inspect the current visible page and click the visible `Search` button.
2. Fill the visible textbox whose placeholder is `Search News Releases, Organizations, Resources, and Products` with the user's exact keyword.
3. Wait for the overlay state, then press Enter. Verify both the current URL and a result-page heading such as `All Search Results` or `News Search Results`.
4. Verify the displayed keyword and at least one result title, organization, product/resource row, or explicit empty state. Keep the query exact; do not silently autocorrect or broaden it.
5. Choose the visible result type: `All`, `News`, `Organizations`, `Products`, or `Resources`. For News, verify the heading, query, timestamp/title, and release link. For Organizations, open the visible `/news/<slug>/` link only when organization history is requested.
6. If a page-size control is present, select only a visible enabled option, then verify the URL/state and result heading again. Treat result counts and rows as live.

## Search behavior observed

The overlay can show `Searching for your content...` and then `No results found` before submission. A keyword that is known from a visible release may still require Enter to reach the final result route. The final News route observed was `/search/news/?keyword=<query>` and exposed type tabs and page-size controls.

## Verification and output

Report the exact query, result type, route, heading, and a concise set of currently visible result titles/links. State when the overlay had no suggestions but the submitted result page returned matches. Re-fetch the search for every task; do not write current counts, rankings, or result rows into durable notes.

## Safety and limits

- Do not enter personal data, credentials, OTPs, or private search history.
- Do not click social-share controls, send a release, request a demo, submit contact/account forms, or follow an external partner link as part of search.
- If login, CAPTCHA, or a security interstitial appears, stop that branch and report it.

## Drift maintenance

Before acting, compare the current visible search button, placeholder, result tabs, route, and controls with this procedure. If a stable change is directly verified, patch this skill or the site package, preserve public/authenticated variants separately, and run the safe search again plus `quick_validate.py`. Never store live result values or speculate about inaccessible behavior.

## References

- [interaction-guide.md](../../sites/pr-newswire/references/interaction-guide.md) — search controls, list controls, and evidence rules.
- [data-model.md](../../sites/pr-newswire/references/data-model.md) — search, release, organization, and resource relationships.
