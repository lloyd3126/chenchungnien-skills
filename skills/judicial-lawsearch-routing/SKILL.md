---
name: judicial-lawsearch-routing
description: Use the Taiwan Judicial legal-search portal in the built-in browser to route a request to the law, interpretation, judgment, simplified-case, exclusion-judgment, or public-summons subsystem, including desktop/mobile routing. Use when the user asks where or how to search on lawsearch.judicial.gov.tw.
---

# Judicial legal-search routing

在 `lawsearch.judicial.gov.tw` 的目前瀏覽器分頁判斷正確子系統，並把使用者帶到可驗證的公開查詢入口。

## Workflow

1. 先讀 `../../sites/judicial-lawsearch/AGENTS.md` 與 `references/site-map.md`、`references/form-controls.md`。
2. 取得目前分頁 URL、標題／heading、截圖與 DOM。若使用者要求行動版，使用 `/LAW_Mobile_SEARCH/default.aspx` 與其展開後實際 href；否則使用桌面版首頁。
3. 依意圖分流：法規走 `legal.judicial.gov.tw/FLAW`，判解函釋走 `legal.judicial.gov.tw/FINT`，裁判書與三種特殊程序走 `judgment.judicial.gov.tw/FJUD`。
4. 只使用首頁、網站導覽或當前頁面看得到的連結。導覽後立即重新確認 URL、標題／heading、截圖與 DOM。
5. 若任務含查詢條件，交給 `$judicial-lawsearch-legal` 或 `$judicial-lawsearch-judgments`；不要在 routing skill 內重複發明表單流程。
6. 回答時提供選用的子系統、實際入口與未探索／未驗證的限制；不要把入口頁的動態最新內容當成搜尋結果。

## Route map

- 法規：`https://legal.judicial.gov.tw/FLAW/default.aspx`
- 判解函釋：`https://legal.judicial.gov.tw/FINT/default.aspx`
- 裁判書：`https://judgment.judicial.gov.tw/FJUD/default.aspx`
- 簡易案件：`https://judgment.judicial.gov.tw/FJUD/defaulte.aspx`
- 除權判決：`https://judgment.judicial.gov.tw/FJUD/defaultk.aspx?ty=E`
- 公示催告裁定：`https://judgment.judicial.gov.tw/FJUD/defaultk.aspx?ty=V`

## Boundaries

- 只做公開、唯讀的頁面導覽；不登入、不輸入憑證、不儲存、不分享、不下載、不提交外部表單。
- 不要把 `law.moj.gov.tw`、`terms.judicial.gov.tw` 或 `opendata.judicial.gov.tw` 當成已完成探索的本套件路徑。
- 不猜測查詢 token、法院代碼、資料 ID 或結果 URL；只能使用目前 UI 提供的 href。
- 每次互動後都要有狀態檢查。若截圖或控制 API 失敗，保留錯誤分類並重試同一分頁一次，再決定是否為 client-blocked、網站錯誤頁或未驗證。

詳細路由、行動版差異與證據狀態見 [site-map.md](../../sites/judicial-lawsearch/references/site-map.md)。
