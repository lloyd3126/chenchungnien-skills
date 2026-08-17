# GlobeNewswire site map and exploration evidence

## Verified public routes

| Page type | Stable entry / pattern | Confirmed purpose | Status | Evidence |
| --- | --- | --- | --- | --- |
| Home | `/` | Marketing landing page, global navigation, public newsroom entry | explored | current-tab DOM/interaction |
| Newsroom | `/newsroom` | Latest public news entry, category navigation, search form | explored | current-tab DOM/interaction |
| Search results | `/en/search/keyword/<encoded-keyword>?pageSize=10` | Keyword results with filter chips, result rows, and Next Page | explored | current-tab DOM/interaction |
| Organization results | `/en/search/organization/<visible-encoded-name>?page=1` | Releases attributed to one visible source organization | explored | current-tab DOM/interaction |
| Tag results | `/en/search/tag/<visible-encoded-tag>` | Candidate route observed from a release tag; not opened in this pass | partial | current-tab DOM/interaction |
| Category list | `/news/<category>` | Topic/industry release list with subcategory tiles and pagination | explored (`energy`) | current-tab DOM/interaction |
| Subcategory list | `/news/<category>/<subcategory>` | Narrower topic/industry list; visible in navigation | partial | current-tab DOM/interaction |
| Release detail | `/news-release/<date>/<release-id>/<version>/<language>/<slug>.html` | Title, publication time, source, body, tags, industry, public actions, related releases | explored | current-tab DOM/interaction |
| RSS directory | `/rss/list` | RSS/ATOM/JavaScript feeds grouped by subject, industry, and location | partial; Subject panel opened | current-tab DOM/interaction |
| About | `/about` | First-party company, distribution, trust, FAQ, PR/IR explanations | explored | current-tab DOM/interaction |
| Services | `/services` | First-party PR/IR service catalogue and links | explored | current-tab DOM/interaction |
| Customer login | `/home/signin` → Notified login | Username step, reCAPTCHA, registration and legal links | protected boundary | current-tab DOM/interaction |

## Main navigation and taxonomy

The public navigation labels observed in Newsroom were:

- `Consumer Products and Services News`: Automobiles and Parts, Food & Beverage, Home Goods & Construction, Leisure Goods, Media & Entertainment, Personal Care, Retail, Travel and Leisure.
- `Energy News`: Alternative Energy, Oil Gas and Coal, Chemicals.
- `Banks & Financial Services News`: Banking, Closed-End Investments, Finance and Credit Services, Investment Banking and Brokerage Services, Insurance, Real Estate & REITs.
- `Healthcare News`: Healthcare Providers, Medical Equipment, Medical Supplies and Services, Biotechnology, Pharmaceuticals, Cannabis Producers.
- `Industrials and Utilities News`: Aerospace and Defense, Construction and Materials, Utilities, Industrials, Metals & Mining.
- `Technology and Telecom News`: Software, IT Services, Semiconductors, Electronic Components & Equipment, Computer Hardware, Telecom Equipment, Telecom Services.

Use the exact visible href for subcategory navigation. The navigation also exposes `Newsroom`, `Services`, `Contact Us`, `About Us`, `English`, `Sign In`, and `Register`.

## Search and pagination evidence

On `/newsroom`, the public search area showed a scope control labeled `Everything`, a keyword textbox, `SEARCH`, and buttons `Industry`, `Subject`, `Tag`, `Language`, and `More Filters`. Filling the visible `SEARCH` textbox with a safe representative word and pressing Enter produced the keyword route above, a `Search Results` heading, a `Keyword` filter chip, release rows, and a visible `Next Page` link.

Category pages reuse a keyword search control and show release rows followed by topic tiles and `View All`. Search and category results are live; titles, dates, counts, ordering, and availability must be fetched per task.

## RSS directory evidence

`/rss/list` showed `RSS by Subject` as the selected panel, with `Speciality Business News` expanded and visible feed links for `Public Companies`, `Dividend Reports and Estimates`, `Earnings Releases and Operating Results`, and `Mergers and Acquisitions`. Each visible feed offered `ATOM`, `Java Script`, and `RSS` links. `RSS by Industry` and `RSS by Location` were visible tabs but their content was not confirmed after click in this pass.

## Sitemap and robots status

| Candidate | Result | Retrieval status | Evidence |
| --- | --- | --- | --- |
| `/robots.txt` | Browser reported `ERR_BLOCKED_BY_CLIENT`; same-tab retries left the visible DOM on Home | `client-blocked` | automation/control error plus current-tab DOM |
| `/sitemap.xml` | Site 404 page: “The page you were looking for is no longer here” | `invalid/unavailable` | current-tab DOM after open and same-tab retry |
| `/sitemap_index.xml` | Same site 404 page | `invalid/unavailable` | current-tab DOM after open and same-tab retry |
| `/sitemap.xml.gz` | Initial automation body was empty/document-like; same-tab retry showed the same site 404 page | `invalid/unavailable` | current-tab DOM after retry; no download artifact |

No Sitemap XML was visually or locally parsed in this pass. Screenshot capture attempts consistently failed or timed out in the browser-control path; those errors are not treated as evidence that a route was empty. Route claims above rely on current-tab DOM/interaction plus URL and heading/state verification.

## Coverage and second pass

| Area | Status | Notes |
| --- | --- | --- |
| Home, navbar, footer, languages | explored | Revisited after candidate sitemap checks; footer includes RSS, About, Contact, Notified, Legal, Resources |
| Newsroom and category navigation | explored | Newsroom, Energy category, visible six-category taxonomy |
| Keyword search | explored | Safe keyword input verified URL, heading, filter chip, result rows, and Next Page |
| Organization results | explored | Entered through a visible source link and verified Organization filter chip and historical release list |
| Release detail | explored | Verified metadata, body, tags, industry, website, Print/PDF/RSS/ATOM and related-release surfaces |
| RSS directory | partial | Subject panel and formats observed; Industry/Location tab content not confirmed after click |
| About and Services | explored | First-party explanations and FAQ content read |
| Customer/Reader account | protected—awaiting user choice | Login boundary observed; no credentials or CAPTCHA action |
| Major search filter buttons | partial | Labels observed; click control path timed out, so option lists/results are unconfirmed |
