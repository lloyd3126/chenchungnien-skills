---
name: pokecabook-content-research
description: Research public PokecaBook content in the Codex in-app browser, including tournament result lists, deck recipe indexes and articles, card lists, environment rankings, columns, and rule explanations. Use when the user asks for article facts, deck structures, event results, card text, or current Tier context.
---

# PokecaBook Content Research

## Purpose and route selection

Use this skill after the user names a PokecaBook topic, article, deck, event, card set, rule, or category. Start from the current public tab and keep one tab. Read [page-types.md](references/page-types.md) for route families and extraction fields, and [site-map.md](../../sites/pokecabook/references/site-map.md) for the full public inventory.

Useful public routes include:

- `/archives/category/tournament` and its `city-league`, `jim-battle`, `champions`, and `extra` children.
- `/archives/category/deck-recipe`, `/archives/category/card-list`, `/archives/category/column`, and `/archives/category/beginner`.
- `/archives/26148` for the current environment/Tier article structure, `/archives/1417` for the environment deck index, and `/archives/<numeric-id>` for individual articles.
- `/post` for the chronological public post list.

## Procedure

1. Identify the requested entity and choose the narrowest visible category, sitemap link, search result, or direct article URL. Do not exhaustively crawl a paginated archive.
2. Verify the page title, main heading, current URL, publication/update date when shown, and the relevant visible headings or table/cards.
3. For category/list pages, capture the category heading, representative post titles, category labels, dates, detail URLs, and pagination. Treat ordering and counts as dynamic.
4. For article pages, follow the visible table of contents when useful. Extract the requested fields from the article body, not from a guessed URL or image filename. Preserve section associations.
5. For deck/event pages, distinguish the article's deck or event claims from the site's links to official Pokémon deck-code pages. Keep external pages out of scope unless the user explicitly asks for them.
6. For the Tier/ranking article, use the live article as the source of truth. Report its update date and current Tier headings; do not hard-code today's deck positions into this skill or into `AGENTS.md`.
7. Cross-check claims against a second first-party PokecaBook page when practical (for example, a category list plus its article, or a ranking entry plus its deck index). Report disagreements instead of silently choosing one.

## Page semantics

PokecaBook article pages commonly expose a title, social links, a table of contents using `#tocN` anchors, section headings, images or card text, comments, and footer navigation. Category pages expose post cards and pagination. Card-list articles expose set release information and card sections. Tournament result articles may group decks by event, season, environment, rank, or date.

## Safety, scope, and freshness

- Read public content only. Do not submit comments, inquiries, social posts, or any account-changing form.
- Do not follow external X, LINE, `pokemon-card.com`, Google, or other outbound links during normal research.
- Current rankings, event results, release dates, card text, and article revisions are time-sensitive; refetch them for each task and cite the route in the report.
- If content is absent, client-blocked, behind CAPTCHA, or protected by a login wall, record that exact limitation. Do not infer missing data from the sitemap.

## Drift maintenance

Before research, compare live labels, headings, category routes, TOC structure, and result-card semantics with [page-types.md](references/page-types.md). Update the owning reference only for stable structural changes; keep current entities and values live. Rerun one representative category-to-article workflow and the skill validator after a change.

## References

- [page-types.md](references/page-types.md) — route families, entity model, and extraction guidance.
- [site-map.md](../../sites/pokecabook/references/site-map.md) — explored public routes, sitemap status, and evidence boundaries.
