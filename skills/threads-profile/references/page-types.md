# Threads Profile Page Types

## Header

The observed public profile header can include:

- display name and username
- bio
- one or more external links
- follower count and recent views
- `追蹤` and `發送訊息` controls
- the profile activity tabs

Read only the fields needed for the current task. These values can change and may be permission-scoped.

## Activity tabs

| Label | Route | What to inspect |
| --- | --- | --- |
| `串文` | `/@<username>` | Posts authored by the profile |
| `回覆` | `/@<username>/replies` | Reply activity, including `正在回覆` context |
| `影音內容` | `/@<username>/media` | Posts containing image, video, audio, or music |
| `轉發` | `/@<username>/reposts` | Content reposted by the profile, with original author context |

## Profile-to-post routing

Public post cards expose the author and a time link to ` /@<username>/post/<post-id>`. Topic links can open search results. Media links can open ` /@<username>/post/<post-id>/media`. Verify each href in the current DOM before using it.

## Unconfirmed author search

The profile page exposed `搜尋<username>的貼文` with `/search?from_author=<username>`. A click in the observed session did not leave the profile page, so future agents must verify the current UI transition and should fall back to the profile tabs if it remains inert.
