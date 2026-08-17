# Seeking Alpha Data Model

## Core entities

| Entity | Identifier | Important fields or states | Related pages |
| --- | --- | --- | --- |
| Instrument / Security | ticker or symbol route segment, e.g. `<ticker>` | name, exchange/asset type, quote, percentage change, market cap, yield, estimates, rating grades; values are live | `/symbol/<ticker>`, market news cards, screen rows, article side rails |
| Symbol page | `/symbol/<ticker>` | summary, rating families, financials, earnings, dividends, valuation, growth, profitability, momentum, peers, options, charting; content tabs for analysis/news/transcripts/filings/releases | symbol hub and its child routes |
| Analysis article | `/article/<id>-<slug>` | title, summary/body availability, author, linked ticker(s), analyst disclosure, SA disclosure, comments, like/share/print controls, related stocks | analysis list, symbol analysis, article detail |
| Market news item | `/news/<id>-<slug>` | headline, publication/update context, linked ticker(s), category, comments and related news | market-news list, symbol news, news detail |
| Author | `/author/<slug>` | author identity, profile, follower count, published articles; follow control may be protected or side-effectful | article detail, author links |
| Screener definition | preset screen route or custom query state | universe, criteria, operator/value selections, sort, result scope, optional saved state | `/screeners`, preset screen, comparison handoff |
| Screen result row | row identity normally includes a symbol plus current fields | ticker, company name, quote, ratings, financial or valuation columns; rows/counts change | preset/custom screen result |
| Earnings event | symbol + report date | report date, EPS/revenue estimate and actual fields, beat/miss, revision/rating view | earnings calendar, symbol earnings |
| Market series | series key + interval | instrument, time range, price/return values, chart/table representation | home indices, symbol charting, article side rail |
| Portfolio / follow state | user-account scoped | holdings, follows, saved articles/screens, alerts, private permissions | `/account/portfolio`, account-dependent controls |

## Relationships

- An Instrument is the central join key: a symbol page links to its analysis, news, earnings, transcripts, SEC filings, press releases, peers, ETFs holding it and charts.
- An Analysis article can mention one or more Instruments, has an Author, and exposes comments and disclosure text; its body may be gated independently of the symbol quote rail.
- A Market news item links to one or more Instruments and can be opened from a category list or a symbol's news section.
- A Screener definition produces Screen result rows; opening a row should hand off to the corresponding Symbol page before making company-level claims.
- An Earnings event belongs to an Instrument and is viewed through a date-scoped calendar or the symbol's earnings section.
- A Portfolio or follow state belongs to a signed-in user; never infer or persist it from a public page.

## Interpretation rules

- Keep site ratings, author opinions, news facts, estimates, and primary-company disclosures as separate evidence layers.
- A current quote or screen row is not a durable fact. Re-fetch it with the requested symbol, date range, filter state and observation time.
- A symbol link from a news/article card identifies the related instrument; it does not prove that every claim in the content applies to that instrument.
- A paywall or register gate changes body availability, not the existence of the article metadata. Report the visible boundary and do not attempt to bypass it.
