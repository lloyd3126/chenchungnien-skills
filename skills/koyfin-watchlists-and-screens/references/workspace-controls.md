# Koyfin workspace controls

## Read-only control map

| Workspace | Safe inspection | Boundary actions |
| --- | --- | --- |
| My Watchlists | Search filter, clear text, table view, column selection, summary, group, sort, currency, read rows | Manage, Duplicate, Share, Download, Create new watchlist, Add Ticker, New Group |
| My Screens | Hide Criteria, read criteria/result table, open Modify Criteria, inspect tabs/rows, Cancel | Save as watchlist, Share, Download, Create new screen, Save and Apply |
| My Portfolio | Profit/Loss, Exposure, Hypothetical Performance, Analysis, Risk, Holdings Matrix, Scatter Plot when enabled; read table controls | Edit Portfolio, account changes, alerts, notes, imports or exports |
| My Dashboards | Open visible dashboard, read panels, wait for chart/table loading | Edit dashboard, Delete dashboard, Full View when it changes state, Remove, Share, Download |
| My Graphs | Only inspect a stable empty/list/chart state | Create new graph, Save As, Add Metric/Ticker if it commits state |

## Verification

- Before a workspace action, confirm the visible workspace/list/screen/dashboard label and current route.
- For a search/filter, record the input and verify a changed result plus the ability to clear/reset it.
- For a screen criteria dialog, record only criterion labels and structural operators needed to reproduce navigation; do not persist current threshold values unless the user explicitly needs them for the immediate answer.
- For a portfolio, minimize exposure of sensitive fields and avoid repeating account-specific rows.
- For a dashboard, identify panel title/type and loading completion; do not infer that a panel is absent from a transient loading or error state.

## Privacy and freshness

Workspace rows are user-specific and can change at any time. Do not store them in `AGENTS.md`, skills or references. When a task requires quoting a row, obtain it in the current session, state its scope and observation time, and avoid exposing unrelated holdings or account details.
