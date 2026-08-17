# Web of Science site map

## Evidence basis

The route map combines `current-tab visual` and `current-tab DOM/interaction` evidence from the user's existing Codex in-app browser: a public Smart Search/Documents pass on 2026-08-18 and a separately recorded authenticated Researcher Profile pass on 2026-08-17. Treat public and authenticated behavior as separate variants.

## Verified route and page types

| Page type | Verified route or entry | Purpose | Verified controls / sections | Status |
| --- | --- | --- | --- | --- |
| Smart Search | `/wos/woscc/smart-search` or `/wos/alldb/smart-search` | Natural-language/topic search across the selected database scope | Database toggle, query box, query-processing disclosure, quick-add keywords, results, refinement, sorting | UI-verified in public variant |
| Smart Search Results | `/wos/<database>/summary/...` | Review a live result set | Result heading, query interpretation, Documents/Researchers links, Refine results, sort, Analyze Results, Full Record links | UI-verified; query identifiers are dynamic |
| Analyze Results | `/wos/<database>/analyze-results/...` | Aggregate a result set by a selected field | Field selector, sort, display count, minimum record count, refine/exclude/download controls | UI-verified; data state depends on selection and permissions |
| Documents — Fielded Search | `/wos/woscc/basic-search` | Search explicit bibliographic fields | Database/edition selectors, field rows, operators, date range, Add row, Clear, Search | UI-verified in public variant |
| Documents — Cited References | `/wos/woscc/cited-reference-search` | Find records by cited author/work/year | Cited Author, Cited Work, Cited Year(s), index/search aids, Add row, Add date range, Clear, Search | UI-verified in public variant |
| Documents — Query Builder | `/wos/woscc/advanced-search` | Build a structured query | Entry and tab were opened; distinct control behavior remains to be rechecked | Partial |
| Researcher Search | `/wos/author/author-search` | Find author records | Search mode, name fields, ResearcherID/ORCID field, organization field, publication-scope radios, autocomplete, Search/Clear | UI-verified |
| Author Profile | `/wos/author/record/<record-id>` | Read an author record | Identifiers, published names, organizations, subject categories, Metrics, Documents, Peer Review | UI-verified |
| Full Record | `/wos/<database>/full-record/<WOS accession>` | Read one indexed document | By, source, volume/issue/pages, DOI, published/indexed, type, addresses, categories, expanded fields, Citation Network | UI-verified in public and authenticated variants |
| Metrics Dashboard | Profile `Metrics dashboard panel` overlay | Read profile metrics and beamplot/citation sections | Core Collection metrics, Author Impact Beamplot, `Open Filters` → Author Position, Geographic Citation Map, Peer Review Metrics, Derwent notice | UI-verified |
| General Settings | `/wos/my/settings/general` | Read defaults | Language, default search page, Smart Search/Core Collection defaults, advanced-search defaults, rows/display sorting | UI-verified |
| Profile Settings | `/wos/my/settings/profile` | Read/edit profile preferences | Edit profile, Publication preferences, Peer review preferences, ORCID syncing tab, View profile | UI-verified for page and first three tabs; ORCID tab unconfirmed |
| Communications Settings | `/wos/my/settings/communications` | Read notification preferences | Profile events, reviewed-article notifications, profile tips, authored-publication updates | UI-verified; email values intentionally not retained |
| Homepage Settings | `/wos/my/settings/homepage` | Read homepage widget preferences | Widget switches, move up/down controls, View Homepage, Save | UI-verified; no changes made |

## Global menus

- Header `Language dropdown. English selected` showed Simplified Chinese, Traditional Chinese, English, Japanese, Korean, Portuguese, Spanish, Russian, and Arabic. No language was changed.
- Header `Web of Science products dropdown` showed Master Journal List, InCites Benchmarking & Analytics, Journal Citation Reports ™, Web of Science Research Intelligence, Research Horizon Navigator, Essential Science Indicators, EndNote, and EndNote Click. These are linked-product entry points and were not followed.
- Header account menu showed My Profile, Settings, End session, and End session and log out. Only Settings was opened; the two end-session entries were not used.
- Side `MENU` showed My Web of Science → Profile and My records. My records exposed Publications, Grants, Peer reviews, Editor records, Editorial board memberships, Pending records, and their add controls; child pages were not opened.

### Public 2026-08-18 variant

- Header showed `Smart Search`, `Advanced Search`, `Research Assistant`, `Sign In`, `Register`, language, and Products.
- Smart Search showed `All Databases` and `Web of Science Core Collection` scope toggles and the query field `Search documents, researchers, affiliations, and more`.
- The public Smart Search result page exposed `See how we processed your query`, quick-add keywords, `Analyze Results`, a disabled `Citation Report` in the observed context, `Create Alert`, `Refine results`, sorting, `Add To Marked List`, `Export`, and same-site publication links.
- `Advanced Search` exposed `DOCUMENTS` and `RESEARCHERS`. Documents showed `FIELDED SEARCH`, `QUERY BUILDER`, and `CITED REFERENCES`; Researchers showed `Name Search` with Last Name and First Name fields.
- The footer exposed first-party legal/support/training links and no visible Sitemap link. External links were not followed.

## Inventory status

- No visible site map was found in the current UI.
- `robots.txt` and `sitemap.xml` were attempted and retried only in the current tab. Neither was visibly rendered or downloaded. Keep both as `client-blocked`, not `invalid`, `unavailable`, or proof of absence.
- Do not copy the current result list, tokenized session URL, user-specific record ID, or live metrics into route guidance.
