# 站點地圖與路由證據

最後驗證：2026-08-17。以下只記錄從目前分頁的第一方 UI 看得到的路由與穩定結構，不記錄首頁或查詢結果的即時筆數、日期與熱門項目。

## 探索狀態

| 入口 | 結果 | 證據與限制 |
| --- | --- | --- |
| `https://lawsearch.judicial.gov.tw/default.aspx` | UI-verified | 首頁、導覽列、查詢功能選單與子系統連結均以截圖及 DOM 確認。 |
| `https://lawsearch.judicial.gov.tw/sitemap.aspx` | UI-verified | 第一方 HTML 網站導覽，以同分頁截圖及 DOM 確認。 |
| `https://lawsearch.judicial.gov.tw/robots.txt` | client-blocked | 同分頁導覽時瀏覽器回報 `ERR_BLOCKED_BY_CLIENT`，重試後仍停留在原頁；這不代表 robots.txt 無內容或網站沒有 sitemap。 |
| `https://lawsearch.judicial.gov.tw/LAW_Mobile_SEARCH/default.aspx` | UI-verified | 行動版首頁與 hamburger 選單均以同分頁確認。 |
| `https://legal.judicial.gov.tw/FLAW/default.aspx` | UI-verified | 法規一欄式查詢、結果分類與法規詳細頁已確認。 |
| `https://legal.judicial.gov.tw/FINT/default.aspx` | UI-verified | 判解函釋一欄式查詢、分類結果與詳細頁已確認。 |
| `https://judgment.judicial.gov.tw/FJUD/default.aspx` | UI-verified | 裁判書查詢、分類結果與裁判詳細頁已確認。 |
| `https://judgment.judicial.gov.tw/FJUD/readme.aspx` | error-page | 同分頁重試兩次均導向「連線逾時」系統訊息頁，未將其內容當作說明證據。 |

## 桌面版功能路由

### 法學資料入口

| 顯示名稱 | 連結 |
| --- | --- |
| 首頁 | `/default.aspx` |
| 本院主管或審判相關法規 | `https://legal.judicial.gov.tw/FLAW/default.aspx` |
| 判解函釋 | `https://legal.judicial.gov.tw/FINT/default.aspx` |
| 裁判書查詢 | `https://judgment.judicial.gov.tw/FJUD/default.aspx` |
| 簡易案件查詢 | `https://judgment.judicial.gov.tw/FJUD/defaulte.aspx` |
| 除權判決查詢 | `https://judgment.judicial.gov.tw/FJUD/defaultk.aspx?ty=E` |
| 公示催告裁定查詢 | `https://judgment.judicial.gov.tw/FJUD/defaultk.aspx?ty=V` |

入口首頁也提供上述每個功能的「一欄式查詢」與「更多條件查詢」；進階路由分別是同一子系統的 `Default_AD.aspx`、`Defaultk_AD.aspx` 或 `Defaulte_AD.aspx`。

### 法令判解系統

| 區域 | 一欄式 | 進階 |
| --- | --- | --- |
| 本院主管或審判相關法規 | `/FLAW/default.aspx` | `/FLAW/Default_AD.aspx` |
| 判解函釋 | `/FINT/default.aspx` | `/FINT/Default_AD.aspx` |
| 系統說明 | `/readme.aspx` | — |

已從 UI 確認的詳細頁路由形狀：法規資料使用 `/FLAW/dat02.aspx` 等頁面，判解函釋使用 `/FINT/data.aspx`。完整 href 必須從目前結果清單讀取。

### 裁判書系統

| 區域 | 一欄式 | 進階 |
| --- | --- | --- |
| 裁判書查詢 | `/FJUD/default.aspx` | `/FJUD/Default_AD.aspx` |
| 簡易案件查詢 | `/FJUD/defaulte.aspx` | `/FJUD/Defaulte_AD.aspx` |
| 除權判決查詢 | `/FJUD/defaultk.aspx?ty=E` | `/FJUD/Defaultk_AD.aspx?ty=E` |
| 公示催告裁定查詢 | `/FJUD/defaultk.aspx?ty=V` | `/FJUD/Defaultk_AD.aspx?ty=V` |
| 系統說明 | `/FJUD/readme.aspx` | — |

裁判書詳細頁使用 `/FJUD/data.aspx?ty=JD&id=<observed-id>&ot=in` 的形狀；`<observed-id>` 不可自行猜測。

## 行動版路由

入口：`/LAW_Mobile_SEARCH/default.aspx`。

行動版 hamburger 選單以 UI 確認以下導覽：

- 法規：`https://legal.judicial.gov.tw/LAW_Mobile_FLAW/FLAW/default.aspx`
- 判解函釋：`https://legal.judicial.gov.tw/LAW_Mobile_FLAW/FINT/default.aspx`
- 裁判書查詢：`https://judgment.judicial.gov.tw/LAW_Mobile_FJUD/FJUD/default.aspx`
- 簡易案件：同一 `LAW_Mobile_FJUD/FJUD/default.aspx?ty=e` 路由家族
- 除權判決：同一 `LAW_Mobile_FJUD/FJUD/default.aspx?ty=ke` 路由家族
- 公示催告裁定：同一 `LAW_Mobile_FJUD/FJUD/default.aspx?ty=kv` 路由家族
- 電腦版：`https://lawsearch.judicial.gov.tw`

行動版首頁的最新內容會連到 `cons.judicial.gov.tw`、法令判解行動頁或裁判書行動頁；那些是可見的一方連結，但內容與數量屬動態資料。
