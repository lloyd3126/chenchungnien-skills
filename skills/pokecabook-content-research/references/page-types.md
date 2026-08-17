# PokecaBook public page types

Exploration basis: 2026-08-17, public state in the Codex in-app browser. This reference describes reusable structure, not current content values.

## Route families

| Page type | Representative routes | Extract |
|---|---|---|
| Category list | `/archives/category/tournament`, `/archives/category/deck-recipe`, `/archives/category/card-list`, `/archives/category/column`, `/archives/category/beginner` | heading, post cards, category labels, dates, detail URLs, pagination |
| Tournament subcategory | `/archives/category/tournament/city-league`, `/jim-battle`, `/champions`, `/extra` | event type, environment/date, placement scope, article links |
| Chronological list | `/post` | newest public posts, category, date, detail URL, pagination |
| Article detail | `/archives/<numeric-id>` | title, date, TOC, section headings, section content, first-party links |
| Environment deck index | `/archives/1417` | deck archetype labels and links to recipe articles |
| Tier/ranking article | `/archives/26148` | update date, environment, Tier headings, explanatory text, links to deck indexes and card-adoption analysis |
| Card-list article | `/archives/323482` or another current card-list link | set name, release date, TOC, card names, card text/attacks when rendered |
| Season/result roundup | `/archives/30272` | season headings, environment sections, event-result links, placement/deck references |

## Entity relationships

```text
category/list → post/article → TOC section → deck/event/card entity
ranking article → deck-index article → recipe/detail article
tournament roundup → season/environment → event result article → deck entry
card-list category → set article → card section
```

Article TOCs use visible `#tocN` anchors. A deck entry can be represented by a section heading, an image-backed recipe, a placement/date line, or a link to an official Pokémon deck-code page. The external deck-code page is a separate source and must not be conflated with PokecaBook's article claim.

## Observed structural examples

- Tournament list pages expose `次のページ`, page numbers, and `次へ`; archive depth varies by category.
- City League entries commonly describe `ベスト16`; Jim Battle entries commonly describe daily `優勝` summaries; Champions League entries group named events and World Championships; Expanded entries group environment or event summaries.
- The Tier article contains `ストームエメラルダ環境`, `Tier ランキング`, and Tier sections. It also links to deck recipe pages and the `カード採用率` route. Its live update date and Tier assignments must always be refetched.
- Card-list articles use a set heading, a release-date line, a TOC, and card sections with names, abilities, attacks, and effect text.
- Public contact and privacy pages are not research data sources. `/inquiries` directs users to the site's X account DM; `/privacy-policy` documents site disclaimers and reCAPTCHA usage.

## Evidence and limits

Use current-tab visual evidence when a screenshot succeeded, current-tab DOM/interaction for rendered text and links, and automation/control error for browser failures. During this exploration, same-origin `/robots.txt` and `/sitemap.xml` were client-blocked, while `/sitemap_index.xml` rendered a PokecaBook 404; do not infer that blocked routes are empty. No authenticated account branch was observed.
