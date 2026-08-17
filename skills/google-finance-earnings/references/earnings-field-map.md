# Earnings field map

## Earnings calendar

- Time scope: `昨天`、`今天`、`明天`、`本週`、`下週`.
- Scope filter: `所有股票`; authenticated variants may also expose `在你的清單中`.
- Company card: date, time zone, company name, accounting period, estimated EPS, estimated revenue, quote link, and an `新增至日曆` external link.
- Verification: selected time tab, selected scope filter, completed loading state, and company quote URL.

## Company earnings

- Report metadata: previous report date and accounting period.
- Surprise fields: EPS actual / estimate, revenue actual / estimate, and over- or under-expectation state.
- Conference-call material: recording duration, transcript, highlighted content, and source links when shown.
- Treat narrative summaries as dynamic site content; do not store them as methodology.

## Financials and holdings

- Financials: `損益表`、`資產負債表`、`現金流量`; record the visible unit and period selector before reading rows.
- Holdings: `內部人士` and `政治人物`; record the table title, column names, third-party disclosure, page number, and pagination state.
- Keep values from the current page separate from the durable field names and navigation rules.
