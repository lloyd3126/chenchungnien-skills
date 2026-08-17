# Reuters Agent 可用性測試

這些是未來維護時可用的唯讀 forward-test 情境。每次測試都要重新取得 live data，並以目前 UI 驗證結果。

## Scenario 1 — 搜尋與篩選

Request shape：`找 Reuters 最近一週與 AI 相關的 Technology 文章，依最新排序。`

Expected route：`$reuters-news-search` → `Open search bar` → `Search Reuters` 輸入 query → `Search` → Section `Technology` → Date range `Past week` → Sort `Newest`。

Pass criteria：Agent 能指出 `/site-search/`、核對三個 selected controls、結果 heading／time／category，並說明結果數量是動態值。

## Scenario 2 — 市場區域與表格

Request shape：`看 Reuters Markets 的 Europe 分頁，讀出目前可見的指數與 delay context。`

Expected route：`$reuters-market-data` → `/markets/` → `Europe` tab → index cards／Stocks table。

Pass criteria：Agent 能核對 `Europe [selected]`、instrument label、Last／Change、LSEG source 與至少 15 分鐘 delay；不宣稱即時或投資建議。

## Scenario 3 — 文章詳情

Request shape：`讀這篇 Reuters 文章，整理作者、時間、Summary、正文的可見限制與來源提示。`

Expected route：`$reuters-article-research` → article URL → title／authors／time → Summary → body → media／tags／Our Standards。

Pass criteria：Agent 能區分可見正文與 gate、標記 `Exclusive`／`ANALYSIS`／Sponsored 等 content label，且不點 Save／Share／Email。

## Scenario 4 — Sitemap 找候選

Request shape：`從 Reuters 的 first-party sitemap 找某月份文章入口。`

Expected route：footer `Article Sitemap` → `/sitemap/` → year/month → day/partition → 回到 UI 開啟代表 article。

Pass criteria：Agent 將 Sitemap 記為 inventory candidate，核對 article title／time／route，不把 sitemap 列表當成完整內容或權限證明；robots client block 要單獨回報。
