---
name: adl-teacher-workflows
description: "Use the Codex in-app browser for read-only 教育部因材網 teacher workflows: authenticated dashboard routing, task progress and diagnostic data, class and account lookup, learning-support assessment, course overview, and AI companion entry points. Trigger whenever a user asks about 指派任務、任務儀表板、學生任務進度、班級／帳號、學習扶助、課程總覽 or AI 學伴 on adl.edu.tw. For creating, assigning, importing, editing, or sending anything, stop at the final side-effect boundary and request action-time confirmation."
---

# 因材網教師工作流

## Purpose and entry point

在 Codex 內建瀏覽器中使用已登入的因材網教師介面，優先支援唯讀查詢與路由。開始時必須以目前分頁視覺確認 app bar 或其他明確的登入後 UI；初始探索曾確認 `操作介紹`、`課程總覽`、`ＡＩ學伴`、`指派任務`、`登出`、待辦／行事曆、公告與任務儀表板。

如果目前畫面只有公開首頁、登入入口或受保護路由被導回首頁，不要猜測已登入，也不要代填帳密；請使用者在同一內建瀏覽器分頁手動登入後再繼續。重新載入後仍需確認頁面 heading、app bar、當前學期與資料 scope。

## Procedure

1. 保存目前分頁的 URL、title、screenshot 與 DOM；確認是因材網教師工作區，而非同站公開首頁。
2. 依意圖走當前可見入口：
   - 任務進度／診斷 → `任務儀表板` → 當前任務卡 → 詳情／數據 → 必要時診斷報告。
   - 建立／指派任務 → 頂部 `指派任務` 或 dashboard `+ 指派任務` → 任務類型 → 內容 → 名稱／時間／對象 → 設定預覽。
   - 班級／帳號查詢 → 班級管理區塊的 `帳號`／`帳號管理` → 使用目前 UI 的查詢控制。
   - 學習扶助 → `學習扶助` → `科技化評量` 或 `學習扶助編班` → 依當前 UI 選擇範圍後查詢。
   - 課程或 AI 學伴 → 由目前 app bar 的 `課程總覽`／`ＡＩ學伴` 進入；若內容、權限或 label 不同，記錄差異，不要猜測。
3. 每次點擊、篩選或切換後，先確認目前頁面 heading、selected／active 控制與實際結果，再進下一步。
4. 回報任務、學生或學扶資料時，重新讀取當次結果與 scope；不把學生姓名、帳號、身分證後五碼、診斷結果、任務數字或個人工作區值寫入長期檔案。

### Observed-link fallback

若同頁 modal／選單中的點擊因頁面自動跳轉、session 不穩定或控制器失去元素而無法完成，但 DOM／accessibility snapshot 已讀到該可見項目的實際 `href`，可在同一分頁直接使用該已觀察到的完整連結。不得自行猜測、改寫或拼接 query 參數；開啟後仍須重新擷取 URL、title、screenshot 與 DOM，確認到達的 heading、scope 與下一層控制項。此 fallback 僅適用於唯讀導覽，遇到建立、指派、儲存、送出或其他副作用連結時仍停在確認邊界。

因材網的課程總覽特例：dashboard HTML 會預先包含隱藏的 `.course-main.materialList`（位於 tooltip／overlay 容器），不一定要等 modal 開啟才出現。科目連結可從 `.course-main.materialList a` 讀取；國小清單的年級群組位於 `#elementaryList dl.menu-item`。這些連結在隱藏狀態下可能不被可見元素 locator 找到；若正常點擊無法穩定展開，應使用 DOM 已觀察到的完整 `href` 在同一分頁導覽，並重新驗證結果。

若目前 session 會在 F12、DevTools、頁面 `evaluate()` 或其他注入式檢查後立即導回公開首頁，將其視為疑似防除錯／防自動化或受保護路由狀態，不再反覆執行頁面內 JavaScript。改用已觀察到的完整唯讀 `href` 在同一分頁導覽，並只用截圖確認是否停留在教材頁與單元頁；不要因此推論網站本身不能執行一般 JavaScript。

## Confirmed read-only workflows

### 查看任務進度

1. 開啟 `任務儀表板`。
2. 由當前任務卡找詳情箭頭或等價控制。
3. 開啟 `查看試題及數據` 或等價入口。
4. 讀取任務完成率、節點教材完成率、觀看／測驗次數、節點狀態、答對率；確認當前是 `顯示任務內容` 還是 `顯示歷史紀錄`。
5. 診斷類型任務可再開啟學生診斷報告，但要確認學生 identity、任務與測驗範圍。

### 查帳號與班級

使用班級管理的 `帳號`／`帳號管理`，依目前可見的「一般查詢」或「姓名查詢」讀取年級、班級、科目、帳號狀態與權限 scope。`科任班級設定` 可能需要校管先開權限；不可把非任教班級當成教師可編輯範圍。

### 查學習扶助

進入 `科技化評量` 後，依當前 UI 設定班級類型、年級、班級、學生類型並查詢；再依領域讀取節點／試卷、測驗模式與精熟狀態。學生帳號與科技化評量可能以身分證／居留證後五碼綁定，這是敏感資料，不要複製或傳送。

## Side-effect boundaries

- `建立`、`確定指派`、`送出修改`、`儲存`、`新增班級`、`匯入使用者`、`帳號轉入／轉出`、`停用`、`刪除`、代幣發放／兌換、邀請家長、上傳檔案與 AI 對話送出，都可能改變資料或傳送資料。
- 即使使用者先說「幫我做」，也在瀏覽器最後一步再次說明目的地、對象、內容與即將發生的副作用，取得當下確認後才提交。
- 若只是幫使用者找流程或查看結果，停在副作用按鈕前，不要代替使用者按下去。

## Page and field semantics

- `Task`：任務類型、內容、名稱、時間、對象、完成／觀看設定，以及完成率、教材完成率、答對率、節點狀態與診斷報告。
- `Class`／`Account`：學期、年級、班級、科目、教師／導師關係、學生帳號狀態；值是動態且可能是私人資料。
- `Learning-support assessment`：測驗、領域、班級範圍、學生類型、節點／試卷、測驗模式與精熟／未精熟狀態。
- 知識結構教材完成率與診斷精熟度不是同一指標；需要精熟結論時，找診斷任務或診斷報告的第一方說明。

## Drift maintenance

- 每次使用前對照目前 app bar、側欄、任務卡、學期／班級 scope、label、權限與 `sites/adl/references/teacher-workflows.md`。
- 若受保護路由在目前 session 被導回首頁、出現登入牆或權限不同，標記為目前 session 的 blocked／partial，不把它寫成網站不存在。
- 穩定差異要在同一分頁安全重跑受影響的唯讀流程後，才更新 owning AGENTS、skill 或 reference；修改後執行 `quick_validate.py`。

## References

- [../../sites/adl/AGENTS.md](../../sites/adl/AGENTS.md) — 全站 session、導覽、freshness 與安全規則。
- [../../sites/adl/references/teacher-workflows.md](../../sites/adl/references/teacher-workflows.md) — 任務、班級、帳號與學扶的第一方工作流。
- [../../sites/adl/references/page-types-and-entities.md](../../sites/adl/references/page-types-and-entities.md) — Task、Class／Account 與學扶資料模型。
- [../../sites/adl/references/coverage.md](../../sites/adl/references/coverage.md) — 初始教師 dashboard 的證據與受保護缺口。
