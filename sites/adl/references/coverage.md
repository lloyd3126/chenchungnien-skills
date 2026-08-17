# 探索覆蓋與證據

探索日期：2026-08-17。所有瀏覽證據來自使用者原本開啟的同一 Codex 內建瀏覽器分頁；沒有建立臨時分頁或切換瀏覽器。

## Sitemap 與 route inventory

| Route / source | 內容 | 狀態 | 證據來源 |
| --- | --- | --- | --- |
| `/HomePage/sitemap/` | 站內導覽：首頁、登入、消息、活動、操作手冊、FAQ、問題回報、教育雲、政策頁 | UI-verified | current-tab visual + current-tab DOM |
| `/robots.txt` | 同源 robots 候選 | unavailable；同一分頁開啟與重試皆呈現網站 404 | current-tab visual |
| `/HomePage/home/` | 公開首頁、最新消息／活動入口、研習與帳號、操作手冊、FAQ | explored | current-tab visual + current-tab DOM |
| `/modules_new.php?op=modload&name=dashboard&file=modules_dashboard` | 登入後教師儀表板候選 | initial UI-verified；離開原始狀態後重開被導回公開首頁 | current-tab visual + current-tab DOM；後續 redirect 也是 current-tab visual |

沒有因為 robots 404 就宣稱網站沒有 Sitemap；目前已有站內導覽，因此沒有再猜測大量 sitemap 路徑。

## 公開區 coverage

| Area | 可見入口／頁型 | 安全測試 | 狀態 |
| --- | --- | --- | --- |
| 首頁 | `首頁`；banner、最新消息、活動、研習與帳號、操作手冊、FAQ、頁尾 | 展開網站選單，確認公開導覽 label | explored |
| 最新消息 | `最新消息`／`檢視全部消息`；列表與詳細頁 | 從第 1 頁點擊可見的 `2`，URL 與列表內容改變；開啟一則詳細頁，確認標題、更新時間、正文與外連 | explored |
| 最新活動 | `更多活動`；日期區間／標題／目標連結列表 | 讀取列表與分頁控制；未追入離站活動 | explored |
| 操作手冊 | `操作手冊`；角色、功能、帳號、影片與 PDF／文件入口 | 讀取區段與可見連結；未下載或開啟外部文件 | explored |
| 常見問題 | `常見問題`；六個角色／主題分類 | 點擊 `教師操作篇`，確認 active 狀態、heading 與問答集合改變 | explored |
| 研習與帳號 | `研習與帳號` → `帳號申請`；角色 accordion | 展開 `教師帳號申請`，確認證明文件與線上申請入口；未上傳、填寫或送出 | partial |
| 網站導覽 | 頁尾 `網站導覽` | 開啟並讀取 12 個可見入口 | explored |

## 登入後初始視覺

初始使用者分頁標題為「教育部因材網0086」，公開頁 banner 顯示「連淑貞 歡迎」。原始分頁視覺與 DOM 曾顯示：

- app bar：`操作介紹`、`課程總覽`、`ＡＩ學伴`、`指派任務`、`登出`。
- 主區域：`待辦事項`、本週待辦狀態、日期欄、公告、任務儀表板、`+ 指派任務`、`快速檢視` 與列表／篩選類控制。
- 受保護路由可見，但在公開頁探索完成後，對同一路由的直接重開於同一分頁等待後導回 `/HomePage/home/`；這是 session／授權狀態需重新確認的證據，不是受保護功能不存在的證據。

## Evidence integrity checklist

- [x] 探索前先檢查並 claim 使用者目前分頁。
- [x] 每個重要目標都在同一分頁開啟後才解讀。
- [x] 導航後擷取同一分頁 screenshot；robots 導航與重試也都擷取。
- [x] robots 404 被記為 unavailable，不被改寫成 no sitemap discovered。
- [x] 沒有使用外部瀏覽器、API、CLI、web search、cookie 或 session 檔案。
- [x] 沒有把目前消息標題、活動數量、任務、學生資料或個人資料寫入長期操作規則。

## Unconfirmed or intentionally untested

- `課程總覽`、`ＡＩ學伴` 與完整受保護側欄在初始 dashboard 上可見，但本輪未能在公開探索後重新開啟並驗證其內容。
- 沒有進行登入／登出、帳號綁定、帳號申請、檔案上傳、任務建立／指派、班級／學生資料修改、匯入、轉入／轉出、代幣、問題回報或任何會產生外部副作用的操作。
- 外部 Google Drive、YouTube、Google Sites、Facebook、教育雲與活動網站只記錄為當前 UI 顯示的連結，不把外部頁面內容視為本輪已驗證。
