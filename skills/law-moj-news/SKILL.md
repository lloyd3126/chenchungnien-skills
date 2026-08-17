---
name: law-moj-news
description: Use the Taiwan Laws & Regulations Database in the built-in browser to browse and filter the latest-year legal change notices, including laws, regulations, administrative rules, local regulations, and draft regulations, then open a public notice detail.
---

# Law MOJ latest news

查找全國法規資料庫最近一年的法規異動訊息，保留分類、日期、摘要與詳情連結。

## Workflow

1. 開啟 `/News/NewsList.aspx`，確認頁面 heading 說明時間範圍是最近一年。
2. 依意圖選「全部」「法律」「法規命令」「行政規則」「地方法規」或「法規草案」。分類通常以 URL query 表示；提交後核對 heading、選取狀態與表格內容。
3. 讀取表格的日期、類別、摘要與 `NewsDetail.aspx?msgid=<ID>` 連結；需要更多內容時使用實際 `msgid` 開詳情。
4. 使用每頁 20／40／60 與分頁查找更多項目，並記錄當下查詢條件。不要硬編總筆數或把當天清單當成永久資料。
5. 若訊息連往公報或主管機關，先說明那是來源導覽；不要僅以新聞摘要代替正式法規文本。

## References

入口與分類見 [site-map.md](../../sites/law-moj/references/site-map.md)，更新週期與官方範圍見 [first-party-guidance.md](../../sites/law-moj/references/first-party-guidance.md)。

## Boundaries

- 只做公開讀取與分類／分頁；不訂閱電子報、不送出回饋、不登入。
- 每次導覽都取得同一分頁的 URL、標題／heading、截圖與 DOM；若視覺重試失敗，回報 DOM 證據限制。
- 不把最新訊息解讀成法律意見；若使用者需要正文，轉到正式法規或主管機關來源並重新核對。
