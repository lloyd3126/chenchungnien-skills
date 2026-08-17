---
name: judicial-lawsearch-judgments
description: Use the Taiwan Judicial judgment system in the built-in browser to search judgments, simplified cases, exclusion judgments, and public-summons rulings by text, court, case number, date, subject, or full text, then read a verified detail page.
---

# Judicial judgment search

在 `judgment.judicial.gov.tw` 的目前瀏覽器分頁完成公開裁判書或特殊程序查詢，並確認結果清單與詳細頁。

## Workflow

1. 讀 `../../sites/judicial-lawsearch/AGENTS.md`、`data-model.md`、`form-controls.md` 與 `first-party-guidance.md`。
2. 依使用者意圖選入口：一般裁判書 `/FJUD/default.aspx`、簡易案件 `/FJUD/defaulte.aspx`、除權判決 `/FJUD/defaultk.aspx?ty=E`、公示催告裁定 `/FJUD/defaultk.aspx?ty=V`。先確認 URL、標題／heading、截圖與 DOM。
3. 公開簡單查詢使用 `textbox` `檢索字詞` 與 `button` `送出查詢`。頁面提供的安全格式示例包括 `105訴123` 與 `台北地院105訴123`；若使用者提供自己的條件，原樣保留並記錄。
4. 需要法院、案件類別、案號、日期、案由、主文、全文或大小條件時，改走 `/FJUD/Default_AD.aspx`；不要以一欄式語法取代明確的進階欄位。
5. 送出後確認結果 heading、依法院／年度／案件類別／裁判類別的側欄、排序、頁數與 `iframe#iframe-data`。筆數與頁數只作本次狀態，不要固化。
6. 若清單在 iframe，使用 `frameLocator("#iframe-data")` 取得目前可見的裁判 href。只開啟一個代表性結果，必要時在同一分頁直接開啟該完整 href；不要猜測複合 `id`。
7. 詳細頁至少確認裁判字號、日期、案由與正文。需要時閱讀主文、事實及理由，並記錄可見的歷審裁判、名詞查詢、列印或 PDF 入口；不要因存在 PDF link 就自動下載。

## Special procedures

- 簡易案件頁面明示：若本單元查無簡易案件裁判書，可回到裁判書查詢單元；只有在這個頁面提示後才把它當成有限 fallback，不要把兩種結果集直接混合。
- 除權判決與公示催告裁定使用 `defaultk.aspx` 的 `ty=E`／`ty=V` 桌面路由，應維持各自的資料集與結果頁。
- 行動版選單的特殊程序使用另一組 `ty=e`／`ty=ke`／`ty=kv` href；使用行動版時以選單實際 href 為準。

## Results and detail model

一般裁判結果清單可見裁判法院、裁判字號、裁判日期、裁判案由、內容大小、摘要、分頁與排序。詳細頁可見裁判 metadata、正文、名詞服務、PDF／列印、分享與歷審裁判。

詳細頁路由形狀是 `/FJUD/data.aspx?ty=JD&id=<observed-id>&ot=in`；`<observed-id>` 只能取自當前結果清單的 href。法院代碼、年度、字別與日期不要自行拼接。

## Boundaries

- 只做公開、唯讀搜尋與閱讀；不登入、不分享、不下載、不儲存、不送出外部表單。
- 裁判書正文可能含個人、案件或敏感法律資訊；只閱讀使用者任務所需的最小範圍，回答時避免不必要重述個資。
- `/FJUD/readme.aspx` 在本次探索中兩次導向「連線逾時」系統訊息頁，因此不要宣稱未從查詢 UI 驗證的資料收錄範圍或更新週期。
- 動態最新清單、筆數、頁碼與裁判正文不可用作固定測試期待；成功條件是當次頁面的 heading、清單與詳細頁實際可見內容。

詳細控制項見 [form-controls.md](../../sites/judicial-lawsearch/references/form-controls.md)，路由與驗證狀態見 [site-map.md](../../sites/judicial-lawsearch/references/site-map.md)。
