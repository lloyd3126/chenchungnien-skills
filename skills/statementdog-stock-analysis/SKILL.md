---
name: statementdog-stock-analysis
description: Inspect and explain a company in Statement Dog through the Codex in-app browser, including its overview, health checks, financial statements, profitability, safety, growth, valuation, ownership, key indicators, products, topics, and related news. Use when the user asks about a specific ticker, company page, current financial metric, or company analysis workflow.
---

# Statement Dog stock analysis

Use this skill for company-level research in Statement Dog. It is an in-app-browser operating guide, not a static database: current prices, ratios, rankings, news, and table values must be read from the current page at execution time.

## Browser and entry

- Work only in the Codex in-app browser and the user's current same-site tab.
- Start at the current Statement Dog tab or `https://statementdog.com/`.
- Use the homepage search field `搜尋個股或題材` when the user provides a name or topic. Prefer the autocomplete result that identifies the requested company, then verify the URL and page heading.
- A company page normally uses `/analysis/<ticker>`. `/analysis` may redirect to the site's default company page, so it is not a company-list entry point.
- Read `sites/statementdog/references/site-map.md`, `data-model.md`, and `form-controls.md` when the request spans several sections or uses a form.

## Workflow

1. Identify the company and market from the page identity, ticker, and breadcrumb. Do not infer a ticker from a partial name when autocomplete offers multiple matches.
2. Record the current page date or update timestamp when the answer depends on freshness.
3. Read the overview before drilling down. Separate company identity, latest activity, topics, investment highlights/risks, important metrics, related news, business, and industry/competition sections.
4. Use the section navigation to open the relevant specialized page:
   - `最新動態`: `/analysis/<ticker>/`
   - `股票健診`: `/analysis/<ticker>/stock-health-check`
   - `財務報表`: `/analysis/<ticker>/monthly-revenue`
   - `獲利能力`: `/analysis/<ticker>/profit-margin`
   - `安全性分析`: `/analysis/<ticker>/financial-structure-ratio`
   - `成長力分析`: `/analysis/<ticker>/monthly-revenue-growth-rate`
   - `價值評估`: `/analysis/<ticker>/pe`
   - `董監與籌碼`: `/analysis/<ticker>/broker-trading`
   - `關鍵指標`: `/analysis/<ticker>/long-term-and-short-term-monthly-revenue-yoy`
   - `產品組合`: `/analysis/<ticker>/product-revenue`
5. For pages with year/range selectors, inspect the available options, choose the requested period, wait for the table/chart to update, and verify the selected values and visible result. Do not report a changed URL as proof of a changed result.
6. Follow links such as `詳細數據`, `指標解釋`, `查看`, or `查看完整健診細節` when the user needs methodology or a reason behind a signal.
7. Distinguish Statement Dog's interpretation from primary-source data. When relevant, check the page's source note and defer discrepancies to the official source described in `first-party-guidance.md`.
8. Route a company discovered in a topic, industry, ranking, or report back to its `/analysis/<ticker>` page before making company-level claims.

## Page semantics

The company overview is a hub. It can connect a company to topics, related news, business/industry descriptions, and metric-specific analysis pages. Specialized pages are the authoritative UI location for the corresponding metric family, while health-check pages group rule-based signals such as value, growth, safety, quality, turnaround, and chip/ownership checks.

Treat all displayed figures, dates, ranking positions, latest-news titles, and health-check statuses as dynamic. Preserve the site's terminology and units. For example, a revenue table may state that the unit is thousand NTD and that the data comes from the Market Observation Post System; do not silently convert or mix units.

## Authentication and safety

If the current visible page clearly shows an authenticated session, do not ask a separate permission question merely to inspect login-dependent company features. Re-check the public route/forms in that authenticated state, then continue through safe protected branches. If authentication is not visible, finish the public workflow first; ask whether to explore protected features, and let the user perform any sign-in manually in the in-app browser.

Do not submit the company-opinion textbox, follow/unfollow, save/bookmark, delete, purchase, export private data, change account settings, or perform any other representational or irreversible action unless the user explicitly asks and the action is confirmed at the appropriate point. A paywall, usage limit, CAPTCHA, or unavailable page is a result to report, not a reason to bypass controls.

## Drift maintenance

Never hard-code current numbers into a reusable skill. If a control, route, label, or page behavior differs from these instructions, complete the user's task using the current UI, record the observed drift, and update the most relevant site reference and this skill when the change is stable enough to document. Keep transient values out of the repository.

## References

- `sites/statementdog/references/site-map.md` — routes, page types, and coverage status.
- `sites/statementdog/references/data-model.md` — company, metric, topic, industry, and article relationships.
- `sites/statementdog/references/form-controls.md` — search and period-selector behavior.
- `sites/statementdog/references/first-party-guidance.md` — site disclaimer, data-source precedence, and methodology notes.
