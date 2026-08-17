# SEC 一方說明與使用限制

需要精確或最新規則時，重新在 Codex 內建瀏覽器開啟原頁。下列是本輪從 SEC 一方頁面取得、適合重用的穩定語意；不是法律、會計或投資意見。

## EDGAR public search

- `Search Filings` 將 Company Search、Full Text Search、Latest Filings、CIK Lookup、SIC Codes、EDGAR APIs 與 Search Assistance 分開呈現。
- Full Text Search 的 landing page 說明可搜尋 2001 年以來電子 filings 的全文；進階控制可按 keyword、company/person/ticker/CIK、filing category、日期與地點縮小結果。搜尋結果要重新核對 query、filters 與結果表，不要把一個查詢樣本寫成固定結果。
- Latest Filings 頁說明其列表面向當前官方 filing date 的最新提交，並提供公司、CIK、form type 與 ownership 篩選；日期與結果內容會變動。
- CIK Lookup 頁說明 CIK 用來辨識向 SEC 提交揭露的公司、基金或個人；名稱可能以不同順序或縮寫出現，搜尋結果超過 100 筆時會截斷，因此應縮窄關鍵字。

## Filing detail and archive recovery

- Filing Detail 以 `Form`、`SEC Accession No.`、`Filing Date`、`Accepted`、`Documents` 與 `Document Format Files` table 組成。可由 primary HTML/XML 或 complete submission text file 進入內容。
- SEC Webmaster FAQ 說明：若只有 Archive component document URL，可從 URL 中的 accession number 建立對應 Filing Detail index；將 accession 中的數字依 SEC 規則加上連字號，並以 `-index.htm` 結尾。實作時優先以頁面上可見的 Filing Detail／Company Search link 驗證，不要只依字串猜路由。
- Filing Detail 可能同時列出 Filer 與 Subject；不要因結果卡片只顯示其中一個名稱就誤判 filing 的實際角色。

## EDGAR APIs and data

SEC 的 EDGAR API 說明頁指出：

- `data.sec.gov` 提供 JSON REST APIs；該頁說明公開 submissions 與 XBRL 資料 API 不需要 authentication 或 API key。
- `data.sec.gov/submissions/CIK##########.json` 使用含前導零的 10 位 CIK，提供 entity metadata 與近期 filing history；有更多歷史時會連到分段 JSON files。
- XBRL API 分為 `companyconcept`（單一公司／概念）、`companyfacts`（單一公司所有 concepts）與 `frames`（按期間聚合的 fact）。units、period、taxonomy 與 company context 必須一起解讀。
- API JSON 會隨 filings disseminated 更新；bulk ZIP 是較適合大量資料的 nightly delivery。不要以頁面中看到的現值推導最新結果。
- SEC API 頁面同時說明 `data.sec.gov` 不支援 CORS；程式化使用仍須遵守 SEC Privacy and Security Policy 與 Developer FAQ。

## Fair access

SEC Developer Resources 說明要只下載需要的資料、降低 server load，並列出每位使用者合計每秒不超過 10 個 requests 的公平存取限制；SEC 可阻擋過量請求，也不允許未分類 bot 或不符合政策的自動爬取。未來若使用者另行授權程式化取得，先讀目前 Developer FAQ，設計節流、明確 user-agent 與必要範圍；本網站探索 skill 預設仍只用內建瀏覽器 UI。

## Rulemaking and comments

- `Rulemaking Activity` 提供文字搜尋、Rulemaking Status、Division／Office 與 Year 篩選；狀態至少包括 `Final`、`Interim Final`、`Proposed`、`Interpretive`、`Concept`。篩選後要核對結果標題、rule identifier／detail link 與目前篩選器。
- `Submit Public Comments` 對每個 proposal／request 可能同時提供官方 notice／PDF、`Submit a Comment` 與 `View Comments Received`。讀取 notice 或 comments 是公開查詢；送出 comment 會傳送內容，永遠停在送出前並取得動作當下確認。

## Freshness

`Last Reviewed or Updated` 日期、filing rows、新聞標題、rule status、comment period、API JSON 與 bulk archive 都可能改變。永久 references 只保留定義、路由、欄位與更新規則；需要答案時重新開頁、重設查詢、記錄抓取時間與來源頁。
