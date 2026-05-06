# Dataset Catalog

Use `tw-stock list-datasets --json` for the authoritative machine-readable catalog. If the CLI is not installed globally and you are inside the `tw-stock-cli` project, use `uv run tw-stock list-datasets --json`. From another directory, use `uv run --project /path/to/tw-stock-cli tw-stock list-datasets --json`.

Current catalog size: 72 datasets: 7 TWSE, 7 TPEx, 9 TAIFEX, and 49 MOPS.

The CLI now normalizes common output columns to English `snake_case`. Prefer `tw-stock describe <dataset> --json` or `tw-stock fetch <dataset> --schema-only --format json` before writing analysis code that depends on exact columns.

## Common Parameters

- `--date`: trading date in `YYYY-MM-DD`.
- `--year`: ROC year or AD year for MOPS datasets.
- `--month`: month number for MOPS monthly revenue.
- `--quarter`: quarter number, `1` through `4`, for MOPS financial statements.
- `--market`: MOPS market, default usually `sii`; common values are `sii`, `otc`, `rotc`, `pub`, and `all` for some single-company queries.
- `--foreign`: MOPS monthly revenue foreign-company flag, default `0`.

## Column Naming

- Common security identifiers use `stock_id` and `stock_name`.
- Price data uses `open`, `high`, `low`, `close`; do not use the old `max` and `min` column names.
- Valuation data uses lowercase `per` and `pbr`; do not use the old `PER` and `PBR` column names.
- Institutional trading fields use suffixes such as `_buy`, `_sell`, and `_net_buy`.
- Margin trading fields use prefixes such as `margin_purchase_` and `short_sale_`.
- TAIFEX FCM volume files use `fcm_id`, `fcm_name`, `subtotal`, `total`, `market_share`, product columns such as `mtx`, and total product columns such as `total_mtx`.
- MOPS financial statement line items remain in Chinese, but shared identifier columns are normalized to `stock_id` and `stock_name`.

## TWSE

| Dataset ID | Required params | Key columns | Example |
|---|---|---|---|
| `twse.stock-price` | `--date` | `stock_id`, `stock_name`, `open`, `high`, `low`, `close`, `date` | `tw-stock fetch twse.stock-price --date 2026-04-30 --limit 5 --format table` |
| `twse.stock-list` | `--date` | `stock_id`, `stock_name`, `date` | `tw-stock fetch twse.stock-list --date 2026-04-30 --format jsonl` |
| `twse.stock-per` | `--date` | `stock_id`, `stock_name`, `close`, `dividend_yield`, `dividend_year`, `per`, `pbr`, `financial_report_period`, `date` | `tw-stock fetch twse.stock-per --date 2026-04-30 --limit 5 --format table` |
| `twse.institutional-trade` | `--date` | `stock_id`, `stock_name`, `foreign_ex_dealer_net_buy`, `investment_trust_net_buy`, `dealer_net_buy`, `institutional_net_buy` | `tw-stock fetch twse.institutional-trade --date 2026-04-30 --limit 5 --format json` |
| `twse.margin-trade` | `--date` | `stock_id`, `stock_name`, `margin_purchase_balance`, `short_sale_balance`, `offsetting_trade`, `note` | `tw-stock fetch twse.margin-trade --date 2026-04-30 --limit 5 --format table` |
| `twse.foreign-holding` | `--date` | `stock_id`, `stock_name`, `issued_shares`, `foreign_held_shares`, `foreign_held_ratio` | `tw-stock fetch twse.foreign-holding --date 2026-04-30 --limit 5 --format jsonl` |
| `twse.total-return-index` | `--date` | `date`, `total_return_index` | `tw-stock fetch twse.total-return-index --date 2026-04-30 --format table` |

## TPEx

| Dataset ID | Required params | Key columns | Example |
|---|---|---|---|
| `tpex.stock-price` | `--date` | `stock_id`, `stock_name`, `close`, `open`, `high`, `low`, `date` | `tw-stock fetch tpex.stock-price --date 2026-04-30 --limit 5 --format table` |
| `tpex.stock-list` | `--date` | `stock_id`, `stock_name`, `industry_category`, `date` | `tw-stock fetch tpex.stock-list --date 2026-04-30 --limit 10 --format table` |
| `tpex.stock-per` | `--date` | `stock_id`, `stock_name`, `per`, `dividend_per_share`, `dividend_year`, `dividend_yield`, `pbr`, `date` | `tw-stock fetch tpex.stock-per --date 2026-04-30 --limit 5 --format json` |
| `tpex.institutional-trade` | `--date` | `stock_id`, `stock_name`, `foreign_total_net_buy`, `investment_trust_net_buy`, `dealer_total_net_buy`, `institutional_net_buy` | `tw-stock fetch tpex.institutional-trade --date 2026-04-30 --limit 5 --format table` |
| `tpex.margin-trade` | `--date` | `stock_id`, `stock_name`, `margin_purchase_balance`, `margin_purchase_usage_ratio`, `short_sale_balance`, `short_sale_usage_ratio` | `tw-stock fetch tpex.margin-trade --date 2026-04-30 --limit 5 --format jsonl` |
| `tpex.foreign-holding` | `--date` | `rank`, `stock_id`, `stock_name`, `foreign_held_shares`, `foreign_held_ratio` | `tw-stock fetch tpex.foreign-holding --date 2026-04-30 --limit 5 --format table` |
| `tpex.total-return-index` | `--date` | `date`, `index`, `total_return_index` | `tw-stock fetch tpex.total-return-index --date 2026-04-30 --format table` |

## TAIFEX

| Dataset ID | Required params | Key columns | Example |
|---|---|---|---|
| `taifex.futures-daily` | `--date` | `trade_date`, `contract`, `expiry_month_week`, `open`, `high`, `low`, `close`, `volume` | `tw-stock fetch taifex.futures-daily --date 2026-04-30 --limit 10 --format table` |
| `taifex.options-daily` | `--date` | `trade_date`, `contract`, `expiry_month_week`, `strike_price`, `call_put`, `close`, `volume` | `tw-stock fetch taifex.options-daily --date 2026-04-30 --limit 10 --format jsonl` |
| `taifex.futures-tick` | `--date` | `trade_date`, `contract`, `expiry_month_week`, `trade_time`, `trade_price`, `trade_volume` | `tw-stock fetch taifex.futures-tick --date 2026-04-30 --limit 20 --format jsonl` |
| `taifex.options-tick` | `--date` | `trade_date`, `contract`, `strike_price`, `expiry_month_week`, `call_put`, `trade_time`, `trade_price` | `tw-stock fetch taifex.options-tick --date 2026-04-30 --limit 20 --format jsonl` |
| `taifex.futures-institutional` | `--date` | `row_number`, `contract_name`, `investor_type`, `trade_long_volume`, `open_interest_long_volume` | `tw-stock fetch taifex.futures-institutional --date 2026-04-30 --format table` |
| `taifex.fcm-futures-volume-day` | none | `fcm_id`, `fcm_name`, `subtotal` | `tw-stock fetch taifex.fcm-futures-volume-day --limit 10 --format table` |
| `taifex.fcm-futures-volume-night` | none | `fcm_id`, `fcm_name`, `total`, `market_share` | `tw-stock fetch taifex.fcm-futures-volume-night --limit 10 --format json` |
| `taifex.fcm-options-volume-day` | none | `fcm_id`, `fcm_name`, `total`, `market_share` | `tw-stock fetch taifex.fcm-options-volume-day --limit 10 --format table` |
| `taifex.fcm-options-volume-night` | none | `fcm_id`, `fcm_name`, `total`, `market_share` | `tw-stock fetch taifex.fcm-options-volume-night --limit 10 --format jsonl` |

## MOPS

MOPS now includes broad-market statement tables, single-company statements, revenue, dividends, corporate actions, governance, insiders, related-party transactions, ESG metadata, and PDF/electronic-book download indexes.

| Dataset ID | Title | Required params | Optional params | Key columns |
|---|---|---|---|---|
| `mops.annual-report-electronic-book` | 年報與股東會電子書 metadata | `--stock-id, --year` | `--market` | `stock_id`, `document_year`, `document_type`, `detail_type`, `meeting_type`, ... |
| `mops.asset-acquisition-disposal` | 月取得或處分資產資訊 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `market`, `report_year`, `report_month`, ... |
| `mops.asset-acquisition-disposal-financial` | 取得或處分資產財務資料表 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `report_year`, `report_month`, `financial_assets_total`, ... |
| `mops.balance-sheet` | 資產負債表 | `--year, --quarter` | `--market` | multiple tables; common columns include `stock_id`, `stock_name` |
| `mops.board-attendance-training` | 董事會出席與進修情形 | `--stock-id` | `--market` | `stock_id`, `stock_name`, `market`, `section`, `role`, ... |
| `mops.cash-flow` | 現金流量表 | `--year, --quarter` | `--market` | multiple tables; common columns include `stock_id`, `stock_name` |
| `mops.company-balance-sheet` | 個別公司資產負債表 | `--stock-id, --year, --quarter` | `--market` | `stock_id`, `stock_name`, `report_year`, `quarter`, `statement`, ... |
| `mops.company-basic-info` | 公司基本資料 | none | `--market, --stock-id, --industry-code` | `stock_id`, `stock_name`, `short_name`, `industry`, `chairman`, ... |
| `mops.company-cash-flow` | 個別公司現金流量表 | `--stock-id, --year, --quarter` | `--market` | `stock_id`, `stock_name`, `report_year`, `quarter`, `statement`, ... |
| `mops.company-equity-changes` | 個別公司權益變動表 | `--stock-id, --year, --quarter` | `--market` | `stock_id`, `stock_name`, `report_year`, `quarter`, `statement_year`, ... |
| `mops.company-governance-structure` | 公司治理組織架構 | none | `--market, --stock-id` | `market`, `stock_id`, `stock_name`, `articles_board_seats`, `articles_independent_director_seats`, ... |
| `mops.company-income-statement` | 個別公司綜合損益表 | `--stock-id, --year, --quarter` | `--market` | `stock_id`, `stock_name`, `report_year`, `quarter`, `statement`, ... |
| `mops.director-supervisor-remuneration` | 董監事酬金相關資訊 | `--year` | `--market` | `market`, `report_year`, `report_type`, `role`, `industry`, ... |
| `mops.dividend-distribution` | 公司股利分派情形 | `--stock-id, --year` | `--market` | `stock_id`, `stock_name`, `dividend_year`, `cash_dividend_per_share`, `capital_surplus_cash_per_share`, ... |
| `mops.employee-benefit-expense` | 員工福利及薪資費用統計 | `--year` | `--market, --industry-code` | `market`, `report_year`, `industry`, `stock_id`, `stock_name`, ... |
| `mops.employee-welfare-policy` | 員工福利政策及權益維護措施 | `--stock-id, --year` | `--market` | `stock_id`, `stock_name`, `report_year`, `disclosure_year`, `section`, ... |
| `mops.endorsement-guarantee` | 背書保證明細 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `report_year`, `report_month`, `guarantor_name`, ... |
| `mops.esg-company-disclosure` | 企業 ESG 資訊揭露個別公司查詢 metadata | `--stock-id, --year` | `--market` | `stock_id`, `mops_year`, `report_year`, `inquiry_url` |
| `mops.ex-dividend-announcement` | 除權息公告 | `--year` | `--market, --stock-id, --month, --start-day, --end-day` | `stock_id`, `stock_name`, `dividend_period`, `record_date`, `cash_dividend_from_earnings_per_share`, ... |
| `mops.financial-report-electronic-book` | 財務報告電子書 metadata | `--stock-id, --year` | `--market` | `stock_id`, `document_year`, `document_type`, `detail_type`, `detail_description`, ... |
| `mops.full-time-employee-salary` | 非擔任主管職務全時員工薪資統計 | `--year` | `--market, --industry-code` | `market`, `report_year`, `industry`, `stock_id`, `stock_name`, ... |
| `mops.functional-committee` | 功能性委員會設置及成員 | none | `--market, --committee` | `market`, `committee_code`, `committee_name`, `stock_id`, `stock_name`, ... |
| `mops.fund-lending` | 資金貸與明細 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `report_year`, `report_month`, `lender_name`, ... |
| `mops.income-statement` | 綜合損益表 | `--year, --quarter` | `--market` | multiple tables; common columns include `stock_id`, `stock_name` |
| `mops.independent-director-profile` | 獨立董事基本資料 | none | `--market` | `market`, `sequence_no`, `stock_id`, `stock_name`, `role`, ... |
| `mops.insider-holding-company-list` | 內部人持股餘額公司清單 | `--year, --month` | `--market, --industry-code` | `stock_id`, `stock_name`, `report_ym`, `market`, `detail_available` |
| `mops.insider-holding-detail` | 董監事持股餘額明細資料 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `report_ym`, `role`, `person_name`, ... |
| `mops.insider-pledge-ratio-summary` | 董監事質權設定持股占比彙總表 | `--year, --month` | `--market` | `stock_id`, `stock_name`, `report_ym`, `pledge_ratio_bucket`, `pledge_ratio` |
| `mops.insider-pledge-summary` | 內部人質權設定彙總表 | `--year, --month` | `--market` | `stock_id`, `stock_name`, `report_ym`, `directors_supervisors_held_shares`, `directors_supervisors_pledged_shares`, ... |
| `mops.insider-shareholding-change` | 內部人股權異動彙總表 | `--year, --month` | `--market` | `stock_id`, `stock_name`, `report_ym`, `issued_shares`, `directors_supervisors_increase_shares`, ... |
| `mops.insider-shareholding-detail` | 內部人持股異動事後申報表 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `report_ym`, `role`, `person_name`, ... |
| `mops.insider-transfer-declaration-detail` | 內部人持股轉讓事前申報表-個別公司 | `--stock-id, --year` | `--market, --month, --start-month, --end-month` | `stock_id`, `stock_name`, `declaration_date`, `declarer_role`, `declarer_name`, ... |
| `mops.insider-transfer-declaration-summary` | 內部人持股轉讓事前申報彙總表 | `--year` | `--market, --month, --start-month, --end-month` | `stock_id`, `stock_name`, `declaration_date`, `declarer_role`, `declarer_name`, ... |
| `mops.insider-transfer-untransferred-detail` | 內部人持股未轉讓申報表-個別公司 | `--stock-id, --year` | `--market, --month, --start-month, --end-month` | `stock_id`, `stock_name`, `declaration_date`, `declarer_role`, `declarer_name`, ... |
| `mops.insider-transfer-untransferred-summary` | 內部人持股未轉讓申報彙總表 | `--year` | `--market, --month, --start-month, --end-month` | `stock_id`, `stock_name`, `declaration_date`, `declarer_role`, `declarer_name`, ... |
| `mops.investor-conference` | 法人說明會一覽表 | `--year` | `--market, --stock-id, --month` | `stock_id`, `stock_name`, `conference_date`, `conference_time`, `location`, ... |
| `mops.major-shareholder-relationship` | 年報前十大股東相互間關係 metadata | `--year` | `--market, --stock-id` | `market`, `report_year`, `stock_id`, `stock_name`, `shareholder_meeting_date`, ... |
| `mops.manager-compensation-distribution` | 經理人員工酬勞分派情形 | `--stock-id, --year` | `--market` | `stock_id`, `stock_name`, `compensation_year`, `distribution_year`, `stock_compensation_shares`, ... |
| `mops.material-info` | 重大訊息 | `--year` | `--market, --stock-id, --month, --start-day, --end-day` | `stock_id`, `stock_name`, `announcement_date`, `announcement_time`, `subject`, ... |
| `mops.material-info-detail` | 重大訊息詳細資料 | `--stock-id, --seq-no, --spoke-date, --spoke-time` | `--market` | `stock_id`, `stock_name`, `seq_no`, `announcement_date`, `announcement_time`, ... |
| `mops.month-revenue` | 月營收 | `--year, --month` | `--market, --foreign` | `stock_id`, `revenue`, `revenue_year`, `revenue_month` |
| `mops.private-placement` | 私募有價證券資料 | none | `--market, --stock-id` | `stock_id`, `stock_name`, `market`, `security_type`, `decision_date`, ... |
| `mops.related-company-reports` | 關係企業三書表電子書 metadata | `--stock-id, --year` | `--market` | `stock_id`, `document_year`, `document_type`, `detail_type`, `detail_description`, ... |
| `mops.related-party-transaction` | 關係人交易申報明細 | `--stock-id, --year, --month` | `--market` | `stock_id`, `stock_name`, `report_year`, `report_month`, `transaction_type`, ... |
| `mops.related-party-transaction-difference` | 關係人交易查核核閱差異說明 | `--stock-id, --year, --quarter` | `--market` | `stock_id`, `stock_name`, `report_year`, `quarter`, `transaction_type`, ... |
| `mops.shareholder-meeting` | 股東會日期地點及電子投票 | `--year` | `--market, --stock-id, --month, --start-day, --end-day` | `stock_id`, `stock_name`, `meeting_type`, `meeting_date`, `book_closure_start`, ... |
| `mops.shareholding-distribution` | 股權分散表 | `--stock-id, --year` | `--market` | `stock_id`, `stock_name`, `query_year`, `data_date`, `section`, ... |
| `mops.sustainability-report` | 永續報告書 metadata | `--year` | `--market, --stock-id` | `market`, `report_year`, `stock_id`, `stock_name`, `industry`, ... |
| `mops.treasury-stock-buyback` | 庫藏股買回基本資料 | `--stock-id` | `--market` | `stock_id`, `stock_name`, `buyback_no`, `report_date`, `board_resolution_date`, ... |

Common MOPS examples:

```bash
tw-stock fetch mops.company-cash-flow --stock-id 2395 --year 2025 --quarter 4 --market sii --format json
tw-stock fetch mops.employee-welfare-policy --stock-id 2395 --year 2025 --market all --format json
tw-stock fetch mops.esg-company-disclosure --stock-id 2395 --year 2024 --market sii --format json
tw-stock fetch mops.investor-conference --stock-id 2395 --year 2025 --market sii --limit 5 --format json
```

`--market` values:

- `sii`: listed companies
- `otc`: OTC companies
- `rotc`: emerging stock companies
- `pub`: public companies
- `all`: all markets, supported by some single-company MOPS endpoints
