---
name: website-skill-builder
description: Systematically inventory and explore an accessible website through the Codex in-app browser, first attempting a same-site sitemap inventory and then validating public functionality before exploring protected functionality when the current session is visibly authenticated or after explicit user consent and manual sign-in. After authentication, re-explore previously covered areas because navigation, data, permissions, and controls may differ. Map its information architecture, safely test its interactions, understand its data model and workflows, and create maintainable AGENTS.md and agent skills for future operation. Use when a user asks to reverse-engineer a website for repeated AI-agent use specifically in the built-in browser, build website-specific operating guidance, or turn in-app browser exploration into reusable skills.
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

### Active-tab invariant and evidence provenance

- Bind to exactly the already-visible active Codex in-app browser tab supplied by the user. Do not create, open, or switch to a temporary tab, popup, window, browser session, or alternate browser for discovery. Do not treat a tab created by a helper or `open` call as the user's current tab.
- Capture the current tab visually before the first navigation, after each navigation, and after every navigation error. All retries must target that same tab. If an attempted navigation reports an error but the tab remains on the previous page, the previous page's screenshot is the only evidence about what is currently visible.
- Track the evidence source for every important claim: `current-tab visual`, `current-tab DOM/interaction`, `browser download UI plus local artifact`, `user-provided screenshot`, or `automation/control error`. A control error is evidence only that that attempt failed; it is never evidence about the target response body.
- A user-provided screenshot can establish what the user saw at that time, but it does not prove that the current tab was reopened. Report it as user-provided evidence and do not write “我已在目前分頁重新確認” unless a new screenshot of the same current tab confirms it.
- Require current-tab visual evidence before marking a resource or route `visually accessible` or `UI-verified`. DOM text from a temporary tab, a successful `goto`, HTTP metadata, or a tool error cannot substitute for that evidence.
- Never overwrite or downgrade earlier visual/download/parse evidence merely because a later attempt gets `ERR_BLOCKED_BY_CLIENT`, timeout, or an empty automation result. Append the later attempt as `client-blocked` with its evidence source and keep the earlier result intact.

### Mandatory open-then-inspect protocol

For every target route, resource, representative Sitemap URL, or page that the user asks to inspect:

1. Record the current URL and visually inspect the existing active tab.
2. Actually navigate/open the target in that same built-in-browser tab. A navigation API call is only an attempt; it is not proof that the target was opened.
3. Immediately capture a screenshot of that same tab, regardless of whether the navigation API reports success, timeout, `ERR_BLOCKED_BY_CLIENT`, or another error.
4. If the screenshot still shows the previous page, a blank state, or an error state, perform one more same-tab normal browser navigation: follow the visible first-party link when available; otherwise retry the target navigation in the same tab. Capture another screenshot after the retry.
5. Only then classify the result as visually accessible, invalid, unavailable, or client-blocked. If the target never appears in a screenshot of the active tab, say “本輪未在目前分頁視覺打開成功” and do not say that the target had no content.

Never stop at step 2 because a navigation API returned `ERR_BLOCKED_BY_CLIENT`. The required next action is step 3 visual inspection, followed by step 4 retry when the target is not visible.

Authentication is conditional: do not substitute another browser or source, and do not continue into protected areas on assumptions. If the current visible page clearly confirms an authenticated session, no separate permission question is required; treat it as an authenticated site variant and proceed with safe protected exploration after the public pass. If authentication is not visible, finish the public exploration and its second-pass audit first, then ask whether the user wants protected functionality explored. Only if the user agrees should you ask them to sign in manually in the same Codex in-app browser tab and wait for confirmation. If the user declines, report those branches as not explored.

## Required workflow

### 1. Discover sitemap and alternate inventories

Before broad navigation, look for the site's own sitemap or another first-party URL inventory through the Codex in-app browser. A sitemap is common but optional; absence is a valid outcome.

1. Visually inspect the current page for a `Sitemap`, `Site map`, `サイトマップ`, footer link, help entry, documentation link, RSS/Atom feed, or equivalent. Prefer an exact same-site link exposed by the UI.
2. Check the same-origin `/robots.txt` early. It often contains one or more `Sitemap:` lines, but it may contain none. Also record `User-agent`, `Allow`, and `Disallow` patterns as `robots—candidate` route clues, grouped by path family. These clues can suggest account, content, admin, search, or other areas, but they are not a feature map or an access-control result.
3. For every Sitemap URL exposed by the visible page or `robots.txt`, use the mandatory open-then-inspect protocol in the same already-visible in-app browser tab; do not open a temporary tab. If XML renders, inspect its root type and sample entries. If a compressed file such as `.xml.gz` downloads instead of rendering, confirm the download completed in that same browser session, inspect the downloaded artifact through the available local-file path, decompress it, and sample the XML. Do not fetch a replacement with `curl`, a CLI, an API, or an external browser unless the user explicitly changes the operating boundary.
   - Treat `ERR_BLOCKED_BY_CLIENT`, `client block`, a `goto` timeout, an empty automation response, or a parser that receives no body as an inconclusive browser-control result—not as proof that the resource is empty, unavailable, or unparsable. First visually inspect the current in-app tab, then retry through the exact visible Sitemap/robots link or the browser's normal address/navigation flow. If the tab visibly renders text/XML or shows a completed download, trust that visual evidence and continue with the appropriate inspection or local parsing step even when an automation read is empty.
   - Only classify a resource as `invalid` after content was visibly or otherwise reliably retrieved and confirmed to be empty, HTML, malformed, or not the expected Sitemap format. If the browser still cannot expose the resource after the visual retry, use `client-blocked` and state that the browser control path did not provide content; never report “沒有可解析內容” as if the resource itself had been proven empty. Keep the Sitemap or robots entry as discovered evidence and continue normal UI exploration.
4. If no Sitemap was found, consider only a small set of conventional same-origin candidates such as `/sitemap.xml`, `/sitemap_index.xml`, and `/sitemap.xml.gz`, plus any first-party HTML sitemap, help, documentation, or feed entry discovered through the UI. Do not guess or crawl an exhaustive list of paths.
5. Record the discovery source, whether it is an index, compressed XML, URL list, feed, or HTML page, child sitemap names, stable URL patterns, labels or categories, language variants, and apparent private or dynamic branches. For a large inventory, inspect the index and representative entries; do not open every URL or copy the full URL list into the repository.
6. Treat every discovered route as a candidate, not proof that a feature exists, is public, is current, or behaves as the URL suggests. Mark it `sitemap—unverified` until the corresponding UI or page is opened and confirmed. A Sitemap URL itself must receive a separate retrieval status; finding the URL is not the same as retrieving its contents.
7. Add Sitemap candidates and robots-derived route clues to the coverage checklist, deduplicate route patterns, group them into page types, and return to the current visible page. The inventory accelerates discovery; actual labels, controls, transitions, permissions, and results must still be verified through the site UI.

Use these Sitemap retrieval statuses in the checklist and completion report:

- `discovered`: listed in visible UI, `robots.txt`, documentation, or another first-party inventory; contents not retrieved.
- `visually accessible`: XML or an inventory page rendered in the user's current in-app browser tab and confirmed visually.
- `downloaded`: the browser completed a download, but the artifact has not been parsed.
- `locally parsed`: a downloaded artifact was decompressed or read and its XML/text structure validated.
- `UI-verified`: representative URLs were reopened in the user's current in-app browser tab and confirmed visually through the website UI.
- `client-blocked`: the in-app browser control path reported a client block, timeout, or empty automation result and visual retry did not expose the resource; this does not establish that the resource itself is empty or nonexistent.
- `blocked`: visual evidence, a permission boundary, or a server response prevented retrieval, such as HTTP 403. Record whether the block came from the browser client, the site/server, login, or an explicit safety boundary.
- `unavailable`: visible navigation showed a missing route or network failure without evidence of a policy block; do not use this for an automation-only timeout before visual retry.
- `invalid`: content was actually retrieved and confirmed to be empty, HTML, malformed, or otherwise not the expected Sitemap format.
- `no sitemap discovered`: the explored first-party inventory paths contained no Sitemap entry, and that is a valid outcome.

Do not follow private, tokenized, or unsafe URLs merely because an inventory lists them. Do not treat HTTP 200, a browser tab, a `Disallow` rule, or a robots entry alone as proof that a page or Sitemap is available. `Disallow` is crawler guidance, not a user-facing permission result. If retrieval is blocked, record the evidence and the layer that blocked it, do not attempt policy workarounds, and continue with normal UI exploration. A browser-control error is not a substitute for visual inspection: never turn an empty tool result into a claim that the page had no parseable content, and never claim that the current tab was reopened when the error came from a temporary or unbound tab.

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

At the end of this public pass, ask whether the user wants the recorded protected areas explored only when the current visible session is not already authenticated. Do not ask at the first login wall. If an authenticated session is already visible, continue into safe protected branches without a separate permission prompt. Otherwise, if the user agrees, pause for manual sign-in in the same in-app browser tab, then explore only the protected branches that are now available. If the user declines, keep them documented as protected and unconfirmed.

### 10. Re-explore in the authenticated variant (conditional)

Treat the authenticated site as a separate site variant, not as a simple continuation. When the current visible session is authenticated—whether it was already active or the user just signed in—revisit every top-level entry point, page type, workflow, and major safe interaction recorded during the public pass—even when it appeared fully understood before authentication.

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

For Sitemap and route claims, include the evidence source. Use `current-tab visual` only when the user's existing tab was visibly inspected; use `user-provided screenshot` for screenshots supplied by the user; use `browser download UI plus local artifact` for downloaded and parsed files; and report `automation/control error` separately. Never describe a control error as proof that the target had no content.

Use the templates in [references/output-templates.md](references/output-templates.md) when they improve consistency.
