---
name: tabelog-search
description: Search and filter public Tabelog restaurant listings through the Codex in-app browser. Use when the user wants restaurants by area, station, keyword, genre, budget, meal time, party size, scene, facilities, ranking, or current availability, and when safe form interaction or result verification is needed.
---

# Tabelog Search

## Purpose and entry point

Use this skill for discovery. Work only in the Codex in-app browser, starting from the currently open Tabelog tab or `https://tabelog.com/`. Do not switch to an external browser, API, scraper, or stored session data. Read [the site map](../../sites/tabelog/references/site-map.md) when routing is unclear.

The public search flow is:

`首頁 → area/station + keyword → date/time/party size → 検索 → result list → filters/sort/pagination → restaurant detail`

If the user already has a restaurant or detail URL and wants its fields or subpages, use `$tabelog-restaurant` instead.

## Procedure

1. Inspect the current tab and visible site state. Preserve the existing tab and session; never inspect cookies, passwords, local storage, or authentication data.
2. On the homepage or shared header, use the visible search controls:
   - `エリア・駅` (`sa`) for a city, station, or area.
   - `キーワード` (`sk`) for a cuisine, restaurant name, or term such as private room.
   - `search_date` for the visit date.
   - `svt` for time, displayed in 30-minute options from 10:00 through 24:00 in the observed public form.
   - `svps` for party size, with options from 1名 through 99名 in the observed public form.
3. For `エリア・駅`, wait for the visible autocomplete suggestions and select the intended exact station or area. Suggestions can distinguish a station from same-named areas in different prefectures. Typing text without selecting a suggestion was observed to show `該当のエリア・駅が見つかりませんでした` and fall back to a national result list, so do not report that as an area-specific result.
4. Submit only a safe, read-only search. If the UI click is unreliable, inspect the visible form action and current public controls, then use one focused navigation derived from that form. Do not invent hidden state or copy tokens.
5. On the result page, verify the new page heading, selected controls, visible condition summary, and/or URL query state. For an area search, confirm the heading names the selected station/area or that the URL contains the corresponding area/station scope. Record the area, keyword, date, time, party size, and any filter values used.
6. Apply filters incrementally and re-check after each meaningful change. Safe observed examples include:
   - `LstCos` / `LstCosT`: lower and upper budget ranges.
   - `LstRev`: meal / operating-hour conditions such as `ランチ`.
   - visible condition links for Vポイント, 個室, 飲み放題, cards, parking, 食べ放題, children, pets, coupons, takeout, delivery, smoking, and space/equipment.
   - scene links such as family/children, date, girls' night, group party, or business entertainment.
7. Use sorting, result pagination, and category breadcrumbs only when needed. Treat counts, rankings, prices, reviews, and availability as live query results, not stable facts.
8. Open representative result cards to inspect a restaurant with `$tabelog-restaurant`. Keep the current query context so the user can reproduce the result.

## Form and result verification

- A visible control is not evidence that it works. After an interaction, confirm at least two of: page heading, selected option, condition summary, URL query state, or changed result cards.
- Search fields accept free text; do not assume autocomplete semantics until the current UI shows suggestions. Use exact visible labels and wait for the result page to settle.
- Dropdowns can appear in both the shared header and the result filter form. Target the form associated with the intended action and re-read all duplicate controls after navigation.
- Use `詳細条件` only for read-only filtering. Record whether the panel expanded, which options were offered, and what changed.
- If no result or an error appears, preserve the query and report the empty/error state rather than silently broadening the search.

## Authentication boundary

Public search should continue until the public coverage is complete. `保有Vポイント`, `行ったお店`, `保存リスト`, `無料会員登録/ログイン`, and card-level `行った`／`保存` may require login. Record those branches and continue with public search; do not stop at the first login wall.

After the public pass and its second-pass audit, ask whether the user wants protected functionality explored. If yes, ask the user to manually sign in in the same in-app browser tab and wait. Then re-run the previously covered search, filters, dropdowns, date/time/party-size controls, sorting, and result verification to compare authenticated behavior before using any protected feature.

## Safety and freshness

- Do not click final reservation, payment, save, mark-visited, publish, delete, or external confirmation actions as part of discovery.
- Current result values and availability must be fetched during the task. For time-sensitive restaurant decisions, advise confirming directly with the restaurant.
- Stop at CAPTCHA, safety interstitial, or an ambiguous third-party authentication page; do not bypass it.

## Drift maintenance

Before using this procedure, compare the live search form and result page with the documented controls. If a stable field name, label, route, filter, option set, validation behavior, or result-verification rule differs, use the live UI safely, record the exact evidence, and update this skill or its references in the authorized workspace. Keep public and authenticated behavior separate. Do not write current result values, counts, rankings, prices, or availability into the skill; update only the retrieval or verification rule. Re-run the affected safe search and `quick_validate.py` after a clear update; report ambiguous or broad changes instead of guessing.

## References

- [site-map.md](../../sites/tabelog/references/site-map.md) — explored public routes and verified interactions.
- [data-model.md](../../sites/tabelog/references/data-model.md) — result and restaurant entity relationships.
- [form-controls.md](references/form-controls.md) — search fields, filter names, duplicate-control handling, and evidence pattern.
