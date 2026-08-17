# Koyfin security navigation

## Resolve the security first

1. Use the visible top search `Search for a name, ticker, or function`, or open `Advanced Search` → `Security Search`.
2. Search by name or ticker. The global search modal exposes category tabs such as All, Equities, ETFs, Mutual Funds, SMAs, Indices, Govt Yields, Forex, Crypto, Futures and Economic.
3. Treat a ticker as ambiguous until the visible result supplies the required Country, exchange, asset category and security name. Security Search exposes `Asset Category`, `Country`, `Sector`, `Trading Currency` and `Trading Exchanges` filters, followed by a results table.
4. Select the visible result. Never construct an `eq-*` identifier or UUID from memory. Re-resolve it when the task starts.

## Sidebar route map

The security sidebar uses a selected security card and collapsible parents. Expand the parent before clicking its child:

| Parent | Child labels observed | Task |
| --- | --- | --- |
| `Snapshots` | `Overview`, `Description`, `Percentile Rank`, `Dividend`, `Ownership`, `Earnings History` | identity, quote, profile, rankings, dividend, ownership and earnings history |
| `Analyst Estimates` | `Actuals and Consensus`, `Price Target`, `Estimates Overview`, `Estimates Trends` | reported/consensus estimates and target trends |
| `Financial Analysis` | `Income Statement`, `Balance Sheet`, `Cash Flow`, `Multiples`, `Enterprise Value`, `Profitability`, `ROIC`, `Solvency` | financial statements and derived analysis |
| `News, Filings & Transcripts` | `News`, `Press Releases`, `Filings`, `Transcripts` | company events and source documents |
| `Graphs` | `Historical`, `Comparison`, `Intraday`, `Performance` | configurable time series and comparisons |

Stable route families observed include `/snapshot/<view>/<security-id>`, `/estimates/<view>/<security-id>`, `/fa/<view-id>/<security-id>`, `/charts/<view>/<security-id>`, and `/news/<view>/<security-id>`. These are route patterns only; IDs are session/UI-resolved values.

## Verification checklist

- Confirm the page heading and selected security name/ticker.
- Confirm the active tab or section and period/frequency/currency controls.
- Confirm at least one real field, table row, chart legend item, news source/time, or filing form.
- For a changed control, wait for the loading state to finish and verify the selected state remains active.
