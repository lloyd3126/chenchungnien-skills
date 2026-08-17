# SEC.gov 頁型與路由地圖

探索基準：2026-08-17，起點為使用者已開啟的 `https://www.sec.gov/`。所有新聞、filing、規則、日期、狀態、數量與結果均為動態資料；本文件只保留穩定頁型、路由模式與重新取得方法。

## Evidence boundary

| Evidence source | Meaning in this inventory |
| --- | --- |
| `current-tab visual` | 首頁 `/` 已在原使用者分頁截圖確認；可見官方政府 banner、SEC header、Menu、hero、Quick Links 與首頁內容。 |
| `current-tab DOM` | 首頁 DOM 確認 `Site Map`、主要 footer links、Quick Links 與首頁 page structure。 |
| `temporary-tab control/DOM` | 其餘頁面在探索期間由瀏覽器控制取得 DOM／form／link 線索；原始使用者分頁的視覺重核因清理失效未完成。這些路由可作為未來 Agent 的候選入口，但不能在本輪標為原分頁 `UI-verified`。 |
| `control error` | 暫存分頁清理與後續 screenshot 曾失效；該錯誤不代表 SEC 路由無內容或不存在。 |

## Sitemap and inventory status

| Source / route | Discovery | Retrieval status | Evidence | Durable conclusion |
| --- | --- | --- | --- | --- |
| footer `Site Map` → `/sitemap` | discovered | `discovered`, not UI-verified in original tab | current-tab DOM; temporary-tab DOM | SEC provides an HTML site map candidate with top-level categories; re-open in the active tab before relying on it. |
| `/robots.txt` | not checked in the original active tab | unknown | none | Do not infer route or access policy from absence of a record. |
| compressed Sitemap candidates | not checked | unknown | none | No download or local parse was performed. |

## Coverage map

| Area | Representative route | Page type and stable controls | Status in this run |
| --- | --- | --- | --- |
| Home | `/` | Official government banner, SEC header/Menu, mission hero, `Quick Links`, Latest News, Upcoming Events, Rulemaking, Investor.gov, footer Site Map. | `explored`; current-tab visual + DOM |
| Site Map | `/sitemap` | HTML inventory grouped by Search Filings, Submit Filings, Data & Research, Rules & Regulations, Enforcement & Litigation, Compliance, Featured Topics and About. | `partial`; temporary-tab DOM, current-tab visual recheck needed |
| Search Filings | `/search-filings` | `Company Search`; `Company and Person Lookup` with placeholder `Name, ticker symbol, or CIK`; Full Text Search; Latest Filings; CIK; SIC; APIs; Search Assistance. | `partial`; temporary-tab DOM |
| Full Text Search | `/edgar/search/` | Initial keyword/company/ticker/CIK/name box; `+ more search options`; `SEARCH`; `Clear all`; advanced date, filing category and location controls; result filters and Show Columns. | `partial`; temporary-tab DOM + safe test query control evidence |
| Latest Filings | `/cgi-bin/browse-edgar?action=getcurrent` | Company, CIK, Form Type, ownership Include/Exclude/Only, entries selector, Retrieve Filings, RSS Feed, filing rows with HTML/text and accession links. | `partial`; temporary-tab DOM |
| Filing Detail | `/Archives/edgar/data/<cik>/<accession>/<accession>-index.htm` | Form, SEC Accession No., Filing Date, Accepted, Documents table, primary document/XML/text, Filer/Subject metadata, CIK, Act, file/film number, SIC. | `partial`; temporary-tab DOM |
| CIK Lookup | `/search-filings/cik-lookup` | Name search, `Search`, up to 100 matching records, name-variation tips, SIC link and EDGAR company database link. | `partial`; temporary-tab DOM |
| Newsroom | `/newsroom` | Latest Press Releases, What's New, Upcoming Events, Speeches & Statements, Videos, Social Media Directory, Podcasts, alert/contact links. | `partial`; temporary-tab DOM |
| Rulemaking Activity | `/rules-regulations/rulemaking-activity` | Search text, status select (`Final`, `Interim Final`, `Proposed`, `Interpretive`, `Concept`), division/office select, year select, activity links and related-activity links. | `partial`; temporary-tab DOM |
| Submit Public Comments | `/rules-regulations/submit-public-comments` | Recent proposals/requests; official PDF or notice; `Submit a Comment`; `View Comments Received`; SRO rulemaking link. | `partial`; temporary-tab DOM |
| Data & Research | `/data-research` | Data Library, Recent Data Sets, Interactive Data Visualizations, Research and Reports, Data Resources, Data Governance, structured data and developer links. | `partial`; temporary-tab DOM |
| EDGAR APIs | `/search-filings/edgar-application-programming-interfaces` | Submissions API, XBRL companyconcept/companyfacts/frames, CORS, bulk ZIPs, update schedule, programmatic access and Developer FAQ links. | `partial`; temporary-tab DOM |
| Submit Filings | `/submit-filings` | EDGAR Next, Filer Manual, Forms Index, Technical Specifications, filing portals, announcements, taxonomies and support contacts. | `partial`; temporary-tab DOM |

## Global navigation clues

The content-site DOM exposed these top-level labels: `Search Filings`, `Submit Filings`, `Data & Research`, `Rules, Enforcement, & Compliance`, `Featured Topics`, `About`, and `Submit a Tip or Complaint`. Utility links included `Newsroom`, `Investors`, `Small Businesses`, and `Whistleblowers`. Re-check labels in the active tab because the mobile Menu and responsive layout can collapse them.

## Unexplored or intentionally untested

- No authenticated or filer-portal variant was explored.
- No comment, complaint, filing, email subscription, RSS subscription, API-token, upload, payment, or account-management action was submitted.
- No exhaustive Sitemap, robots, current filing list, news list, rule list, or comment list was copied.
