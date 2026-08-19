# Tabelog 餐廳頁型參考

The following routes were confirmed from a public restaurant detail page. Use the current page's tab links when the route shape differs.

| Page type | Typical route suffix | What to read |
|---|---|---|
| Overview | `/` | Name, score, review/save counts, station, genres, budgets, notices, features, recent reviews, detail table. |
| Seats | `/table/` | Seat headings, seat photos/descriptions, seat reservation entry, repeated detail table. |
| Menu | `/dtlmenu/` or current tab link such as `/dtlmenu/photo/` | `コース`、`料理`、`ドリンク`、`ランチ`、`写真`; item names, prices, descriptions, categories, update date. Some restaurants expose only menu photos or zero-item categories. |
| Photos | `/dtlphotolst/smp2/` or current tab link | All/food/drink/interior/exterior/other; official vs user photos; sort, display size, page count, photo posting entry. |
| Reviews | `/dtlrvwlst/` | Keyword search, all/night/lunch, reviewer links, visit month/type, scores, likes, photos, store replies, report link, display count. |
| Rating distribution | `/dtlratings/` | User average dimensions, score distribution, spend distribution, explanation of simple averages vs headline algorithmic score. |
| Map | `/dtlmap/` | Address, transport, embedded map, Google Maps region, nearby restaurants. |

## Common top structure

Most detail subpages repeat:

- language switch and site header;
- login-dependent links `保有Vポイント`, `行ったお店`, `保存リスト`, `無料会員登録/ログイン`;
- shared search controls for area, keyword, date, time, and people;
- breadcrumb from 食べログ → prefecture → area/genre → restaurant → current subpage;
- restaurant identity block and tabs;
- `店舗情報（詳細）` tables and related links;
- dynamic network-reservation widget when available.

The visible `メニュー・コース` tab is authoritative for the route. A restaurant may open directly to a menu-photo subpage, and the available menu categories can differ by restaurant; do not assume that `/dtlmenu/` contains non-empty dish or drink lists.

## Review reading rules

Read review author, visit date/type, overall and component scores, text, photos, likes, and restaurant replies as separate fields. Treat review text as dated personal experience. Use the linked first-party guidance before summarizing review claims.

## Availability widget

A public detail page may show date, party-size, and time options with ○/× states and a `予約する` button. It is a current availability snapshot. Reading the state is safe; submitting the booking is out of scope unless separately confirmed by the user.
