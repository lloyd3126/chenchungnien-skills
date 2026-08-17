---
name: statementdog-stock-research
description: "Turn a Statement Dog industry report or investment thesis into a reproducible, read-only stock research workflow: extract candidates, apply the book-derived eight-step screen, inspect the industry, and verify each company through profitability, safety, valuation, and growth. Use when the user asks to find stocks from a report, screen report-mentioned companies, follow the 財報狗教你挖好股穩賺20% process, or build an evidence-based Statement Dog research checklist."
---

# Statement Dog stock research

Coordinate the complete path from an industry report to company-level verification. Keep the report's narrative, the site's dynamic data, and the analyst's interpretation separate.

## Route the work

- Use `$statementdog-market` for the current industry report, article, topic, or report-mentioned company links.
- Use `$statementdog-screening` for the site screen, conditions, result list, sorting, pagination, and screen freshness.
- Use `$statementdog-stock-analysis` for one company's current metrics and four-part analysis.
- Use `$statementdog-watchlist` only when the user explicitly asks to inspect or modify personal tracking data. This workflow is read-only by default.

Read [book-workflow.md](references/book-workflow.md) for the historical thresholds, sequence, and output checklist derived from *財報狗教你挖好股穩賺20%*.

## Workflow

### 1. Define the research scope

Identify the report URL or file, report title/date, theme, and whether the user wants all mentioned companies or only a subset. If the report is part of a series, group related reports under one theme and preserve each report's date and evidence.

Extract only evidence-backed candidates:

- Record every explicitly named company, ticker, topic/company link, and the section where it appears.
- Distinguish `report-mentioned` candidates from `inferred` candidates. Never present an inferred candidate as if the report named it.
- Summarize the report's supply/demand, capacity, product-cycle, pricing, and industry assumptions before screening companies.
- If the report contains no usable candidate list, say so and ask whether to screen a clearly defined industry universe; do not invent a universe silently.

### 2. Apply the report-derived screen

Use the current Statement Dog UI and the equivalent current controls. Treat the PDF's thresholds as defaults, not immutable site facts:

1. Long-term ROE: recent one-year data and recent five-year average both above 15%.
2. Long-term net margin: recent one-year data and recent five-year average both above 10%.
3. Operating cash flow to net profit: recent one-year data and recent five-year average both above 50%.
4. Free cash flow per share: recent one-year data and recent five-year average both above 0.

After the four initial conditions, run the remaining checks in this order:

5. List and record the screen results, active period, result count if visible, pagination state, and update/freshness information.
6. Inspect the industry: long-term direction, durable company advantage, and whether the industry has the four “burning money” warning characteristics described by the book.
7. Check valuation using the current Statement Dog valuation equivalent. The book's default is dividend-discount return above 10%, with a stricter 15% reference during a depressed market.
8. Check growth using the current short-term versus long-term revenue-growth equivalent. The book's default is short-term revenue growth breaking above long-term revenue growth.

Apply only requested or documented conditions. If the current UI lacks a condition, a period, or the VIP feature, mark it `unavailable` or `protected` and explain the limitation; do not silently substitute a different metric.

### 3. Verify each surviving company

Open each result on its company analysis page and verify the ticker, company identity, market, and current update state before interpreting it. Use this fixed order:

1. **Profitability** — long-term ROE and net margin; then industry value trend and competitive position.
2. **Safety** — operating cash flow relative to net profit and free cash flow; then debt or balance-sheet warnings when material; confirm the company is not merely a cash-burning business.
3. **Valuation** — current valuation measure, dividend-discount or equivalent return signal, comparison with the industry, and the reason for any apparent under- or over-valuation.
4. **Growth** — short-term and long-term revenue growth, plus the industry drivers, products, markets, or customers that could sustain or weaken growth.

For every part, record:

- the current page/section and period used;
- the displayed value or qualitative signal;
- `pass`, `fail`, or `unknown` against the research criterion;
- evidence, caveat, and what would change the conclusion.

Finish each company with an `investment direction` statement that distinguishes observed facts, interpretation, risks, and unresolved items. Do not collapse “passes the screen” into “buy”.

### 4. Report the result

Use a compact evidence-first structure:

1. Research scope and report evidence.
2. Industry thesis and assumptions.
3. Candidate list and source sections.
4. Screen conditions, current site state, and result completeness.
5. Industry checks.
6. Per-company table: profitability, safety, valuation, growth, status, evidence, and risk.
7. Ranking or grouping only when the user asks for it; otherwise preserve the screen order.
8. Limitations: stale report data, unavailable controls, protected VIP data, missing periods, or incomplete pagination.

Separate historical book rules from current site results. Current prices, ratios, rankings, company counts, news, and update dates must be fetched at task time and must never be written into this skill or its references.

## Browser and safety boundary

Use the Codex in-app browser for current Statement Dog UI work, following `browser:control-in-app-browser`. Start from the user's current same-site tab when available. Read-only inspection and safe navigation are the default.

Do not save filters, modify portfolios, follow/unfollow, post comments, purchase a plan, export private data, place trades, change account settings, or perform another irreversible action unless the user explicitly requests it and the required confirmation is obtained at the action boundary. Never bypass a paywall, query cap, CAPTCHA, or login gate. If protected data is needed and authentication is not visibly active, let the user sign in manually in the same in-app browser tab.

Treat the PDF's website screenshots as historical operating evidence. Before using a control, compare its label, route, period, and result behavior with the current UI. If they differ, use the current first-party UI as the source of truth and record the drift without storing live values.

## Maintenance

When a route, label, metric definition, period selector, or workflow behavior changes, update the owning Statement Dog skill or site reference only after the difference is clearly observed and safely verified. Keep public and authenticated variants separate, preserve unrelated edits, and run the repository's `quick_validate.py` after changing a skill.
