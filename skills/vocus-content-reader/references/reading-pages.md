# vocus Reading Pages

## Article checklist

For `/article/<id>`, capture only fields needed for the request:

- title/heading and content type;
- author and linked creator;
- salon and room context;
- published and updated timestamps;
- visible read time;
- `目錄` headings and in-page anchors, when present;
- body, tags, access marker, AI/sponsor labels, and visible comment state.

Use the article body for substance and the metadata for provenance. Do not treat reaction counts or recommendation cards as stable article facts.

## Post checklist

For `/post/<id>`, distinguish the post author, heading, body/media, dates, read time, reactions, comment sort (`熱門`, `最新`, `最舊`), and visible replies. A comment textbox is an interaction boundary, not a reading requirement.

## Creator checklist

For `/user/@<handle>` or `/user/<id>`, verify the heading, bio/social links, follower state, sponsor entry, salon cards, `前往沙龍`, selected `發佈內容`/`我的成就` tab, and visible feed controls. Follower counts, follow state, and feed contents are personalized and must be re-read.

## Evidence labels

- `UI-verified`: URL and visible page structure were confirmed with a successful same-tab screenshot.
- `DOM-verified`: URL and semantic content were confirmed, but screenshot control was incomplete or timed out.
- `partial`: only a route or partial state was confirmed; do not summarize missing content.
