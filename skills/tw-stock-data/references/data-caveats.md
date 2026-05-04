# Data Caveats

## Trading days

Most date-based datasets only return data for valid trading days. If a user provides a weekend or market holiday, validation may fail or return zero rows. Ask for a nearby trading day when the intent is ambiguous.

## Large tick data

`taifex.futures-tick` and `taifex.options-tick` can return hundreds of thousands of rows. Use `--limit` for exploration and only fetch the full dataset when the user asks for full raw data or provides an output path.

## MOPS financial statements

MOPS financial statement datasets return multiple tables because the source groups companies by industry/report format. Use `json` or `jsonl`. CSV and parquet are intentionally not supported for multi-table outputs.

## TAIFEX FCM volume CSV files

The day-session futures/options FCM volume files are monthly wide CSV files. Repeated product columns become pandas columns such as `MTX`, `MTX.1`, `MTX.2`. Do not assume each row represents a single date unless the data has been normalized by a downstream process.

## Exchange source changes

TWSE and TPEx have changed response shapes over time, including moving from `data9`/`aaData` to `tables[].data`. Run `validate` before building a report that users rely on.

## Numeric values

Many fields are returned as strings and may include commas, percentages, dashes, or blank values. Convert numbers explicitly in analysis code and preserve original strings when producing raw exports.

