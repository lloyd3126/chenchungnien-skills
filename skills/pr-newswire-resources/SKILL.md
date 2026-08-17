---
name: pr-newswire-resources
description: Research public PR Newswire products, Amplify modules, resource articles, RSS guidance, and contact/account boundaries through the Codex in-app browser. Use for product or first-party resource explanations without submitting forms.
---

# PR Newswire Resources

## Purpose and entry points

Use this skill for stable product/resource research and first-party terminology. Start from the visible `Products`, `Resources`, or footer `RSS` link in the current PR Newswire tab. Read [the site package](../../sites/pr-newswire/AGENTS.md), [the route map](../../sites/pr-newswire/references/site-map.md), and [first-party guidance](../../sites/pr-newswire/references/first-party-guidance.md).

## Products and Amplify

1. Open `Products` → `Explore Our Platform` for `/amplify-platform/`, or `All Products` for `/products/all-products/`.
2. On Amplify, route by the visible lifecycle labels `PLAN`, `CREATE`, `DISTRIBUTE`, and `REPORT`. The page also explains Multichannel Amplification and exposes a public FAQ and Request a Demo form.
3. On All Products, use the visible category tabs `All`, `Marketing`, `Public Relations`, `IR & Compliance`, and `Agency`, then open a product card whose title matches the user's intent.
4. Verify the page title/heading, visible module description, and any first-party FAQ or related route. Treat network sizes, award claims, performance percentages, and product promises as current marketing claims; quote/attribute them to the page and refresh them for every task.

`/products/overview/` redirected to `/amplify-platform/` during exploration. Re-check the current redirect before relying on that alias.

## Resource library

1. Open `Resources` → `/resources/`.
2. Choose a visible section tab: `Articles`, `Tip Sheets`, `White Papers`, `Webinars`, `Case Studies`, `Toolkits`, or `News Trends`.
3. Verify the list heading, resource type/title, page-size state, and pagination. The overview also exposes a category selector with `All Categories`, `Target Influencers`, `Create Campaigns`, `Distribute Content`, `Monitor Measure`, and `Success Stories`.
4. Open the visible resource card/detail route when the user asks for the content itself. Verify the title, body, author/source context, and internal links. Downloads (for example `Download Now`) are inbound actions but still require checking the current UI and file type before using them.

If an asynchronous category selector does not complete under browser control, use the visible resource-section route instead of retrying blindly; record the control as unconfirmed for that session.

## RSS and syndication

Open footer `RSS` → `/rss/`. The page lists visible channels such as all releases and topical feeds, explains that RSS contains headlines, summaries, and links, and provides raw-feed buttons. Click a raw-feed control only when the user requests the current feed and the resulting same-tab/current-tab state can be verified. Do not guess feed URLs.

## Public forms and login boundaries

The Amplify demo form, Contact form, and Send a Release account form include contact/organization fields, marketing or contractual language, reCAPTCHA, and disabled submit buttons until completion. Inspecting their structure is within scope; do not enter personal data, check consent boxes, solve CAPTCHA, or submit. `Client Login` opens a Cision username screen; do not enter credentials or OTPs. Protected product behavior is unconfirmed unless the user later signs in manually in the same tab.

## Verification and freshness

Use the current visible page and first-party FAQ/guidance as the source of truth. Verify at least the current URL plus heading and one module/resource/definition. Re-fetch resource lists, pagination, product claims, and feed channels; never store live content, counts, rankings, or marketing claims as fixed route facts.

## Drift maintenance

Before acting, compare current product/resource tabs, route redirects, labels, controls, form boundaries, and first-party definitions with this skill. If a stable discrepancy is directly verified, patch the owning skill/reference and run the safe representative workflow plus `quick_validate.py`. Preserve public/authenticated variants and report broad or unsafe changes rather than guessing.

## References

- [site-map.md](../../sites/pr-newswire/references/site-map.md) — products, resources, RSS, form, and login routes.
- [data-model.md](../../sites/pr-newswire/references/data-model.md) — resource, product/module, and feed entities.
- [first-party-guidance.md](../../sites/pr-newswire/references/first-party-guidance.md) — AEO/GEO, Multichannel Amplification, RSS, attribution, and safety context.
- [interaction-guide.md](../../sites/pr-newswire/references/interaction-guide.md) — safe controls and evidence rules.
