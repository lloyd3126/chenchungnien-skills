# data.gov.tw data model

## Core entities

### Dataset

The stable identifier is the numeric `nid` in `/dataset/<nid>`. A dataset detail page exposes:

- title and description
- major field notes; bold fields are marked as data-standard fields when present
- one or more resource distributions, or an API service definition
- provider agency and provider contact
- update frequency
- license and pricing model
- publication date, ingestion/publication method, and metadata last-modified time
- service category, keywords, related URLs, notes, related datasets, applications, rating, usage counters, and comments/login state

The displayed values are dynamic. Re-fetch the detail page for every task and report the observed metadata time when freshness matters.

### File distribution

A file-backed dataset has a resource section such as `CSV`, a resource name/description, and a download URL. The URL may point to an agency domain rather than `data.gov.tw`. Do not infer that the file is reachable, current, UTF-8, or schema-compliant from the format label alone. Verify the resource link when the user asks for a download or data-content task.

The detail page may also expose `檢視資料`; treat it as a safe UI entry point, but verify the resulting state before claiming that an inline preview is available.

### API-service distribution

An API-service dataset uses `資料提供屬性: API服務` and exposes:

- an API address or an API documentation URL, often on an external platform
- a short operation description
- an API說明文件 link
- provider, frequency, license, cost, category, keywords, related URL and notes

The note may require registration and an API key on the external platform. Never register, create keys, or enter credentials during read-only exploration. Treat the API endpoint and its current availability as separate facts.

## DCAT vocabulary modal

The detail page's `DCAT 詞彙` button opens a modal with a Turtle representation. Durable concepts observed in the modal include:

- `dcat:Dataset` and `dcat:CatalogRecord`
- title, description, identifier, issued date and modified time
- publisher and contact point
- accrual/update frequency, theme, keyword, landing page and related datasets
- distribution, download URL and encoding format
- license and offer/price metadata

Use this modal to clarify field semantics or export structure. Do not copy live identifiers, contact details, dates, scores or resource URLs into reusable instructions.

## Relationships

`Dataset → distribution/resource` supports file download or API access. `Dataset → provider` links to a provider-filtered search. `Dataset → service category` links to a category-filtered search. `Dataset → related datasets` links to other `/dataset/<nid>` pages. `Dataset → applications` links to `/applications?name=<dataset title>`. Comments require a login link when the current session is not authenticated.

## Freshness and validation

For a live answer, verify the current page heading and URL, the current metadata-modified time, provider, field notes, resource/API URL, and the resulting page or external resource state. Never use search-card counts or the current dataset page's view/download counters as a proxy for data freshness.
