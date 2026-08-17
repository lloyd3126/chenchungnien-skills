---
name: nlpi-digital-resources
description: Explain and route National Library of Public Information digital resources through the Codex in-app browser. Use when the user asks about the digital-resource portal, ebook platform, one-pass eligibility, resource categories, or course-application entry points; do not log in or submit an application.
---

# 國資圖數位資源

## Purpose and entry point

Use only the Codex in-app browser. Start from the visible `數位資源介紹` link or `https://www.nlpi.edu.tw/StaticPage/resources-intro`. Read [first-party-guidance.md](../../sites/nlpi/references/first-party-guidance.md) and [site-map.md](../../sites/nlpi/references/site-map.md) when routing is unclear.

## Procedure

1. Open the first-party introduction and verify its heading and current URL.
2. Read the visible description of resource categories and eligibility. Keep current counts, platform availability, and login requirements dynamic.
3. Use the page's visible sub-navigation to distinguish:
   - `數位資源介紹` — categories, general usage and platform links;
   - `數位資源一證通` — one-pass guidance;
   - `數位資源課程申請` — course application entry point.
4. Explain the handoff by naming the visible target, such as `ers.nlpi.edu.tw` for the public-library digital resource portal or `ebook.nlpi.edu.tw` for ebooks. Do not open a new tab or enter credentials during ordinary explanation.
5. If the user explicitly wants to use an external platform, first verify the current visible link and then treat that platform as a separate site with its own session and confirmation boundaries.

## Safety and freshness

- Holding an NLPI physical or digital library card is described as an eligibility condition for the resource portal; confirm current wording on the first-party page.
- Reader categories can have different ebook login paths, including partner-library one-pass cases. Do not invent or generalize credentials.
- Do not click external login, registration, application submission, download, or checkout actions as part of discovery.

## Drift maintenance

Compare the current introduction page, tabs, categories, eligibility text, and external links with this skill. If a stable route or service definition changes, safely verify it, update this skill or the linked reference with evidence and date, and run `quick_validate.py`. Never store passwords, tokens, private records, or live platform counts.

## References

- [first-party-guidance.md](../../sites/nlpi/references/first-party-guidance.md) — current page semantics and eligibility caveats.
- [site-map.md](../../sites/nlpi/references/site-map.md) — digital collection and cross-site routes.
