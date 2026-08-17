# Threads personal pages map

This reference describes stable routes and UI concepts observed in authenticated Threads. It intentionally excludes current posts, counts, rankings, and account-specific items.

| Surface | Observed route | Stable UI concepts | Status |
| --- | --- | --- | --- |
| Activity | `/activity` | Heading `動態`; `全部` filter; category menu for all, following, replies, mentions, quotes, reposts | UI-verified |
| Activity category | `/activity/<type>` | Selected category changes the route and list state | `回覆` UI-verified at `/activity/replies`; other result lists not separately verified |
| Following feed | `/following/` | Heading `追蹤中`; composer entry; feed cards with author/topic/time/media/action labels | UI-verified |
| Saved | `/saved/` | Heading `已儲存`; saved post cards or a loading/empty state | UI-verified after waiting for cards to load |
| Ephemeral posts | `/ghost_posts/` | Heading `限時貼文`; post card; remaining-lifetime label | UI-verified |

## Safe interpretation

Activity filters describe notification/event categories, while following and saved are content collections. `限時貼文` is a separate time-limited surface. Do not assume that a visible action button has been activated, and do not infer retention or ranking rules from the UI.

## Not established

The exact event taxonomy, notification ordering, saved-item persistence rules, ephemeral-post expiration behavior, and empty-state conditions were not fully established. Recheck the current UI when a task depends on any of those details.
