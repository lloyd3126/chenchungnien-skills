# Koyfin exploration coverage

本文件保存本輪在使用者現有 Codex 內建瀏覽器分頁中的探索摘要。它是維護索引，不是當前市場資料快照；所有 live values、結果列、日期、價格、持倉與個人工作區內容都要重取。

## Evidence and inventory

| Area | Representative UI / route | Status | Evidence and safe test |
| --- | --- | --- | --- |
| My Screens | `My Screens` `/mys/<screen-id>` | UI-verified | `Modify Criteria` dialog opened and cancelled; criteria、universe、Screen Name、`Save and Apply` boundary observed. UI states a maximum of 2,000 displayed results sorted by Market Cap. |
| Home and news | `/home`, `/news/top`, `/news/gmn` | UI-verified | `Top News`、`Global Markets`、news category tabs and dynamic lists observed. |
| Market Movers | `/mov` | UI-verified | Universe、Sector Filter、market-session controls、performance chart、Gainers／Losers observed; sector filter opened and closed. |
| Security Analysis | `/snapshot/<section>/<security-id>`, `/estimates/<view>/<security-id>`, `/fa/<view-id>/<security-id>`, `/charts/<view>/<security-id>` | UI-verified | A selected security was followed through Overview, Actuals and Consensus, Income Statement and Historical Chart; annual／quarterly, period, currency and chart controls tested. |
| Security news and filings | `/news/n/<security-id>`, `/news/cf/<security-id>` | UI-verified | Company News and Recent Filings panels opened; no filing download or external document was opened. |
| Global search | top search modal | UI-verified | `AAPL` produced multiple listings; `MSFT` temporarily showed no results in this session, so no absence inference is allowed. Modal was closed without selection side effects. |
| My Watchlists | `/myw/<watchlist-id>` | UI-verified | Search filter narrowed the visible table to a representative ticker and was cleared; table view, groups, columns, summary, sort and currency controls observed. |
| My Portfolio | `/myp/pl` | UI-verified | Profit/Loss table and read-only tabs observed; `Edit Portfolio` was not opened. |
| My Dashboards | `/myd/<dashboard-id>` | UI-verified | Sample dashboard panels and chart/table cards loaded; `Edit dashboard`, `Delete dashboard`, `Full View` and `Remove` were not used. |
| My Graphs | `/myg` | partial | Initial screenshot showed an error state; retry DOM showed `Create your first graph`, while later screenshot calls timed out. Treat visual status as unconfirmed. |
| Market dashboards | `/wei` plus sidebar candidates | partial | World Equity Indices was opened and verified; other visible dashboard children were not individually opened. |
| Research tools | `/lot`, `/ms` | UI-verified | Lots of Charts grid and Market Scatter controls/table verified; dynamic charts/results not persisted. |
| Advanced Search | `/search/security`, `/search/transcripts` | UI-verified | Security Search with ticker and Reset; Transcripts Search with event-type filter and Clear; exact listing disambiguation observed. |
| Calendars | `/earc`, `/ecal` | UI-verified | Earnings Calendar and World Economic Calendar headings, date/universe/country controls and table/card structures verified. |
| Advisor Tools | visible sidebar labels | not explored | Client Portfolios、Model Portfolios、Reports remained unverified and may be more permission-sensitive. |

## Sitemap and robots status

- No visible Site Map or first-party inventory link was found in the explored navigation.
- `/robots.txt`: opened in the same active tab; current-tab visual showed Koyfin's wrong-place SPA HTML rather than robots directives. Status: `invalid` for the expected robots metadata response, not evidence that robots or Sitemap is absent.
- `/sitemap.xml`: opened and retried in the same active tab; screenshot/control path timed out and a later retry reported target closed. Status: `client-blocked` with `automation/control error` evidence. It was not parsed and must not be described as empty.
- After the index checks, the same tab was returned to the original `My Screens` route. The later screenshot control continued to time out, so the URL/title confirmation is stronger than a final screenshot for that last restore step.

## Safe interaction evidence

- Collapsed sidebar parents must be expanded before clicking child routes such as `Snapshots`, `Analyst Estimates`, `Financial Analysis`, `News, Filings & Transcripts`, `Graphs`, `Market Dashboards`, `Calendars` and `Advanced Search`.
- Loading indicators appeared on quarterly estimates, financial analysis, historical charts and chart grids; wait for loading to finish before extracting fields.
- Search/filter controls accepted safe representative values and could be cleared/reset. Use the visible result identity and selected filters as verification.
- Save, Apply, Create, Edit, Delete, Share, Duplicate, Import, Download, Export, Add to My Watchlists, Alerts, Notes and portfolio edits were treated as confirmation boundaries.

## Maintenance gaps

- Revisit the unverified Advisor Tools and remaining Market Overview children only when a task needs them and the session's permissions make a read-only inspection appropriate.
- If the same-origin index routes later render real robots/XML content, update this file and the site AGENTS inventory with the actual Sitemap source and stable categories.
- If My Graphs becomes visually stable, repeat its create/list/read workflow without clicking `Create new graph` unless the user explicitly requests a mutation.

## Agent usability checks

These checks were simulated from the generated `AGENTS.md`, skills and directly linked references, without relying on the exploration transcript:

| Request shape | Selected skill and route | Expected safe sequence | Outcome |
| --- | --- | --- | --- |
| 研究一檔股票的目前概覽、估值與財務 | `$koyfin-security-research` → global search／`Security Search` → `Snapshots` → `Financial Analysis` | 先消歧 listing；確認 heading、period、currency；等待 loading；停在儲存／分享前 | Pass: skill gives a concrete entity-resolution path, parent-expansion rule, verification fields and freshness rule. |
| 找市場異動與本週經濟事件 | `$koyfin-market-monitoring` → `/mov` and `Calendars` → `/ecal` | 記錄 universe、sector、date range、timezone；安全篩選；等待載入；以結果表／事件卡驗證 | Pass: route matrix distinguishes movers from macro calendar and prevents treating dynamic values as durable. |
| 不改動地檢查我的 screen 與 watchlist | `$koyfin-watchlists-and-screens` → `/mys/<screen-id>` and `/myw/<watchlist-id>` | 用 search／criteria inspection；screen dialog 選 `Cancel`；清除暫時 filter；不按 Save and Apply | Pass: workspace reference clearly separates read-only controls from mutation boundaries and privacy rules. |
| 確認 ticker 的確切上市標的並搜尋 earnings calls | `$koyfin-advanced-search` → `/search/security` and `/search/transcripts` | 用 Country／Asset Category／Exchange 消歧；設定 event type；等待結果；用 Clear／Reset 收尾 | Pass: skill explicitly handles multiple listings, filters, result verification, transient no-result states and reset. |
