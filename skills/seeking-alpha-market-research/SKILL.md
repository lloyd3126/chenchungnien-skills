---
name: seeking-alpha-market-research
description: Research current Seeking Alpha market news, analysis articles, sectors, dividends, ETFs, market data, search results and earnings calendars through the Codex in-app browser. Use when the user asks about market-wide content, a news or analysis article, a theme/category, current earnings dates, or site-wide search.
---

# Seeking Alpha market research

## Purpose and entry points

Use this skill for current content across multiple symbols or for reading a specific news/analysis/earnings page. Work only in the Codex in-app browser and use the current visible Seeking Alpha tab.

Read [site-map.md](../../sites/seeking-alpha/references/site-map.md), [form-controls.md](../../sites/seeking-alpha/references/form-controls.md), and [first-party-guidance.md](../../sites/seeking-alpha/references/first-party-guidance.md) when the request spans page types, form controls or investment interpretation.

## Procedure

1. Route by intent: `/latest-articles` for analysis, `/market-news` for breaking/news categories, `/earnings/earnings-calendar` for dates and estimates, `/etfs-and-funds/etf-tables/<table>` for market tables, or homepage `/` / `/basic-search` for symbols, analysts and keywords.
2. Verify the page heading/title, current URL and any selected topic, date, tab or query before reading results.
3. For a list, capture only the requested current items with their displayed date/source context and linked symbol. Do not treat a page of results as exhaustive unless pagination and scope are verified.
4. For an article or news detail page, read the title, visible summary/body, author/source, linked instruments, disclosure text, comments count and access state. Record what is visible versus gated.
5. For the earnings calendar, select the requested date/range, then use `EPS`, `Revenue`, or `Analysts Revisions & Ratings`; verify the date state, selected tab and table columns/rows.
6. For a market table or chart, preserve the displayed units, interval and as-of context. Re-fetch live values rather than relying on this skill or prior results.
7. If the task becomes a company-level financial or valuation analysis, hand off to `$seeking-alpha-stock-analysis`; if it becomes a set/ranking/filter task, hand off to `$seeking-alpha-screening`.

## Page and field semantics

- Analysis list cards connect title, author, symbol, comments and article detail; `Show summaries` may change the visible list representation.
- Market news cards connect headline, topic, linked symbol, comments and news detail; topic links such as Technology, AI, IPO, Energy, Dividend, Trending and Top News are route families, not fixed current inventories.
- Earnings tables can show report timing, market cap, current-quarter estimates, actuals, beat/miss and recent history. Do not confuse estimates with actuals.
- Article pages contain third-party author opinion plus analyst and Seeking Alpha disclosure. A registration or Premium gate is an access boundary.

## Safety and limits

Use read-only operations. Do not Save, Share, Follow, Like, comment, subscribe, purchase, create an account, enter sensitive data, or bypass a paywall/CAPTCHA. Current headlines, numbers, rankings, article availability and result counts are dynamic and must be reported with observation time.

## Drift maintenance

Before acting, compare the current route, heading, labels, filters, tab state, permissions and first-party explanations with this procedure. If a stable mismatch is safely verified, update the owning skill/reference and re-run the affected read-only workflow plus the validator. Never write current headlines, prices, counts, rankings, personal data, credentials, cookies or tokens into the repository.

## References

- [site-map.md](../../sites/seeking-alpha/references/site-map.md) — route families and page coverage.
- [form-controls.md](../../sites/seeking-alpha/references/form-controls.md) — search, news, article and earnings controls.
- [data-model.md](../../sites/seeking-alpha/references/data-model.md) — article, news, instrument and earnings relationships.
- [first-party-guidance.md](../../sites/seeking-alpha/references/first-party-guidance.md) — disclosures and source limits.
