# Seeking Alpha 網站操作指引

## Scope

這份指引適用於透過 Codex 內建瀏覽器操作 `https://seekingalpha.com/`。Seeking Alpha 是金融研究與投資資料平台，涵蓋個股、新聞、分析文章、量化評等、財報日曆、選股器、ETF、股息、產業與市場資料。本輪以未登入的公開頁面為基線；價格、評等、文章、結果列、日期與帳號內容都必須在任務當下重新取得。

## Sitemap-assisted inventory

- 本輪從首頁側欄、頂部導覽、頁面結構與已見頁尾連結未取得可用的 Sitemap／Site map 入口。
- 同源 `https://seekingalpha.com/robots.txt` 曾在目前的內建瀏覽器分頁中嘗試開啟；瀏覽器控制路徑回報 `ERR_BLOCKED_BY_CLIENT`，未取得內容。這只記為 `client-blocked` 的探索證據，不代表 robots 或 Sitemap 不存在，也不把它當成權限判定。
- 已由目前分頁的視覺與 DOM／互動驗證代表路由：`/`、`/latest-articles`、`/market-news`、`/symbol/AAPL`、`/earnings/earnings-calendar`、`/screeners`、`/basic-search`、`/article/<id>-<slug>`。持久文件只保存路由模式，不保存本輪文章清單、價格、排名或結果數量。
- 未追蹤 tokenized `#source` 參數、完整 sitemap 清單、robots 的 Disallow 路徑、私人帳號路由或付費後內容。

## Global routing

- 想查單一股票／ETF 的目前報價、評等、財務、股息、估值、同業或公司頁面 → `$seeking-alpha-stock-analysis`。
- 想讀市場新聞、分析文章、產業／股息／ETF 類別、財報日曆或市場資料 → `$seeking-alpha-market-research`。
- 想依條件尋找、排序、篩選或比較股票／ETF → `$seeking-alpha-screening`。
- 需要路由、頁型、欄位關係、控制項或第一方免責聲明 → 先讀取 `references/site-map.md`、`data-model.md`、`form-controls.md` 或 `first-party-guidance.md`。

## Navigation

- `Home` `/`：首頁、全站搜尋、AM Need To Know、指數／商品快照、Trending Analysis／News，以及教育、影音與比較入口。
- `Stock Analysis` `/latest-articles`：分析文章列表；文章卡片可通往文章、作者、標的與評論，並有 `Show summaries`、`Save`、`Share` 等控制。
- `Market News` `/market-news`：Breaking Stock Market News；可由主題分類、新聞卡、關聯 symbol 與頁碼進入新聞詳情。
- `Market Data`：主要入口為 `/etfs-and-funds/etf-tables/key_markets`，另有 currencies、cryptocurrency、dividends 與其他 ETF 表格。
- `Earnings` `/earnings/earnings-calendar`：依日期區間和單日查看財報，並切換 `EPS`、`Revenue`、`Analysts Revisions & Ratings`。
- `Find & Compare` `/screeners`：預設股票篩選器入口；主導覽也提供 `All Stocks`、`Top Rated Stocks`、`Top Growth Stocks`、`Top Value Stocks`、`ETF Screener` 與 `Comparisons` 等候選入口。
- `Search for Symbols, analysts, keywords` `/basic-search`：全站搜尋入口；首頁搜尋欄的 placeholder 為 `Symbols, Analysts, Keywords`。
- `Portfolio` `/account/portfolio`、`Premium` `/subscriptions/premium`、`Investing Groups` `/marketplace/directory`：登入／方案／個人化分支，執行任務前要重新確認權限與安全邊界。

## Operating rules

- 只使用 Codex 內建瀏覽器與目前可見的同站分頁；不要改用外部瀏覽器、API、CLI、爬蟲、cookies、local storage 或 session 檔案。
- 導覽後至少核對目前 URL、頁面 title／主要 heading、選中控制項或結果內容中的兩項。URL 改變本身不是互動成功的證明。
- 搜尋、評等、估值、價格、財務、財報預期、新聞、排名、頁碼與可見性都是動態資料；記錄觀察時間與查詢條件，必要時重新整理。
- 文章與部分資料可能在 `Register for free to keep reading` 或 Premium gate 後停止；不要繞過註冊、付費牆、CAPTCHA、query cap 或其他安全攔截。
- `Save`、`Share`、`Follow`、`Like`、留言、建立投資組合、儲存篩選器、訂閱、購買、登入、改帳號設定與登出都屬於副作用邊界；讀取任務只做到最後確認前。
- 目前公開基線顯示 `Create Free Account` 與 `Login / Register`；未把登入後的個人化資料當成公開能力。若未來目前分頁明確已登入，將登入狀態視為另一個變體，先重查公開頁型再安全探索受保護分支。

## Drift maintenance

- 每次任務前比對目前可見的頁面、路由、label、控制項、權限與第一方說明；目前 UI 優先於本文件。
- 若穩定路由、頁型、欄位或流程改變，記錄公開／登入狀態、頁型、舊行為、目前行為、驗證方式與日期，更新負責的 skill 或 reference；不要記錄密碼、cookies、tokens、私人資料或動態結果。
- 若只是價格、排名、數量、文章或目前可用性變動，更新重新取得與驗證方法，不要把數值寫死。
- 修改後重新執行受影響的安全流程與 skill validator；廣泛、矛盾或無法安全驗證的差異標記為 maintenance gap，不要猜測。

## Known limits

- 本輪只完成公開頁面探索；Portfolio、Follow／Save 後資料、投資群組內容、訂閱與帳號設定未驗證。
- `/screeners` 的預設卡片與入口已驗證，但自訂條件、儲存篩選器、比較結果與 Premium 解鎖後完整欄位未完成安全測試。
- `robots.txt` 的本輪控制路徑為 `client-blocked`；沒有把這次失敗轉寫成「沒有 Sitemap」。
- 分析文章正文可能只顯示摘要並要求免費註冊；能讀到的作者、披露、評論與右側標的資料要與付費／登入後內容分開。

## References

- [site-map.md](references/site-map.md)：代表路由、頁型、驗證狀態與探索缺口。
- [data-model.md](references/data-model.md)：標的、文章、新聞、篩選器、財報事件與帳號實體關係。
- [form-controls.md](references/form-controls.md)：搜尋、日期、分頁、tab、篩選器與文章控制項的操作與驗證。
- [first-party-guidance.md](references/first-party-guidance.md)：網站與文章披露、資料解讀限制及來源優先順序。
- [agent-usability.md](references/agent-usability.md)：可用來檢查未來 Agent 是否能正確選 skill、驗證結果與安全停點的請求形狀。
