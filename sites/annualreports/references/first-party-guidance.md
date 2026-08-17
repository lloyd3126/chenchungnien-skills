# First-party guidance and constraints

## Provider definitions

The FAQ describes AnnualReports.com as a free directory intended to let users review annual reports in their actual format. It says report information is provided directly by participating companies and that reports may be viewed in HTML or PDF. The About page also describes search by company name/ticker, sector, industry, exchange, alphabet, and index, but the currently observed UI is the authoritative routing source when those descriptions differ.

Do not treat the directory, its ratings, or report contents as investment advice. The Legal page says the service does not guarantee accuracy, completeness, or timeliness and does not endorse investment decisions or trading strategies.

## Safe read-only behavior

- Search, browse, open profiles, expand older reports, and inspect report links are read-only navigation.
- Re-fetch current report years, ratings, counts, company status, and availability on every task.
- Preserve empty states and errors; do not silently broaden a search.
- Verify a navigation target in the same in-app browser. A URL returned by a click handler, tracking route, or `window.open` call is not itself proof of a loaded report.

## Confirmation boundaries

Stop before any of the following unless the user explicitly requests it and action-time confirmation is satisfied:

- selecting a star and pressing `Submit` in the report rating modal;
- clicking a hardcopy/request control when it starts a request flow;
- submitting `AddCompany`;
- submitting `SUBMIT SHIPMENT DETAILS` on `/sendreportsform`;
- sending email or calling provider contact links;
- uploading, transmitting, or entering contact information into a form;
- following an external partner or legacy company URL when doing so expands the requested scope.

Inbound report downloads are allowed by the browser policy, but future agents should download only when the user asks for a local file or when the workflow explicitly requires an artifact. Prefer the visible `Download` link over guessing a file URL.

## Report-link behavior observed

The current profile exposes `View PDF`, `View HTML`, and `View Form 10K (HTML)` links. Their click handlers open a `/Click/<id>` target in a new window and open a rating prompt in the current page. If the report window does not appear, record the target as attempted and use a visible archive `View Annual Report` or `Download` link instead; do not rate the report to unlock it.

Archived report cards expose a direct file link. `View Annual Report` targets a new tab; `Download` carries a download attribute. File extensions and available years vary by company.

## Inventory evidence

The in-app browser attempted `/robots.txt` and `/sitemap.xml` in the existing AnnualReports tab. Both attempts reported `ERR_BLOCKED_BY_CLIENT`, and visual retry left the previous page visible. Keep these as browser-control limitations (`client-blocked`), not as evidence that no inventory exists. Do not switch to curl, an API, web search, or another browser to work around the boundary.

## Drift maintenance

If a label, control, route, form field, report format, or permission changes, record the public/authenticated variant, page type, route, old behavior, current behavior, evidence source, and date. Patch the owning skill or reference only when the difference is clear and stable, then repeat the affected safe workflow and validator. Never store passwords, cookies, tokens, private records, or live result values.
