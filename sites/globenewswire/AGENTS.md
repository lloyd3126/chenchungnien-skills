# GlobeNewswire

## Scope

這份 site package 適用於透過 Codex 內建瀏覽器讀取 `https://www.globenewswire.com/` 的公開新聞、新聞稿、發布者、分類與 RSS/ATOM feed。預設只做讀取與可逆互動；不要把當次搜尋結果、價格、排名、數量、帳號資料或新聞內容寫死在操作指引中。

## Routing

- 想依關鍵字、產業分類、公司發布者或 tag 找公開新聞 → `$globenewswire-search`。
- 已有新聞稿 URL，想讀取標題、時間、來源、正文、tags、分類與公開動作 → `$globenewswire-release`。
- 想找主題、產業、地區的 RSS、ATOM 或 JavaScript widget feed → `$globenewswire-rss`。
- 想理解 GlobeNewswire 的服務、資料分發與 FAQ 定義 → 讀取 [first-party-guidance.md](references/first-party-guidance.md)，必要時直接開啟 `/about` 或 `/services`。

## Navigation

- 首頁：`https://www.globenewswire.com/`；可通往 Newsroom、Services、About Us、語言切換、Sign In 與 Register。
- Newsroom：`/newsroom`；公開搜尋欄、六個主要新聞分類與 `View All`（`/en/search`）。
- 主要分類：`/news/consumer-products-services`、`/news/energy`、`/news/banks-financial-services`、`/news/heathcare`、`/news/industrials-utilities`、`/news/technology-telecom`。子分類應從目前 UI 的可見連結取得，不要猜 opaque ID。
- 公開關鍵字結果：`/en/search/keyword/<encoded-keyword>?pageSize=10`；公司與 tag 結果應從搜尋結果的可見 source/tag link 進入。
- 新聞稿詳情：`/news-release/<YYYY>/<MM>/<DD>/<release-id>/<version>/<language>/<slug>.html`；`release-id`、version、language 與 slug 皆應取自可見連結。
- RSS 入口：`/rss/list`；詳情頁也可能提供該發布者的 RSS/ATOM link。Feed URL 常含分類字串或 token，不要自行重建 token。
- About：`/about`；Services：`/services`。它們是第一方說明與服務路由，不等於已登入的發佈或管理權限。

## Sitemap-assisted inventory

- 首頁與 footer 未見 sitemap link。`https://www.globenewswire.com/robots.txt` 已在目前使用者分頁中嘗試並重試，但內建瀏覽器回報 `ERR_BLOCKED_BY_CLIENT`，畫面/DOM 留在首頁；狀態是 `client-blocked`，不是「沒有 sitemap」。證據來源分開記為 current-tab DOM 與 automation/control error。
- `/sitemap.xml`、`/sitemap_index.xml`、`/sitemap.xml.gz` 均在同一使用者分頁中開啟並重試；網站 DOM 顯示自己的 404 頁，未取得 XML。標記為 `invalid/unavailable`，不宣稱 Sitemap 資源不存在以外的內容，也未用 CLI、API、curl 或外部瀏覽器替代抓取。
- Sitemap、robots 的完整目前 URL 清單與 tokenized feed URL 不應寫入 skills；穩定路由請參考 [site-map.md](references/site-map.md)。

## Operating rules

- 只使用 Codex 內建瀏覽器，固定目前已開啟的 GlobeNewswire 分頁；不要查 cookies、local storage、profiles、密碼或 session 檔案。
- 導覽或互動後至少核對目前 URL、heading、選中控制項、結果列或明確錯誤狀態中的兩項。URL 成功不單獨證明頁面已完成載入。
- 公開資料是動態的。重新取得當下的新聞、時間、結果、排序、分頁、feed entries 與可用操作；不要保存本輪 live values。
- 以網站 UI 與第一方說明為準。若控制項標籤、路由、欄位或權限漂移，先用目前 UI 完成安全任務，再更新所屬 skill/reference，並記錄日期、頁型、舊行為、新行為與證據來源。
- `Industry`、`Subject`、`Tag`、`Language`、`More Filters` 等搜尋篩選按鈕已看見，但本輪點擊控制路徑逾時，沒有把選項或成功改變結果寫成已驗證行為。RSS 的 `RSS by Industry` 與 `RSS by Location` tab 也只確認可見，未確認點擊後的內容；未來操作需重新驗證。
- `Follow`、分享、Reader account、發佈、註冊、寄送、付款、修改、刪除與任何不可逆確認都不屬於公開盤點的安全讀取範圍。

## Authentication

本輪目前分頁顯示 `Sign In`、`Register`、`Sign into Reader Account`，沒有已登入的使用者選單，因此按未登入公開變體處理。`/home/signin` 會導向 Notified login 頁，顯示 Username、Next、Forgot Username 與 reCAPTCHA；未輸入帳密、未解 CAPTCHA，也未進入客戶管理區。Reader account 的登入與建立帳號是另一個受保護/外部分支。

若使用者要求受保護功能，先完成公開流程後請使用者在同一個 Codex 內建瀏覽器分頁手動登入；登入後把它當成另一個 site variant，重新核對公開搜尋、分類、新聞稿與 RSS 入口，再探索安全的受保護分支。不要代填密碼，也不要把私人帳號資料寫入 artifacts。

## References

- [site-map.md](references/site-map.md)：路由、page taxonomy、coverage、Sitemap/robots evidence 與互動狀態。
- [data-model.md](references/data-model.md)：release、organization、taxonomy、search、tag 與 feed 的關係。
- [first-party-guidance.md](references/first-party-guidance.md)：About、Services、FAQ、內容來源與解讀限制。

## Drift maintenance

每次使用前比較目前畫面、URL、可見 labels、controls、權限與第一方說明。若只是新聞、搜尋結果、時間、feed entries 或其他動態值改變，更新重新取得資料的路徑即可；若穩定的路由、頁面結構、欄位語義或操作流程改變，完成安全重驗證後更新本檔或所屬 skill，並重新執行受影響的安全流程與 validator。遇到廣泛、矛盾或不可安全確認的變更，標記 maintenance gap，不要猜測。
