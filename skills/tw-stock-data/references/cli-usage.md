# CLI Usage

Prefer `tw-stock` when the CLI is installed in the current environment. Use `uv run tw-stock` when working inside a checkout of the `tw-stock-cli` project and the CLI is not installed globally.

If neither command is available, identify the correct dataset and parameters for the user, then explain that fetching requires the `tw-stock-cli` project or an installed `tw-stock` command.

## Discovery

```bash
tw-stock list-datasets
tw-stock list-datasets --group twse --json
tw-stock describe twse.stock-price --json
```

## Fetching

```bash
tw-stock fetch twse.stock-price --date 2026-04-30 --format table
tw-stock fetch twse.stock-price --date 2026-04-30 --format jsonl
tw-stock fetch twse.stock-price --date 2026-04-30 --columns stock_id,stock_name,close --format csv
tw-stock fetch twse.stock-price --date 2026-04-30 --limit 10 --format json
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
tw-stock fetch mops.income-statement --year 114 --quarter 4 --market sii --format json
```

MOPS financial statements return multiple tables. Prefer `json` or `jsonl`.

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
