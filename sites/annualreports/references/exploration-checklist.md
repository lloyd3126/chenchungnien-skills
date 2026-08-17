# AnnualReports.com exploration checklist

Use this checklist for future drift audits. `UI-verified` requires the current tab to have been visually inspected; DOM-only findings and automation errors must stay distinct.

## Public pass

- [x] Home and header search — `UI-verified`; current-tab visual + DOM/interaction.
- [x] Main menu and `BROWSE BY` — `UI-verified`; current-tab visual + DOM/interaction.
- [x] Exchange index — DOM verified; screenshot automation error.
- [x] Representative exchange list — `UI-verified` for NASDAQ.
- [x] Industry index — DOM verified; screenshot automation error.
- [x] Representative industry list — `UI-verified` for Application Software.
- [x] Sector and alphabetical route families — visible links verified; representative page not separately opened.
- [x] Other Filters page — DOM verified; screenshot automation error.
- [x] Keyword search results — `UI-verified` for a representative company query.
- [x] Company profile — `UI-verified` for a representative company.
- [x] Older-report expansion — `UI-verified`; archive list and formats observed.
- [x] Current-report controls — `UI-verified`; rating modal behavior observed; report target itself not verified in a new tab.
- [x] Featured Reports — DOM verified; screenshot automation error.
- [x] Empty Cart — DOM verified; screenshot automation error.
- [x] About and FAQ — DOM verified; screenshot automation error.
- [x] Contact, Send Reports, shipment form, Legal, Add Company — DOM verified; forms not submitted.
- [x] `/robots.txt` and `/sitemap.xml` — `client-blocked`; visual retry showed the prior page.

## Not explored or intentionally stopped

- [ ] Authenticated variant — no login/account state was visible.
- [ ] External partner and company websites — out of scope for this site pass.
- [ ] Report rating submission — representational action, not tested.
- [ ] Hardcopy/request, Add Company, and shipment submission — outbound actions, not tested.
- [ ] Pagination/sorting — not exposed in the representative DOM; do not assume absent without rechecking.

## Evidence vocabulary

- `current-tab visual`: screenshot of the user's existing in-app tab was captured and inspected.
- `current-tab DOM/interaction`: current tab route and visible DOM/control behavior were read.
- `automation/control error`: a browser-control attempt failed or timed out; it is not evidence about page content.
- `client-blocked`: navigation and visual retry did not expose the requested inventory resource in the in-app browser.
