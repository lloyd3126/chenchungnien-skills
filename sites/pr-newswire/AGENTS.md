# PR Newswire

## Scope

PR Newswire is a public newsroom, press-release archive, multimedia gallery, resource library, and product-marketing site. This package covers public discovery and read-only research through the Codex in-app browser.

Use:

- `$pr-newswire-search` for keyword search and result-type filtering.
- `$pr-newswire-news` for news categories, topic/list pages, organization release indexes, individual releases, and multimedia.
- `$pr-newswire-resources` for products, Amplify modules, resources, RSS guidance, and public first-party explanations.

## Sitemap-assisted inventory

- The visible footer `Site Map` at `https://www.prnewswire.com/sitemap/` was opened in the user's existing tab and rendered as an HTML sitemap. It groups Products, Resources, News Releases, Contact Us, About PR Newswire, RSS News Feeds, Blogs, MultiVu, ProfNet, Request a Product Demo, and language variants.
- Representative sitemap routes were reopened through the same tab and UI-verified: `/news-releases/`, category and list routes under `/news-releases/`, `/news-releases/multimedia/`, `/resources/`, `/resources/articles/`, `/amplify-platform/`, `/products/all-products/`, `/rss/`, `/contact-us/`, and public account/demo forms.
- Same-origin `/robots.txt` was attempted twice in the same tab. The in-app browser reported `ERR_BLOCKED_BY_CLIENT`; visual retry left the prior Sitemap page visible. Record this as `client-blocked` evidence, not as proof that robots.txt or an XML sitemap is empty or absent.
- Do not exhaustively crawl the sitemap or copy live URL inventories into durable instructions. Treat sitemap-only entries as candidates until the corresponding UI is reopened.

Read [site-map.md](references/site-map.md) for the route map and evidence status.

Read [agent-usability-tests.md](references/agent-usability-tests.md) when choosing between the three skills or reviewing routing regressions.

## Global routing

- Keyword or organization lookup → `$pr-newswire-search` → header `Search` → query → `All`, `News`, `Organizations`, `Products`, or `Resources` result type.
- Latest, category, topic, or time-sliced releases → `$pr-newswire-news` → `News` or a visible news-menu category → overview/list page.
- A specific release → `$pr-newswire-news` → open the visible release card/link → verify title, provider, timestamp, body, and related links.
- Product comparison or platform explanation → `$pr-newswire-resources` → `Products`/`All Products` or `Amplify Platform`.
- Article, white paper, webinar, case study, or toolkit → `$pr-newswire-resources` → `Resources` and its visible resource-section tabs.
- Feed or syndication explanation → `$pr-newswire-resources` → footer `RSS`.

## Navigation

- `News` → public newsroom overview at `/news-releases/`.
- `Products` → Amplify platform at `/amplify-platform/`; its product menu exposes Plan, Create, Distribute, Report, Amplify Content, and All Products.
- `Resources` → resource overview at `/resources/`; resource-section tabs expose Articles, Tip Sheets, White Papers, Webinars, Case Studies, Toolkits, and News Trends.
- `Search` → overlay with placeholder `Search News Releases, Organizations, Resources, and Products`.
- `News in Focus`, `Business & Money`, `Science & Tech`, `Lifestyle & Health`, `Policy & Public Interest`, and `People & Culture` → expandable news menus. Use the visible child label rather than guessing a slug.
- `Client Login` → `app.prnewswire.com`/Cision login. `Send a Release` → public account-creation form.

## Operating rules

1. Use only the Codex in-app browser and the user's already-visible active tab. Preserve the tab and session; do not switch browsers, create a discovery tab, use an API/CLI, or use web search as a substitute.
2. Before each task, compare the current visible labels, URL, controls, permissions, and first-party explanations with this package. The current UI is authoritative.
3. Keep public exploration read-only. Do not click social-share links, send a release, request a demo, submit contact/account forms, accept marketing terms, upload media, or follow an external partner link unless the user explicitly requests the action and any required confirmation is obtained.
4. Never enter passwords, OTPs, personal contact details, private company data, or payment information. Do not solve CAPTCHAs. The public forms observed here include contact fields, contractual checkboxes, marketing-consent language, reCAPTCHA, and disabled submit buttons until completed.
5. The current session was not visibly authenticated. If a future task needs protected Amplify functionality, finish the public route first, then ask the user to sign in manually in this same tab. After login, re-check public routes and controls as a separate authenticated variant before documenting differences.
6. Re-fetch current release rows, dates, timestamps, counts, pagination, resource listings, product claims, and organization records during each task. Never store live search results or one-off counts in instructions.
7. Verify every navigation with the current URL plus a page heading, selected control, result title, or explicit empty/protected state. A successful navigation/control call alone is not evidence that the page visibly opened.

## Data and freshness

See [data-model.md](references/data-model.md) for entities and relationships, and [interaction-guide.md](references/interaction-guide.md) for safe controls and verification. See [first-party-guidance.md](references/first-party-guidance.md) for definitions and site-provided limitations.

## Drift maintenance

If the live UI differs, complete a safe task using the current visible UI, then record the public/authenticated variant, route, old documented behavior, observed behavior, evidence source, and date. Patch this file, the owning skill, or a reference only when the change is stable and directly supported. Keep dynamic results out of durable guidance and re-run the affected safe workflow plus `quick_validate.py` after edits. Report broad, contradictory, or unsafe changes instead of guessing.

## Known limits

- No protected Amplify workspace was explored because the current tab showed the Cision login screen rather than an authenticated session.
- Login, account creation, Send a Release, Request a Demo, Contact, subscription/marketing forms, social sharing, CAPTCHA, and contractual acceptance were intentionally not submitted or completed.
- Some later same-tab screenshot calls returned a timeout or `target closed` control error while the page DOM was available. Those errors are recorded as control limitations, not as claims that the routes were empty or unavailable.
