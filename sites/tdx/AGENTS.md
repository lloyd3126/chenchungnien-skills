# TDX Transport Data eXchange

## Scope

This guidance applies to the TDX website at https://tdx.transportdata.tw/ when operating through the Codex in-app browser. TDX is the Ministry of Transportation and Communications transport open-data portal for public transport, roads, traffic, parking, GIS, aviation, shipping, tourism, and related services.

Use the focused skills for operational detail:

- $tdx-api-discovery — discover service families, API/OAS documentation, standards, supply status, public statistics, and data-market offerings.
- $tdx-member-data-access — inspect authenticated API/MQTT keys, service access, usage, applications, cart, subscription, and points.

## Sitemap-assisted inventory

- The visible first-party HTML site map is /sitemap. It exposes service families, developer guidance, standards, public statistics, data-mart pages, monitoring, about pages, and linked source-management systems.
- /robots.txt was opened in the same in-app browser session but rendered the TDX HTML shell rather than parseable robots directives. Record this as invalid robots content; do not infer that no robots file exists.
- Do not copy the current site-map URL inventory, live service counts, current prices, rankings, supplier cells, or account values into instructions.
- Linked GitHub, GitBook, Google Drive, vendor, TICP/Traffic/Parking backend, and digiroad resources are separate sites or systems with their own access and freshness.

## Global routing

- Need a current transport data service or domain → public service family → $tdx-api-discovery.
- Need endpoint groups, OAS, schemas, server URL, or sample-code routing → /api-service/swagger → $tdx-api-discovery.
- Need current source availability by transport category or provider → /data-provide → $tdx-api-discovery.
- Need standards, validators, quality tools, or data-model explanations → /data-standard/description → $tdx-api-discovery.
- Need public platform usage → /statistics → $tdx-api-discovery.
- Need private-sector product descriptions → /data-mart/about or /data-mart/list → $tdx-api-discovery; treat vendor claims and purchase/credential instructions as product-specific.
- Need account keys, enabled service families, per-key usage, applications, or subscription → authenticated member routes → $tdx-member-data-access.

## Navigation

- Header dropdowns: 資料服務, 開發指引, 應用活化, 服務統計, 資料市集, 服務監控, 關於平臺, 來源資料管理.
- 資料服務 menu includes 基礎服務, 進階服務, 加值服務, 票證服務, 歷史服務, GTFS服務Beta, 圖資服務, 第三方服務, 主題服務, and 主資料代碼表查詢.
- 開發指引 menu includes 新手上路指引, API使用指引, MQTT使用指引, MCP使用指引, 範例程式碼, 資料標準規範, and 運輸資料使用指引.
- Footer includes 資料授權利用條款, 隱私權保護及資訊安全, and 網站地圖.
- Authenticated sidebar routes include /user/home, /user/apply/cart, /user/apply/history, /user/dataservice/access, /user/dataservice/key, /user/dataservice/statistics, /user/memberService/manage, and /user/memberService/getEditAuth.

## Operating rules

- Use only the Codex in-app browser for this site task. Bind to the existing active tab, visually inspect before interpreting a route, and capture/verify the same tab after navigation or retry.
- Treat the current visible UI and first-party explanations as the source of truth. A sitemap is an inventory accelerator, not proof that a route, permission, or workflow works.
- Treat service cards, API results, supplier matrices, statistics, pricing, points, application rows, dates, and subscription state as dynamic. Re-fetch them at task time and report the selected route/category/period.
- Keep public and authenticated variants separate. A visible 會員中心, 登出, and auto-logout countdown confirms the authenticated variant; re-check public paths after login when documenting member behavior.
- Default to read-only work. Do not sign out, submit applications, request access, authorize Swagger, purchase or change plans, create/delete keys, change account details, or send forms without explicit action-time approval.
- Never inspect cookies, local storage, session files, passwords, API Client Secrets, download passwords, or unrelated private data. Do not persist full Client Ids or current account values.
- The personal-account branch /user/memberService/getEditAuth is a password gate. Stop there and ask the user to enter the password manually if account details are required.
- Empty content after an initial navigation can be a loading state. Wait or reload the same route once before classifying it; preserve earlier visual evidence if a later control attempt fails.

## Freshness and validation

For a live answer, state the route and selected filters, re-fetch the current result, and verify at least two signals such as heading plus URL, selected control plus result state, or table/chart plus first-party explanation. Do not present the current session's values as durable site knowledge.

## Drift maintenance

Before acting, compare the current visible UI, route, labels, controls, permissions, and first-party definitions with this file and the owning skill. If a stable mismatch is clear, safely complete the requested read-only task, record the public/authenticated variant, route, old behavior, observed behavior, verification evidence, and date, then patch the owning artifact. Do not write secrets or dynamic values. Re-run the affected safe workflow and quick_validate.py; report broad or ambiguous changes instead of guessing.
