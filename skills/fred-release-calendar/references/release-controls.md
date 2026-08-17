# FRED release catalog and calendar controls

## Release catalog

`/releases` is a paginated list of release names. The observed public variant exposes page links and `pageID` query parameters, and each release name links to `/release?rid=<rid>`. Treat release IDs and counts as dynamic; use the visible link rather than guessing an ID.

## Release calendar controls

| Control | Confirmed behavior | Verification |
| --- | --- | --- |
| Release combobox | Includes `All Releases` and named releases such as `Gross Domestic Product`; selecting GDP in the observed week produced the visible empty state `No release dates are available for the selected options.` | Confirm selected option and read either rows or the empty-state message. |
| `‹` / `›` | Moves the displayed calendar period. | Confirm the date-range heading and day headers. |
| `today` | Returns the calendar to the current period. | Confirm the heading reflects the current period. |
| `Date` / `Name` | Sorts release rows through visible links/query state. | Confirm active label and row order. |
| Calendar table | Shows date columns, release names, links and times. | Report the site's stated timezone: U.S. Central Time. |

## Limits and interpretation

- The footer note states that release dates are published by data sources and do not necessarily represent when data will be available on FRED.
- A release with no rows in the current window is an empty result for that filter/date window, not proof that the release has no schedule.
- Release detail and release table pages can have additional controls; open and verify them when the user asks for release-specific metadata or tables.
