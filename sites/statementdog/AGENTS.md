# 財報狗（Statement Dog）網站操作指引

## Scope

這份指引只適用於透過 Codex 內建瀏覽器操作 `https://statementdog.com/`。它整理財報狗的穩定導覽、個股與產業資料、選股流程、新聞內容，以及登入後追蹤功能。價格、排名、指標、新聞、可用方案與帳號資料都必須在任務當下重新取得。

## Global routing

- 想查看單一公司、財務指標、亮點／風險、健診或歷史圖表 → `$statementdog-stock-analysis`。
- 想依條件找股票、查看績優／轉機清單、指標排行榜或比較公司 → `$statementdog-screening`。
- 想查看大盤、產業、題材、新聞、網誌或產業報告 → `$statementdog-market`。
- 想查看登入後的追蹤動態、追蹤股組合或帳號區域 → `$statementdog-watchlist`。

## Navigation

- 首頁：`https://statementdog.com/`；提供全站搜尋、個股／題材／新聞分類建議與主要功能入口。
- 個股：`/analysis` 會導向目前預設的公司頁；已知代號時使用 `/analysis/<ticker>`。個股頁再分為最新動態、股票健診、財務報表、獲利能力、安全性分析、成長力分析、價值評估、董監與籌碼、關鍵指標、產品組合。
- 選股：`/screeners`、`/screeners/custom`、`/screeners/quality`、`/screeners/turnaround`，以及月營收、殖利率、本益比、毛利率排行榜。
- 市場與產業：`/taiex`、`/taiex/<slug>`、`/market-trend`、`/industry_reports`、`/industry_reports/<id>`。
- 題材與新聞：`/tags/<id>`、`/news`、`/news/latest`、`/news/trending`；新聞與題材頁會互相連到公司、標籤與文章。
- 網誌與比較：`/blog/`、`/compare/tpe`。
- 登入後追蹤：`/feeds`、`/portfolios`；帳號選單提供 `/users/account`、`/users/account/payment`、`/users/account/password` 與登出入口。

## Sitemap-assisted inventory

- 首頁頁尾未觀察到可用的 sitemap 連結。
- `https://statementdog.com/robots.txt` 已在目前使用者可見的內建瀏覽器分頁中讀取成功，內容列出 `/contact`、`/users/*`、`/insight/benefit`、`/insight/contribute` 的 Disallow 規則，以及兩個 Sitemap：`/sitemap.xml.gz` 與 `/news/sitemap`。
- `https://statementdog.com/news/sitemap` 已在內建瀏覽器中以視覺方式確認，能顯示 XML news sitemap 與新聞 URL／標題欄位。
- `https://statementdog.com/sitemap.xml.gz` 在內建瀏覽器中成功下載為 `.xml.gz`，再由下載檔解壓讀取 XML；已確認根節點為 Sitemap `urlset` 並抽樣路由。不要把目前完整 URL 清單或筆數寫入 skills。
- 本輪從首頁直接重試 `/robots.txt` 與 `/news/sitemap` 時，內建瀏覽器回報 `ERR_BLOCKED_BY_CLIENT`，而目前分頁視覺仍停留在首頁；這只代表本輪瀏覽器控制路徑未取得內容，不代表資源不存在或沒有可解析內容。保留前述已取得的視覺與下載證據，並將本輪重試另記為 `client-blocked`。
- 本次仍以首頁 navbar、footer、頁面內連結與代表頁型建立已驗證路由。未把目前 URL 清單、排名或動態資料寫入 skills。

本輪登入變體重新檢查首頁、共用搜尋（`全部`／`個股`／`題材`／`新聞`）、個股頁、自訂選股頁、大盤頁、新聞頁、網誌頁、比較頁，以及登入後的 `/feeds`、`/portfolios`、`/users/account`。網誌搜尋以安全關鍵字測試後，確認會導向 `/blog/search/<encoded-term>` 結果頁；不保存當次搜尋結果數量或文章清單。

Sitemap 抽樣路由已回到內建瀏覽器驗證：`/taiex` → 大盤頁、`/screeners/custom` → 自訂選股頁、`/analysis` → `/analysis/2330` 個股頁；驗證依據為目前 URL、頁面標題與主要 heading，不保存當下數值。

## Operating rules

- 只使用 Codex 內建瀏覽器；不要改用 Chrome、外部瀏覽器、API、爬蟲、CLI、cookies、local storage 或 session 檔案。
- 先以目前可見頁面為準，操作後至少驗證 heading、目前控制項、URL／query state、結果內容或頁面狀態中的兩項。
- 首頁搜尋欄為全站搜尋，輸入關鍵字後可切換「全部／個股／題材／新聞」；等待建議並選擇具體結果，不要把單純輸入文字當成已完成導覽。
- 個股、產業、題材、選股結果、價格、估值、報酬率、新聞與方案都是動態資料；回覆時記錄查詢條件與觀察時間，必要時重新整理。
- 網站免責聲明指出，資料如有歧異以交易所、公司或官方公布資料為準；網站分析只作投資決策輔助，不保證獲利或減少損失。
- 預設只做讀取與可逆的安全互動。不要在探索時訂閱、付款、儲存選股條件、修改帳號、上傳頭像、改密碼、登出、刪除追蹤股或送出評論。

## Authentication

- 每次先從可見畫面確認 session。若帳號選單顯示頭像以及「帳號設定／用量與付款／重設密碼／登出」，或 `/feeds` 顯示個人追蹤股票清單，即可視為目前分頁已登入；帳號設定頁內部分頁目前顯示「修改密碼」。
- 若目前分頁已明確登入，不需要另外詢問是否探索登入後功能；直接把登入狀態當成另一個網站變體，重新核對首頁、navbar、主要頁型、搜尋欄、篩選器、下拉選單與表單，再探索安全的登入後分支。
- 若無法確認已登入，先完成可用的公開功能；只有在公開探索與第二輪核對完成後，才詢問使用者是否要探索受保護功能。若使用者同意，請使用者在同一個內建瀏覽器分頁手動登入，不代填密碼。
- 使用者若明確要求只看公開功能，優先遵守。登入本身不代表可執行付款、刪除、登出、改密碼、修改方案或其他不可逆動作。
- 登入後不要記錄 email、頭像 URL、方案付款資料、私人通知、追蹤清單內容或其他個人資料。

## Drift maintenance

- 未來操作前先比較目前內建瀏覽器中的頁面、路由、標籤、控制項、權限、方案限制與網站說明。
- 若穩定的操作方式改變，先用目前 UI 完成安全任務，再把清楚且已驗證的差異更新回負責的 AGENTS、skill 或 reference；保持公開與登入狀態分開。
- 更新時記錄頁面類型、狀態、舊行為、目前行為、驗證方式與日期；不要寫入密碼、cookies、tokens、私人資料或動態結果值。
- 若只是目前價格、排名、數量、報酬率、新聞或帳號值變動，更新重新取得資料的路徑，不要把數值寫死。
- 修改後重新執行受影響的安全流程與 `quick_validate.py`；遇到廣泛、矛盾或無法安全驗證的變更，標記 maintenance gap，不要猜測。

## References

- [site-map.md](references/site-map.md)：已驗證的導覽、路由、頁面類型、登入邊界與探索缺口。
- [data-model.md](references/data-model.md)：公司、指標、產業、題材、選股策略、文章與追蹤清單的關係。
- [form-controls.md](references/form-controls.md)：全站搜尋、年份區間、選股條件、排行榜、題材分類與追蹤控制項。
- [first-party-guidance.md](references/first-party-guidance.md)：免責聲明、資料來源、選股方法與網站自己的定義。
