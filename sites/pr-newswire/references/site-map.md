# PR Newswire route map

## Evidence legend

- `current-tab visual`: the user's existing Codex in-app browser tab visibly rendered the page.
- `current-tab DOM/interaction`: the same tab exposed the page labels, controls, or transition through the visible UI/DOM.
- `automation/control error`: a browser-control timeout or client error; never treat it as proof about page contents.

Exploration date: 2026-08-17. Dynamic page contents and counts must be refreshed.

## Inventory and status

| Route or label | Page type | Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| Footer `Site Map` → `/sitemap/` | HTML sitemap | UI-verified | current-tab visual + current-tab DOM/interaction | Products, Resources, News Releases, Contact, About, RSS, Blogs, MultiVu, ProfNet, demo, and language groups. |
| `/robots.txt` | robots metadata candidate | client-blocked | automation/control error + same-tab visual retry | `ERR_BLOCKED_BY_CLIENT`; prior Sitemap page remained visible after retry. |
| `/` | marketing homepage | UI-verified | current-tab visual + current-tab DOM/interaction | Hero, product claims, featured stories, journalists/resources, topics, sectors, newsletter form. |
| `/news-releases/` | newsroom overview | UI-verified | current-tab DOM/interaction | Featured, Latest, Most viewed, journalist/marketer calls to action. |
| `/news-releases/news-releases-list/` | all-news list candidate | discovered/UI route family | sitemap + visible Latest links | Reopen and verify current controls before use. |
| `/news-releases/<category>-latest-news/` | category overview | UI-verified | current-tab DOM/interaction | Health was verified; other top-level categories use visible menu links. |
| `/news-releases/<category>-latest-news/<category>-list/` | category list | UI-verified | current-tab DOM/interaction | Health list exposed date/time, Go, page-size, and latest cards. |
| `/news-releases/<slug>-<id>.html` | release detail | UI-verified | current-tab DOM/interaction | Title, provider, ET timestamp, bullets/body, source, related releases, categories. |
| `/news/<organization-slug>/` | organization release index | UI-verified | current-tab DOM/interaction | Date/time jump and release list; opened for Centene Corporation. |
| `/search/all/?keyword=<query>` | all search results | UI-verified | current-tab DOM/interaction | Search overlay submits here; result-type tabs preserve the keyword. |
| `/search/news/?keyword=<query>` | news search results | UI-verified | current-tab DOM/interaction | Search result page exposed 25/50/75/100 options, with 75/100 disabled in the observed state. |
| `/news-releases/multimedia/` | multimedia overview | UI-verified | current-tab DOM/interaction | Featured releases with videos/photos and Latest multimedia list. |
| `/news-releases/multimedia/multimedia-list/` | multimedia list | discovered/UI route family | visible Latest link | Reopen before use. |
| `/resources/` | resources overview | UI-verified | current-tab DOM/interaction | Resource tabs, page-size, category selector, cards, pagination. |
| `/resources/articles/` | resource category list | UI-verified | current-tab DOM/interaction | Articles list with pagination and the same generic category control. |
| `/resources/<section>/<slug>/` | resource detail | UI-verified | current-tab DOM/interaction | Article title, explanatory body, source links, author block. |
| `/amplify-platform/` | Amplify platform overview | UI-verified | current-tab DOM/interaction | Plan/Create/Distribute/Report sections, FAQ, public demo form. |
| `/products/all-products/` | product catalog | UI-verified | current-tab DOM/interaction | All/Marketing/Public Relations/IR & Compliance/Agency tabs and product cards. |
| `/products/overview/` | product overview candidate | redirected | current-tab DOM/interaction | Navigation resolved to `/amplify-platform/` during exploration; verify before relying on the alias. |
| `/rss/` | RSS explainer | UI-verified | current-tab DOM/interaction | Channel table, raw-feed buttons, widget and publisher guidance. |
| `/contact-us/` → `/contact-us/general-inquiries/` | contact form | UI-verified | current-tab DOM/interaction | Public form with personal/contact fields, terms, reCAPTCHA, disabled submit. |
| `/account/online-account-form/` | Send a Release account form | UI-verified | current-tab DOM/interaction | Account-creation form with contact, organization, release-volume, terms, reCAPTCHA. |
| `app.prnewswire.com/login/auto` | protected login | UI-verified | current-tab DOM/interaction | Cision login showed username, keep-signed-in checkbox, next step, help, and account-unlock links. |

## Sitemap groups

The HTML sitemap exposed stable route families for Products (`/products/`), Resources (`/resources/`), News Releases (`/news-releases/`), Contact (`/contact-us/`), RSS (`/rss/`), and multilingual sections (`/cs/`, `/da/`, `/de/`, `/es/`, `/fr/`, `/it/`, `/nl/`, `/no/`, `/pl/`, `/pt/`, `/ru/`, `/sk/`, `/sv/`). Language pages were not exhaustively opened; use their visible labels and current UI when requested.

Do not follow tokenized tracking URLs, `javascript:` share links, CAPTCHA links, or external partner links merely because they appear in the sitemap or page DOM.
