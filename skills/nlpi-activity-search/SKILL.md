---
name: nlpi-activity-search
description: Find and inspect current National Library of Public Information activities through the Codex in-app browser. Use for activity calendars, date windows, seasons, audience or topic filters, keyword searches, pagination, and activity detail pages; do not use it to submit registration.
---

# 國資圖活動搜尋與詳情

## Purpose and entry point

Use only the Codex in-app browser. Start at the visible `活動日曆` link or `https://www.nlpi.edu.tw/ActivityInfo/recap`. Read [activity-controls.md](../../sites/nlpi/references/activity-controls.md) for exact controls and verification.

## Find activities

1. Confirm the page heading `活動日曆` and current year. Use visible year or seasonal links when the user gives a year or quarter.
2. For a simple date window, use the visible radios `今日`, `近7天`, `近14天`, `近30天`, or `不限`. After the control action, verify the actual selected state and the result count; the `近7天` click was not stable in the exploration.
3. For keyword discovery, fill `關鍵字` and click `搜尋`. Verify the retained keyword, filter summary, result count, and changed cards. Do not report success when only the textbox changed.
4. For audience/topic/date combinations, open `進階搜尋`, select the requested checkboxes or dates, then click `查看結果`. Verify the visible filter tags plus result count/cards. Use `清除全部` and `查看結果` to reset temporary filters.
5. Use visible pagination and current activity cards. Treat titles, counts, dates, registration state, and availability as live values.

## Read an activity detail

1. Open a visible activity card at `/ActivityInfo/recap/Detail/<id>`.
2. Verify the heading, current URL, activity date/date range, location, audience links, `活動資訊` body, tags, optional `活動場次` table, and `回列表`.
3. Summarize only fields visible on the current detail page. Distinguish the main activity date from individual session dates.
4. Stop before external `報名`, `[報名連結]`, Google Calendar, third-party forms, or login. Those actions can transmit data or create commitments and require a separate user request and confirmation.

## Drift maintenance

Compare the live activity list, dialog labels, selected states, URL, result count and detail layout with this procedure. If a stable route, control, or workflow changes, complete only safe work, record the evidence and date, update this skill or the linked reference, and run `quick_validate.py`. Never write current activities, dates, counts, or availability into reusable guidance.

## References

- [activity-controls.md](../../sites/nlpi/references/activity-controls.md) — list, dialog and detail semantics.
- [data-model.md](../../sites/nlpi/references/data-model.md) — activity entity and relationships.
