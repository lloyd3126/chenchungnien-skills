---
name: vocus-studio
description: Inspect authenticated vocus Salon Studio analytics, content management, plans, members, earnings, and settings in read-only mode. Use when a user asks to review a salon dashboard or understand a Studio page without changing account or public content state.
---

# Vocus Salon Studio

Use this skill only when the current vocus tab visibly shows an authenticated Salon Studio session. Read [the site guide](../../sites/vocus/AGENTS.md), [studio-pages.md](../../sites/vocus/references/studio-pages.md), and [studio-controls.md](references/studio-controls.md) first.

## Procedure

1. Confirm the current tab shows the Studio shell, salon identity, and a Studio heading. Do not infer authentication from a route alone. If the session is not visibly authenticated, stop and ask the user to sign in manually in the same tab.
2. Navigate through visible Studio sidebar links or the exact same-origin route. Verify route query, title/heading, selected tab, date/filter state or explicit empty state, and one representative table/card.
3. Use the route family that matches the request:
   - `statistics?tab=general|statisticsChart|incomeAnalyze` for summary tables, charts, and income analysis.
   - `collections?status=0|2|1|3` for draft, published, scheduled, or private content lists.
   - `plans?tab=content|product|donate|advertisement` for monetization plans and settings.
   - `members?tab=member|blacklist` for member filters and blocked-list state.
   - `earnings?tab=salon|donate|collaboration|ad|orders` for income and order views.
   - `setting?tab=basic-setting|home-setting|room-setting|auth-setting|role-and-payment` for salon configuration.
4. Read only the requested visible fields. Metrics, members, earnings, prices, dates, and statuses are current/private data; summarize their labels and state without storing account-specific values in reusable files.
5. If a CSV, export, upload, save, create, or status-change control appears, stop before activating it and obtain explicit user direction if the task actually requires that mutation.

## Hard safety boundary

Never create, edit, publish, schedule, delete, import, upload, add members/rooms/plans, change permissions or ad/revenue status, provide identity/tax/bank data, create payment methods, request withdrawal, or expose private member/payment/account details during a read-only task. Do not copy private sponsor URLs or real account names into notes.

## Verification and drift

Dashboard data is volatile. Re-fetch the requested date range, filters, selected tab, table state, and empty state for every task. If a heavy page times out, retry in the same tab and report whether the result is UI-verified, DOM-verified, blocked, or partial. Do not treat a route transition alone as evidence that the page loaded.

## References

- [studio-controls.md](references/studio-controls.md) — safe read-only route matrix and mutation boundaries.
- [studio-pages.md](../../sites/vocus/references/studio-pages.md) — Studio page families and fields.
- [data-model.md](../../sites/vocus/references/data-model.md) — MetricSnapshot, ContentRecord, Plan, MemberRecord, and EarningRecord.
- [interaction-rules.md](../../sites/vocus/references/interaction-rules.md) — authentication and side-effect rules.
