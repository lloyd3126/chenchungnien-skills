---
name: globenewswire-search
description: Search and filter public GlobeNewswire newsroom releases through the Codex in-app browser. Use when the user wants current releases by keyword, news category, organization, tag, or safe pagination and result verification.
---

# GlobeNewswire Search

## Purpose and entry point

Use this skill for public discovery on `https://www.globenewswire.com/`. Work only in the Codex in-app browser and preserve the currently open GlobeNewswire tab and session. Read [the site map](../../sites/globenewswire/references/site-map.md) when a route or page type is unclear. For a known release's body and metadata, hand off to `$globenewswire-release`; for syndication feeds, use `$globenewswire-rss`.

## Choose the route

- **Keyword:** start at `/newsroom`, use the visible `Search All News` form, keep the visible scope `Everything` unless the user specifies another live option, fill the keyword field labeled/placeholder `SEARCH`, and submit with Enter. The observed result pattern is `/en/search/keyword/<encoded-keyword>?pageSize=10`.
- **Broad topic:** use the visible Newsroom navigation link such as `Energy News`, then verify the category heading and release list. Use its visible subcategory links rather than inventing route segments.
- **Organization:** open the visible `Source` link on a result or release page. Verify the `Search Results` page and an `Organization` filter chip; do not construct the encoded organization route yourself.
- **Tag:** open a visible tag link from a release detail page. Verify the resulting filter/heading before using the result list; tag routes were observed but not fully opened during the initial exploration.
- **All search:** use the visible `View All` link to `/en/search` when the user wants the broader search surface, then re-read the current form controls.

## Keyword workflow

1. Inspect the current tab and visible page. If necessary, return through the GlobeNewswire logo or a visible `Newsroom` link in the same tab.
2. Locate the visible newsroom search field. Do not use a hidden duplicate or assume that typing alone submitted the query.
3. Fill the user's exact non-sensitive keyword and press Enter. This is a read-only search; do not add credentials or private data.
4. Verify at least two signals: the result URL, `Search Results` heading, selected `Keyword` chip, result row, or explicit empty/error state.
5. Read the live result rows' publication time, `Source`, title, and summary. Keep them dynamic; open a result with `$globenewswire-release` only when the user wants detail.
6. For more results, follow the visible `Next Page` link and re-verify the new page. Do not guess `page`, `load/more`, or page-size parameters when a visible link is available.

## Categories, organizations, and tags

For category pages, verify the category heading, the current result list, the visible topic tiles, and any `Next Page` link. The observed Energy page used `/news/energy` and exposed Alternative Energy, Oil Gas and Coal, and Chemicals subcategories; other categories are listed in the site reference.

For organization results, use the visible source link from a release row. The page exposes a live organization filter chip and historical/current release rows. Treat the organization name as a public attribution, not as independent proof of the issuer's claims.

For tag results, use the exact visible tag link from a release detail page. Preserve an empty result or malformed route as observed; do not silently broaden the tag query.

## Search controls and limits

The newsroom/search UI showed `Industry`, `Subject`, `Tag`, `Language`, and `More Filters` buttons, plus an `Everything` scope control. Their labels were confirmed, but this exploration's click path timed out before their option lists and result changes could be verified. On a future task, use the live control, then confirm the selected state or changed results before relying on it.

`Articles per page` and a `Next Page` control can appear on result pages. Treat page size, counts, ordering, release dates, and availability as live query results. Use [data-model.md](../../sites/globenewswire/references/data-model.md) for field semantics.

## Safety and authentication

- Keep the workflow read-only. Do not follow, share, subscribe, publish, register, purchase, or submit external forms during discovery.
- Do not click `Follow`, reader-account actions, or any irreversible confirmation as part of a search.
- If the current session is not visibly authenticated, complete public search only. If protected search or reader features are requested, finish the public pass, ask the user to sign in manually in the same in-app browser tab, then re-check the public search in the authenticated variant before exploring safe protected branches.
- Stop at CAPTCHA, security interstitial, or ambiguous external authentication; never bypass it.

## Drift maintenance

Before acting, compare the live search field, labels, route, filters, result state, and pagination with this procedure. If a stable route or control differs, adapt only as far as the current UI makes safe and clear, record the old/new behavior and evidence source, update this skill or its site reference, and re-run the safe search plus the skill validator. Do not write current result values, counts, rankings, or release titles into this skill.

## References

- [site-map.md](../../sites/globenewswire/references/site-map.md) — verified routes, category labels, search evidence, and coverage gaps.
- [data-model.md](../../sites/globenewswire/references/data-model.md) — release, organization, taxonomy, query, tag, and feed relationships.
- [first-party-guidance.md](../../sites/globenewswire/references/first-party-guidance.md) — site terminology, publisher-claim boundaries, and authentication limits.
