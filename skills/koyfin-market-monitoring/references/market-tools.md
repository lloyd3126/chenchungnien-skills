# Koyfin market tools

| Need | Visible path | Controls to capture | Verification |
| --- | --- | --- | --- |
| Top or regional news | `Market News` → `Top News` / `Global Markets` | category tabs, source/category, headline time | heading, selected tab, source/time/title rows |
| Movers | `Market Movers` `/mov` | universe, `Sector Filter`, market session, chart/table view | heading, selected universe/sector and Gainers/Losers table |
| Equity indices | `Market Dashboards` → `World Equity Indices` `/wei` | region groups, group/columns, table rows | heading plus regional group and index row |
| Scatter comparison | `Research Tools` → `Market Scatter` `/ms` | universe, X metric, Y metric, Vertical/Horizontal | heading, plot and matching table columns |
| Chart grid | `Research Tools` → `Lots of Charts` `/lot` | sector, universe, period buttons, pagination | heading, loaded cards, page range |
| Company earnings events | `Calendars` → `Earnings Calendar` `/earc` | universe, period, ticker search, group, currency | heading, date group and fiscal/revenue/EBITDA fields |
| Macro events | `Calendars` → `Economic Calendar` `/ecal` | country filter, date range, 3-Day/Week, timezone | heading, date column/card and Actual/Consensus/Previous |

## Control rules

- Expand `Market Dashboards` or `Calendars` before clicking child links; a collapsed parent can make an otherwise visible child click fail.
- Record selected universe and date range before reading. Defaults are not stable across accounts or time.
- After a filter or period change, wait until the loading state resolves and verify the resulting selected state plus a result.
- Use `Reset`, clear buttons or temporary text-field clearing to return to the prior read-only state.
- Treat disabled market-session controls as a current-state/permission observation; do not force them through script or alternate endpoints.

## Freshness and output

Return the query settings and observation time with the result. For a current-market answer, re-run the page at answer time. Keep live rows, current values, counts and headlines out of durable documentation.
