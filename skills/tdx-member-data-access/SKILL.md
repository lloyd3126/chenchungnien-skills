---
name: tdx-member-data-access
description: Safely inspect authenticated TDX member workflows for API/MQTT keys, service-access permissions, usage statistics, historical-data applications, application carts, and subscription status in the Codex in-app browser. Use when the user asks about their TDX account data, key limits, enabled services, usage history, or application progress; do not use it to enter credentials or perform purchases, deletions, or submissions without explicit action-time approval.
---

# TDX Member Data Access

## Purpose and session gate

Use this skill only when the current TDX tab visibly shows an authenticated member session, such as `會員中心`, `登出`, and the auto-logout countdown. The main routes are:

- `/user/dataservice/key` — API/MQTT access keys and key guidance.
- `/user/dataservice/access` — enabled and approval-required service families.
- `/user/dataservice/statistics` — per-key usage statistics.
- `/user/apply/history` — historical/ticket application records and file status.
- `/user/apply/cart` — pending application list.
- `/user/memberService/manage` — current subscription and points overview.
- `/user/memberService/getEditAuth` — password-protected account branch.

Load [member-workflows.md](references/member-workflows.md) when the user needs field semantics, statuses, or a safe stopping boundary.

## Procedure

1. Confirm the visible authenticated state and preserve the current session. If the tab is not visibly authenticated, finish any public task first and ask the user to sign in manually in this same tab; do not enter passwords.
2. Choose the route that matches the user's intent. Prefer the page's visible navigation or a route already confirmed in the site map/sidebar; do not guess account URLs.
3. After each navigation, visually verify the same tab and confirm the page heading, selected controls, URL, and result state. An empty table means no visible records, not that the feature does not exist.
4. Re-fetch current account values, enabled services, statistics, application statuses, points, and dates at task time. Never persist live identifiers, Client Secrets, passwords, private records, or current counts in instructions.
5. Stop before any irreversible or representational boundary: creating/deleting keys, applying for access, submitting a form, purchasing/upgrading, downloading a user-specific file, changing account settings, or entering a password.

## Workflows

### Inspect API/MQTT keys

1. Open `/user/dataservice/key` and read `API金鑰使用說明` and `MQTT金鑰使用說明` before interpreting a key row.
2. API keys consist of Client Id and Client Secret and use OIDC Client Credential authentication. The page states that each member may create at most three API keys; subscription level controls call frequency.
3. MQTT uses ClientId, account, and password to authenticate and then subscribes to topic names. Treat these as sensitive credentials.
4. Record only non-secret properties needed by the user: key type, masked identifier presence, creation/status labels, and the route for `查詢用量`. Do not click `刪除` or change `管理` state during inspection.

### Inspect service access

1. Open `/user/dataservice/access`.
2. Separate `免審核提供資料` from `需審核提供資料`. The page shows enabled families such as basic, advanced, premium, historical, tourism, weather, and MaaS, and approval-gated families such as ticket, GTFS Beta, booking/dispatch integrations, and shipping.
3. For each family, verify the current status and the visible `申請使用服務` or `查詢服務使用歷程` action. Do not submit an application as part of a read-only task.

### Inspect usage statistics

1. Open `/user/dataservice/statistics`.
2. Use the `金鑰名稱` selector to choose all keys or one key. Use the `月`, `季`, or `年` period buttons, then verify the year/month/quarter inputs and press `查詢` only when the user requests a query.
3. Report the selected period and key scope with the result. A visible `無資料` state is a valid result; do not replace it with public statistics.

### Inspect historical applications

1. Open `/user/apply/history` and read the page's rules before interpreting a row.
2. Use the status filter only for a user-requested read-only lookup. Durable status meanings include `候隊審核`, `資料準備中`, `產製完成`, `產製失敗`, `已購買`, `資料逾期`, `申請退回`, and `自行取消`.
3. The table can show item, application time, data interval, production progress, file size, estimated points, status, and management controls. Keep current rows out of durable guidance.
4. Historical files may be produced asynchronously and the site says completion is notified by email. Purchased historical/ticket files are available for 30 days from production completion; do not copy a download password or click a download unless the user explicitly requests that specific file action.

### Inspect cart and subscription

- `/user/apply/cart` lists selected services, data intervals, and management controls. An empty table is a normal state. Do not submit or remove items.
- `/user/memberService/manage` shows the current plan, next-cycle plan, discounts, and points usage. Treat all amounts, dates, and points as dynamic. Do not click payment, upgrade, renewal, or reduction controls.
- `/user/memberService/getEditAuth` is a password gate for account details. Stop at the prompt and hand the password entry back to the user.

## Safety and privacy

- Never record or reveal passwords, API Client Secrets, full Client Ids, email addresses, private account records, download passwords, or user-specific files.
- Login state does not authorize purchases, submissions, access requests, deletion, password entry, or account changes. Confirm at action time for any such operation.
- Keep public and authenticated observations separate. A route can show a different page after login, as `/data-service/gtfs` did during exploration; re-check the authenticated variant instead of copying public assumptions.
- Do not sign out or let an idle session expire intentionally. If the countdown is near expiry, stop and ask the user to take over.

## Drift maintenance

Before acting, compare the current visible authenticated UI, route, labels, controls, permissions, and first-party explanations with this procedure. If a stable behavior differs, safely complete only the requested read-only portion, record the old/new behavior, page variant, route, verification evidence, and date, and patch this skill or its reference when the change is clear. Never store dynamic values or secrets. Re-run the affected safe workflow and `quick_validate.py`; report ambiguous or broad changes instead of guessing.

## References

- [member-workflows.md](references/member-workflows.md) — route matrix, field semantics, status meanings, and confirmation boundaries.
