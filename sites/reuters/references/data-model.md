# Reuters 資料模型

## Core entities

| Entity | 用途 | 重要欄位／識別方式 | 關聯頁面 |
| --- | --- | --- | --- |
| Article | Reuters 新聞或評論內容 | title、slug/date route、author(s)、published／updated time、summary、body、section、topic、media、tags、access state | section、search、article、sitemap |
| Section | 頂層內容分類 | visible label、route（如 `/world/`、`/business/`、`/technology/`） | home、main nav、search filter |
| Topic / category | section 下的主題或地區 | label、category route、article list | World／Markets／footer sitemap |
| Author | 文章作者或評論作者 | display name、`/authors/<slug>/` route、linked articles | article、Authors Sitemap、Commentary |
| Search result | 某 query 的文章結果項 | query、section、date range、sort、title、category、time、article href | `/site-search/` |
| Market instrument | LSEG quote／index／future／currency／bond | display name、quote route、last、change、unit、as-of/delay context | Markets tables、quote page |
| Market region | Markets dashboard 的資料 scope | `US`、`Europe`、`Asia Pacific` selected tab | `/markets/` |
| Sitemap index | 文章／topic／author inventory | year/month/day、A–Z grouping、candidate route | `/sitemap/`、`/sitemap/topics/`、`/sitemap/authors/` |

## Relationships

```text
Section → Topic/category → Article
Author ────────────────┘
Article → media / tags / related articles
Markets → Market region → Market instrument → quote or table
Search query + filters → Search result → Article
Sitemap index → candidate Article / Topic / Author route
```

## Semantics and freshness

- Article route 會將 section／region、slug 與日期編入 URL，但 URL 本身仍要在目前 UI 核對 title、author、時間與可見內容。
- Search result count、result order、times、article availability 與 article body 是動態值；不要在 skills 或 references 寫入本輪數字或清單。
- Markets 的 `Last`、`% Change`、`Yield`、`Today's Range` 與 region cards 都是動態 quote data；記錄畫面顯示的 unit、as-of 與 delay context，再於任務時重抓。
- Article 的 `Summary` tab 可先提供重點清單；正文、圖片 gallery、video、tags 與 Trust Principles context 位於同一 article entity 的不同區塊。
- `Exclusive`、`ANALYSIS`、`Sponsored Content` 與 `This content is not reviewed by Reuters journalists` 是內容屬性或來源提示，不要與 Reuters 編採新聞混為一談。
