# 頁型、資料模型與路由

## Entity model

| Entity | Stable identifiers／fields | Read and search surfaces | Relationships |
| --- | --- | --- | --- |
| Vacancy | `ID` from the current row's `data-vacurl`; vacancy number; posting date; school code/name/address; county/district; vacancy type; education level; domain/subject; quota; status; recruitment rounds; hire period | `/ptst/JobVacancy/Index` result table → click row → `/ptst/JobVacancy/Detail?ID=...` | Belongs to a school and one or more domain/subject entries; may expose a protected application action and favorite control. |
| School | school code, name, address, county/district; contact and description may be protected | Vacancy detail; school-name filter | Publishes vacancies; map link is external and not part of PTST read model. |
| Recruitment round | round number, registration deadline, examination date, qualification notes | Vacancy detail | Belongs to a vacancy; additional rounds may require login. |
| News item | list/detail `ID`, type, date, title, publisher, body | `/ptst/News/Index` → `/ptst/News/Detail?ID=...` | Categorized as all／announcement／activity／instant news. |
| County support item | county code from visible county link, date, title, body, optional image | `/ptst/RecruitSupport/Index` → county list → detail | Belongs to one county; measures and eligibility are time-sensitive. |
| FAQ item | question text, expanded state, answer text | `/ptst/FAQ/Index`; keyword filter and accordion | FAQ page provides first-party explanations, not an independent legal opinion. |
| Law entry | row number, title, category, external URL | `/ptst/Laws/Index` | PTST links to external legal sources; link presence is not a current-law verification. |
| Teaching resource | number, title, external video or same-origin PDF URL | `/ptst/Teaching/Index` | Resource is an entry point; content is not verified until the resource is opened. |
| Candidate account | account identifier, password, CAPTCHA, profile/resume fields and protected favorite/application surfaces | `/ptst/Account/Login`, registration modal/form, redirect from favorites | Not explored in authenticated state; never invent fields or values beyond current visible form. |
| Employer account | management login and county/school application links | `/Config/` | Protected; no school-side vacancy creation or matching workflow was explored. |

## Page taxonomy

### Vacancy search/list

Entry: home `職缺資訊` or site-map `2-1 職缺資訊`.

Core controls: announcement date range, examination date range, required county, dependent district, establishment type, school name, vacancy type, education level, domain, dependent subject, keyword, `查詢`, `重設`.

Result: table with county, school, domain/subject, announcement date, examination date, hire period, education level, vacancy type and favorite column. The site warns that only the latest 100 related records are shown or that the search should be narrowed; pagination is visible when more results exist.

Verification: check selected options, query URL/state, result table headings and at least one row. If a row is clicked, verify the detail heading and vacancy identity.

### Vacancy detail

Entry: click a current result row. The row is not a visible link; the current DOM exposes `data-vacurl`.

Read-only fields: posting date, vacancy number, school code/name/address, county/district, type, education level, domains/subjects, quota, vacancy status, recruitment rounds and hire period.

Unauthenticated limits: additional rounds, contact person, phone, email, related links and vacancy description may appear as `請登入後查詢`.

Stop conditions: `我有意願`, favorite/star, login and any confirmation or form submission.

### News and county-support lists

News is a category-filtered list with date/title/publisher links to detail. County support starts with a county directory, then a county list, then detail with date/title/body. Use current visible hrefs; IDs and county codes are lookup values, not a route grid to guess.

### FAQ and reference pages

FAQ is a keyword-filtered accordion. The query can update the question set without changing the URL; the expanded button and answer text are the verification signal. Laws and Teaching are tables of links; they do not make the linked external contents part of the current verified page.

## Workflow routing

| User need | Entry → path | Result verification |
| --- | --- | --- |
| Find vacancies by county／school／type | Home → `職缺資訊` → set filters → `查詢` | Selected controls + query state + table headings/rows. |
| Read one vacancy | Current result row → detail | Vacancy number, school, type, level, rounds, status and protected-field markers. |
| Find an announcement | `訊息公告` → current category/list item → detail | Heading, type, date, publisher, body and return link. |
| Read county support | Support index → visible county → list item → detail | County heading, item date/title and full visible body. |
| Answer eligibility question | `常見問題` → keyword if useful → expand current question | Expanded state and answer text; cross-check linked law only on request. |
| Find operation material | `求職說明` or `操作教學` | Page heading and visible first-party statement/link; external resource remains unverified until opened. |

## Freshness and drift

Treat all result rows, counts, dates, statuses, quota, support benefits, FAQ answers and link inventories as live. Re-fetch the current entry page and record the current UI state instead of using this reference as a data cache. If a route or field changes, preserve the old observation as historical evidence only and update this file only after a current same-tab visual/DOM verification.
