# data.gov.tw site map and coverage

## Source and evidence

`https://data.gov.tw/sitemap` was opened from the visible `關於平臺 → 網站導覽` menu in the user's existing Codex in-app browser tab. The page rendered visually and exposed first-party links. Treat route patterns as stable hints, then re-check the current UI before acting.

## Route map

| Area | Visible label | Confirmed route | Coverage | Evidence / notes |
| --- | --- | --- | --- | --- |
| Home | 首頁 | `/` | explored | Current-tab visual and DOM/interaction. |
| Dataset search | 全部資料集瀏覽 | `/datasets/search` | explored | Search, advanced search, facets, sorting, page size, results and query state tested. |
| Dataset detail | 資料集 result | `/dataset/<nid>` | partial | File and API variants opened in the same tab; DOM/interaction confirmed. Visual retries for detail pages were blank or timed out in this run, so do not call them visually accessible without a new screenshot. |
| Pending removal | 預計下架資料集 | `/datasets/unpublished` | explored | Table, keyword search, advanced search, sortable columns, and empty state visually confirmed. |
| Historical | 歷史資料專區 | `/datasets/history` | partial | Table, keyword search, advanced search, sortable columns, pagination and dynamic row list confirmed by DOM/interaction. |
| Dataset inventory downloads | 資料集清單下載區 | `/datasets/datasets_download` | partial | Full and recent-change CSV/XML/JSON download controls confirmed by DOM; downloads intentionally not triggered. |
| API-service subset | API服務資料集 | `/datasets/search?dt=openapi` | explored | Results show `資料提供屬性: API服務`; representative API dataset detail opened. |
| High-value topics | 高應用價值主題專區 | `/high_value_datasets` | partial | Nine topic categories and application carousel controls confirmed; category links currently expose the same route pattern and need current UI re-check. |
| Application showcase | 應用展示專區 | `/expos` | partial | Representative list page opened through `互動專區` default route; individual exposition pages not exhaustively opened. |
| Education / applications / rewards | 教育資源專區／活化應用專區／獎勵活動專區 | `/courses`, `/applications`, `/rewards` | route-map only | First-party site map links confirmed; not needed for dataset retrieval in this run. |
| Interactive requests | 我想要更多／我有話要說 | `/suggests`, `/comments` | route-map only | Site-map links confirmed; comments may require login and were not submitted. |
| News | 最新消息 | `/news` | explored | Category radios, keyword search, export controls, RSS link, table and pagination confirmed. |
| Columns | 專欄文章 | `/columns` | route-map only | Site-map link confirmed; not explored beyond routing. |
| Consultation | 諮詢小組 | `/consult_team` | partial | Heading, setup-point PDF link and meeting-record link confirmed. External PDF not opened. |
| About | 關於平臺 | `/about` | route-map only | Site-map link confirmed. |
| Site map | 網站導覽 | `/sitemap` | explored | First-party route inventory and accessibility keys confirmed visually. |
| FAQ / tools / documents | 常見問答／應用工具專區／指引文件 | `/faqs`, `/convert`, `/about/doc` | route-map only | First-party links confirmed; not needed for the dataset workflows covered here. |
| License / M2M | 授權條款／M2M專區 | `/licenses`, `/m2m` | partial / route-map | `/licenses` heading and language tabs confirmed; article content was empty in the exposed DOM. `/m2m` only route-map confirmed. |
| Statistics | 統計資料 | `/statistics/*` | route-map only | Six first-party statistics routes listed by site map; dynamic charts not explored. |
| Related links | 跨平臺介接即時狀態表／相關資料中心 | `/datasets_links2`, `/civil_dataset_center` | route-map only | Site-map links confirmed; not opened. |

## Main menu structure

- `資料集`: 全部資料集瀏覽、預計下架資料集、歷史資料專區、資料集清單下載區.
- `高應用價值主題專區`: direct link.
- `資料故事館`: 應用展示專區、教育資源專區、活化應用專區、獎勵活動專區.
- `互動專區`: the visible default route is 應用展示專區; site map separately exposes 我想要更多 and 我有話要說.
- `消息專區`: 最新消息、專欄文章.
- Direct links: 諮詢小組、授權條款.
- `關於平臺`: 關於平臺、網站導覽、常見問答、應用工具專區、指引文件.

## Discovery gaps

- No XML Sitemap was retrieved. The first-party HTML site map is the only inventory evidence used here.
- Authentication state was not visibly confirmed. Login-dependent comments and any account functionality remain unexplored.
- External resource URLs, RSS payloads, CSV/XML/JSON downloads, TDX registration, API-key creation, and irreversible submissions were intentionally not executed.
