# 國資圖可重用資料模型

## Entities

### Website page

An internal page is identified by its visible heading plus current path. Common page types are folder, static guidance, search, activity list, activity detail, and member dashboard. A route found in `/SiteMap` is only an inventory candidate until the page is visually opened.

### Search query

| Field | Meaning | Source |
| --- | --- | --- |
| `keyword` | User-entered keyword for site or activity search | visible textbox |
| exact phrase | Phrase that must match exactly | advanced search field |
| any words | Words that may appear | advanced search field |
| OR expression | Uppercase `OR` expression and exclusion syntax | advanced search helper text |
| query state | Path, query string, hash, retained input, result count | current page |

The site search may be rendered through Google Custom Search, so the result body and URL hash can be separate from the host page's path.

### Activity

An activity detail has a current visible title, image(s), activity date or date range, location, audience, body, tags, optional sessions table, optional Google Calendar link, optional external registration link, and previous/next/list navigation. All dates, availability, registration state, and counts are live values.

### Member account and records

The authenticated dashboard exposes a member session, service launch cards, `我的借閱` and `我的預約` tabs, and links for space booking, ebook history, and activity registration history. Borrowing, reservation, ebook, and activity records are account-scoped dynamic entities; do not store their values in reusable docs.

### Digital resource service

A digital resource service is described by a first-party introduction page and may hand off to a separate platform. Examples include the public-library digital resource portal, the ebook platform, digital archive, online video, and partner databases. Important fields are service name, subject/category, eligibility, login path, external URL, and whether the action is read-only or requires authentication.

## Relationships

```text
SiteMap / homepage
  ├── SearchQuery ──→ Website page results
  ├── Activity filters ──→ Activity list ──→ Activity detail ──→ registration handoff
  ├── Digital resource guidance ──→ Digital resource service ──→ external platform
  └── Member dashboard ──→ account records / service handoffs
```

## Retrieval rule

Use visible links and current controls to resolve entities. Do not infer a current activity, result, record, or service status from an old URL, stored count, or a Sitemap entry. For reports, preserve the query/filter/date context and cite the page that supplied the field.
