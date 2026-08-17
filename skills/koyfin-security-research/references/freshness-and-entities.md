# Koyfin entities and freshness

## Entity model

| Entity | Durable identity | Common views |
| --- | --- | --- |
| Security | visible name, ticker, country/exchange, asset category and UI-selected internal ID | Snapshot, Estimates, Financial Analysis, News/Filings/Transcripts, Graphs |
| Estimate series | metric, fiscal period, period ending/report date, annual or quarterly view, currency | Actuals and Consensus, Price Target, Estimates Overview/Trends |
| Financial series | statement/derived metric, LTM/quarterly/annual period, fiscal date, currency | Income Statement, Balance Sheet, Cash Flow, Multiples, Enterprise Value, Profitability, ROIC, Solvency |
| Event | security, event type/form, source, timestamp/date, title and related document | News, Press Releases, Filings, Transcripts |
| Chart series | ticker/security, metric, date range, frequency, adjustment and visualization state | Historical, Comparison, Intraday, Performance |

## Freshness rules

- Capture the observation time and the UI's period/date/report-date labels. A quote, estimate, filing and chart can each have a different as-of date.
- Re-fetch after changing Annual/Quarterly, LTM/Quarterly/Annual, date range, frequency, currency or chart adjustment.
- Preserve the active universe, source/category filters and timezone for market/event pages.
- Loading indicators are part of the retrieval protocol: do not read a table or chart while `Your data is loading...` is present.
- Current values, ranking rows, result counts, current news, filing lists, trial text and personal workspace records are not durable reference data.

## Safety classification

- Read-only: opening security pages, tabs, filters, search results, charts, period/date/currency controls, and clearing temporary filters.
- Confirmation boundary: Add to My Watchlists, My Alerts, My Notes, Save/Save As, Share, Download/Export, Create, Edit, Delete, Import and portfolio changes.
- Sensitive: portfolio holdings, watchlist entries, dashboard contents, notes, alerts and account-specific labels. Use only to answer the immediate task and never copy them into reusable site guidance.
