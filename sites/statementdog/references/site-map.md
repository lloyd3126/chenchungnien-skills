# 財報狗網站地圖與覆蓋紀錄

## Sitemap status

| 項目 | 結果 | 狀態 |
| --- | --- | --- |
| 首頁可見 sitemap 連結 | 未觀察到 | 不可用 |
| `https://statementdog.com/robots.txt` | 先前已在使用者可見分頁讀取；本輪首頁直接重試回報 `ERR_BLOCKED_BY_CLIENT`，視覺仍停在首頁 | visually accessible; current retry `client-blocked` |
| `https://statementdog.com/sitemap.xml.gz` | 由 robots.txt 發現；先前內建瀏覽器下載 `.xml.gz` 後已解壓讀取 XML `urlset` 並抽樣路由 | downloaded; locally parsed; current inventory not persisted |
| `https://statementdog.com/news/sitemap` | 先前已在內建瀏覽器視覺確認 XML news sitemap、新聞 URL 與欄位；本輪直接重試回報 `ERR_BLOCKED_BY_CLIENT` | visually accessible; current retry `client-blocked` |
| UI 導覽與頁面連結 | 已取代 sitemap 作為主要 inventory | explored |

## Top-level coverage

| 區域 | 入口／代表路由 | 已確認內容 | 狀態 |
| --- | --- | --- | --- |
| 首頁 | `/` | 全站搜尋、個股／題材／新聞建議、功能導流、footer | explored |
| 個股 | `/analysis/<ticker>` | 公司摘要、題材、亮點／風險、重要數據、新聞、公司與產業說明 | explored |
| 個股子頁 | `/analysis/<ticker>/<section>` | 10 個分析區域；部分頁含年份區間與表格 | explored representative routes |
| 選股 | `/screeners` | 自訂、績優、轉機、四種指標排行榜 | explored |
| 自訂選股 | `/screeners/custom` | 多分類條件、操作符、數值、清單與儲存入口 | explored; no save |
| 排行榜 | `/screeners/*_ranking` | 目前期別、排序、分頁、公司分析連結 | explored representative route |
| 大盤與產業 | `/taiex`、`/taiex/<slug>` | 大盤指數說明、P/B 解讀、產業卡片、上下游分頁與公司列表 | explored |
| 市場焦點 | `/market-trend` | 市場範圍、期間篩選、概念／族群表現視覺化 | explored |
| 題材 | `/tags/<id>` | 受惠分類、公司卡片、受惠原因、新聞、相關標籤 | explored |
| 新聞 | `/news`、`/news/latest`、`/news/trending` | 文章、日期、標籤與分類 | explored representative routes |
| 網誌 | `/blog/` | 分類、文章列表、文章搜尋欄、分頁 | explored; search submit effect unconfirmed |
| 產業報告 | `/industry_reports`、`/industry_reports/<id>` | 報告列表、章節、供應鏈地圖、公司連結 | explored |
| 比較 | `/compare/tpe` | 多公司輸入、年度區間、比較類別；部分內容受方案／次數限制 | partial |
| 追蹤 | `/feeds`、`/portfolios` | 追蹤動態、股票清單、組合、加股／改名入口 | authenticated explored; no mutation |
| 帳號 | `/users/account` | 頭像、顯示名稱、email、方案、電子報 checkbox | authenticated read-only |

## Navigation inventory

- `個股` → `/analysis`
- `選股` → `/screeners`、`/screeners/custom`、`/screeners/quality`、`/screeners/turnaround`、`/screeners/revenues_ranking`、`/screeners/dividend_yield_ranking`、`/screeners/pe_ranking`、`/screeners/gross_margin_ranking`
- `產業` → `/industry_reports`、`/news`，以及多個焦點 `/tags/<id>`
- `市場` → `/taiex`、`/market-trend`
- `購買` → `/pricing`
- `更多` → `/compare/tpe`、`/blog`、外部 CakeResume 徵才頁
- `我的追蹤` → `/feeds`
- 齒輪會員選單 → `/users/account`、`/users/account/payment`、`/users/account/password`、登出；本輪首頁選單標籤為「帳號設定／用量與付款／重設密碼／登出」，帳號頁內部分頁為「修改密碼」
- footer → 個股、選股、大盤產業、比較、美股列表、網誌、購買、客服、法律與資料來源

## Robots-derived candidates

`robots.txt` currently exposes these stable paths:

- `https://statementdog.com/sitemap.xml.gz` — compressed general sitemap; download through the in-app browser, then decompress and sample XML routes. The current URL inventory is dynamic and is not stored here.
- `https://statementdog.com/news/sitemap` — visually confirmed XML news sitemap.

Use the visible robots file as the refresh path. Treat downloaded sitemap URLs as discovery candidates until the corresponding UI or page is opened successfully.

## Current browser revalidation

| Resource | Current attempt | Visual evidence | Interpretation |
| --- | --- | --- | --- |
| `/robots.txt` | In-app browser navigation returned `ERR_BLOCKED_BY_CLIENT` | Tab remained on the Statement Dog homepage | `client-blocked` control path; not evidence of an empty or missing robots file |
| `/news/sitemap` | In-app browser navigation returned `ERR_BLOCKED_BY_CLIENT` | Tab remained on the Statement Dog homepage | `client-blocked` control path; retain prior visual XML evidence |

When this happens in a future run, visually inspect the current tab and retry through an exact visible first-party link or normal browser navigation. Do not downgrade a previously retrieved artifact or report “沒有可解析內容” solely from the automation error.

## Sitemap route validation

The downloaded general sitemap was sampled rather than exhaustively crawled. These representative routes were reopened in the Codex in-app browser:

| Sitemap route | Observed browser result | Verification |
| --- | --- | --- |
| `/taiex` | TAIEX and industry performance page | URL, title, and `台股大盤與類股表現` heading |
| `/screeners/custom` | Custom screening form | URL, title, and screening-category headings |
| `/analysis` | Redirected to `/analysis/2330` | Final URL, title, and company-section headings |

Current prices, counts, dates, and the complete sitemap inventory remain dynamic and are intentionally omitted.

## Page taxonomy

| 類型 | 代表路由 | 穩定結構 |
| --- | --- | --- |
| 公司總覽 | `/analysis/<ticker>` | ticker/name/market、價格與日期、籌碼、題材、亮點／風險、指標摘要、新聞、公司／產業說明 |
| 公司指標 | `/analysis/<ticker>/monthly-revenue` 等 | 圖表或 table、可能有年份區間、指標說明、同一組個股 section 導覽 |
| 健診 | `/analysis/<ticker>/stock-health-check` | 排除地雷、定存、成長、便宜、籌碼、績優、轉機等健診卡片與深入說明 |
| 選股策略 | `/screeners/quality`、`/screeners/turnaround` | 策略說明、今日清單、公司卡片、歷史績效／原理說明 |
| 自訂表單 | `/screeners/custom` | 分類條件、操作符、數值選單、我的清單、開始／清空／儲存入口 |
| 排行榜 | `/screeners/revenues_ranking` 等 | 當期標題、欄位排序、公司分析連結、分頁／載入更多 |
| 大盤／產業 | `/taiex`、`/taiex/<slug>` | 指數或產業表現、圖表、定義、產業鏈與公司列表 |
| 市場／題材 | `/market-trend`、`/tags/<id>` | 範圍／期間控制、概念表現或受惠分類、新聞與標籤 |
| 內容 | `/news/*`、`/blog/*`、`/industry_reports/*` | 標題、日期、分類／標籤、文章本文、相關公司與外部連結 |
| 追蹤／帳號 | `/feeds`、`/portfolios`、`/users/account` | 個人清單、通知、表單與帳號設定；需要登入且含私人資料 |

## Authentication boundary

本次探索開始時，首頁 shared header 顯示可進入「我的追蹤」，同一 session 的 `/feeds` 顯示個人追蹤股票清單，齒輪選單也顯示頭像與「帳號設定／用量與付款／重設密碼／登出」，因此以登入狀態探索。`/users/account` 內部分頁顯示「修改密碼」。沒有為了建立未登入對照而登出。

- 已探索的登入後只讀分支：`/feeds`、`/portfolios`、`/users/account`。
- 已看到但未深入或未執行的帳號分支：付款／方案變更、密碼重設、登出、頭像上傳、儲存帳號變更、通知內容。
- 未確認：未登入時的完整 header 差異、登入後與未登入的每一個公開頁面差異、方案升級後解鎖內容。

## Second-pass audit

- [x] 首頁 navbar、footer、主要 CTA 與 shared search 重新檢查
- [x] 選股、產業、市場、更多 dropdown 重新檢查
- [x] 個股主要 section 與代表性子頁重新檢查
- [x] 搜尋分類、年份區間、排行榜期間／排序、市場焦點期間重新測試
- [x] 題材、產業、新聞、網誌、產業報告代表頁重新檢查
- [x] 登入後追蹤與帳號入口檢查
- [x] 登入變體重新檢查首頁搜尋分類、個股、自訂選股、大盤、新聞、網誌與比較頁
- [x] 網誌搜尋表單安全測試；結果頁導向已確認，動態結果數量未保存
- [x] robots.txt：已在使用者可見分頁讀取並取得 Sitemap 指向
- [x] news sitemap：已在內建瀏覽器視覺確認 XML 結構
- [x] general sitemap XML：已透過瀏覽器下載、解壓並抽樣確認 XML 結構
- [x] 本輪 robots/news Sitemap 直接重試的 `client-blocked` 已與歷史成功證據分開記錄
- [ ] 比較頁完整資料：目前畫面顯示方案／查詢次數限制
- [ ] 付款、密碼、登出、刪除與儲存等不可逆或帳號變更流程：刻意未執行
