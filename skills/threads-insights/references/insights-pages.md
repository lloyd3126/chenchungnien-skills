# Threads Insights page map

This reference records stable routing and controls observed in the authenticated Threads web UI. It does not record current metrics, rankings, dates, or account data.

## Dashboard

| Surface | Observed route | Stable controls or content | Verification notes |
| --- | --- | --- | --- |
| Insights dashboard | `/insights/` | Heading `洞察報告`; date button; links for `瀏覽次數`, `互動次數`, `追蹤者`, and posts/popular content | UI-verified with the visible authenticated account |
| Date range | `/insights?days=<n>` | `過去7天`, `過去14天`, `過去30天`, `過去90天` | UI-verified; preserve the selected range when drilling down |
| Views detail | `/insights/views?days=<n>` | `總瀏覽次數`, `查看來源`, source labels such as `其他`, `搜尋`, `首頁` | UI-verified; values are dynamic |
| Interactions detail | `/insights/interactions?days=<n>` | Heading and date control; interaction breakdown may load asynchronously | Route and control UI-verified; loading state observed during one capture |
| Followers detail | `/insights/followers?days=<n>` | Heading and date control; follower breakdown may load asynchronously | Route and control UI-verified; loading state observed during one capture |
| Posts detail | `/insights/posts?days=<n>` | `熱門內容`, `貼文`, `瀏覽次數`, `所有貼文` | UI-verified; an empty date-range state is possible |

## Safe reading procedure

1. Confirm authentication and page readiness.
2. Select or verify the date range, then verify the URL query.
3. Open one detail link at a time and retain the same range.
4. Separate loaded content, empty state, and skeleton loading in the report.

## Boundaries

The exact metric definitions, aggregation windows, ranking algorithm, export behavior, weekly recap content, and all settings were not established by this exploration. Do not infer them from labels alone.
