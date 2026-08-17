---
name: tw-gov-data-dataset
description: Inspect a data.gov.tw dataset page in the Codex in-app browser, including metadata fields, file resources, API-service definitions, DCAT vocabulary, related datasets, provider links, and freshness checks. Use when the user has a dataset ID, result link, or asks for download/API/resource details.
---

# Taiwan Government Dataset Detail

## Purpose and entry point

Start from a visible search result or navigate the same in-app browser tab to `https://data.gov.tw/dataset/<nid>`. Do not infer detail fields from a search card alone. Use the current page and first-party explanations as the source of truth.

## Procedure

1. Open the candidate dataset and verify the URL `/dataset/<nid>`, the heading, and the description.
2. Read the durable metadata fields: major field notes, provider, provider contact, update frequency, license, pricing, publication date, ingestion method, metadata last-modified time, category, provision property, keywords, related URLs, notes, and related datasets.
3. For a file-backed resource, record the visible format label, resource name/description, and current download URL. If the user needs the file, follow the browser download and verification procedure; do not assume an external agency URL works just because it is displayed.
4. For an API service, record the API address, operation description, API documentation link, provider, update frequency, and current note about registration or API keys. Never register or create a key as part of inspection.
5. Use `DCAT 詞彙` when the user needs semantic or export-field interpretation. Inspect the modal's Turtle text and map Dataset, CatalogRecord, Distribution, publisher, contact, frequency, license, keyword, landing page, download URL, and encoding to the page fields. Do not save live identifiers, contacts, timestamps, or resource URLs as reusable instructions.
6. Use related dataset, provider, category, and applications links for the next read-only step. Comments may expose a login link; stop at that boundary unless the user separately authorizes a supported manual sign-in flow.

## Verification and freshness

- For a live answer, re-open the detail page and verify heading, current metadata-modified time, provider, field notes, resource/API URL, and the resulting state.
- Keep file distributions and API-service distributions separate. A free dataset page does not prove that an external API is unauthenticated or that the resource is currently reachable.
- Treat ratings, view/download counts, related lists, application lists, contact details, dates, and resource URLs as dynamic values.

## Safety and limits

- Do not download or open an external resource unless the user needs that artifact or validation step.
- Do not submit ratings, comments, forms, login credentials, API registrations, or API keys.
- Do not call `檢視資料` successful merely because the button exists; verify the resulting UI. In the sampled page, the click did not expose a distinct visible preview state.

## Drift maintenance

- Compare the current visible page, route, labels, metadata fields, permissions, and DCAT explanation with this procedure before acting.
- If the file/API detail structure changes, record the page type, old behavior, observed behavior, evidence source, and date; patch this skill or its reference only when the difference is stable and directly supported.
- Re-run one file-detail and one API-detail read-only workflow plus `quick_validate.py` after editing. Report broad or unverified changes instead of guessing.

## References

- [data-model.md](../../sites/data-gov-tw/references/data-model.md) — dataset entities, file/API distributions, DCAT semantics, relationships, and freshness rules.
- [site-map.md](../../sites/data-gov-tw/references/site-map.md) — confirmed entry points and unconfirmed external branches.
