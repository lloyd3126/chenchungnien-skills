---
name: website-skill-builder
description: Systematically inventory and explore an accessible website through the Codex in-app browser, first attempting a same-site sitemap inventory and then validating public functionality before optionally exploring protected functionality after explicit user consent and manual sign-in. After login, re-explore previously covered areas because navigation, data, permissions, and controls may differ. Map its information architecture, safely test its interactions, understand its data model and workflows, and create maintainable AGENTS.md and agent skills for future operation. Use when a user asks to reverse-engineer a website for repeated AI-agent use specifically in the built-in browser, build website-specific operating guidance, or turn in-app browser exploration into reusable skills.
---

# Website Skill Builder

## Purpose

Treat the target website as an unfamiliar long-term tool. Explore it through its actual interface, distinguish stable operating knowledge from changing data, and package the result so another agent can use the site without starting over.

Do not optimize for one immediate question. First understand the website itself; then create only the durable routing, workflows, references, and skills that the evidence supports.

## Inputs and operating boundary

1. Identify the target website, the active Codex in-app browser tab or URL, the target workspace, and the authorized output location.
2. Use only the Codex in-app browser and its browser-control capability. If the in-app browser is unavailable, report the blocker and stop; do not switch to Chrome, Edge, an external browser, Computer Use, standalone Playwright, an API, a CLI, or web search.
3. Inspect and operate the site through the in-app browser UI. Prefer the site UI and its own documentation over assumptions.
4. Detect authentication gates before exploring protected areas. If the site requires login, record the protected branch and continue exploring all other accessible public areas; do not pause the current exploration at the first login wall.
5. Preserve the user's existing login and session. Never request, enter, or expose passwords, API keys, cookies, or unrelated personal data. Never bypass or programmatically inspect authentication.
6. Read-only exploration is the default. Treat submit, save, publish, delete, purchase, send, import, and other irreversible confirmation actions as approval boundaries.

Follow the `browser:control-in-app-browser` skill for in-app browser setup, tab handling, interaction, and evidence capture. Use the currently visible site state as the source of truth; URLs and page text alone are not enough to establish that an interaction works. Never inspect cookies, local storage, profiles, passwords, or session stores.

Authentication is a staged gate: do not substitute another browser or source, and do not continue into protected areas on assumptions. Finish the public exploration and its second-pass audit first. Then ask the user whether they want protected functionality explored. Only if the user agrees, ask them to sign in manually in the same Codex in-app browser tab and wait for confirmation; after confirmation, re-check the visible page state and resume from the recorded protected branch. If the user declines, report those branches as not explored.

## Required workflow

### 1. Try a sitemap-first inventory

Before broad navigation, attempt to obtain the website's own sitemap or site-map index through the Codex in-app browser.

1. Inspect the current page for a visible `Sitemap`, `Site map`, `サイトマップ`, footer link, help entry, or equivalent. Prefer opening the exact same-site link exposed by the UI.
2. If no visible sitemap exists, optionally try a conventional same-origin metadata route such as `/sitemap.xml` or `/robots.txt` in the in-app browser only. Do not use web search, `curl`, a CLI, an API, or an external browser. If the route is unavailable or blocked, record that and continue with UI exploration.
3. Record the sitemap source, whether it is an index or URL list, child sitemap names, URL patterns, labels or categories, language variants, and any apparent private or dynamic branches. For a large sitemap, inspect the index and representative child entries; do not open every URL.
4. Treat sitemap entries as discovery candidates, not proof that a feature exists, is public, is current, or behaves as the URL suggests. Mark their source as `sitemap—unverified` until the corresponding UI or page is opened and confirmed.
5. Add sitemap-derived candidates to the coverage checklist before following the site's navbar, sidebar, homepage, footer, account menus, search, and settings. Deduplicate URL patterns and group them into page types so the sitemap accelerates coverage without turning exploration into exhaustive crawling.
6. Return to the current visible page and continue with the UI. The sitemap is an inventory aid; actual labels, controls, transitions, permissions, and results must still be verified through the site interface.

Do not treat `robots.txt` as a feature map, do not follow private or tokenized URLs, and do not store current sitemap contents or large URL lists in generated skills. Preserve only stable route patterns and the retrieval path.

### 2. Establish a coverage map

Start from the current page and inspect every reasonable top-level entry point:

- navbar, sidebar, menus, dropdowns, tabs, footer navigation, dashboards, account/user menus, search, and settings
- primary calls to action and links that lead to another functional area
- help, documentation, methodology, FAQ, and about links

Maintain a coverage checklist while exploring. Record exact visible labels, destinations, discovered child areas, status (`explored`, `partial`, `blocked`, or `not applicable`), and the next unexplored branch. Use [references/exploration-checklist.md](references/exploration-checklist.md).

When a new entry point appears, add it before continuing. Do not declare coverage complete until the second-pass review in step 9.

If an entry point is blocked by login, record its exact label, route, visible explanation, and likely capability in the checklist, mark it `protected—awaiting user choice`, and continue with unrelated public branches.

### 3. Classify page types

Open representative examples rather than enumerating every content instance. Identify each distinct page type, such as list, search results, detail, dashboard, report, analysis, editor, settings, documentation, comparison, or workflow pages.

For each page type, record:

- how to enter it and what it is for
- sections, tabs, fields, tables, charts, controls, and status indicators
- safe actions and their results
- outgoing navigation and relationships to other page types
- variants that materially change the structure

### 4. Test safe interactions

For each major interaction, perform the smallest safe test and record the observed behavior:

- search, filters, sorting, pagination, tabs, dropdowns, expansion, view switching, date ranges, chart/table controls, comparison, advanced search, exports, history, and bookmarks
- form controls and query builders: search bars, keyword fields, autocomplete/typeahead, filter panels, select/dropdown/multi-select controls, checkboxes, radio buttons, toggles, date/number/price ranges, sort controls, reset/clear controls, and safe submit actions up to—but not including—an irreversible confirmation
- validation messages, empty states, loading states, permissions, limits, and error recovery

For every tested control, capture: how it starts, accepted inputs, options and defaults, state changes, result location, follow-up navigation, validation messages, reset behavior, and constraints. Use representative safe values; do not mark a feature understood merely because a button or field is visible.

### 5. Read first-party explanations

Open relevant tooltips, info icons, help pages, guides, documentation, methodology notes, definitions, and FAQ content. Prefer the website's definitions over common knowledge.

Capture only durable facts such as terminology, calculation rules, categories, scoring, algorithms, data sources, update rules, and limitations. Follow directly linked internal documentation when it is needed to understand the feature; stop when the concept is sufficiently defined.

### 6. Reconstruct the data model

Identify the site's actual entities and relationships without imposing a preconceived schema. For each important entity, record:

- name and purpose
- important fields, identifiers, statuses, timestamps, and units
- links to related entities
- pages that search, view, analyze, edit, compare, or export it
- how an agent reaches it from other entities

Separate entity structure from the current values shown on the site. Never hard-code live numbers, rankings, search results, or user-specific records into reusable instructions.

### 7. Trace natural workflows

Walk through the main read-only workflows end to end. Derive them from the site rather than assuming a standard pattern. For each workflow record:

`entry → navigation → controls and inputs → intermediate page/state → result → next actions`

Trace alternate routes when they are visible, and note prerequisites, permissions, freshness, failure states, and safe stopping points.

### 8. Build retrieval and navigation routing

Convert the exploration into abstract routing that answers:

`agent need → site capability → navigation path → page or entity → fields/controls → verification → next step`

Route by user intent and page type, not by one temporary URL. State where to re-fetch dynamic information and which first-party explanation or reference to consult.

### 9. Run a second-pass audit

Return to the navbar, sidebar, homepage, footer, main dashboard, and each major page type. Compare what is visible now with the checklist. Look specifically for:

- collapsed menus, dropdown options, important tabs, undiscovered page types, unexplained terminology, untested major controls, and documentation links
- workflows that stop before their result or verification step
- information that was observed but lacks a retrieval path
- assumptions that were not confirmed by the UI or first-party documentation

Continue exploring until the remaining gaps are explicitly blocked, unsafe to test, unavailable to the current session, or genuinely out of scope.

At the end of this public pass, ask whether the user wants the recorded protected areas explored. Do not ask at the first login wall. If the user agrees, pause for manual sign-in in the same in-app browser tab, then explore only the protected branches that are now available. If the user declines, keep them documented as protected and unconfirmed.

### 10. Re-explore after login (conditional)

Treat the authenticated site as a separate site variant, not as a simple continuation. After the user signs in and confirms, revisit every top-level entry point, page type, workflow, and major safe interaction recorded during the public pass—even when it appeared fully understood before login.

Compare and record the authenticated state for:

- navbar, sidebar, menus, dropdowns, tabs, destinations, and newly visible entry points
- page sections, fields, tables, charts, filters, exports, empty states, and result scope
- search bars and form controls, including accepted values, default selections, option lists, autocomplete behavior, validation, reset/clear behavior, and resulting query state
- entity identifiers, statuses, personalization, permissions, and available actions
- workflow steps, validation, errors, confirmation boundaries, and next actions
- first-party help, definitions, methodology, and documentation that may now be available

Mark each public area as rechecked or blocked in the authenticated state. Record differences explicitly and do not copy public observations into authenticated guidance unless they were reverified. After revisiting the public paths, explore the newly available protected branches and run a second authenticated coverage audit.

For every public search, filter, dropdown, and other form control, perform a safe representative input again after login and compare the accepted values, options, defaults, validation, resulting URL or state, result set, and reset behavior. If the authenticated state changes the form semantics or available data, document the public and authenticated variants separately.

### 11. Package the knowledge

Write to the authorized target workspace, not to this skill's own directory unless the user explicitly asks for that:

- update or create `AGENTS.md` with only cross-task site knowledge
- create one or more focused skills under `skills/<skill-name>/`
- add `agents/openai.yaml` metadata for each new skill when the repository convention supports it
- add directly linked `references/` files for detailed schemas, methodology, page maps, or variant-specific procedures

Keep `AGENTS.md` focused on site identity, global navigation, skill routing, session rules, freshness, validation, and major constraints. Put operational details in the skill that owns the workflow. Split skills by cohesive capability (for example, discovery, analysis, or account management), not by every page and not into one oversized skill.

Every generated skill must have a valid lowercase hyphenated name, frontmatter with only `name` and `description`, explicit triggers in the description, procedural instructions, entry paths, verification steps, and links to any needed references. Do not add README, changelog, installation guide, or other process documentation unless the user explicitly requests it.

When the `skill-creator` tooling is available, initialize each generated skill with its `init_skill.py`, edit the generated files, and run its `quick_validate.py`. Do not install remote packages or skills during site exploration unless the user explicitly authorizes that change and it is required for the requested output.

### 12. Perform an agent usability test

Using only the generated `AGENTS.md`, skills, and references, simulate several independent requests across different site areas. For each, verify that an agent can identify:

- the correct skill and entry point
- the correct page, entity, fields, and controls
- the safe operation sequence and stopping boundary
- how to obtain current data and verify the result

If the simulated agent would need to rediscover the site, cannot choose between skills, misreads a field, or lacks a next step, revise the artifacts and repeat the test. Report unconfirmed or inaccessible areas separately; do not present them as facts.

### 13. Define a maintenance loop for future use

Every generated site `AGENTS.md`, skill, or reference that describes an operation must tell future agents how to handle drift:

1. Before acting, compare the current visible UI, route, labels, controls, permissions, and first-party explanations with the documented procedure.
2. If they differ, treat the current UI and current first-party documentation as the source of truth. Complete the user's safe task with the smallest necessary adaptation, or stop at an unsafe/ambiguous boundary.
3. Capture the mismatch precisely: public/authenticated variant, page type, route, old documented behavior, observed behavior, verification evidence, and date. Do not record passwords, cookies, tokens, private data, or live result values.
4. In the authorized workspace, autonomously patch the owning `AGENTS.md`, skill, or reference when the change is clear, stable, and directly supported by the observed UI. Keep public and authenticated variants separate and preserve unrelated user changes.
5. Do not write dynamic prices, rankings, counts, search results, availability, or one-off content into instructions. Update the retrieval path or verification rule instead.
6. Re-run the relevant safe workflow and `quick_validate.py` after editing. If the change is broad, contradictory, or cannot be safely verified, report it as a maintenance gap instead of speculating.

Generated skills should include a short `Drift maintenance` or equivalent section so this loop remains available during ordinary future website tasks, not only during a new full exploration.

## Stable knowledge versus dynamic data

Write stable knowledge into instructions and references:

- navigation and page types
- feature purpose and control behavior
- field meanings, entity relationships, workflows, methodology, and limitations

For dynamic information, document the retrieval path instead:

- current values, search results, rankings, prices, statuses, user records, and recent updates
- the page, query, filter, date range, or refresh action required to obtain them

Always include a freshness and verification rule when a result can change.

## Completion report

Finish with a concise report covering:

1. explored scope and major site structure
2. created or updated skills and each skill's purpose
3. important references and routing decisions
4. unconfirmed, inaccessible, or intentionally untested areas
5. agent usability test scenarios and outcomes

Use the templates in [references/output-templates.md](references/output-templates.md) when they improve consistency.
