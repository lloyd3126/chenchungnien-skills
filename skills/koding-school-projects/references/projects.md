# 作品、工作室與帳號 reference

## Verified authenticated routes

| Need | Route pattern | Verified structure | Boundary |
| --- | --- | --- | --- |
| My projects | `/my/projects` | `專案名稱` GET search, `回收桶`, language tabs, project cards | Do not edit or delete. |
| Deleted projects | `/my/projects/deleted` | Entry link visible from project list | Not opened; treat as a destructive/recovery branch. |
| Project detail | `/projects/<project-id>` | Project-card destination | Not opened during this pass; do not infer editor controls. |
| My studios | `/my/studios` | `新增工作室`, `進入` links | Creation is a side effect. |
| Studio detail | `/studios/<studio-id>` | Title, `我的工作室`, project cards, `新增作品`, `移除` | Do not add or remove. |
| Resume/profile | `/resume/<student-id>` | Skills, projects, pagination such as `?page=2` | Personal data; keep current values out of docs. |
| Inbox | `/my/messages` and `/my/messages/<message-id>` | Message list and detail route pattern | Message bodies not explored for privacy. |
| Account settings | `/my/account` | Account/email/birthday/nickname/location/biography fields | Primary form posts to `/my/account`; never submit during discovery. |

The current account menu did not expose `訂閱紀錄` or `訂單記錄`; those financial branches remain unconfirmed and intentionally unexplored. Do not guess their routes.

## Project list

The project list exposes language tabs including `Web`, `JavaScript`, `Python`, `App Inventor`, `Scratch 3`, `Aibotgame`, and `Lua` when available. The `專案名稱` field belongs to a GET form whose action is `/my/projects`; its semantic query is `q`, while `utf8` and `button` are form transport parameters. Use the visible search button, then verify the URL and visible card state. A search can reduce the visible tab set to languages with matching results. If the page does not visibly change, do not guess whether filtering succeeded.

The list also exposes `回收桶` and may expose public collection links. Current project names, ids, authors, language counts, and card order are dynamic and user-specific.

## Studio page

`/studios/<studio-id>` is a collection page. The verified representative page showed a heading, a return link to `我的工作室`, project cards with `/projects/<project-id>` links, `新增作品`, and `移除`. Treat `移除` as destructive and `新增作品` as a creation flow. Inspect a project only when the user identifies the project and read-only access is appropriate.

## Account and privacy

The account form labels were `帳號`, `Email`, `生日`, `頭像`, `履歷背景圖`, `暱稱`, `居住地區`, and `簡介`. The form method is POST to `/my/account`. These fields can contain sensitive personal data; do not read, repeat, fill, upload, or submit them unless the user requests the exact operation and confirms immediately before the browser action.

The resume page currently reports a missing zh-TW controller translation in its document title. Treat this as a UI defect, not as a reason to invent a different route.

## Verification checklist

1. Confirm signed-in navigation and page heading.
2. For a list, verify the route, visible search/tabs, and current card state.
3. For a studio, verify title, project-card route, and whether the requested action is read-only.
4. For profile/account/inbox, minimize exposure and report only the requested field or route.
