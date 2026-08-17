---
name: seeking-alpha-stock-analysis
description: Inspect a current Seeking Alpha stock or ETF symbol page through the Codex in-app browser, including quote context, ratings, financials, earnings, dividends, valuation, growth, profitability, momentum, peers, options, charting, related analysis, news, filings and press releases. Use when a user asks about one ticker, company, ETF, symbol page, or company-level analysis workflow.
---

# Seeking Alpha stock analysis

## Purpose and entry point

Use this skill for one company, stock or ETF at a time. Work only in the Codex in-app browser and start from the current Seeking Alpha tab or `https://seekingalpha.com/`. Use the global search field when the user gives a name instead of a ticker, then verify the chosen symbol page.

Read [site-map.md](../../sites/seeking-alpha/references/site-map.md), [data-model.md](../../sites/seeking-alpha/references/data-model.md), and [first-party-guidance.md](../../sites/seeking-alpha/references/first-party-guidance.md) when the task spans multiple sections or needs interpretation limits.

## Procedure

1. Identify the instrument from the visible symbol, company name, asset type and page heading. Do not guess when autocomplete offers multiple symbols.
2. Open `/symbol/<ticker>` and record the observation time, current page identity and the requested top-level tab.
3. Use the symbol tabs for the requested scope: `Summary`, `Ratings`, `Financials`, `Earnings`, `Dividends`, `Valuation`, `Growth`, `Profitability`, `Momentum`, `Peers`, `Options`, or `Charting`.
4. Use content tabs such as `Analysis`, `News`, `Comments`, `Transcripts & Insights`, `SEC Filings`, `Press Releases`, or `Related Analysis` when the request concerns company-linked content.
5. Read the requested fields in their displayed units and distinguish quote, site rating, estimate, actual, author opinion and disclosure. Do not mix live values with historical values without dates.
6. After each tab or filter change, verify the selected state plus the resulting heading, table, chart or section. A URL change alone is insufficient.
7. For a linked article or market-news item, hand off full content reading to `$seeking-alpha-market-research` when the task is primarily article/news research.

## Page and field semantics

- The symbol page is a hub that joins the Instrument to ratings, financial statements, earnings, dividends, valuation, growth, profitability, momentum, peers, options, charts, articles, news, transcripts, SEC filings and press releases.
- Treat `Quant`, `SA Author`, and `Wall Street` ratings as separate site-generated or third-party evidence layers. Preserve the label and timestamp; do not turn them into personal advice.
- Current quote, yield, market cap, estimates, chart points, ratings and related content are dynamic. Re-fetch them for every request.
- If an article body is gated, report the visible summary and registration/Premium boundary rather than bypassing it.

## Safety and limits

Read-only inspection is the default. Do not Follow, Save, Like, Share, comment, create a portfolio, place a trade, subscribe, purchase, enter credentials, or change account state unless the user explicitly requests the exact action and the browser confirmation boundary is satisfied. Treat a paywall, CAPTCHA, login prompt or query limit as a result.

## Drift maintenance

Compare the live page's route, headings, tab labels, fields, permissions and first-party explanations with this procedure before acting. If a stable difference appears, complete the safe task with the current UI, update the owning site reference or skill with the evidence and date, and re-run the affected workflow and validator. Keep dynamic values, private data, credentials, cookies and tokens out of the repository.

## References

- [site-map.md](../../sites/seeking-alpha/references/site-map.md) — symbol routes and coverage.
- [data-model.md](../../sites/seeking-alpha/references/data-model.md) — instrument, article, news and earnings relationships.
- [form-controls.md](../../sites/seeking-alpha/references/form-controls.md) — symbol tabs and verification rules.
- [first-party-guidance.md](../../sites/seeking-alpha/references/first-party-guidance.md) — disclosures and interpretation limits.
