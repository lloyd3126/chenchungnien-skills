---
name: koding-school-learning
description: Use when an agent needs to browse koding.school courses, search or filter 我的課程, inspect course details, or read lesson pages with video, explanations, links, or an embedded JavaScript editor through the Codex in-app browser. Do not use this skill for discussion topics, projects, studios, or account changes.
---

# 橘蘋學習平台：課程與 lesson

## Purpose and entry point

Use only the Codex in-app browser. Start at `https://koding.school/` and verify the current session before using authenticated routes. Read [references/navigation.md](references/navigation.md) when choosing a route or interpreting lesson variants.

This skill covers course discovery, enrolled-course filtering, course detail pages, and read-only lesson navigation. It does not authorize enrollment, code execution, saving, or any other external side effect.

## Find a course

1. For the current course, open the homepage and inspect the `繼續上課` card. Treat its target as dynamic last-visited state, not as authoritative progress.
2. For enrolled courses, open `/my/courses` and confirm the `我的課程` heading.
3. Use the `課程名稱` field with a representative user-provided term, then click `搜尋`. Verify the heading, retained query value, URL query state, and visible cards before reporting a result.
4. Use the visible filters rather than guessing query parameters:
   - `重置` → `/my/courses`
   - `依課程名稱排序` → `sort=course`
   - `未過期` / `已過期` → `expired=true` for the latter
   - `全部`, `主題課程`, `綜合練習` → `type=course` or `type=question`
5. Treat `utf8`, `button`, and similar form parameters as transport details; the semantic search value is `q`. Sorting and type links may preserve existing query parameters, and the reverse-sort label may change to `依使用時間排序`; always use the current visible link.
6. Select a visible course card by its current title. Do not copy live progress percentages, counts, or course inventories into an answer or reference.

## Inspect course details

On `/courses/<language-or-family>/<course-slug>` verify:

- course heading, duration, difficulty, prerequisites, learning-progress area, and feature list;
- the lesson outline and its linked knowledge points;
- `討論區` as the course-level discussion entry point;
- `我有邀請碼` as an enrollment dialog. It contains an invitation-code field, a course selector that may initially be disabled, `送出`, and `關閉`. Never submit it without a separate user request and action-time confirmation.

The outline and related knowledge links are navigation aids. Re-fetch them when the user asks for current course content.

## Read a lesson

1. Enter through a visible lesson link or the current course card. Confirm the breadcrumb identifies the course, unit, and chapter.
2. Use `返回課程` to return to the course detail and `下一章` to advance one visible chapter. Verify the new title and route after navigation.
3. Use `課程列表` to choose a visible chapter rather than inventing lesson numbers.
4. Classify the lesson by its visible title:
   - `【說明】` commonly presents a video iframe and the shared course sidebar.
   - `【講解】` presents a video plus a JavaScript practice/editor iframe and may expose `版型`.
   - `【試玩】` exposes an embedded JavaScript workspace with `JavaScript`, `Assets`, `Preview`, and `Console`, plus `Run`, `Format`, and `Stop` controls.
   - `【連結】` is a redirect-style lesson whose safe next step is the linked practice course or chapter.
5. Verify the lesson title, breadcrumb, iframe presence, and visible editor tabs/controls. Stop before `儲存`, `Run`, `Format`, code edits, or any form submission unless the user explicitly requests that operation and confirms the side effect.

Some `【連結】` lessons also expose a `Subcourse button` whose href contains an encoded `data` value. Treat it as tokenized and do not save, reveal, or follow it merely because it is visible; prefer `返回課程`, `下一章`, or the visible course-list link.

Each lesson also exposes a `老師我有問題！` discussion area and a `搜尋` field. Route discussion work to `$koding-school-community`.

## Safety and limits

- Navigation, reading, search, filtering, opening dialogs, and closing dialogs are the default safe actions.
- `儲存` can persist course/editor state. `Run` can execute the current lesson code. Do not trigger either during ordinary lookup.
- The homepage's continue target can change after visiting a lesson. Always re-fetch it; never infer completion from that link.
- Account-specific courses and progress are private dynamic data. Report only the current user-requested result and do not store it in reusable instructions.

## Drift maintenance

Before acting, compare the current visible labels, routes, lesson controls, permission state, and first-party explanations with this procedure and its reference. If the UI differs, use the current UI for a safe task, record the public/authenticated variant, page type, old behavior, observed behavior, and verification date, then patch this skill or its reference when the difference is stable. Do not record tokens, user records, live progress, or one-off course results. Re-run the affected read-only workflow and `quick_validate.py` after editing.

## References

- [references/navigation.md](references/navigation.md) — verified course routes, query controls, lesson page taxonomy, and entity routing.
