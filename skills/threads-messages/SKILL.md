---
name: threads-messages
description: Inspect authenticated Threads Direct message inbox, requests, hidden messages, and new-message entry points through the Codex in-app browser. Use when the user asks to review message navigation or message-page structure; never send or modify messages as part of this read-only skill.
---

# Threads Messages

## Purpose and entry points

Use this skill to inspect the authenticated Threads Direct message surfaces without changing message state. Start at `/messages/` or the visible `訊息` navigation entry, and load [message-pages.md](references/message-pages.md) for stable routes and boundaries.

Confirm the page is Threads, the URL is on `threads.com`, the page has loaded, and authentication is visibly present. If not, stop after public exploration and ask the user to sign in manually before protected inspection.

## Workflow

1. Open the inbox and record the URL, title, heading, search field, navigation links, onboarding dialog, and loading state.
2. If the `網頁版現已推出 Direct 訊息` onboarding dialog appears, record it as an onboarding state and do not click `繼續` unless the user explicitly asks.
3. Open `陌生訊息` at `/messages/requests` and verify its heading, `返回`, `新訊息`, `隱藏`, and `管理設定` links. Read the visible explanation that messages from people the user does not follow appear there.
4. Open `/messages/hidden` or `/settings/messages` only when requested and only read visible structure.
5. Open `/messages/new/` only to inspect its entry state. If recipients or the composer are loading, record that state and stop.
6. Report message-page structure and loading/onboarding state, never message bodies or account-specific previews unless the user explicitly requests a safe read-only summary.

## Verification and safety

- Navigating between message pages is read-only.
- Never type a recipient, message, search query, or reply in this skill. Never send, accept, hide, delete, forward, or change message settings.
- Do not click `繼續` in an onboarding dialog unless explicitly requested.
- Treat conversation previews and timestamps as dynamic private data; do not write them into stable references.
- A visible new-message route is not proof that a composer is ready; verify the actual field state.

## Drift maintenance

If Threads changes message routes, labels, onboarding text, or request controls, recheck the visible UI and update [message-pages.md](references/message-pages.md) and the site map. Keep conversation identifiers and message content out of the skill.

## References

- [Message pages map](references/message-pages.md)
- [Threads site map](../../sites/threads/references/site-map.md)
- [Threads data model](../../sites/threads/references/data-model.md)
- [Threads operating guidance](../../sites/threads/AGENTS.md)
