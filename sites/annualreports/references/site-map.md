# AnnualReports.com site map

This is a route and coverage map, not a copy of the live directory. Route labels and query parameters were observed through the Codex in-app browser on 2026-08-17. Dynamic counts, rankings, current report years, and ratings are intentionally omitted.

## Coverage

| Area | Route or entry | What it exposes | Status | Evidence |
|---|---|---|---|---|
| Home | `/` | Global search, Featured Reports, Featured Companies, exchange links, alphabet links, footer | UI-verified | current-tab visual + DOM/interaction |
| Main menu | header `Menu` → `BROWSE BY` | Exchanges, Industry, Other Filters, header search | UI-verified | current-tab visual + DOM/interaction |
| Exchanges | `/Browse/Exchange` | AIM, AMEX, ASX, LSE, NASDAQ, NYSE, OTC, TSX, TSX-V | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| Exchange list | `/Companies?exch=<id>` | Company rows with company, industry, sector | UI-verified for NASDAQ | current-tab visual + DOM/interaction |
| Industry | `/Browse/Industry` | Sector groups and industry links | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| Industry list | `/Companies?ind=<id>` | Company rows for an industry | UI-verified for Application Software | current-tab visual + DOM/interaction |
| Sector list | `/Companies?sect=<id>` | Company rows for a sector | route observed from visible links; representative page not separately opened | current-tab DOM link evidence |
| Alphabetical list | `/Companies?a=<letter>` | Company rows by first letter | route observed from visible links; representative page not separately opened | current-tab DOM link evidence |
| Other Filters | `/Search` | Company search, industry/sector comboboxes, exchange links, featured programs, alphabet links | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| Keyword results | `/Companies?search=<query>` | Matching companies and company/industry/sector columns | UI-verified for a representative keyword | current-tab visual + DOM/interaction |
| Company profile | `/Company/<slug>` | Identity, taxonomy, description, official site, ratings, current and archived reports | UI-verified for a representative company | current-tab visual + DOM/interaction |
| Featured Reports | `/Featured/Reports` | Links to featured company profiles | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| Empty cart | `/Cart` | Empty-cart state and return-to-home link | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| About | `/About` | Provider description and stated search/report capabilities | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| FAQ | `/FAQ` | Provider definitions and report-source/use explanations | DOM-verified; screenshot automation error | current-tab DOM/interaction; automation/control error |
| Contact | `/Contact` | Provider contact details and Send Reports entry | DOM-verified | current-tab DOM/interaction |
| Send Reports | `/sendreports` | Printed-report fulfillment explanation and shipment-form link | DOM-verified | current-tab DOM/interaction |
| Shipment form | `/sendreportsform` | Company/contact/shipment fields and `SUBMIT SHIPMENT DETAILS` | DOM-verified; not submitted | current-tab DOM/interaction |
| Legal | `/Disclaimer` | Investment-information disclaimer and third-party-site limitations | DOM-verified | current-tab DOM/interaction |
| Add Company | `/AddCompany` | Company/contact form and `Add Company` button | DOM-verified; not submitted | current-tab DOM/interaction |
| robots | `/robots.txt` | Candidate crawler inventory | client-blocked | current-tab visual retry + automation/control error |
| sitemap | `/sitemap.xml` | Candidate URL inventory | client-blocked | current-tab visual retry + automation/control error |

## Route patterns

Use visible links to obtain IDs and slugs. The observed families are:

- `/Companies?search=...`
- `/Companies?exch=...`
- `/Companies?ind=...`
- `/Companies?sect=...`
- `/Companies?a=...`
- `/Company/...`
- `/HostedData/AnnualReportArchive/...`
- `/Click/<report-id>` as a tracking/open target behind current-report buttons

The route family is stable enough for routing, but query values, company slugs, report IDs, and available years must be re-read from the current page.

## Coverage gaps

The authenticated variant was not applicable: no login/account state was visible during the public pass. External partner destinations such as ResponsibilityReports.com, company websites, and legacy third-party report URLs were not explored because they are outside the current site's public route map. Pagination, sorting, and hardcopy/request workflows were not submitted or confirmed beyond their visible controls.
