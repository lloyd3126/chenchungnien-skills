# Web of Science data model

## Entities and relationships

| Entity | Stable purpose | Important fields or relationships | Dynamic / private notes |
| --- | --- | --- | --- |
| Smart Search Query | Natural-language or topic input translated into a Web of Science query | Query text, selected database scope, processed-query interpretation, quick-add keyword suggestions, link to a result set | Query identifiers, counts, suggestions, and result rows are dynamic; retrieve them live |
| Document Search Query | Structured bibliographic query | Database, edition, field rows, operators, field values, publication-date or index-date range | Defaults and available fields can vary by database/session; verify the current UI |
| Cited Reference Query | Query for records citing a cited author, work, or year | Cited Author, Cited Work, Cited Year(s), operators, optional index/date aids | Inputs and result counts are task-specific; never persist user queries unless requested |
| Search Result Set | Live set of documents or researchers returned by a query | Query context, database, result links, refinement facets, sort order, analysis route | Result counts, rankings, record rows, and dynamic route tokens must not be hard-coded |
| Author Record | Canonical researcher identity shown by Web of Science | Display name, Web of Science ResearcherID and/or ORCID, published names, organizations, subject categories; links to documents and peer reviews | Identifier, name, organization list, and record contents can change; never hard-code a user's identifier |
| Author Search Query | Input used to locate an Author Record | Mode: Name Search, Author Identifiers, or Organization; name fields or ResearcherID/ORCID; for Organization, publication scope: Most recent publications, Publications within 5 years, or All publications | Query and autocomplete options must be obtained live; the Organization field's accessible label was inconsistent in the observed UI |
| Publication / Document | Work associated with an Author Record | Title, document type, authors, source/journal, date, volume/issue/pages, DOI or WOS accession, categories, citations/references, full-text link | Result order, counts, dates, citation values, and availability are dynamic |
| Core Collection Full Record | Detailed view of one indexed Document | By, source, volume, issue, page, DOI, published/indexed dates, document type, addresses, research areas, WOS categories; expanded Language, Accession Number, ISSN/eISSN, IDS Number; Citation Network | Verify against the current page and distinguish WOS metadata from publisher full text |
| Citation Data | Citation context for a Full Record or Author Record | Citations, cited references, last-180-days/since-2013 indicators, Core Collection index sources | Counts are live and account/database dependent |
| Researcher Profile | Signed-in user's editable profile surface | Profile photo, display name, primary organization, published-name and organization-history display switches; publications, grants, peer reviews, editor records, editorial-board memberships, pending records, notifications | Edits, uploads, add controls, and Save change account state |
| Profile Metrics | Aggregate metrics tied to an Author Record | Publications, sum of times cited, H-index, citing articles, patents/policy metrics, peer-review metrics, author impact beamplot | Subscription and account dependent; disabled/premium indicators are session-specific |
| Profile Settings | Preferences for the signed-in account | General search defaults, profile preferences, publication automatic updates, peer-review display/availability, communications, homepage widgets | Some controls are switches/selects and Save; do not alter without explicit request |

## Durable field semantics

- `Name Search` searches an author record using first and last names; the site provides autocomplete suggestions for both fields.
- `Author Identifiers` accepts a Web of Science ResearcherID or ORCID.
- `Organization` adds a publication-scope choice: Most recent publications, within 5 years, or all publications. In the observed UI, the organization textbox exposed an inconsistent accessibility name, so future agents should use the visible field under the `Organization` mode rather than relying on that name.
- `Published names` are publication-author strings associated with an Author Record; `Organizations` are affiliations on the record, not necessarily the current employer.
- A Full Record `DOI` and `WOS accession number` are durable identifiers for that record; retrieve them from the current page rather than constructing them.
- `Web of Science Core Collection` is the database context explicitly attached to the observed metrics and Citation Network.
- `Topic` in Fielded Search is defined by the UI as title, abstract, keyword plus, and author keywords.
- Smart Search can expose a processed query such as `TS=(...)`; treat that text as the current query interpretation and verify it for each request.
- A Full Record connects a Document to authors, source/journal, affiliations, research areas/categories, funding, citation network, and optional external full-text links. External links are not part of the same-site read-only workflow.
- `Profile Completeness Score` is private-to-user UI and should not be written to shared artifacts as a live value.
