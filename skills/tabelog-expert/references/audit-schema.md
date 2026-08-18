# Tabelog Expert audit schema

Use this ledger internally while browsing. Keep live values in the task output, never in the skill.

## Request record

| Field | Required content |
|---|---|
| Retrieval | Date and timezone used for the live check |
| Scope | Exact area/station, visible autocomplete choice, and result URL |
| Target | User wording, normalized Tabelog keyword, synonyms, and false positives |
| Origin / route | User-provided origin, or `未指定`; whether the output should use a nearest-station walk estimate or an origin-to-store transit route |
| Intended opening | Month/date, weekday if known, calendar dates checked, and reservation controls ignored or used |
| Requested count | User-requested Top N, or default `3` when no count is given |
| Review window | Start/end dates and whether month-only dates limit precision |
| Decision state | Current route stage: request contract, inventory, hard-gate screen, evidence audit, official cross-check, state classification, or ranking |
| Format scope | Whether the request requires standalone retail/takeout, allows café/course formats, or leaves access open |
| Scenario map | The core lenses to report every time: overall pick, exact product/format, price/value, transport/route, availability/ease, best regardless of price/distance; add seasonal/period-limited, local/branch-limited, and established/signature when applicable. For future, seasonal, period-limited, local, or branch-limited requests also record official source, observation date, status, and consistency with Tabelog |
| Navigation integrity | After each navigation: visible title/heading, area, keyword/category, URL scope, and selected sort. Mark pass/fail; if two checks fail, record homepage recovery and route rebuild. |

## Candidate record

| Field | Allowed values or guidance |
|---|---|
| Identity | Name, branch, detail URL, live score, review count |
| Storefront | Physical address, observed distance from requested station, nearest station, facility/branch context, storefront yes/no/unclear |
| Transport | If no origin: nearest station and approximate walk time derived from observed distance, labelled approximate. If origin is provided: route source and observation date, total transit time, line(s), transfer count, station exit/final walk, and route verified/unverified. Never infer a route duration or transfer count. |
| Opening | Weekly hours, holidays, facility dependency, one of the four opening statuses |
| Product match | Exact, variant/seasonal, analog/like, wish-only, branch mismatch, unclear |
| Product format | Retail/takeout, café, course, hotel lounge, buffet, pop-up, wish-only |
| Product access | `standalone takeout`, `single-item dine-in`, `course dessert`, `bar/lounge dessert`, `seasonal pop-up`, `store takeout flag only`, `wish-only`, or `unclear`. A store-level takeout flag is not item-level takeaway proof. |
| Takeout evidence | `已確認可外帶`, `近期外帶紀錄`, `僅店家標示外帶`, or `外帶未確認`; only the first two are positive item-level evidence |
| Current evidence | Current text listed; current photo only; current menu not listed; unconfirmed |
| Official evidence | Official website or official SNS linked from Tabelog; exact item/variant, sale window, branch, format, hours/holiday or stock rule; source type, URL, observation date, status (`官方目前列出`, `官方近期公告`, `固定季節／販售期`, `歷年同期模式（今年未公告）`, `官方未確認`, `官方與 Tabelog 衝突`), and consistency with Tabelog. Prior-year recurrence is never current-year confirmation. |
| Review evidence | Newest visit month, detail-page visit month/date when exposed, publication date or `未取得`, exact item/price/context; preserve mismatches rather than collapsing dates |
| Service | Takeout, dine-in, reservation recorded independently |
| Freshness | Strong/current, Recent, Historical, Weak/non-qualifying |
| Confidence | High/medium/low plus the reason and unresolved caveat |
| Last checked | Observation date/time for live score, hours, menu, official source, or availability fields used in the decision |
| Qualification | Qualified / near-miss / excluded, with the first failed gate or unresolved uncertainty |
| Ranking boundary | Raw score rank, qualified rank, Top N candidate, boundary candidate, equal-score tie, or higher-scoring near-miss |
| Product-season state | `已確認`, `季節模式支持`, `條件式`, or `歷史／排除` for future seasonal/rotating items. Main pool may use the first two; `條件式` remains a labelled near-miss unless the user accepts it explicitly. |
| Review expansion | Expanded / not expanded / unavailable; preserve `內容未展開` when applicable |
| Scenario evidence | Exact product price and basis; venue budget band; nearest-station walk time or verified origin-to-store route; direct/indoor/transfer access; opening, stock, queue, and reservation friction; explicit local or branch-exclusive wording; award, signature, or established-shop signal; official current/announcement evidence kept separate from historical review evidence |
| Scenario winner | One or more applicable lenses won, or `未找到`; record the evidence and the trade-off rather than inventing a winner |

## User-facing delivery record

Keep these checks separate from the research ledger. They control how the evidence is presented, not how it is gathered.

| Field | Required content |
|---|---|
| Lead conclusion | Open with the recommendation and the decision-relevant limitation. Do not open with browser actions, search keywords, sort controls, page counts, or a research diary |
| Decision lenses | State the applicable trade-offs as recommendations. Do not render the internal scenario map as a process explanation or create a second full ranking |
| Future-month wording | Say whether the month is confirmed, supported by prior-year seasonality, conditional, or not confirmed. Never turn `今年未公告` into a current-year promise |
| Result count | Match the requested Top N. Return fewer only when fewer candidates pass the evidence gates, and explain the shortfall |
| Store naming | Use Traditional Chinese or a Taiwan-familiar transliteration. Let the Tabelog link carry the formal Japanese name |
| Link placement | Embed Tabelog, official-site, and SNS links in the sentence that uses the source. Do not add a separate link appendix |
| Format | First-person Traditional Chinese plain-text paragraphs. No Markdown headings, bullets, numbered lists, tables, bold, semicolons, or em dashes |
| Transport prose | Use nearest-station walking time without an origin. With an origin, use verified total time, lines, transfer count, station exit, and final walk |
| Caveat density | Give each candidate one primary caveat. Keep raw metres, unverified routes, internal labels, and method details out of the main prose unless they change the decision |

## Source note

For each material claim, retain:

```text
claim:
source_surface: official_site | official_sns | detail | menu_text | menu_photo | review_search | review_detail | search_result
url:
observed_at:
evidence_level:
freshness_or_visit_month:
official_status_or_consistency:
uncertainty:
```

For review dates, also retain:

```text
card_visit_month:
detail_visit_date_or_month:
publication_date:
date_reconciliation:
```

For navigation, retain:

```text
navigation_title_or_heading:
navigation_area:
navigation_keyword_or_category:
navigation_url_scope:
navigation_sort:
navigation_recovery:
```

For transport, retain:

```text
transport_origin:
transport_source_url:
transport_observed_at:
transport_total_time:
transport_lines:
transport_transfers:
transport_final_walk:
transport_route_status: verified | unverified | nearest_station_estimate_only
```

For a boundary candidate, retain the comparison reason against the nearest qualified candidate. For a near-miss, retain exactly one primary exclusion reason (for example `歷史曾出現`, `無實體店面`, `branch mismatch`, `analog-only`, or `指定日期未確認`) and any secondary caveat separately. Scenario advantages never override a failed qualification gate.

Do not treat search-card snippets, reservation vacancy, a missing menu entry, or a reviewer's wish as positive current product evidence.
