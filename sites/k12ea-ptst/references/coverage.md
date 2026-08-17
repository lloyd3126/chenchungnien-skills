# 覆蓋範圍與證據

探索基準：2026-08-17，Codex 內建瀏覽器目前唯一可見分頁，起點為 `https://hr.k12ea.gov.tw/ptst/Home/ptst`。本表保留穩定路由與證據狀態，不保留當次職缺、公告、visitor counter 或登入資料。

## Sitemap inventory

| 來源／路由 | 類型 | 狀態 | 證據 | 備註 |
| --- | --- | --- | --- | --- |
| `/ptst/Sitemap/Index` | 站內 HTML site map | `UI-verified` | `current-tab visual` + `current-tab DOM/interaction` | 由可見「網站導覽」按鈕開啟；列出 PTST 七個主要入口及其他入口網專區。 |
| `/robots.txt` | robots metadata 候選 | `client-blocked` | `automation/control error` + `current-tab visual` | 導航與同分頁重試皆回報 `ERR_BLOCKED_BY_CLIENT`，畫面仍是原首頁；不能推論沒有 robots 內容。 |
| `/sitemap.xml` | conventional Sitemap 候選 | `invalid` | `current-tab visual` + `current-tab DOM/interaction` | 實際呈現網站錯誤 HTML，不是 XML。 |
| `/sitemap_index.xml` | conventional Sitemap 候選 | `invalid` | `current-tab visual` + `current-tab DOM/interaction` | 實際呈現網站錯誤 HTML，不是 XML。 |
| `/sitemap.xml.gz` | compressed Sitemap 候選 | `invalid` | `current-tab visual` + `current-tab DOM/interaction` | 實際呈現網站錯誤 HTML，未產生下載。 |

## Public coverage

| Area | Route／入口 | Status | Evidence and notes |
| --- | --- | --- | --- |
| PTST home | `/ptst/Home/ptst` | explored | `current-tab visual` + `current-tab DOM/interaction`; homepage exposes search summary, support links, news summary, video and qualification graphic. |
| Site map | `/ptst/Sitemap/Index` | explored | `UI-verified`; exact labels and shortcut keys were read. |
| Vacancy index | `/ptst/JobVacancy/Index` | explored | `current-tab visual` + DOM; filters, dependent district/subject controls, result table and pagination confirmed. |
| Vacancy detail | `/ptst/JobVacancy/Detail?ID=<current-row-id>` | explored | Opened by clicking a current `tr[data-vacurl]`; detail fields, recruitment rounds, status and protected fields confirmed. |
| News index | `/ptst/News/Index` | explored | `current-tab visual` + DOM; category links `全部`／`公告訊息`／`活動訊息`／`即時新聞` and detail links confirmed. |
| News detail | `/ptst/News/Detail?ID=<current-list-id>` | explored | `current-tab visual` + DOM; heading, type, date, publisher, body, return link and external share links confirmed. |
| Support index | `/ptst/RecruitSupport/Index` | explored | `current-tab visual` + DOM; all visible county entry labels and links confirmed. |
| Support list/detail | `/ptst/RecruitSupport/List?CountyCode=<visible-code>` and detail from visible list | partial | DOM and same-tab navigation confirmed; repeated screenshot attempts timed out or returned target-closed control errors. Preserve the route/content evidence, but do not call these pages visually accessible from this run. |
| Job-seeker guidance | `/ptst/Instruction/Index?FormID=<visible-href>` | explored | `current-tab visual` + DOM; page says login and resume completion are required for vacancy search. |
| Laws | `/ptst/Laws/Index` | explored | `current-tab visual` + DOM; 10-row first page table and external link types confirmed. Do not infer current law text without opening the linked first-party source on request. |
| FAQ | `/ptst/FAQ/Index` | explored | `current-tab visual` + DOM; keyword search changed the visible question set while URL stayed the same; accordion answer expanded successfully. |
| About | `/ptst/About/Index?FormID=<visible-href>` | explored | `current-tab visual` + DOM; site purpose and interaction model read. |
| Teaching | `/ptst/Teaching/Index` | explored | `current-tab visual` + DOM; video and job-seeker PDF links listed. External resources were not opened. |
| Privacy／security | `/ptst/Home/Privacy?...`, `/ptst/Home/Safety?...` | explored | `current-tab visual` + DOM; first-party data, cookie, security and external-link explanations read. |

## Authentication and protected branches

| Entry | Observed behavior | Status | Evidence |
| --- | --- | --- | --- |
| `求職者登入` | PTST login page with account, password, CAPTCHA, quick registration, password recovery and social login controls | explored, no sign-in | `current-tab visual` + DOM; no credentials or CAPTCHA entered. |
| `快速註冊Sign` | Terms modal first; registration form asks for Email, password, name, phone, birthday, national ID and CAPTCHA | explored, no agreement | `current-tab visual` + DOM; modal closed without checking or accepting. |
| `我的最愛` | Redirects to `/Home/Account/Login?ReturnUrl=...` in unauthenticated session | protected—awaiting user choice | `current-tab visual` + DOM. This is a login boundary, not proof the feature is absent. |
| `求才者登入` | `/Config/` management login with CAPTCHA and county/school account application links | protected—awaiting user choice | `current-tab visual` + DOM; no backend exploration. |
| Resume／application／employer workflows | Not entered | protected—awaiting user choice | No user login consent was provided; do not infer fields or permissions. |

## Safe interaction evidence

| Feature | Start and test | Observed result | Boundary |
| --- | --- | --- | --- |
| City → district | Select `臺北市` in `*必填 縣市` | `地區` populated with `全區` and current Taipei districts | Safe read-only interaction; re-read options per county. |
| Domain → subject | Select `語文領域` | `領域科目` populated with current language-subject options and selected default | Options are dynamic; do not hard-code a closed taxonomy. |
| Vacancy query | Choose representative filters, enter a non-sensitive school keyword, click `查詢` | Query route retained parameters and table changed; empty result is a valid result state | Query is safe; report selected filters and verify result state. |
| Vacancy reset | Click `重設` | Form controls cleared; observed query URL could remain and result state could stay empty | Re-open unfiltered index when a fresh search is needed. |
| Vacancy row | Click first result row | `tr[data-vacurl]` navigated to detail | Do not click `我有意願`; it is an application/interest action. |
| FAQ accordion | Click a visible question | Button became `[expanded]` and answer text appeared | Read only current answer; do not make legal conclusions beyond site text. |
| FAQ keyword search | Enter `資格`, click `查詢` | Visible question set narrowed; URL stayed `/ptst/FAQ/Index` | Client-side/current-page behavior must be rechecked after drift. |

## Second-pass audit

- [x] Returned to site map and checked the PTST route group again.
- [x] Returned to PTST home and rechecked header, nav, vacancy controls, support links, news and account buttons.
- [x] Revisited the major page types: list, detail, FAQ, policy, guidance, laws and teaching links.
- [x] Rechecked public form controls and documented the city/district and domain/subject dependencies.
- [x] Marked robots and sitemap-candidate failures separately from UI-verified site map evidence.
- [x] Marked authenticated branches as protected rather than assuming absence.
- [x] Stopped before login, CAPTCHA, registration agreement, favorite mutation, application, sharing and employer-side changes.
