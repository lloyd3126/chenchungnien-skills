# 活動日曆與活動詳情控制項

## Activity list `/ActivityInfo/recap`

The current page exposes:

- year links for adjacent years and seasonal anchors `1-3月`, `4-6月`, `7-9月`, `10-12月`;
- time radios `今日`, `近7天`, `近14天`, `近30天`, `不限`;
- `關鍵字` textbox and `搜尋` button;
- `進階搜尋` dialog;
- grouped activity cards and pagination links.

The list path may change to `/ActivityInfo/recap/Search?pageIndex=0` after filtering. Use the current visible heading, selected state, filter tags, result count and card list rather than constructing query parameters.

## Advanced filter dialog

The dialog `進階篩選` contains:

- `開始時間` and `結束時間` date inputs;
- quick date controls `今日` and `本周`;
- audience checkboxes: `聽視障`, `青少年`, `樂齡`, `親子兒童`, `多元文化族群`, `分館活動群眾`, `一般大眾`;
- topic checkboxes: `講座`, `研習`, `展覽`, `活動`, `電影欣賞`;
- `清除全部` and `查看結果`.

Select only safe read-only filters. After `查看結果`, verify visible filter tags and the changed result count/cards. `清除全部` clears the dialog fields; apply it with `查看結果` before declaring the list reset.

In the 2026-08-17 exploration, the `樂齡` + `講座` combination applied and displayed two filter tags with an empty result for the retained keyword. Clearing the dialog and applying it removed the tags. A direct click on `近7天` did not visibly change the selected `今日` state in that run; treat that control as needing live verification, not as a guaranteed action.

## Activity detail `/ActivityInfo/recap/Detail/<id>`

Verify:

- heading and current detail URL;
- activity date/date range and location;
- audience link(s);
- `活動資訊` panel, body, images, tags, and optional `活動場次` table;
- `回列表` plus previous/next links.

An activity may include `google 活動行事曆` and an external `報名` or `[報名連結]`. Reading the link target is sufficient for discovery. Do not follow or submit registration, third-party forms, calendar creation, or login flows during ordinary research.
