# TDX member workflow reference

## Session and privacy

The authenticated variant is confirmed by visible 會員中心, 登出, and an auto-logout countdown. Keep public and authenticated observations separate. Do not write live key identifiers, secrets, email addresses, current account counts, or private rows into durable files.

## Route matrix

| Intent | Route | Stable fields or controls | Safe stopping point |
| --- | --- | --- | --- |
| Inspect API/MQTT keys | /user/dataservice/key | API/MQTT tabs, Client Id/Secret guidance, creation/status labels, 管理, 查詢用量 | Do not create, delete, rotate, or reveal credentials |
| Inspect access rights | /user/dataservice/access | 免審核提供資料, 需審核提供資料, family status, 申請使用服務, history link | Read statuses; do not submit an access request |
| Inspect member usage | /user/dataservice/statistics | key selector, 月/季/年, year/period inputs, 查詢 | Query only when requested; report selected scope |
| Inspect applications | /user/apply/history | status filter, item/time interval/progress/size/points/status/management columns | Do not cancel, purchase, copy a download password, or download without a specific user request |
| Inspect pending cart | /user/apply/cart | selection, service, data interval, management columns | Do not submit or remove items |
| Inspect plan and points | /user/memberService/manage | current/next plan, renewal, discounts, points | Do not pay, upgrade, renew, or reduce |
| Account branch | /user/memberService/getEditAuth | password identity-verification prompt | Stop and ask the user to enter the password manually |

## Key semantics

- The key page says one member may create at most three API keys.
- Each API key has Client Id and Client Secret and uses OIDC Client Credential authentication.
- MQTT uses ClientId, account, and password, then subscribes to data-service topics.
- Subscription level affects call-frequency limits. Fetch the current pricing page when the user asks for the active limit.

## Access semantics

The access page separates membership-enabled families from approval-gated families. During exploration, enabled families were basic, advanced, premium, historical, tourism, weather, and MaaS; approval-gated families included ticket, GTFS Beta, Taiwan Rail booking, THSR booking, taxi dispatch, Taipei Bus Station booking, and shipping. These labels and statuses must be refreshed because the account can change.

## Usage semantics

The usage page supports all keys or one key and month, quarter, or year scopes. The default period values are current and therefore dynamic. Verify the chosen key and period in the UI before reading a chart or 無資料 state.

## Historical application semantics

The application-history explanation states:

- Historical files may take time to produce; completion is notified by email.
- Historical and ticket services use different point rules and approval paths; read the current page explanation before calculating anything.
- Purchased historical/ticket files are available for 30 days from production completion.
- The page instructs users to copy a download password before opening the download page. That password is sensitive and must never be recorded or exposed.

## Confirmation boundaries

Always stop and request action-time confirmation before creating/deleting keys, submitting an access or historical-data application, purchasing data, changing a subscription, downloading a private/user-specific file, changing account details, or entering a password. Reading a page, changing a local selector, and inspecting an empty table are safe.

## Drift maintenance

Compare the current route, labels, controls, permissions, and first-party explanations with this reference before acting. Record verified stable mismatches with page variant, route, old behavior, new behavior, evidence, and date; patch the owning skill when clear. Never replace a retrieval rule with a current account value or secret. Re-run the affected safe workflow and the skill validator.
