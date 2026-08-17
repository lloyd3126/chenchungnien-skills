# Chen Chung Nien Skills

[繁體中文](./README.zh-TW.md)

A curated collection of reusable agent skills designed by Chen Chung Nien.

This repository showcases the skills I design and publish to help AI agents work more reliably in specific domains.

## About

Each skill in this repository is designed to be practical, maintainable, and clearly scoped for real work instead of one-off prompting.

## Skills In This Repo

| Skill | Description |
| :--- | :--- |
| [`tw-gov-data`](skills/tw-gov-data) | Discover, inspect, compare, and summarize datasets from Taiwan's government open data platform, `data.gov.tw`. |
| [`tw-stock-data`](skills/tw-stock-data) | Fetch, validate, and analyze Taiwan stock, OTC, futures, options, and MOPS financial datasets using the `tw-stock` CLI. |
| [`website-skill-builder`](skills/website-skill-builder) | Systematically explore a website in Codex's built-in browser and turn its stable structure, workflows, and data model into reusable agent guidance. |
| [`reuters-news-search`](skills/reuters-news-search) | Search and filter current Reuters coverage through the built-in browser. |
| [`reuters-market-data`](skills/reuters-market-data) | Inspect Reuters Markets sections, regional tabs, quote tables, and delayed LSEG data. |
| [`reuters-article-research`](skills/reuters-article-research) | Read Reuters article details, visible source context, media, and access state. |
| [`globenewswire-search`](skills/globenewswire-search) | Search and verify public GlobeNewswire newsroom releases by keyword, category, organization, or tag. |
| [`globenewswire-release`](skills/globenewswire-release) | Inspect public GlobeNewswire release metadata, body structure, tags, links, and related-release routes. |
| [`globenewswire-rss`](skills/globenewswire-rss) | Locate and verify public GlobeNewswire RSS, ATOM, and JavaScript widget feeds. |
| [`pr-newswire-search`](skills/pr-newswire-search) | Search and filter public PR Newswire releases, organizations, products, and resources. |
| [`pr-newswire-news`](skills/pr-newswire-news) | Browse and verify PR Newswire news releases, categories, organization histories, and multimedia. |
| [`pr-newswire-resources`](skills/pr-newswire-resources) | Research PR Newswire products, Amplify modules, resources, RSS, and public guidance. |
| [`sec-filings-research`](skills/sec-filings-research) | Search and verify SEC.gov and EDGAR company records, CIKs, filing histories, filing details, and API documentation. |
| [`sec-regulatory-monitoring`](skills/sec-regulatory-monitoring) | Monitor SEC newsroom items, rulemaking activity, public-comment dockets, and related regulatory documents. |
| [`tabelog-search`](skills/tabelog-search) | Search and filter public Tabelog listings in Codex's built-in browser, including autocomplete-based area selection and result verification. |
| [`tabelog-restaurant`](skills/tabelog-restaurant) | Inspect Tabelog restaurant pages and related menus, photos, reviews, ratings, maps, and availability through the built-in browser. |
| [`koding-school-learning`](skills/koding-school-learning) | Browse koding.school courses, enrolled-course filters, course details, and lesson page variants through the built-in browser. |
| [`koding-school-community`](skills/koding-school-community) | Read koding.school knowledge points and safely search course discussions and replies. |
| [`koding-school-projects`](skills/koding-school-projects) | Browse signed-in koding.school projects, studios, profile, inbox, and account entry points without mutating data. |
| [`statementdog-stock-analysis`](skills/statementdog-stock-analysis) | Inspect Statement Dog company pages, health checks, financial metrics, valuation, ownership, products, topics, and related news. |
| [`statementdog-screening`](skills/statementdog-screening) | Build and verify Statement Dog custom screens, strategy lists, metric rankings, sorting, pagination, and comparisons. |
| [`statementdog-market`](skills/statementdog-market) | Explore Statement Dog market, industry, topic, news, blog, and industry-report views. |
| [`statementdog-watchlist`](skills/statementdog-watchlist) | Read signed-in Statement Dog feeds, tracking portfolios, and account areas without mutating the account. |
| [`manny-pro-methodology`](skills/manny-pro-methodology) | Extract reusable business research methods from Manny Pro 商業解碼 articles. |
| [`manny-pro-research`](skills/manny-pro-research) | Run Manny Pro-style value-chain, unit-economics, capital-efficiency, scenario, and reverse-valuation research. |
| [`manny-pro-statementdog-bridge`](skills/manny-pro-statementdog-bridge) | Map Manny methods to Statement Dog facts, custom calculations, and external-data gaps. |
| [`x-home-feed`](skills/x-home-feed) | Read X home timelines, including For You, Following, and visible custom timelines, without publishing or interacting. |
| [`x-profile`](skills/x-profile) | Inspect X profiles, public timeline tabs, profile metadata, and profile entry points. |
| [`x-search`](skills/x-search) | Search X with autocomplete and verify popular, latest, people, media, and list results. |
| [`x-post`](skills/x-post) | Inspect X posts, conversations, quoted content, media, and available post analytics. |

## Website-specific Guidance

The [Tabelog site package](sites/tabelog/AGENTS.md) provides routing, session, freshness, and verification guidance for the Tabelog skills. Its [references](sites/tabelog/references) document the sitemap hierarchy, data model, and first-party explanations discovered during exploration.

The [X site package](sites/x/AGENTS.md) provides shared routing, autocomplete, post/profile data-model, session, and safety guidance for the X skills. Its [references](sites/x/references) document verified page types and interaction rules.

The [Statement Dog site package](sites/statementdog/AGENTS.md) provides shared routing, authentication, freshness, and verification guidance for the four Statement Dog skills. Its [references](sites/statementdog/references) document the site map, data model, form controls, and first-party explanations.

The [橘蘋學習平台 site package](sites/koding-school/AGENTS.md) provides routing, public/authenticated session boundaries, freshness rules, and safe-operation guidance for the koding.school skills. Its skill references document the verified course, discussion, project, and studio page types.

The [SEC.gov site package](sites/sec/AGENTS.md) provides shared EDGAR, Newsroom, rulemaking, public-comment, freshness, evidence, and safety guidance for the SEC skills. Its [references](sites/sec/references) document the route map, data model, first-party API/search guidance, and agent usability scenarios.

The [GlobeNewswire site package](sites/globenewswire/AGENTS.md) provides shared public newsroom, release, RSS, freshness, evidence, and authentication-boundary guidance for the three GlobeNewswire skills. Its [references](sites/globenewswire/references) document verified routes, the public data model, and first-party terminology.

The [Reuters site package](sites/reuters/AGENTS.md) provides shared public-navigation, sitemap, search, Markets, article, freshness, source, and safety guidance for the Reuters skills. Its [references](sites/reuters/references) document the route map, data model, controls, first-party guidance, and agent usability scenarios.

The [PR Newswire site package](sites/pr-newswire/AGENTS.md) provides shared public-newsroom, product/resource, RSS, freshness, evidence, and authentication-boundary guidance for the three PR Newswire skills. Its [references](sites/pr-newswire/references) document the route map, public data model, controls, first-party terminology, and safety boundaries.

## Usage

Use `website-skill-builder` when a website should become a reusable tool for future agents. It explores the current tab in Codex's built-in browser, starts with the site's sitemap when available, covers public functionality first, and proceeds into safe protected functionality when the current session is visibly authenticated; otherwise it asks before manual sign-in and protected exploration.

For Tabelog tasks, use `tabelog-search` for listings and filters, and `tabelog-restaurant` for restaurant details and subpages. Future agents should compare live UI and documentation with these files and update stable, verified differences when the workspace is writable.

For X tasks, route by intent to `x-home-feed`, `x-profile`, `x-search`, or `x-post`. Future agents should compare the live X UI with `sites/x/AGENTS.md` and keep search results, post content, metrics, and account data dynamic.

For Statement Dog tasks, route by intent to `statementdog-stock-analysis`, `statementdog-screening`, `statementdog-market`, or `statementdog-watchlist`. Future agents should compare the live UI with `sites/statementdog/AGENTS.md` and keep financial values, rankings, articles, market data, and account data dynamic.

For Manny Pro research tasks, use `manny-pro-methodology` to extract article methods, `manny-pro-research` for full company research, and `manny-pro-statementdog-bridge` to connect the methods to Statement Dog facts and external data gaps. Series notes, the method index, and the coverage matrix live under `sites/manny-pro/references`; the 10 method references live under `skills/manny-pro-methodology/references` and follow the Statement Dog industry-methodology pattern.

For koding.school tasks, route course and lesson work to `koding-school-learning`, knowledge and discussion work to `koding-school-community`, and project/studio/account-entry work to `koding-school-projects`. Keep current progress, project records, messages, and other account data dynamic and private.

For SEC.gov tasks, use `sec-filings-research` for CIK/company search, EDGAR full-text and latest filings, filing detail, or API/XBRL documentation; use `sec-regulatory-monitoring` for Newsroom, rulemaking, events, speeches, and public comments. Keep current filings, news, rule status, comment availability, and counts dynamic, and stop before filing or comment submission.

For GlobeNewswire tasks, use `globenewswire-search` for public discovery, `globenewswire-release` for a specific release, and `globenewswire-rss` for syndication feeds. Keep current release rows, timestamps, tags, feed entries, and account data dynamic; stop at login, CAPTCHA, registration, publishing, sharing, or other irreversible actions.

For Reuters tasks, use `reuters-news-search` for site search and filters, `reuters-market-data` for Markets, quotes, tables, and regional tabs, and `reuters-article-research` for article details and source context. Keep current headlines, result counts, article text, rankings, prices, yields, and account data dynamic; stop before Save, Share, Subscribe, account, or purchase actions.

For PR Newswire tasks, use `pr-newswire-search` for keyword/result-type discovery, `pr-newswire-news` for releases, categories, organizations, and multimedia, and `pr-newswire-resources` for products, resources, RSS, and first-party guidance. Keep current releases, timestamps, counts, resource listings, product claims, and account data dynamic; stop before sharing, submitting forms, solving CAPTCHA, entering credentials, or sending a release.

## Installation

You can browse and install skills from this repository using the [Vercel skills CLI](https://skills.sh/docs/cli).

### Using Vercel skills CLI

```sh
# Interactively browse and install skills from this repo.
npx skills add lloyd3126/chenchungnien-skills --list

# Install a specific skill globally.
npx skills add lloyd3126/chenchungnien-skills --skill tw-gov-data --global
npx skills add lloyd3126/chenchungnien-skills --skill tw-stock-data --global
npx skills add lloyd3126/chenchungnien-skills --skill website-skill-builder --global
npx skills add lloyd3126/chenchungnien-skills --skill pr-newswire-search --global
npx skills add lloyd3126/chenchungnien-skills --skill pr-newswire-news --global
npx skills add lloyd3126/chenchungnien-skills --skill pr-newswire-resources --global
npx skills add lloyd3126/chenchungnien-skills --skill sec-filings-research --global
npx skills add lloyd3126/chenchungnien-skills --skill sec-regulatory-monitoring --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-search --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-restaurant --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-stock-analysis --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-screening --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-market --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-watchlist --global
npx skills add lloyd3126/chenchungnien-skills --skill manny-pro-methodology --global
npx skills add lloyd3126/chenchungnien-skills --skill manny-pro-research --global
npx skills add lloyd3126/chenchungnien-skills --skill manny-pro-statementdog-bridge --global
npx skills add lloyd3126/chenchungnien-skills --skill x-home-feed --global
npx skills add lloyd3126/chenchungnien-skills --skill x-profile --global
npx skills add lloyd3126/chenchungnien-skills --skill x-search --global
npx skills add lloyd3126/chenchungnien-skills --skill x-post --global
```
