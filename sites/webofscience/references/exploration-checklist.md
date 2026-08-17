# Web of Science exploration checklist

## Evidence integrity

- [x] Existing active tab identified and claimed before navigation.
- [x] All target navigation attempts used the same in-app tab; no temporary tab or alternate browser was created.
- [x] Screenshots were captured before navigation, after each navigation attempt, after retries, and after meaningful interactions.
- [x] `robots.txt` and `sitemap.xml` control failures were retained as `client-blocked` evidence and not converted into claims of empty content.
- [x] Account email, live counts, current search results, session URL, and user-specific identifiers were not written into durable artifacts.

## Coverage

### Public pass — 2026-08-18

| Area | Observed labels / state | Status | Evidence |
| --- | --- | --- | --- |
| Smart Search landing | Database scope toggle, natural-language query box, Research Assistant cards, sign-in/register gate | explored | current-tab visual + DOM/interaction |
| Smart Search results | Processed-query disclosure, keyword chips, Refine results, sorting, Analyze Results, same-site record links | explored | current-tab visual + DOM/interaction |
| Result refinement | Search within topic, Review Article, Open Access, Database, Publication Years | explored | current-tab visual + DOM/interaction |
| Result sorting | Relevance, date, citations, usage, recently added, author/title ordering | explored | current-tab visual + DOM/interaction |
| Analyze Results | Research Areas field, sort/show/minimum-count controls, refine/exclude/download controls | partial | current-tab visual + DOM/interaction; observed data state had no selected rows |
| Documents — Fielded Search | Database/edition, field rows, operators, date range, Add row, Clear, Search | explored | current-tab visual + DOM/interaction |
| Documents — Cited References | Cited Author, Cited Work, Cited Year(s), index/search aids, Add row, Add date range | explored | current-tab visual + DOM/interaction |
| Documents — Query Builder | Entry opened; distinct behavior not fully confirmed | partial | current-tab visual + DOM/interaction |
| Full Record from document results | title, author, source, DOI, dates, type, abstract/keywords, categories, funding, Citation Network | explored | current-tab visual + DOM/interaction |
| Public authentication boundary | Sign In and Register visible; no credentials entered | protected—awaiting manual sign-in | current-tab visual |

| Area | Observed labels / state | Status | Evidence |
| --- | --- | --- | --- |
| Researcher Search | Name Search, Author Identifiers, Organization; name autocomplete; organization publication-scope radios | explored | current-tab visual + DOM/interaction |
| Author Profile | Published names, Organizations, Subject Categories, Metrics, Documents, Peer Review | explored | current-tab visual + DOM/interaction |
| Metrics Dashboard | Core Collection metrics, Author Impact Beamplot, Open Filters, Geographic Citation Map, Peer Review Metrics, Derwent notice | explored | current-tab visual + DOM/interaction |
| Full Record | title, author, source, DOI, dates, type, address, categories, expanded fields, Citation Network | explored | current-tab visual + DOM/interaction |
| General Settings | language, default search page, database, advanced-search defaults, row/display sorting | explored | current-tab visual + DOM/interaction |
| Profile Settings | Edit profile, Publication preferences, Peer review preferences | partial | current-tab visual + DOM/interaction |
| ORCID syncing | tab visible but outside active viewport; safe click could not be completed | blocked | automation/control error; no behavior claim |
| Communications Settings | four notification groups and ON switches; account email visible but omitted | explored | current-tab visual + DOM/interaction |
| Homepage Settings | widget switches, move up/down, View Homepage, Save | explored | current-tab visual + DOM/interaction |
| My records child pages | Publications, Grants, Peer reviews, Editor records, Editorial board memberships, Pending records labels visible | partial | current-tab DOM/interaction; child pages not opened |
| Products links | linked product names visible | not followed | current-tab visual + DOM/interaction |
| External full text / publisher pages | links visible on Full Record | not followed | current-tab DOM/interaction |

## Interaction evidence

| Feature | Input/state | Observed result | Durable implication |
| --- | --- | --- | --- |
| Name Search | Last Name + First Name, then autocomplete options | Suggestions appeared; first Search click selected a suggestion; second exact Search click opened Author Profile | Resolve suggestions before submitting and verify the result |
| Author Identifiers | Mode switch | Field label stated Web of Science ResearcherID or ORCID; placeholder showed example formats | Use live visible field; do not hard-code examples as data |
| Organization | Mode switch | Organization field plus radio choices for recent/5-year/all publications | Preserve current radio selection in result verification |
| Metrics dashboard | Open metric dashboard → Open Filters | Full overlay; Author Position filter exposed `All`; empty profile showed no data | Read only; treat empty/premium states as account-specific |
| Profile tabs | Documents ↔ Peer Review | Peer Review initially loaded, then showed explicit empty state | Wait for loading before classifying empty |
| Full Record expansion | See more data fields | Language, accession, ISSN/eISSN, IDS fields appeared | Expand only when needed and verify new labels |
| Settings navigation | Visible settings links | General, Profile, Communications, Homepage routes loaded | Route from visible links; account settings remained unverified |

## First-party explanations captured

- `Name Search` says it finds an author record by searching first and last names.
- Metrics Dashboard says citation counts are from Web of Science Core Collection.
- Profile Completeness says a complete profile increases visibility in institutional search results and is private to the user.
- Profile Settings says published names are the names on publications and organization history comes from article address fields; document-level corrections use Data Correction.
- Peer Review preferences expose display/availability/automatic-add controls; these are account settings, not read-only search filters.

## Remaining gaps

- No Sitemap or robots XML/text was retrieved; both candidates remain client-blocked in the in-app control path.
- The public pass did not fully verify Query Builder's distinct behavior, Smart Search's Research Assistant cards, export/alert/marked-list actions, or external publisher/product pages.
- The authenticated profile/settings branch was not re-entered during the 2026-08-18 public pass; use the earlier authenticated notes only after confirming the current visible account variant.
- ORCID syncing tab behavior, Account Settings, child My records pages, external product pages, publisher pages, and all state-changing controls remain unconfirmed or intentionally untested.
