# Web of Science

## Scope

- Web of Science provides Smart Search, document fielded search, Query Builder, cited-reference search, author search, author records, Core Collection full records, citation metadata, researcher profiles, profile metrics, peer-review records, and account/profile settings.
- This guidance covers a public Smart Search/Documents variant observed in the Codex in-app browser on 2026-08-18 and a separately recorded authenticated Researcher Profile variant observed on 2026-08-17.
- Keep dynamic data out of durable instructions. Re-fetch names, identifiers, counts, metrics, publication lists, dates, availability, permissions, and settings at task time.

## Sitemap-assisted inventory

- No visible `Sitemap` or `Site map` link was found in the current page, navigation, or footer.
- Same-origin `https://www.webofscience.com/robots.txt`: attempted and retried in the user's existing in-app tab. The control path redirected to a WOS session URL while the screenshot showed a blank/prior-page state; no robots directives were retrieved. Status: `client-blocked`; evidence: `current-tab visual` plus `automation/control error`.
- Same-origin `https://www.webofscience.com/sitemap.xml`: attempted and retried in the same tab. No XML was visibly rendered or downloaded; the browser control path again redirected/left a blank state. Status: `client-blocked`; evidence: `current-tab visual` plus `automation/control error`.
- Do not interpret either client block as proof that the site has no robots file or Sitemap. No CLI, API, web search, external browser, or replacement fetch was used.

## Global routing

- Search documents with a natural-language/topic query → `$wos-document-search` → Smart Search (`/wos/woscc/smart-search` or `/wos/alldb/smart-search`) → choose database scope → submit → verify the result heading/query state → use refinement, sorting, analysis, or a visible same-site Full Record.
- Search documents by explicit fields → `$wos-document-search` → Documents → Fielded Search (`/wos/woscc/basic-search`) → choose fields/operators/date range → Search → verify the result state.
- Search cited references → `$wos-document-search` → Documents → Cited References (`/wos/woscc/cited-reference-search`) → fill Cited Author, Cited Work, or Cited Year(s) → Search → verify results.
- Read a document or citation record → `$wos-document-search` or `$wos-researcher-search` → choose a visible same-site publication title → `/wos/<database>/full-record/<WOS accession>` → verify metadata and Citation Network; do not follow publisher/full-text links unless asked.
- Search an author by name, Web of Science ResearcherID/ORCID, or organization → `$wos-researcher-search` → Researcher Search (`/wos/author/author-search`) → choose the visible search mode → wait for and select autocomplete options → `Search` → verify Author Profile.
- Read the signed-in user's own profile, metrics, peer-review tab, records menu, or settings → `$wos-researcher-profile` → visible account menu or `MENU` → `My Profile`, `Settings`, or `My Web of Science`.

## Navigation and page map

- In the public 2026-08-18 variant, `Smart Search` resolves to `/wos/woscc/smart-search` or `/wos/alldb/smart-search`; `Advanced Search` links to `/wos/woscc/basic-search`, while `RESEARCHERS` links to `/wos/author/author-search`.
- Documents exposes `FIELDED SEARCH`, `QUERY BUILDER`, and `CITED REFERENCES`; fielded search was UI-verified, cited-reference search was UI-verified, and the Query Builder entry was opened but its distinct controls remain only partially confirmed.
- Smart Search result routes contain dynamic query identifiers under `/wos/<database>/summary/...`; never persist those identifiers or live counts.
- `MENU` → `My Web of Science` → `Profile` → `My researcher profile`, `Edit Profile`, `My records`, and `Profile notifications`.
- Expanded `My records` showed `Publications`, `Grants`, `Peer reviews`, `Editor records`, `Editorial board memberships`, and `Pending records`; their add controls are state-changing and were not used.
- Account menu → `My Profile`, `Settings`, `End session`, and `End session and log out`. Never click either end-session item unless explicitly requested.
- `Settings` pages verified in the current tab: `/wos/my/settings/general`, `/wos/my/settings/profile`, `/wos/my/settings/communications`, and `/wos/my/settings/homepage`. `Account Settings` was visible but exposed `javascript:void(0)` and was not verified.
- `Products` exposes linked products including `Master Journal List`, `InCites Benchmarking & Analytics`, `Journal Citation Reports ™`, `Web of Science Research Intelligence`, `Research Horizon Navigator`, `Essential Science Indicators`, `EndNote`, and `EndNote Click`; linked products were not followed.

## Session and operating rules

- Use only the Codex in-app browser and the already-visible user tab. Before navigation, capture URL/title/visible state; after every navigation or meaningful interaction, verify the current URL or heading plus a selected control, result, or explicit state.
- The 2026-08-18 tab visibly showed `Sign In` and `Register`, so treat it as a public/unauthenticated variant. Do not enter credentials; protected profile/settings branches require the user to sign in manually in the same tab.
- Treat the authenticated variant as a separate site variant. Re-check public search, result cards, records, and controls after login before relying on authenticated behavior.
- Select exact autocomplete options before submitting search. A first click on `Search` may select an open suggestion instead of submitting; confirm that suggestion lists are closed, then press the exact `Search` button again.
- Search, opening an observed author profile, opening an observed same-site full record, opening a metrics dashboard, expanding fields, switching tabs, and reading settings are read-only exploration.
- Stop before `Claim my record`, `Submit a correction`, `Share`, `Edit`, `Select file`, `Add`, `Save`, toggling a setting, `End session`, or `End session and log out`. These actions can transmit data or change account state. Opening publisher/full-text links is an external navigation boundary; do not follow unless the user asks.
- Never copy or persist personal email addresses, account names, private profile content, session identifiers, cookies, passwords, ORCID/ResearcherID values, or live result values. Use placeholders and retrieval paths instead.
- Feature availability is variant- and account-dependent: the public pass exposed Documents and disabled Citation Report on the observed result page, while the earlier authenticated/Free View pass showed different disabled or premium controls. Report the current visible state; do not infer global availability.

## Freshness and validation

- For search results, verify the search mode, selected autocomplete values, Author Profile heading, visible identifier/organization/name fields as needed, and result loading state.
- For a full record, verify the breadcrumb, title, author line, source, volume/issue/pages where present, DOI or accession number, published/indexed dates, document type, categories, and the Citation Network section. Use `See more data fields` only when the task needs language, ISSN/eISSN, IDS, or other expanded fields.
- For metrics, record the metric label and current retrieval time; counts and percentile values are dynamic and must not be hard-coded.
- If labels, routes, controls, permissions, or first-party explanations differ, use the current visible UI as source of truth, make the smallest safe adaptation, and record the exact mismatch, public/authenticated variant, route, evidence source, and date. Patch the owning artifact only when the change is stable and directly supported; otherwise report a maintenance gap.

## Known limits

- Sitemap and robots retrieval remained client-blocked in the current-tab browser path; no sitemap or robots directives were retrieved. This does not establish that the site lacks them.
- The public pass did not fully verify Query Builder's distinct behavior, Smart Search's Research Assistant workflows, export/alert/marked-list actions, or any external publisher/product page.
- The authenticated profile branch was explored only for the current signed-in account. The own profile showed empty records and zero metrics in this session; those values are not durable facts.
- Profile Settings `ORCID syncing` was visible as a tab but not opened because the tab was outside the active viewport and the in-app interaction path could not click it safely. Its behavior remains unconfirmed.
- The current exploration did not follow external product links, publisher full-text links, or the irreversible/account-changing controls listed above.

## References

- [site-map.md](references/site-map.md) — verified routes, labels, page types, and navigation.
- [data-model.md](references/data-model.md) — durable entity and field semantics; dynamic fields are explicitly marked.
- [interaction-rules.md](references/interaction-rules.md) — search, autocomplete, tab, settings, verification, and safety rules.
- [document-search.md](references/document-search.md) — public Smart Search, Documents search, result refinement, analysis, and record-reading workflows.
- [exploration-checklist.md](references/exploration-checklist.md) — evidence-backed coverage, tested interactions, and gaps.

## Agent usability checks

- `找 Web of Science 中某作者` → `$wos-researcher-search` → Researcher Search → choose `Name Search`/`Author Identifiers`/`Organization` → select autocomplete values → `Search` → verify Author Profile. This route is directly supported.
- `用主題找文獻` → `$wos-document-search` → Smart Search → submit a query → verify result state → refine/sort or open a same-site Full Record. This route is directly supported.
- `用欄位和日期找文獻` → `$wos-document-search` → Documents → Fielded Search → set fields/date range → Search → verify results. This route is directly supported.
- `找某篇文獻引用的參考文獻` → `$wos-document-search` → Documents → Cited References → fill visible cited fields → Search → verify results. This route is directly supported.
- `讀某篇作者出版品的 DOI 與索引欄位` → `$wos-researcher-search` → verified Author Profile → visible publication title → Full Record → `See more data fields` → verify metadata and Citation Network. This route is directly supported.
- `查看我的研究者指標或設定` → `$wos-researcher-profile` → visible account or `MENU` → Profile/Settings → verify heading and selected tab; stop before Save/Edit/toggle. This route is directly supported.
