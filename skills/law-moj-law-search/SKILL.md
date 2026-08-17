---
name: law-moj-law-search
description: Use the Taiwan Laws & Regulations Database in the built-in browser to find central laws, treaties, cross-strait agreements, full law text, article numbers, article keywords, histories, chapters, and combined-search results. Use when a user asks to locate or verify public legal materials on law.moj.gov.tw.
---

# Law MOJ law search

在 `https://law.moj.gov.tw/` 的目前瀏覽器分頁完成公開法規查詢，並把查詢條件與結果來源交代清楚。

## Workflow

1. 先判斷意圖：指定法規或條文走中央法規；指定跨資料類別、日期或文號走綜合查詢；指定條約或兩岸協議走各自專區。
2. 導覽到入口後讀取同一分頁的 URL、標題／heading、截圖與 DOM。不要因按鈕點擊沒有錯誤就假設頁面已變更。
3. 從實際清單連結取得 `pcode`；不要猜測法規識別碼。再使用全文、編章節、條號、條文或沿革入口。
4. 條號查詢使用逗號、`-` 範圍與 `.` 之條語法，例如 `1,11-13,35,756.1`；送出後確認結果 URL、heading 與每個條號。
5. 條文檢索把核心詞放在「含有」，需要時加入「且含」「或」「不含」；確認結果有關鍵字高亮與完整上下文。
6. 綜合查詢先勾選資料類別，再填條件；結果頁確認法規名稱／法條內容分頁與實際命中項目，不要固定引用動態筆數。
7. 回答時保留入口、查詢詞、資料類別、結果頁與資料庫的官方限制；法律問題不要提供未經核實的個案結論。

## Routing

- 中央法規：`/Law/LawSearchLaw.aspx`
- 全文：`/LawClass/LawAll.aspx?pcode=<PCODE>`
- 編章節：`/LawClass/LawAllPara.aspx?pcode=<PCODE>`
- 條號：`/LawClass/LawSearchCNKey.aspx?BTNType=NO&pcode=<PCODE>`
- 條文：`/LawClass/LawSearchCNKey.aspx?BTNType=CON&pcode=<PCODE>`
- 沿革：`/LawClass/LawHistory.aspx?pcode=<PCODE>`
- 條約：`/Law/LawSearchAgree.aspx`
- 兩岸協議：`/Law/LawSearchTwo.aspx`
- 綜合查詢：`/Law/LawSearchAll.aspx`

詳細資料模型與表單規則見 [data-model.md](../../sites/law-moj/references/data-model.md) 與 [form-controls.md](../../sites/law-moj/references/form-controls.md)；權威範圍見 [first-party-guidance.md](../../sites/law-moj/references/first-party-guidance.md)。

## Boundaries

- 只做公開、可重做的讀取與搜尋；不要登入、儲存會員收藏、送出外部表單或以 API 取代瀏覽器驗證。
- PDF、友善列印、外部司法院／機關連結只有在使用者要求且能確認目前分頁仍在預期頁面時才開啟。
- 動態結果、筆數、更新日期與資料截止日必須重新讀取；若截圖失敗，標示 DOM 已驗證但視覺重試未成功。
