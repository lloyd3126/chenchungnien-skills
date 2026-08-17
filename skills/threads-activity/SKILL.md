---
name: threads-activity
description: Inspect authenticated Threads activity filters, following feed, saved posts, and ephemeral posts through the Codex in-app browser. Use when the user asks about notifications, activity categories, followed content, saved content, or Threads limited-time posts.
---

# Threads Activity

## Purpose and entry points

Use this skill for read-only inspection of authenticated personal surfaces. The stable entry points are `/activity`, `/following/`, `/saved/`, and `/ghost_posts/`. Load [personal-pages.md](references/personal-pages.md) for the page map.

Confirm that the current Threads page is visibly authenticated before opening these routes. If it is not, stop at public exploration and ask the user to sign in manually before protected exploration. Do not rely on route names alone as proof of access.

## Workflow

1. Confirm URL, title, heading, and loading state for the selected surface.
2. On `動態`, open the `全部` filter and read the visible categories: `全部`, `追蹤`, `回覆`, `提及`, `引用`, and `轉發`.
3. Select the requested activity category and verify the route and selected filter. For example, selecting `回覆` was UI-verified at `/activity/replies`.
4. On `追蹤中`, read the feed cards and their author, topic, time, media, and available action labels without activating an action.
5. On `已儲存`, wait for the page to settle and distinguish loaded saved cards from skeletons or an empty state. Never save or unsave a post.
6. On `限時貼文`, read the visible post and remaining-lifetime label without opening or changing its actions.
7. Report only stable structure and the state observed during the run. Treat notifications, post content, and counts as dynamic account data.

## Verification and safety

- Opening pages and changing the activity filter are safe read-only actions.
- Do not like, follow, repost, quote, share, save, unsave, delete, publish, or reply.
- If a surface is still loading, record `loading` rather than treating missing cards as empty.
- A route that renders a shell is not proof that all content or controls are available; verify the heading and content state.

## Drift maintenance

If Threads changes a route, filter label, or page heading, recheck the visible UI and update [personal-pages.md](references/personal-pages.md) and the Threads site map. Keep current activity items and post content out of this skill.

## References

- [Personal pages map](references/personal-pages.md)
- [Threads site map](../../sites/threads/references/site-map.md)
- [Threads data model](../../sites/threads/references/data-model.md)
- [Threads operating guidance](../../sites/threads/AGENTS.md)
