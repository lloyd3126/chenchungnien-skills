---
name: koyfin-watchlists-and-screens
description: Use Koyfin through the Codex in-app browser to safely inspect authenticated My Watchlists, My Screens, My Portfolio, My Dashboards, and My Graphs. Trigger when a user asks to read or filter their Koyfin workspace; default to read-only and stop before save, edit, share, import, delete, download, or portfolio mutations.
---

# Koyfin watchlists and screens

## Purpose and entry point

This skill handles Koyfin's personalized `My Koyfin` workspace. It assumes the current tab may be authenticated and may expose sensitive user data. Use visible workspace links and IDs; never guess a list, screen or dashboard ID and never copy live records into reusable guidance.

## Procedure

1. Inspect the current tab, visible account state and selected workspace. Preserve the same in-app browser tab.
2. Choose the visible entry point:
   - `My Watchlists` `/myw/<watchlist-id>` for table/list inspection.
   - `My Screens` `/mys/<screen-id>` for criteria and result-table inspection.
   - `My Portfolio` `/myp/pl` for read-only Profit/Loss, Exposure and analysis tabs.
   - `My Dashboards` `/myd/<dashboard-id>` for panel/table/chart inspection.
   - `My Graphs` `/myg` only when the current visual state is stable; this route was partial in the exploration.
3. Use safe controls: search filter, clear/reset, table view, column selection, summary/group/sort/currency dropdowns, read-only tabs, and panel expansion. Verify the selected list/screen/dashboard before interpreting results.
4. For a screen, inspect `Hide Criteria` or open `Modify Criteria` to read the universe, filters and Screen Name, then choose `Cancel`. Do not click `Save and Apply`.
5. For a watchlist, a representative search filter can narrow the table; confirm the visible row and clear the text field before finishing.
6. For a portfolio or dashboard, read only the fields needed for the task and explicitly avoid `Edit Portfolio`, `Edit dashboard`, `Delete dashboard`, `Remove`, or any account/workspace mutation.
7. Report the workspace name, selected view, filters, observation time and what was actually visible. Treat all rows and values as private, dynamic task evidence.

## Page and field semantics

- Watchlists expose a selected list, table views, groups, columns, summary, sort, currency and ticker search. `Manage Watchlists`, `Duplicate`, `Share`, `Download` and `Create new watchlist` are boundary actions.
- Screens expose a query builder with a universe, criteria, Screen Name and a result-table cap. The observed dialog states that only the top 2,000 results sorted by Market Cap are displayed; this is a UI limit, not a complete result-set claim.
- Portfolio views can include holdings, account, purchase date, quantity and average cost. These are sensitive account records; do not repeat them unless the user asked for the immediate answer.
- Dashboards are collections of panels such as tables and charts. Panel controls like Full View, Remove and dashboard edit/delete are not read-only.
- My Graphs may show an error or empty state depending on session/page loading. Verify the current visual before relying on it.

## Safety and limits

- Do not click `Save`, `Save and Apply`, `Create`, `Edit`, `Delete`, `Duplicate`, `Share`, `Import`, `Download`, `Export`, `Add Ticker`, `New Group`, `Edit Portfolio`, `Remove`, alerts, notes or add-to-watchlist actions unless explicitly requested.
- Do not reveal or persist holdings, watchlist entries, personal notes, alerts, dashboard contents, account names or current values in site docs.
- A filter that returns no row is not proof of an empty workspace; check the active list, search text, universe, loading state and permissions.

## Drift maintenance

- Compare the current visible workspace name, controls, permissions and safety boundaries with this procedure.
- If a stable control or route changes, re-run a read-only interaction and update the reference; do not “test” a mutation just to confirm its behavior.
- Keep the authenticated workspace variant separate from public Koyfin research routes.

## References

- [workspace-controls.md](references/workspace-controls.md) — safe controls, mutation boundaries and workspace-specific verification.
