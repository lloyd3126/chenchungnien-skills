---
name: pr-newswire-news
description: Browse and verify public PR Newswire news releases through the Codex in-app browser. Use for latest/category/topic lists, date and hour filtering, organization release histories, individual release details, or multimedia gallery pages.
---

# PR Newswire News

## Purpose and entry points

Use this skill for newsroom research, not product marketing or account work. Start from the visible `News` link, a visible news-menu child, or a release link already shown in the current PR Newswire tab. Read [the site package](../../sites/pr-newswire/AGENTS.md), [the route map](../../sites/pr-newswire/references/site-map.md), and [the interaction guide](../../sites/pr-newswire/references/interaction-guide.md) when needed.

## Choose the route

- Latest newsroom → `News` → `/news-releases/`.
- Category/topic → expand `News in Focus`, `Business & Money`, `Science & Tech`, `Lifestyle & Health`, `Policy & Public Interest`, or `People & Culture`; select a visible child.
- Full category list → use the visible `Latest` link on a category overview.
- Organization history → open the provider's visible organization link or `More Releases From This Source`.
- Specific release → open the visible release card/link from a list or search result.
- Multimedia → `News in Focus` → `Multimedia Gallery`, or `/news-releases/multimedia/`; use its visible `Latest` link for the list.

Do not infer category or organization slugs when a visible link is available.

## News list workflow

1. Verify the route and page heading (`Browse News Releases`, a category heading, `All <Category>`, or an organization heading).
2. On list pages, use `Jump to News Releases:` with `MM/dd/yyyy` and the visible hour selector only when the user requests a time slice. Click `Go` and verify the selected date/hour plus the first result timestamp.
3. Use the enabled `Select number of items per page` option when useful. Verify the selected option, current state/URL, heading, and first result after the update.
4. Read release cards as live records: timestamp, title, summary, image/media presence, and URL. Open the exact card only when details are needed.

The observed list query encoded `month`, `day`, `year`, and `hour`; route encoding may change, so trust the current UI and verify the selected controls instead of constructing query strings.

## Release detail workflow

Verify:

- page title and release URL
- `News provided by` organization
- publication timestamp with timezone label
- key-point bullets and article body
- source line, ticker/financial link when present, and forward-looking/legal language
- `Also from this source`, `More Releases From This Source`, and `Explore` routes when relevant

Attribute company claims to the release. A press release is not independent verification. Share links for Facebook, Twitter, LinkedIn, WhatsApp, Pinterest, and email are outward-action controls; do not click them during read-only research.

## Multimedia workflow

On `Multimedia Gallery`, verify the page explanation, featured cards, image/video presence, and the visible `Latest` list link. Individual multimedia releases still use the normal release-detail model; do not assume every media asset is downloadable or reusable without checking the current UI and rights context.

## Freshness and output

Re-fetch current lists, timestamps, counts, most-viewed/featured sections, and organization records for each request. Report the route, heading, retrieval time/date when useful, and evidence-backed current release fields. Keep live rows out of skills and references.

## Safety and limits

- Use only the user's existing Codex in-app browser tab; no API, CLI, web search, external browser, or temporary discovery tab.
- Do not publish, share, subscribe, submit a release, request a demo, complete a form, solve CAPTCHA, or enter credentials.
- If a branch requires login or the current session is not visibly authenticated, report it as protected and ask before manual sign-in. No authenticated Amplify workspace was explored in this pass.

## Drift maintenance

Compare the current visible menus, routes, labels, list controls, release structure, and first-party explanations with this procedure before acting. Patch only stable, directly verified differences in this skill or its references, keeping public/authenticated variants separate; then re-run a safe representative list/detail workflow and `quick_validate.py`.

## References

- [site-map.md](../../sites/pr-newswire/references/site-map.md) — verified route families and inventory status.
- [data-model.md](../../sites/pr-newswire/references/data-model.md) — release, organization, taxonomy, search, and media entities.
- [interaction-guide.md](../../sites/pr-newswire/references/interaction-guide.md) — date/hour/page-size controls and safe evidence checks.
- [first-party-guidance.md](../../sites/pr-newswire/references/first-party-guidance.md) — release attribution and freshness rules.
