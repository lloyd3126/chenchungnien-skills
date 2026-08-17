---
name: statementdog-market
description: Explore current Statement Dog market, industry, topic, news, blog, and industry-report information in the Codex in-app browser, or analyze user-provided local Statement Dog report snapshots without browsing. Use for TAIEX, sector performance, market focus, concept stocks, supply chains, articles, report-series reading, comments/replies, forecast timelines, and report-to-company handoff.
---

# Statement Dog market and content

Use this skill for market-wide, site-content, and industry-report research. Choose the source mode before reading:

- `current_site`: use the Codex in-app browser and re-open dynamic pages for the task.
- `local_snapshot`: use only provided or existing local files when the user requests offline work; do not infer current values or site state.
- `mixed`: combine historical local evidence with a separately authorized live check while preserving both dates.

For industry reports, first read [research-contract.md](references/research-contract.md). For a multi-report or comment/reply task, also read [industry-report-methodology.md](references/industry-report-methodology.md). Use [method-routing.md](references/method-routing.md) to select only the relevant domain methodology.

## Current-site entry points

Use these routes only in `current_site` or authorized `mixed` mode:

- `/taiex` — TAIEX and industry performance overview; industry detail follows `/taiex/<slug>`.
- `/market-trend` — market-focus visualization with market, period, and scale filters.
- `/tags/<id>` — concept/topic page with supply-chain categories, company cards, reasons, and related news.
- `/news`, `/news/trending`, `/news/latest` — recommended, popular, and latest news.
- `/blog/` — site blog with category navigation and article search.
- `/industry_reports` and `/industry_reports/<id>` — industry-report list and detail pages.

Read [../../sites/statementdog/references/site-map.md](../../sites/statementdog/references/site-map.md) for the navigation inventory and [../../sites/statementdog/references/data-model.md](../../sites/statementdog/references/data-model.md) for topic, industry, article, report, and company relationships.

## Workflow

1. Record source mode, observation or capture date, requested scope, and whether the user needs one report, a complete series, or candidate extraction.
2. Choose the page or local artifact. In `local_snapshot` mode, start from a manifest if present, read saved HTML, inspect local images, and use text only as a fallback. Never turn a snapshot into a current price, ratio, UI, news, or inventory claim.
3. For current `/taiex`, read the update date and the page's explanation before comparing sectors. If asked whether the index is high or low, include the site's warning that an absolute index level is insufficient and market P/B is only a relative reference.
4. For current `/market-trend`, verify market, period, and scale. After changing a filter, confirm the visible visualization or labels changed; the URL alone is not proof.
5. On a topic page, distinguish supply-chain category, company card, benefit level, stated reason, related news, and related tags. Route a specific stock to `$statementdog-stock-research` when a thesis or complete company check is needed.
6. On news or blog pages, record category, publication date, and observation time. Treat historical paths, lists, comments, and rankings as potentially stale.
7. On an industry report, read the full body, headings, tables, charts, diagrams, company/topic links, comments, and official replies that are available in the selected source mode. Describe what each visual supports and what it cannot prove.
8. For a series, preserve newest-to-oldest archive order, group genuine continuations by theme, normalize product/geography/period/unit scope, and build both a timeline and forecast ledger before concluding.
9. Classify every material claim and preserve its causal mechanism, expected trace, disconfirming trace, evidence stage, and status. A later report repeating a claim is continuity, not independent confirmation.
10. Mark candidates `explicit`, `inferred`, or `unverified`, preserve their source section and role, and pass them through the company handoff gate in [research-contract.md](references/research-contract.md). Report inclusion is not a recommendation.
11. Use the selected domain methodology for product-specific indicators, capacity timing, commercialization stages, substitution, and invalidation rules.
12. Route company-level financial, valuation, price, news, and monitoring verification to `$statementdog-stock-research`.

## Interpretation and limitations

Keep these layers separate:

- historical report observation, assumption, forecast, or example;
- reader question or disputed correction;
- author/official clarification;
- analyst inference;
- current evidence with its own observation date;
- unavailable or `current_not_checked` evidence.

Current percentages, company counts, article lists, rankings, report contents, UI labels, and comments are dynamic. Keep them out of the skill. Do not treat `not_present_at_read_time` as proof that comments never existed.

Statement Dog describes its information as an auxiliary reference that may contain delays or errors and should not replace official disclosures or be treated as a recommendation. Consult [../../sites/statementdog/references/first-party-guidance.md](../../sites/statementdog/references/first-party-guidance.md) when presenting an investment conclusion.

Some controls are custom widgets. A click is verified only when checked state or visible content changes. Report unverified behavior rather than claiming the interaction worked.

## Authentication and safety

If a current page visibly shows an authenticated session, safe read-only inspection does not require a separate permission question. If authentication is absent, complete public exploration first and let the user sign in manually when protected content is needed.

Do not publish, comment, subscribe, purchase, send messages, save reports, modify watchlists, change account data, bypass a paywall/CAPTCHA/query limit, or perform trading actions during research.

## Drift maintenance

If a route, filter, tab, heading, metric definition, or control changes, finish the safe task using the visible current UI and update the owning site reference only after verification. Never store current market values, article titles, report conclusions, or company recommendations as permanent skill knowledge.

## References

- [research-contract.md](references/research-contract.md) — source modes, scope normalization, claim schema, status vocabulary, handoff gate, and data-quality checks.
- [industry-report-methodology.md](references/industry-report-methodology.md) — article-by-article reading, visuals, comments/replies, series comparison, and output records.
- [method-routing.md](references/method-routing.md) — routes a claim or company role to the relevant domain method.
- [../../sites/statementdog/references/site-map.md](../../sites/statementdog/references/site-map.md) — market, topic, content, and report routes.
- [../../sites/statementdog/references/data-model.md](../../sites/statementdog/references/data-model.md) — site entities and relationships.
- [../../sites/statementdog/references/form-controls.md](../../sites/statementdog/references/form-controls.md) — filter and interaction notes.
- [../../sites/statementdog/references/first-party-guidance.md](../../sites/statementdog/references/first-party-guidance.md) — disclaimer, TAIEX explanation, and source precedence.
