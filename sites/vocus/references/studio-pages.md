# vocus Salon Studio Pages

Only use these routes when the current vocus tab visibly shows an authenticated Studio session. Read labels and structures, but do not persist account-specific values.

| Area | Route/query | Safe read-only fields | Boundaries |
| --- | --- | --- | --- |
| Settings | `/studio/setting?tab=basic-setting` | name/intro field labels, logo/avatar/cover/share image slots, custom URL, adult-content flag, about-page entry | file selection, checkbox changes and `儲存` are state changes |
| Home settings | `?tab=home-setting` | layout slots: banner, link slot, Top 5, products, rooms; `瀏覽首頁` | `新增版位` and layout edits change public presentation |
| Room settings | `?tab=room-setting` | room name, members, paid members, content count, functions | add/reorder/edit/delete room |
| Permission settings | `?tab=auth-setting` | member, permission, start date, status and function columns | adding/removing members or changing permissions |
| Identity/payment | `?tab=role-and-payment` | identity source, verification notice, payment-method flow, review time and privacy notice | never enter/upload identity, bank or tax data |
| Statistics | `/studio/statistics?tab=general` | summary metrics, content table, filters, pagination, CSV entry | values are dynamic; do not export unless requested |
| Statistics chart | `?tab=statisticsChart` | date comparison, metric cards, chart dimension, day/week/month, last-updated signal | current values are dynamic |
| Income analysis | `?tab=incomeAnalyze` | date comparison, salon/sponsor/ad cards, plan tables, empty state | do not change payment or revenue settings |
| Collections | `/studio/collections?status=0|2|1|3` | draft, published, scheduled and private lists, title, room, engagement columns | create, import, edit, schedule, private/publish/delete |
| Plans | `/studio/plans?tab=content|product|donate|advertisement` | membership/product plan rows, prices/status/review/order columns, sponsor copy fields, ad placement state | create plan, edit sponsor text, change ad/revenue status |
| Members | `/studio/members?tab=member|blacklist` | member filters, plan state, billing date, join days, comments, blocked-list empty state | member identity is private; block/unblock or export only with explicit task |
| Earnings | `/studio/earnings?tab=salon|donate|collaboration|ad|orders` | income summaries, month, adjustments, detail table, order filters, withdrawal history entry | do not submit identity/payment, withdraw, or expose account-specific data |

Verify each page with route, title/heading, selected tab, date/filter state or explicit empty state, and one representative table/card. Do not infer permissions from an icon or route alone.
