---
name: k12ea-ptst-public-resources
description: "Use the Codex in-app browser to read and verify public resources in the 國中小代理代課教師人才庫媒合專區: site map, news and announcement details, county recruitment/support measures, job-seeker guidance, laws index, FAQ search/accordion, about page, teaching links, privacy, and information-security pages. Trigger for requests about public PTST guidance or current hr.k12ea.gov.tw/ptst announcements and reference pages."
---

# 國中小代理代課公開資源

## Purpose and entry point

在 Codex 內建瀏覽器中唯讀讀取 `https://hr.k12ea.gov.tw/ptst/` 的公開頁。先確認目前分頁的 URL、title、主要 heading 與登入狀態；使用網站可見 label 導航，外部 YouTube、法規網站、Google Maps、Facebook、LINE 與 PDF 只當作站內提供的連結入口。

## Procedure by user intent

1. `網站導覽`：開啟 `/ptst/Sitemap/Index`，確認第 2 區的 `職缺資訊`、`訊息公告`、`求職說明`、`相關法規`、`常見問題`、`關於本專區`、`操作教學`。把它當候選 inventory，不當作權限證明。
2. `訊息公告`：開啟 `訊息公告`，先確認目前類別 `全部`、`公告訊息`、`活動訊息`、`即時新聞`，再從目前列表選 detail。detail 要核對 heading、日期、發布單位、正文與返回列表；目前結果與日期是動態的。
3. `縣市攬才／支持措施`：開啟 `各縣市教師攬才及支持措施公告區`，從目前可見縣市 link 選擇，核對縣市列表、日期、標題，再開 detail 核對正文。不要把某縣市本輪看到的補助、年資或福利敘述擴張成全國規則。
4. `求職說明`：閱讀頁面自己的說明與流程圖。頁面目前陳述需登入並在 `教師登入` → `履歷表` 完成履歷後才能查詢職缺；首頁／職缺頁的未登入 UI 本輪仍顯示公開職缺列表。遇到這個差異時同時報告兩個證據，不要猜測登入後資料範圍。
5. `相關法規`：讀取站內法規表的標題、分類與連結網址；外部法規內容未經使用者要求不要開啟。回答法律問題時，只引用網站列出的入口或 FAQ／法規頁的明確文字，不自行做個案法律適用。
6. `常見問題`：可在 `關鍵字` 輸入非敏感詞並按 `查詢`；本輪觀察到 URL 可保持不變但問答集合會縮小。點擊 `展開/收合按鈕` 或問題文字後，確認 `[expanded]` 與 A 內容；使用目前分頁的問題與分頁，不猜測 page number。
7. `關於本專區`：用來理解網站自述目的——整合國中小代理、代課、兼任及正式（獨招）公告，並提供教師與學校的互動式配對及縣市支持措施入口。這是網站自己的描述，不是對媒合結果的保證。
8. `操作教學`：確認目前的影片／PDF 連結與標題，例如入口網站介紹、求職者帳號註冊、會員管理、職缺搜尋與應徵、學校端帳號／職缺／媒合管理。外部影片不開啟，除非使用者明確要求；同源 PDF 也先當入口，下載／閱讀需另行確認當次需求。
9. `隱私權宣告`／`資訊安全宣告`：需要解釋資料與安全邊界時讀取第一方頁面；不要保存可識別個資、登入資料、cookie 或頁面中的 live user data。

## Page and field semantics

- News list/detail：列表項目含日期、標題與發布單位；detail 含類型、日期、發布單位、正文、返回列表與外部分享 link。
- Support list/detail：入口依縣市分流；detail 以日期、標題及正文說明地方措施，內容與適用條件可能隨時間更新。
- FAQ：問題以 Q／A accordion 顯示；`+` 代表可展開，展開後以目前頁面文字作為答案來源。
- Laws：表格欄位是編號、標題、法規分類、連結網址；連結大多離站至法務部、教育部法規或 PDF。
- Teaching：表格欄位是編號、標題、連結網址；內容以影片和一份求職者 PDF 手冊為主。

## Safety and limits

- 只做讀取、搜尋、展開、分頁與站內導航。停止於外部分享、註冊條款同意、登入、CAPTCHA、送驗證碼、表單送出、帳號申請、上傳、應徵或媒合動作。
- 公告、支持措施、FAQ、法規清單、影片／PDF 清單與網站更新時間會變動；回答前重新讀取目前頁面。
- 登入後的履歷、我的最愛、完整聯絡資料、學校後台、職缺開立與媒合管理不屬本輪公開資源；未登入時不宣稱這些功能不存在。

## Drift maintenance

- 執行前比較目前 header labels、site map、類別 tabs、FAQ controls、detail heading、第一方說明與外部 link 型態。
- 發現差異時以目前 UI 安全完成工作並記錄頁型、route、舊／新 label、public/authenticated variant、日期及視覺／DOM 證據；不要以 URL 存在或控制 API 成功代替頁面驗證。
- 只有穩定且直接由 UI／第一方說明支持的差異才更新本 skill、site AGENTS 或 reference，之後重跑受影響流程與 `quick_validate.py`。

## References

- [../../sites/k12ea-ptst/AGENTS.md](../../sites/k12ea-ptst/AGENTS.md) — 共用路由、session、freshness 與安全規則。
- [../../sites/k12ea-ptst/references/coverage.md](../../sites/k12ea-ptst/references/coverage.md) — Sitemap、頁型、互動與限制證據。
- [../../sites/k12ea-ptst/references/first-party-guidance.md](../../sites/k12ea-ptst/references/first-party-guidance.md) — 網站自述、FAQ、求職說明、註冊條款與政策頁重點。
