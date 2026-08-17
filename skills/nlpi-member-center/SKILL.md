---
name: nlpi-member-center
description: Read and navigate the authenticated National Library of Public Information member center in the Codex in-app browser. Use when the user asks about borrowing/reservation tabs, member record entry points, or the library's authenticated service cards; never register, renew, reserve, log out, or enter credentials during ordinary lookup.
---

# 國資圖會員中心

## Purpose and entry point

Use only the Codex in-app browser. Start from a visible authenticated `會員中心` page or `/member`. Confirm that the page visibly shows an authenticated member state before reading account-scoped content. Read [member-services.md](../../sites/nlpi/references/member-services.md) for card routes and known gaps.

## Procedure

1. Inspect the current tab and confirm the heading, URL, and visible login state. In the explored authenticated variant, `/member` led to `/Member/myipac`.
2. Read the service cards and record-navigation row without opening new tabs. Card links use `_blank` and are handoffs to other platforms; route those platforms only when the user explicitly asks for them.
3. For borrowing and reservations, use the `我的借閱及預約` section and select `我的借閱` or `我的預約`. Verify the selected tab and current list state.
4. For space, ebook, or activity history, use the visible links `空間預約資訊`, `我的電子書紀錄`, and `活動報名紀錄`. Re-check the resulting heading/URL and treat an error page, unchanged dashboard, or client block as an access gap—not as an empty record.
5. Report only the current user-requested fields. Do not repeat private record contents in reusable files.

## Safety and limits

- Do not click `登出`, `報名`, `借閱`, `續借`, `預約`, `儲存`, delete, or account-change controls during discovery.
- Do not inspect or enter passwords, OTPs, cookies, local storage, or unrelated personal data.
- The current exploration saw an `Unexpected Error` page for `/Member/myispace` and `/Member/myactivity`; `/Member/myebook` did not leave the dashboard and a direct same-tab retry was client-blocked. Recheck these routes at task time.
- Do not assume a service-card click succeeded: those links target a new tab and the external service's own session and safety rules apply.

## Drift maintenance

Before acting, compare the current authenticated dashboard, cards, tab labels, routes, permissions, and record states with this skill. If a stable difference appears, use the live UI safely, document public/authenticated variant, evidence and date, update this skill or its reference, and run `quick_validate.py`. Keep user records and dynamic values out of reusable guidance.

## References

- [member-services.md](../../sites/nlpi/references/member-services.md) — dashboard and cross-site handoffs.
- [first-party-guidance.md](../../sites/nlpi/references/first-party-guidance.md) — borrowing semantics.
