# Agent usability tests

These scenarios were simulated using only `sites/pr-newswire/AGENTS.md`, the three site skills, and the linked references. They are routing tests, not stored live-result tests.

| Request shape | Skill route | Expected page/entity/control | Safe stopping boundary | Outcome |
| --- | --- | --- | --- | --- |
| “Search PR Newswire for a named release or organization.” | `$pr-newswire-search` | Search overlay → exact keyword → Enter → `All`/`News`/`Organizations` tab; verify URL, heading, keyword, and result. | Stop before sharing, forms, login, or external partner links. | Pass: skill names the placeholder, submit behavior, result tabs, and verification signals. |
| “Find Health releases from a date/hour and open one.” | `$pr-newswire-news` | Visible news category → category list → date `MM/dd/yyyy`, hour selector, `Go`; verify selected time and first card → release detail. | Read title/provider/time/body only; do not click share controls. | Pass: skill distinguishes overview/list/detail and dynamic freshness. |
| “Show all public releases from an organization.” | `$pr-newswire-news` | Release detail `News provided by` or search organization result → `/news/<organization-slug>/` → organization list controls and cards. | Stop before external company links or outward actions. | Pass: data model identifies organization and release relationships. |
| “Explain PR Newswire Amplify, its modules, and current RSS options.” | `$pr-newswire-resources` | `/amplify-platform/` → Plan/Create/Distribute/Report and FAQ; `/rss/` → visible channel/raw-feed controls. | Attribute marketing claims; do not submit demo/contact/account forms. | Pass: skill gives both routes and defines freshness/attribution. |
| “Contact PR Newswire or start sending a release.” | `$pr-newswire-resources` plus site safety rules | Public form route with contact/organization fields, terms, reCAPTCHA, disabled submit. | Do not enter personal data, accept terms, solve CAPTCHA, or submit. | Pass: generated artifacts identify this as an inspection-only boundary. |
| “Use the client portal.” | Site package protected branch | `Client Login` → Cision username screen. | Ask for manual sign-in only if protected work is required; never enter credentials. | Pass: authenticated variant is explicitly unconfirmed. |

The tests confirm that future agents can choose a skill, identify the page/entity/control, verify a current result, and stop at the correct safety boundary without rediscovering the site.
