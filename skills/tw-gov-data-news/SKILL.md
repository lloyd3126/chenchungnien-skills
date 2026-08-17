---
name: tw-gov-data-news
description: Find and filter current data.gov.tw news and dataset announcements in the Codex in-app browser. Use when the user asks for recent updates, dataset upload/removal notices, open-data news, local-government alerts, columns, RSS, or news-result export.
---

# Taiwan Government Open Data News

## Purpose and entry point

Use the existing Codex in-app browser tab on `https://data.gov.tw/news`. Re-fetch the page for every request because news rows, dates, categories, and pagination are dynamic.

## Procedure

1. Verify heading `最新消息`, the keyword field, and the news table.
2. Use `關鍵字搜尋` and `搜尋` for a topic. Use the category radio group to narrow to `全部`, `資料集上架公告`, `資料集下架公告`, `資料開放最新快訊`, `地方政府最新快訊`, `平臺維運公告`, or `其他`.
3. Verify the selected category and query state, then read the table's publication date, title, category, and `/news/<id>` link. Open a news detail only when the user needs the article content.
4. Use the table sort controls and pagination when the request specifies order or a date window. Do not hard-code current row counts or dates.
5. Use `匯出搜尋結果清冊` CSV/XML/JSON or `訂閱 RSS` only when the user requests an export/feed. Verify the browser download or RSS page before claiming success.

## Verification and freshness

- Confirm the current URL, selected radio, table heading/rows, and category label after filtering.
- Report the search term, category, and observation time when summarizing current news.
- Distinguish dataset upload/removal notices from general open-data news; do not infer dataset status from an article title without opening the linked notice when needed.

## Safety and limits

- Keep the workflow read-only. Do not submit comments, login, subscribe to a private account, or alter site content.
- RSS and export controls are outbound navigation or inbound download boundaries; use them only for the requested artifact.

## Drift maintenance

- Compare the current visible UI, routes, labels, categories, and first-party explanations with this procedure before acting.
- If the category model, table fields, export controls, or RSS route changes, record old behavior, observed behavior, evidence source, and date, then patch this skill only when stable and verified.
- Re-run one category-filter workflow and `quick_validate.py` after editing. Keep unverified route changes as maintenance gaps.

## References

- [site-map.md](../../sites/data-gov-tw/references/site-map.md) — first-party route map and coverage status.
- [search-controls.md](../../sites/data-gov-tw/references/search-controls.md) — shared search-state and download-boundary conventions.
