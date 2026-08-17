---
name: tw-gov-data-search
description: Search and filter Taiwan government open-data datasets in the data.gov.tw UI. Use when the user asks to find datasets by keyword, category, provider, file format, API-service type, popularity, metadata conditions, sorting, pagination, or search-result export through the Codex in-app browser.
---

# Taiwan Government Dataset Search

## Purpose and entry point

Use the user's existing Codex in-app browser tab on `https://data.gov.tw/`. If it is not already on the site, navigate the same in-app tab to the homepage and verify the page heading before continuing. Use the current UI as the source of truth; do not replace this workflow with API calls, scraping, or an external browser.

## Procedure

1. Choose the entry point from the request: homepage search, `/datasets/search`, a homepage service category, `/datasets/search?type=pop`, `/datasets/search?dt=openapi`, or a provider link.
2. For keyword discovery, fill `請輸入關鍵字`, wait for autocomplete, and either select the exact intended suggestion or click `搜尋`. Verify `資料集列表 | Datasets`, the encoded `rft` query, and visible result cards.
3. For structured discovery, open `進階搜尋`; fill dataset ID, provider, child-agency inclusion, and repeatable AND/OR field rows. Use `新增` for another condition, submit with the advanced `搜尋`, and verify the resulting state. Use `清空` when resetting only the advanced form.
4. Open `展開過濾條件` for agency, topic, service category, file format, data-provision property, and keyword facets. Apply the smallest relevant safe filter and verify the result state; facet counts are dynamic.
5. Use `選擇排序` and `選擇一頁幾個項目` when ranking or pagination matters. Verify the selected label and URL query (`s`, `size`, `p`) before reading results.
6. For every candidate, capture title, provider, description, major field notes, current metadata update time, provision property, formats, and the `/dataset/<nid>` link. Hand off detail/resource questions to `$tw-gov-data-dataset`.
7. Trigger `搜尋結果匯出` only when the user requested a downloadable inventory. Treat the browser download UI and the downloaded artifact as the evidence; do not claim an export from a button label alone.

## Verification and freshness

- Re-fetch the search for every live request. Never reuse current result counts, rankings, usage counters, or update timestamps from this skill.
- Verify at least the current URL/query, heading or control state, and one result card after search, filter, sort, or pagination.
- If a control does not change the visible state, inspect the page before retrying and report the control as unconfirmed rather than looping.

## Safety and limits

- Keep exploration read-only and reversible. Do not submit comments, login, register on external API platforms, create API keys, or enter secrets.
- A format label such as CSV or JSON is metadata, not proof that the external resource is reachable or that its rows are valid.
- Do not write dynamic facet counts, result lists, rankings, URLs with live tokens, or one-off search results into instructions.

## Drift maintenance

- Compare the current visible UI, route, labels, controls, permissions, and first-party explanations with this procedure before acting.
- If a stable search control or query encoding changes, record the public/authenticated variant, page type, old and observed behavior, evidence source, and date; update this skill or its reference only when the change is clear.
- Re-run a safe keyword search and `quick_validate.py` after editing. Keep ambiguous or broad changes as a maintenance gap.

## References

- [search-controls.md](../../sites/data-gov-tw/references/search-controls.md) — query paths, advanced fields, facets, sorting, pagination, and safe export boundaries.
- [site-map.md](../../sites/data-gov-tw/references/site-map.md) — confirmed first-party routes and exploration limits.
