---
name: statementdog-screening
description: Build, inspect, compare, and verify Statement Dog stock screens through the Codex in-app browser, including custom conditions, quality and turnaround lists, revenue, dividend, P/E and gross-margin rankings, sorting, pagination, and company comparison. Use when the user wants to find or rank stocks by site-supported criteria.
---

# Statement Dog screening

Use this skill when the requested result is a set, ranking, comparison, or filter rather than one company's full analysis. Execute the screen in the current Statement Dog UI and report the criteria, page state, and freshness together with the result.

## Entry points

Work only in the Codex in-app browser. Main routes are:

- `/screeners` — screening overview and strategy cards.
- `/screeners/custom` — custom conditions and saved-list areas.
- `/screeners/quality` and `/screeners/turnaround` — rule-based strategy lists.
- `/screeners/revenues_ranking`, `/screeners/dividend_yield_ranking`, `/screeners/pe_ranking`, `/screeners/gross_margin_ranking` — metric rankings.
- `/compare/tpe` — comparison workspace for selected Taiwan stocks.

Read `sites/statementdog/references/form-controls.md` for observed control semantics and `data-model.md` for the relationship between a result row and a company analysis page.

## Workflow

1. Translate the request into the site's available strategy, ranking, or custom condition. If the user asks for a metric not exposed by the current screen, say so instead of silently substituting another metric.
2. For custom screening, inspect the criterion label beside each paired control. The usual pattern is an operator select (`大於`/`小於`) plus a criterion-specific value select. Check the period label such as `近一季數據`, `近一年數據`, or a multi-year average before choosing a value.
3. Apply only the requested conditions, then use `開始選股`. Use `清空` only when it is safe to discard the current unsaved form. Do not use `儲存條件`, `儲存篩選條件`, or a personal-list control without explicit confirmation.
4. For quality or turnaround lists, read the linked `策略選股原理` and, when methodology matters, `策略歷史績效`. Preserve the site's rule explanation; do not infer a strategy from the current rows alone.
5. For ranking pages, record the heading's current period, inspect the available sort links, select the requested sort, and verify that the visible order or result changed. Some sorting is AJAX-like and may leave the URL unchanged.
6. Use `查看下 100 家公司` or equivalent pagination only when the user needs more rows. Do not assume the first page represents the whole universe.
7. For comparison, enter only the requested symbols, inspect the year selectors, and report a paywall or daily query cap as a limitation. Never purchase a plan or bypass the limit.
8. Open a result's company link and use the stock-analysis skill for company-level interpretation. Keep the screen's selection logic separate from later qualitative analysis.

## Verification and interpretation

Every screening answer should include the screen type, conditions or sort order, page date/update state, and whether the displayed list is complete or paginated. Current rows, counts, prices, ranks, and ratios are dynamic and must not be written into reusable references.

The site's quality strategy explanation is itself a first-party definition: it describes filtering free-cash-flow-return deterioration, ranking three-year average free-cash-flow return, P/B, P/E, and dividend yield, then combining ranks. Read `first-party-guidance.md` before explaining that methodology.

## Authentication and safety

If the current visible page clearly shows an authenticated session, no extra permission question is needed to inspect safe login-dependent screening areas. Re-check public screen routes/forms in that state. If authentication is not visible, finish public screening first, ask whether to explore protected functionality, and let the user sign in manually.

Do not save a screen, alter a tracking list, send a message, buy a subscription, export private data, or perform another external or irreversible action unless the user explicitly requests it and confirms the final action. A blocked feature, query cap, or paywall should be reported as observed.

## Drift maintenance

When the UI differs, use the current controls to complete the task if safe, then update the relevant site reference and this skill with the stable route/control change. Never store current ranking values or stock rows as skill knowledge.

## References

- `sites/statementdog/references/site-map.md` — screening routes and page taxonomy.
- `sites/statementdog/references/data-model.md` — screen, ranking, metric, and company relationships.
- `sites/statementdog/references/form-controls.md` — custom-screen controls, sorting, pagination, and comparison controls.
- `sites/statementdog/references/first-party-guidance.md` — strategy definitions and source precedence.
