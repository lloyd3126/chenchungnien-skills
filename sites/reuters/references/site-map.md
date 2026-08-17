# Reuters 路由與頁型地圖

## Evidence boundary

本表由 2026-08-17 目前 Codex 內建瀏覽器分頁的 `current-tab visual`、`current-tab DOM/interaction` 與 `automation/control error` 整理。動態文章與數值不保存在此。

## First-party inventory

| 路由 | 用途／可見結構 | 狀態 | 證據 |
| --- | --- | --- | --- |
| `/sitemap/` | 年份 → 月份 → 日期文章 inventory；2026-08 連到 `/sitemap/2026-08/<day>/1/` | UI-verified | current-tab visual + DOM/interaction |
| `/sitemap/2026-08/` | 2026 年 8 月的日期索引 | DOM explored; not UI-verified | current-tab DOM/interaction + screenshot control error |
| `/sitemap/topics/` | Topics 分頁，A–Z 入口 | DOM explored; not UI-verified | current-tab DOM/interaction + screenshot control error |
| `/sitemap/authors/` | Authors 分頁，A–Z 入口與作者連結 | DOM explored; not UI-verified | current-tab DOM/interaction + screenshot control error |
| `/robots.txt` | 同源 robots candidate | client-blocked | automation/control error after same-tab visual retry |
| `/sitemap.xml` | 傳統 Sitemap candidate；顯示 Reuters 404 HTML | invalid | current-tab visual |
| `/sitemap_index.xml` | Sitemap index candidate；顯示 Reuters 404 HTML | invalid | current-tab visual |

## Top-level routes

| Visible label | Route | Page type | Confirmed durable behavior |
| --- | --- | --- | --- |
| Home | `/` | home / latest feed | 顯示 top stories、topic blocks、newsletter、market ticker 與 footer Site Index |
| World | `/world/` | section list | 顯示主要新聞卡、category links 與 `Load more articles` |
| Business | `/business/` | section list | 顯示 business lead story 與新聞列表 |
| Markets | `/markets/` | markets dashboard | 顯示 category nav、region tabs、security search、行情表格與市場文章 |
| Sustainability | `/sustainability/` | section list | 頁首主分類為 Sustainability；細節欄位需依任務重抓 |
| Legal | `/legal/` | section list | 頁首主分類為 Legal；細節欄位需依任務重抓 |
| Commentary | `/commentary/` | commentary hub | `Reuters Open Interest`、`Reuters Breakingviews`、Explore more 與 Sponsored Content |
| Technology | `/technology/` | section list | 頁首主分類為 Technology；AI 可由此或搜尋進入 |
| Investigations | `/investigations/` | special-report hub | `Reuters Investigates`、`More Investigations` 與 video/report links |
| Search | `/site-search/?query=<encoded>` | search results | Search heading、result count、Section／Date range／Sort by controls |
| Article | `/world/<region>/<slug>-<date>/` 等 | article detail | title、authors、time、Summary、body、media、tags、source/standards context |

## More menu families

`More` 展開後的 visible route families：`/sports/`、`/science/`、`/lifestyle/`、`/city-memo/`、`/graphics/`、`/pictures/`、`/wider-image/`、`/podcasts/`、`/live/`、`/fact-check/`、`/video/`、`/media-center/`、`/sponsored/` 與 `/press-releases/`。其子路由包含 sports leagues、podcast series、Media Center categories 與 Sponsored Content branches；只在任務需要時開啟代表頁。

## Refresh rule

用 Sitemap 找到候選文章或作者後，回到 Reuters UI 重新開啟並核對 title、heading、時間與內容。Sitemap 是 inventory accelerator，不是 feature、permission、currentness 或結果完整性的證明。
