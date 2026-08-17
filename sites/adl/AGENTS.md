# 教育部因材網

## Scope

這份指引適用於 `https://adl.edu.tw/` 的公開內容、第一方說明文件，以及已在目前 Codex 內建瀏覽器分頁中確認的教師儀表板。即時消息、活動、任務、班級、學生資料、權限與登入狀態都必須在當次工作重新取得。

依使用者意圖選擇技能：

- [`$adl-public-resources`](../../skills/adl-public-resources/SKILL.md)：公開首頁、最新消息、活動、公告詳細頁、操作手冊、FAQ、帳號申請與網站導覽。
- [`$adl-teacher-workflows`](../../skills/adl-teacher-workflows/SKILL.md)：登入後教師儀表板、任務指派／進度、課程總覽、AI 學伴、班級／帳號與學習扶助路由。

詳細覆蓋範圍與證據請先看 [`references/coverage.md`](references/coverage.md)；頁型與資料模型看 [`references/page-types-and-entities.md`](references/page-types-and-entities.md)；教師工作流看 [`references/teacher-workflows.md`](references/teacher-workflows.md)。

## Sitemap-assisted inventory

- 頁尾可見「網站導覽」，在目前分頁開啟後以視覺與 DOM 確認為 `https://adl.edu.tw/HomePage/sitemap/`，列出首頁、登入、最新消息、最新活動、操作手冊、常見問題、網站導覽、問題回報、教育雲與政策頁。這是 UI-verified 的站內導覽，不是完整的所有應用路由清單。
- 同源 `https://adl.edu.tw/robots.txt` 已在同一目前分頁開啟並重試；畫面兩次都呈現網站自己的 `404 Not Found`，記為 `unavailable`，證據來源為 `current-tab visual`。不要把它解讀為沒有 Sitemap 或沒有受保護路由。
- 不要把目前消息、活動、分頁筆數、任務、排名、使用者資料或 tokenized／動態 URL 寫入長期指引。從 UI 重新取得當下資料即可。

## Global routing

- 查目前公告、新聞或活動 → `$adl-public-resources` → 首頁的「最新消息」／「更多活動」→ 驗證列表 heading、日期／標題與詳細頁內容。
- 查某則公告 → `$adl-public-resources` → 從當下可見列表選取項目 → 詳細頁 → 驗證標題、更新時間、正文與外連。
- 查操作方式或定義 → `$adl-public-resources` → 「操作手冊」或「常見問題」→ 先用角色／分類篩選，再依當前頁面與第一方說明回答。
- 查帳號申請 → `$adl-public-resources` → 「研習與帳號」→「帳號申請」→ 展開對應角色；涉及上傳、填寫、寄信或送出時停在副作用邊界。
- 查教師任務或學生學習資料 → `$adl-teacher-workflows` → 先確認登入後教師儀表板可見，再依「指派任務」、「任務儀表板」、「班級管理」或「學習扶助」路由。

## Navigation

### 公開／入口區

- `https://adl.edu.tw/HomePage/home/`：公開首頁；可見「最新消息」、「更多活動」、「研習與帳號」、「操作手冊」、「常見問題」及頁尾「網站導覽」。
- `https://adl.edu.tw/HomePage/news-list/?page=1`：最新消息列表；從當前可見列表分頁，不猜測 `Id`。
- `https://adl.edu.tw/HomePage/activity-list/?page=1`：活動列表；每筆包含日期區間、標題與目標連結，部分連結會離站。
- `https://adl.edu.tw/HomePage/webinfo/?id=4`：操作手冊；依教師、學生、校管、家長／大學伴、教師功能、功能列表等區段尋找第一方文件與影片。
- `https://adl.edu.tw/HomePage/faq/`：常見問題；可用「帳號篇」、「校管操作篇」、「教師操作篇」、「學習扶助篇」、「其他」篩選。
- `https://adl.edu.tw/HomePage/account-apply/`：研習與帳號的分頁區，內含帳號申請與角色 accordion。

### 登入後教師入口

本輪目前分頁最初以視覺確認了 `https://adl.edu.tw/modules_new.php?op=modload&name=dashboard&file=modules_dashboard` 的教師儀表板，頂部可見「操作介紹」、「課程總覽」、「ＡＩ學伴」、「指派任務」、「登出」；主要區域可見待辦事項／行事曆、公告、任務儀表板與「+ 指派任務」。這個登入變體在離開原始頁面後再次直接開啟時被導回公開首頁，因此後續 Agent 必須每次以目前畫面確認受保護頁是否仍可用，不要只依 URL 宣稱已登入。

## Operating rules

1. 只使用 Codex 內建瀏覽器目前分頁與網站 UI；不切換 Chrome／Edge，不使用外部瀏覽器、API、CLI、web search、cookie、local storage、session 檔案或猜測 URL 網格。
2. 每次操作前核對目前 URL、頁面標題／主要 heading、可見登入狀態與 selected／active 控制。導航成功必須以目前分頁的視覺或 DOM 結果確認，URL 改變本身不算成功。
3. 先公開、後受保護。若頁面沒有明確顯示已登入，不代填帳密；需要受保護功能時，請使用者在同一內建瀏覽器分頁手動登入後再繼續。
4. 搜尋結果、消息、活動、任務、學生名單、報表、權限、數量與目前時間都是動態資料；長期文件只保留取回路徑、欄位語義、穩定流程與驗證規則。
5. `建立`、`確定指派`、`送出`、`儲存`、`上傳`、`寄信`、`問題回報`、`登入／綁定`、`匯入`、`刪除`、`停用`、`轉入／轉出`、代幣發放或兌換，都視為副作用邊界。除非使用者在當下明確確認，停在最後一步並說明即將傳送的資料與目的地。
6. 先用網站自己的操作手冊與 FAQ 解釋欄位、角色與限制；不要用一般常識補齊未驗證的應用行為。
7. 若目前 UI 與文件不同，先以目前可見 UI 安全完成工作，記錄登入變體、頁型、舊／新 label、實際結果與日期；只有穩定且可再次確認的差異才更新本套件。

## Freshness and validation

- 公開消息／活動：重新開啟列表，確認 heading、當前日期／標題，必要時開啟詳細頁並核對更新時間與正文。
- FAQ／手冊：確認目前分類、問題／文件標題與第一方說明仍在頁面上；外部 Google Drive／YouTube 連結只當作文件入口，不把未開啟內容當作已驗證事實。
- 教師任務：確認登入後 app bar、任務卡、班級／學生 scope、當前學期與控制項；任務數據與診斷結果不可沿用文件中的示例值。

## Known limits

- 本輪沒有取得可用的 robots metadata：同源 `robots.txt` 在目前分頁兩次視覺呈現 404。
- 公開區已視覺確認；教師儀表板只在本輪最初目前分頁狀態中確認。離開該狀態後直接重開受保護路由會被導回公開首頁，故課程總覽、AI 學伴與完整教師選單標記為 partial／需目前登入狀態重新驗證。
- 沒有執行登入、帳號申請、檔案上傳、任務建立／指派、學生資料修改、匯入、問題回報、代幣操作、登出或任何不可逆動作。

## References

- [`references/coverage.md`](references/coverage.md)：路由、證據來源、頁型覆蓋與未確認分支。
- [`references/page-types-and-entities.md`](references/page-types-and-entities.md)：公開頁型、第一方文件類型與教師工作區 entity 模型。
- [`references/teacher-workflows.md`](references/teacher-workflows.md)：由可見教師儀表板、FAQ 與操作手冊整理的唯讀路由與副作用邊界。
