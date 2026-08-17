# X 公開與已登入頁型地圖

探索基準：2026-08-17，使用 Codex 內建瀏覽器，起點為 `https://x.com/lloyd3126`。本次是中斷點續查，不重新掃描整站；不要把下列動態頁面內容當成固定資料。

## Coverage

| 區域 | 代表路由 | 狀態 | 可重用知識 |
|---|---|---|---|
| 首頁時間軸 | `/home` | explored | 推薦／正在跟隨／自訂時間軸、發佈編輯器、貼文卡片 |
| 探索 | `/explore` | explored | 搜尋框、趨勢、新聞／體育／娛樂分頁、推薦帳戶 |
| 搜尋結果 | `/search?q=<query>&src=typeahead_click` | explored | 熱門、最新、人物、媒體、列表分頁 |
| 個人頁 | `/<handle>` | explored | 個人資料摘要、貼文／回覆／轉發／媒體或影片分頁 |
| 貼文詳情 | `/<handle>/status/<post-id>` | explored | 對話、貼文正文、互動摘要、回覆編輯器 |
| 貼文分析 | `/<handle>/status/<post-id>/analytics` | partial | 已登入且為帳戶本人貼文時可見 `貼文分析` dialog |
| 鍵盤快捷鍵說明 | `/i/keyboard_shortcuts` | explored | `鍵盤快速鍵` dialog，含導覽、動作與媒體三組表格 |
| 個人頁相片 | `/<handle>/photo`、`/<handle>/header_photo` | observed route | 頭像與標題圖片入口，未深入圖片檢視器 |
| 個人列表／社群 | `/<handle>/lists`、`/<handle>/communities` | route observed | 由更多選單進入，未深入內容 |
| 通知、私訊、歷史、設定 | `/notifications`、`/i/chat`、`/i/history`、`/settings` | protected—unexplored | 可能包含個人資料或改變帳戶狀態 |

## Global navigation

主要導覽目前可見：`首頁`、`搜尋和探索`、`通知`、`私人訊息`、`Grok`、`Premium`、`歷史記錄`、`創作者工作室`、`文章`、`個人資料`，以及 `更多選單項目`。更多選單另顯示 `列表`、`社群`、`商業`、`廣告`、`建立你的音訊空間`、`設定和隱私`。

## Search tabs

使用一般搜尋後，結果頁目前提供：

- `熱門`：相關貼文結果。
- `最新`：即時／時間排序的貼文結果；URL 觀察到 `f=live`。
- `人物`：帳戶結果；URL 觀察到 `f=user`。
- `媒體`：圖片與影片縮圖／媒體連結；URL 觀察到 `f=media`。
- `列表`：列表結果；URL 觀察到 `f=list`。

這些 query 參數是本次 UI 觀察，不要用來猜測未看見的路由；優先點選可見 tab。

## Profile tabs

個人頁 header 下方目前可見 `貼文`、`回覆`、`轉發`、`媒體`。點選媒體後，已登入頁的選取狀態顯示為 `影片`，內容為影片時間軸與空狀態；未來操作應以當下可見 tab 名稱為準，不要假設 `媒體`／`影片` 標籤固定。

個人頁也可見：個人檔案相片、編輯個人資料、顯示翻譯、加入日期、跟隨中、跟隨者與個人頁搜尋按鈕。數量與 bio 必須現場重讀。

## Sitemap and robots status

| Source | discovered | visually accessible | downloaded | locally parsed | UI-verified route | final status |
|---|---|---|---|---|---|---|
| visible site map link | no | no | n/a | n/a | n/a | `no sitemap discovered` |
| `/sitemap.xml` | yes, as a conventional probe | yes; X 404 page | no | no | no | `unavailable` |
| `/robots.txt` | yes, as a conventional probe | no; client blocked the request and the visible page remained the sitemap 404 | no | no | n/a | `blocked` |

No `.xml.gz` was discovered or downloaded, so decompression and local XML parsing were not applicable. No Sitemap, User-agent, Allow, or Disallow directives were available from the current browser session. This is a UI inventory, not a sitemap inventory.

## Follow-up route validation

續查只抽樣驗證既有穩定路由，未重新探索整站：

| 路由 | 頁面標題／內容證據 | 結果 |
|---|---|---|
| `/home` | `首頁 / X`；等待實際內容後可見 `你的首頁時間軸` | verified |
| `/explore` | `探索 / X`；可見 `探索` | verified |
| `/<handle>`（本次為目前開啟的個人頁） | `Chen Chung Nien (@lloyd3126) / X`；可見 `@lloyd3126` | verified |

以上只保存穩定路由模式與頁面證據，不保存完整 URL 清單、目前貼文數、貼文內容、日期或即時互動數。

## Unexplored branches

- 未讀取通知、私訊、歷史記錄或帳戶設定中的個人內容。
- 未執行發佈、回覆、按讚、轉發、收藏、追蹤、排程、推廣、編輯或刪除。
- 未探索第三方登入、付款、Premium、Grok、Creator Studio、Spaces 或廣告管理。
