---
name: adl-public-resources
description: "Use the Codex in-app browser to read and verify Taiwan Ministry of Education Adaptive Learning Network (教育部因材網) public resources: homepage navigation, latest news, activities, announcement details, operation manuals, FAQ categories, account-application guidance, and sitemap. Trigger whenever a user asks about adl.edu.tw public announcements, activities, manuals, FAQs, account routes, site navigation, or current public content."
---

# 教育部因材網公開資源

## Purpose and entry point

在 Codex 內建瀏覽器中唯讀探索與驗證 `https://adl.edu.tw/` 的公開內容。從目前可見分頁開始，保留同一分頁與 session；若目前畫面顯示登入後應用程式，也先確認公開入口是否仍可由可見 UI 導航。

## Procedure

1. 讀取目前分頁的 URL、title、主要 heading 與 screenshot，確認目前確實是教育部因材網；不要只依 URL。
2. 依意圖使用可見 label 導航：
   - 最新消息 → 首頁的 `最新消息`／`檢視全部消息` → 讀列表；分頁只點擊目前可見頁碼。
   - 某則公告 → 從當前列表點擊目標 → detail 頁核對標題、`更新時間`、正文與外連。
   - 最新活動 → `更多活動` → 核對日期區間、標題與目標連結；離站前先告知並重新確認目的地。
   - 操作方法 → `操作手冊` → 依角色／功能 heading 找第一方 PDF、文件或影片入口。
   - FAQ／故障排除 → `常見問題` → 使用 `全部`、`帳號篇`、`校管操作篇`、`教師操作篇`、`學習扶助篇` 或 `其他`；點擊後確認 active 狀態與 heading。
   - 帳號申請 → `研習與帳號` → `帳號申請` → 展開對應角色 accordion，僅讀取說明。
   - 網站導覽 → 頁尾 `網站導覽` → 讀取可見站內入口；需要 robots 時只在同一分頁開啟同源路徑並按畫面判定。
3. 每次導航後用目前分頁的 screenshot 或 DOM 確認目標已真的打開；若控制回報錯誤，仍先視覺檢查，再在同一分頁重試一次。
4. 回報即時內容時記錄當次頁面、查詢／分頁狀態與頁面顯示時間；不要把現行標題、結果數量或活動內容硬編碼進長期 instructions。

## Page and field semantics

- News list：日期、標題、detail link、分頁；`Id` 必須從當前可見 link 取得。
- News detail：標題、更新時間、正文段落與可能的外部連結。
- Activity list：活動日期區間、標題、站內 detail 或離站目標。
- Operation manual：角色／功能分區與文件／影片連結；連結存在不代表外部文件本輪已讀取。
- FAQ：分類按鈕會改變 active 狀態、分類 heading 與問答集合；先確認分類再解讀答案。
- Account application：角色 accordion 可能要求證明文件、線上表單或寄信；只讀取，不替使用者填寫。

## Safety and limits

- 不登入、不輸入密碼／OTP、不上傳證明文件、不送出帳號申請、不寄信、不回報問題、不接受 CAPTCHA，也不把可見個人資料寫入 references。
- `Google Drive`、`YouTube`、`Google Sites`、Facebook、教育雲等離站連結只能依使用者明確需求開啟；在本技能的公開盤點中只驗證到連結出現在站內頁面。
- Sitemap 是導覽加速器，不是完整功能或權限證明；`robots.txt` 的缺失／404 也不能推論功能不存在。

## Drift maintenance

- 使用前比較目前 header／footer label、路由、heading、selected category 與第一方說明。
- 若 UI 變更，先以目前可見 UI 安全完成工作並記錄舊／新行為、頁型、日期與證據；只有穩定且可重新驗證的差異才更新 owning AGENTS、skill 或 reference。
- 更新後重新跑相應列表／detail／FAQ 唯讀流程與 `quick_validate.py`；不要保存動態內容、帳號資料、cookie 或 token。

## References

- [../../sites/adl/AGENTS.md](../../sites/adl/AGENTS.md) — 全站 session、導覽、freshness 與安全規則。
- [../../sites/adl/references/coverage.md](../../sites/adl/references/coverage.md) — 已探索頁型與證據來源。
- [../../sites/adl/references/page-types-and-entities.md](../../sites/adl/references/page-types-and-entities.md) — 公開頁型與 entity 語義。
