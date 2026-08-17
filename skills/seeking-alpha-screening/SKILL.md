---
name: seeking-alpha-screening
description: Find, filter, sort and compare current Seeking Alpha stocks or ETFs through the Codex in-app browser, including preset screeners, custom screening entry points, Quant or dividend-oriented screens, result tables and comparison handoffs. Use when the user wants a set, ranking, filter, screen or cross-symbol comparison rather than one company's full analysis.
---

# Seeking Alpha screening

## Purpose and entry point

Use this skill when the answer should be a set of instruments, a ranking, a screen or a comparison. Start at `/screeners` in the current Codex in-app browser tab and use visible preset links or the visible custom-screen entry. Read [site-map.md](../../sites/seeking-alpha/references/site-map.md), [form-controls.md](../../sites/seeking-alpha/references/form-controls.md), and [data-model.md](../../sites/seeking-alpha/references/data-model.md) for route and field semantics.

## Procedure

1. Translate the request into the site's visible universe, preset screen or custom criteria. If the requested metric is not exposed by the current UI, say so instead of substituting another metric.
2. On `/screeners`, inspect the visible preset card label and description, then open the card link when it matches the user's intent. Verify the destination heading and criteria before reading rows.
3. For custom screening, inspect the actual current controls, operators, units, periods, sort controls and reset behavior. The complete custom field set was not verified in the public pass, so do not invent selectors or silently claim that a screen was applied.
4. Record the criteria, universe, sort order, selected filters, page/date state and whether the result is paginated. Current rows, counts, prices, ratings and ratios are dynamic.
5. Verify a screen with at least the screen heading, criteria/filter state, result table headers and visible result rows. A changed URL or clicked card alone is not enough.
6. Open a result's symbol page and hand off company-level interpretation to `$seeking-alpha-stock-analysis`. Use `$seeking-alpha-market-research` for linked market/news context.
7. Use `/comparison` only after re-checking the current visible comparison UI; the route is present in navigation but the full interaction was not verified in this pass.

## Page and field semantics

- The overview shows preset screens such as all stocks, top-rated stocks, Quant-oriented screens, dividend screens, growth/value/small-cap screens and ETF screens; labels and result sets can change.
- A screen definition consists of an instrument universe plus criteria, operators/values, optional time period, sort and result scope. A result row joins back to an Instrument.
- `Copy Screen ... link` copies a route-like screen reference; copying or saving is not necessary for read-only research and can be an external side effect.
- An account or Premium prompt such as `Unlock all filters` limits the public view. Do not bypass it or claim access to hidden criteria.

## Safety and limits

Do not save a screen, create an account, subscribe, purchase Premium, alter a portfolio, follow symbols or transmit data unless explicitly requested and confirmed at the action boundary. Treat paywalls, account prompts, empty results, query caps and CAPTCHA as observable limits.

## Drift maintenance

Compare the current screen's labels, criteria controls, table fields, permissions and first-party explanations before acting. If a stable change is directly verified, update this skill or the owning reference, then re-run the affected read-only screen and validator. Keep current rows, counts, rankings, prices, credentials, cookies, tokens and private lists out of durable files.

## References

- [site-map.md](../../sites/seeking-alpha/references/site-map.md) — screening routes and coverage status.
- [form-controls.md](../../sites/seeking-alpha/references/form-controls.md) — preset, custom and verification controls.
- [data-model.md](../../sites/seeking-alpha/references/data-model.md) — screen definitions, result rows and symbol handoff.
- [first-party-guidance.md](../../sites/seeking-alpha/references/first-party-guidance.md) — interpretation and access limits.
