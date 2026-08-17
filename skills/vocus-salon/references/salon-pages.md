# vocus Public Salon Pages

## Salon homepage

For `/salon/<slug-or-id>`, verify the salon heading, logo/cover context when visible, member/content summary, public/private access state, join entry, Top 5, room sections, and at least one article or post link. Preserve the salon slug when opening a child content page.

## Rooms

Room links may appear inside the salon navigation or room sections. The observed route pattern is `/salon/<slug>/room/<room>`, but it was only partially rechecked. Confirm the live room heading, selected navigation, access state, content list, and any `查看更多` control before relying on the route.

## Creator-to-salon handoff

Creator profiles can expose salon cards and `前往沙龍`. That link is useful for navigation, but it does not establish the viewer's membership, the creator's ownership, or the salon's access policy. Verify those independently on the salon page.

## Dynamic fields

Member/content counts, Top 5 ordering, feed cards, join state, room availability, and access labels change over time or by session. Store route patterns and evidence requirements, not current values.
