---
name: reuters-article-research
description: Read and verify a Reuters article through the Codex in-app browser, including title, authors, timestamps, Summary, visible body, media, tags, source context, and access state. Use when the user provides or asks for a Reuters article.
---

# Reuters Article Research

## Purpose and entry point

Open a Reuters article from a visible section, search result, author/topic page, or Sitemap candidate in the current in-app browser tab. Read [../../sites/reuters/AGENTS.md](../../sites/reuters/AGENTS.md), [data-model.md](../../sites/reuters/references/data-model.md), and [first-party-guidance.md](../../sites/reuters/references/first-party-guidance.md).

## Procedure

1. Open the user-provided or UI-derived Reuters article URL in the same tab. Verify the page title, article heading, URL, and visible access state.
2. Capture the article title, author links, published/updated time, visible section/category, and any `Exclusive`, `ANALYSIS`, or sponsored label.
3. Read the selected `Summary` tab when present, then distinguish the visible body from advertisements, newsletter CTAs, video, gallery, related links, and gated content.
4. Record durable source context: the article's `Our Standards` / `The Thomson Reuters Trust Principles` link, visible corrections or source notes, and any first-party data disclosure link. Do not copy dynamic live values into references.
5. For media, capture caption, item position, and licensing context only when requested. Verify `Expand gallery in a modal window` or forward/back controls from the current article before using them.
6. Report what was visible, what was gated or unavailable, and the observation time. Do not infer missing paragraphs or author details.

## Page semantics

- Article identity is the title plus the current route, not only a slug or Sitemap entry.
- Authors are linked entities under `/authors/<slug>/`; tags and suggested topics link back to category or topic pages.
- `Summary` is a read-only article view; the body may contain inline links, image galleries, videos, ads, and newsletter prompts.
- `Save article` can write to an account. `Share article`, social share buttons, `Email article`, and `Copy link` can transmit or represent information. They are not part of a read-only research workflow.

## Safety and limits

Stop at login, registration, paywall, CAPTCHA, or subscription gates. Do not bypass access controls. Do not click Save, Share, Follow, Email, Subscribe, Purchase Licensing Rights, or other side-effect controls unless the user explicitly asks and the required action-time confirmation is available.

## Drift maintenance

Compare the live article layout, labels, access state, first-party explanations, and media controls before acting. If a stable mismatch is safely verified, patch this skill or the owning reference, re-run the read-only article workflow and validator, and preserve public/authenticated variants separately. Keep current article text, counts, prices, rankings, and personal data out of the repository.

## References

- [site-map.md](../../sites/reuters/references/site-map.md) — article route families and entry points.
- [data-model.md](../../sites/reuters/references/data-model.md) — article, author, topic, and media relationships.
- [form-controls.md](../../sites/reuters/references/form-controls.md) — Summary, gallery, and safety-boundary controls.
- [first-party-guidance.md](../../sites/reuters/references/first-party-guidance.md) — source, content classification, and access limits.
