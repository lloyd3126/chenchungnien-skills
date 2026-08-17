---
name: law-moj-cross-government
description: Use the Taiwan Laws & Regulations Database in the built-in browser to search captured legal content from selected central or local government agency sites, preserving the agency scope, keyword conditions, cached-page links, and source limitations.
---

# Law MOJ cross-government search

在跨機關檢索中，以公開關鍵字與明確機關範圍查找機關網站的週期性擷取內容。

## Workflow

1. 開啟 `/CrossGov/CrossGov.aspx`；確認頁面說明資料是從機關法規網站擷取，並辨識中央／地方機關選項。
2. 必填「含有」關鍵字，至少勾選一個中央或地方機關範圍；需要時加入「且含」「或」「不含」。
3. 使用安全、低風險的公開詞做驗證，送出後核對結果 URL、heading、機關名稱、命中片段與「庫存頁面」連結。
4. 報告結果時同時寫出關鍵字、機關範圍、結果頁與資料擷取／來源限制。不要把機關擷取頁面當成當下正式公文或最新法規正文。
5. 若需要原始機關內容，先取得使用者同意再開外部來源；保留全國法規資料庫的結果作為入口證據。

## References

控制項與驗證規則見 [form-controls.md](../../sites/law-moj/references/form-controls.md)，路由與證據分級見 [site-map.md](../../sites/law-moj/references/site-map.md)，跨機關資料模型見 [data-model.md](../../sites/law-moj/references/data-model.md)。

## Safety

- 不在沒有機關範圍的情況下提交模糊全站查詢；必要條件不足時先補齊。
- 不遞迴爬取外部機關網站、不輸入憑證、不送出外部表單。
- 動態命中數、擷取日期與結果標題不可硬編；每次重新讀取。
- 若表單 DOM 已驗證但同分頁截圖重試失敗，明確標示視覺證據不足。
