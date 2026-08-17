# Koyfin advanced search controls

## Security Search

Entry: `Research Tools` → `Advanced Search` → `Security Search` (`/search/security`).

Observed controls:

- `Search terms` textbox with placeholder `Type terms you want to search`.
- `Asset Category` dropdown defaulting to `Search Everything`.
- `Reset` and `Search Securities` buttons.
- Available Filters: Country, Sector, Trading Currency and Trading Exchanges.
- Results table: Ticker, Country, Security Name and Asset Category, with pagination when applicable.

Safe test: search a representative ticker, verify multiple listings by visible Country/Security Name/Asset Category, then use `Reset`. Do not copy the returned rows into durable files.

## Transcripts Search

Entry: `Research Tools` → `Advanced Search` → `Transcripts Search` (`/search/transcripts`).

Observed controls:

- Search terms textbox and `Advanced Terms`.
- Date Range with a current start/end date.
- `Reset` and `Search Transcripts`.
- Event Types including Analyst/Investor Day, Company Conference Presentations and Earnings Calls, with `Show more`.
- Companies field `Add companies to filter`, Security Lists and Sectors.

Safe test: apply one event type, wait for the loading state to finish, verify filtered event rows, then use the visible `Clear` action or `Reset`. Record the date range and event type with any answer.

## Disambiguation and error handling

- A ticker search may return common-stock listings, ETFs or other asset classes. Use the requested country/exchange/asset class; if it remains ambiguous, ask rather than guessing.
- A no-result or reduced result set may come from the active date range, filter, account scope, query syntax or transient loading. Verify the visible form state before concluding.
- Search URL changes and API/control success are not enough; use the current tab's heading, selected tab and result content as evidence.
