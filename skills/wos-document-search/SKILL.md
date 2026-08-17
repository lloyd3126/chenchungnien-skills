---
name: wos-document-search
description: "Use the Codex in-app browser to search Web of Science documents with Smart Search, Fielded Search, Query Builder, or Cited References, then refine, sort, analyze, and inspect same-site Full Records. Trigger whenever the user asks to find papers, search a topic, search by title/author/date/field, find cited references, inspect DOI or citation metadata, or read a Web of Science record."
---

# Web of Science Document Search

## Purpose and access

Use this skill for read-only document and citation lookup in the user's existing Codex in-app browser. Preserve the current tab and session. Do not open a temporary tab, switch browsers, use an API/CLI, or bypass authentication. Read [document-search](../../sites/webofscience/references/document-search.md), [the site map](../../sites/webofscience/references/site-map.md), and [the interaction rules](../../sites/webofscience/references/interaction-rules.md) when the route or field meaning is unclear.

The current public variant exposed Smart Search and Documents. Availability can differ by database, account, subscription, and session; verify the visible UI before acting.

## Choose the entry point

- Natural-language or broad topic request → `Smart Search` at `/wos/woscc/smart-search` or `/wos/alldb/smart-search`.
- Explicit fields, operators, or date range → Documents → `FIELDED SEARCH` at `/wos/woscc/basic-search`.
- Cited author, cited work, or cited years → Documents → `CITED REFERENCES` at `/wos/woscc/cited-reference-search`.
- Query Builder request → open `QUERY BUILDER` at `/wos/woscc/advanced-search`, then re-inspect its current controls because its distinct behavior was not fully confirmed in the public pass.
- DOI, WOS accession, source, citation, or detailed metadata request → open a visible same-site result title and verify its Full Record.

## Smart Search procedure

1. Inspect the current tab visually. Confirm the Web of Science header, current route, database scope, and whether `Sign In`/`Register` or an authenticated account variant is visible.
2. If needed, use a visible first-party `Smart Search` link in the same tab. Do not navigate to a guessed session URL.
3. Select `All Databases` or `Web of Science Core Collection` as requested. If the user does not specify a scope, preserve the visible selection and report it.
4. Fill `Search documents, researchers, affiliations, and more` with the user's query and submit. Wait for loading to finish.
5. Verify the result heading, query text, database scope, and at least one result control or same-site record link. Result routes contain dynamic query identifiers; do not persist them.
6. Expand `See how we processed your query` when the query interpretation matters. Treat the displayed interpretation, for example `TS=(...)`, as task-time evidence.
7. Use `Refine results`, sorting, or `Analyze Results` only when requested. Re-fetch and verify the result state after each change.

The result page may expose `Create Alert`, `Add To Marked List`, `Export`, or account-specific controls. Inspect them read-only; stop before executing any alert, export, save, share, or marked-list action unless the user explicitly requests it and the action boundary is clear.

## Fielded Search procedure

1. Open `Advanced Search` → `DOCUMENTS` → `FIELDED SEARCH` and verify the database and edition selectors.
2. Configure visible rows and operators. The observed field picker included `All Fields`, `Topic`, `Title`, `Author`, `Publication Titles`, `Year Published`, `Affiliation`, `Funding Agency`, `Publisher`, and `Publication Date`.
3. Treat the UI's `Topic` definition as authoritative: it searches title, abstract, keyword plus, and author keywords.
4. Inspect the current publication-date picker before selecting a range. Observed choices included `All years`, `Last 5 years`, `Custom`, `Current week`, `Last 2 weeks`, `Last 4 weeks`, and `Year to date`; the available list may drift.
5. Use `Add row` only as needed, fill the requested values, submit `Search`, and verify the result heading or explicit validation/error state.

## Cited References procedure

1. Open `Advanced Search` → `DOCUMENTS` → `CITED REFERENCES`.
2. Use the visible `Cited Author`, `Cited Work`, and `Cited Year(s)` rows, with `And` operators and any current index/search-aid control.
3. Use `Add row` or `Add date range` only when the request needs them. Submit `Search` and verify the resulting route, heading, and result state.

## Refinement, sorting, and analysis

- `Refine results` is a read-only panel. Re-fetch current quick filters, database facets, and publication-year facets; counts are live.
- The sort menu may include relevance, date, citations, usage, recently added, conference title, first-author name, publication title, and document title. Select only the requested order and verify the selected label.
- `Analyze Results` can expose a field selector, sort/show/minimum-count controls, selected-row actions, and download controls. Do not claim an analysis succeeded until the table or chart has loaded; disabled controls may reflect the current selection or account.

## Full Record procedure

1. From a verified result set or Author Profile, choose a visible same-site publication title. Do not follow a publisher or full-text link.
2. Verify the breadcrumb, title, author line, source, volume/issue/pages where present, DOI or WOS accession, published/indexed dates, document type, and the `Citation Network` / `Use in Web of Science` sections.
3. When requested, read abstract, keywords, affiliations, research areas/categories, funding, or `See more data fields`; verify each field on the current page.
4. Report the query, selected scope/fields, record verification signals, and retrieval time. Keep live counts and result rows as task output only, not durable guidance.

## Safety and privacy

- Use only the current Codex in-app browser tab. Never inspect cookies, local storage, passwords, session stores, or hidden account data.
- Do not enter credentials or continue into protected profile/settings work when authentication is not visibly confirmed. Ask the user to sign in manually in the same tab if protected work is requested.
- Stop before `Create Alert`, `Add To Marked List`, `Export`, `Save`, `Share`, `Submit a correction`, `Claim my record`, any edit/upload/add control, or any external publisher/product/full-text navigation unless explicitly requested.
- Never store passwords, session URLs, query identifiers, account names/emails, user identifiers, live counts, citation values, or one-off result rows in skills or references.

## Drift maintenance

Before acting, compare the current visible UI, route, labels, fields, defaults, permissions, and first-party explanations with this procedure. If they differ, use the current UI as the source of truth, make the smallest safe adaptation, and record the public/authenticated variant, route, old and observed behavior, evidence source, and date. Patch the owning site reference only when the difference is stable and directly supported. Re-run the affected safe workflow and the skill validator after editing; report broad or ambiguous changes rather than guessing.

## References

- [Document-search workflows](../../sites/webofscience/references/document-search.md)
- [Site map](../../sites/webofscience/references/site-map.md)
- [Data model](../../sites/webofscience/references/data-model.md)
- [Interaction rules](../../sites/webofscience/references/interaction-rules.md)
- [Exploration checklist](../../sites/webofscience/references/exploration-checklist.md)
