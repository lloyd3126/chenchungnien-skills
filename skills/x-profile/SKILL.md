---
name: x-profile
description: Read and navigate public X profiles in the Codex in-app browser. Use whenever the user asks to inspect an X/Twitter account, its posts, replies, reposts, media/videos, profile metadata, following/follower entry points, or profile-scoped search. Keep the workflow read-only and verify the current profile and selected tab.
---

# X Profile

## Purpose and entry point

Use this skill for read-only inspection of `https://x.com/<handle>`. Start from the currently open Codex in-app browser tab when it is already on X; otherwise navigate to the exact handle supplied by the user. Read [the site map](../../sites/x/references/site-map.md) when routing is unclear and [the interaction rules](../../sites/x/references/interaction-rules.md) for profile search or tab verification.

## Procedure

1. Inspect the visible URL, page title, profile heading, handle, selected tab, and account state.
2. Confirm that the visible profile matches the requested handle. Do not identify an account from display name or avatar alone.
3. For posts, replies, reposts, or media, click the visible profile tab and wait for the timeline or empty state to settle.
4. Verify the selected tab, profile-specific heading, and at least one result card or the empty-state message.
5. For a specific post, use its visible time link or card link and hand off to `$x-post`; do not invent post IDs.
6. For current counts, dates, bio, media, following, or followers, read them from the current page and report the route and retrieval time. Never copy those dynamic values into the skill or references.

## Profile page semantics

- Header fields may include display name, verified marker, handle, bio, location, joined date, following/followers links, profile photo, and header photo.
- The profile timeline currently exposes `貼文`, `回覆`, `轉發`, and `媒體`; after activation, the last tab may render as `影片`. Use the label visible in the current DOM.
- `回覆` can include the original author’s post together with the target account’s reply. `轉發` is identified by a `你已轉發` marker.
- A profile search button can open `/explore` with a prefilled `from:<handle>` query. The restriction was not reliable in the tested `from:lloyd3126 AI` case; verify every returned author before claiming the results are profile-only.

## Safe boundaries

- Safe by default: navigation, tab switching, opening public profiles, opening visible post links, and reading public content.
- Do not edit the profile, follow/unfollow, like, repost, bookmark, post, reply, send a message, or upload media during exploration. These actions change state or transmit content and require an explicit user request plus action-time confirmation where applicable.
- Do not read notifications, private messages, browsing history, settings, drafts, or account data merely because the current session is signed in.

## Verification and freshness

After each meaningful interaction, verify at least two of: current URL, title or heading, selected tab, handle, first result author/title, or empty state. Refresh the profile when current values matter. Counts, result order, post text, and media availability are dynamic.

## Drift maintenance

Compare the live profile UI, labels, routes, permissions, and first-party explanations with this procedure before acting. If a stable change is clearly verified, update this skill or its owning X reference, then re-run the affected read-only flow and `quick_validate.py`. Keep public and authenticated variants separate and never record passwords, cookies, tokens, private data, or live result values.

## References

- [site-map.md](../../sites/x/references/site-map.md) — X routes and page taxonomy.
- [data-model.md](../../sites/x/references/data-model.md) — Profile, Post, Repost, Media, and related entities.
- [interaction-rules.md](../../sites/x/references/interaction-rules.md) — tab, profile-search, and freshness rules.
