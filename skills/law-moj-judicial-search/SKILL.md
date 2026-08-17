---
name: law-moj-judicial-search
description: Use the Taiwan Laws & Regulations Database in the built-in browser to search Constitutional Court judgments, Grand Justices interpretations, and Supreme Court civil, criminal, or administrative precedents, then verify a public decision's metadata, holding, related laws, and source links.
---

# Law MOJ judicial search

在公開的司法解釋與判例區搜尋、排序並核對司法資料；不要把摘要或智慧查找結果當成裁判全文。

## Workflow

1. 開啟 `/Law/LawSearchJudge.aspx`，先依使用者指定的司法類別篩選：憲法法庭裁判（新制）、大法官解釋（舊制）、最高法院民事判例、最高法院刑事判例或最高行政法院判例。
2. 讀取同一分頁的 URL、標題／heading、截圖與 DOM。需要排序時使用頁面提供的日期排序，並確認清單順序真的變更。
3. 從清單取得完整的 `ty`、`JC`、`JNO`、`JYEAR`、`JCASE` 等實際參數，再開啟 `/LawClass/ExContent.aspx?...`；不要自行拼接司法識別碼。
4. 在單筆頁核對案號、日期、來源、案由、主文、相關法條與外部司法院連結。若只得到 DOM 而截圖重試失敗，明確報告證據限制。
5. 回答時分開寫「網站呈現的資料」與「對使用者個案的法律適用」；後者不由本 skill 推論。

## Evidence and routing

主要入口是 `/Law/LawSearchJudge.aspx`，單筆路由是 `/LawClass/ExContent.aspx?...`。分類、資料模型與外部來源邊界見 [site-map.md](../../sites/law-moj/references/site-map.md) 與 [data-model.md](../../sites/law-moj/references/data-model.md)。

司法資料可能連到司法院憲法法庭或其他外部官方頁面；只有使用者明確要求時才離開目前網站範圍，並保留原始資料庫連結。

## Safety

- 不登入、不輸入憑證、不送出會員或回饋表單。
- 不把「主文」誤稱為完整理由，也不把相關法條連結誤稱為已完成法律分析。
- 不固定記錄目前筆數、日期或最新案號；每次任務重新讀取。
