---
name: annualreports-search
description: Search and filter public AnnualReports.com company listings through the Codex in-app browser. Use when the user wants to find a company by name or ticker, browse by exchange, sector, industry, alphabet, or Featured Reports, or verify a read-only search result.
---

# AnnualReports Search

Use this skill for public discovery only. Keep the current in-app browser tab and session, read [the site map](../../sites/annualreports/references/site-map.md) when routing is unclear, and never replace the browser with an API, CLI, web search, external browser, or stored session data.

## Choose the route

- **Named company or ticker:** start at `/` and use the visible home search field `Company Name or Ticker Symbol`; submit the safe read-only search.
- **Exchange:** use `BROWSE BY` → `Exchanges`, then select a visible exchange; the result route is `/Companies?exch=<id>`.
- **Industry:** use `BROWSE BY` → `Industry`, then select the visible industry; the result route is `/Companies?ind=<id>`.
- **Sector:** use the visible sector link or `/Search` selector; the result route is `/Companies?sect=<id>`.
- **Alphabetical:** use the visible alphabet link; the result route is `/Companies?a=<letter>`.
- **Featured Reports:** use `/Featured/Reports`; it routes to company profiles rather than report files.
- **Other Filters:** `/Search` exposes a company search, industry/sector comboboxes, exchange links, featured programs, and alphabet links. Its visible `Search by Company Name or Ticker` input was observed with an empty HTML `name`, so prefer the home/header search form for keyword lookup and do not assume this form preserves a query until verified.

## Keyword search workflow

1. Inspect the current tab and visible page. If needed, return to the same site's home through the visible logo.
2. Locate the visible home field `Company Name or Ticker Symbol` or the same field in the header menu. Do not use a hidden or duplicate field when a visible field is available.
3. Fill the user's exact company name or ticker and click the associated `Search` control.
4. Verify at least two signals: URL contains `Companies?search=...`, heading says `Companies matching "<query>"`, and the result row shows the intended company plus its industry and sector.
5. Open the exact company link only when the user wants profile/report details; otherwise report the verified list result.
6. Preserve explicit empty/error results. Do not silently broaden, autocorrect, or replace the query.

## Taxonomy and Featured workflows

For exchange, industry, sector, and alphabet routes:

1. Enter through the visible menu, homepage link, or a visible profile `More` link.
2. Select a label that is actually visible; do not guess opaque numeric IDs.
3. Verify the result heading (`All NASDAQ Companies`, `All <industry> Companies`, or the current equivalent), current URL, and at least one row's company/industry/sector columns.
4. Treat current row order, membership, company status, and any counts as live data.

For `/Featured/Reports`, verify the heading `All Featured Annual Reports` and a visible company link. Follow the company link only when profile inspection is requested.

## Safety and evidence

- Use the Codex in-app browser only and preserve the current tab/session.
- After every navigation or meaningful control interaction, verify the current URL plus one page/result signal.
- Do not submit ratings, request hardcopies, add a company, send shipment details, or enter personal/contact data.
- If a CAPTCHA, login wall, security interstitial, or ambiguous external authentication appears, stop that branch and report it.
- Do not treat `/robots.txt` or `/sitemap.xml` as empty when the in-app browser reports `ERR_BLOCKED_BY_CLIENT`; see [first-party-guidance.md](../../sites/annualreports/references/first-party-guidance.md).

## Output

Report the query/route, observed heading, verification signals, and the exact company links or taxonomy labels found. Separate live results from stable route knowledge. Use `$annualreports-company` for profile and report retrieval.

## Drift maintenance

Before acting, compare the current labels, route, field semantics, and result verification with this procedure. If the UI differs, use the current visible UI for a safe task, record the public/authenticated variant, route, old behavior, observed behavior, evidence source, and date, then patch this skill or the site reference only when the change is clear and stable. Re-run the relevant search and `quick_validate.py`; do not record dynamic counts or result values.

## References

- [site-map.md](../../sites/annualreports/references/site-map.md) — routes, page types, and evidence status.
- [data-model.md](../../sites/annualreports/references/data-model.md) — company/list/taxonomy relationships.
- [first-party-guidance.md](../../sites/annualreports/references/first-party-guidance.md) — provider definitions and safety boundaries.
