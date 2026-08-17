# Facebook UI Data Model

This is an operational model inferred from visible Facebook UI. It describes durable field roles, not current values.

## Entities

### FeedPost

- `author`: profile or page that owns the post.
- `published_at`: relative or absolute time shown by the post header.
- `audience`: visible audience label such as friends or everyone.
- `body` and `media`: text, image, video, Reel or story links.
- `actions`: reaction, comment, share/send and post-menu controls. These are side-effecting when submitted.
- Related entities: `Comment`, `Profile`, `Story`, `Media`.

### SearchRequest and SearchResult

- `query`: text from the shared `搜尋 Facebook` combobox.
- `scope`: all, people, Reel, Marketplace, pages, groups or events.
- `filters`: observed post recency, viewed-state, publish date, source and tagged location controls; option sets must be reread from the live UI.
- `results`: feed posts or entity cards, each linking to a detail surface.
- Route relationship: `SearchRequest → /search/<scope>/ → SearchResult → entity detail`.

### MarketplaceListing

- `listing_id`: opaque identifier in the item route; use only for the current lookup.
- `title`, `price`, `availability`, `condition`, `description`, `location` and approximate location display.
- `seller`: seller identity shown by the detail page; do not copy it into durable notes unless the user explicitly needs it.
- `actions`: send message, save, share, more options and map/location view. Treat message, save, share and any purchase flow as external side effects.
- Route relationship: `Marketplace search → Listing card → MarketplaceListing detail`.

### GameCard

- `game_id`: route segment for the game page.
- `title`, `description`, `category`, `player_count` and `play_link`.
- Route relationship: `Games hub → featured card → game surface`. The observed hub was not used to launch a game.

### AccountControl

- `profile`: current profile and optional switchable profiles.
- `settings`: settings/privacy, language, privacy checkup, privacy center, activity log and content preferences.
- `support`: help, scam prevention, account status, support inbox and report problem.
- These fields are personalized and permission-sensitive. Use them for routing only; do not persist current profile names or records.

## Retrieval rules

- Fetch current values from the visible page at task time. Do not calculate or infer prices, rankings, counts, inventory, audience, recommendation order or player counts from old pages.
- Confirm entity identity from the heading, route pattern and at least one relevant field before reporting details.
- Keep public search results separate from authenticated/personalized results. A visible result in a signed-in session does not prove public accessibility.
