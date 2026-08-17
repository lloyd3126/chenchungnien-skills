# PR Newswire public data model

## Entities

### News release

The release detail page is the canonical entity view. Stable fields exposed in the UI are:

- title and URL slug/identifier (`/news-releases/<slug>-<id>.html`)
- publication timestamp, shown with an ET timezone label
- source/provider organization link
- optional logo or media asset
- summary or key-point bullets
- article body, headings, citations, and source line
- ticker/financial modal links when present
- related releases from the same source
- `Explore` links to taxonomy pages and similar topics
- share controls (outward-action boundary; do not click by default)

Treat title, timestamp, body, provider, media, and related releases as live values. Reopen the release on every task.

### Organization/source

An organization is reached from `News provided by`, `More Releases From This Source`, or search results. The public route is `/news/<organization-slug>/`. It exposes a chronological release index with the same date/time jump, page-size, and card pattern as category lists.

### News taxonomy

The top-level taxonomy is presented through expandable buttons such as `News in Focus`, `Business & Money`, `Science & Tech`, `Lifestyle & Health`, `Policy & Public Interest`, and `People & Culture`. Child categories are visible links, for example `Health`, `Health Insurance`, `Health Care & Hospitals`, and `Medical Pharmaceuticals`. Prefer the current visible child link; do not infer slugs.

### Search result

The search overlay accepts a keyword and routes to a result entity with a type tab: `All`, `News`, `Organizations`, `Products`, or `Resources`. Search results preserve `keyword=<query>` and may expose result-specific pagination/page-size controls. A result row can link to a release, organization, product, or resource.

### Resource

Resources have a section/type (Articles, Tip Sheets, White Papers, Webinars, Case Studies, Toolkits, or News Trends), title, detail URL, body, internal links, and sometimes an author block or download link. Current resource listings are paginated and dynamic.

### Product/module

Product cards and the Amplify overview describe product/module capabilities. The observed platform model is `Plan → Create → Distribute → Report`, with Multichannel Amplification as a cross-channel extension. All Products also exposes marketing, public relations, IR/compliance, and agency filters.

### RSS channel

The RSS page models a feed as a channel (all releases or a visible category such as Health or Business Technology) with a raw-feed control. The page explains that feeds contain headlines, summaries, and links. Obtain the current feed URL through the visible RSS control; do not guess it.

## Relationships

`Search query` → `News release | Organization | Product | Resource`.

`News taxonomy` → `Category overview` → `Category list` → `News release`.

`Organization` → `Release list` → `News release`.

`News release` → `Provider organization`, `related releases`, `taxonomy`, and optional `media`.

`Resource section` → `Resource list` → `Resource detail`.

`Product catalog` → `Product/module detail` → public demo/account form or protected Amplify workspace.
