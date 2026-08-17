---
name: x-home-feed
description: Read X/Twitter home timelines in the Codex in-app browser. Use whenever the user asks to inspect the For You, Following, custom list, or community feed on X, summarize visible posts, or verify the current home timeline. Never publish or interact as part of feed reading.
---

# X Home Feed

## Purpose and entry point

Use this skill for read-only work on `https://x.com/home`. Start from the current X tab when possible and read [the site map](../../sites/x/references/site-map.md) for the timeline taxonomy.

## Procedure

1. Open `/home` only if the current tab is not already on it, then inspect the selected timeline tab and the visible composer state.
2. Recognize the current timeline from the visible tabs: `為你推薦`, `正在跟隨`, or a user-specific list/community label.
3. Switch to the requested visible timeline tab and wait for the feed to settle.
4. Verify the selected tab, `你的首頁時間軸` or equivalent heading, and at least one visible post card or loading/empty state.
5. Read only the requested posts. For a specific post, use its visible time link and hand off to `$x-post`.
6. Report the selected timeline, current route, retrieval time, and the evidence used. Do not preserve live posts, recommendations, ads, or counts in references.

## Safety boundaries

The home page contains a composer labelled `貼文文字` with media, GIF, image generation, poll, emoji, scheduling, location, disclosure, and `發佈` controls. Do not type, upload, schedule, or publish while reading a feed. Likes, reposts, bookmarks, replies, follows, shares, and account-menu actions are also out of scope unless separately requested.

## Verification and freshness

After switching timelines, verify at least two of: current URL, selected tab, timeline heading, first post author/time, changed post cards, or empty/loading state. Feed ordering, recommendations, ads, and counters are personalized and dynamic; fetch them again for every task.

## Drift maintenance

Compare the current home tabs, composer controls, permissions, and feed heading with this procedure. Update the owning skill or X reference only for stable, clearly verified changes, then rerun the read-only timeline flow and `quick_validate.py`. Do not record live feed content, personal drafts, or account data.

## References

- [site-map.md](../../sites/x/references/site-map.md) — home timeline routes and tabs.
- [data-model.md](../../sites/x/references/data-model.md) — Timeline and Post semantics.
