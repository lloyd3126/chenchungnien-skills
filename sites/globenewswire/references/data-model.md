# GlobeNewswire public data model

## Entities

| Entity | Purpose | Important fields observed | Relationships and routes |
| --- | --- | --- | --- |
| Release | A public corporate press release or disclosure | title, publication timestamp with timezone, language, source organization, body, release summary, tags, industry, company website, release URL/identifier | Search/category rows link to Release detail; detail links back to Organization, Tag, RSS/ATOM, and adjacent releases |
| Organization | The named source/company attributed to a release | display name, encoded visible route, release list, page number | Release `Source` link opens Organization results; Organization results contain Release rows and pagination |
| Taxonomy category | Broad public news group | visible label, category path, subcategory labels | Home/Newsroom navigation → category list → subcategory list → Release rows |
| Keyword query | User-supplied public search term | keyword, scope (`Everything` observed), page size (`10` observed), result page | Newsroom search → `/en/search/keyword/<encoded-keyword>?pageSize=10`; result rows link Release and Organization |
| Search filter | Optional narrowing dimension | `Industry`, `Subject`, `Tag`, `Language`, `More Filters` labels; selected chips such as `Keyword` or `Organization` | Search Results page; available option list and semantics must be re-read from live UI because this pass could not validate button expansion |
| Tag | Release-associated topic label | visible tag text, encoded tag route | Release detail → Tag results route; representative Tag route was observed but not opened in this pass |
| Feed | Public syndication representation | grouping (subject/industry/location), format (RSS, ATOM, JavaScript), feed title, visible first-party URL | `/rss/list` directory → exact visible feed link; Release detail may expose organization RSS/ATOM links |

## Relationship map

`Keyword query` and `Taxonomy category` return `Release` rows. Each Release points to one `Organization`, zero or more `Tag` values, one or more visible taxonomy labels, and optional `Feed` links. Organization and Tag routes return another Release list rather than a different private record type.

## Field interpretation rules

- Treat a displayed date/time as the release's published time shown by GlobeNewswire, not as the time the agent retrieved it. Store both only when the task needs temporal provenance.
- Treat `Source` as the public organization attribution. Do not infer legal identity, ownership, financial condition, or endorsement from the label.
- Treat `Release Summary`, body text, forward-looking statements, and company profile as issuer-provided content. Preserve attribution and distinguish it from independently verified facts.
- Treat `Industry`, `Subject`, and `Tag` as site taxonomy or release labels. Do not infer that missing labels mean the release does not belong to a topic.
- Treat PDF/Print/RSS/ATOM links as representations or retrieval surfaces for the same public release; verify the target before claiming an export or feed was opened.

## Dynamic versus durable information

Durable knowledge includes route patterns, page types, field meanings, and navigation labels. Dynamic knowledge includes current release rows, timestamps, organization histories, tag membership, feed entries, search counts, ordering, and availability. Re-fetch dynamic values for every task and never copy them into skills or site guidance.
