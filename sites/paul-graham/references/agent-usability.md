# Agent usability test

以下測試只檢查 artifacts 是否能導向正確頁型，不把本輪 live 結果寫成答案。

| Scenario | Expected route | Required verification | Result |
| --- | --- | --- | --- |
| 「找 Paul Graham 的 How to Do Great Work 並讀摘要」 | `$paul-graham-essay-research` → `/articles.html` → visible essay link → `greatwork.html` | title、date（若顯示）、intro/body、current URL | pass：skill 指定從 Essays 或 Index 找到可見 href，並要求回讀頁面欄位 |
| 「找一篇標題不確定的文章」 | `$paul-graham-essay-research` → `/ind.html` → `Prev/Next` → visible title | 字母段落、href、目的頁 title；不依猜測 slug | pass：skill 明確禁止猜 URL，要求以 Index 可見連結路由 |
| 「查看 Hackers & Painters 書籍資料」 | `$paul-graham-reference-research` → `/books.html` → `/hackpaint.html` | book title、description、publisher/year/pages/ISBN（若可見）、external links | pass：skill 將 hub 與 detail 分開，並設定外部購買連結停點 |
| 「了解 Bel 的 guide/source/examples 入口」 | `$paul-graham-reference-research` → `/bel.html` → visible resource links | page title、date、連結用途；不保存 CDN query/token | pass：skill 與 interaction reference 都有參數化資源規則 |
| 「整理 FAQ、RAQ 或 Quotes」 | `$paul-graham-reference-research` → `/faq.html`／`/raq.html`／`/quo.html` | title、section/list entry、當次內容；不虛構搜尋或篩選 | pass：skill 明確列出 hub 路由與 freshness |

未測試或 intentionally untested：外部 Y Combinator／Amazon／社群／論壇／feed 內容、任何寄信／購買／申請／互動，以及 sitemap XML 解析（本輪沒有可用 sitemap artifact）。
