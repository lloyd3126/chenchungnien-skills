# Chen Chung Nien Skills

[繁體中文](./README.zh-TW.md)

A curated collection of reusable agent skills for reliable, repeatable work across research databases, market tools, government services, social platforms, and content sites.

Each skill has one clear responsibility. Website packages add shared navigation, data-model, freshness, authentication, evidence, and safety guidance so related skills behave consistently.

## Start Here

- To use an existing skill, find the task area below and choose the narrowest matching skill.
- To understand a supported website as a whole, open the package name; it links to that site's shared `AGENTS.md` guidance.
- To turn a new website into reusable guidance and skills, use `website-skill-builder`.
- To see what still needs live validation, check [Known Unverified Workflows](#known-unverified-workflows) before using a package.

Browser-based skills default to current, verifiable page state and read-only exploration. Credentials, session data, live counts, and one-off results do not belong in durable guidance; actions that publish, purchase, submit, message, or change account state require explicit authorization.

## Known Unverified Workflows

This is the repository-wide rollup of gaps explicitly recorded in the site packages. `Unverified` or `partial` means a workflow was not exercised end to end in the available in-app browser session; it does **not** mean the feature is unavailable or does not exist. Re-check the linked source and current UI before relying on any workflow below.

Across every package, state-changing actions—sign-in or sign-out, account edits, save or follow, publishing, commenting, messaging, form submission, booking, purchase, payment, upload, credential or token creation, CAPTCHA, and third-party authorization—remain intentionally untested unless a package explicitly records otherwise and the user authorizes the action.

### Taiwan Public Data, Law, Education, and Libraries

| Package | Unverified or partial workflows |
| :--- | :--- |
| [Taiwan Government Open Data](sites/data-gov-tw/references/site-map.md) | `Columns` and statistics pages are route-map only; authenticated comments/account features, RSS payloads, external resources, and download flows were not fully explored. |
| [TDX](sites/tdx/AGENTS.md) | Personal account details stop at a password gate; purchases, deletion, applications, and other submissions were not exercised. |
| [Taiwan Judicial legal search](sites/judicial-lawsearch/references/first-party-guidance.md) | Protected content was not explored; the judgment-system guidance page timed out, so its complete coverage and update schedule remain unverified. |
| [Taiwan Laws & Regulations Database](sites/law-moj/references/site-map.md) | E-government login, favorite laws, and custom folders remain unverified; some long judicial, cross-agency, refresh, API, and Smart Search pages have DOM evidence but not complete visual verification. |
| [Adaptive Learning Network](sites/adl/references/coverage.md) | Course Overview, AI Companion, and the complete protected teacher sidebar need authenticated re-verification; assignment, class/student changes, imports, uploads, and account operations were intentionally not tested. |
| [Substitute Teacher Talent Pool](sites/k12ea-ptst/AGENTS.md) | Authenticated resumes, favorites, complete contact data, later-round recruitment data, applications, matching, and employer/admin workflows were not explored. |
| [National Library of Public Information](sites/nlpi/AGENTS.md) | `myispace` and `myactivity` returned site errors, `myebook` was client-blocked, external member-service destinations were not deeply explored, and standalone 7-day/keyword activity filters were unstable. |

### Markets, Companies, and Regulatory Research

| Package | Unverified or partial workflows |
| :--- | :--- |
| [Google Finance](sites/google-finance/AGENTS.md) | The signed-out variant remains unconfirmed; research submission, discussions/tasks, deep search, watchlist analysis, list creation, and portfolio creation were not exercised. |
| [Koyfin](sites/koyfin/references/coverage.md) | Advisor Tools, remaining Market Overview children, and individual press-release/transcript pages remain unverified; My Graphs is only partially verified. |
| [Statement Dog](sites/statementdog/references/site-map.md) | Blog search submission remains unconfirmed and company comparison is partial; saving screens, changing watchlists/accounts, payments, and comments were not exercised. |
| [Seeking Alpha](sites/seeking-alpha/references/site-map.md) | Portfolio, subscriptions, Investing Groups, and account-dependent content remain unverified; custom screener fields, operators, sorting, reset, save, and comparison are not fully tested. |
| [SEC.gov](sites/sec/AGENTS.md) | Authenticated and filer-management branches remain unexplored; filings, public comments, tips/complaints, subscriptions, API tokens, uploads, and account actions were not submitted. |
| [FRED](sites/fred/references/site-map.md) | Release/source/category detail pages, account features, Add-in, mobile apps, maps, and ALFRED were not deeply explored; detailed Help panels remained on a spinner. |
| [AnnualReports.com](sites/annualreports/references/exploration-checklist.md) | The current-report target was not verified in a new tab; pagination/sorting, authenticated variants, external partners, ratings, hardcopy requests, Add Company, and shipment submissions remain unverified or intentionally untested. |

### News, Essays, and Research Databases

| Package | Unverified or partial workflows |
| :--- | :--- |
| [Reuters](sites/reuters/AGENTS.md) | My News, saved/followed content, accounts, registration/login, subscriptions, paywalled content, and personalization were not verified. |
| [GlobeNewswire](sites/globenewswire/references/site-map.md) | RSS Industry/Location tab content and major search-filter option lists/results remain partial; customer/reader account workflows were not explored. |
| [PR Newswire](sites/pr-newswire/AGENTS.md) | The protected Amplify workspace remains unconfirmed; client login, account creation, release submission, demo/contact, marketing forms, social sharing, and CAPTCHA were intentionally not completed. |
| [Manny Pro](sites/manny-pro/references/site-map.md) | Account Profile is partial; membership management, subscription cancellation, refunds, payments, payment-info changes, sign-out, and Apple/Spotify linking were not tested. |
| [Paul Graham](sites/paul-graham/references/agent-usability.md) | External Y Combinator, Amazon, community/forum, and feed destinations were not explored; email, purchase, application, and interaction flows were intentionally not tested. |
| [Web of Science](sites/webofscience/references/exploration-checklist.md) | Query Builder's distinct behavior, Research Assistant cards, export/alerts/marked lists, current authenticated profile re-entry, ORCID syncing, Account Settings, child My Records pages, and publisher/product pages remain unconfirmed. |

### Social, Publishing, Learning, and Local Discovery

| Package | Unverified or partial workflows |
| :--- | :--- |
| [X](sites/x/references/site-map.md) | Notifications, direct messages, history, account settings, Grok, Premium, Creator Studio, Articles, Spaces, ads, third-party login, and payments were not explored. |
| [Threads](sites/threads/references/site-map.md) | Date-before/custom-date/profile search filters and the profile-to-author-search route are not fully verified; some Insights details and new-message flows remained on loading skeletons. |
| [Facebook](sites/facebook/AGENTS.md) | Personalized group feeds, actual account-setting changes, messaging, posting/interactions, payments, and Marketplace listing flows were not tested. |
| [vocus](sites/vocus/AGENTS.md) | Some heavy feed/salon pages have DOM-only or partial visual evidence; purchasing, membership changes, publishing, and Studio mutations were intentionally not exercised. |
| [koding.school](sites/koding-school/references/exploration-checklist.md) | Project editor, recycle bin, studio creation/removal, account updates, private message bodies, payments, orders, and subscriptions remain unverified. |
| [PokecaBook](sites/pokecabook/references/site-map.md) | No authenticated/account branch was observed; inquiry-by-X-DM, reCAPTCHA, external destinations, and irreversible workflows were not tested. |
| [Tabelog](sites/tabelog/references/site-map.md) | Third-party authentication, signed-in navigation, saved/visited lists, review editor, personalization, member rankings, reservation-account features, booking, and payment remain unverified or intentionally untested. |

When a gap is verified, update the owning site package first, then remove or narrow its README entry in the same change. Keep transient outages and browser-control failures distinct from genuine feature absence.

## Skill Directory

The directory is organized by task domain first, then by platform or website package, with focused skills listed under each package.

[Taiwan public data, law, education, and libraries](#taiwan-public-data-law-education-and-libraries) · [Markets, companies, and regulatory research](#markets-companies-and-regulatory-research) · [News, essays, and research databases](#news-essays-and-research-databases) · [Social, publishing, learning, and local discovery](#social-publishing-learning-and-local-discovery) · [Build website skills](#build-website-skills)

### Taiwan Public Data, Law, Education, and Libraries

- **[Taiwan Government Open Data](sites/data-gov-tw/AGENTS.md)** — Search datasets, inspect metadata and resources, or follow platform news.

  Skills: [`tw-gov-data`](skills/tw-gov-data) · [`tw-gov-data-search`](skills/tw-gov-data-search) · [`tw-gov-data-dataset`](skills/tw-gov-data-dataset) · [`tw-gov-data-news`](skills/tw-gov-data-news)

- **Taiwan market data** — Fetch and analyze TWSE, TPEX, TAIFEX, and MOPS datasets with the `tw-stock` CLI.

  Skill: [`tw-stock-data`](skills/tw-stock-data)

- **[TDX](sites/tdx/AGENTS.md)** — Discover transport APIs and safely inspect authenticated member access, usage, and applications.

  Skills: [`tdx-api-discovery`](skills/tdx-api-discovery) · [`tdx-member-data-access`](skills/tdx-member-data-access)

- **[Taiwan Judicial legal search](sites/judicial-lawsearch/AGENTS.md)** — Route among legal and judgment systems, search public materials, and verify result pages.

  Skills: [`judicial-lawsearch-routing`](skills/judicial-lawsearch-routing) · [`judicial-lawsearch-legal`](skills/judicial-lawsearch-legal) · [`judicial-lawsearch-judgments`](skills/judicial-lawsearch-judgments)

- **[Taiwan Laws & Regulations Database](sites/law-moj/AGENTS.md)** — Search laws, judicial materials, legal notices, scenario guides, and captured government content.

  Skills: [`law-moj-law-search`](skills/law-moj-law-search) · [`law-moj-judicial-search`](skills/law-moj-judicial-search) · [`law-moj-news`](skills/law-moj-news) · [`law-moj-smart-search`](skills/law-moj-smart-search) · [`law-moj-cross-government`](skills/law-moj-cross-government)

- **[Adaptive Learning Network (因材網)](sites/adl/AGENTS.md)** — Read public resources and inspect authenticated teacher workflows safely.

  Skills: [`adl-public-resources`](skills/adl-public-resources) · [`adl-teacher-workflows`](skills/adl-teacher-workflows)

- **[Substitute Teacher Talent Pool](sites/k12ea-ptst/AGENTS.md)** — Find current vacancies and read public recruitment guidance and announcements.

  Skills: [`k12ea-ptst-job-search`](skills/k12ea-ptst-job-search) · [`k12ea-ptst-public-resources`](skills/k12ea-ptst-public-resources)

- **[National Library of Public Information](sites/nlpi/AGENTS.md)** — Search the site, find activities, route digital resources, and inspect member services read-only.

  Skills: [`nlpi-site-search`](skills/nlpi-site-search) · [`nlpi-activity-search`](skills/nlpi-activity-search) · [`nlpi-digital-resources`](skills/nlpi-digital-resources) · [`nlpi-member-center`](skills/nlpi-member-center)

### Markets, Companies, and Regulatory Research

- **[Google Finance](sites/google-finance/AGENTS.md)** — Research quotes and comparisons, earnings calendars, financial statements, and ownership disclosures.

  Skills: [`google-finance-market-research`](skills/google-finance-market-research) · [`google-finance-earnings`](skills/google-finance-earnings)

- **[Koyfin](sites/koyfin/AGENTS.md)** — Monitor markets, resolve securities, research companies, and inspect personal workspaces read-only.

  Skills: [`koyfin-market-monitoring`](skills/koyfin-market-monitoring) · [`koyfin-security-research`](skills/koyfin-security-research) · [`koyfin-advanced-search`](skills/koyfin-advanced-search) · [`koyfin-watchlists-and-screens`](skills/koyfin-watchlists-and-screens)

- **[Statement Dog](sites/statementdog/AGENTS.md)** — Analyze companies, screen stocks, explore markets, inspect watchlists, and turn reports into reproducible research.

  Skills: [`statementdog-stock-analysis`](skills/statementdog-stock-analysis) · [`statementdog-screening`](skills/statementdog-screening) · [`statementdog-market`](skills/statementdog-market) · [`statementdog-watchlist`](skills/statementdog-watchlist) · [`statementdog-stock-research`](skills/statementdog-stock-research)

- **[Seeking Alpha](sites/seeking-alpha/AGENTS.md)** — Research a security, build stock or ETF screens, or investigate market-wide news and calendars.

  Skills: [`seeking-alpha-stock-analysis`](skills/seeking-alpha-stock-analysis) · [`seeking-alpha-screening`](skills/seeking-alpha-screening) · [`seeking-alpha-market-research`](skills/seeking-alpha-market-research)

- **[SEC.gov](sites/sec/AGENTS.md)** — Search EDGAR filings and monitor current SEC news, rulemaking, events, and public-comment dockets.

  Skills: [`sec-filings-research`](skills/sec-filings-research) · [`sec-regulatory-monitoring`](skills/sec-regulatory-monitoring)

- **[FRED](sites/fred/AGENTS.md)** — Find economic series and observations or inspect release schedules and calendars.

  Skills: [`fred-series-data`](skills/fred-series-data) · [`fred-release-calendar`](skills/fred-release-calendar)

- **[AnnualReports.com](sites/annualreports/AGENTS.md)** — Find companies and verify current or archived annual-report links and formats.

  Skills: [`annualreports-search`](skills/annualreports-search) · [`annualreports-company`](skills/annualreports-company)

### News, Essays, and Research Databases

- **[Reuters](sites/reuters/AGENTS.md)** — Search news, inspect market data, and read article details with source and access context.

  Skills: [`reuters-news-search`](skills/reuters-news-search) · [`reuters-market-data`](skills/reuters-market-data) · [`reuters-article-research`](skills/reuters-article-research)

- **[GlobeNewswire](sites/globenewswire/AGENTS.md)** — Search public releases, inspect release details, and locate RSS or ATOM feeds.

  Skills: [`globenewswire-search`](skills/globenewswire-search) · [`globenewswire-release`](skills/globenewswire-release) · [`globenewswire-rss`](skills/globenewswire-rss)

- **[PR Newswire](sites/pr-newswire/AGENTS.md)** — Find and verify releases, organizations, multimedia, products, resources, and RSS guidance.

  Skills: [`pr-newswire-search`](skills/pr-newswire-search) · [`pr-newswire-news`](skills/pr-newswire-news) · [`pr-newswire-resources`](skills/pr-newswire-resources)

- **[Manny Pro](sites/manny-pro/AGENTS.md)** — Read site content, extract reusable business methods, conduct company research, and connect methods to Statement Dog evidence.

  Skills: [`manny-pro-content`](skills/manny-pro-content) · [`manny-pro-methodology`](skills/manny-pro-methodology) · [`manny-pro-research`](skills/manny-pro-research) · [`manny-pro-statementdog-bridge`](skills/manny-pro-statementdog-bridge)

- **[Paul Graham](sites/paul-graham/AGENTS.md)** — Find and compare essays or inspect books, language projects, FAQs, feeds, and other reference pages.

  Skills: [`paul-graham-essay-research`](skills/paul-graham-essay-research) · [`paul-graham-reference-research`](skills/paul-graham-reference-research)

- **[Web of Science](sites/webofscience/AGENTS.md)** — Search documents and cited references, find researchers, and inspect authenticated profiles and metrics.

  Skills: [`wos-document-search`](skills/wos-document-search) · [`wos-researcher-search`](skills/wos-researcher-search) · [`wos-researcher-profile`](skills/wos-researcher-profile)

### Social, Publishing, Learning, and Local Discovery

- **[X](sites/x/AGENTS.md)** — Read home feeds, profiles, searches, posts, conversations, media, and available analytics.

  Skills: [`x-home-feed`](skills/x-home-feed) · [`x-profile`](skills/x-profile) · [`x-search`](skills/x-search) · [`x-post`](skills/x-post)

- **[Threads](sites/threads/AGENTS.md)** — Search public content, inspect profiles and posts, or review authenticated activity, insights, and messaging surfaces read-only.

  Skills: [`threads-search`](skills/threads-search) · [`threads-profile`](skills/threads-profile) · [`threads-post`](skills/threads-post) · [`threads-activity`](skills/threads-activity) · [`threads-insights`](skills/threads-insights) · [`threads-messages`](skills/threads-messages)

- **[Facebook](sites/facebook/AGENTS.md)** — Navigate Facebook safely, search public result types, and inspect Marketplace listings without interacting.

  Skills: [`facebook-navigation`](skills/facebook-navigation) · [`facebook-search`](skills/facebook-search) · [`facebook-marketplace`](skills/facebook-marketplace)

- **[vocus](sites/vocus/AGENTS.md)** — Search and read content, salons, and products or inspect Salon Studio read-only.

  Skills: [`vocus-search`](skills/vocus-search) · [`vocus-content-reader`](skills/vocus-content-reader) · [`vocus-salon`](skills/vocus-salon) · [`vocus-product`](skills/vocus-product) · [`vocus-studio`](skills/vocus-studio)

- **[koding.school](sites/koding-school/AGENTS.md)** — Browse courses and lessons, read community discussions, and inspect projects or studios safely.

  Skills: [`koding-school-learning`](skills/koding-school-learning) · [`koding-school-community`](skills/koding-school-community) · [`koding-school-projects`](skills/koding-school-projects)

- **[PokecaBook](sites/pokecabook/AGENTS.md)** — Search Pokémon Trading Card Game content, research articles and events, and compare deck recipes or card adoption.

  Skills: [`pokecabook-site-search`](skills/pokecabook-site-search) · [`pokecabook-content-research`](skills/pokecabook-content-research) · [`pokecabook-deck-analytics`](skills/pokecabook-deck-analytics)

- **[Tabelog](sites/tabelog/AGENTS.md)** — Search restaurants and inspect restaurant details, menus, photos, reviews, maps, and availability.

  Skills: [`tabelog-search`](skills/tabelog-search) · [`tabelog-restaurant`](skills/tabelog-restaurant)

### Build Website Skills

- **Website skill builder** — Explore a website systematically, map stable behavior and data structures, and create maintainable site guidance and focused skills.

  Skill: [`website-skill-builder`](skills/website-skill-builder)

## Repository Layout

```text
skills/<skill-name>/SKILL.md          Focused task instructions
skills/<skill-name>/agents/           Agent metadata, when provided
sites/<site>/AGENTS.md                Shared site-level operating guidance
sites/<site>/references/              Stable routes, controls, and data models
```

Live page content remains dynamic. The repository records reusable operating knowledge, not cached answers or private session data.

## Installation

Browse and install skills with the [Vercel skills CLI](https://skills.sh/docs/cli):

```sh
# Browse every installable skill in this repository.
npx skills add lloyd3126/chenchungnien-skills --list

# Install one skill globally; replace the name with any linked skill above.
npx skills add lloyd3126/chenchungnien-skills --skill wos-document-search --global
```
