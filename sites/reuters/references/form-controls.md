# Reuters 表單與互動控制項

## Site search

| Control | 起點／輸入 | 觀察結果與驗證 |
| --- | --- | --- |
| `Open search bar` | 頁首 button | 顯示 `Search Reuters` searchbox、`Search`、`Close search bar`；先確認 searchbox 已 active |
| `Search Reuters` | 代表安全輸入 `AI` | Submit 後路由為 `/site-search/?query=AI`，heading 為 `Search results for “AI”`；query 與結果須當下重抓 |
| `Section` | native select；`All`、`World`、`Business`、`Legal`、`Markets`、`Breakingviews`、`Technology`、`Sustainability`、`Science`、`Sports`、`Lifestyle` | 變更後 URL 會加入如 `section=technology`；核對選中 label、heading、result count 與結果 category，不只看 URL |
| `Date range` | `Any time`、`Past 24 hours`、`Past week`、`Past month`、`Past year` | 變更後重新等待結果；記錄 query、date scope 與 observation time |
| `Sort by` | `Newest`、`Oldest`、`Relevance` | 變更後核對 selected option 與第一筆時間／排序；不要把結果順序永久化 |
| `Clear search text` | 有 query 時顯示 | 清除後必須重新確認 input value、Search 狀態與是否需要重新 submit |

## Markets

- `/markets/` 有 `Category` navigation，包含 `On the Money`、`Asian Markets`、`Carbon Markets`、`Commodities`、`Currencies`、`Deals`、`Emerging Markets`、`ETFs`、`European Markets`、`Funds`、`Econ World`、`Global Market Data`、`Rates & Bonds`、`Stocks`、`U.S. Markets`、`Wealth`。
- `US`、`Europe`、`Asia Pacific` 是 tablist；點選後以 `[selected]`、tabpanel label、region card 與頁面內容確認 state。切換可能先顯示 loading state。
- Markets 內的 `Search for securities` 是另一個 securities lookup control；輸入前確認目標是 quote lookup，不要誤用成全站文章搜尋。
- Tables 會以 `Future`／`Exchange`／`Name`／`Index` 等 row headers 與 `Last`／`Yield`／`% Change` 欄位顯示，並連到 quote route。保留來源與至少 15 分鐘 delay context。

## Article controls

- `Summary` 是 read-only tab；用 `[selected]` 和 summary list 驗證。
- `Change text size` 是閱讀視圖控制；若點擊無法安全驗證，保留 DOM evidence，不要猜測尺寸選項。
- `Save article` 可能寫入帳戶，`Share article` 可開啟分享流程；`Share article on X/Facebook/LinkedIn`、`Email article`、`Copy link` 都是 side-effect boundary。唯讀任務不要點。
- `Expand gallery in a modal window` 與 `Scroll image forward/backward` 是可讀媒體控制；進入 modal 前仍核對 current article 與 image caption。

## Interaction verification

每次控制後至少核對 URL、selected state／heading、結果或 status 中的兩項。若只看見按鈕或 label，不能宣稱控制項已理解。若頁面顯示 loading、空結果、錯誤或 target closed，先等待並用同一分頁重新檢查，再把未確認狀態標出。
