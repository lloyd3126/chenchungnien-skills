# FRED series page and data controls

## Confirmed series-page controls

| Control / field | Use | Verification |
| --- | --- | --- |
| `Observations` | Shows a recent observation sample and a `View All` link. | Confirm the series title/ID and the visible date/value rows. |
| `1Y`, `5Y`, `10Y`, `Max` | Selects a graph date range. | Confirm the selected range and chart axis after the change. |
| Calendar control | Provides a custom date-range entry point. | Re-check the visible date fields and resulting graph range. |
| `Edit Graph` | Opens graph customization. | Confirm selected series, transformation, frequency and chart state. |
| `Download` | Opens data/graph export choices. | Re-open the menu and verify the current format label before downloading. |
| `View as data table, Chart` | Exposes the chart as a data table. | Confirm table headers and values if the user needs a tabular chart view. |
| `Share Graph` | Sharing/representational action. | Do not use by default; requires an explicit user request and action-time confirmation at the external side-effect boundary. |

## Confirmed metadata

The series page and `/data/<series_id>` table can expose:

- title and series ID;
- current observation summary and updated timestamp;
- next release date;
- source and release links;
- units, frequency, seasonal adjustment and date range;
- notes, account codes, definitions and suggested citation;
- release tables and related data suggestions.

## Download menu observed in the GDP representative page

- `CSV (data)` — raw series data download.
- `Excel (data)` — spreadsheet data download.
- `Image (graph)` — graph image.
- `PowerPoint (graph)` — graph export.

The menu is stateful and its query parameters encode graph state, dates, transformation, frequency and vintage/revision dates. Never hard-code those parameters; select the current UI option and verify the resulting artifact.

## Data-table shape

`/data/<series_id>` has a metadata table followed by a table with `DATE` and `VALUE` columns. The metadata table includes at least title, series ID, source, release, seasonal adjustment, frequency, units, date range, last updated and notes in the observed variant.
