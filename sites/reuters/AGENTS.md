# Reuters 網站操作指引

## Scope

這份指引適用於透過 Codex 內建瀏覽器唯讀操作 `https://www.reuters.com/`。Reuters 是國際新聞、商業與市場資訊網站；本輪（2026-08-17）完成未登入公開頁面探索，並將穩定的導覽、搜尋、Markets 與文章頁型整理成可重用路由。

目前頁首可見 `Sign In`、`Register`，沒有已登入訊號。`My News`、儲存文章、個人化內容、訂閱與帳號設定因此都視為受保護或有副作用的分支。

## Sitemap-assisted inventory

- 首頁／錯誤頁的第一方 footer `Site Index` 暴露 `Article Sitemap` `/sitemap/`、`Topic Sitemap` `/sitemap/topics/`、`Authors` `/sitemap/authors/` 與 `Archive` `/archive/`。
- `/sitemap/` 在目前分頁以 `Sitemap | Reuters` 顯示年份與月份索引；可見 2026 年 1–8 月、2025–2021 年月份，以及 `Articles from before 2021-01-04`。代表月份 `/sitemap/2026-08/` 再按日期導向 `/sitemap/2026-08/<day>/1/`。這些是文章 inventory，不是權限或功能證明。
- `/sitemap/topics/` 與 `/sitemap/authors/` 都顯示 `Topics and Authors sitemap | Reuters`，可依英文字母分段進入 topic／author。只保存路由模式，不保存當下文章、作者或數量。
- `/robots.txt` 在目前內建瀏覽器以兩次同分頁導覽與視覺重試後仍回報 `ERR_BLOCKED_BY_CLIENT`，記為 `client-blocked`；不代表 robots 或 Sitemap 不存在。
- `/sitemap.xml` 與 `/sitemap_index.xml` 在目前分頁可視為 Reuters 404 HTML（`We can't find that page`），不是 XML Sitemap，記為 `invalid`。不要再猜測大量 Sitemap 路徑。
- 2026-08 月份頁的 DOM 已讀到日期索引，但該頁視覺擷取多次因控制逾時失敗，故不要稱為 `UI-verified`；證據來源是 `current-tab DOM/interaction` 加 `automation/control error`。

## Global routing

- 想搜尋 Reuters 全站新聞、套用 section／日期／排序 → `$reuters-news-search`；需要詳細欄位與選項時讀 [form-controls.md](references/form-controls.md)。
- 想看 Markets 頁、區域分頁、商品／匯率／債券／股票表格或 quote page → `$reuters-market-data`。
- 想讀一篇 Reuters 文章、確認作者／時間／摘要／正文／圖片／來源與 access state → `$reuters-article-research`。
- 想找 topic、author、月份或日期 inventory → 讀 [site-map.md](references/site-map.md)，再用目前 UI 開啟代表頁，不要把 Sitemap 當成內容或權限證明。

## Navigation

- `World` `/world/`：世界新聞與區域／國家子分類。
- `Business` `/business/`：商業、公司、金融、產業與消費新聞。
- `Markets` `/markets/`：市場首頁，含 `US`、`Europe`、`Asia Pacific` 分頁、Markets 子分類與延遲行情表格。
- `Sustainability` `/sustainability/`：永續、氣候與 ESG 相關新聞。
- `Legal` `/legal/`：法律、監管、交易與政府相關新聞。
- `Commentary` `/commentary/`：`Reuters Open Interest`、`Reuters Breakingviews` 與其他評論／贊助內容入口。
- `Technology` `/technology/`：科技與 AI 相關新聞。
- `Investigations` `/investigations/`：`Reuters Investigates` 與 `More Investigations` 特別報導。
- `More` 展開後可見 `Sports`（含 World Cup、Athletics、Baseball、Basketball、Cricket、Cycling、Formula 1、Golf、NFL、NHL、Soccer、Tennis）、`Science`、`Lifestyle`、`City Memo`、`Graphics`、`Pictures`、`Wider Image`、`Podcasts`、`Live`、`Fact Check`、`Video`、`Media Center` 與 `Sponsored Content`。
- 頁尾也提供 `Videos`、`Pictures`、`Graphics`、`Podcasts`、`Newsletters`、`Reuters Fact Check`、`Data Disclosure and Sources`、`Terms & Conditions`、`Corrections` 與 `See here for a list of exchanges and delays` 等第一方入口。

## Operating rules

- 只使用目前使用者可見的 Codex 內建瀏覽器分頁；不要改用外部瀏覽器、API、CLI、搜尋引擎、cookies、local storage 或 session 檔案。
- 每次操作前比較目前畫面的 URL、title／heading、選中 tab 或結果；導覽成功不能只靠 URL 判定。若視覺控制失敗，保留 `automation/control error`，不要把它改寫成頁面不存在。
- 文章、新聞清單、作者內容、搜尋結果、結果數量、排名、行情、百分比、日期與可見性都是動態資料；執行任務時重新取得，並保留查詢、篩選、排序與觀察時間。
- Reuters Markets 頁的行情表格標示資料來自 `LSEG`，並顯示至少延遲 15 分鐘的說明；不要把行情當成即時報價或投資建議。
- `Save article`、`Share article`、`Email article`、`Follow`、`Subscribe`、註冊、登入、留言、購買 licensing rights、修改帳號與任何最後確認都屬副作用邊界。唯讀任務在最後確認前停止。
- 不要繞過登入、註冊、付費牆、CAPTCHA、內容限制或受保護文章。若未來分頁明確已登入，先把登入狀態視為另一個 site variant，重新檢查公開頁與控制項後才寫入登入後行為。
- Sitemap、robots、頁面 200 或 HTML 連結只提供 inventory clues；只有在目前分頁 UI／DOM 實際驗證後，才可描述某功能或頁型可用。

## Drift maintenance

- 每次任務前比對目前 UI、路由、label、controls、權限與第一方說明；目前 UI 優先於這份文件。
- 若穩定路由、頁型、欄位、控制項或流程改變，記錄 public／authenticated variant、頁型、舊行為、觀察行為、驗證證據與日期，再更新負責的 skill 或 reference。
- 若只是價格、排名、數量、文章、結果或可用性改變，更新重新取得與驗證方法，不要把 live value 寫入指引。
- 修改後重跑受影響的唯讀流程與 skill validator。若差異廣泛、矛盾或無法安全驗證，標記為 maintenance gap，不要猜測。

## Known limits

- 本輪只完成公開、未登入探索；`My News`、Save／Follow 後內容、帳號、註冊、登入、訂閱、付費內容與個人化資料未驗證。
- `robots.txt` 是瀏覽器控制路徑的 `client-blocked`；沒有把它解讀成「沒有 Sitemap」。
- 部分含廣告或動態元件的頁面視覺擷取曾逾時或回報 target closed；若文件標示 `current-tab DOM/interaction`，不要升級成 `current-tab visual` 或 `UI-verified`。
- 搜尋篩選的結果內容、數量與排序都要在任務當下重新確認；Section 篩選會反映到 URL query，但不要只靠 URL 推斷結果已正確套用。

## References

- [site-map.md](references/site-map.md)：第一方 Sitemap、代表路由、頁型與探索狀態。
- [data-model.md](references/data-model.md)：文章、section、topic、author、search result、market instrument 與 Sitemap entity 關係。
- [form-controls.md](references/form-controls.md)：站內搜尋、篩選／排序、Markets 區域 tabs 與文章控制項。
- [first-party-guidance.md](references/first-party-guidance.md)：Reuters／LSEG 來源、延遲行情、Trust Principles、贊助內容與 access 限制。
- [agent-usability.md](references/agent-usability.md)：未來 Agent 的路由與安全停點測試情境。
