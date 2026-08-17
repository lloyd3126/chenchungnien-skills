# Facebook Search Controls

## Shared search

- Visible label: `搜尋 Facebook`.
- Safe interaction: fill a non-sensitive keyword and submit; verify the heading and URL query state.
- Observed route shape: `/search/top/?q=<query>` with locale and tracking parameters that should not be copied into durable notes.

## Scope tabs

Observed result scopes are `全部`, `人物`, `Reel`, `Marketplace`, `粉絲專頁`, `社團` and `活動`. Each scope can change the result entity type and route. Re-read the active tab and heading after switching.

## Result filters

On `全部`, the observed controls include switches for `最新貼文` and `你看過的貼文`, plus comboboxes for `依發佈日期篩選`, `貼文來源` and `標註的地點`. The option lists are dynamic and should be read from the current UI before choosing one.

## Evidence pattern

For a search or filter change, capture the query text, active scope, selected filter and one result-page signal. Do not save current result names, counts, timestamps or post text as reference data.
