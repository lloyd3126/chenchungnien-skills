# Google Finance data model

## Entities

| Entity | Identifier / selector | Important fields | Related views |
| --- | --- | --- | --- |
| Security | symbol + exchange, e.g. `symbol:exchange` | name, price, change, percent change, quote time, currency, market status | Search, quote, comparison, related assets |
| Index | index symbol + index exchange | index level, change, session state, open/high/low, 52-week high/low | Homepage market card, index quote |
| Quote chart | security or index + time window | chart type, time window, series, comparison, indicators | Quote page |
| Earnings event | company quote link + date | date, time zone, accounting period, estimated EPS, estimated revenue, calendar link | Earnings calendar, company earnings |
| Earnings report | security + report period | report date, period, EPS actual/estimate, revenue actual/estimate, surprise, conference materials | Quote `收益` |
| Financial statement | security + statement type + period | statement rows, period columns, visible unit | Quote `財務` |
| Holding / transaction record | security + record category | person, role or party, transaction type, date, shares, amount, disclosure fields | Quote `持有資產` |
| News item | security or market context + external source | publisher, timestamp, headline, external URL | Homepage, quote, index quote |
| Watchlist / portfolio | authenticated account context | list label, saved securities, personalized insight or calendar filter | Sidebar, earnings filter, research panel |

## Relationships

- A Security has one or more exchange-specific quote identities and can link to related securities, news, earnings, financial statements, and holdings.
- An Index is a market entity that can appear as a homepage card and as a quote page; it may expose fewer company-specific tabs.
- An Earnings event points to a Security quote page and may expose an external calendar link.
- A Quote chart belongs to a Security or Index and is parameterized by a selected time window; comparison and indicators are presentation state, not new securities.
- Watchlist and portfolio data are account-scoped. Do not assume another user sees the same entries or permissions.

## Freshness rules

Values, news, estimates, event dates, transaction records and personalized lists are dynamic. Store the retrieval path, query, selected filters, period, unit and timestamp—not the current value—as durable knowledge.
