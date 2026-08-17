---
name: tdx-api-discovery
description: Discover and verify TDX transport data services, API documentation, data standards, supply-status tables, public statistics, and data-mart offerings through the Codex in-app browser. Use when the user asks which TDX service or domain to use, how to find current transport data, how to inspect the Swagger/OAS guide, or how to validate availability and freshness without using raw HTTP or undocumented APIs.
---

# TDX API Discovery

## Purpose and entry points

Use this skill for public and currently visible TDX discovery work. Start from the existing in-app browser tab when possible and confirm the current page before navigating. The primary routes are:

- `/data-service/basic`, `/data-service/advanced`, `/data-service/premium`, `/data-service/ticket`, `/data-service/historical`, `/data-service/gtfs`, and `/layoutMap-service/layoutMap` — service catalog families.
- `/api-service/swagger` — interactive API/OAS guide.
- `/data-provide` — first-party data supply-status matrix.
- `/data-standard/description` — transport data standards, validators, examples, and search tools.
- `/statistics` — public API call/download statistics.
- `/data-mart/about` and `/data-mart/list` — private-sector data-market background and offerings.
- `/sitemap` — first-party HTML route inventory.

Load [api-routing.md](references/api-routing.md) when choosing among page types or interpreting TDX terminology.

## Procedure

1. Confirm the visible domain, route, session state, and page heading. Use only the Codex in-app browser and the current user tab for site exploration.
2. Route by intent: service family for catalog discovery, Swagger for an API contract, `/data-provide` for source availability, `/data-standard/description` for schema/validation guidance, `/statistics` for platform-level usage, and data-mart pages for private offerings.
3. After navigation, visually verify the same tab and then read the visible heading, controls, result state, and any first-party explanation. A navigation call alone is not evidence that a route loaded.
4. Re-fetch dynamic service cards, supplier status, statistics, pricing, and product descriptions at task time. Do not copy current counts, rankings, dates, prices, or result rows into durable instructions.
5. Report the exact route, selected category/domain, and verification evidence. If the UI is blank, stale, or contradictory, retry the same route once and record the mismatch instead of guessing.

## Core workflows

### Find a suitable service

1. Open the relevant service family and inspect its `資料主題`, `領域類型`, and `資料類型` controls plus service cards.
2. Record the service title, version, whether it is batch or real-time where shown, the current access policy, the `計次`/`計量` pricing labels, and the service explanation.
3. Use the first-party `資料使用授權規範` link when access or billing semantics are unclear. Treat the service page as a live catalog, not a static inventory.
4. For historical data, distinguish browsing the description from downloading: the page states that non-members can browse descriptions but members must apply for files or use the API.

### Inspect an API contract

1. Open `/api-service/swagger` and verify `API使用指引`.
2. Use the `服務類別` selector first, then the `領域分類` selector. Confirm the selected values and resulting OAS/endpoint content; do not infer a service from an option label alone.
3. The guide exposes OAS 3.0 documentation, server URLs, `Authorize`, endpoint groups, and a `Schemas` control. Use the linked OAS text or sample-code link when the user needs a machine-readable contract.
4. The guide explains that unauthenticated visitor mode is limited to browser access, basic services, and a daily IP limit; complete member mode requires a TDX API key. Never enter or expose Client Id/Client Secret values in notes or responses.
5. If a category change updates the option list but the server or endpoint panel remains on an earlier selection, treat that as a UI mismatch and re-check the visible state before reporting success.

### Check supply status or standards

- On `/data-provide`, choose the visible category and read the matrix legend before interpreting cells: `－` means no such data, `○` means not yet provided, `●` means published via automated integration, `◆` means published via non-automated supply, and red marks current-year additions. Treat the table as dynamic.
- On `/data-standard/description`, use the standards table to reach the relevant specification, online XML Schema validator, sample code, route/stop query, or quality-checking guide. Keep standards documentation separate from current data values.

### Read public statistics

1. Open `/statistics` and verify the chart plus `API服務用量` filters.
2. Select `服務類別`, then inspect the populated `領域分類`; choose the month only when the user specifies a period.
3. Verify the filtered chart/list and use the page's `Download SVG`, `Download PNG`, or `Download CSV` controls only when the user asks for an export. Never treat a chart label or current total as stable knowledge.

## Safety, authentication, and limits

- Default to read-only actions. Do not authorize Swagger, submit applications, purchase data, change subscriptions, or send forms as part of discovery.
- A visible `會員中心`/`登出` state means the site is authenticated; the authenticated site variant can expose different catalog and permission states. Preserve the session and do not sign out.
- If authentication is not visible, complete public discovery first. Ask the user to sign in manually in the same in-app browser tab before exploring protected branches; never type passwords or inspect cookies, storage, or session files.
- Treat linked GitHub, GitBook, Google Drive, vendor, and management-backend pages as separate linked resources. Follow them only when needed and keep their access/ownership distinct from TDX UI evidence.
- Do not treat HTML shown at `/robots.txt` as a parsed robots file. In the current exploration it rendered the site shell; the first-party HTML `/sitemap` was the reliable inventory.

## Drift maintenance

Before acting, compare the current visible route, labels, controls, permissions, and first-party definitions with this procedure. If a stable route or workflow changes, use the current UI safely, record the exact old/new behavior, page variant, route, verification evidence, and date, then update this skill or its reference. Do not write dynamic counts, rankings, prices, availability, or user-specific values. Re-run the affected read-only workflow and `quick_validate.py`; report broad or ambiguous changes instead of speculating.

## References

- [api-routing.md](references/api-routing.md) — verified route families, page taxonomy, first-party definitions, and navigation decisions.
