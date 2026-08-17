# Koyfin

## Scope

這份指引適用於 `https://app.koyfin.com/` 的唯讀金融研究、市場監控、搜尋與個人工作區導覽。Koyfin 會依目前登入狀態、方案、資料載入狀態與個人工作區呈現不同內容；本輪目前分頁已明確顯示登入中的 trial banner，因此把公開／登入後頁面視為同一站點的不同變體。

使用：

- [`$koyfin-security-research`](../../skills/koyfin-security-research/SKILL.md)：解析單一股票、ETF 或其他證券，串接 Snapshot、估計、財務、新聞／申報與圖表。
- [`$koyfin-market-monitoring`](../../skills/koyfin-market-monitoring/SKILL.md)：市場新聞、Market Movers、指數、散點圖、Lots of Charts 與日曆。
- [`$koyfin-watchlists-and-screens`](../../skills/koyfin-watchlists-and-screens/SKILL.md)：唯讀檢查 watchlist、screen、portfolio 與 dashboard。
- [`$koyfin-advanced-search`](../../skills/koyfin-advanced-search/SKILL.md)：Security Search 與 Transcripts Search 的條件搜尋、消歧與清除。

## Sitemap-assisted inventory

- 本輪沒有在可見導覽中找到 Site Map 入口。
- 同源 `/robots.txt` 已在目前內建瀏覽器分頁嘗試並完成視覺檢查；頁面呈現 Koyfin SPA 的「How did you get here? / It seems you landed in the wrong place.」錯誤頁，而非 `User-agent`、`Allow`、`Disallow` 或 `Sitemap` 文字。記為「已取得 HTML 但不是 robots metadata」，不據此推論站點沒有 Sitemap。
- 同源 `/sitemap.xml` 已在同一分頁嘗試並重試；控制路徑在截圖時逾時／回報 target closed，未取得可驗證的 XML。記為 `client-blocked`，不是 `no sitemap discovered`。
- 持久文件只保存由 UI 驗證的穩定路由模式；不保存本輪的價格、排名、結果數、新聞清單、登入資料、tokenized security ID 或個人工作區值。

詳見 [`references/coverage.md`](references/coverage.md) 的路由覆蓋、證據來源與缺口。

## Global routing

- 單一證券的公司概覽、估值、財務、估計、新聞、申報或圖表 → `$koyfin-security-research` → 先用全站搜尋或 Advanced Search 解決確切證券，再進入 Security Analysis。
- 市場新聞、漲跌幅／成交量、區域指數、散點圖、圖表網格或財經日曆 → `$koyfin-market-monitoring` → 使用 Market Overview、Research Tools 或 Calendars 的可見入口。
- 讀取 watchlist、screen、portfolio 或 dashboard → `$koyfin-watchlists-and-screens` → 使用 My Koyfin；先確認目前工作區與權限。
- 精確 ticker／交易所消歧或逐字稿條件搜尋 → `$koyfin-advanced-search` → `Advanced Search` 的 `Security Search` 或 `Transcripts Search`。

## Navigation

- `Market News` `/news/top`：Top News、Global Markets 與其他新聞分類入口。
- `Market Movers` `/mov`：市場時段、universe、Sector Filter、漲跌幅／相對成交量與 Gainers／Losers。
- `Security Analysis`：先選目前證券，再展開 `Snapshots`、`Analyst Estimates`、`Financial Analysis`、`News, Filings & Transcripts` 或 `Graphs`；父節點收合時，先展開才能可靠點擊子頁。
- `My Watchlists` `/myw/<watchlist-id>`、`My Portfolio` `/myp/pl`、`My Screens` `/mys/<screen-id>`、`My Graphs` `/myg`、`My Dashboards` `/myd/<dashboard-id>`：個人化工作區。ID 必須由目前 UI 解析，不能猜測或硬編碼。
- `Market Dashboards`：可見子項包含 `World Equity Indices` `/wei`、`US Sectors`、`Countries`、`Recent IPOs`、`World Economics`、`Global Yields`、`Currencies`、`Commodities`、`Corporate Credit`、`Yield Spreads`、`Yield Curve`、`Factor Analysis` 與 `Fixed Income Factors`；使用目前 sidebar label 導航。
- `Calendars`：`Earnings Calendar` `/earc` 與 `Economic Calendar` `/ecal`。
- `Research Tools`：`Lots of Charts` `/lot`、`Market Scatter` `/ms`、`Advanced Search` `/search`，再選 `Security Search` `/search/security` 或 `Transcripts Search` `/search/transcripts`。
- 頂部全站搜尋的可見 label 為 `Search for a name, ticker, or function`；搜尋 modal 可依 All、Equities、ETFs、Indices、Forex、Crypto、Futures、Economic 等類別縮小範圍。

## Operating rules

1. 只使用 Codex 內建瀏覽器與使用者目前可見的同一分頁；保留 session，不使用外部瀏覽器、API、CLI、web search、cookies、local storage 或 session 檔案。
2. 每次任務先以目前 UI 為準，核對 URL、主要 heading／title、selected control 與實際結果；URL 改變本身不是互動成功的證明。
3. 導航後等待 `Your data is loading...` 消失再讀取表格或圖表。價格、估計、財務、新聞、結果數、日期、pagination、current quote 與個人工作區內容都必須在任務當下重新取得。
4. 目前登入後工作區可能包含敏感個人資料。可安全檢查頁面、搜尋、篩選、分頁、切換 tab、展開面板與清除暫時條件；不要把當前 holdings、watchlist entries、dashboard data、alerts 或 notes 寫入長期文件。
5. `Save`, `Save and Apply`, `Create`, `Edit`, `Delete`, `Duplicate`, `Share`, `Import`, `Add to My Watchlists`, `My Alerts`, `My Notes`, `Download`／`Export` 與投資組合編輯都視為副作用或資料外流邊界。除非使用者明確要求，停在按鈕前。
6. Ticker 可能對應多個交易所、國家、證券類別或 ETF。先透過搜尋結果的 Country、Exchange、Asset Category 與 Security Name 選取確切 entity；不要猜 `eq-*` 或 UUID。
7. 將動態數值、新聞結果與當前篩選條件視為暫時證據；長期 guidance 只保留取回路徑、欄位語義、freshness 與驗證方法。
8. UI 若與本文件不同，使用目前可見 label 安全完成任務，記錄 route、登入變體、舊／新行為與證據來源；只有穩定且可再次驗證的差異才更新文件。

## Data and freshness

主要 entity 是 `Security`、`Market Item`、`News/Filings/Transcript Event`、`Calendar Event` 與個人工作區中的 `Watchlist`、`Screen`、`Portfolio`、`Graph`、`Dashboard`。同一 Security 可從 snapshot、estimates、financial analysis、news、filings、transcripts 與 charts 互相串接；但各頁面可能使用不同時間區間、幣別、頻率與資料延遲。

每次回答應保存查詢時刻、UI 顯示的日期／period、幣別／timezone、universe／filters 與 selected security，並在結果頁重新核對 heading、entity identity、selected controls 及至少一個實際欄位。不要以文件中的範例值代替重新整理。

## Known limits

- 沒有取得可驗證的同源 Sitemap；`/robots.txt` 呈現 SPA 錯誤 HTML，`/sitemap.xml` 在同一分頁重試後仍為 browser-control `client-blocked`。
- 本輪已以唯讀方式探索登入後的 My Watchlists、My Portfolio、My Screens 與 Sample Dashboard；沒有編輯、儲存、分享、刪除、匯入、下載或變更帳號／投資組合。
- `My Graphs` 首次視覺顯示 `Something went wrong / Please try again later`；同分頁重試後 DOM 顯示 `Create your first graph`，但後續 screenshot control 逾時，因此只記為 partial／不確定，不把它當成完整 UI 驗證。
- `Client Portfolios`、`Model Portfolios`、`Reports`，以及部分 Market Overview 子頁、Press Releases／Transcripts 個別頁面未逐一開啟；sidebar 中可見的 route 只代表可導航候選，不代表本輪已驗證其內容與權限。
- 本輪未深入打開 Help Center、methodology、資料來源或計算定義頁；若任務涉及指標定義，應優先尋找當前頁面的第一方 tooltip／help 文字再回答。

## References

- [`references/coverage.md`](references/coverage.md)：探索證據、頁型、已測安全互動與未驗證分支。
- [`../../skills/koyfin-security-research/references/navigation.md`](../../skills/koyfin-security-research/references/navigation.md)：證券消歧與 Security Analysis 路由。
- [`../../skills/koyfin-security-research/references/freshness-and-entities.md`](../../skills/koyfin-security-research/references/freshness-and-entities.md)：entity、欄位、資料新鮮度與敏感值規則。
- [`../../skills/koyfin-market-monitoring/references/market-tools.md`](../../skills/koyfin-market-monitoring/references/market-tools.md)：市場工具路由與 safe controls。
- [`../../skills/koyfin-watchlists-and-screens/references/workspace-controls.md`](../../skills/koyfin-watchlists-and-screens/references/workspace-controls.md)：個人工作區的控制項與副作用邊界。
- [`../../skills/koyfin-advanced-search/references/search-controls.md`](../../skills/koyfin-advanced-search/references/search-controls.md)：Security／Transcripts Search 的欄位與消歧。
