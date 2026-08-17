# 財報狗資料模型

## Entity map

```text
Company
├── Analysis sections
│   ├── Health checks
│   ├── Financial time series / metrics
│   ├── Valuation and ownership
│   └── Product / business profile
├── Topic memberships ── Topic
├── Industry membership ── Industry ── upstream / middle / downstream sub-industries
├── News articles / external sources
└── User watchlists (authenticated)

Screener strategy ── criteria ── ranked Company results
Industry report ── sections / supply-chain roles ── Company and Topic links
```

## Entities and fields

| Entity | Stable identity / fields | Connected views |
| --- | --- | --- |
| Company | ticker, display name, market, exchange, company URL, business description, industry | `/analysis/<ticker>`, analysis sections, news, topics, reports |
| Analysis section | section name, route, metric definitions, chart/table, date range, unit, source note | company overview and one of the 10 section routes |
| Metric observation | metric name, value, unit, period, as-of date, source | summary table, chart, ranking, screener condition |
| Health check | check category, pass/risk explanation, supporting indicator, methodology text | `/analysis/<ticker>/stock-health-check` |
| Topic / tag | stable tag id, label, topic explanation, benefit level/category, related companies, related news, related tags | `/tags/<id>`, company topic analysis, news, reports |
| Industry | slug, label, performance period, definition, upstream/middle/downstream groups, member companies | `/taiex/<slug>`, industry reports |
| Screener strategy | strategy name, criteria, operator/value controls, ranking method, result list, historical method | `/screeners/*`, `/screeners/custom` |
| Ranking result | ranking dimension, period, order, company link, current row values | ranking pages; always re-fetch |
| Article / report | title, published date, category, tags, body, related companies/topics, source links | `/news/*`, `/blog/*`, `/industry_reports/*` |
| Watchlist / portfolio | user-owned list name, tracked companies, prices/changes/metrics, add/rename/delete controls | `/feeds`, `/portfolios`; authenticated |
| Account | avatar, email, display name, plan, newsletter setting, payment/password routes | `/users/account`; authenticated and private |

## Relationship rules

- A company can belong to an industry and many topics; a topic can connect to many companies and articles.
- A company overview links to specialized metric pages; metric pages are the authoritative route for the metric's current series and unit.
- A screener produces a current ranked set of companies; it is not a persistent entity unless the user explicitly saves it.
- An industry report can describe a supply-chain role and link to company analysis pages; the report's prose is context, not a replacement for current company data.
- A watchlist contains user-specific company references. Its current contents and values must never be copied into reusable skills.

## Dynamic-data rule

Current prices, ratios, rankings, report availability, article lists, performance percentages, plan prices, notification contents and watchlist values are dynamic. Store the route, query, selected controls, date/time and verification signal instead of the value.
