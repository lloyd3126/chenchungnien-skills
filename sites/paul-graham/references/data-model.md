# Paul Graham content model

只描述頁面結構，不保存本輪的文章正文、Quote 內容、清單數量、公告、token 或當前排名。

## Entities

| Entity | Purpose | Stable fields / signals | Related pages |
| --- | --- | --- | --- |
| SitePage | 任一同站 HTML 頁面 | route、title、visible label、page type、outbound links、internal links | `/`、所有 sidebar routes |
| Essay | 一篇文章 | title、route、date（若頁面顯示）、image alt、intro、body、footnote anchors、related links | `/articles.html`、`/ind.html`、`/<essay>.html` |
| EssayIndexEntry | Index 中可選取的內容項目 | visible title、href、目前字母段落、Prev/Next state | `/ind.html` 與後續 index pages |
| Book | 書籍介紹 | title、detail route、cover image、description、publisher/year/pages/ISBN（若可見）、review links、buy links | `/books.html`、`/onlisp.html`、`/acl.html`、`/hackpaint.html` |
| ProjectHub | 技術／主題導覽 | hub title、description、internal child links、external resources | `/arc.html`、`/bel.html`、`/lisp.html`、`/antispam.html` |
| ReferencePage | FAQ、RAQ、Quotes、Bio、RSS、Email 等內容頁 | title、section/list entries、definition or guidance text、internal/outbound links | `/faq.html`、`/raq.html`、`/quo.html`、`/rss.html`、`/bio.html`、`/info.html` |
| ExternalResource | 同站頁面指向的外部內容 | visible label、destination origin、purpose、whether action is read-only | Amazon、Y Combinator、外部 feed、forum、CDN text files |

## Relationships

```text
Home
├── Essays ──> Essay list ──> Essay ──> footnote / related links
├── Index ──> EssayIndexEntry ──> any SitePage
├── Books ──> Book ──> publisher / buy ExternalResource
├── ProjectHub ──> internal child pages or ExternalResource
└── ReferencePage ──> FAQ/RAQ/Quote/Bio/RSS/Email content
```

## Dynamic fields

- 首頁 `New` 公告與 YC CTA。
- Essay 清單的順序、最新文章、正文、日期與外部資源 availability。
- Index 的目前分頁內容與頁數。
- Quotes、FAQ／RAQ 條目與外部連結是否仍可用。
- Bel 的 CDN 時間／查詢參數與資源內容。

對這些欄位，重新開目的頁並以當次 UI 顯示為準；不要從 URL pattern、舊文件或記憶中補值。
