# koding.school 探索 checklist

這份 checklist 只保存穩定的探索狀態與驗證方法；課程進度、卡片數量、作品名稱、訊息內容、作者與時間均為動態資料，不寫入此檔。

## Sitemap／robots inventory

| 來源 | 類型 | 狀態 | 證據與後續 |
| --- | --- | --- | --- |
| 首頁、課程頁、知識點頁頁尾 | UI inventory | no sitemap discovered | 看見 `關於我們`、聯絡方式；未看見 HTML sitemap、Help、Documentation 或 FAQ。 |
| `/robots.txt` | robots metadata | blocked | Codex 內建瀏覽器回報 `ERR_BLOCKED_BY_CLIENT`；未取得 `User-agent`、`Allow`、`Disallow`、`Sitemap:`，不產生 robots route clue。 |
| `/sitemap.xml` | XML candidate | blocked | Codex 內建瀏覽器回報 `ERR_BLOCKED_BY_CLIENT`；未視覺取得 XML、未下載、未解析、未做 UI-verified。 |
| `.xml.gz` candidate | compressed XML | no sitemap discovered | 未由 UI 或 robots 發現 `.gz`，未觸發下載。 |

`blocked` 只描述目前內建瀏覽器的 retrieval path，不代表資源不存在或使用者沒有權限。不要把 Disallow（若未來取得）當成 user permission 或 page absence 證明。

## Coverage

| 區域／入口 | 已確認內容 | 狀態 | 安全邊界 |
| --- | --- | --- | --- |
| 首頁 | `繼續上次的課程`、課程卡、collapsed navigation、頁尾 | explored | 目前進度與繼續目標要每次重新取得 |
| `創造` | Scratch3、JavaScript、Web、Micro:Bit、Ozobot、App Inventor、Python、Roblox 與專案名稱欄位；`新增作品` 初始 disabled | explored | 不輸入名稱、不新增作品 |
| `我有邀請碼` | 邀請碼欄位、disabled 課程選擇、`送出`、`關閉` | explored | 不輸入邀請碼、不送出 |
| `我的課程` | 名稱搜尋、重置、排序、未／已過期、全部／主題課程／綜合練習 | explored | 搜尋、排序、篩選可測；結果與進度不寫入文件 |
| 課程詳情與 lesson | lesson outline、知識點、討論區；`說明`／`講解`／`試玩`／`連結` 型態 | explored | 不執行 Run、Format、Stop，不儲存或編輯程式 |
| 課程討論 | 課程 board、lesson board、`搜尋`、主題詳情、回覆編輯器 | explored | 搜尋與閱讀可做；不新增主題、不留言、不開專案編輯器 |
| 知識點 | heading、正文或 `尚無內容`、相關知識點、更新標記 | explored | 文章與更新時間保持動態 |
| `我的作品` | 名稱搜尋、回收桶、語言 tabs、作品卡 | explored | 不開啟編輯、回收桶、刪除或上傳流程 |
| `我的工作室`／工作室 | `進入`、工作室標題、作品卡、`新增作品`、`移除` | explored | 不新增、不移除 |
| 履歷 | 技能、作品、頁碼路由 | partial | 未保存個人欄位與作品內容 |
| 收信匣 | list heading 與 `/my/messages/<message-id>` 路由模式 | partial | 未讀取訊息本文 |
| 帳號設定 | 帳號、Email、生日、頭像、履歷背景圖、暱稱、居住地區、簡介；主要 form POST `/my/account` | explored | 不讀值、不填寫、不上傳、不送出 |
| 頁尾語言 | 內容頁 `繁中`、`简中`、`English`、`日本語` | explored | 不主動切換語言，避免改變 session／頁面狀態 |

## 已實測的安全互動

- 課程搜尋：輸入代表詞後確認 `q` query、保留欄位與可見結果。
- 課程篩選：確認重置、名稱排序、`type=question` 的可見連結與結果；排序後 UI 會把反向操作標籤顯示為 `依使用時間排序`。
- 討論搜尋：輸入代表詞後列表縮小；用全選／Backspace 清除後列表恢復。
- 作品搜尋與語言 tab：確認 `q` query 與 tabpanel；搜尋結果不足時部分語言 tab 可能不顯示。
- 創造／邀請碼／語言選單：只開啟與關閉；未送出、未切換。

## Authenticated second pass

目前 session 由首頁導覽中的登入者選單與另一個知識點頁的 `我的課程`／帳號按鈕明確確認為已登入。已重新核對首頁、課程、lesson、知識點、討論、作品、工作室、履歷、收信匣與帳號入口；未登出重做匿名變體，因為登出會改變使用者 session，且不是本次安全探索的必要步驟。

## Maintenance gaps

- Sitemap／robots retrieval 仍受內建瀏覽器 client block；若未來 UI 提供第一方 sitemap 或 robots 內容，再補做 XML／robots parsing 與代表路由 UI verification。
- 專案編輯器、回收桶、工作室建立／移除、帳號更新、私訊本文、付款／訂單與訂閱流程未驗證。
