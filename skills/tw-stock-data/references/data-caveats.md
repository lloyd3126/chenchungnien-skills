# Data Caveats

## Trading days

Most date-based datasets only return data for valid trading days. If a user provides a weekend or market holiday, validation may fail or return zero rows. Ask for a nearby trading day when the intent is ambiguous.

## Large tick data

`taifex.futures-tick` and `taifex.options-tick` can return hundreds of thousands of rows. Use `--limit` for exploration and only fetch the full dataset when the user asks for full raw data or provides an output path.

## MOPS financial statements

MOPS financial statement datasets return multiple tables because the source groups companies by industry/report format. Use `json` or `jsonl`. CSV and parquet are intentionally not supported for multi-table outputs.

For free cash flow calculations, prefer the single-company statement datasets such as `mops.company-cash-flow`, because they preserve more line-item detail than broad-market summary tables.

## MOPS PDF and ESG metadata

Some MOPS datasets intentionally return filing metadata and download or inquiry URLs instead of parsed document contents:

- `mops.financial-report-electronic-book`
- `mops.annual-report-electronic-book`
- `mops.related-company-reports`
- `mops.major-shareholder-relationship`
- `mops.sustainability-report`
- `mops.esg-company-disclosure`

Use these URL fields when the user wants the original PDF, electronic book, sustainability report, or ESGGen+ company page. Do not imply that the CLI has parsed the underlying PDF or front-end rendered ESG indicator tables unless the dataset schema exposes those fields.

## TAIFEX FCM volume CSV files

The FCM volume files are wide CSV files. The CLI normalizes common columns to `fcm_id`, `fcm_name`, `subtotal`, `total`, and `market_share`; product columns are lowercased, such as `mtx`, and product total columns are prefixed, such as `total_mtx`.

Do not assume each row represents a single date unless the source file or downstream process provides an explicit date column.

## Column naming changes

The current CLI normalizes many source-language fields to English `snake_case`. Use `describe` or `--schema-only` before relying on exact names. Common changes include:

- `max` / `min` are now `high` / `low`.
- `PER` / `PBR` are now `per` / `pbr`.
- Chinese security identifier fields are now `stock_id` and `stock_name`.
- MOPS statement line items can remain Chinese, but shared identifiers are still normalized.

## Exchange source changes

TWSE and TPEx have changed response shapes over time, including moving from `data9`/`aaData` to `tables[].data`. Run `validate` before building a report that users rely on.

## Numeric values

Many fields are returned as strings and may include commas, percentages, dashes, or blank values. Convert numbers explicitly in analysis code and preserve original strings when producing raw exports.
