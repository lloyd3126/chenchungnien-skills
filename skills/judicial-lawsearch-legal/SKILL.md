---
name: judicial-lawsearch-legal
description: Use the Taiwan Judicial legal system in the built-in browser to search court-related laws, interpretations, constitutional decisions, grand-chamber materials, and administrative interpretations, then read a verified result or detail page.
---

# Judicial law and interpretation search

在 `legal.judicial.gov.tw` 的目前瀏覽器分頁完成公開法規或判解函釋查詢，並確認結果頁與詳細內容。

## Workflow

1. 讀 `../../sites/judicial-lawsearch/AGENTS.md`、`data-model.md`、`form-controls.md` 與 `first-party-guidance.md`。
2. 依任務選入口：本院主管或審判相關法規使用 `/FLAW/default.aspx`；判解函釋使用 `/FINT/default.aspx`。先取得 URL、標題／heading、截圖與 DOM。
3. 優先使用一欄式欄位完成低風險公開查詢。法規欄位的 placeholder 是「可輸入法規名稱、舊法規名稱、法規簡稱、全文檢索字詞」；判解函釋與站方示例使用「可輸入法院名稱、裁判案號、案由、全文檢索字詞」。
4. 需要條件組合時，改走對應的 `Default_AD.aspx`，先確認 checkbox、案號、案由與日期欄位，再送出。不要把 FLAW 的條件套到 FINT，兩者的資料態樣不同。
5. 送出後立即確認結果 heading、側欄分類、排序／篩選與 `iframe#iframe-data`。若結果在 iframe，使用 `frameLocator("#iframe-data")` 讀取實際可見的清單與 href。
6. 只從目前清單取得一個代表性詳細 href。若 iframe 內 click 沒有改變頂層 URL，先重新讀取 iframe 狀態；必要時在同一分頁開啟該次觀察到的完整 href，不要自行拼接識別碼。
7. 詳細頁至少確認標題／資料名稱、日期／字號、正文或條文，以及可見的相關法規、附件、歷史或輸出入口。回答時引用實際頁面來源與查詢條件。

## Query syntax

系統說明已驗證的運算元：半形 `+` 為或、`-` 為不含、`&` 為且、`( )` 為組合；依左至右順序比對。除上述符號外不要輸入特殊符號。送出後必須用結果頁驗證語法真的生效。

可用作操作示例的站方公開輸入包括：

- 法規：`民訴法`。
- 判解函釋：`91台上1926` 或 `台東地院101訴225`。

這些只是流程示例，不是固定的結果、筆數或現行法律結論。

## Results and detail routes

- FLAW 結果可按法規名稱／條文內容分組；法規詳細頁提供所有條文、編章節、條文檢索、條號查詢、修正條文與法規沿革。
- FINT 結果可按資料態樣、年度與有效狀態分組；清單包含大法官解釋、精選裁判、決議、行政函釋等可見類別。
- FLAW 詳細頁使用目前結果 href 的 `/FLAW/dat02.aspx` 等路由家族；FINT 詳細頁使用目前結果 href 的 `/FINT/data.aspx` 路由家族。
- 結果 token、筆數、日期、排序與清單正文是動態資料，不要寫入固定規則。

## Boundaries

- 只做公開、唯讀搜尋與閱讀；不登入、不分享、不下載、不儲存、不送出外部表單。
- 法令判解資料不是法律意見。若站方提示資料與主管機關公布文字不同，以主管機關正式公布資料為準。
- 不把 FINT 的收錄範圍或更新週期外推到裁判書系統；裁判書系統說明頁在本次探索中是連線逾時錯誤頁。
- 不能以當前查詢結果推論「全部」資料，也不能只因查無結果就斷定資料不存在；先確認查詢欄位、資料態樣、語法與結果頁狀態。

詳細欄位與官方邊界見 [form-controls.md](../../sites/judicial-lawsearch/references/form-controls.md) 與 [first-party-guidance.md](../../sites/judicial-lawsearch/references/first-party-guidance.md)。
