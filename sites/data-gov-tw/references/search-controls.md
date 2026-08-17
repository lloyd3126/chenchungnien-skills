# data.gov.tw search controls

## Entry points

- Homepage simple search: `/` → textbox `請輸入關鍵字` → `搜尋`.
- Full dataset list: `/datasets/search`.
- Popular list: homepage `熱門資料集 → 查看全部` → `/datasets/search?type=pop`.
- Category list: homepage category links such as `/datasets/search?ct=257`.
- Provider list: dataset detail provider links use `/datasets/search?qs=<provider-id>`.
- API-service list: `/datasets/search?dt=openapi`.

## Keyword search

Fill `請輸入關鍵字` with a representative term. The page can expose autocomplete options such as `空氣品質AQI`; select a suggestion only when it matches the user's intent. Clicking `搜尋` updates a state similar to:

`/datasets/search?p=1&size=10&s=_score_desc&rft=<encoded-keyword>`

Validate the heading `資料集列表 | Datasets`, the URL query, the current input value, and at least one result card. Search results expose title, description, major field notes, provider, metadata update time, dynamic usage counters, category/keyword badges, and format labels.

## Advanced search

`進階搜尋` exposes:

- `資料集ID`
- provider multi-select `請輸入提供機關(複選)`
- `是否須包含底下子機關/單位`, checked by default in the observed public state
- repeatable AND/OR + field + value rows
- `新增`, `搜尋`, and `清空`

After submitting, verify the resulting URL or form state and the result set. Do not treat a visible control as understood until its submitted state is observable.

## Facets and result controls

`展開過濾條件` exposes tree groups for central/local agencies, common topics, service classification, file format, data-provision property and keywords. Counts are live facet counts; do not write them into instructions. Selecting a facet is safe, but verify that the query/result state changed before reporting a filtered result.

Observed sorting options include relevance, publication date, view/download counts, metadata modified date and agency name. The selected value is encoded in `s`, for example `s=pubdate.date_desc` for publication date newest-first. Page-size options are `10項/頁`, `30項/頁`, `50項/頁`, and `100項/頁`, encoded in `size`.

Pagination exposes previous/next buttons, numbered pages, and a `頁` spinbutton. Verify the current page in the URL (`p`) and a changed result card before claiming pagination succeeded.

## Safe boundaries

`搜尋結果匯出` and list-page CSV/XML/JSON controls are inbound downloads, but only trigger them when the user asks for the artifact. Never submit comments, login, API registration, or key creation as part of dataset search.
