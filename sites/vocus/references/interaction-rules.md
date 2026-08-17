# vocus Interaction and Verification Rules

## Search

1. Open the header search dialog through the visible search icon.
2. Fill only a non-sensitive query and wait for suggestions.
3. Suggestions are grouped as `內容`, `創作者`, `沙龍`, and `關鍵字`; choose the requested scope or `查看更多`.
4. Verify both the query value and the URL scope. For content, verify the selected content type and sort state in the URL when present.
5. Re-fetch every result for the current task; counts, order, timestamps and recommendations are not durable.

Observed content controls:

- Type: `全部內容`, `文章`, `貼文`.
- Sort: `發佈日期由新至舊`, `發佈日期由舊至新`, `愛心數由高至低`, `留言數由高至低`, `瀏覽數由高至低`.
- Example verified query state: `type=article`; like sorting used `sort=likeCount&order=desc`.

## Content reading

- Article pages expose an optional `目錄` with in-page heading anchors, author, salon/room, publish/update dates, read time, body, tags, comments and sponsor entry.
- Post pages expose author, body/media, publish/update dates, read time, reactions, comment ordering and a comment textbox.
- Creator pages expose profile identity, follower state, sponsor entry, participating salon cards, `發佈內容`／`我的成就`, content type and chronological controls.

## Public and authenticated variants

- Home feed tabs and public search must be rechecked after login because results and extra entries can be personalized.
- A visibly authenticated session may be used to inspect Studio read-only pages. If authentication is not visible, stop before protected routes and ask the user to sign in manually in the same tab.
- Do not copy private member names, personal data, sponsor URLs, identity/payment fields or current dashboard values into reusable guidance.

## Side-effect boundaries

Treat these as read-only observation only unless the user explicitly asks and any action-time confirmation requirements are satisfied: follow/unfollow, join/leave salon, like, comment, share, save, sponsor, purchase, create/edit/publish/schedule/delete content, import/upload, save Studio settings, add rooms/members/plans, change ads/revenue status, submit identity/payment data and request withdrawal.
