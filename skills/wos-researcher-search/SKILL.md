---
name: wos-researcher-search
description: "Use the Codex in-app browser to search Web of Science researchers/authors by name, Web of Science ResearcherID or ORCID, or organization, then verify an Author Profile, inspect its publication list, or open a same-site Core Collection Full Record. Trigger whenever the user asks to find an author, researcher profile, DOI, WOS accession, indexed publication, or citation metadata in Web of Science."
---

# Web of Science Researcher Search

## Purpose and entry point

Use this skill for read-only author and publication lookup in the Codex in-app browser. Start from the user's already-open Web of Science tab, preferably `/wos/author/author-search`; do not create a temporary tab, switch browsers, use an API/CLI, or bypass authentication. Read [the site map](../../sites/webofscience/references/site-map.md), [the data model](../../sites/webofscience/references/data-model.md), and [the interaction rules](../../sites/webofscience/references/interaction-rules.md) when the route or field meaning is unclear.

## Procedure

1. Inspect the current tab visually and through the DOM. Confirm the Web of Science header, current route, search tab, and whether an account/profile variant is visible.
2. If the current tab is elsewhere in Web of Science, use a visible first-party `Researcher Search` or `Web of Science` link in that same tab. If the tab is not Web of Science, stop and report that the required current tab is unavailable; do not open another browser.
3. In the `RESEARCHERS` search surface, open `Filter by` and choose exactly one visible mode:
   - `Name Search`: fill `Last Name` and `First Name`.
   - `Author Identifiers`: fill the visible `Web of Science ResearcherID or ORCID` field with a user-provided identifier.
   - `Organization`: fill the visible organization field and choose `Most recent publications`, `Publications within 5 years`, or `All publications`.
4. For name and organization inputs, wait for autocomplete/listbox suggestions and select the intended exact option. Do not treat typed text alone as a resolved entity. If a suggestion list is still open, the first `Search` click may select a suggestion; confirm the list is closed and click the exact `Search` button again.
5. After search, wait for loading to finish. Verify the Author Profile heading, breadcrumb, identifier/name/organization sections as needed, result tab, result count/state, and any visible warning such as Free View or premium limitations. Re-fetch dynamic values rather than copying exploratory values.
6. To inspect a publication, choose one visible same-site publication title from the verified Author Profile. Do not follow a publisher/full-text link unless the user explicitly requests external reading.
7. On the Full Record, verify the current URL, title, author line, source, volume/issue/pages where present, DOI or WOS accession, publication/indexed dates, document type, address, categories, and the Citation Network/Core Collection section. Use `See more data fields` only when extra metadata is needed, then verify the newly visible field labels.
8. Report the query, selected mode/options, page/record verification signals, and freshness. Do not report a dynamic result as a durable site rule.

## Page and field semantics

- Name Search is explicitly described by the UI as finding an author record from first and last names.
- Author Identifiers accepts Web of Science ResearcherID or ORCID.
- Organization adds a publication-scope choice; the observed organization textbox had an inconsistent accessible name, so target the visible field under the selected mode.
- Author Profiles can expose published names, organizations, subject categories, metrics, documents, and peer review. These lists and metrics change over time.
- Full Records can expose Core Collection context, source/journal metadata, DOI, accession, indexed date, document type, addresses, research areas, WOS categories, Language, ISSN/eISSN, IDS Number, citations, and cited references.

## Safety and limits

- Search and same-site record reading are read-only. Stop before `Submit a correction`, `Claim my record`, `Share`, any edit/add/save/upload control, or an external publisher/full-text link.
- Never store passwords, cookies, session URLs, account email, user-specific identifiers, live counts, or current result rows in skill files or references.
- Disabled Documents search, filters, citation reports, or premium sections describe the current account/session only; do not infer global availability.

## Drift maintenance

- Before acting, compare the current visible UI, route, labels, controls, permissions, and first-party explanations with this procedure.
- If they differ, make the smallest safe adaptation supported by the UI, record the public/authenticated variant, route, old and observed behavior, evidence source, and date, then update the owning site artifact only when the difference is stable and clear.
- Re-run one safe name/identifier/organization search and the affected validation checks after editing. Report broad or ambiguous changes instead of guessing.

## References

- [Site map](../../sites/webofscience/references/site-map.md) — verified routes and page types.
- [Data model](../../sites/webofscience/references/data-model.md) — author, publication, full-record, and citation fields.
- [Interaction rules](../../sites/webofscience/references/interaction-rules.md) — autocomplete, verification, freshness, and safety.
- [Exploration checklist](../../sites/webofscience/references/exploration-checklist.md) — evidence and known gaps.
