---
name: k12ea-ptst-job-search
description: "Use the Codex in-app browser to search and verify current 國中小代理代課教師人才庫媒合專區 vacancies, filters, dependent district/subject controls, result rows, vacancy detail pages, and unauthenticated access boundaries. Trigger for requests about current PTST vacancies, schools, counties, vacancy types, education levels, subjects, recruitment dates, vacancy details, or favorites on hr.k12ea.gov.tw/ptst."
---

# 國中小代理代課職缺搜尋

## Purpose and entry point

在 Codex 內建瀏覽器中唯讀查詢 `https://hr.k12ea.gov.tw/ptst/JobVacancy/Index`。從目前可見分頁開始，保留同一個使用者分頁與 session；如果目前不是 PTST，先由可見 `國中小代理代課教師人才庫媒合專區` 或 `職缺資訊` 入口返回，再確認 URL、title 與 `職缺資訊` heading。

## Procedure

1. 先檢查目前是否明確登入。未登入時仍可讀取公開列表，但不要輸入帳密、驗證碼或個資。
2. 開啟 `職缺資訊`，確認篩選表與結果表已在目前分頁顯示。不要把首頁摘要的目前列當成完整結果。
3. 依使用者意圖填寫目前可見控制項：
   - `職缺公告日期區間`、`甄試日期區間`：使用頁面 placeholder `年/月/日` 的日期欄位。
   - `*必填 縣市`：先選縣市；`地區` 會依縣市載入，先確認選項，再選 `全區` 或目前可見行政區。
   - `設立類別`：`國立`、`私立`、`公立`。
   - `學校名稱`：輸入使用者提供的學校關鍵字，不猜測校名或代碼。
   - `職缺類型`：`代理`、`代課`、`兼任`、`正式(獨招)`。
   - `教育級別`：`國小` 或 `國中`。
   - `領域`：先選領域，再確認 `領域科目` 是否更新；例如 `語文領域` 會載入目前可見的 `國文`、`英語`、`第二外國語文`、`臺灣手語`、`新住民語文`、`閩南語`、`閩東語`、`客家語`、`原住民族語`。
   - `關鍵字`：輸入安全、非敏感的查詢字串。
4. 填寫後按目前頁面顯示的 `查詢`，等待結果刷新。確認 URL（若查詢使用 query string）、保留的 selected 值、結果表的 heading／欄名與資料列；只有按鈕被點擊不算查詢成功。
5. 注意頁面明示「僅顯示近100筆相關資料或請縮小搜尋範圍」。結果以分頁呈現，分頁號碼與 `>` 必須從目前 UI 取得，不能猜頁數或直接建立 URL 網格。
6. 如需清空條件，按 `重設`，確認欄位回到 `請選擇`／空白、地區回到 `全區`；本輪觀察到重設會清空表單，但可能保留目前 query URL 與空結果狀態，因此需要新查詢時重新開啟未帶條件的 `職缺資訊` 路由並驗證。

## Read result rows and detail

- 結果表欄位為 `地區`、`學校名稱`、`領域(科目)`、`公告日期`、`甄試日期`、`聘任期間`、`教育級別`、`職缺類型`、`加入最愛`。
- 資料列不是可見 `<a>`；目前 DOM 以 `tr[data-vacurl]` 實作點擊導向。從當下結果列點擊，不要把別次探索的 `ID` 寫死。驗證 detail URL、`職缺資訊` heading 與 detail table。
- detail 可讀欄位包含刊登日期、職缺編號、學校代碼／名稱／地址、地區、職缺類型、教育級別、領域／科目／缺額類科、雙語教師欄、名額、職缺狀態、招次及報名／甄試日期、聘任期間。
- 未登入 detail 可能只顯示 `請登入後查詢` 的 3 招以上、聯絡人、電話、Email、相關連結與職缺描述；把它當成權限訊號，不要猜測內容。
- detail 的 `我有意願` 是主動應徵／媒合相關動作；不要點擊。學校地址的 `查看地圖(另開視窗)` 是外部連結，除非使用者要求，不要離站。

## Favorites and authentication boundary

- 列表中的星號／`加入最愛` 與 `我的最愛` 都可能改變帳戶狀態；除非使用者在當下明確要求並確認副作用，不要點擊星號或儲存收藏。
- 未登入開啟 `/ptst/Resume/JobVacancyFav` 時，本輪實際導向入口網 `/Home/Account/Login?ReturnUrl=...`。這是 `protected—awaiting user choice`，不是功能不存在。
- `求職者登入` 會要求 Email 或手機、密碼、驗證碼；`快速註冊` 先顯示會員條款，再要求 Email、密碼、姓名、手機、生日、身分證字號與驗證碼。不要代填或接受條款。
- 若使用者要探索登入後履歷、收藏、應徵或完整聯絡資料，先請使用者在同一個 Codex 內建瀏覽器分頁手動登入；登入後需把 public 與 authenticated 當成兩個變體重新核對。

## Safety and limits

- 搜尋、篩選、分頁、點擊資料列與閱讀 detail 是唯讀；查詢中的學校／職缺關鍵字也應避免輸入個資。
- 停在 `我有意願`、加入最愛、登入、註冊、發送驗證碼、上傳履歷、儲存履歷、應徵送出與任何確認視窗前。
- 目前資料、結果數量、職缺狀態、名額、日期和列表排序都要重新抓取；不可把探索時的 live row 寫入回答以外的長期文件。

## Drift maintenance

- 每次執行前比較目前可見 header、route、`職缺資訊` 表單 labels、selected 值、分頁、結果欄位與第一方 `求職說明`／`操作教學`。
- 若 label、依賴下拉、query state、資料列點擊或權限行為改變，先用目前 UI 完成安全任務，再記錄 public/authenticated variant、舊／新行為、日期與證據。
- 只有在差異穩定、清楚且可再次安全驗證時才更新本 skill 或 site reference；更新後重跑本流程與 `quick_validate.py`。不記錄密碼、cookies、token、個資或 live result value。

## References

- [../../sites/k12ea-ptst/AGENTS.md](../../sites/k12ea-ptst/AGENTS.md) — 共用 session、路由、freshness 與安全邊界。
- [../../sites/k12ea-ptst/references/page-types-and-entities.md](../../sites/k12ea-ptst/references/page-types-and-entities.md) — 職缺列表、detail 與帳號分支的欄位語義。
- [../../sites/k12ea-ptst/references/coverage.md](../../sites/k12ea-ptst/references/coverage.md) — 本輪覆蓋與證據狀態。
