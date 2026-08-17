# 會員中心服務與限制

## Entry and dashboard

When the current page visibly confirms an authenticated session, `/member` resolves to `/Member/myipac`. The dashboard shows a welcome area, `登出`, horizontal service cards, a record-navigation row, and the `我的借閱及預約` section.

## Service cards

The visible cards and same-site launch routes are:

| Label | Launch route | Browser behavior |
| --- | --- | --- |
| 一證通整合平台 | `/Member/go/allpass` | `_blank`, `noopener noreferrer` |
| 館藏查詢 | `/Member/go/webpacx` | `_blank`, `noopener noreferrer` |
| 電子書服務平台 | `/Member/go/ebook` | `_blank`, `noopener noreferrer` |
| 預約訂位管理 | `/Member/go/srb` | `_blank`, `noopener noreferrer` |
| 數位資源入口網 | `/Member/go/ers` | `_blank`, `noopener noreferrer` |
| 線上視聽媒體中心 | `/Member/go/vod` | `_blank`, `noopener noreferrer` |
| 活動資訊平台 | `/Member/go/activity` | `_blank`, `noopener noreferrer` |

These are cross-site handoffs. The current website exploration did not switch to their new tabs, inspect credentials, or assume that a successful click means the target platform loaded.

## Account record navigation

- `我的借閱及預約` is the current dashboard section with tabs `我的借閱` and `我的預約`.
- `空間預約資訊` links to `/Member/myispace`.
- `我的電子書紀錄` links to `/Member/myebook`.
- `活動報名紀錄` links to `/Member/myactivity`.

The current session showed empty record lists in the main tabs. `/Member/myispace` and `/Member/myactivity` rendered the site's `Unexpected Error` page during exploration; `/Member/myebook` did not leave the dashboard when clicked and a direct same-tab retry was client-blocked. Preserve these as maintenance gaps and re-check them before reporting account records.

## Safety

Reading current records is account-scoped and should be limited to the user's explicit request. Never click `登出`, change account data, confirm a reservation, renew, borrow, save, upload, register, or send a form as part of discovery. Never repeat or store personal names, IDs, borrowing titles, messages, or record contents in reusable instructions.
