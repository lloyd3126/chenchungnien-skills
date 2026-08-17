# vocus Salon Studio Controls

Only use these controls when the current tab visibly shows an authenticated Studio shell. Route parameters are observed patterns, not a substitute for verifying the selected tab.

| Area | Read-only route states | Verify | Do not activate |
| --- | --- | --- | --- |
| Statistics | `statistics?tab=general`, `statisticsChart`, `incomeAnalyze` | date range, selected tab, metrics/table/chart/empty state | CSV/export unless requested |
| Collections | `collections?status=0`, `2`, `1`, `3` | draft/published/scheduled/private state, row headings, pagination | create, import, edit, publish, schedule, delete |
| Plans | `plans?tab=content`, `product`, `donate`, `advertisement` | plan rows, status, prices/labels, sponsor/ad state | create/edit plan, change revenue/ad status |
| Members | `members?tab=member`, `blacklist` | filter, member table or empty state | add, block/unblock, export, expose identities |
| Earnings | `earnings?tab=salon`, `donate`, `collaboration`, `ad`, `orders` | period, income detail, order filter, empty state | withdraw, submit payment/identity data |
| Settings | `setting?tab=basic-setting`, `home-setting`, `room-setting`, `auth-setting`, `role-and-payment` | fields, layout, rooms, permissions, identity/payment notices | save, upload, add room/member, change permissions, create payment method |

## Verification

For each page, retain the final route/query, title or heading, selected tab, one filter/date state or empty state, and one table/card. Never write account-specific names, member identities, sponsor URLs, income amounts, tax/bank data, or current dashboard metrics into reusable references.
