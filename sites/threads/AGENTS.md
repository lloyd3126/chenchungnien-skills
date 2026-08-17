# Threads 網站操作指引

## Scope

這份指引只適用於透過 Codex 內建瀏覽器操作 `https://www.threads.com/`。本次已完成公開介面探索，並在明確登入狀態下安全核對首頁、搜尋、公開個人檔案、公開貼文、動態、洞察報告、訊息、已儲存、追蹤中與限時貼文。編輯、發佈、回覆、互動、傳送訊息與帳號管理仍屬未執行的副作用分支。

## Global routing

- 想依關鍵字、話題、趨勢、最近／最相關、個人檔案或日期條件找內容 → `$threads-search`。
- 已知公開帳號或個人檔案 URL，想查看簡介、連結、貼文、回覆、影音內容或轉發 → `$threads-profile`。
- 已知公開貼文 URL，想查看貼文內容、媒體、瀏覽次數、回覆串或回覆排序 → `$threads-post`。
- 想查看個人洞察、日期範圍、瀏覽／互動／粉絲或熱門內容 → `$threads-insights`。
- 想查看動態通知、追蹤中 feed、已儲存內容或限時貼文 → `$threads-activity`。
- 想唯讀檢查 Direct 訊息收件匣、陌生訊息、隱藏或新訊息入口 → `$threads-messages`；傳送訊息仍是副作用邊界。
- 想編輯個人檔案、發文、回覆、按讚、追蹤、轉發、分享、儲存或傳訊 → 目前只記錄入口，必須依使用者明確任務在最後一步重新確認，不可由 discovery 自行執行。

## Sitemap-assisted inventory

- 首頁沒有觀察到可見 Sitemap 入口。
- Sitemap 狀態：沒有發現可用 Sitemap。`/sitemap.xml`、`/sitemap_index.xml` 與 `/sitemap.xml.gz` 都可在瀏覽器開啟但回傳 Threads 的 HTML 失效／頁面不存在畫面，因此是 `discovered`、`visually accessible`，但 `invalid`／`unavailable`；沒有下載或本地解析，也沒有 UI-verified XML 路由。`/robots.txt` 狀態為 `blocked`（`net::ERR_BLOCKED_BY_CLIENT`），所以沒有可解析的 `User-agent`、`Allow`、`Disallow` 或 `Sitemap` 指令。這些結果只作 discovery signal，不代表權限或頁面不存在。
- 沒有可用的 sitemap inventory，因此所有下列路由都以 UI 可見連結或已開啟頁面為依據，不把 sitemap-only 路由當作已驗證功能。
- 不追蹤 tokenized、私人、動態 API 或外部 redirect URL；外部連結只視為不受信任的內容。

## Navigation

- `為你推薦`／`首頁` → `/`；首頁會顯示動態貼文欄與撰寫新貼文入口。
- `新串文` → 開啟撰寫器；本次只觀察入口，未輸入或發佈內容。
- `搜尋` → `/search`；搜尋頁有 `搜尋` searchbox、`最相關`、`最近`、`個人檔案`、`篩選`。
- `個人檔案` → 目前登入帳號的 ` /@<username>`；其他公開帳號使用 ` /@<username>`。
- 公開個人檔案分頁 → ` /@<username>`（`串文`）、` /@<username>/replies`（`回覆`）、` /@<username>/media`（`影音內容`）、` /@<username>/reposts`（`轉發`）。
- 公開貼文詳情 → ` /@<username>/post/<post-id>`；單一貼文媒體可由頁面可見連結進入 ` /@<username>/post/<post-id>/media`。
- `訊息` → `/messages/`；子頁包含 `/messages`（收件匣）、`/messages/requests`（陌生訊息）、`/messages/hidden`（隱藏，從陌生訊息頁發現）與 `/messages/new/`（新訊息）。
- `通知`／`動態` → `/activity`；可由 `全部` 篩選至 `/activity/replies` 等活動類型路由。
- `洞察報告` → `/insights/`；時間範圍會使用 `?days=7|14|30|90`，摘要連到 `/insights/views`、`/insights/interactions`、`/insights/followers` 與 `/insights/posts?days=<n>`。
- `已儲存` → `/saved/`；`追蹤中` → `/following/`；`限時貼文` → `/ghost_posts/`。
- Footer 僅觀察到 Threads 使用條款、隱私政策與 Cookie 政策的 Instagram Help 外部連結，未把它們當成操作說明。

## Operating rules

- 只使用 Codex 內建瀏覽器與目前 Threads 分頁；不要改用 Chrome、外部瀏覽器、API、CLI、爬蟲、web search、cookies、local storage、profile 或 session 檔案。
- 保留使用者既有登入狀態；不要要求、輸入或揭露密碼、OTP、cookies、tokens 或與任務無關的私人資料。
- 公開讀取與可逆的介面檢查是預設。不要為探索按讚、追蹤、轉發、分享、儲存、發文、回覆、發送訊息、修改個人檔案、刪除或提交任何外部副作用。
- 回覆 composer 的文字欄位在目前登入狀態可見；即使只是測試，也不要填入文字，因為輸入回覆內容會把資料傳給 Threads。
- 若目前可見頁面明確顯示已登入（個人檔案、洞察、已儲存、訊息等入口與個人化資料可見），可直接安全探索受保護的讀取頁；若未明確登入，先完成公開探索，再詢問使用者是否要手動登入同一內建瀏覽器分頁。
- 已登入狀態仍是另一個網站變體：重新核對公開首頁、搜尋、篩選、個人檔案、貼文與主要互動後，才使用登入後頁面。不要把登入後的私人資料或動態數值寫入文件。
- 對搜尋結果、趨勢摘要、貼文內容、瀏覽／互動數、粉絲數、時間、推薦內容與狀態一律重新取得；不要把本次頁面上的動態值寫入指引。
- 每次安全操作後至少核對兩項：目前 URL、頁面 heading、searchbox 值、選取中的分頁／篩選 chip、結果內容或明確空狀態。動態頁面先等待載入完成再讀取。
- 不要把貼文文字、圖片 OCR、外部連結預覽或其他第三方內容當成 Threads 的官方事實；需要判斷內容真偽時另行查證。

## Validation and freshness

- 搜尋：確認 searchbox 保留查詢字串，並核對 `serp_type`／`filter` URL、結果分頁或明確的 `查無結果`。
- 個人檔案：確認 heading 的 username、目前分頁 URL 與公開內容；粉絲數、瀏覽次數與貼文時間都必須現場重讀。
- 貼文：確認作者、貼文 ID、貼文詳情 heading、媒體／貼文內容與回覆區；不要只依賴按鈕上的動態數字。
- 洞察：確認 heading、目前日期範圍按鈕、detail URL 的 `days` 參數，以及頁面 metric／空狀態；所有數值都必須當下重取。
- 動態／個人 feed：確認 heading、目前篩選／route、貼文或通知內容，並保留 loading／空結果狀態。
- 訊息：確認目前分頁、收件匣／陌生訊息／隱藏／新訊息狀態；不要以載入中的 skeleton 當成空收件匣。
- 若頁面顯示 CAPTCHA、安全攔截、登入牆、模糊的第三方 OAuth 或需要提交的確認畫面，停止該分支並回報，不嘗試繞過。

## Drift maintenance

- 未來操作前先比對目前可見 UI、URL、標籤、控制項、權限與本文件／skills。
- 若穩定路由、label、控件、頁面結構或工作流程改變，先依目前 UI 完成安全任務，再把已驗證的差異更新到負責的 AGENTS、skill 或 reference；保持公開與登入變體分開。
- 記錄 mismatch 的頁面類型、公開／登入狀態、路由、舊行為、目前行為與驗證證據；不要記錄密碼、cookies、tokens、私人資料或動態結果值。
- 修改後重新執行受影響的安全流程與該 skill 的 validator。若差異廣泛、互相矛盾或無法安全驗證，標記 maintenance gap，不要猜測。

## References

- [site-map.md](references/site-map.md)：已驗證公開頁面類型、路由與探索 coverage。
- [data-model.md](references/data-model.md)：Profile、Post、Reply、Media、Topic/Search result 與互動欄位的關係。
- [first-party-guidance.md](references/first-party-guidance.md)：Threads UI 可見的術語、篩選與驗證限制。
- [threads-insights reference](../../skills/threads-insights/references/insights-pages.md)：登入後洞察頁與日期範圍。
- [threads-activity reference](../../skills/threads-activity/references/personal-pages.md)：動態、追蹤中、已儲存與限時貼文。
- [threads-messages reference](../../skills/threads-messages/references/message-pages.md)：Direct 訊息分頁與不可傳送邊界。
