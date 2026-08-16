# Website Exploration Checklist

Use this as a working note during exploration. Keep exact labels from the site and mark uncertainty explicitly.

## Sitemap inventory

| Source label / route | Type | Child sitemap or URL patterns | Stable categories discovered | Access status | Follow-up |
| --- | --- | --- | --- | --- | --- |
|  | visible site map / sitemap index / XML / robots metadata |  |  | available / partial / blocked / unavailable |  |

Use the visible site-map link first. A same-origin `/sitemap.xml` or `/robots.txt` check is only a fallback and must be performed in the Codex in-app browser. Keep sitemap-derived routes marked `sitemap—unverified` until a corresponding UI or page is opened. Do not copy current URL inventories, tokenized URLs, or private branches into final skills.

## Coverage

| Area / entry point | Visible label | Destination or state | Discovery source | Child areas found | Status | Next branch |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | UI / sitemap—unverified / first-party docs |  | unexplored |  |

Status values: `explored`, `partial`, `protected—awaiting user choice`, `blocked`, `unsafe`, `not applicable`.

## Page taxonomy

| Page type | Representative route | Purpose | Sections / controls | Safe actions | Outgoing links | Variants |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Interaction evidence

| Feature | How started | Inputs / options | Observed result | Limits / errors | Verification |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Include search bars, keyword fields, autocomplete, filter panels, dropdowns, multi-selects, checkboxes, radio buttons, toggles, date/number ranges, sort controls, reset/clear controls, and query builders. Do not mark a feature as tested when only its label, button, or field was observed.

## First-party explanations

| Term / feature | Source page or tooltip | Site definition | Durable rule or limitation | Reference target |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Entity model

| Entity | Identifier | Important fields | Related entities | View / search page | Analysis / edit page |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Workflow and routing

| User need | Entry point | Path | Result | Freshness | Verification / next step |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Authenticated re-exploration

Use this section after the user has explicitly approved protected exploration and manually signed in.

| Previously explored area | Public state | Authenticated state | Difference | Rechecked / blocked | Evidence |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

- [ ] Every public top-level entry point revisited after login
- [ ] Every public page type revisited after login
- [ ] Every major public interaction rechecked after login
- [ ] Every public search, filter, dropdown, and form control rechecked after login
- [ ] Navigation, fields, data scope, permissions, and actions compared
- [ ] Newly visible authenticated branches explored safely
- [ ] Authenticated second-pass audit completed

## Second-pass audit

- [ ] Visible sitemap or site-map entry checked first
- [ ] Same-origin standard sitemap/robots fallback considered only in the in-app browser
- [ ] Sitemap index/child maps sampled without exhaustive crawling
- [ ] Sitemap-only candidates clearly separated from UI-verified features
- [ ] Navbar reviewed again
- [ ] Sidebar and collapsed menus reviewed again
- [ ] Homepage and primary dashboard reviewed again
- [ ] Footer and account/settings menus reviewed again
- [ ] Important tabs and dropdown options checked
- [ ] Major safe interactions tested rather than merely observed
- [ ] First-party help and methodology links reviewed
- [ ] Every remaining gap is labeled as blocked, unsafe, unavailable, or out of scope
