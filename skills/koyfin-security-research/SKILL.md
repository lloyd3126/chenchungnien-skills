---
name: koyfin-security-research
description: Use Koyfin through the Codex in-app browser to resolve an exact stock, ETF, index, or other security and perform read-only research across Snapshot, analyst estimates, financial analysis, news, filings, transcripts, and charts. Trigger when a user asks to investigate one security or compare its current research fields; never guess Koyfin internal security IDs.
---

# Koyfin security research

## Purpose and entry point

Use the existing active Koyfin tab to answer a focused question about one security. Start from the visible global search or `Advanced Search`, resolve the exact listing, then branch through `Security Analysis`. This is a read-only skill: current prices, estimates, filings, news and chart values are retrieved at task time and are not durable facts.

## Procedure

1. Inspect the current tab and current authentication state. Preserve the user's existing tab and session.
2. Resolve the entity through the top search label `Search for a name, ticker, or function`, or open `Research Tools` → `Advanced Search` → `Security Search`. Search by name/ticker, then use visible Country, exchange, asset category and Security Name to choose the exact listing. A ticker can have several country/exchange/ETF matches.
3. Enter the selected security's Snapshot page. If the sidebar section is collapsed, expand `Snapshots` first, then choose `Overview`. Verify the page heading, security name/ticker and at least one visible field before reading values.
4. Choose the smallest research branch that answers the request:
   - estimates → expand `Analyst Estimates` → `Actuals and Consensus`; compare `Annual (Y)` or `Quarterly (Q)`, date range and currency.
   - reported financials → expand `Financial Analysis` → `Income Statement`, `Balance Sheet`, `Cash Flow`, `Multiples`, `Enterprise Value`, `Profitability`, `ROIC` or `Solvency`; verify period and currency.
   - company events → expand `News, Filings & Transcripts` → `News`, `Press Releases`, `Filings` or `Transcripts`; distinguish event time, source and filing form/type.
   - price or metric series → expand `Graphs` → `Historical`; verify ticker, metric, date range, frequency and adjustment settings before reading the chart.
5. Wait for `Your data is loading...` to clear after changing a tab, period, currency, date range or chart control. Then record the query time, selected entity, period/frequency, currency/timezone and the fields actually observed.
6. Verify the result with the heading/entity identity plus selected control and a real table/chart/news field. If the answer depends on current values, state that the data is time-sensitive and was read from the current UI.

## Page and field semantics

- `Security` is an entity, not just a ticker string. Use the visible listing identity and Koyfin-generated internal ID only after UI resolution.
- Snapshot Overview combines identity, quote, next earnings date, sector/industry, market cap, valuation, volume, return ranges, chart ranges and key data. Do not treat all fields as the same timestamp.
- Estimates can switch annual/quarterly and expose period-ending/report-date columns; financial analysis can switch LTM/quarterly/annual and currency.
- News, filings and transcripts are event collections. Preserve source, event/form type, date/time and the active security rather than copying a temporary result count.
- Historical Chart is a configurable visualization. A saved template or chart artifact is a mutation boundary; read the current chart configuration without using `Save As` unless requested.

## Safety and limits

- Do not click `Add to My Watchlists`, `My Alerts`, `My Notes`, `Save As`, `Save`, `Share`, `Download`, `Export` or any edit/create action unless the user explicitly requests it.
- Never enter credentials, inspect cookies/session data, or infer a security ID from a URL or a failed search. A no-result search is session-specific evidence, not proof that a security does not exist.
- Current prices, estimates, ratios, news rows and filing lists are dynamic. Do not write them into skills, AGENTS.md or references.
- If a target page is visually unavailable or a browser-control call times out, preserve the earlier evidence and report the control limitation instead of claiming the page is empty.

## Drift maintenance

- Compare the current sidebar labels, selected security, controls and first-party explanations with this procedure before acting.
- If a stable route, label, field, permission or workflow changes, update the owning site AGENTS or reference only after safely re-running the affected read-only path.
- Keep authenticated and non-authenticated variants separate; never write private holdings, alerts, notes or current result values.

## References

- [navigation.md](references/navigation.md) — entity resolution, sidebar expansion and Security Analysis route map.
- [freshness-and-entities.md](references/freshness-and-entities.md) — entity model, field interpretation and freshness rules.
