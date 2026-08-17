# 課程導覽 reference

## Verified entry points

| Need | Route pattern | Verified UI | Notes |
| --- | --- | --- | --- |
| Continue current lesson | `/` → visible `繼續上課` | Homepage card | Dynamic last-visited state; re-fetch every time. |
| Enrolled course list | `/my/courses` | `我的課程` | Authenticated; cards expose course links and dynamic progress. |
| Course search | `/my/courses` with visible `課程名稱` + `搜尋` | URL contained `q=<term>` after a safe search | Verify heading, query, and cards. |
| Course filters | `/my/courses?sort=course`, `expired=true`, `type=course`, `type=question` | Visible sort/status/type links | Preserve current query state when combining filters. |
| Course detail | `/courses/<family>/<slug>` | Course heading, duration, difficulty, prerequisites, features | May expose invite-only enrollment dialog. |
| Course discussion | `/courses/<slug>/topics` | Lesson-group list with topic counts | Counts are dynamic. |
| Lesson | `/courses/<family>/<slug>/lessons/<unit>/<chapter>` | Breadcrumb, `返回課程`, `下一章`, `儲存`, lesson content | Do not save or run code by default. |

## Enrolled-course controls

The verified `我的課程` controls were:

- `重置` returns to `/my/courses`.
- `依課程名稱排序` uses `sort=course`.
- `未過期` uses the base route; `已過期` uses `expired=true`.
- `全部` uses the base route; `主題課程` uses `type=course`; `綜合練習` uses `type=question`.
- Search submits a GET query whose semantic value is `q=<term>`; `utf8` and `button` may also appear as form transport parameters. Search results must be described from the current page, not from a stored inventory.
- After selecting `依課程名稱排序`, the current sort link can be labelled `依使用時間排序`, and status/type links preserve the existing query. Read the current href instead of constructing combinations.

## Lesson taxonomy

Lesson titles expose the kind of page an agent is entering:

- `【說明】`: a lesson page with a video iframe, shared course navigation, and discussion area.
- `【講解】`: a lesson page with a video iframe plus a JavaScript practice/editor iframe; `版型` may also be visible.
- `【試玩】`: an embedded JavaScript workspace under an iframe with `JavaScript`, `Assets`, `Preview`, `Console`, line numbers, and `Run`, `Format`, `Stop` controls.
- `【連結】`: a redirect-style lesson; follow only the visible next link and verify the destination.

Some `【連結】` pages expose a tokenized `Subcourse button` with an encoded `data` query value. Do not store or blindly follow it; use visible course navigation and verify the destination first.

All variants may show `老師我有問題！`, a topic search box, `課程列表`, and a `下一章` link. The lesson sidebar groups chapters under numbered units and exposes exact visible chapter links, so prefer those links over guessed numeric routes.

## Entity model

- Course: a titled learning program with duration, difficulty, prerequisites, features, lesson outline, and knowledge-point links.
- Unit: a numbered course section such as `貪吃蛇 AI`.
- Lesson: a typed chapter within a unit; it may be video, explanation, practice, or a link.
- Knowledge point: a `/knowledges/<slug>` entity linked from lessons and course outlines.
- Discussion board: a course or lesson-scoped collection of topics, linked from course and lesson pages.

Progress, current lesson, course availability, counts, timestamps, and card inventories are dynamic values, not entity definitions.

## Verification checklist

1. Read the visible heading and current URL.
2. For a course, confirm duration/difficulty and the relevant lesson or discussion entry point.
3. For a lesson, confirm breadcrumb, lesson type, `下一章`, and whether the page has video/editor if relevant.
4. For a search/filter, confirm both the URL query state and the visible result state.
