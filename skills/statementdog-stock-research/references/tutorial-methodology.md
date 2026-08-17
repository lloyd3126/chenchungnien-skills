# Statement Dog tutorial-derived methodology

This reference distills the 67 articles in Statement Dog's historical foundation-tutorial archive, read from newest to oldest, together with the visible reader comments and author/official replies. It is method guidance, not current market data or a current Statement Dog UI specification.

## What the archive adds

The archive shows a consistent research backbone, even though individual articles have different purposes:

`company and products → industry supply/demand and cycle → revenue trend → margins and EPS → cash quality and balance-sheet safety → valuation → monitoring`

The articles are not interchangeable. Separate:

- **Quick triage**: a fast first pass for an unfamiliar company.
- **Full research**: the book-derived eight-step screen and company verification.
- **Concept lessons**: articles that explain one metric, accounting item, or investing behavior.
- **Historical editorials and book reviews**: useful for principles, not automatic screen conditions.

## Use two screening layers without conflating them

### Quick triage from the newer tutorial

Use only when the user asks for a quick first look. Check:

1. Safety: debt ratio roughly below 50% and five-year free cash flow not persistently negative.
2. Profitability: five-year ROE roughly stable above 10%.
3. Valuation: PE below roughly 12 or low relative to its own five-year range.

These are rough filters, not buy rules. Industry, business quality, cash conversion, dilution, and current valuation still need verification.

### Full research sequence

Use the book-derived eight-step workflow in [book-workflow.md](book-workflow.md) for a complete report. Preserve its distinct defaults: ROE and net margin thresholds, CFO/net-profit ratio, free cash flow per share, industry analysis, valuation equivalent, and short- versus long-term revenue growth. Do not replace those rules with the quick-triage thresholds without saying so.

## Company research order

For each ticker, use this order and write down the period and current page section:

1. **Business identity and product mix** — confirm what the company sells, its major products/customers/markets, and the revenue mix. Use the annual report or product-business disclosure when the site summary is vague.
2. **Industry thesis** — explain demand, supply, capacity, pricing, product generation or technology cycle, capital intensity, and the company's durable advantage. A narrative is not evidence until it leaves a trace in revenue, margins, asset turnover, capex, or cash flow.
3. **Revenue growth** — prefer year-over-year and cumulative year-over-year trends over single-month or sequential growth because seasonality can mislead. Compare short-, medium-, and long-term trends and explain any crossover.
4. **Profitability** — inspect gross margin, operating margin, net margin, EPS, ROE, and ROA. Decompose improvement or deterioration into price/mix, cost, operating expenses, non-operating items, asset efficiency, and leverage.
5. **Earnings quality and safety** — compare operating cash flow with net income, calculate or inspect free cash flow, then check receivable turnover/days, inventory turnover/days, debt composition, current liabilities, fixed assets/depreciation, equity issuance, and dilution.
6. **Valuation** — use PE/PB or the current Statement Dog valuation equivalent in context of expected 3–5 year growth, industry cycle, asset quality, and peer economics. Historical highs/lows are reference ranges, not fair value by themselves.
7. **Price and news** — use price to understand valuation, market expectations, and confirmation, not as proof that the business thesis is right. Prefer official announcements, orders, capacity additions, product launches, and regulatory filings; verify the expected effect in operating data. Treat media target prices and speculative headlines as hypotheses.
8. **Monitoring plan** — after a conclusion, define what to check monthly (revenue), quarterly (margins, EPS, cash conversion, balance sheet), and when industry or product-cycle assumptions change.

## Normalize the data before interpreting it

The article comments repeatedly show that formula and period mistakes can reverse a conclusion. Before comparing a company with itself or peers, record:

- consolidated or standalone statement;
- single-quarter, cumulative, trailing-twelve-month, or annual value;
- year-over-year, sequential, or multi-period average comparison;
- average or ending assets, equity, receivables, and inventory in the denominator;
- currency, unit, scale, fiscal/calendar period, and any restatement;
- recurring operation or one-off asset sale, investment gain/loss, impairment, tax effect, or fair-value change;
- basic/diluted share count, equity issuance, convertibles, and treasury stock;
- whether the company is a financial institution or another business for which ordinary operating-company ratios are structurally unsuitable.

When the exact definition is unavailable, mark the comparison `unknown`; do not repair it with an assumed formula.

## Interpretation rules repeatedly supported by the archive

- Trend and turning point usually matter more than one absolute ratio, but only after controlling for seasonality, industry differences, and reporting scope.
- Revenue is an early signal; EPS, operating profit, and cash flow confirm whether growth is real.
- High ROE can come from high margins, efficient asset use, or leverage. A high ROE driven mainly by rising leverage is a warning, not a quality stamp.
- High dividends do not prove high quality. Check recurring earnings, cash generation, capital reserves, debt funding, and reinvestment opportunities.
- Debt is not automatically bad. Distinguish operating liabilities such as payables or advances from interest-bearing financial debt, and check whether borrowed funds produce returns.
- A one-off asset sale, investment gain, tax effect, or valuation change should not be extrapolated into recurring EPS or PE.
- Receivables and inventory must be judged by trend and industry context. Rising revenue with worsening collection or inventory turnover deserves a deeper check.
- Free cash flow is a guardrail against accounting-only growth, but negative FCF can be reasonable during productive expansion. Explain the use and expected return of the spending.
- A growing share count can dilute EPS even while revenue and net income rise. Always inspect share count, equity issuance, convertible instruments, and treasury stock when the story depends on per-share growth.
- A low PE or PB can be a value trap when earnings, margins, industry economics, or asset quality are deteriorating.

## Comment-derived operating cautions

The reader discussions are useful for validation, not as an equal source of current data:

- Recheck formulas and labels. Comments caught errors in EPS, free-cash-flow wording, turnover formulas, quick ratio, chart labels, and stock-dividend formulas.
- Confirm consolidated versus standalone statements, single-quarter versus cumulative data, and whether a ratio is based on average or ending assets.
- Financial-sector data and thresholds may not be comparable with ordinary operating companies.
- Historical comments often point to old navigation paths, VIP features, tax rules, or data coverage. Use them to understand definitions and intent, then verify the current first-party UI.
- The article header's historical response count may differ from currently visible Disqus comments. Never infer sentiment or completeness from the header count alone.
- A reader correction is a disputed point until the article, an official reply, the formula, or the underlying statement supports it. Silence is not confirmation.

## Required output discipline

For each company, separate:

- `observed`: current value, period, page section, and source;
- `interpretation`: what the value suggests and why;
- `risk`: what could invalidate the interpretation;
- `unknown`: missing, protected, stale, or ambiguous data;
- `next check`: the exact monthly, quarterly, filing, or industry event to monitor.

Never turn a screen pass into a buy recommendation. State whether the company passed a filter, whether the business thesis is supported, whether valuation is acceptable, and what remains unresolved.
