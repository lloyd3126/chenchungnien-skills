---
name: statementdog-market
description: Explore current Statement Dog market, industry, topic, news, blog, and industry-report information through the Codex in-app browser. Use when the user asks about TAIEX, sector performance, market focus, concept stocks, supply chains, articles, or site-authored industry research.
---

# Statement Dog market and content

Use this skill for market-wide or site-content research. These pages are dynamic views of current prices, performance, concepts, articles, and reports; re-open the relevant page for every task.

## Entry points

Work only in the Codex in-app browser. Main routes are:

- `/taiex` — TAIEX and industry performance overview; industry detail follows `/taiex/<slug>`.
- `/market-trend` — market-focus visualization with market, period, and scale filters.
- `/tags/<id>` — concept/topic page with supply-chain categories, company cards, reasons, and related news.
- `/news`, `/news/trending`, `/news/latest` — recommended, popular, and latest news views.
- `/blog/` — site blog with category navigation and article search.
- `/industry_reports` and `/industry_reports/<id>` — industry-report list and detail pages.

Read `sites/statementdog/references/site-map.md` for the navigation inventory and `data-model.md` for topic, industry, article, and report relationships.

## Workflow

1. Choose the page type from the user's request. Use `/taiex` for broad market/industry performance, `/market-trend` for current moving concepts, `/tags/<id>` for a named concept, `/news` or `/blog/` for current articles, and `/industry_reports` for long-form site research.
2. On `/taiex`, read the update date and the page's own explanation before comparing sectors. If the user asks whether the index is high or low, include the site's warning that an absolute TAIEX level is not sufficient and that market P/B is a relative reference.
3. On `/market-trend`, verify the selected market (`全部`, `台股`, `美股`), period (`1天`, `1周`, `1月`, `3月`, `YTD`, `1年`), and scale. After changing a filter, verify the visible visualization or labels changed; do not rely on the URL alone.
4. On a topic page, distinguish benefit/supply-chain categories, company cards, benefit levels, reasons, related news, and related tags. Use the company link to route a specific stock to the stock-analysis skill.
5. On news or blog pages, record the active category and article date. For blog search, submit the visible `搜尋文章` field and verify the resulting `/blog/search/<encoded-term>` page when the current UI supports it; treat the result list as dynamic and fall back to visible category/article links if submission does not change the page.
6. On an industry report, use the report's headings to locate the requested process, supply-chain map, company summary, or mentioned stocks. Follow links to topics or companies only when needed.
7. Read site-authored explanations such as `怎麼判斷大盤指數高低`, report methodology buttons, and terminology help before paraphrasing the site's definitions.

## Interpretation and limitations

Current performance percentages, company counts, article lists, topic reasons, rankings, and report contents are dynamic. Keep them out of the skill and references. Cite the page and its update state in the user-facing answer when freshness matters.

Statement Dog's disclaimer says its information is an auxiliary reference, may contain delay or errors, and should not replace official disclosures or be treated as a recommendation. For an investment conclusion, clearly separate the site's description from the user's decision and consult `first-party-guidance.md`.

Some topic controls may be custom widgets: a click is only verified when the checked state or visible content changes. Some concept blocks may not expose semantic links in the current DOM. Report such behavior as unverified rather than claiming an interaction worked.

## Authentication and safety

If the current visible page clearly shows an authenticated session, no separate permission question is needed to inspect safe protected content routes; re-check public content paths in that authenticated state. If authentication is not visible, complete the public exploration first, ask whether protected exploration is wanted, and let the user sign in manually.

Do not publish, comment, subscribe, purchase, send messages, or alter account data while exploring. Opening an article or report is safe; following an external link is not by itself evidence that Statement Dog endorses or verifies the destination.

## Drift maintenance

If a route, filter, tab, page heading, or control behavior changes, use the current UI to finish the safe task and update the relevant site reference and this skill. Do not preserve current market values or article titles as stable knowledge.

## References

- `sites/statementdog/references/site-map.md` — market, topic, content, and report routes.
- `sites/statementdog/references/data-model.md` — industry, topic, article, report, and company relationships.
- `sites/statementdog/references/form-controls.md` — market filters and topic/blog interaction notes.
- `sites/statementdog/references/first-party-guidance.md` — disclaimer, TAIEX explanation, and source precedence.
