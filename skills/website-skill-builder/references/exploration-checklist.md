# Website Exploration Checklist

Use this as a working note during exploration. Keep exact labels from the site and mark uncertainty explicitly.

## Sitemap inventory

| Source label / route | Type | Child sitemap or URL patterns | Stable categories discovered | Access status | Evidence source | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |
|  | visible site map / sitemap index / XML / robots metadata |  |  | discovered / visually accessible / downloaded / locally parsed / UI-verified / client-blocked / blocked / unavailable / invalid / no sitemap discovered | current-tab visual / current-tab DOM / download UI + local artifact / user-provided screenshot / control error |  |

Check the current page for a visible site-map or first-party inventory, then check same-origin `/robots.txt` early because it often exposes Sitemap URLs. A Sitemap or robots entry is optional, not guaranteed. Track discovery, retrieval, parsing, and UI verification separately: a discovered URL is not proof that its contents can be fetched. Use only the user's already-visible active tab; do not create temporary tabs. If a compressed Sitemap downloads, confirm the browser download and inspect the local artifact before marking its XML as locally parsed. Keep all discovered routes marked `sitemap—unverified` until a corresponding UI or page is opened in that same tab. Do not copy current URL inventories, tokenized URLs, or private branches into final skills. Treat `ERR_BLOCKED_BY_CLIENT`, a timeout, or an empty automation body as inconclusive until the current tab has been visually checked and the visible link/navigation path retried; do not record “no parseable content” from that signal alone. Use `client-blocked` when the control path remains blocked after the visual retry, and reserve `invalid` for content that was actually retrieved and confirmed invalid. Preserve earlier successful visual/download evidence when a later retry fails.

## Coverage

| Area / entry point | Visible label | Destination or state | Discovery source | Child areas found | Status | Next branch |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | UI / sitemap—unverified / robots—candidate / first-party docs |  | unexplored |  |

Status values: `explored`, `partial`, `protected—awaiting user choice`, `blocked`, `unsafe`, `not applicable`.

## Robots-derived route clues

| User-agent | Directive | Path or Sitemap URL | Candidate area / path family | Access status | Evidence source | UI verification / follow-up |
| --- | --- | --- | --- | --- | --- | --- |
|  | Allow / Disallow / Sitemap |  |  | discovered / client-blocked / blocked / unavailable | current-tab visual / user-provided screenshot / control error |  |

Treat these as structural clues only. `Disallow` does not prove that a page is private, nonexistent, or inaccessible to a user; verify any safe candidate through the visible site UI. Do not copy a large current robots inventory into final skills.

## Evidence integrity

- [ ] The existing active tab was identified before navigation
- [ ] Each target was actually opened in the active tab before interpreting its status
- [ ] A screenshot was captured after the target navigation attempt, including when the API returned an error
- [ ] A same-tab retry was performed when the target was not visible after an API error
- [ ] No temporary tab, popup, or alternate browser was used
- [ ] A screenshot was captured after each navigation error
- [ ] User-provided screenshots are labeled as user-provided evidence
- [ ] `client-blocked` was not converted into `invalid`, `unavailable`, or `no sitemap discovered`
- [ ] Later control errors did not overwrite earlier successful visual/download evidence

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

Use this section whenever an authenticated session is visibly confirmed. If the user is already signed in, no separate protected-exploration question is required; manual sign-in remains user-only when authentication is not already present.

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
- [ ] Same-origin `/robots.txt` checked early; absence recorded as a valid result
- [ ] Same-origin standard sitemap candidates considered only in the in-app browser
- [ ] Compressed Sitemap downloads checked and parsed when produced
- [ ] Sitemap index/child maps sampled without exhaustive crawling
- [ ] Sitemap-only candidates clearly separated from UI-verified features
- [ ] Robots-derived route clues recorded separately from Sitemap retrieval status
- [ ] `Disallow` and `Allow` rules not treated as user-facing permissions
- [ ] Navbar reviewed again
- [ ] Sidebar and collapsed menus reviewed again
- [ ] Homepage and primary dashboard reviewed again
- [ ] Footer and account/settings menus reviewed again
- [ ] Important tabs and dropdown options checked
- [ ] Major safe interactions tested rather than merely observed
- [ ] First-party help and methodology links reviewed
- [ ] Every remaining gap is labeled as blocked, unsafe, unavailable, or out of scope
