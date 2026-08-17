---
name: koding-school-projects
description: Use when an agent needs to browse koding.school projects, studios, the signed-in profile/resume, or account-management entry points through the Codex in-app browser. Use it for read-only discovery and routing; stop before creating, editing, removing, saving, or changing account data.
---

# 橘蘋學習平台：作品、工作室與帳號入口

## Purpose and entry point

This skill is for authenticated, user-specific areas. Start at `https://koding.school/`, open the navigation menu, and verify the signed-in account before using `/my/*` routes. Read [references/projects.md](references/projects.md) for page taxonomy and privacy boundaries.

## Browse projects

1. Open `/my/projects` and verify the page is the signed-in `我的作品` view.
2. Use the visible `專案名稱` search field and `搜尋` control only when the user supplies a search term. The form is a GET to `/my/projects`; verify the semantic `q` value and visible result state rather than assuming a filter worked. `utf8` and `button` may appear as transport parameters.
3. Use visible language tabs such as `Web`, `JavaScript`, `Python`, `App Inventor`, `Scratch 3`, `Aibotgame`, and `Lua` to change the list view when present.
   Search results may expose only tabs with matching content; treat the current tab set as dynamic.
4. `回收桶` is a separate `/my/projects/deleted` branch. Do not restore, delete, or otherwise mutate anything while browsing.
5. A project card leads to `/projects/<project-id>`. Treat its content as user-specific and do not switch into edit mode unless the user asks for that exact project operation.

## Browse studios

1. Open `/my/studios` and verify the `我的工作室` page.
2. Select a visible `進入` link to `/studios/<studio-id>` only when the user asks to inspect that studio.
3. A studio page shows its title, `我的工作室`, project cards, `新增作品`, and `移除`. `新增作品` and `移除` are state-changing controls; stop before them.
4. `新增工作室` on the list page is also a creation boundary. Opening a form may be safe, but do not submit it without confirmation.

## Browse the signed-in profile

- `/resume/<student-id>` exposes a profile/resume page with skills, projects, and pagination such as `?page=2`. Treat the student id, project list, and biography as dynamic personal data.
- `/my/messages` lists private inbox threads and `/my/messages/<message-id>` is a message detail route. Do not open message bodies unless the user explicitly requests that private read.
- `/my/account` contains account, email, birthday, nickname, residence, and biography controls. Its primary form posts to `/my/account`; never edit or submit it during discovery.
- The current account menu exposes `我的課程`, `我的作品`, `我的工作室`, `我的收信匣`, `我的履歷`, `帳號設定`, and `登出`. Subscription/order links were not visible in this pass; do not assume they exist or open guessed financial routes.
- The account page can also contain invitation and project-creation forms. Treat every non-account form and its hidden fields as a side-effect boundary; inspect labels only and never submit during discovery.

## Safety and limits

- Do not record current project names, ids, studio names, message content, profile fields, progress, or other user records in durable guidance.
- `新增作品`, `新增工作室`, `儲存`, `移除`, account updates, project edits, uploads, and sign-out are action boundaries. Ask for confirmation immediately before any such browser action.
- Do not use a project or studio link as permission to expose its private content or to modify it.

## Drift maintenance

Before acting, compare the visible account menu, route, labels, tabs, permissions, and form structure with this procedure. If they differ, complete only a safe read-only task using the current UI, record the exact authenticated mismatch and date, and patch this skill or its reference when stable. Never store private records, credentials, cookies, tokens, or live project data. Re-run the affected read-only workflow and `quick_validate.py` after editing.

## References

- [references/projects.md](references/projects.md) — verified project, studio, profile, inbox, and account page routing.
