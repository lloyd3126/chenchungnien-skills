---
name: sec-filings-research
description: Search, inspect, and verify SEC.gov and EDGAR company records, CIKs, filing histories, full-text filings, filing detail pages, and SEC data/API documentation through the Codex in-app browser. Use for requests about 10-K, 10-Q, 8-K, forms, accession numbers, company filings, latest filings, XBRL, or EDGAR search.
---

# SEC Filing Research

## Purpose and entry points

Use only the Codex in-app browser and the already-visible active SEC tab. Read [sites/sec/AGENTS.md](../../sites/sec/AGENTS.md), [data-model.md](../../sites/sec/references/data-model.md), and [first-party-guidance.md](../../sites/sec/references/first-party-guidance.md) when the task needs field semantics or API limits.

Choose the smallest matching entry point:

- Company or person → `https://www.sec.gov/search-filings`
- CIK only → `https://www.sec.gov/search-filings/cik-lookup`
- Filing text or phrase → `https://www.sec.gov/edgar/search/`
- Current submissions → `https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent`
- A known filing document → its visible HTML/text link, then its `Filing Detail` index
- API or XBRL explanation → `https://www.sec.gov/search-filings/edgar-application-programming-interfaces`

## Procedure

1. Inspect the current tab URL, title, heading, authentication state, and visible controls before navigating. Follow the browser skill's open-then-screenshot protocol; a `goto` success is not proof that the page visibly loaded.
2. For a company search, open `Search Filings`, use `Company and Person Lookup` with a name, ticker, or CIK, and verify the resulting entity identity before selecting a filing. If the name is ambiguous, use `CIK Lookup` and narrow the name because the site can return at most 100 matches.
3. For full-text search, open `Full Text Search`, enter the requested keyword or phrase, expand `+ more search options` when needed, and set only the requested date, filing category, company/person, CIK, or location controls. Use `SEARCH`, then verify query state and result table. `Clear all` is a safe reset.
4. For latest filings, open `Latest Filings Search`, set Company, CIK, Form Type, and ownership (`Include`, `Exclude`, or `Only`) as requested, choose the entries count, and use `Retrieve Filings`. Verify the table header, accepted time, filing date, form, entity role, and HTML/text links. The RSS link is a read-only alternative; do not subscribe.
5. For a specific filing, follow a visible result link rather than guessing an accession URL. On `Filing Detail`, read Form, SEC Accession No., Filing Date, Accepted, Documents, and the `Document Format Files` table. Distinguish primary HTML/XML from the complete submission text file, and distinguish Filer, Subject, Filed by, and Reporting roles.
6. For SEC API or XBRL questions, read the first-party guidance before acting. Treat submissions, companyconcept, companyfacts, frames, bulk ZIPs, CORS, update cadence, user-agent, and fair-access limits as current documentation that must be rechecked when the task is live or programmatic.
7. Report current filing values with the query, filters, page, source URL, and retrieval time. Never promote a live row, result count, ticker association, or API value into reusable skill text.

## Page and field semantics

- CIK is the stable SEC entity identifier and is ten digits with leading zeros in the API form.
- Filing Date and Accepted are separate fields; preserve both when they are relevant.
- Accession number identifies a submission; a document URL can be only one component of that submission. Prefer the visible Filing Detail index for the full document set.
- Full-text result columns may include Form & File, Filed, Reporting for, Filing entity/person, CIK, location, incorporation, file number, or film number. Check Show Columns state before interpreting a table.
- Latest Filings Key to Descriptions defines Filer, Subject, Filed by, Reporting, Paper, and Cover; read it when a row contains a role label.

## Safety and limits

- Default to read-only public research. Do not sign into or use EDGAR Filer Management, EDGAR Filing Portal, Online Forms Management, or EDGAR Next during research.
- Do not submit a filing, upload a document, create an API token, subscribe to RSS/email, or alter a filer/account setting. Stop before any external side effect and request action-time confirmation if the user explicitly wants it.
- Do not use external browsers, web search, CLI, cookies, local storage, or direct API requests to replace the in-app browser workflow unless the user explicitly changes the operating boundary.
- Follow SEC fair-access guidance. Request only what is needed, avoid high-frequency or unclassified automation, and re-read Developer Resources before any programmatic alternative.
- If a route is blocked, requires login, shows a CAPTCHA/security interstitial, or the current tab is unavailable, record the evidence and stop that branch; do not infer data from a navigation error.

## Drift maintenance

Compare the current visible UI, route, labels, controls, permissions, and SEC first-party definitions with this procedure before acting. If a stable route, field, control, or workflow changes, adapt only the safe minimum, record old/new behavior and date, update [sites/sec/AGENTS.md](../../sites/sec/AGENTS.md) or the owning reference when directly verified, and rerun the affected workflow plus `quick_validate.py`. Keep public and authenticated variants separate; never write passwords, cookies, tokens, private data, dynamic results, or speculative behavior.

## References

- [site-map.md](../../sites/sec/references/site-map.md) — route coverage and evidence status.
- [data-model.md](../../sites/sec/references/data-model.md) — filing, document, filer, search, and API entities.
- [first-party-guidance.md](../../sites/sec/references/first-party-guidance.md) — SEC definitions, API endpoints, update rules, and fair-access constraints.
- [agent-usability.md](../../sites/sec/references/agent-usability.md) — request-shape routing and verification scenarios.
