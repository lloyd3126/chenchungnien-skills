# 全站與進階搜尋控制項

## 全站搜尋 `/Search`

The visible page exposes:

| Control | Purpose | Safe verification |
| --- | --- | --- |
| `關鍵字` | Free-text site keyword | Retained input and heading |
| `送出搜尋` | Starts the search | URL/hash, result count, pagination or visible result cards |
| `進階搜尋` | Opens `/AdvancedSearch` and can retain the prior query | New heading and fields |

The observed search submission for a representative keyword moved the page to a `#gsc.tab=0` state. After the embedded search settled, the page exposed a result count, page links, and a link to search Google. The embedded result area may emit CSP `EvalError` messages in the current browser; treat that as an incomplete rendering signal and do not mistake it for a search result.

## Advanced search `/AdvancedSearch`

The form shows three required textboxes:

1. `與以下字詞或語句完全相符： (必填)` — exact phrase; helper text explains surrounding a phrase with quotes.
2. `含以下任何字詞： (必填)` — words that may appear; helper text explains exclusion examples.
3. `在各搜尋字詞之間輸入 OR(大寫)： (必填)` — uppercase `OR` expression; helper text explains minus/exclusion syntax.

`搜尋` applies the form and `一般搜尋` returns to the ordinary search. Verify that the form values, current query state, result count and pagination agree; the observed page retained a previous `q` value and showed embedded-search CSP messages, so do not assume every field changed the result merely because the button was clicked.

## Safe interaction protocol

1. Start from the current visible page and identify duplicate search controls by their accessible label.
2. Enter a non-sensitive representative keyword supplied by the user or a neutral test term.
3. Submit once and wait for the page or embedded results to settle.
4. Confirm at least two signals: heading, retained input, URL/hash, result count, pagination or visible result cards.
5. If the result area is blank or shows a browser/client error, report the rendering limitation and keep the query visible; do not broaden the search or follow the external Google link automatically.
