# Google Finance page map

## Verified routes and page types

| Page type | Entry / route pattern | Confirmed structure | Status |
| --- | --- | --- | --- |
| Homepage | `/finance/beta` | `首頁`、`研究`、watchlist sidebar、market category buttons、market cards、summary/news、earnings preview、rankings、search | UI-verified |
| Research | Homepage `研究` tab | Research input, popular questions, tool entry points, watchlist insight entry | UI-verified; submission not tested |
| Search overlay | Homepage `搜尋股票、ETF 等` | `詢問相關問題或搜尋` combobox, asset filters, suggestions, voice search, AI ask button | UI-verified; only read-only autocomplete tested |
| Equity / ETF quote | `/finance/beta/quote/{symbol}:{exchange}` | Identity, quote block, chart, time windows, overview/analysis/earnings/financials/holdings when available | UI-verified with representative stock |
| Index quote | `/finance/beta/quote/{symbol}:{index-exchange}` | Identity, intraday status, chart, time windows, overview and related assets | UI-verified with representative index |
| Earnings calendar | `/finance/beta/earnings` | Date tabs, scope filter, company cards, calendar links | UI-verified |

## Navigation map

- Homepage → search overlay → autocomplete option → quote page.
- Homepage → `更多即將發布的財報` → earnings calendar → company earnings quote.
- Homepage market card → index quote page.
- Quote page → chart time window and quote section tabs.
- Quote page → related asset link → another quote page.
- Quote page → `研究` → research panel; prompt submission is a confirmation boundary.

## Route evidence

These patterns were observed through the current tab's DOM and navigation, not from a Sitemap. Query parameters such as `window=1Y` and `tab=earnings` / `tab=holdings` were observed on a representative quote flow; future agents must verify the current URL instead of constructing query strings blindly.
