# Seeking Alpha Form and Interaction Controls

## Global search

- Entry: homepage search field or `/basic-search`.
- Observed placeholder: `Symbols, Analysts, Keywords`.
- Search supports symbols, analysts and keywords; use the visible suggestions/results rather than treating typed text as a completed search.
- Verify the retained query, result heading or selected scope, and URL/state after submitting. Do not save or subscribe from a search result without explicit user intent.

## Symbol page tabs

- Top-level tabs observed on `/symbol/<ticker>`: `Summary`, `Ratings`, `Financials`, `Earnings`, `Dividends`, `Valuation`, `Growth`, `Profitability`, `Momentum`, `Peers`, `Options`, `Charting`.
- Content tabs observed: `All`, `Analysis`, `Comments`, `News`, `Transcripts & Insights`, `SEC Filings`, `Press Releases`, `Related Analysis`.
- Verify the selected tab and resulting heading／section. The same label can appear in more than one tablist, so scope the locator to the visible tablist or use the page heading.

## Analysis and news lists

- Analysis list exposes `Show summaries`, article cards, author and symbol links, `Save`, `Share`, and pagination where available.
- Market news exposes `Show full stories`, topic/category links, symbol links, `Copy Link`, `Save`, and `Next`／page links.
- Reading is safe; Save, Share, Follow, Like, comment and other outbound or account actions are not default exploration actions.

## Earnings calendar

- Entry: `/earnings/earnings-calendar`.
- Observed controls: a date-range button, day buttons labelled by date, `Open Search Modal`, `Open Settings Modal`, and tabs `EPS`, `Revenue`, `Analysts Revisions & Ratings`.
- The page presents a table whose fields can include Symbol, Report, Market Cap, current-quarter estimates, actuals, beat/miss and recent beat/miss history. The row set is date-scoped and dynamic.
- Verify the selected date or range, selected tab, table heading/column labels, and result rows. Do not use a changed URL or clicked button alone as evidence.

## Screeners

- Entry: `/screeners`.
- The overview shows preset screen cards with a label, description, result summary and `Copy Screen ... link` control; it also advertises custom screening and may show `Unlock all filters` / account or Premium prompts.
- A preset screen link uses a route pattern like `/screeners/<screen-id>-<slug>`; re-open the visible card link and verify its heading, criteria and table before reporting results.
- Custom criteria, operators, sort order, reset and saved screens were not fully verified in this public pass. Do not invent field names or claim that a screen was saved.

## Article detail

- Article pages expose title, summary/body when available, author, `Follow`, disclosure paragraphs, `Like`, `Share`, `Print`, comments and related symbol charts.
- A visible `Register for free to keep reading` gate is an access boundary. Read visible material and state the limit; do not create an account or bypass the gate as part of research.

## Universal verification and drift

- After a control, verify two of: selected state, retained input, visible heading/content change, table/chart change, or URL/query state.
- Treat empty results, loading states, account prompts, paywalls, query caps and CAPTCHA as results to report.
- Re-check current labels and options before acting. If the control structure differs, use the current visible UI safely and update this reference only after stable, direct verification.
