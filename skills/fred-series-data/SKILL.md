---
name: fred-series-data
description: Find, inspect, and download FRED economic data series through the Codex in-app browser. Use when the user asks for FRED data, a series ID, observations, a graph, current economic indicators, metadata, categories, sources, popular series, CSV/Excel exports, or a comparison-ready series choice.
---

# FRED Series Data

## Purpose and entry point

Use the FRED website UI to resolve an exact series, verify its metadata and current observations, and optionally obtain a read-only graph or inbound data download. Start at `https://fred.stlouisfed.org/` unless the user supplies a visible FRED route or series ID.

Read [references/series-page-fields.md](references/series-page-fields.md) when the task depends on field meanings, transformations, or download formats. Read [../../sites/fred/references/data-model.md](../../sites/fred/references/data-model.md) for entity relationships and [../../sites/fred/references/first-party-guidance.md](../../sites/fred/references/first-party-guidance.md) for provenance, help, API, or citation questions.

## Procedure

1. If the user provides a series ID, open `/series/<series_id>` in the same Codex in-app browser tab. Otherwise use the homepage `Search FRED Data...` field with a concise keyword and `Submit Search`; verify the result URL, heading, and exact series identity.
2. On the search result, choose the exact title and variant. Check the displayed unit, frequency, seasonal adjustment, date range and description; similar titles can represent different series.
3. On the series page, read the title plus series ID, current observation summary, `Updated`, `Next Release Date`, `Source`, `Release`, `Units`, `Frequency`, and `Notes`. Do not copy the current value into this skill or any reference.
4. For recent observations, open `Observations` and use its visible sample. For the full table, follow `View All` to `/data/<series_id>` and verify the metadata table and `DATE`/`VALUE` columns.
5. For a graph request, use the visible date-range controls (`1Y`, `5Y`, `10Y`, `Max`) or `Edit Graph`. Re-check the current options before selecting transformations, frequency, or comparison series; verify the chart label and active series afterward.
6. For a data export, open `Download` and choose the requested visible format. The observed menu included `CSV (data)`, `Excel (data)`, `Image (graph)`, and `PowerPoint (graph)`. Downloads are inbound; verify the browser completed the download and report its artifact path when available.
7. Report the exact series ID, query or route, metadata relevant to interpretation, retrieval time, and any freshness or revision caveat. Use the current FRED page as the source of truth.

## Discovery routes

- `Category` → browse topic hierarchy, then follow a visible category or series link.
- `Source` → browse source names, then verify the source on the target series page.
- `Popular Series` → use popularity only as a discovery hint; choose the correct frequency and seasonal-adjustment variant.
- Search results may contain many results and `other formats`; do not assume the first title is the intended series.

## Safety and limits

- Use only the Codex in-app browser and the existing active FRED tab. Do not switch to external browsers, web search, API calls, CLI fetching, cookies, local storage or session inspection.
- After navigation or interaction, verify the same tab's URL, heading, control state and result. If automation reports a client block, timeout or empty result, capture the same tab visually and retry once before classifying it.
- Keep the operation read-only. Do not add favorites, share or publish a graph, open account tools, subscribe to the newsletter, modify an account, or submit external forms.
- Current values, result counts, periods, popularity and download query parameters are dynamic. Re-fetch them for every task.

## Drift maintenance

- Compare the current visible UI, route, labels, options, permissions, metadata and first-party explanations with this procedure before acting.
- If a stable route, control, field or workflow changes, make the smallest safe adaptation, then update this skill or its owning reference with the old behavior, new behavior, evidence and date.
- Keep public and authenticated variants separate; never record passwords, cookies, tokens, private data or one-off result values.
- Re-run the affected safe workflow and `quick_validate.py` after editing. Report broad or ambiguous changes instead of guessing.

## References

- [references/series-page-fields.md](references/series-page-fields.md) — series metadata, observation table, graph and download details.
- [../../sites/fred/references/data-model.md](../../sites/fred/references/data-model.md) — FRED entity model and freshness rules.
- [../../sites/fred/references/site-map.md](../../sites/fred/references/site-map.md) — confirmed routes and coverage gaps.
- [../../sites/fred/references/first-party-guidance.md](../../sites/fred/references/first-party-guidance.md) — FRED Help, API docs and provenance.
