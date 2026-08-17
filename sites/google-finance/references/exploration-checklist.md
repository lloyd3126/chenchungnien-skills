# Google Finance exploration checklist

## Sitemap inventory

| Target | Result | Evidence | Notes |
| --- | --- | --- | --- |
| Visible site map / first-party inventory | Not found in visible homepage UI | current-tab visual + DOM | No sitemap link observed |
| `/robots.txt` | `client-blocked` after same-tab retry | automation/control error + current-tab visual | Tab remained on Finance homepage; no directives parsed |
| `/sitemap.xml` | `client-blocked` after same-tab retry | automation/control error + current-tab visual | No download or local artifact |

## Coverage

| Area | Status | Verification |
| --- | --- | --- |
| Homepage and market categories | explored | Homepage screenshot and DOM; crypto, currency and futures cards visibly changed |
| Search and autocomplete | explored | `TSM` input produced exchange-specific options; one option opened a quote |
| Stock / ETF quote | explored | Representative stock quote page, chart controls and quote tabs |
| Index quote | explored | Representative Nikkei index quote page and related assets |
| Research tab | partial / unsafe | UI and entry points inspected; no prompt or work submitted |
| Earnings calendar | explored | Date tabs, loading state, all-stock and watchlist filters, event cards |
| Earnings / financials / holdings | explored | Quote `收益`, `財務`, `持有資產`; insider and political-person views |
| Settings | partial / unsafe | Theme and up/down color menu labels inspected; no settings changed |
| Watchlist / portfolio mutations | unsafe | Existing list visible; add/create actions not executed |

## Authenticated variant

The visible page showed an authenticated Google account variant. The sidebar watchlist, `在你的清單中` earnings filter, and personalized research entry were visible and read-only inspected. A logged-out variant was not created or tested.

## Second-pass result

Homepage, quote page, earnings calendar, research tab, sidebar, footer links, settings menu, major dropdowns and primary read-only tabs were revisited or inspected. Remaining gaps are explicitly labeled as unsafe, client-blocked, or authenticated-variant dependent above.
