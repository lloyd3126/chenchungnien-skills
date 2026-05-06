# CLI Usage

Prefer `tw-stock` when the CLI is installed in the current environment. Use `uv run tw-stock` when working inside a checkout of the `tw-stock-cli` project and the CLI is not installed globally. From another directory, use `uv run --project /path/to/tw-stock-cli tw-stock`.

If neither command is available, identify the correct dataset and parameters for the user, then explain that fetching requires the `tw-stock-cli` project or an installed `tw-stock` command.

## Discovery

```bash
tw-stock list-datasets
tw-stock list-datasets --group twse --json
tw-stock describe twse.stock-price --json
```

Use `describe` or `--schema-only` whenever exact output columns matter. The CLI normalizes common columns to English `snake_case`, and references should not assume old source-language column names.

## Fetching

```bash
tw-stock fetch twse.stock-price --date 2026-04-30 --format table
tw-stock fetch twse.stock-price --date 2026-04-30 --format jsonl
tw-stock fetch twse.stock-price --date 2026-04-30 --columns stock_id,stock_name,open,high,low,close --format csv
tw-stock fetch twse.stock-price --date 2026-04-30 --limit 10 --format json
```

Inspect metadata without fetching source data:

```bash
tw-stock fetch twse.stock-price --schema-only --format json
tw-stock fetch twse.stock-price --source-url-only --format json
```

Write files with `--output`:

```bash
tw-stock fetch tpex.stock-price --date 2026-04-30 --format csv --output tpex-stock-price.csv
tw-stock fetch twse.stock-price --date 2026-04-30 --format parquet --output twse-stock-price.parquet
```

Parquet output requires a parquet engine such as `pyarrow` in the environment.

## MOPS examples

```bash
tw-stock fetch mops.month-revenue --year 115 --month 3 --market sii --format jsonl
tw-stock fetch mops.month-revenue --year 2026 --month 3 --market sii --format csv --output revenue.csv
tw-stock fetch mops.month-revenue --year 115 --month 3 --market sii --foreign 1 --format json
tw-stock fetch mops.income-statement --year 114 --quarter 4 --market sii --format json
tw-stock fetch mops.company-cash-flow --stock-id 2395 --year 2025 --quarter 4 --market sii --format json
tw-stock fetch mops.employee-welfare-policy --stock-id 2395 --year 2025 --market all --format json
tw-stock fetch mops.esg-company-disclosure --stock-id 2395 --year 2024 --market sii --format json
tw-stock fetch mops.investor-conference --stock-id 2395 --year 2025 --market sii --limit 5 --format json
```

MOPS financial statements return multiple tables. Prefer `json` or `jsonl`.

MOPS PDF/electronic-book datasets return metadata and download URLs by design. Use the URL fields when the user wants to download/read the original filing instead of forcing PDF table extraction.

## Column examples

- Stock price datasets use `stock_id`, `stock_name`, `open`, `high`, `low`, `close`, `date`.
- PER/PBR datasets use lowercase `per` and `pbr`.
- Institutional trading datasets use fields such as `foreign_total_net_buy`, `investment_trust_net_buy`, `dealer_total_net_buy`, and `institutional_net_buy`.
- Margin trading datasets use fields such as `margin_purchase_balance` and `short_sale_balance`.
- TAIFEX FCM volume datasets use fields such as `fcm_id`, `fcm_name`, `subtotal`, `total`, and `market_share`.

## Validation

```bash
tw-stock validate twse.stock-price --date 2026-04-30 --json
tw-stock validate mops.month-revenue --year 115 --month 3 --market sii --json
```

Treat `ok: false` as a source, date, parameter, or parser problem. Report the error instead of continuing silently.

## Output format selection

- `table`: human-readable preview.
- `json`: structured output for small or multi-table datasets.
- `jsonl`: best default for agents and pipelines.
- `csv`: best for spreadsheets and user handoff.
- `parquet`: best for analysis workflows when a parquet engine is installed.
