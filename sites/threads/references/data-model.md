# Threads 公開資料模型

## Entities

### Profile

- **Purpose**：代表一個公開 Threads 帳號。
- **Stable key**：URL 中的 `<username>` handle；顯示名稱可能改變。
- **Observed fields**：display name、username、bio、外部連結、followers、recent views、Instagram link、串文／回覆／影音內容／轉發分頁。
- **Related entities**：owns Posts、authors Replies、may attach Media and external links。
- **Views**：`/@<username>`、`/@<username>/replies`、`/@<username>/media`、`/@<username>/reposts`。

### Post / Thread

- **Purpose**：一則公開串文或其詳情頁。
- **Stable key**：`<username>/post/<post-id>` 中的 `post-id`；不要用貼文文字或時間當 ID。
- **Observed fields**：author profile、published time、text、topic/tag links、media items、external preview、view count（若詳情頁可見）、like/reply/repost/share controls。
- **Views**：feed card、profile tab、search result、`/@<username>/post/<post-id>`。
- **Media route**：由貼文可見媒體 link 進入 `.../media`；不要自行猜測未見的 media route。

### Reply

- **Purpose**：附屬於一則 root post 的回覆內容；回覆本身也可能有自己的 post route。
- **Observed fields**：reply author、time、text／media、作者標記、like/reply/repost/share controls、parent context。
- **Views**：post detail 的 reply list；可用 `排序 熱門` 控件改變順序（本次未提交任何回覆）。

### Media

- **Purpose**：貼文或回覆所附的圖片、影片、音樂或多圖內容。
- **Observed fields**：alt text／caption、媒體序號、video player、muted state、music metadata、media link。
- **Views**：feed、profile media、post media route、post detail。
- **Freshness**：媒體與 OCR/alt text 只代表當次頁面可見內容；不要把它寫成官方事實。

### Topic / Search result

- **Purpose**：由 searchbox、貼文 topic link 或趨勢卡片產生的結果集合。
- **Observed fields**：query、`serp_type`、`filter`、result cards、profile cards、trend summary。
- **Views**：`/search?q=<query>&serp_type=default`、`filter=recent`、`filter=profiles`、`serp_type=tags`、`serp_type=trends`。
- **Freshness**：結果、趨勢、摘要、排名與數量皆是動態資料；保存 query/filter state，不保存當次結果值。

### Activity event

- **Purpose**：登入後的通知／活動事件，例如建議串文、開始追蹤、貼文瀏覽門檻、提及、回覆、引用或轉發。
- **Observed fields**：event type label、actor profile、related post/profile link、relative time、engagement controls。
- **Views**：`/activity`；類型篩選可進入 `/activity/replies`，其他 filter route 以目前 UI 為準。
- **Freshness**：事件與數量個人化且會改變；不要寫入當次事件或 actor 清單。

### Insights report

- **Purpose**：登入後帳號的成效摘要與明細。
- **Stable routing**：`/insights/`，日期範圍使用 `?days=7|14|30|90`；明細包括 `/insights/views`、`/insights/interactions`、`/insights/followers`、`/insights/posts?days=<n>`。
- **Observed fields**：date range、summary cards、views、interactions、followers、popular posts、source breakdown、empty state。
- **Freshness**：所有數值、日期標籤、來源比例、熱門內容與貼文數是動態個人資料；必須在任務當下重新取得。

### Saved collection / Personal feed

- **Purpose**：登入者已儲存內容或追蹤中的個人化 feed。
- **Views**：`/saved/`、`/following/`。
- **Observed fields**：post cards、author、topic、media、repost context、engagement controls。
- **Safety**：讀取不等於可修改；儲存／取消儲存、追蹤／取消追蹤與互動都是副作用。

### Message thread

- **Purpose**：登入後的 Direct message inbox、request、hidden 或 thread。
- **Views**：`/messages/`、`/messages`、`/messages/requests`、`/messages/hidden`、`/messages/new/`，以及 inbox 顯示的 `/messages/t/<thread-id>/`。
- **Observed fields**：conversation participant、latest message preview、relative time、request category、onboarding dialog。
- **Safety**：讀取 thread 與輸入／傳送訊息是不同操作；不得因看見 composer 而輸入或傳送。

### Ephemeral post

- **Purpose**：`/ghost_posts/` 顯示的限時貼文。
- **Observed fields**：author、text、remaining lifetime、like entry。
- **Freshness**：剩餘時間與可見內容會快速變動；每次即時讀取，不保存內容或倒數值。

### Engagement / Activity

- **Purpose**：貼文上的 like、reply、repost、share、follow、message、save 等互動入口。
- **Observed semantics**：按鈕會顯示動態計數或狀態，但本次只讀取標籤；未測試副作用流程。
- **Safety**：like、follow、repost、share、save、message、reply、publish、delete 都要分別視為副作用或受保護邊界，不要在 discovery 中觸發。

## Relationships

```text
Profile ──authors──> Post/Thread ──contains──> Media
Profile ──authors──> Reply ──belongs-to──> Post/Thread
Post/Thread ──links-to──> Topic/Search result
Post/Thread ──has──> Engagement/Activity controls
Search result ──opens──> Profile or Post/Thread
Profile ──tabs──> Posts, Replies, Media, Reposts
Account ──has──> Activity events, Insights reports, Saved collection, Message threads
Account ──reads──> Following feed and Ephemeral posts
```

## Retrieval rules

- 先用 visible link、目前 URL 與 heading 取得 entity key，再讀相關欄位。
- Handle、post ID、query、filter 和 `serp_type` 是 routing context；顯示名稱、數量、時間、內容、摘要和推薦列表是當次資料。
- 若 URL 與 visible heading 或內容互相矛盾，以目前頁面 UI 為準，重新開啟正確的 visible route，並記錄 drift。
