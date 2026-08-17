# koding.school 穩定路由圖

這是以目前 UI 驗證的 route pattern，不是 Sitemap inventory。需要目前資料時，從可見連結重新取得，不要拼接私人 id、token 或完整 URL 清單。

## Intent routing

| Agent need | Entry point | Route pattern | Owning skill | Verification |
| --- | --- | --- | --- | --- |
| 繼續最近課程 | 首頁 `繼續上課` | `/` → `/courses/<family>/<slug>/lessons/<unit>/<chapter>` | `koding-school-learning` | URL、breadcrumb、lesson 標題 |
| 找已加入課程 | 帳號選單 `我的課程` | `/my/courses` | `koding-school-learning` | `我的課程` heading、query、可見卡片 |
| 看課程內容 | 課程卡／lesson `返回課程` | `/courses/<family>/<slug>` | `koding-school-learning` | heading、時數、難度、outline、討論區 |
| 看課程討論 | 課程詳情 `討論區` | `/courses/<slug>/topics` | `koding-school-community` | 課程 heading、lesson board links |
| 看單一 lesson 討論 | 課程 board 的 lesson link | `/courses/<slug>/lessons/<lesson-id>/topics` | `koding-school-community` | `Lesson N > 討論區`、搜尋、主題列表 |
| 看知識點 | 課程 outline 或相關知識點 | `/knowledges/<slug>` | `koding-school-community` | heading、正文／`尚無內容`、相關連結 |
| 搜尋作品 | 帳號選單 `我的作品` | `/my/projects` + visible `q` form | `koding-school-projects` | 搜尋欄、query、tab、結果狀態 |
| 看工作室 | 帳號選單 `我的工作室` | `/my/studios` → `/studios/<studio-id>` | `koding-school-projects` | 工作室 heading、作品卡、返回連結 |
| 看履歷 | 帳號選單 `我的履歷` | `/resume/<student-id>` | `koding-school-projects` | heading、技能／作品區、頁碼 |
| 看收信匣入口 | 帳號選單 `我的收信匣` | `/my/messages` | `koding-school-projects` | `我的收信匣` heading；私訊本文需額外明確請求 |
| 看帳號欄位 | 帳號選單 `帳號設定` | `/my/account` | `koding-school-projects` | 欄位 label、POST boundary；不讀值或送出 |

## Lesson page variants

由可見 lesson 標題分類，不要以編號猜頁型：

- `【說明】`：教學影片／課程側欄。
- `【講解】`：影片、`版型` 與 JavaScript practice/editor iframe。
- `【試玩】`：JavaScript、Assets、Preview、Console 與 Run／Format／Stop；只讀取畫面，不執行。
- `【連結】`：導向綜合練習的 lesson；可能同時出現帶編碼 `data` 的 `Subcourse button`，視為 tokenized，不能保存或盲目跟隨。

所有 variant 都可能提供 `返回課程`、`下一章`、`課程列表` 與 `老師我有問題！`。每次都以當下可見 breadcrumb 與連結為準。

## Query and freshness

- `/my/courses` 的搜尋使用可見 `課程名稱` 欄位與 `搜尋`，驗證 `q` 與結果；`utf8`、`button` 等表單輔助參數不代表額外語意。
- `/my/courses` 的排序／狀態／類型 links 會組合既有 query；不要硬寫當前課程或進度。
- `/my/projects` 的搜尋同樣以可見 `專案名稱` 與 `q` 驗證；tabs 與結果是當前帳號的動態資料。
- 討論搜尋是 lesson board 內的可見文字過濾；輸入後確認列表縮小，清除後確認恢復。
- 課程進度、主題數、作者、時間、作品名稱、訊息與履歷內容都必須重新讀取，不能寫成路由規則。
