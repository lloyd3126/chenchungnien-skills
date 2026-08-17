# vocus Site Map and Coverage

## Evidence status

This inventory is based on the current Codex in-app browser session on 2026-08-17. Route patterns are durable hints; content and counts are dynamic.

| Page family | Confirmed route pattern | UI state observed | Coverage |
| --- | --- | --- | --- |
| Home | `/` and `/?tab=popular`, `/?tab=curated`, `/?tab=salons` | `精選`、`熱門`、`方格動態`、`我加入的沙龍` feed tabs | UI-verified / DOM-verified |
| Explore menu | `/topic`, `/latest`, `/global`, `/politics`, `/investment`, `/technology`, `/reading`, `/develop`, `/adult`, and other category paths | `探索` dropdown exposed exact labels and links | UI-verified for menu; representative pages partial |
| Search | `/search/content?keyword=<q>`, `/search/user?keyword=<q>`, `/search/salon?keyword=<q>`, `/search/tag?keyword=<q>` | Four result scopes; content type and sort controls | UI-verified / DOM-verified |
| Tag | `/tags/<tag>` | Heading, content count, content-type and sort controls, feed cards | DOM-verified |
| Article | `/article/<id>` | Heading, author, salon/room, dates, read time, TOC, body, tags, comments, sponsor entry | UI-verified / DOM-verified |
| Post | `/post/<id>` | Heading, author, body/media, reactions, comment composer and comment ordering | DOM-verified |
| Creator profile | `/user/@<handle>` or `/user/<id>` | Profile header, follow/sponsor entries, salon cards, published/achievement tabs, feed controls | DOM-verified |
| Public salon | `/salon/<slug-or-id>` | Header, member/content summary, Top 5, room sections, post/article cards, join entry | DOM-verified; screenshot control gap on heavy page |
| Salon room | `/salon/<slug>/room/<room>` | Discovered from visible salon navigation; not separately rechecked in this pass | Partial |
| Product list | `/product` | Featured and all products, categories, sort control, product cards | DOM-verified |
| Product detail | `/salon/<slug>/products/<product-id>` | Discovered from visible product cards; purchase flow not opened | Partial / purchase boundary |
| Studio setting | `/salon/<id>/studio/setting?tab=...` | Basic, home, room, permission, identity/payment tabs | DOM-verified |
| Studio statistics | `/salon/<id>/studio/statistics?tab=general|statisticsChart|incomeAnalyze` | Overview table, chart metrics, income analysis, CSV entry | UI-verified / DOM-verified |
| Studio collections | `/salon/<id>/studio/collections?status=...` | Draft, published, scheduled, private publication lists | DOM-verified |
| Studio plans | `/salon/<id>/studio/plans?tab=content|product|donate|advertisement` | Membership/product plans, sponsor, ads | DOM-verified |
| Studio members | `/salon/<id>/studio/members?tab=member|blacklist` | Member filters/list and blocked list | DOM-verified |
| Studio earnings | `/salon/<id>/studio/earnings?tab=salon|donate|collaboration|ad|orders` | Income summaries, details, withdrawals, orders | DOM-verified |

## Intentionally not followed

External social links, app deep links, payment or sponsor destinations, purchase confirmation, creator editor, imports, uploads, payout, account identity submission, and irreversible Studio actions were not executed.
