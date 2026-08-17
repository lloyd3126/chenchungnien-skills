# 財報狗表單與互動控制

## Shared search

1. On the homepage or shared header, locate `搜尋個股或題材`.
2. Type a representative term and wait for the suggestion panel.
3. The panel can classify results as `全部`, `個股`, `題材`, and `新聞`; selecting `題材` was verified to show a topic result such as `台積電・概念股` while preserving the homepage.
4. Prefer the concrete result link: company routes use `/analysis/<ticker>`, topic routes use `/tags/<id>`, and article routes use `/news/<id>`.
5. Verify the destination heading and route. Clear the field or navigate away after a safe test.

## Company analysis ranges

- `財務報表` exposes two year `<select>` controls representing a start/end range; the observed default range used the earliest visible year through the current available year.
- `安全性分析`、`成長力分析`、`價值評估`、`關鍵指標` can also expose year-range selects and a `確定` action.
- After changing a range, verify the selected values and the chart/table period. Never copy the resulting numbers into instructions.

## Custom screening

- `/screeners/custom` groups conditions under `財報數據條件`、`獲利能力條件`、`安全性條件`、`成長力條件`、`價值評估條件`、`經營階層條件` and `關鍵指標條件`.
- A condition is represented by an operator select (`大於`／`小於`) and a value select. Conditions use different units and option sets; read the nearby label before selecting a value.
- The page also exposes `我的選股清單1`–`5`, presets such as `彼得．林區`、`巴菲特選股`、`葛拉漢選股`, and controls named `開始選股`、`清空`、`儲存條件`／`儲存篩選條件`.
- Selecting a condition is a safe local test. Saving a condition or changing a named list is an external account mutation and requires the user's action-time confirmation.

## Ranking and market controls

- Ranking pages expose column links such as `股號／名稱`、`月營收年增率`、`月營收月增率` and `月營收`; clicking a sort link may update the result through a remote page update without changing the URL.
- Verify sort direction from the visible heading, active column or first rows, and use `查看下 100 家公司` only when the user needs more rows.
- `/market-trend` exposes market scope `全部`／`台股`／`美股` and periods `1天`、`1周`、`1月`、`3月`、`YTD`、`1年`. A period change was verified to replace the concept/sector visualization with a new current result set.
- Topic pages expose benefit-level radio controls and company checkboxes. The radio controls were visible, but a direct programmatic click did not change the selected state in the tested page; do not assume the filter worked without a visible state change.

## Blog and account controls

- `/blog/` has `搜尋文章`, category links, article cards and pagination. Filling the field and pressing `Submit` was verified to navigate to `/blog/search/<encoded-term>` and show a result page. Treat the result count and article list as dynamic; if the current UI does not show a result change, use category links or article links instead.
- `/portfolios` exposes `新增個股`, `修改清單名稱`, an `新增個股到此清單` field and table columns including stock name, price, change, change percentage, P/E, dividend yield, P/B and delete. Do not submit add, rename or delete actions while exploring.
- `/users/account` exposes avatar upload, display name, plan and newsletter checkbox. The account menu currently labels the password route `重設密碼`, while the account page tab labels it `修改密碼`. Do not upload, save, reveal, or modify account data during discovery.
