# Dataset Catalog

Use `tw-stock list-datasets --json` for the authoritative machine-readable catalog. If the CLI is not installed globally and you are inside the `tw-stock-cli` project, use `uv run tw-stock list-datasets --json`.

## TWSE

| Dataset ID | Required params | Description |
|---|---|---|
| `twse.stock-price` | `--date` | Listed securities daily open, high, low, close. |
| `twse.stock-list` | `--date` | Listed security codes and names. |
| `twse.stock-per` | `--date` | PER, dividend yield, and price-to-book ratio. |
| `twse.institutional-trade` | `--date` | Daily institutional investor buy/sell details. |
| `twse.margin-trade` | `--date` | Margin purchase and short sale balances. |
| `twse.foreign-holding` | `--date` | Foreign and mainland China investor holding statistics. |
| `twse.total-return-index` | `--date` | TWSE total return index for the month containing the date. |

## TPEX

| Dataset ID | Required params | Description |
|---|---|---|
| `tpex.stock-price` | `--date` | OTC securities daily open, high, low, close. |
| `tpex.stock-list` | `--date` | OTC security list and daily quote columns by category. |
| `tpex.stock-per` | `--date` | PER, dividend yield, and price-to-book ratio. |
| `tpex.institutional-trade` | `--date` | Daily institutional investor buy/sell details. |
| `tpex.margin-trade` | `--date` | Margin purchase and short sale balances. |
| `tpex.foreign-holding` | `--date` | Foreign holding ratio ranking. |
| `tpex.total-return-index` | `--date` | TPEx index and total return index for the month containing the date. |

## TAIFEX

| Dataset ID | Required params | Description |
|---|---|---|
| `taifex.futures-daily` | `--date` | Daily futures market data. |
| `taifex.options-daily` | `--date` | Daily options market data. |
| `taifex.futures-tick` | `--date` | Futures tick data. Large dataset. |
| `taifex.options-tick` | `--date` | Options tick data. Large dataset. |
| `taifex.futures-institutional` | `--date` | Futures institutional positions and open interest. |
| `taifex.fcm-futures-volume-day` | none | Futures commission merchant futures volume, day session. |
| `taifex.fcm-futures-volume-night` | none | Futures commission merchant futures volume, night session. |
| `taifex.fcm-options-volume-day` | none | Futures commission merchant options volume, day session. |
| `taifex.fcm-options-volume-night` | none | Futures commission merchant options volume, night session. |

## MOPS

| Dataset ID | Required params | Optional params | Description |
|---|---|---|---|
| `mops.month-revenue` | `--year`, `--month` | `--market`, `--foreign` | Monthly revenue. `--year` accepts ROC year or AD year. |
| `mops.income-statement` | `--year`, `--quarter` | `--market` | Quarterly income statement summary tables. |
| `mops.balance-sheet` | `--year`, `--quarter` | `--market` | Quarterly balance sheet summary tables. |
| `mops.cash-flow` | `--year`, `--quarter` | `--market` | Quarterly cash flow summary tables. |

`--market` values:

- `sii`: listed companies
- `otc`: OTC companies
- `rotc`: emerging stock companies
- `pub`: public companies
