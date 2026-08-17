---
name: wos-researcher-profile
description: "Use the Codex in-app browser to inspect an authenticated Web of Science Researcher Profile, profile metrics, Documents/Peer Review tabs, My Web of Science records, or General/Profile/Communications/Homepage Settings without changing account state. Trigger whenever the user asks about their Web of Science profile, metrics dashboard, peer-review preferences, notifications, homepage widgets, or researcher settings."
---

# Web of Science Researcher Profile

## Purpose and access

Use this skill for safe, read-only inspection of the signed-in Researcher Profile variant. Start from the user's existing Web of Science tab and confirm authentication from visible UI such as the account menu, `My Web of Science`, or profile controls. If authentication is not visibly confirmed, do not enter credentials; finish any public lookup with `$wos-researcher-search` and ask the user to sign in manually in the same tab before protected work.

Read [the site map](../../sites/webofscience/references/site-map.md), [the data model](../../sites/webofscience/references/data-model.md), and [the interaction rules](../../sites/webofscience/references/interaction-rules.md) before using an unfamiliar profile route.

## Profile and metrics workflow

1. Inspect the current tab, then open `MENU` → `My Web of Science` → `Profile` → `My researcher profile`. Verify the Author Profile heading and current route; do not copy the account's name or identifier into durable notes.
2. Read stable sections as needed: Identifiers, Profile Completeness Score, Metrics, Profile summary, Documents, and Peer Review. Treat counts, names, organizations, metrics, and publication rows as live data.
3. Switch `Documents` and `Peer Review` tabs only for reading. Wait for loading to finish and distinguish an explicit empty state such as `No peer reviews available for this author` from a still-visible progress indicator.
4. Open `Metrics dashboard panel` for a read-only overlay when the task needs metrics. Verify the Core Collection context and current metric labels. `Open Filters` exposed `Author Position` with `All` selected in the observed session; do not infer global unavailability from an empty or premium state.
5. Use visible `My records` labels to route future tasks to Publications, Grants, Peer reviews, Editor records, Editorial board memberships, or Pending records. These child pages were not opened in the exploration, so verify the current route and controls before operating them.

## Settings workflow

1. Open the account menu and choose `Settings`, then verify the settings route and page heading.
2. Use the visible settings navigation:
   - `General Settings`: language, default search page, starting database, advanced-search starting database, number of rows, and default result sorting.
   - `Profile Settings`: `Edit profile`, `Publication preferences`, `Peer review preferences`, and an `ORCID syncing` tab. The first three tabs were inspected; ORCID syncing remained unconfirmed because the active viewport could not safely click it.
   - `Communications Settings`: profile events, reviewed-article notifications, profile reminders/tips, and authored-publication updates. The page shows the account email; never quote or save it.
   - `Homepage Settings`: widget on/off switches, move-up/move-down controls, `View Homepage`, and `Save`.
3. Read controls without changing them. Do not toggle a switch, reorder a widget, edit profile fields, select a file, click Save, or follow `Account Settings` when it only exposes `javascript:void(0)` unless the user explicitly requests that state change and confirms at the action boundary.

## Page and field semantics

- Profile Settings `Edit profile` includes profile photo, first/middle/last name, published-name display, primary organization, organization history, Cancel, and Save.
- Publication preferences includes automatic updates for Core Collection/Preprint records and Grant records, plus a link to communications settings.
- Peer review preferences includes publisher-invited review display settings, author-review display, grant-review display, reviewer availability, reviewer-interest links, and automatic addition of partnered-journal/funder reviews.
- General Settings values are account defaults, not current search-result filters. Re-read the selected values for the current account.
- Homepage widget order and visibility are account state. A visible Save button means local inspection is not enough to claim a change.

## Safety and privacy

- Stop before `Edit`, `Select file`, any `ADD` control, `Claim my record`, `Submit a correction`, `Share`, `Save`, setting toggles, `View Homepage` if it changes state, `End session`, and `End session and log out`.
- Never record passwords, cookies, email addresses, account names, private profile content, ResearcherIDs/ORCIDs, live counts, or one-off records. If the user asks to operate on their own private value, ask only for the minimum needed and confirm immediately before any transmission.
- Do not follow external product, publisher, or help links unless the user asks for that extension of scope.

## Drift maintenance

- Before acting, compare the current visible authenticated variant, routes, labels, controls, permissions, and first-party explanations with this procedure.
- If the authenticated UI differs from the documented public or prior state, re-check the affected page and keep public/authenticated variants separate. Record old behavior, observed behavior, route, evidence source, and date without recording private values.
- Patch the owning `AGENTS.md`, skill, or reference only for a stable, clearly verified change. Re-run the affected safe profile/settings read and the skill validator; report broad or ambiguous changes as maintenance gaps.
