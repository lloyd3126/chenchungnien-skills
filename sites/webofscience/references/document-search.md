# Web of Science document-search workflows

## Evidence basis

The public workflow below was inspected in the user's existing Codex in-app browser on 2026-08-18. Evidence was `current-tab visual` plus `current-tab DOM/interaction`; no alternate browser, API, CLI, or external site was used. The visible tab showed `Sign In` and `Register`, so this is a public/unauthenticated variant. Re-check permissions and labels at task time.

## Smart Search

Entry: `Smart Search` → `/wos/woscc/smart-search` or `/wos/alldb/smart-search`.

1. Confirm the database toggle (`All Databases` or `Web of Science Core Collection`) and the current route.
2. Fill `Search documents, researchers, affiliations, and more` with the user's query and submit.
3. Wait for the loading state to finish. Verify the results heading, query text, database scope, and at least one result control or record link.
4. Expand `See how we processed your query` when the query interpretation matters. The public pass showed a fielded interpretation such as `TS=(...)`; treat it as the current query explanation, not a universal parser rule.
5. Use `Add Keywords` or visible quick-add keyword chips only when the user asks to broaden or narrow the query. Re-fetch results after the change.

The results page can expose `Analyze Results`, `Citation Report`, `Create Alert`, `Refine results`, a sort menu, `Add To Marked List`, `Export`, and a preferred-results mode such as `Combined Semantic and Boolean`. Alert, marked-list, export, and other account-affecting actions are approval boundaries; inspect controls without executing them unless explicitly requested.

## Result refinement and sorting

`Refine results` opened a read-only panel with `Search within topic`, quick filters such as `Review Article` and `Open Access`, database filters, and publication-year filters. Counts in this panel are live and must not be copied into durable guidance.

The observed sort menu included relevance, newest/oldest publication date, citation order, usage order, recently added, conference title, first-author name, publication title, and document title. Obtain the current option list from the visible menu because it may vary by result context.

## Documents: Fielded Search

Entry: `Advanced Search` → `DOCUMENTS` → `FIELDED SEARCH` → `/wos/woscc/basic-search`.

- Confirm `Search in: Web of Science Core Collection` and the visible `Editions` selection before submitting.
- The observed initial rows were `Topic`, `All Fields`, and `Publication Date` with an `And` operator between text rows and a default date-range value. Do not assume the default date range is unchanged for another session.
- The field picker exposed `All Fields`, `Topic`, `Title`, `Author`, `Publication Titles`, `Year Published`, `Affiliation`, `Funding Agency`, `Publisher`, and `Publication Date`.
- The `Topic` help text defined Topic as searching title, abstract, keyword plus, and author keywords.
- Publication-date options included `All years`, `Last 5 years`, `Custom`, `Current week`, `Last 2 weeks`, `Last 4 weeks`, and `Year to date`; the UI also showed an `Index Date` grouping and a `Custom` option. Read the current picker before selecting a range.
- Use `Add row`, visible operators and field pickers, then `Search`. Use `Clear` only when clearing the current query is within the user's request.

## Documents: Cited References

Entry: `Advanced Search` → `DOCUMENTS` → `CITED REFERENCES` → `/wos/woscc/cited-reference-search`.

The observed form exposed `Cited Author`, `Cited Work`, and `Cited Year(s)` rows, `And` operators, `Select from Index` or search-aid controls where available, `Add row`, `Add date range`, `Clear`, and `Search`. Fill only the fields needed for the user's citation lookup and verify the result heading after submission.

## Query Builder

`QUERY BUILDER` linked to `/wos/woscc/advanced-search` and was opened during the public pass, but the distinct control model was not fully confirmed. Re-inspect the current tab before relying on a Query Builder-specific procedure; do not infer its behavior from Fielded Search.

## Full Record

From a visible same-site result title, open `/wos/<database>/full-record/<WOS accession>` and verify the breadcrumb, title, author line, source, volume/issue/pages where present, DOI or accession number, published/indexed dates, document type, abstract/keywords when requested, categories, and the `Citation Network` / `Use in Web of Science` sections. Use `See more data fields` only when additional metadata is needed.

Full-text publisher and ProQuest links were visible on the inspected record but were not followed. Treat them as external-navigation boundaries and stop unless the user explicitly asks to open them.

## Freshness and privacy

Search result counts, result rows, citation counts, usage values, dates, availability, session/query identifiers, and user/account values are dynamic or sensitive. Retrieve them live for each task; never hard-code the exploratory result or a tokenized route into skills, references, or reports.
