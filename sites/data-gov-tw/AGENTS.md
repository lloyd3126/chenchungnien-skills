# 政府資料開放平臺（data.gov.tw）

## Scope

這份指引只適用於透過 Codex 內建瀏覽器操作 `https://data.gov.tw/`。它整理公開資料集的搜尋、篩選、詳情、資源與消息頁面。資料集名稱、筆數、排名、下載次數、更新時間與新聞內容都會變動，任務當下必須重新取得。

## Global routing

- 想依關鍵字、機關、主題、格式或資料屬性找資料集 → `$tw-gov-data-search`。
- 已知資料集 ID、需要欄位、提供機關、更新頻率、下載網址、API 位址、DCAT 或相關資料集 → `$tw-gov-data-dataset`。
- 想找最新消息、上架／下架公告、資料開放快訊、地方政府快訊或 RSS → `$tw-gov-data-news`。
- 需要更廣的資料集 metadata 盤點或既有 API 工作流時，才使用 `$tw-gov-data`；若本任務要求內建瀏覽器，優先採用上面三個 UI skills。

## Navigation

- 首頁 `/`：簡易搜尋、進階搜尋、17 個服務分類、每日異動資料集與熱門資料集。
- 資料集選單：全部資料集瀏覽 `/datasets/search`、預計下架 `/datasets/unpublished`、歷史資料 `/datasets/history`、資料集清單下載 `/datasets/datasets_download`。
- API 服務資料集：`/datasets/search?dt=openapi`；這是搜尋結果的資料提供屬性變體，不是另一個資料集頁型。
- 高應用價值主題：`/high_value_datasets`；目前頁面說明 9 類主題：農業永續、空間資訊、氣候環境、災害防救、交通運輸、健康醫療、能源管理、社會救助、企業永續。
- 資料故事館：應用展示 `/expos`、教育資源 `/courses`、活化應用 `/applications`、獎勵活動 `/rewards`。
- 互動專區：我想要更多 `/suggests`、我有話要說 `/comments`。
- 消息專區：最新消息 `/news`、專欄文章 `/columns`。
- 關於平臺：`/about`、網站導覽 `/sitemap`、常見問答 `/faqs`、應用工具 `/convert`、指引文件 `/about/doc`。
- 規範及統計：`/licenses`、`/m2m`，以及 `/statistics/site`、`/statistics/category`、`/statistics/agency`、`/statistics/quality`、`/statistics/wordcloud`、`/statistics/dashboard`。

## Operating rules

- 以使用者目前可見的內建瀏覽器分頁為唯一來源；不要改用 Chrome、外部瀏覽器、CLI、爬蟲、cookies、local storage 或 session 檔案。
- 導覽後先確認目前 URL、頁面 heading、主要控制項與結果狀態。若要聲稱某頁面「視覺可用」，必須有同一分頁的截圖證據；DOM 或控制錯誤不能取代視覺證據。
- 搜尋與篩選只做安全、可逆操作。下載 CSV／XML／JSON、開啟外部提供機關資源或 API 說明頁，只有在使用者需要該產物或後續操作時才執行，並驗證瀏覽器下載或外部頁面結果。
- 資料集詳情頁的資源網址常在外部機關網域；不要把 `data.gov.tw` 頁面存在誤當成外部資源可用，也不要在沒有使用者要求時註冊 TDX、建立 API key 或輸入任何秘密。
- 回應、建議、留言、登入、帳號與 API key 都是權限或外部狀態邊界。公開探索完成前不要要求登入；目前分頁未顯示登入狀態，本輪不探索受保護功能。
- 不要把當次搜尋結果、即時筆數、排名、下載次數、評分、新聞日期或資源 URL 寫死在 instructions；寫入重新搜尋與重新驗證的路徑。

## Sitemap-assisted inventory

- `/sitemap` 是由首頁「關於平臺 → 網站導覽」進入的第一方 HTML site map；本輪以目前分頁視覺與 DOM/interaction 確認，列出上述穩定路由。
- `/robots.txt` 在目前分頁被導向站內「無此頁面」狀態；截圖控制路徑曾 timeout／target closed，因此不能據此聲稱 robots 內容為空，也沒有把 Sitemap XML 標成已發現。
- 本輪未取得 `/sitemap.xml`、`/sitemap_index.xml` 或壓縮 XML；未使用 web search、CLI fetch、API 或外部瀏覽器補抓。
- 路由清單只是 inventory。每個動態頁仍要在目前分頁重新開啟並以當下 UI 驗證，詳見 [site-map.md](references/site-map.md)。

## Drift maintenance

- 操作前比較目前頁面的 URL、標籤、控制項、權限、欄位名稱與第一方說明；現行 UI 優先於本文件。
- 若穩定路由或流程改變，記錄公開／登入變體、頁型、舊行為、新行為、驗證證據與日期；不要寫入密碼、cookies、tokens、私人資料或動態結果。
- 只有在差異清楚、穩定且已由目前 UI 支持時，才更新負責的 AGENTS、skill 或 reference，並重跑受影響的安全流程與 skill validator。
- 若差異廣泛、矛盾或無法安全驗證，保留為 maintenance gap，不要猜測。

## References

- [site-map.md](references/site-map.md)：第一方網站導覽、頁型與本輪覆蓋狀態。
- [data-model.md](references/data-model.md)：資料集、資源分布、API 服務、DCAT 與關聯資料的穩定欄位語義。
- [search-controls.md](references/search-controls.md)：搜尋、進階搜尋、過濾、排序、分頁與 URL state。
