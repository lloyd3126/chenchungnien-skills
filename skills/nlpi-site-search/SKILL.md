---
name: nlpi-site-search
description: Search and filter the National Library of Public Information website through the Codex in-app browser. Use whenever the user wants NLPI pages, announcements, services, policies, digital-resource guidance, or current site content by keyword, including ordinary or advanced search.
---

# 國資圖全站搜尋

## Purpose and entry point

Use only the Codex in-app browser on `https://www.nlpi.edu.tw/`. Start from the visible current tab, the homepage, the main menu's `全站搜尋`, or `/Search`. Read [search-controls.md](../../sites/nlpi/references/search-controls.md) when a query or result state is ambiguous.

This skill covers host-site search only. Route activity discovery to `$nlpi-activity-search`; route authenticated records to `$nlpi-member-center`; route digital-resource service semantics to `$nlpi-digital-resources`.

## Procedure

1. Inspect the current page and confirm the visible heading and current URL before entering a query.
2. Open `全站搜尋` or `/Search`. Use the visible `關鍵字` textbox and enter a non-sensitive user term.
3. Click `送出搜尋` once and wait for the embedded result area to settle.
4. Verify at least two signals: heading, retained input, URL/hash, result count, page links, or visible result cards. The page may move into a `#gsc.tab=0` Google Custom Search state.
5. If exact matching, inclusion, exclusion, or OR semantics are needed, open `進階搜尋` and read the field helper text before filling the three required inputs. Verify each retained value and the resulting result state separately.
6. Report the query, current result state, and any rendering limitation. Do not treat a search button click, a blank embedded panel, or a CSP error as proof of a meaningful result.

## Safety and limits

- Search is read-only, but the embedded panel may expose a link to search Google; do not follow it unless the user explicitly asks for that external search.
- Do not enter passwords, IDs, contact details, or private member data into a search box.
- The current exploration saw CSP `EvalError` messages inside the embedded Google result area. Preserve the query and report incomplete rendering rather than inventing results or silently broadening the query.

## Drift maintenance

Compare the live search controls, labels, result embedding, query state, and first-party guidance with this procedure. If a stable route or control changes, safely verify it, update this skill or the linked reference, and run `quick_validate.py`. Keep live result values and counts out of the files.

## References

- [search-controls.md](../../sites/nlpi/references/search-controls.md) — field semantics and verification.
- [site-map.md](../../sites/nlpi/references/site-map.md) — route inventory and page taxonomy.
