# FRED site map and page taxonomy

本 reference 整理本輪在目前 Codex 內建瀏覽器分頁確認的穩定頁型。Sitemap 與 robots 的結果是探索線索，不是完整功能或權限清單。

## Inventory status

| Route / source | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `/` | UI-verified | current-tab visual + DOM | Search、四個 Browse Data 入口、At a Glance、News and Blog、footer help。 |
| `/robots.txt` | client-blocked | automation/control error + same-tab visual retry | 兩次 `ERR_BLOCKED_BY_CLIENT`，分頁仍停在首頁；不可推論內容為空。 |
| `/sitemap.xml` | invalid candidate | current-tab visual + DOM | 顯示 FRED HTML 404，而非 XML Sitemap。 |
| `/sitemap_index.xml` | invalid candidate | current-tab visual + DOM | 顯示 FRED HTML 404，而非 Sitemap index。 |
| `/sitemap.xml.gz` | invalid candidate | current-tab visual + DOM | 顯示 FRED HTML 404，沒有下載 artifact。 |
| `/searchresults/?st=<term>` | UI-verified | current-tab DOM/interaction | 搜尋結果頁；結果連到 series。完整結果頁截圖在本輪因頁面過大而擷取逾時，保留 DOM/URL 證據。 |
| `/series/<series_id>` | UI-verified | current-tab DOM/interaction | 代表系列頁 `GDP` 已確認。 |
| `/data/<series_id>` | UI-verified | current-tab DOM/interaction | 代表資料表頁 `GDP` 已確認；完整截圖擷取逾時。 |
| `/categories` | UI-verified | current-tab DOM/interaction | 顯示主題與子主題；只驗證根頁，子分類需在未來任務中重新開啟。 |
| `/releases` | UI-verified | current-tab visual + DOM | Release catalog，50 筆一頁，使用 `pageID` 分頁；不要保存當下筆數。 |
| `/releases/calendar` | UI-verified | current-tab DOM/interaction | Release filter、日期導覽、排序與日期表格。 |
| `/sources` | UI-verified | current-tab DOM/interaction | Source catalog，使用 `pageID` 分頁；source detail 由頁面連出但本輪未深入。 |
| `/tags/series?ob=pv` | UI-verified | current-tab DOM/interaction | Popular series；顯示 popularity、單位、頻率、期間與同系列不同頻率變體。 |
| `https://fredhelp.stlouisfed.org/` | UI-verified | current-tab DOM/interaction | 第一方說明首頁，Data／Graphs／Maps／Account／FAQ／About 分頁；部分 accordion 內容本輪停留 spinner。 |
| `/docs/api/fred/` | UI-verified | current-tab DOM/interaction | FRED API Version 1/2 文件入口與 endpoint 索引。 |

## Page types and routing

| Page type | Entry | Durable fields / controls | Next step |
| --- | --- | --- | --- |
| Search results | Homepage search | keyword query, result title, series ID link, unit, frequency, seasonal adjustment, date range, description, other-format disclosure | Choose the exact series, then verify its series page. |
| Series detail / graph | `/series/<id>` | title and ID, current observation summary, updated time, next release, observations popup, date ranges, Edit Graph, Download, chart, source, release, notes, release tables | Use `/data/<id>` for a table; use Download only when an inbound artifact is needed. |
| Table data | observations `View All` or `/data/<id>` | metadata table, `DATE`, `VALUE` | Read current rows and cite metadata; refresh before reporting values. |
| Category catalog | Homepage `Category` | hierarchical topic labels and series counts | Follow a visible category link; counts are dynamic. |
| Release catalog | Homepage `Release` or `/releases` | release names, detail links, page navigation | Open `/releases/calendar` for dates or a visible release detail. |
| Release calendar | Main menu `Release Calendar` | release select, date controls, `today`, Date/Name sort, release rows and times | Verify selected release, displayed week/month, and empty states. |
| Source catalog | Homepage `Source` | source names and source IDs | Follow a visible source link; do not infer source coverage from names alone. |
| Popular series | Homepage `Popular Series` | popularity rank, series title, frequency/SA variants, periods | Choose a visible series variant, then use series workflow. |

## Coverage gaps

- Individual release detail, source detail, category detail, FRED account, FRED Add-in, mobile apps, maps, and ALFRED were not deeply explored.
- Help accordion panels for detailed Data/Graphs guidance remained on a spinner in this session; use the visible topic labels as routing hints and re-check the loaded content before relying on a detailed rule.
