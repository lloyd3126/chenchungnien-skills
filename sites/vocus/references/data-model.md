# vocus Data Model

## Core entities

| Entity | Identifier / route | Important fields | Relationships |
| --- | --- | --- | --- |
| Content | Article `/article/<id>` or Post `/post/<id>` | title, body, media, author, salon, room, published/updated time, tags, read time, access marker, reaction/comment controls | belongs to Creator and often a Salon/Room; appears in Home, Search, Tag, Profile and Salon feeds |
| Creator | `/user/@<handle>` or `/user/<id>` | display name, avatar, bio, followers, social links, sponsor entry, published content, achievements | owns or participates in Salons; authors Content; may be represented by a Salon card |
| Salon | `/salon/<slug-or-id>` | name, avatar/logo/cover, member count, content count, description, rooms, Top 5, public/private access state | contains Rooms and Content; has public page and authenticated Studio |
| Room | `/salon/<slug>/room/<room>` | name, description or section role, content list, access state | belongs to Salon; Content can be published into a Room |
| Product | `/salon/<slug>/products/<product-id>` | name, current/original price, seller Salon, reviews, sales/view metadata, access/purchase state | belongs to Salon; listed in `/product`; purchase is an external side-effect boundary |
| SearchResult | `/search/<scope>?keyword=<q>` | query, scope, result card, type, sort, route state | resolves to Content, Creator, Salon or Tag entities |

## Studio entities

- `MetricSnapshot`: date range, members, views, reads, completion rate, content, likes, saves, comments; values are dynamic.
- `ContentRecord`: draft/published/scheduled/private state, title, room, updated/published time, engagement columns and pagination.
- `Plan`: membership or product plan, name, paid/unpaid counts, status, visibility, product price and review state.
- `MemberRecord`: member identity, plan, next billing date, join duration, comments and status; never persist personal names or payment details.
- `EarningRecord`: salon, sponsor, collaboration, ad or order income; month, gross/third-party/platform adjustments, tax and withdrawal state; values and account details are dynamic and sensitive.
- `SalonSetting`: basic information, home layout slots, rooms, permissions, identity and payment configuration.

## Retrieval relationships

`SearchResult → Content → Creator / Salon / Room → related Content`

`Product → Seller Salon → public Salon page`

`Salon → public page / Rooms → authenticated Studio → Metrics, ContentRecords, Plans, Members, Earnings`
