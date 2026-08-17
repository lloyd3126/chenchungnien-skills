---
name: koyfin-market-monitoring
description: "Use Koyfin through the Codex in-app browser for read-only market monitoring: Market News, Market Movers, World Equity Indices, Market Scatter, Lots of Charts, Earnings Calendar, Economic Calendar, and related Market Overview pages. Trigger when a user asks for current market screens, calendars, movers, indices, or broad market research."
---

# Koyfin market monitoring

## Purpose and entry point

Route broad market questions to the visible Koyfin sidebar rather than guessing a market-data URL. Use the current UI, selected universe, filters, date range, period and timezone as the query definition. All market rows, chart points, counts and event values are dynamic.

## Procedure

1. Inspect the current tab and preserve the existing in-app browser session.
2. Use the visible entry point:
   - `Market News` → `/news/top`; switch to `Global Markets` when regional news is needed.
   - `Market Movers` → `/mov`; verify universe, market session and `Sector Filter`.
   - expand `Market Dashboards` → `World Equity Indices` `/wei` or another visible child.
   - `Research Tools` → `Market Scatter` `/ms` or `Lots of Charts` `/lot`.
   - expand `Calendars` → `Earnings Calendar` `/earc` or `Economic Calendar` `/ecal`.
3. Apply only safe filters, tabs, periods, groups, date ranges, table columns, sort controls or search inputs. Record the exact visible selection, not an assumed default.
4. Wait for loading to finish after changing a control. Verify the page heading, selected universe/date/timezone and at least one real list, table, card or chart result.
5. Report the result with its observation time and query settings. Re-fetch if the user asks for current values or if the page shows a dynamic date range.

## Page and field semantics

- `Market News` has Top News and Global Markets views with category/source lists; distinguish headline timestamp/source from the time of retrieval.
- `Market Movers` combines a universe, sector filter, market-session controls, a performance-versus-relative-volume chart and Gainers/Losers tables. Session controls can be disabled depending on current market state or permissions.
- `World Equity Indices` groups index rows by region and exposes price, daily change, z-score, one-year return and 52-week range fields.
- `Market Scatter` uses a selected universe, X/Y metric controls and vertical/horizontal layout; its table is the verification companion to the plot.
- `Lots of Charts` is a paginated chart grid with period buttons, universe/sector controls and dynamic chart cards. Pagination and chart contents must be re-read each task.
- `Earnings Calendar` and `Economic Calendar` are event tables/cards whose date range, country/universe, fiscal period, consensus/actual fields and timezone are part of the query.

## Safety and limits

- Do not use `Save as watchlist`, `Save`, `Share`, `Download` or `Export` unless explicitly requested; they may create data or transmit current results.
- Never infer that a missing ticker, event or chart means it does not exist. A filter, universe, date range, market session, entitlement or loading state may explain it.
- Do not store current ranking rows, prices, percentages, result counts, event values or news titles in AGENTS.md, skills or references.

## Drift maintenance

- Compare current visible labels, selected universe, period/date controls and source/category options before acting.
- If a market route or control changes, re-run one safe query and update the owning reference only when the change is stable and visually verified.
- Keep authentication/entitlement differences separate from public observations.

## References

- [market-tools.md](references/market-tools.md) — route matrix, controls, verification and freshness.
