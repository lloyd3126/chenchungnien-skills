# 曼報 Pro 資料模型

這是由頁面 UI 推導的操作模型，不是 Firstory 後端 schema。欄位名稱是給 Agent 做頁面定位與結果驗證用的抽象名稱；當前值必須每次從頁面讀取。

## Entities

| Entity | Purpose | Important fields / signals | Relationships |
| --- | --- | --- | --- |
| Content item | 一篇文章或一集 Podcast | `title`、`published_at`（頁面顯示日期／相對時間）、`member_only`、`summary`、detail route | 屬於一個或多個 `Content collection`；可在首頁被精選 |
| Article | 會員文章內容 | `title`、`published_at`、`tag`、`member_only`、`detail_slug`、正文存取狀態 | 由 `/posts`、tag collection、首頁文章卡片進入 |
| Episode | Podcast 單集 | `title`、`published_at`、`duration`、`member_only`、`detail_slug`、播放按鈕／收聽狀態 | 由 `/episodes`、首頁熱門單集進入；可對應一篇原始文章 |
| Content collection | 文章或集數的列表視圖 | `content_type`、`access_tab`（一般／會員限定）、`sort_direction`、載入狀態 | 列表中的 item 連到 detail；tag collection 是文章 collection 的變體 |
| Tag | 內容產品／社群分類 | 可見 label（商業解碼、科技曼讀、巨人之聲、曼報俱樂部）、query route | 透過 `/posts?tag=<tag-id>` 篩選 Article |
| Plan | 會員訂閱方案 | `name`、`billing_period`、`price`、entitlements、FAQ links | Plan grants access to member-only Articles / Episodes and community benefits |
| Membership / account | Firstory 登入與會員權限 | account menu、會員管理入口、實際內容可見性、播放器狀態 | Membership controls access; account identity is sensitive and must not be persisted |
| Account profile | 登入後的會員管理頁 | route `/account/profile`、`帳戶資訊`、`已連結的應用程式`、`付款資訊`、可見的付款／登出控制 | 由 account dropdown 的 `會員管理` 進入；只讀取區塊，不執行變更 |
| FAQ item | 方案與帳務說明 | `category`、`question`、expanded answer、first-party source | FAQ categories belong to Plan page; answers may link to Firstory Help Center |

## Access and freshness

- `member_only` 是頁面上明示的內容標記，不等同於目前 Agent 已獲得讀取權限。
- 會員權限應以 detail page 正文、播放按鈕或登入／加入會員提示驗證；不能只看帳戶頭像或 tab 數字。
- `published_at`、`duration`、列表數量、`price` 與會員狀態都是動態欄位。只回報任務當下頁面讀到的值，並附上查詢頁面與時間背景。
- 文章 detail 與 episode detail 的 slug 是頁面連結中的識別值；從可見卡片取得，不要從標題自行轉換。
- Episode detail 的播放器可能是自訂控制，不一定會出現原生 `<audio>`；以可見的播放／跳轉／速度控制與 `敘述` heading 驗證。
- Article detail 的正文以 heading 階層、引用連結與 `延伸閱讀` 組成；不要把當前文章標題、提問或內容段落寫進持久化模型。
- Tag collection 的 selected access tab 與卡片 `member_only` 標記可能不一致；以卡片標記與實際正文／播放狀態共同判斷。

## Entity routing

```text
首頁
├── 精選 Episode ──> /episodes/<slug>
├── 文章卡片 ─────> /posts/<slug>
└── 加入會員 ─────> /join#faq

頁首
├── PODCAST ──────> Episode collection ──> Episode detail
├── 文章 ─────────> Article collection ──> Article detail
└── content tag ──> Tagged article collection

方案 /join
└── Plan + FAQ ───> Firstory Help Center / membership management（受保護或可能改變狀態）
```

## Agent interpretation rules

1. 使用者說「找文章」時，先在 `/posts` 以標題與可見分類尋找；不要直接猜 detail URL。
2. 使用者說「找某系列」時，優先使用頁首的可見 tag link，再在結果頁確認 heading／active state。
3. 使用者說「找 Podcast」時，進入 `/episodes`；用集數標題、摘要與 duration 交叉核對。
4. 使用者問「怎麼取消／退款／改方案」時，先讀 `first-party-guidance.md` 與 `/join#faq` 的最新答案；只有在使用者要執行動作時才進入會員管理，並在不可逆或帳務提交前停下確認。
