---
name: statementdog-stock-research
description: Turn a Statement Dog report, investment thesis, local report snapshot, or ticker into reproducible read-only stock research. Use to verify a company's business and industry role, revenue and profit trends, earnings quality and safety, valuation, price/news context, competitive advantage, and monitoring plan; also use for report-mentioned candidates or the historical 財報狗教你挖好股穩賺20% workflow.
---

# Statement Dog stock research

Coordinate the path from a report or ticker to company-level verification. Keep historical narrative, observed company data, and analyst interpretation separate.

Read [../statementdog-market/references/research-contract.md](../statementdog-market/references/research-contract.md) for source modes, claim records, the company handoff gate, statuses, and data-quality checks. Use [../statementdog-market/references/method-routing.md](../statementdog-market/references/method-routing.md) to select only the relevant domain method.

Read [tutorial-methodology.md](references/tutorial-methodology.md) for the research order distilled from the 67 foundation-tutorial articles and comments. Read [book-workflow.md](references/book-workflow.md) only when the user requests the historical eight-step screen or its thresholds. Read [industry-metric-matrix.md](references/industry-metric-matrix.md) for role-specific operating and financial traces.

## Route the work

- Use `$statementdog-market` to read or reconstruct an industry report, article, topic, series timeline, comments, and report-mentioned candidates.
- Use `$statementdog-screening` only when a task actually requires site filters, result lists, sorting, pagination, or screen freshness.
- Use `$statementdog-stock-analysis` for the current metrics and four-part analysis of one company.
- Use `$statementdog-watchlist` only when the user explicitly requests personal tracking data. This workflow is otherwise read-only.

## Choose the research track

Record both the track and source mode before starting:

- `direct_ticker`: research a named company. Do not require a cross-sectional screen.
- `report_handoff`: verify explicit or inferred candidates against the report thesis. Complete the role-exposure gate before ratios.
- `historical_screen`: apply the book-derived conditions to narrow a universe only when the user asks for that screen or methodology.

For `direct_ticker` and `report_handoff`, also record `quick_triage` or `full_research` depth. Use quick triage only when the user asks for a fast first pass; apply the rough safety, ROE, and valuation checks in [tutorial-methodology.md](references/tutorial-methodology.md) after confirming company identity, and list what still requires full research.

Use `current_site`, `local_snapshot`, or authorized `mixed` mode as defined in the research contract. In local mode, do not claim current prices, ratios, news, filings, UI labels, or thesis validation; mark them `current_not_checked`.

## Workflow

### 1. Define identity, scope, and evidence

Record ticker, company, market, source mode, observation/capture date, and requested depth. For report handoff, also record report/file, date, section, series, and `explicit`, `inferred`, or `unverified` candidate status.

Confirm what the company sells, its major products, customer/end-market mix, geography, industry-chain role, and whether the relevant exposure is material or undisclosed. Do not begin with a ratio dump.

### 2. Build the thesis card

Write one testable card before judging the stock:

- normalized product, end market, geography, period, and unit;
- structural, cyclical, product-transition, or policy/pull-forward driver;
- demand, inventory, usable supply, capacity, price/mix, and substitution mechanism;
- exact company role and competitive-advantage hypothesis;
- expected operating trace, then revenue, margin, working-capital, capex, and cash-flow trace;
- time horizon, catalyst, earliest invalidator, and unavailable evidence.

Use the domain method and role matrix to choose the right indicators. A good industry story that cannot be connected to role exposure and measurable traces is still unverified.

### 3. Apply screening only when it fits the track

For `historical_screen`, apply the book defaults with the current equivalent controls when live access is authorized:

1. one-year and five-year-average ROE above 15%;
2. one-year and five-year-average net margin above 10%;
3. one-year and five-year-average operating cash flow/net profit above 50%;
4. one-year and five-year-average free cash flow per share above 0;
5. record complete results, active conditions, periods, pagination, and update state;
6. inspect industry direction, durable advantage, and the four capital-intensity warnings;
7. inspect the current valuation equivalent; the book used dividend-discount returns above 10%, with 15% as a stricter reference;
8. inspect whether short-term revenue growth breaks above long-term revenue growth using the exact displayed periods.

These are historical defaults, not universal buy rules. For `direct_ticker` or `report_handoff`, use relevant metrics diagnostically; do not reject or approve a company solely because it crosses these thresholds. If a live control is renamed, protected, or unavailable, record that boundary without silent substitution.

### 4. Verify the company in a fixed order

1. **Business and industry role** — products, customers, end markets, capacity, pricing, product cycle, capital intensity, and actual report exposure.
2. **Industry thesis and competitive advantage** — test demand, supply, inventory, qualification, substitution, timing, and the claimed cost/yield/technology/customer/scale/service advantage with role-specific operating evidence.
3. **Revenue and growth** — use year-over-year and cumulative year-over-year trends where seasonality matters; separate volume, units/bits/content, ASP, mix, pull-forward, backlog conversion, and acquisitions.
4. **Profitability** — gross, operating, and net margin; EPS; ROE/ROA and DuPont drivers. Separate price/mix, cost, operating expense, non-operating items, asset efficiency, leverage, and dilution.
5. **Earnings quality and safety** — CFO/net income, FCF, receivables and inventory turnover/days, debt composition, liquidity, capex/depreciation, equity issuance, convertibles, treasury stock, and share count. Explain productive expansion rather than treating every negative FCF period as failure.
6. **Valuation, price, and news context** — use PE/PB or the current equivalent against expected 3–5 year growth, cycle position, asset quality, and peer economics. Use price to judge expectations and valuation, not to prove operations. Treat news as a hypothesis until official disclosure and later operating data support it.
7. **Monitoring and invalidation** — define monthly revenue checks, quarterly margin/cash/balance-sheet checks, role-specific industry events, and the exact condition that would change the conclusion.

Before comparing values, apply the research contract's period, consolidation, averaging, unit, currency, one-off, share-count, backlog, and usable-capacity checks. Financial-sector thresholds are not silently comparable with ordinary operating companies.

### 5. Assign evidence and result states

For each material item, separate:

- `observed`: source, page/section, period, value or qualitative event, and observation date;
- `interpretation`: what the evidence suggests through the stated mechanism;
- `risk`: plausible alternative explanation or invalidator;
- `unknown`: unavailable, protected, stale, ambiguous, or `current_not_checked` data;
- `next_check`: exact metric, filing, monthly/quarterly release, qualification, installation, or customer event.

Use `pass`, `fail`, or `unknown` only against an explicit screen criterion. For historical claims, use `not_tested`, `supports`, `weakens`, `cannot_test`, `unresolved`, or `not_applicable`. A screen pass, report mention, order, design win, or price rise is not a buy signal.

## Output

Present:

1. scope, track, source mode, and completeness;
2. thesis card and normalized causal chain;
3. candidate source and company-role exposure;
4. role-specific operating indicators and competitive-advantage evidence;
5. revenue/profitability, safety/earnings quality, valuation, price/news context, and monitoring;
6. observed evidence, interpretation, risks, unknowns, and next checks;
7. historical-claim validation and investment direction without turning it into personalized trade advice.

Rank or group companies only when requested. Preserve screen order otherwise. Keep current prices, ratios, rankings, news, report conclusions, and company recommendations out of this skill and its references.

## Browser and safety boundary

Use the Codex in-app browser only for authorized current Statement Dog work. Start from the user's current same-site tab when available and follow `browser:control-in-app-browser`. In local mode, remain offline.

Do not save filters, change portfolios or watchlists, follow/unfollow, post, purchase, export private data, place trades, change account settings, bypass access controls, or perform another state-changing action without an explicit user request and any required confirmation.

## References

- [tutorial-methodology.md](references/tutorial-methodology.md) — archive-derived company research order and accounting cautions.
- [book-workflow.md](references/book-workflow.md) — historical eight-step screen and thresholds.
- [industry-metric-matrix.md](references/industry-metric-matrix.md) — cross-industry role, operating-trace, financial-trace, and false-positive matrix.
- [../statementdog-market/references/research-contract.md](../statementdog-market/references/research-contract.md) — evidence and handoff contract.
- [../statementdog-market/references/method-routing.md](../statementdog-market/references/method-routing.md) — domain-method routing.
