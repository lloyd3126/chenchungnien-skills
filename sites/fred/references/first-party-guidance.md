# FRED first-party guidance and provenance

## Visible help routes

The footer links to `https://fredhelp.stlouisfed.org/`. Its visible topic navigation includes:

- Data: `How can I find data on FRED?`, `How can I download data from FRED?`, `What can I do with FRED Data Lists?`, `Understanding the Data`.
- Graphs: `How can I customize a FRED graph?`, `How can I share my FRED graph?`.
- Maps, Account, FAQ, and About.

In this exploration, the detailed accordion panels stayed on a spinner after a safe click. Do not treat the topic label as proof of the panel's detailed contents; re-open and verify loaded text when a task depends on it.

## FRED API documentation

The visible FRED API documentation index is `https://fred.stlouisfed.org/docs/api/fred/`.

- API Version 2 is described as suitable for bulk retrieval of all series observations in a release and full history.
- API Version 1 is described as incremental, series-level retrieval with customization by source, release, category, series and other preferences.
- The index exposes general documentation for FRED/ALFRED, real-time periods, API keys and errors, plus endpoint groups for categories, releases, series, sources, tags and GeoFRED maps.

The browser-first FRED skills do not enter API keys or call the API during ordinary site exploration. Use the documentation only when a user explicitly asks for programmatic retrieval or vintage/revision behavior, and keep credentials out of the browser and repository.

## Citation and provenance

Series pages visibly expose `Source`, `Release`, `Units`, `Frequency`, `Notes`, and a `Suggested Citation`. When reporting a value or interpretation:

1. cite the exact series ID and current FRED series page;
2. include source, release, units and frequency when relevant;
3. record the retrieval date/time for dynamic observations;
4. preserve the series' own notes and attribution rather than replacing them with general economic knowledge.

The chart also links to a FRED Help explanation for shaded U.S. recession areas. Treat graph annotations and transformations as presentation context, not as additional raw observations.
