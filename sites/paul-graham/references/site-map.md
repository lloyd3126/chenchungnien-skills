# Paul Graham route map

探索基準：2026-08-17。這是以目前 Codex 內建瀏覽器分頁讀到的穩定路由與頁型摘要，不是完整 URL inventory。

## Evidence legend

- `current-tab visual`：目前使用者分頁的截圖可見。
- `current-tab DOM/interaction`：目前分頁的可見 DOM 或安全互動結果。
- `automation/control error`：控制器回報失敗，只能證明控制嘗試失敗，不能證明目標沒有內容。
- 直接從 sitemap 候選推得的路徑一律視為未驗證；本表只把網站頁面可見互鏈列為 UI route。

## Core routes

| Route | Visible label / title | Page type | Stable behavior | Evidence |
| --- | --- | --- | --- | --- |
| `/` | Paul Graham | Home / hub | 側欄集中列出內容類別，中央有圖片與公告連結 | current-tab visual + current-tab DOM/interaction |
| `/articles.html` | Essays | Essay list | 頁首有三篇推薦文章，後續為長篇 Essay 連結清單；本輪未見站內搜尋框 | current-tab DOM/interaction |
| `/<essay>.html` | 個別 Essay title | Essay detail | 可見 image alt、日期（若有）、導言、正文、內部註腳 anchor 與回首頁／全站導航 | current-tab DOM/interaction |
| `/ind.html` | Paul Graham Index | Alphabetical index | 內容按字母段落列出跨站頁面連結，底部有 `Prev | Next` | current-tab DOM/interaction |
| `/books.html` | Books | Book hub | 三本書卡片：On Lisp、ANSI Common Lisp、Hackers & Painters | current-tab DOM/interaction |
| `/hackpaint.html` | Hackers & Painters | Book detail | 書封、簡介、出版／ISBN 欄位、評論、外部出版商與 Amazon 連結 | current-tab DOM/interaction |
| `/faq.html` | FAQs | FAQ hub | General、Programming、Startup、Arc、Lisp、Viaweb、Plan for Spam、FFB FAQ | current-tab DOM/interaction |
| `/raq.html` | RAQs | Long-form Q&A | Rarely-Asked Questions 長頁；部分問答有同站連結 | current-tab DOM/interaction |
| `/quo.html` | Quotes | Quote list | 以條目列出 Quote 與來源；沒有看到搜尋／篩選控制 | current-tab DOM/interaction |
| `/rss.html` | RSS | Feed explanation | 說明 Aaron Swartz 建立 essays page 的 scraped feed，連到外部 feed | current-tab DOM/interaction |
| `/bio.html` | Bio | Biography | 作者簡介與照片來源說明，含外部與同站連結 | current-tab DOM/interaction |
| `/info.html` | Paul Graham Info | Contact guidance | 寄信前提醒、FAQ 連結與聯絡方式說明；不含可供 Agent 代寄的表單 | current-tab DOM/interaction |

## Project and topic routes

| Route | Page type | Confirmed child links / semantics |
| --- | --- | --- |
| `/arc.html` | Arc project hub | Forum、Tutorial、Get Arc、Arc's Out、Arc Challenge、Core Language、Arc FAQ、Help Us、Design Philosophy、Old Arc Stuff；部分為外部連結 |
| `/bel.html` | Bel project page | 日期文字 `Oct 2019`；Bel language guide、Bel source、examples 為當頁可見資源連結，URL 可能含 CDN 時間／查詢參數 |
| `/lisp.html` | Lisp topic hub | Roots、What Made Lisp Different、A Lisp Startup、Arc、Lisp Code、Lisp Links、Lisp History、Lisp Quotes、Lisp FAQ |
| `/antispam.html` | Spam topic hub | A Plan for Spam、Plan for Spam FAQ、Bayesian、filter、blacklist、research、resources、archives、links；Spam Conference 為外部連結 |
| `/kedrosky.html` | Responses hub | Founders' Accents、What I Didn't Say、Female Founders、以 Mark Zuckerberg 為題的頁面 |

## Sitemap and inventory status

| Target | Status | Evidence and interpretation |
| --- | --- | --- |
| Visible site map link | no sitemap discovered | 首頁可見 `Index`，但它是 HTML 內容索引，不是 sitemap |
| `/robots.txt` | client-blocked | 同分頁兩次導覽後畫面仍為首頁，控制器回報 `ERR_BLOCKED_BY_CLIENT`；未解析任何內容 |
| `/sitemap.xml` | invalid | 目標畫面可見 Yahoo 404 HTML，非 XML |
| `/sitemap_index.xml` | invalid | 目標畫面可見 Yahoo 404 HTML，非 XML |
| `/sitemap.xml.gz` | client-blocked | 兩次嘗試均未在目前分頁顯示目標或下載；沒有本地 artifact |

不要依此表推斷未列出的頁面不存在；未知頁面應回到可見 Index 或目的頁的可見連結查找。
