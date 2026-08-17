---
name: fred-release-calendar
description: Browse FRED economic releases and release dates through the Codex in-app browser. Use when the user asks for a FRED release, publication schedule, release calendar, next release, release catalog, date filter, or release-date comparison.
---

# FRED Release Calendar

## Purpose and entry point

Use the FRED UI to locate a release, inspect its current calendar window, filter by release, and verify the displayed dates and times. Start at `https://fred.stlouisfed.org/releases/calendar` or reach it from the homepage menu's `Release Calendar` link.

Read [references/release-controls.md](references/release-controls.md) for the observed calendar controls. Read [../../sites/fred/references/site-map.md](../../sites/fred/references/site-map.md) for route coverage and [../../sites/fred/references/first-party-guidance.md](../../sites/fred/references/first-party-guidance.md) for provenance and first-party documentation.

## Procedure

1. Open the release calendar in the existing Codex in-app browser tab and verify the `Release Calendar` heading and current date range.
2. Use the first visible release combobox to select the requested release. Verify the selected option; do not treat a label typed into a control as a completed filter.
3. Use `‹`, `›`, or `today` to move the calendar when the requested period is not visible. Confirm the heading and the day/date headers after each change.
4. Read the release rows, release names, links and times. FRED displays release times in U.S. Central Time; report that timezone when it matters.
5. Use the visible `Date` or `Name` sort link when ordering matters, and verify the active sort state and resulting rows.
6. If the user wants the release catalog rather than dates, open `/releases`; use visible pagination and choose a release detail link. Re-check the detail page because individual release structures were not deeply explored in this pass.
7. If the selected release has no dates in the displayed window, report the visible empty state and change the date range only when the user's request permits it. Do not infer that the release is discontinued.

## Safety and freshness

- Use only the Codex in-app browser and the existing active FRED tab. Do not switch to external browsers, web search, API calls, CLI fetching, cookies, local storage or session inspection.
- After each navigation or filter action, verify the same tab's URL, heading, selected option, period, result rows or empty state. If automation reports a client block, timeout or empty result, capture the same tab visually and retry once before classifying it.
- Release schedules are dynamic and publisher-controlled. Re-fetch the calendar for every task and do not store current dates, counts, release lists or live availability in this skill.
- Read-only browsing is the default. Do not subscribe, create alerts, edit an account, or submit forms.

## Drift maintenance

- Compare the current visible controls, release options, calendar period, sort labels, timezone note and first-party explanations with this procedure before acting.
- If a stable route, control or workflow changes, complete the smallest safe adaptation, then update this skill or its reference with old/new behavior, evidence and date.
- Keep public and authenticated variants separate; never record passwords, cookies, tokens, private data or one-off release results.
- Re-run the affected safe workflow and `quick_validate.py` after editing. Report broad or ambiguous changes instead of guessing.

## References

- [references/release-controls.md](references/release-controls.md) — release catalog and calendar controls.
- [../../sites/fred/references/site-map.md](../../sites/fred/references/site-map.md) — confirmed routes and page taxonomy.
- [../../sites/fred/references/data-model.md](../../sites/fred/references/data-model.md) — release/source/series relationships.
- [../../sites/fred/references/first-party-guidance.md](../../sites/fred/references/first-party-guidance.md) — first-party documentation and provenance.
