# Threads Search Controls

## Confirmed controls

| Control | Observed behavior | Verification |
| --- | --- | --- |
| `搜尋` searchbox | Accepts free text; Enter produced `/search?q=<query>&serp_type=default` | Searchbox retains the query and result tabs are visible |
| `最相關` | Default result view | URL keeps `serp_type=default` without `filter` |
| `最近` | Recent result view | URL adds `filter=recent`; result may legitimately be empty |
| `個人檔案` | Profile result view | URL adds `filter=profiles`; profile cards expose public profile links and `追蹤` buttons |
| `篩選` | Opens a menu | Visible options were date-after, date-before, and from-profile |
| `指定日期之後` | In the observed state immediately added a current-date chip | Verify chip text and `清除`; do not assume a date until the current picker exposes it |
| `清除` | Removes the date chip | Confirm the chip disappears and query state returns to the previous result state |

## Route patterns

- Keyword: `/search?q=<encoded-query>&serp_type=default`
- Recent: same query plus `filter=recent`
- Profiles: same query plus `filter=profiles`
- Topic/tag: `/search?q=<term>&serp_type=tags&tag_id=<id>` as exposed by visible topic links
- Trends: `/search?q=<term>&serp_type=trends&trend_fbid=<id>` as exposed by visible trend cards
- Author search candidate: `/search?from_author=<username>` was visible on a profile but a click did not produce a confirmed transition in one run; verify current behavior before relying on it.

## Safe test pattern

1. Use a non-sensitive representative query.
2. Wait for loading statuses to settle.
3. Inspect heading/URL/searchbox/result state.
4. Apply one filter at a time.
5. Re-read the state after each filter and clear temporary filters before leaving the page.

Do not copy current query results, trend counts, profile counts, or post text into durable guidance.
