# Tabelog 搜尋表單控制項

## Shared search form

The public homepage and many result/detail pages expose the same visible controls:

| Visible purpose | Observed name | Safe use |
|---|---|---|
| Area or station | `sa` | Type a city, station, or area, wait for the visible autocomplete list, then select the intended suggestion such as `銀座駅`. |
| Keyword | `sk` | Enter a cuisine, restaurant name, or condition such as `焼肉`. |
| Date | `search_date` plus a hidden normalized date | Use the visible date control and verify the resulting state. |
| Time | `svt` | Select a visible time option; re-read the selected option after navigation. |
| Party size | `svps` | Select the requested number of people; options observed from 1名 to 99名. |
| Search | visible `検索` button | Safe read-only action; verify the result page. |

The homepage search form observed a GET action at `https://tabelog.com/rst/rstsearch/`. The actual destination can redirect to a genre- or area-specific `/rstLst/` route, so route by the current UI and verify the final page rather than hard-coding a URL.

## Area autocomplete

The `エリア・駅` input exposes visible suggestion list items after typing. A query such as `銀座` offered `銀座駅`, `銀座(東京都 中央区)`, same-named areas in other prefectures, `東銀座駅`, and `銀座一丁目駅`. Select the intended item before submitting. In the public test, submitting after typing without selection displayed `該当のエリア・駅が見つかりませんでした` and loaded a national genre list; selecting `銀座駅` produced headings scoped to `銀座駅の焼肉` and URL parameters for the Tokyo area and station.

## Result filters

- Budget lower / upper selects are represented by `LstCos` and `LstCosT`; options are ranges from no lower/upper limit through progressively higher yen amounts.
- `LstRev` is an operating-hour / meal condition select; observed options included no restriction, breakfast, lunch, late-night entry, after-midnight entry, and until-first-train service.
- Additional conditions appear as links or checkboxes for private rooms, all-you-can-drink/eat, cards, charter, parking, children, pets, coupons, takeout, delivery, smoking, equipment, and scenes.
- `詳細条件` expands more conditions. Use only representative safe checks and record the exact visible label and resulting condition summary.
- There can be duplicate controls in the shared header and sidebar. Scope selectors to the form and action being used; after navigation, inspect fresh DOM rather than trusting stale element state.

## Evidence pattern

For every applied control, record:

1. Initial selected value and default.
2. Exact visible option or input.
3. The control used to apply it.
4. New heading, selected value, URL/query state, or result change.
5. Whether reset/clear was visible or tested.

Observed public evidence: selecting the `銀座駅` autocomplete suggestion scoped the result; selecting a ￥3,000 budget lower bound changed the result heading to an evening ￥3,000-or-more condition; selecting `ランチ` changed it to a lunch condition. Other controls may have site-specific semantics and must be revalidated in the current session.
