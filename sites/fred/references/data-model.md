# FRED data model

## Core entities

| Entity | Identifier / route | Confirmed fields | Relationships |
| --- | --- | --- | --- |
| Series | `series_id`, `/series/<series_id>` | title, series ID, units, frequency, seasonal adjustment, updated time, next release, source, release, notes, date range, chart configuration | Belongs to a source and release; can appear in categories, tags, release tables and related-data suggestions. |
| Observation | series plus `/data/<series_id>` | `DATE`, `VALUE`; series table also exposes metadata and date range | Many observations belong to one series. Values can be revised; always re-fetch. |
| Release | `rid`, `/release?rid=<rid>` and `/releases/calendar` | name, release date/time, linked series/tables; calendar uses U.S. Central Time | Contains or publishes many series and may expose release tables. |
| Source | `soid`, `/source?soid=<soid>` | source name and linked series/releases | Provides attribution for a series; confirm the source on the series page. |
| Category | category ID, `/categories/<id>` | topic hierarchy and visible series counts | Groups series into thematic discovery paths. Counts are dynamic. |
| Popular-series variant | tag/list entry, `/tags/series?ob=pv` | popularity label, title, unit, frequency, seasonal adjustment, period; one title may have several variants | Each variant links to its own series ID and should be treated as a separate series choice. |
| Graph | `/series/<id>` graph controls or `/graph/` links | date range, unit transformation, frequency, optional comparison/transformation, series visibility, download formats | Visualizes one or more series; graph state is not the same as raw observations. |

## Series page field semantics

- `Series ID` is the durable lookup key; do not identify a series by title alone.
- `Units`, `Frequency`, and seasonal adjustment determine how values should be interpreted and compared.
- `Updated` / `Last Updated` and the data date range are freshness signals, not static metadata.
- `Source` and `Release` are first-party attribution and context links; follow them when the user needs provenance.
- `Notes` can contain account codes, definitions, caveats, and source-specific formulas. Prefer these notes over inferred economic definitions.
- `Observations` exposes a short recent sample and `View All` links to the table representation.
- `Download` exposes CSV data, Excel data, image graph, and PowerPoint graph in the observed series-page variant. Re-check the current menu before relying on a format.

## Retrieval rules

1. Resolve the exact series ID from the search result or visible series page.
2. Record the current metadata before reading values.
3. Use the table page for machine-readable `DATE`/`VALUE` rows and the graph page for visual transformations.
4. Preserve the user's requested date range, units, frequency and seasonal-adjustment variant.
5. Treat current values, result counts, periods and download query parameters as dynamic; never write them into reusable instructions.
