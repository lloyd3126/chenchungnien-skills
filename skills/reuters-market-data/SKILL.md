---
name: reuters-market-data
description: Inspect current Reuters Markets pages, regional tabs, quote tables, securities lookup, and LSEG-delayed market data through the Codex in-app browser. Use for Reuters index, commodity, currency, bond, stock, or market-section requests.
---

# Reuters Market Data

## Purpose and entry point

Use the current Reuters tab and start at `/markets/`. Read [../../sites/reuters/AGENTS.md](../../sites/reuters/AGENTS.md), then load [data-model.md](../../sites/reuters/references/data-model.md), [form-controls.md](../../sites/reuters/references/form-controls.md), and [first-party-guidance.md](../../sites/reuters/references/first-party-guidance.md) as needed.

## Procedure

1. Verify the Reuters tab, URL, heading `Markets`, and auth state.
2. Choose a visible Markets category or stay on `/markets/` for the dashboard. Confirm the route and heading after navigation.
3. For a regional request, select `US`, `Europe`, or `Asia Pacific` and verify the selected tab, tabpanel label, loading state, and displayed cards or tables.
4. For a quote or table request, capture the instrument name, row/column label, displayed value, unit, change, as-of context, source, and delay statement. Re-fetch at answer time.
5. Use `Search for securities` only for quote lookup. Do not confuse it with the site-wide `Search Reuters` article search.
6. If the request turns into article or commentary research, hand off to `$reuters-news-search` or `$reuters-article-research`.

## Confirmed Markets structure

The category navigation exposes `On the Money`, `Asian Markets`, `Carbon Markets`, `Commodities`, `Currencies`, `Deals`, `Emerging Markets`, `ETFs`, `European Markets`, `Funds`, `Econ World`, `Global Market Data`, `Rates & Bonds`, `Stocks`, `U.S. Markets`, and `Wealth`.

The dashboard contains market-region tabs, LSEG-linked market performance blocks, and tables for commodities, currencies, rates & bonds, and stocks. Quote routes are entity-specific and must be opened and verified when the user asks for detailed history or fields.

## Safety and limits

Treat quote values, percentages, yields, ranges, and market article lists as dynamic. Preserve the displayed units and delay context; do not claim real-time data or provide investment advice from a raw quote. Do not click trading, purchase, subscription, account, or other side-effect controls.

## Drift maintenance

Before acting, compare the current visible Markets UI, tabs, controls, field labels, sources, and delay notices with this procedure. Patch this skill or the owning reference only for stable, UI-verified changes; re-run the affected read-only workflow and validator. Keep live values and public/authenticated differences out of durable instructions.

## References

- [site-map.md](../../sites/reuters/references/site-map.md) — Markets route families and page types.
- [data-model.md](../../sites/reuters/references/data-model.md) — market instrument and region relationships.
- [form-controls.md](../../sites/reuters/references/form-controls.md) — tabs, securities search, and table controls.
- [first-party-guidance.md](../../sites/reuters/references/first-party-guidance.md) — LSEG source and delay limitations.
