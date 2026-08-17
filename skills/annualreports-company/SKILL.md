---
name: annualreports-company
description: Inspect public AnnualReports.com company profiles and retrieve or verify current and archived annual report links through the Codex in-app browser. Use when the user names a company, ticker, company profile, annual report year, PDF/HTML/Form 10-K format, archive, report download, or sustainability-report link.
---

# AnnualReports Company Reports

Use this skill after a company is known, or hand off discovery to `$annualreports-search`. Work in the Codex in-app browser on the same tab/session, and read [data-model.md](../../sites/annualreports/references/data-model.md) when the entity relationship or report format is unclear.

## Open and verify the profile

1. Search for the exact company through `$annualreports-search` when no profile URL is supplied. Prefer an exact visible company link over a guessed slug.
2. Open `/Company/<slug>` in the current in-app tab and verify at least two identity signals: profile heading, ticker, exchange, industry, sector, or company description.
3. Capture the current profile fields needed for the task: identity, taxonomy, description, official website link, and report sections. Treat ratings, review counts, employee labels, location, and report availability as live values.
4. Keep official-company and partner-site links separate from AnnualReports.com evidence. Do not follow them unless the user asks to expand scope.

## Current report workflow

In `Most Recent Annual Report`, inspect the visible report title and the available controls:

- `View PDF`
- `View HTML`
- `View Form 10K (HTML)`

Verify the title, action label, current URL, and whether a new target page/tab actually appears. On the observed profile these buttons used `/Click/<id>` tracking targets with `window.open(..., '_blank')` and opened a report-rating modal in the current page. A rating modal is not the report. Do not select stars or press `Submit` to continue. If the report target does not appear, report that it was not visually opened and use a visible archive link when appropriate.

## Archived reports

1. Locate `Older/Archived Annual Reports`.
2. If the requested year is not visible, use the exact visible `Show <n> older reports` control and re-read the page.
3. For the requested year, verify the year label and format. Use the visible `View Annual Report` action for browser viewing or `Download` for an inbound local artifact.
4. Treat the path under `/HostedData/AnnualReportArchive/...` as a page-provided link, not a template to guess. Extensions can vary (observed PDF, DOCX, and legacy HTML).
5. After opening or downloading, verify the new tab/page or download completion. A link's presence alone is not proof of a successful report retrieval.

## Other profile branches

- `Request Information` and hardcopy text indicate a request branch; stop before sending or submitting.
- Sustainability reports link to ResponsibilityReports.com, an external partner. Follow only when the user explicitly requests that external source.
- `Visit website` is the company's external site, not an AnnualReports.com report source.
- Report rating controls are representational; do not interact with them during read-only research.

## Output

Return: company identity and taxonomy, profile fields requested, current report title and verified formats, archive year/format/link status, external links kept out of scope, and any blocked or unverified target. Keep current values tied to the observation date and do not hard-code them in this skill.

## Safety and evidence

Use only the Codex in-app browser. Do not enter passwords, contact information, ratings, or upload files. Stop at CAPTCHA, login, security interstitial, ambiguous external authentication, or any form submission. When a report-open attempt times out or a new tab does not appear, record the control error separately from the report's content.

## Drift maintenance

Before acting, compare the current profile sections, labels, report controls, targets, and permissions with this procedure. If they differ, adapt only when the new behavior is clearly visible and safe, record the public/authenticated variant, route, old behavior, current behavior, evidence source, and date, then patch this skill or the site reference. Re-run the affected safe workflow and `quick_validate.py`. Never store live report years, ratings, counts, URLs with one-off IDs, or private data as stable instructions.

## References

- [site-map.md](../../sites/annualreports/references/site-map.md) — public routes and coverage status.
- [data-model.md](../../sites/annualreports/references/data-model.md) — company and report entities.
- [first-party-guidance.md](../../sites/annualreports/references/first-party-guidance.md) — report-link behavior and confirmation boundaries.
