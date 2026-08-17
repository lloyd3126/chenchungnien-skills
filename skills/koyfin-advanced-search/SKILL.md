---
name: koyfin-advanced-search
description: Use Koyfin's Advanced Search in the Codex in-app browser to disambiguate securities or search transcripts by terms, dates, event types, companies, lists, and sectors. Trigger when a ticker has multiple listings or a user needs transcript/security search results; keep the workflow read-only.
---

# Koyfin advanced search

## Purpose and entry point

Use `Research Tools` → `Advanced Search` and select `Security Search` or `Transcripts Search`. This is the reliable route for exact entity resolution and transcript filtering when the global search is ambiguous. Search results are dynamic and may depend on account scope, date range and current data availability.

## Procedure

1. Inspect the current tab and expand `Advanced Search` if the sidebar parent is collapsed.
2. For exact security resolution, choose `Security Search`:
   - enter a name or ticker in `Type terms you want to search`;
   - choose `Asset Category` and, when needed, Country, Sector, Trading Currency or Trading Exchanges;
   - click `Search Securities` and inspect the result table's Ticker, Country, Security Name and Asset Category;
   - select the exact visible listing or use its result identity to continue to Security Analysis;
   - click `Reset` when the task is complete.
3. For transcript research, choose `Transcripts Search`:
   - enter terms in the search field and use `Advanced Terms` only when needed;
   - capture the visible Date Range, Companies, Security Lists, Sectors and Event Types;
   - apply a safe event-type filter such as `Earnings Calls`, wait for loading, inspect the filtered rows, then use `Clear` or `Reset`;
   - preserve event title, company/security identity, event type, date and time rather than only a result count.
4. Verify the active search tab, query/filter state and at least one result row or explicit empty/loading state. Do not interpret a temporary no-result state as proof of absence.

## Page and field semantics

- Security Search returns listings, not abstract ticker strings; Country, Security Name and Asset Category are essential disambiguators.
- Transcripts Search is an event corpus. Date range, event type, company/list/sector filters and terms jointly define the result set.
- `Clear` may clear one active filter, while `Reset` returns the form to its broader state; verify the visible state after either action.
- The site can show result counts and recent matches; counts and rows are dynamic and are not durable reference data.

## Safety and limits

- Search, filter, clear and reset are read-only. Do not download, share, save, import or edit results unless explicitly requested.
- Never guess a Koyfin internal security ID from ticker text or a URL. If multiple listings remain, ask for the intended exchange/country/asset class rather than choosing silently.
- If a result area is loading, empty or visually unavailable, report the exact state and query settings; do not broaden or alter the query invisibly.

## Drift maintenance

- Compare the current visible labels, filter options, selected search tab and reset/clear behavior before acting.
- Re-run the affected safe query after a stable UI change and update the reference; keep live rows, counts and dates out of documentation.

## References

- [search-controls.md](references/search-controls.md) — security/transcript fields, disambiguation and reset behavior.
