---
name: tw-stock-data
description: Fetch, validate, and analyze Taiwan stock, OTC, futures, options, and MOPS financial datasets using the tw-stock CLI. Use whenever the user asks for TWSE, TPEX, TAIFEX, MOPS, 台股, 上市櫃, 期貨, 選擇權, 法人買賣超, 融資融券, 外資持股, 股價, 月營收, 財報, or Taiwan market data, even if they do not mention the CLI.
compatibility: Requires Python 3.10+, uv, network access, and the tw-stock CLI from the tw-stock-cli project.
metadata:
  version: "0.1.0"
---

# Taiwan Stock Data

Use this skill to help users discover, fetch, validate, and analyze Taiwan market datasets exposed by the `tw-stock` CLI.

The CLI is the source of truth. Prefer calling `tw-stock` or `uv run tw-stock` instead of reimplementing crawler logic in the agent.

## Dependency

This skill does not bundle the market data crawler itself. It expects the `tw-stock` CLI from the `tw-stock-cli` project to be available.

Use commands in this order:

1. If `tw-stock` is installed in the current environment, call `tw-stock ...`.
2. If working inside a checkout of the `tw-stock-cli` project, call `uv run tw-stock ...` from that repository root.
3. If neither command is available, tell the user that the skill can identify the right dataset and command, but fetching requires installing or opening the `tw-stock-cli` project.

## First steps

1. If the user is asking what data exists, run:

   ```bash
   tw-stock list-datasets --json
   ```

2. If the user mentions a specific topic but not a dataset ID, inspect [the dataset catalog](references/datasets.md) and map their request to the closest dataset.

3. Before fetching a large dataset, describe it or sample it:

   ```bash
   tw-stock describe taifex.futures-tick --json
   tw-stock fetch taifex.futures-tick --date 2026-04-30 --limit 5 --format json
   ```

4. For analysis workflows, prefer `jsonl` for AI/tool pipelines and `csv` for user-facing files:

   ```bash
   tw-stock fetch twse.stock-price --date 2026-04-30 --format jsonl
   tw-stock fetch twse.stock-price --date 2026-04-30 --format csv --output data.csv
   ```

## Dataset selection

Use these common mappings:

- Stock price / open-high-low-close: `twse.stock-price`, `tpex.stock-price`
- Stock list / security codes: `twse.stock-list`, `tpex.stock-list`
- PER / dividend yield / PBR: `twse.stock-per`, `tpex.stock-per`
- Institutional investor buy/sell: `twse.institutional-trade`, `tpex.institutional-trade`
- Margin purchase / short sale: `twse.margin-trade`, `tpex.margin-trade`
- Foreign holdings: `twse.foreign-holding`, `tpex.foreign-holding`
- Total return indices: `twse.total-return-index`, `tpex.total-return-index`
- Futures and options market data: `taifex.*`
- Monthly revenue and financial statements: `mops.*`

For the complete list, read [references/datasets.md](references/datasets.md).

## Safety and data quality

Taiwan exchange endpoints can change format. If the user needs reliable output, validate first:

```bash
tw-stock validate twse.stock-price --date 2026-04-30 --json
```

If validation fails, report the dataset ID, date/parameters, error code, and source URL. Do not silently substitute another data source unless the user asks for that.

For non-trading days, expect empty data or exchange messages. Ask for a nearby trading day only if the user's date is ambiguous.

## Large datasets

Tick data can return hundreds of thousands of rows. Always use `--limit` when exploring:

```bash
tw-stock fetch taifex.options-tick --date 2026-04-30 --limit 20 --format jsonl
```

Only fetch full tick datasets when the user clearly needs full raw data or provides an output path.

## Reference files

- [references/datasets.md](references/datasets.md): dataset IDs, parameters, and examples.
- [references/cli-usage.md](references/cli-usage.md): command patterns and output formats.
- [references/data-caveats.md](references/data-caveats.md): known source quirks and edge cases.
