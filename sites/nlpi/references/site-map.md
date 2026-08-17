# 國資圖站內導覽與頁型

## Evidence and inventory status

`/SiteMap` 由目前首頁主選單的「網站導覽」開啟，並在目前 Codex 內建瀏覽器分頁以畫面與 DOM 確認。它是本輪唯一取得的站內一方 inventory。`/robots.txt`、`/sitemap.xml`、`/sitemap_index.xml` 在同一分頁重試後均為 `client-blocked`，不能當成空內容。

## Stable route families

| Agent need | Verified entry | Route family | Owner |
| --- | --- | --- | --- |
| Website inventory | 網站導覽 | `/SiteMap` | `nlpi-site-search`／global routing |
| Site keyword search | 全站搜尋 | `/Search` | `nlpi-site-search` |
| Advanced site search | 進階搜尋 | `/AdvancedSearch` | `nlpi-site-search` |
| Activity discovery | 活動日曆 | `/ActivityInfo/recap` → `/ActivityInfo/recap/Search` | `nlpi-activity-search` |
| Activity detail | 活動卡片 | `/ActivityInfo/recap/Detail/<id>` | `nlpi-activity-search` |
| Borrowing guidance | 借還書說明 | `/StaticPage/borrowing-and-return` | `nlpi-member-center`／first-party reference |
| Digital resource guidance | 數位資源介紹 | `/StaticPage/resources-intro` | `nlpi-digital-resources` |
| Member dashboard | 會員中心 | `/member` → `/Member/myipac` | `nlpi-member-center` |

## Site map categories

The visible HTML site map groups the site as:

1. 關於我們 — overview, services, partnerships, disclosure, volunteers.
2. 我要借書 — 館藏查詢, 借閱證, 借閱規定, 館藏介紹, 館員推薦.
3. 到館資訊 — 樓層、開放時間、交通、參訪導覽.
4. 數位館藏 — 資源類型、主題、適用對象、本館精選、服務介紹.
5. 各項服務 — 分眾入口、線上申請、多元文化、FAQ、相關服務、無障礙.
6. 活動訊息 — 公告／新聞稿、全館活動、主題活動.
7. 會員中心.
8. 影音管理.
9. 其他 — 網站導覽、全站搜尋、進階搜尋、政策與 RSS.

These are routing categories, not proof that every child route is currently accessible or public. Reopen a visible link before relying on it.

## Cross-site handoffs

The homepage and authenticated member dashboard expose links to `ipac.nlpi.edu.tw`, `ebook.nlpi.edu.tw`, `ers.nlpi.edu.tw`, `vod.nlpi.edu.tw`, `activity.nlpi.edu.tw`, `ispace.nlpi.edu.tw`, `tour.nlpi.edu.tw`, `irental.nlpi.edu.tw` and other partner systems. Member dashboard service cards use same-site `/Member/go/<service>` redirect routes with `_blank` and `noopener noreferrer`. The present exploration did not switch to those new tabs; treat them as handoff points and re-establish the target site's own UI and session rules if a user explicitly requests that platform.

## Page taxonomy

- **Landing / folder page**: `/Folder/<slug>`; groups related services and child links.
- **Static guidance**: `/StaticPage/<slug>`; first-party definitions, policy, instructions, or resource introductions; preserve tabs and visible sub-navigation.
- **Search page**: `/Search`, `/AdvancedSearch`, and activity search routes; query state and result count are dynamic.
- **Activity list**: `/ActivityInfo/recap` or `/ActivityInfo/recap/Search`; year, time, audience, topic, keyword and pagination controls.
- **Activity detail**: `/ActivityInfo/recap/Detail/<id>`; title, images, date, place, audience, body, tags, sessions and external registration links.
- **Authenticated dashboard**: `/Member/myipac`; service launch cards, borrow/reservation tabs and record entry links.
