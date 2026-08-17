# 國立公共資訊圖書館（NLPI）網站操作指引

## Scope

這份指引適用於透過 Codex 內建瀏覽器操作 `https://www.nlpi.edu.tw/`。網站提供館藏／借閱服務、數位資源、活動資訊、影音、公告與會員中心。本輪以目前開啟的會員中心為起點，完成公開首頁、網站導覽、搜尋、活動日曆、借還書說明與數位資源介紹的代表性探索。

目前可見 session 已登入會員中心；登入後頁面是另一個網站變體，未來若 session 狀態改變，必須重新核對會員入口與資料範圍。不要把會員姓名、借閱紀錄、活動紀錄或其他個人資料寫入 reusable guidance。

## Sitemap-assisted inventory

- `/SiteMap`：由首頁主選單的「網站導覽」開啟；在目前分頁以 DOM 與畫面確認為 `UI-verified`。它列出 1.關於我們、2.我要借書、3.到館資訊、4.數位館藏、5.各項服務、6.活動訊息、7.會員中心、8.影音管理、9.其他等階層，適合作為站內路由 inventory。
- `/robots.txt`、`/sitemap.xml`、`/sitemap_index.xml`：在同一個目前分頁嘗試並各自重試後仍由內建瀏覽器回報 `ERR_BLOCKED_BY_CLIENT`；畫面仍停留在原頁。狀態是 `client-blocked`，證據是 `current-tab visual` 加 `automation/control error`，不能推論資源不存在或內容為空。
- Sitemap／網站導覽只提供候選路由。實際 label、頁面結構、權限與控制項仍須在目前 UI 重新確認；不要把整份動態 URL 清單複製到 skills。

## Global routing

- 搜尋國資圖網站頁面、公告、服務或主題 → `$nlpi-site-search` → `/Search` 或 `/AdvancedSearch`。
- 依日期、季節、時間、分眾、主題或關鍵字找活動，或閱讀活動詳情 → `$nlpi-activity-search` → `/ActivityInfo/recap` → `/ActivityInfo/recap/Detail/<id>`。
- 查看登入後借閱／預約摘要、會員中心入口與跨站服務卡 → `$nlpi-member-center` → `/Member/myipac`。
- 理解數位資源入口網、電子書服務平台、一證通與課程申請路由 → `$nlpi-digital-resources` → `/StaticPage/resources-intro` 的頁籤與可見連結。
- 借閱規則、續借限制與特殊館藏 → 先讀 [first-party-guidance.md](references/first-party-guidance.md)，再以站上說明頁重新確認。

## Navigation

- 首頁 `/`：首頁輪播、AI 找書／關鍵字查詢、精選圖書、活動、公告、影音、數位資源與讀者服務入口。
- 主選單「選單按鈕」：可見全站搜尋、會員登入／登出、快速入口、`回首頁`、`網站導覽` 與 `English`。展開或關閉選單是安全互動。
- 「網站導覽」`/SiteMap`：一方階層式 route map；以此找代表性頁面，不要窮舉每個內容 URL。
- 全站搜尋 `/Search`：關鍵字欄、`送出搜尋`、`進階搜尋`；結果由 Google 自訂搜尋嵌入，可能出現延遲或 CSP 訊息。
- 活動日曆 `/ActivityInfo/recap`：年份／季度、時間範圍、關鍵字、進階篩選、分頁與活動詳情。
- 會員中心 `/member`：登入 session 下導向 `/Member/myipac`；顯示服務卡、借閱／預約 tab 與會員記錄入口。
- 數位資源介紹 `/StaticPage/resources-intro`：說明公共圖書館數位資源入口網、電子書服務平台與相關頁籤。

## Operating rules

- 只使用 Codex 內建瀏覽器；不要改用 Chrome、外部瀏覽器、API、CLI、web search、爬蟲、cookies、local storage、profile 或 session 檔案。
- 綁定使用者目前可見的既有分頁；不要為探索建立或切換臨時分頁。會員中心的服務卡以 `target="_blank"`、`rel="noopener noreferrer"` 開啟跨站入口，除非使用者另有明確請求，探索時只記錄入口，不切換到外部平台。
- 目前 session 若已在畫面中明確顯示登入，才可安全閱讀會員頁；不要代填密碼、OTP 或其他敏感資料，也不要把登入後個人資料寫入 references。
- 預設只做唯讀、可逆互動：導覽、搜尋、篩選、分頁、開啟／關閉進階篩選、閱讀說明。`登出`、活動「報名」、外部表單、儲存、借閱／續借／預約確認與任何帳戶變更都是停止邊界。
- 活動詳情可含外部報名連結、Google 活動行事曆連結與第三方教學平台；不要在探索時跟隨或送出。
- 站上活動、搜尋結果、結果筆數、日期、排名、會員記錄與服務可用性都是動態資料；每次任務重新查詢，回答中附上查詢條件與當下頁面狀態。
- 以頁面 heading、目前 URL、控制項選取狀態、篩選結果摘要／筆數與可見卡片至少兩項核對結果。若頁面只留下輸入值或焦點，不能宣稱搜尋／篩選成功。

## Validation and freshness

- 搜尋：確認 heading、輸入值、URL／hash、結果筆數、分頁或可見結果；Google 自訂搜尋載入失敗或出現 CSP 訊息時，報告結果區不完整，不要把錯誤文字當成內容。
- 活動：確認目前年份／時間範圍、進階篩選 tags、結果筆數與活動卡；進入詳情後確認標題、日期、地點、適用分眾、活動資訊與回列表連結。
- 會員中心：確認 `/Member/myipac`、登入狀態、目前 tab 與服務卡；借閱／預約／電子書／活動記錄只報告當下可見結果，不把空清單或錯誤頁推論成沒有紀錄。
- 一方政策與說明頁的規則仍可能更新。需要借閱限制、數位資源使用資格或服務條件時，重新開啟一方頁面，不依賴本文件中的舊數字。

## Known limits

- 本輪沒有取得 robots 或 XML Sitemap 內容；只有 `/SiteMap` HTML 導覽可用。
- `/Member/myispace` 在目前 session 顯示一方 `Unexpected Error` 錯誤頁；`/Member/myactivity` 也顯示相同錯誤內容。`/Member/myebook` 點擊後未離開會員中心，直接導向嘗試被 client block；這些是本輪的存取／維護缺口，不是功能不存在的證明。
- 會員服務卡的外部館藏查詢、電子書、數位資源入口、線上視聽、活動平台與一證通平台本輪未切換分頁深入探索；只記錄主站可見入口與 target。
- 全站搜尋結果嵌入 Google 自訂搜尋；本輪可見查詢 URL、結果筆數與分頁，但部分內嵌內容出現 CSP `EvalError` 訊息，結果解析需保守。
- 活動日曆的進階篩選（分眾／主題）可套用並顯示 tags 與結果筆數；單獨點擊 `近7天` 與關鍵字搜尋在本輪未穩定改變畫面，未來使用時必須用兩項以上 UI 證據驗證。

## Drift maintenance

未來操作前，比對目前可見 UI、route、label、control、權限與一方說明。若不同，先用目前 UI 完成安全任務，再記錄公開／登入變體、頁型、原文件行為、目前行為、證據來源與日期；只有在差異穩定且直接由畫面支持時，才更新本 AGENTS、負責 skill 或 reference。不要寫入密碼、cookie、token、私人資料、當次結果、筆數、價格或活動日期。更新後重新執行受影響的唯讀流程與 `quick_validate.py`；廣泛或矛盾的差異要標為 maintenance gap，不要猜測。

## References

- [site-map.md](references/site-map.md) — 站內導覽、頁型與跨站入口。
- [data-model.md](references/data-model.md) — 搜尋、活動、會員與數位資源實體關係。
- [search-controls.md](references/search-controls.md) — 全站／進階搜尋欄位與驗證方式。
- [activity-controls.md](references/activity-controls.md) — 活動日曆、進階篩選與活動詳情欄位。
- [member-services.md](references/member-services.md) — 會員中心 tab、服務卡與已驗證的錯誤／限制。
- [first-party-guidance.md](references/first-party-guidance.md) — 借閱規則與數位資源一方說明。
- [agent-usability.md](references/agent-usability.md) — 四個文件-only routing 與安全流程模擬。
