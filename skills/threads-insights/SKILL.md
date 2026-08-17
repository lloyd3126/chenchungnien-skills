---
name: threads-insights
description: Inspect authenticated Threads Insights for a selected date range, views, interactions, followers, weekly recap, and popular posts through the Codex in-app browser. Use whenever the user asks about Threads analytics, account performance, reach, engagement, follower changes, popular content, or a time-window comparison.
---

# Threads Insights

## Purpose and entry point

Use this skill for read-only inspection of the authenticated Threads analytics area. Start at the visible `洞察報告` entry or `https://www.threads.com/insights/`, and load [insights-pages.md](references/insights-pages.md) for the stable page map.

Before navigating, confirm in the Codex in-app browser that the page is Threads, the URL is on `threads.com`, the page has loaded, and the current session is visibly authenticated. If authentication is not visible, complete public exploration and ask the user to sign in manually before inspecting protected analytics. Never invent or reuse cached metrics.

## Workflow

1. Record the current URL, page title, heading, and loading state.
2. Inspect the date-range button. The observed options are `過去7天`, `過去14天`, `過去30天`, and `過去90天`; choose only the range requested by the user, or use the visible default when they did not specify one.
3. Verify the selected button and the resulting `?days=<n>` route before reading any metric. Preserve that range when opening `瀏覽次數`, `互動次數`, `追蹤者`, or `貼文` detail pages.
4. Read only labels, breakdown names, chart state, loading state, and post-list state that are visible in the UI. Distinguish empty date ranges from a still-loading dashboard.
5. Inspect `熱門內容` or `所有貼文` only when requested. Treat the date range and content type controls as part of the result context.
6. Inspect weekly recap or `顯示摘要` only when requested and only as a read-only view.
7. Report the route, selected range, visible labels, and page state. Do not report dynamic numbers without their range and metric label, and do not turn a transient value into a stable reference fact.

## Verification and safety

- Safe actions include opening detail pages and changing an analytics date filter.
- Do not edit a profile, publish, reply, message, follow, like, repost, save, delete, or change settings.
- If a page shows skeletons, an empty-state message, a redirect, or an error, record that state instead of retrying indefinitely.
- A successful route change is not proof that a metric loaded; verify heading, controls, and actual content separately.

## Drift maintenance

If labels, routes, date options, or detail links change, recheck the visible page and update [insights-pages.md](references/insights-pages.md) and the site map. Keep current metric values, rankings, and account-specific content out of the skill.

## References

- [Insights page map](references/insights-pages.md)
- [Threads site map](../../sites/threads/references/site-map.md)
- [Threads data model](../../sites/threads/references/data-model.md)
- [Threads operating guidance](../../sites/threads/AGENTS.md)
