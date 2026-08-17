# TDX API and public-site routing

## Scope

Verified through the Codex in-app browser against the TDX domain on 2026-08-17. Routes and labels are durable routing clues; catalog contents, prices, counts, statistics, supplier cells, and product descriptions are dynamic.

## Inventory and navigation

- /sitemap is the first-party HTML site map. It lists service families, API/developer guidance, standards, public statistics, data-mart pages, monitoring, about pages, and linked source-management systems.
- /robots.txt rendered the TDX HTML shell in the explored session rather than a parseable robots document. Treat this as invalid robots content, not evidence that no robots file exists.
- Header dropdown labels are 資料服務, 開發指引, 應用活化, 服務統計, 資料市集, 服務監控, 關於平臺, and 來源資料管理. The visible 資料服務 menu includes 基礎服務, 進階服務, 加值服務, 票證服務, 歷史服務, GTFS服務Beta, 圖資服務, 第三方服務, 主題服務, and 主資料代碼表查詢.
- The 開發指引 menu exposes 新手上路指引, API使用指引, MQTT使用指引, MCP使用指引, 範例程式碼, 資料標準規範, and 運輸資料使用指引.

## Page taxonomy

| Need | Route | What to verify |
| --- | --- | --- |
| Browse public services | /data-service/<family> | service family heading, 資料主題/領域類型/資料類型, cards, version, access rule, 計次/計量, explanation |
| Read API contract | /api-service/swagger | service-family selector, domain selector, OAS version, server, Authorize, endpoint groups, schemas |
| Check source availability | /data-provide | category, table heading, legend, supplier rows, current-year marker |
| Understand standards | /data-standard/description | transport domain, specification, validator, sample-code, query/quality-check links |
| Read public usage | /statistics | service/domain/month filters, chart/list, optional SVG/PNG/CSV exports |
| Understand data market | /data-mart/about | purpose, exchange principle, listing benefits, application template |
| Browse private offerings | /data-mart/list | vendor/product description, access or purchase wording, product-specific freshness and credentials |
| Read platform rules | /about/faq, /about/service | TDX role, OData/API-key statements, key limit, access approval, history workflow |

## Durable first-party definitions

- TDX describes itself as a Transport Open API Portal for nationwide road, rail, aviation, shipping, GIS, traffic, tourism, and other transport data.
- The FAQ states that public APIs are normalized around transport data standards and exposed through an international OData-style interface.
- The API guide says visitor mode is browser-only, limited to basic services and a daily source-IP limit; member mode requires an API key for full service families.
- /about/service says members can create up to three API keys, some service families are enabled on membership while approval-gated families require a member request and administrator review, and general historical data can be generated from a date range with email notification.
- /data-standard/description explains that standards provide common formats and data models across public transport, roads, parking, and related domains, with validators and search/quality tools.

## Verification notes

- 資料服務 family pages can initially show only the shell while content is loading; wait or reload the same route before classifying the page as empty.
- The basic family visibly exposes a paginated service catalog and cards with 計次 : 1500次 / 1 點 and 計量 : 150MB / 1 點 during this session. Treat these as current UI values, not permanent pricing.
- On Swagger, changing the service-family selector repopulated the domain selector. A later domain selection temporarily left the server URL and endpoint panel inconsistent with the selected family; re-check the current visible selection before claiming the selected OAS loaded.
- /data-provide uses a matrix and legend; do not infer missing data from an omitted row or from a single category.
- /statistics exposes current aggregate totals and Top 10 charts. Always state the selected period/category and refresh before reporting live values.

## Linked-resource boundaries

The site map links to GitHub sample code, GitBook guides, Google Drive tables, link.motc.gov.tw, TICP/Traffic/Parking backends, and digiroad.transportdata.tw. These are linked resources with separate ownership, access rules, and freshness. Use the same in-app browser only when the user asks for the linked material; do not silently treat external content as TDX UI evidence.
