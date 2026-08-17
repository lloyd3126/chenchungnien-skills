# 曼報 Pro 網站地圖與探索證據

## Scope

- 探索日期：2026-08-17。
- 入口：本輪從 Codex 內建瀏覽器中原本開啟的 `https://pro.manny-li.com/` 開始；前一輪曾由 `/join` 延伸核對。
- 探索狀態：公開頁面與目前可見的登入後變體已完成第二輪核對；會員文章／Podcast 詳情與帳戶管理頁已做讀取驗證，帳務與外部授權動作未執行。

## Sitemap / robots status

| Source | Discovery | Visual / retrieval result | Downloaded | Locally parsed | UI-verified | Final status |
| --- | --- | --- | --- | --- | --- | --- |
| Footer / visible UI | 未發現 Sitemap 或 HTML sitemap 連結；Footer 有 Firstory Help Center、服務條款、隱私政策與其他平台連結 | N/A | N/A | N/A | N/A | no sitemap discovered |
| `/robots.txt` | conventional same-origin candidate | 目前使用者分頁已視覺開啟並取得文字內容：`User-agent: GPTBot`／`Disallow: /`、`User-agent: OAI-SearchBot`／`Allow: /` | no | no | yes | UI-verified |
| `/sitemap.xml` | conventional same-origin candidate | 可視覺開啟，但呈現 Firstory HTML 錯誤頁「這個頁面不存在」，不是 XML | no | no | no | invalid |
| `/sitemap_index.xml` | conventional same-origin candidate | 可視覺開啟，但呈現同一個 Firstory HTML 錯誤頁，不是 sitemap index XML | no | no | no | invalid |
| `/sitemap.xml.gz` | conventional compressed candidate | 可視覺開啟 HTML 錯誤頁；等待下載事件逾時，沒有完成下載 | no | no | no | invalid |

結論：沒有發現可解析、可下載或可供抽樣的有效 Sitemap。`robots.txt` 已由目前使用者分頁視覺確認並 UI-verified；它提供的路徑線索是 GPTBot 對 `/` 的 `Disallow`，以及 OAI-SearchBot 對 `/` 的 `Allow`。這些是特定 crawler 的 discovery／crawl signal，不是使用者權限、登入狀態或頁面存在性的證據。先前控制層曾回報 `ERR_BLOCKED_BY_CLIENT`，但在可見分頁取得內容後不再標記為 `client-blocked`。

### robots directives (UI-verified)

- `User-agent: GPTBot` → `Disallow: /`
- `User-agent: OAI-SearchBot` → `Allow: /`
- 路徑線索與 Sitemap 路由分開記錄；本次沒有 Sitemap URL 可由 robots body 解析。
- 不將上述規則解讀成一般使用者的存取控制、登入權限或頁面不存在。

## Information architecture

| Page type | Verified route | Purpose | Stable controls / links | Status |
| --- | --- | --- | --- | --- |
| Home / usage guide | `/` | 說明核心價值、三條內容產品線、會員權益，提供精選 Podcast 與文章入口 | `加入會員`、公開 Podcast 平台連結、文章卡片、`所有單集`、`查看全部` | explored |
| Plan / FAQ | `/join` | 方案介紹、內容頻率、會員社群、研究倫理、團隊介紹、方案 FAQ | `#faq`、三個 FAQ 分類、FAQ 問題展開、Firstory 平台說明、客服連結 | explored |
| Episode collection | `/episodes` | 查看所有 Podcast 集數 | `一般`／`會員限定` tab、排序切換、集數卡片、播放時間按鈕、收聽平台連結 | public shell explored; protected branch partial |
| Post collection | `/posts` | 查看文章列表 | `一般`／`會員限定` tab、排序切換、文章卡片、`閱讀更多`、`載入更多文章` | public shell explored; protected branch partial |
| Tagged post collection | `/posts?tag=<tag-id>` | 依內容產品或社群標籤瀏覽文章 | 頁首可見標籤連結；使用現有 UI 取得 tag id | route pattern verified; representative contents not enumerated |
| Episode detail | `/episodes/<episode-slug>` | 單集詳情與收聽 | 從列表卡片進入；標題、`敘述`、自訂播放器跳轉／速度控制、留言區 | authenticated read-only explored |
| Post detail | `/posts/<post-slug>` | 文章正文與相關資訊 | 從列表卡片進入；文章 heading、引用、`延伸閱讀` | authenticated read-only explored |
| Account profile | `/account/profile` | 讀取登入後帳戶與會員管理入口 | `帳戶資訊`、`已連結的應用程式`、`付款資訊`、`更改付款資訊`、`登出` | authenticated read-only partial |

## Global navigation

頁首導覽目前包含：`首頁` → `/`、`方案` → `/join`、`PODCAST` → `/episodes`、`文章` → `/posts`、`商業解碼`／`科技曼讀`／`巨人之聲`／`曼報俱樂部` → `/posts?tag=<tag-id>`。右側有 theme toggle 與帳戶選單。登入變體的帳戶選單顯示 `會員管理`、`語言: 中文` 與 `登出`；`會員管理` 已讀取到 `/account/profile`，但未執行帳務變更。

頁尾連到 Firstory 的平台頁、服務條款、隱私政策與幫助中心；這些是外部平台頁，需以當前頁面連結為準。Firstory Help Center 的會員解鎖與訂閱 FAQ 已在瀏覽器中 UI-verified。

## Coverage checklist

| Area / entry point | Status | Evidence / next step |
| --- | --- | --- |
| Navbar | explored + authenticated rechecked | 首頁、方案、Podcast、文章與四個 tag link 已驗證 |
| Sidebar | not applicable | 未看到側邊欄 |
| Account dropdown | explored | theme toggle、帳戶選單、語言、會員管理、登出；不執行登出／帳務動作 |
| Account profile | partial | `/account/profile` 的區塊與安全入口已讀取；更改付款資訊與登出未測試 |
| Search / filters | not found | 目前公開與登入頁未看到站內搜尋、篩選或 query builder |
| Tabs / sorting | explored + authenticated rechecked | `/posts`、`/episodes` 的 access tabs 與排序切換已驗證 |
| Load more | explored + authenticated rechecked | `/posts` 載入更多後可見卡片增加 |
| FAQ accordion | explored + authenticated rechecked | `/join#faq` 分類與退款問題展開已驗證 |
| Footer / Help | explored | Firstory Help Center 與訂閱制會員 FAQ UI-verified |
| Sitemap / robots | UI-verified / invalid | robots directives 已視覺確認；Sitemap 候選均實際呈現 HTML 錯誤頁 |

## Verified interactions

### Articles and episodes

1. 進入 `/posts` 或 `/episodes` 後，先確認主要 heading 與目前 selected tab。
2. 點擊「一般」或「會員限定」後，selected/active 狀態會改變；會員限定結果是否出現取決於當前帳戶權限。
3. 點擊「最新到最舊」會切換為「最舊到最新」，列表會重新載入；反向點擊可切回。等待卡片重新出現後再回報結果。
4. `/posts` 的文章列表可使用 `載入更多文章`；不要把當次載入的總數寫入持久化文件。
5. 卡片標題與 `閱讀更多`／集數連結是進入 detail page 的可靠入口；不要手寫或猜 slug。

### Plan FAQ

`/join#faq` 有三個分類：`訂閱相關內容`、`付款與帳務`、`取消與退款`。點分類後，再點問題按鈕展開答案；展開狀態會以 `expanded`／頁面上新增的段落呈現。已驗證的問題包括：方案更改或暫停、七日鑑賞期、扣款時點、資料是否公開、退款。

### Authenticated variant

- `/episodes`：`會員限定` tab 在目前登入 session 顯示集數卡片；集數詳情有標題、`敘述`、跳轉／速度控制與留言區。播放器由自訂控制呈現，未觀察到原生 `<audio>` 元素。
- `/posts`：`會員限定` tab 顯示文章卡片；`載入更多文章` 會增加可見卡片，之後仍需重新核對目前列表。
- `/posts?tag=<tag-id>`：四個已驗證標籤頁都有文章卡片；目前登入變體曾出現 `一般` tab selected、但卡片仍標記 `會員限定` 的狀態，因此要同時核對 tab、卡片標記與實際正文權限。
- 文章詳情可有多層 heading、提問表單／歡迎加入連結、內文引用與 `延伸閱讀`；只讀取，不提交提問或其他內容。

## Protected boundaries

- `/episodes` 與 `/posts` 的會員限定 tab、文章／集數詳情在目前登入變體已做只讀探索；如果未登入，不要以 tab 數量或 URL 猜測權限。
- 會員管理、取消訂閱、退款、付款、`更改付款資訊`、登出與 Apple／Spotify 綁定可能造成帳戶或外部服務狀態變更；本次未測試，之後必須在最後一步按鈕前停下並取得即時確認。
- 不要讀取帳戶選單中的 email、cookie、token 或任何 session 內容；生成文件只記錄「帳戶選單存在／可進入會員管理」這個穩定事實。

## Refresh path

若需要最新文章／集數、標籤、內容數量或價格，回到當前頁首 UI，重新開啟 `/posts`、`/episodes` 或 `/join`，核對主要 heading、active tab、排序文字與第一批結果。不要依賴本文件中的探索快照。
