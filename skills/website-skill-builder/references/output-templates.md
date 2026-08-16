# Output Templates

Use these as outlines, not boilerplate to copy blindly. Keep only facts confirmed from the target site.

## AGENTS.md outline

```markdown
# [Website name]

## Scope

- Site purpose and the kinds of tasks it supports.
- What this workspace's site-specific guidance covers.

## Sitemap-assisted inventory

- [Visible sitemap or same-origin metadata route]: [what was available and how it was reached].
- [Stable URL patterns or categories]: [discovered inventory, marked sitemap-unverified until UI-confirmed].
- [Routes intentionally not followed]: [private, tokenized, dynamic, or excessive branches].

## Global routing

- [Need or entity] → [site capability] → [navigation path] → [skill/reference].

## Navigation

- [Exact label]: [purpose and destination].

## Operating rules

- Use the site UI and first-party definitions as the source of truth.
- Use a sitemap as an inventory accelerator, not as evidence that a feature, permission, or workflow works; re-check sitemap-derived candidates through the UI.
- Prefer a visible site-map link. If absent, only consider same-origin `/sitemap.xml` or `/robots.txt` through the Codex in-app browser; do not use web search, CLI fetching, APIs, or external browsers.
- Explore public functionality first. After the public pass, ask whether the user wants protected functionality explored; only then ask them to sign in manually in the same Codex in-app browser tab and wait for confirmation.
- Treat the authenticated state as a separate site variant and re-check previously explored paths before documenting login-dependent behavior.
- Re-test search bars, filters, dropdowns, and other form controls in both states; document differences in options, validation, query state, results, and reset behavior.
- Re-fetch dynamic values; do not rely on values in these instructions.
- Preserve session state and stop at irreversible confirmation boundaries.
- When live UI differs from the documented procedure, use the current UI safely, record the exact verified mismatch, and update the owning site artifact when the change is stable and clear; never write dynamic values or speculative behavior.

## Skill selection

- Use `$[skill-name]` when [trigger and capability].

## Validation and freshness

- [How to confirm a result].
- [How to determine whether data needs refreshing].

## Known limits

- [Permission, access, or feature limitation].
```

## Skill outline

```markdown
---
name: [lowercase-hyphenated-name]
description: [What it does and when to use it, including concrete triggers.]
---

# [Skill title]

## Purpose and entry point

[Capability, starting page, and required access.]

## Procedure

1. [Navigate to the confirmed entry point.]
2. [Use the confirmed controls and inputs.]
3. [Read the relevant fields or result.]
4. [Follow the verification and freshness rule.]

## Page and field semantics

- [Confirmed field or control]: [meaning and constraints].

## Safety and limits

- [Read-only default, confirmation boundary, permission, or failure state.]

## Drift maintenance

- Compare the current visible UI and first-party definitions with this procedure before acting.
- If a stable route, label, control, page structure, permission, or workflow changes, update the owning `AGENTS.md`, skill, or reference in the authorized workspace after safely verifying it.
- Keep public and authenticated variants separate; do not record passwords, cookies, tokens, private data, or dynamic result values.
- Re-run the affected safe workflow and the skill validator after editing. Report broad or ambiguous changes instead of guessing.

## References

- [references/file.md](references/file.md) — [when to load it].
```

## Reference-file rules

- Keep detailed schemas, terminology, methodology, and page variants in references when they are not needed for every invocation.
- Keep sitemap-derived route inventories out of final skills unless they are stable route patterns; document how to refresh the inventory instead.
- Link every reference directly from the skill that needs it; avoid deep chains of references.
- Do not store current search results, live rankings, or user-specific values as durable knowledge.
