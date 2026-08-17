# Seeking Alpha Site Map and Coverage

## Evidence baseline

這份路由表來自目前 Codex 內建瀏覽器分頁的視覺擷取與 DOM／互動讀取；它描述穩定頁型與路由模式，不保存本輪動態文章、價格、排名或個人資料。已抽樣的頁面 title 與主要 heading 均在同一瀏覽器工作階段驗證。

| Page type | Representative route | Purpose | Key sections or controls | Status |
| --- | --- | --- | --- | --- |
| Home | `/` | 全站入口與市場快照 | Global search, AM Need To Know, indices, trending analysis/news, education/video/podcast links | explored |
| Analysis list | `/latest-articles` | 分析文章流 | `ALL ANALYSIS ARTICLES`, `Show summaries`, article cards, author/symbol links, Save/Share | explored |
| Market news list | `/market-news` | 即時／近期市場新聞 | topic links, news cards, linked symbols, `Show full stories`, Copy Link, pagination | explored |
| Symbol hub | `/symbol/<ticker>` | 單一股票／ETF 的研究入口 | Summary, Ratings, Financials, Earnings, Dividends, Valuation, Growth, Profitability, Momentum, Peers, Options, Charting | explored with AAPL |
| Symbol content | `/symbol/<ticker>/news`, `/analysis`, `/comments`, `/earnings/transcripts`, `/sec-filings`, `/press-releases`, `/related-analysis` | 標的的文章、新聞與公司文件 | content tabs and related links | route pattern UI-verified from symbol hub |
| Article detail | `/article/<id>-<slug>` | 分析文章詳情 | title, summary, author, analyst disclosure, SA disclosure, comments, related stock chart, register gate | explored |
| News detail | `/news/<id>-<slug>` | 單則新聞詳情 | headline, timestamp/source fields, related symbols and news links | linked from news list; re-open and verify at task time |
| Earnings calendar | `/earnings/earnings-calendar` | 財報事件與估計 | date-range button, date buttons, Search/Settings modals, EPS/Revenue/Analysts Revisions & Ratings tabs, table | explored |
| Screeners overview | `/screeners` | 預設與自訂選股入口 | preset cards, result summaries, copy screen link, unlock CTA | explored; custom fields partial/protected |
| Preset screen | `/screeners/<screen-id>-<slug>` | 一組已命名篩選條件與結果 | filter/result table varies by screen | route link observed; re-verify at task time |
| Market data | `/etfs-and-funds/etf-tables/<table>` | 指數、貨幣、加密貨幣、股息與 ETF 表格 | table, period/sort controls vary | navigation route observed; page fields partial |
| Comparison | `/comparison` and `/comparison/<id>-<slug>` | 比較多個股票／ETF | comparison chart/table and symbol selection | route observed in navigation; not fully explored |
| Portfolio / account | `/account/portfolio`, `/account/portfolio/all/holdings` | 個人化持倉與追蹤 | account-dependent controls | protected—not explored |

## Navigation inventory

首頁與分析／個股頁的側欄還提供 Stock Ideas、Market Outlook、Investing Strategy、Long Ideas、IPO Analysis、Editor's Picks、Cryptocurrency、Sectors、Dividends、ETFs、Education、Podcasts、Videos、Investing Groups、Portfolios、Find & Compare 與 Subscriptions。這些是路由家族；內容、權限與可見欄位要以當下頁面重新核對。

## Sitemap and robots status

| Resource | Discovery / retrieval status | Evidence | Interpretation |
| --- | --- | --- | --- |
| Visible Sitemap link | no sitemap discovered in inspected UI | current-tab visual + DOM/interaction | 未見可用的人類導覽 Sitemap 入口 |
| `/robots.txt` | client-blocked | automation/control error: `ERR_BLOCKED_BY_CLIENT` | 不代表資源不存在、空白或沒有 Sitemap；不可視為功能地圖或使用者權限 |
| conventional sitemap candidates | not followed after robots client block | exploration boundary | 不用 CLI、API、外部瀏覽器或猜測式 exhaustive crawl 補洞 |

## Verification and freshness

每次從路由進入頁面後，確認 URL、title／heading、選中 tab 或主要結果中的至少兩項。任何價格、估計、評等、文章、新聞、結果數、日期與可用方案都屬動態值，只能從任務當下頁面讀取。

## Coverage gaps

- 未登入分支的 Portfolio、Subscriptions、Investing Groups 詳情、Follow／Save／Comment 實際提交結果未測試。
- Screener 自訂條件的完整欄位、排序、reset、儲存與比較頁的完整操作未驗證。
- 沒有把 robots Disallow 或可能的 Sitemap URL 當成 UI 已驗證路由。
