---
name: statementdog-watchlist
description: Inspect Statement Dog's signed-in tracking feeds, stock portfolios, notifications, and account settings through the Codex in-app browser without mutating the account. Use when the user asks about their tracked stocks, tracking lists, account plan, or login-dependent Statement Dog workspace.
---

# Statement Dog watchlist and account

Use this skill for login-dependent personal workspace pages. It is intentionally read-oriented: inspect the user's current tracking data and account state without changing it.

## Authentication gate

Use only the Codex in-app browser and the user's existing Statement Dog tab. A visible authenticated state is confirmed by account controls such as `登出`, `我的追蹤`, or personal tracking data. If it is already visibly authenticated, do not ask the user whether to explore login-dependent functions; continue directly through safe read-only paths.

If authentication is not visible, complete any public work first and ask whether the user wants protected exploration. The user must perform sign-in manually in the in-app browser. Never request or handle credentials, one-time codes, or passwords in chat.

## Routes and workflow

1. `/feeds` — inspect `所有追蹤動態`, `追蹤股組合`, tracked-stock summaries, and related news. Record the current update state because the feed is dynamic.
2. `/portfolios` — inspect tracking-list names, the `新增個股`/`修改清單名稱` controls, and the table fields such as stock name, price, change, P/E, dividend yield, P/B, and delete affordance. Opening a modal to understand its fields is safe; do not confirm it.
3. `/users/account` — inspect the types of account fields, plan information, newsletter state, and available settings. Do not expose private email or other account values unnecessarily.
4. Use the account menu to identify `帳號設定`, `用量與付款`, `重設密碼`, and `登出`; the account page may label the same password area `修改密碼`. Do not open or execute payment, password, logout, or destructive flows unless the user explicitly asks.
5. If a tracked stock needs analysis, route it to `/analysis/<ticker>` and use `statementdog-stock-analysis`. Keep private tracking state separate from public company facts.

## Verification and safety

Confirm the visible heading, selected list, or table state before reporting it. Watchlist membership, feed items, notifications, plan status, and usage are dynamic; do not hard-code them into a skill or reference.

Do not add or remove stocks, rename lists, save filters, follow/unfollow, change profile or newsletter settings, submit comments, purchase a plan, change a password, or log out during exploration. If the user later requests a mutation, describe the final action and obtain confirmation immediately before it.

Avoid copying private email addresses, account identifiers, or personal feed details into repository artifacts. Report only the minimum information needed for the user's request.

## Drift maintenance

If the account controls or protected routes differ, use the current visible UI safely, note the difference, and update this skill or `sites/statementdog/references/site-map.md`. If the page is logged out, blocked, or asks for a challenge, report the boundary and wait for the user rather than bypassing it.

## References

- `sites/statementdog/references/site-map.md` — authenticated routes and account-menu coverage.
- `sites/statementdog/references/data-model.md` — watchlist and account entities.
- `sites/statementdog/references/form-controls.md` — protected forms and safe interaction boundaries.
