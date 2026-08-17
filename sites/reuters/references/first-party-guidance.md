# Reuters 第一方說明與限制

## Source context

- Reuters article 會提供作者、published／updated time、正文、`Our Standards` 與 `The Thomson Reuters Trust Principles` 連結；在研究文章時將這些作為 provenance context。
- Markets 頁與表格把 quote data 連到 `LSEG`，並顯示資料至少延遲 15 分鐘。需要目前行情時重新讀取；不要用舊結果推導現價。
- Footer 的 `Data Disclosure and Sources`、`Terms & Conditions`、`Corrections`、`See here for a list of exchanges and delays` 是第一方說明入口；若任務涉及資料定義、延遲或更正，優先開啟這些頁面。

## Content classification

- `Exclusive`、`ANALYSIS`、`Reuters Open Interest`、`Breakingviews`、`Sponsored Content` 與 `This content is not reviewed by Reuters journalists` 代表內容來源／編採狀態差異，報告時要保留 label。
- Article 的 video、gallery、newsletter CTA、related links 與 licensing link 是 article 的附加關聯資源，不等於正文的一部分。
- `Save`、`Follow`、`Subscribe`、`Sign up`、`Purchase Licensing Rights` 不是單純讀取；除非使用者明確要求並在 action-time 確認邊界，維持未操作。

## Access and freshness

- 未登入首頁與文章可能仍可讀取，但 `My News`、帳戶、個人化、訂閱與部分內容可能需要登入／註冊／方案。遇到 gate 時記錄 exact label 與 visible explanation，不繞過。
- 對文章、搜尋結果、行情、排行榜、時間、作者頁內容與可見數量，回報 observation time、query／filters／region；不把 live data 寫進持久 skill。
- 目前頁面若和這裡描述的 label、route、control、access 或第一方說明不同，按目前 UI 安全適應並更新 owning reference；不以常識補全未驗證欄位。
