# AnnualReports.com

## Site identity and operating boundary

AnnualReports.com is a public directory for company profiles and annual reports. Use the Codex in-app browser only, starting from the user's existing AnnualReports tab when available. Treat the visible UI as the source of truth; do not substitute an API, CLI, web search, external browser, or stored session data.

Keep exploration and retrieval read-only. Do not submit ratings, request hardcopies, add a company, send shipment details, contact the provider, upload files, or follow external partner links unless the user explicitly asks and any required confirmation is obtained.

## Routing

- Use `$annualreports-search` for keyword/ticker lookup, exchange lists, sector/industry lists, alphabetical browsing, and Featured Reports.
- Use `$annualreports-company` after a company has been identified; it covers the company profile, current report links, archived reports, and report-link verification.
- Read [site-map.md](references/site-map.md) when the entry point or route parameter is unclear.
- Read [data-model.md](references/data-model.md) when mapping a company to taxonomy or report entities.
- Read [first-party-guidance.md](references/first-party-guidance.md) before interpreting report ratings, provider claims, legal limitations, or outbound forms.

## Stable route map

- Home: `/`
- Main menu `BROWSE BY`: `Exchanges` → `/Browse/Exchange`, `Industry` → `/Browse/Industry`, `Other Filters` → `/Search`
- Keyword result: `/Companies?search=<query>`; the home/header search form is the reliable keyword entry point.
- Exchange result: `/Companies?exch=<id>`
- Industry result: `/Companies?ind=<id>`
- Sector result: `/Companies?sect=<id>`
- Alphabetical result: `/Companies?a=<letter>`
- Company profile: `/Company/<slug>`
- Featured reports: `/Featured/Reports`

Do not infer numeric taxonomy IDs or company slugs. Obtain them from visible first-party links or the current page.

## Session, freshness, and validation

1. Inspect the current tab before navigating and preserve the same tab and session.
2. After navigation or a meaningful interaction, verify at least two signals: current URL, heading, selected control/value, result row, report title, or explicit empty state.
3. Re-fetch live results, report years, ratings, counts, statuses, and availability during each task. Never copy those dynamic values into reusable instructions.
4. Treat `View PDF`, `View HTML`, and archive `View Annual Report` as report-opening actions. Verify whether a new tab or target page actually appears; a successful click or tracking URL alone is not proof that the report opened.
5. Do not select report stars or press `Submit`; rating is a representational action.

## Known exploration limits

On 2026-08-17, same-origin `/robots.txt` and `/sitemap.xml` navigation was attempted in the user's in-app tab. The browser reported `ERR_BLOCKED_BY_CLIENT`, and visual retry left the prior page visible; record these as `client-blocked`, not as evidence that the site has no sitemap. Several list/static routes also returned a screenshot timeout while their DOM loaded; keep visual and DOM evidence separate.

## Drift maintenance

Before acting, compare current labels, routes, controls, permissions, and first-party explanations with this file and the owning skill. If they differ, complete only a safe, clearly verifiable adaptation, record the public/authenticated variant, route, old behavior, observed behavior, evidence source, and date, then patch the owning artifact and re-run its validator. Do not record passwords, cookies, tokens, private data, live result values, or one-off counts.
