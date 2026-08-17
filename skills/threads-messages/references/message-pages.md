# Threads message pages map

This reference records stable authenticated Threads message-page structure observed in the in-app browser. It excludes conversation identifiers, previews, timestamps, and message bodies.

| Surface | Observed route | Stable UI concepts | Status |
| --- | --- | --- | --- |
| Inbox | `/messages/` or `/messages` | Heading `訊息`; search field; inbox and request navigation; conversation list when loaded | UI-verified; onboarding dialog may appear |
| Message requests | `/messages/requests` | Heading `陌生訊息`; `返回`; `新訊息`; `隱藏`; `管理設定`; explanatory copy about people the user does not follow | UI-verified; list content can be loading |
| Hidden messages | `/messages/hidden` | Hidden-message collection entry | Link UI-verified; content not separately explored |
| New message | `/messages/new/` | New-message heading and navigation back to inbox/requests | UI-verified as an entry route; recipient/composer readiness not established |
| Message settings | `/settings/messages` | Message-management settings entry | Link UI-verified; settings content not explored |

## Onboarding state

The inbox may show a modal stating that web Direct messages are available, with a `繼續` button. This is a product onboarding state, not proof that message sending is ready. Record it and stop unless the user explicitly asks to continue.

## Safety boundary

This map supports navigation and read-only inspection only. Sending, accepting, hiding, deleting, forwarding, composing, and changing message settings require a separate explicit request and confirmation, and are outside the default workflow.
