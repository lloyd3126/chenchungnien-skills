# 國中小代理代課教師人才庫媒合專區

## Scope

這份指引適用於 `https://hr.k12ea.gov.tw/ptst/` 的公開內容與目前已在 Codex 內建瀏覽器確認的未登入變體。網站屬於「高級中等以下教育人才庫入口網」的代理、代課、兼任及正式（獨招）職缺媒合專區；目前職缺、公告、縣市支持措施、FAQ、登入狀態與權限都必須在當次工作重新取得。

依使用者意圖選擇技能：

- [`$k12ea-ptst-job-search`](../../skills/k12ea-ptst-job-search/SKILL.md)：搜尋職缺、使用篩選器、閱讀職缺列表與明細、確認未登入時的權限邊界。
- [`$k12ea-ptst-public-resources`](../../skills/k12ea-ptst-public-resources/SKILL.md)：公告、縣市攬才／支持措施、求職說明、法規、FAQ、關於本專區、操作教學、網站導覽與政策頁。

本輪探索基準為 2026-08-17；所有日期、筆數、學校、職缺狀態、名額與公告正文均為動態資料，不得寫入可重用指引。

## Sitemap-assisted inventory

- `https://hr.k12ea.gov.tw/ptst/Sitemap/Index`：由目前分頁的「網站導覽」按鈕開啟，於同一分頁以 DOM 與視覺狀態確認為 `UI-verified`。它列出四個入口網專區；本套件只把第 2 區（代理代課）的路由視為本專區入口。
- 同源 `/robots.txt`：在同一目前分頁導航與重試均回報 `net::ERR_BLOCKED_BY_CLIENT`，截圖仍顯示原首頁；記為 `client-blocked`，證據為 `current-tab visual` 加 `automation/control error`。不要把它解讀為沒有 robots 內容。
- `/sitemap.xml`、`/sitemap_index.xml`、`/sitemap.xml.gz`：同一分頁實際開啟後都呈現網站自己的「抱歉。處理您的要求時發生錯誤。」HTML 頁，不是 Sitemap XML；記為 `invalid`，證據為 `current-tab visual`。不要再用 CLI、API、外部瀏覽器或網路搜尋替代。
- 網站導覽只作為候選路由 inventory；每次仍須以目前 UI 的 label、heading、控制項與結果驗證。不要窮舉或儲存動態 ID、tokenized URL、完整目前職缺清單。

## Global routing

- 查目前職缺 → `$k12ea-ptst-job-search` → `職缺資訊` → 篩選／查詢 → 結果表 → 點擊資料列 → 職缺明細。
- 查某校、縣市、職缺類型或教育級別 → `$k12ea-ptst-job-search` → 先選 `縣市`，再依需要選 `地區`、`設立類別`、`學校名稱`、`職缺類型`、`教育級別`、`領域`／`領域科目` → `查詢`。
- 查公告或某則公告 → `$k12ea-ptst-public-resources` → `訊息公告` → 類別與目前可見項目 → detail。
- 查地方攬才方案 → `$k12ea-ptst-public-resources` → `各縣市教師攬才及支持措施公告區` → 縣市 → 列表 → detail。
- 查資格、薪資或操作方法 → `$k12ea-ptst-public-resources` → `常見問題`、`相關法規`、`求職說明` 或 `操作教學`；以該頁第一方文字為準，不自行延伸法律或人事結論。
- 查履歷、收藏、主動應徵或完整聯絡資訊 → 先確認使用者是否已在目前分頁登入；本輪未登入，這些分支保持受保護，不得代填帳密、驗證碼或個資。

## Navigation

目前公開 UI 的主要入口如下；優先用可見 label 導航，只有在該 label 的 href 已被目前分頁確認後，才可在同一分頁重開該路由：

- `首頁`／`國中小代理代課教師人才庫媒合專區` → `/ptst/Home/ptst`：職缺摘要、縣市支持措施、公告摘要與影片。
- `職缺資訊` → `/ptst/JobVacancy/Index`：完整搜尋表單與分頁結果。
- `訊息公告` → `/ptst/News/Index`：`全部`、`公告訊息`、`活動訊息`、`即時新聞`；明細使用當下列表的 `ID`。
- `各縣市教師攬才及支持措施公告區` → `/ptst/RecruitSupport/Index`：縣市入口；從當下可見縣市 href 進入列表與明細。
- `求職說明` → `/ptst/Instruction/Index?...`：使用目前 UI 顯示的 href，不要硬編 FormID。
- `相關法規` → `/ptst/Laws/Index`：法規表與外部第一方連結。
- `常見問題` → `/ptst/FAQ/Index`：關鍵字搜尋、可展開問答與分頁。
- `關於本專區` → `/ptst/About/Index?...`；`操作教學` → `/ptst/Teaching/Index`。
- `網站導覽` → `/ptst/Sitemap/Index`：一方 route inventory 與快捷鍵說明。
- `求職者登入` → `/ptst/Account/Login`：Email／手機、密碼、驗證碼、快速註冊、忘記密碼／收不到信；登入與 CAPTCHA 未執行。
- `求才者登入` → `/Config/`：管理登入、驗證碼、縣市承辦／學校帳號申請入口；未登入後台。

## Operating rules

1. 只使用 Codex 內建瀏覽器目前分頁與網站 UI；不可改用 Chrome、Edge、外部瀏覽器、API、CLI、爬蟲、web search、cookies、local storage 或 session 檔案。
2. 每次操作前核對目前 URL、title、主要 heading、公開／登入後變體及 selected 控制項。導航 API 成功不代表頁面已在目前分頁視覺打開；要以同一分頁的 screenshot 或 DOM／interaction 確認。
3. 公開內容先探索。若目前畫面沒有明確登入狀態，不要代填帳號、密碼、OTP、CAPTCHA、身分證字號、生日、履歷或其他個資；需要受保護功能時，請使用者在同一分頁手動登入後再繼續。
4. 搜尋、篩選、展開 FAQ、點擊唯讀資料列與閱讀 detail 是安全操作；`我有意願`、加入最愛、註冊、登入、送驗證碼、上傳、儲存、送出、申請、分享及任何應徵／媒合動作都視為副作用邊界，停在最後一步並請使用者確認。
5. 法規表、教學影片、YouTube、Google Maps、Facebook、LINE、外部 PDF 與其他外部連結只記為入口；除非使用者明確要求，不要離站探索。
6. 網站的 live 職缺、公告、支持方案、FAQ 答案、更新時間與 visitor counter 會變動；回答時重新抓取並保留當次路由／查詢／日期，不把結果值寫進文件。
7. 網站自己的求職說明表示需登入並完成履歷後才能查詢職缺；但本輪未登入首頁與職缺頁仍可見公開列表。遇到此差異時，分開報告「說明頁陳述」與「目前 UI 可見行為」，不要猜測登入後範圍。

## Freshness and verification

- 職缺：重開 `職缺資訊`，確認表單 selected 狀態、結果表 heading／欄名與當次列；需要 detail 時由目前結果列取得 `data-vacurl` 對應的點擊行為，核對職缺編號、學校、地區、教育級別、類型、聘任期間、狀態與招次。
- 公告／支持措施：從目前列表選取項目，核對 detail heading、日期、發布單位或縣市及正文；不要把目前公告日期或內容當成永久規則。
- FAQ／法規／教學：重新確認目前問題、展開狀態、標題、法規表或教學連結仍存在；外部頁面未開啟前不宣稱其內容已驗證。
- 任何 UI drift：記錄 public/authenticated variant、頁型、路由、舊／新 label、觀察日期與 `current-tab visual` 或 `current-tab DOM/interaction` 證據；若差異穩定且安全，再更新 owning skill/reference 並重跑 validator。

## Known limits

- 本輪為未登入公開變體；`我的最愛` 實際導向 `https://hr.k12ea.gov.tw/Home/Account/Login?ReturnUrl=...`。履歷、收藏、完整聯絡資料、3 招以上資訊、主動應徵與媒合後台未探索。
- 求職者註冊頁會先顯示會員約定條款 modal，並要求 Email、密碼、姓名、手機、生日、身分證字號與驗證碼；未勾選、未同意、未填寫、未送出。
- `求才者登入` 導向 `/Config/` 管理登入；未執行縣市承辦／學校帳號申請、登入、職缺開立或媒合管理。
- `RecruitSupport` 列表與明細的 DOM／導航成功，但多次 screenshot 控制曾逾時；因此相關頁不把控制錯誤寫成「沒有內容」，並在 coverage reference 中保留證據來源與限制。

## References

- [coverage.md](references/coverage.md)：Sitemap 狀態、公開入口、page taxonomy、互動證據與未確認分支。
- [page-types-and-entities.md](references/page-types-and-entities.md)：職缺、公告、支持措施、FAQ、法規與帳號入口的資料模型和 workflow。
- [first-party-guidance.md](references/first-party-guidance.md)：關於本專區、求職說明、FAQ、註冊條款、隱私／資訊安全頁的第一方說明與解讀限制。
- [agent-usability.md](references/agent-usability.md)：跨職缺、公告、支持措施、FAQ 與收藏邊界的路由選擇測試。
