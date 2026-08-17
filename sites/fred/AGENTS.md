# FRED（Federal Reserve Economic Data）網站操作指引

## Scope

這份指引只適用於透過 Codex 內建瀏覽器操作 `https://fred.stlouisfed.org/` 及其在頁面上明確連出的 FRED Help／API 文件。FRED 的核心用途是搜尋、閱讀、比較與下載經濟資料系列；目前數值、搜尋結果、排名、release 日期與可用選項都必須在任務當下重新取得。

## Global routing

- 想找系列、讀取 metadata／觀測值、看圖表、改變圖表範圍或下載資料 → `$fred-series-data`。
- 想找 release 清單、發佈日程、依 release 篩選日曆或查看日期／名稱排序 → `$fred-release-calendar`。
- 想從主題、資料來源或熱門程度發現系列 → `$fred-series-data`，先使用首頁的 `Category`、`Source` 或 `Popular Series` 入口。

## Sitemap-assisted inventory

- 首頁未觀察到可用的 Sitemap／Site map 連結。
- `https://fred.stlouisfed.org/robots.txt` 在目前的 Codex 內建瀏覽器分頁中嘗試兩次，皆回報 `ERR_BLOCKED_BY_CLIENT`，視覺上仍停留在首頁；狀態是 `client-blocked`，不是「沒有 Sitemap」或「內容為空」。
- `https://fred.stlouisfed.org/sitemap.xml`、`/sitemap_index.xml`、`/sitemap.xml.gz` 都在同一分頁實際開啟並顯示 FRED 的 HTML 404 頁（`Looking for Something?`），因此本輪判為 `invalid` Sitemap candidates；沒有下載或解析壓縮 Sitemap。
- 以上路由證據來自 `current-tab visual` 與 `current-tab DOM/interaction`；不要把控制錯誤改寫成資源不存在，也不要把目前完整 URL 清單寫進 skills。

## Navigation

- 首頁：`/`；提供 `Search FRED Data...`、`Category`、`Release`、`Source`、`Popular Series` 與 `At a Glance`。
- 主選單：`Release Calendar`、`Tools`（`FRED Add-in for Excel`、`FRED API`、`FRED Mobile Apps`）、`News`、`Blog`、`About`（`What is FRED`、`Tutorials`、`Digital Badges`、`Contact Us`）、`My Account`、`Explore Our Apps`（FRED、FRASER、ALFRED、CASSIDI）。
- 搜尋結果：`/searchresults/?st=<term>`；結果列會連到 `/series/<series_id>`，並顯示名稱、單位、頻率、季節調整、期間與描述。
- 系列：`/series/<series_id>`；圖表頁有 observations、日期範圍、圖表編輯、下載、來源／release／notes、release tables 與 related data。
- 資料表：`/data/<series_id>`；以 metadata table 加上 `DATE`／`VALUE` 表格呈現觀測值。
- 發現入口：`/categories`、`/releases`、`/sources`、`/tags/series?ob=pv`；分頁通常以 `pageID` 表示，不要保存當下筆數。
- Release 日曆：`/releases/calendar`；有 release 下拉選單、日期前後移動、`today`、按 `Date`／`Name` 排序與日曆資料表。

## Operating rules

- 只使用 Codex 內建瀏覽器與目前可見的 FRED 分頁；不要改用外部瀏覽器、web search、API、CLI、cookies、local storage 或 session 檔案來替代 UI 探索。
- 每次導航後確認同一分頁的畫面、URL、heading／主要控制項與結果；若發生 client block、timeout 或空的自動化結果，先擷取同一分頁畫面，再重試一次，保留先前成功的證據。
- 以 FRED 目前頁面的 source、release、units、frequency、updated／last updated 與 notes 為準；不要從常識猜測定義。
- 目前觀測值、結果數、熱門程度、期間、release 日期、圖表與下載 query 都是動態資料；回覆時重新取得並注明查詢條件與觀察時間。
- 預設只做讀取與可逆互動。下載 CSV／Excel／圖片是入站下載；不要在探索中收藏、分享／發布圖表、訂閱電子報、修改帳號、付款、登出或送出外部表單。
- 需要 vintage／revision 或大量程式化取用時，先讀 FRED 的第一方 API 文件與 ALFRED 說明；API key、帳號與敏感資料不應在瀏覽器中輸入或保存。

## Authentication

本輪未看到登入後的個人化畫面；`My Account` 會連到 `fredaccount.stlouisfed.org`，登入後功能未探索。若未來分頁沒有明確顯示已登入，先完成公開流程，再詢問是否要在同一內建瀏覽器分頁由使用者手動登入；不要代填密碼。登入不等於允許收藏、分享、付款、登出或修改帳號。

## Drift maintenance

- 操作前比較目前可見的路由、標籤、表單、權限與 FRED Help／API 文件。
- 若穩定的頁型或控制項改變，先用目前 UI 完成安全任務，再更新負責的 AGENTS、skill 或 reference；保持公開與登入變體分開。
- 記錄頁面類型、舊／新行為、驗證方式與日期；不要記錄密碼、cookies、tokens、私人資料或一次性的數值。
- 修改後重新執行受影響的安全流程與 `quick_validate.py`；廣泛或矛盾的變更標為 maintenance gap，不要猜測。

## References

- [references/site-map.md](references/site-map.md)：已確認的頁型、路由、入口與探索證據。
- [references/data-model.md](references/data-model.md)：series、observation、release、source、category 與 graph 的關係。
- [references/first-party-guidance.md](references/first-party-guidance.md)：FRED Help、API 文件、引用與資料解釋的第一方入口。
- [skills/fred-series-data/SKILL.md](../../skills/fred-series-data/SKILL.md)：搜尋、系列頁、資料表、圖表與下載流程。
- [skills/fred-release-calendar/SKILL.md](../../skills/fred-release-calendar/SKILL.md)：release 清單與日曆流程。
