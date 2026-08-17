# Threads 頁面地圖

## Sitemap and robots inventory status

| Candidate or source | discovered | visually accessible | downloaded | locally parsed | UI-verified | final status | Evidence / interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Visible Sitemap link | no | no | no | no | no | no sitemap discovered | Footer showed Terms, Privacy, and Cookie only |
| `/sitemap.xml` | yes | yes | no | no | no | invalid / unavailable | HTML error page said the link/page was unavailable; not XML |
| `/sitemap_index.xml` | yes | yes | no | no | no | invalid / unavailable | Same HTML error page; not XML |
| `/sitemap.xml.gz` | yes | yes | no | no | no | invalid / unavailable | Same HTML error page; no browser download completed |
| `/robots.txt` | yes | no | no | no | no | blocked | In-app browser returned `net::ERR_BLOCKED_BY_CLIENT`; no directives parsed |

The candidates above are discovery probes only. A `Disallow` directive, had it been readable, would not be treated as a permission boundary or proof that a page does not exist. Because no XML or gzip file was obtained, there is no local route sample to preserve.

The rest of this document keeps only UI-visible, opened, or linked stable route patterns and omits current result lists, tokenized URLs, and private content.

## Verified public page types

| Page type | Entry / route pattern | Verified purpose | Important visible controls |
| --- | --- | --- | --- |
| Home feed | `/` | 為你推薦動態欄與撰寫入口 | `新串文`、貼文互動按鈕、媒體播放器 |
| Search landing | `/search` | 搜尋字串、推薦話題、趨勢與推薦個人檔案 | `搜尋` searchbox、`篩選` |
| Keyword results | `/search?q=<query>&serp_type=default` | 以關鍵字查看貼文結果 | `最相關`、`最近`、`個人檔案` |
| Search filters | 同一搜尋路由加 `filter=recent` 或 `filter=profiles` | 最近貼文或個人檔案結果 | `篩選` → `指定日期之後`、`指定日期之前`、`來自個人檔案……` |
| Topic/tag results | `/search?q=<term>&serp_type=tags&tag_id=<id>` | 由貼文中的話題連到話題結果 | `最相關`、`最近`、`個人檔案` |
| Trend results | `/search?q=<term>&serp_type=trends&trend_fbid=<id>` | 由趨勢卡片進入動態話題結果 | 趨勢摘要與貼文結果；內容動態 |
| Public profile | `/@<username>` | 公開帳號簡介與串文 | `串文`、`回覆`、`影音內容`、`轉發`、`追蹤`、`發送訊息` |
| Profile replies | `/@<username>/replies` | 該帳號的回覆活動 | `正在回覆`、回覆貼文串 |
| Profile media | `/@<username>/media` | 該帳號含媒體的內容 | 圖片／影片／音樂內容 |
| Profile reposts | `/@<username>/reposts` | 該帳號轉發的內容 | 原作者內容與轉發貼文 |
| Public post detail | `/@<username>/post/<post-id>` | 單一串文與回覆串 | `排序 熱門`、`查看動態`、回覆 composer、回覆互動 |
| Post media | `/@<username>/post/<post-id>/media` | 單一貼文的媒體內容 | 媒體檢視；路由由貼文頁可見連結驗證 |
| Authenticated activity | `/activity`、`/activity/replies` | 通知／活動 feed 與類型篩選 | `全部` → `全部`、`追蹤`、`回覆`、`提及`、`引用`、`轉發` |
| Following feed | `/following/` | 只讀取追蹤中的個人化 feed | `新串文`、貼文 cards、轉發 context |
| Saved feed | `/saved/` | 只讀取已儲存貼文 | 貼文 cards、作者、topic、media、互動 controls |
| Ephemeral posts | `/ghost_posts/` | 限時貼文檢視 | 剩餘時間、貼文文字、讚入口 |
| Direct messages | `/messages/`、`/messages` | 收件匣與訊息 thread 入口 | 收件匣、陌生訊息、搜尋、thread links、onboarding dialog |
| Message requests | `/messages/requests` | 未追蹤用戶的訊息 | `陌生訊息`、`隱藏`、`新訊息`、管理設定 |
| Message composer entry | `/messages/new/` | 新訊息流程入口；本次只確認 loading／入口 | `新訊息`、收件匣／陌生訊息返回 links |
| Insights dashboard | `/insights/`、`/insights?days=<n>` | 個人化成效摘要與熱門內容 | `過去7天`、`過去14天`、`過去30天`、`過去90天` |
| Insights detail | `/insights/views?days=<n>`、`/insights/interactions?days=<n>`、`/insights/followers?days=<n>`、`/insights/posts?days=<n>` | 瀏覽、互動、粉絲與熱門內容明細 | 日期範圍、metric、貼文／瀏覽次數／所有貼文控制 |

## Authenticated coverage and remaining boundaries

| Visible label | Route | Status |
| --- | --- | --- |
| 訊息 | `/messages/` | UI-verified；收件匣可見，出現 Direct onboarding dialog |
| 通知／動態 | `/activity`、`/activity/replies` | UI-verified；篩選選項已讀取並測試回覆路由 |
| 洞察報告 | `/insights/` 與 detail routes | UI-verified；日期範圍與瀏覽頁已測試，部分 detail 仍可能 loading |
| 已儲存 | `/saved/` | UI-verified；等待載入後可見已儲存貼文 |
| 追蹤中 | `/following/` | UI-verified；個人化 feed 可見 |
| 限時貼文 | `/ghost_posts/` | UI-verified；含剩餘時間 |
| 個人檔案、撰寫、追蹤、訊息等帳號操作 | account-dependent | profile 與入口 UI-verified；編輯／發佈／傳送最後一步未執行 |

## Coverage notes

- 首頁、搜尋 landing、keyword results、recent/profile filter、topic results、public profile 及四個 profile tabs、post detail 與 reply sorting 已經由 UI 讀取，並在已登入狀態重新核對。
- 已登入狀態新增核對首頁、個人檔案四分頁、自己的貼文詳情、動態篩選、追蹤中、已儲存、限時貼文、訊息收件匣／陌生訊息／新訊息入口與洞察 dashboard／detail routes。
- Search filter 的 `指定日期之後` 在當日探索時直接產生「以下日期之後：<當日>」chip；`清除` 可移除。不同日期的 picker、`指定日期之前` 與 `來自個人檔案……` 尚未完整測試。
- 一次從公開 profile 點擊 `搜尋phycause的貼文` 未觀察到 URL 轉換，雖然 DOM 顯示 `/search?from_author=phycause`；這條 routing 只保留為可見但未確認的候選，不把它當成已驗證工作流。
- 動態內容可能出現 loading status、空結果、推薦內容或結果變動；每次任務都要重讀。洞察部分頁與訊息新訊息流程在本次仍觀察到 loading skeleton，不把 skeleton 當成空結果或成功提交。

## Refresh procedure

重新探索時先在同一內建瀏覽器 tab 檢查 `/`、`/search`、一個公開 profile 與一個公開 post，再由可見連結取得 topic、trend、activity、insights、saved、following、messages 與 ghost posts route。只有當目前頁面明確顯示已登入時，才讀取上述個人化頁；任何 route pattern 都不是權限證明。
