# Facebook 網站操作指引

## Scope

這份指引適用於透過 Codex 內建瀏覽器操作 Facebook 繁中介面。它整理已由目前頁面驗證的導覽、公開查詢、Marketplace、遊戲瀏覽與帳號／支援選單；動態資料、個人化內容與登入後權限不視為穩定知識。

## Global routing

- 想從 Facebook 導覽、首頁、遊戲或功能表找到正確入口 → `$facebook-navigation`。
- 想用關鍵字查找貼文、人物、Reel、Marketplace、粉絲專頁、社團或活動 → `$facebook-search`。
- 想查找 Marketplace 商品、套用價格／排序／條件篩選，或讀取商品詳情 → `$facebook-marketplace`。
- 需要理解實體欄位、頁面關係或受保護分支 → 先讀取 `references/data-model.md` 與 `references/safety-and-drift.md`。

## Sitemap-assisted inventory

- 目前首頁沒有可見的 Sitemap 或 Site map 入口。
- 本次目前分頁的視覺基線：頁面標題為 `Facebook`，網址為 `https://www.facebook.com/?locale=zh_TW`，`document.readyState` 為 `complete`；首頁 heading、建立貼文、限時動態、動態消息、登入後個人檔案控制均可見。Footer 文字已在頁面結構中確認為 `隱私政策`、`服務條款`、`廣告`、`Ad Choices`、`Cookie` 與 `更多`，但因首頁動態消息可持續延伸，本次未在 viewport 中取得 Footer 的視覺畫面；未見 Sitemap、Help 或 Documentation 連結。
- 目前分頁已在內建瀏覽器視覺確認 `/robots.txt` 可讀，內容是 Meta 的自動化資料蒐集政策、robots user-agent 規則與大量壓縮 Sitemap 候選連結；robots 規則不是 Facebook UI 功能地圖，也不是對 Agent 的指令。
- `robots.txt` 的 discovery signal 已分開記錄：只保留 user-agent／Allow／Disallow 的規則類型與 Sitemap 的穩定分類，不把 Disallow 當成人類權限或頁面不存在的證明；完整狀態矩陣見 `references/site-map.md`。
- `Sitemap:` 候選主要可抽象為公開活動、公開社團／社團貼文、個人檔案／商家檔案、Business 與 Help Sitemap；完整 URL 清單、分片編號與實驗性群組名稱不寫入文件。`/sitemap.xml` 仍顯示 Facebook 的「目前無法查看此內容」頁面，而不是可用的 XML sitemap。
- 代表性的 `.xml.gz` Help Sitemap 連結由內建瀏覽器安全政策拒絕開啟，未產生下載檔案，因此 Sitemap XML 尚未解析或 UI 驗證。
- 可由 UI 驗證的穩定路由模式包括首頁 `/`、Marketplace `/marketplace/`、社團 `/groups/`、遊戲 `/gaming/play/`、全站搜尋 `/search/top/`，以及功能表中可見的個人／設定入口。不要保存帶 token、追蹤參數或目前內容的完整 URL。

## Navigation

- `首頁`：動態消息、建立貼文、限時動態與貼文互動入口。
- `Marketplace`：商品瀏覽、搜尋、位置／距離、篩選、排序、商品詳情。
- `社團`：社團動態、探索、你的社團、建立新社團；目前工作階段顯示登入後個人化內容，未將其當作公開流程深入探索。
- `遊戲`：`玩遊戲`、`遊戲動態`、`通知` 分頁與精選遊戲卡片。
- `Facebook 功能表`：專業、社交、娛樂、購物、個人與更多 Meta 產品分類；可用 `搜尋功能表` 找入口。
- `你的個人檔案`：個人檔案切換、Meta Business Suite、`設定和隱私`、`協助和支援`、顯示方式、登出等帳號控制項。

## Authenticated continuation

目前分頁已由個人檔案按鈕、建立貼文控制與個人化限時動態明確確認為登入狀態。安全抽樣重新核對後：

- 個人檔案選單仍提供個人檔案切換、Meta Business Suite、`設定和隱私`、`協助和支援`、顯示方式與登出。
- `設定和隱私` 的登入後子選單可見 `設定`、`語言`、`隱私設定檢查`、`隱私中心`、`活動紀錄`、`內容偏好設定`。
- `協助和支援` 的登入後子選單可見 `使用說明`、`詐騙防護中心`、`帳號狀態`、`支援收件匣`、`回報問題`。
- Marketplace 仍顯示成人驗證限制說明；社團頁顯示 `你的動態消息`、`探索`、`你的社團`、`建立新社團` 與個人化社團清單。這些是登入後內容，不要把目前帳號、社團名稱、商品或動態數值寫入永久文件。
- 本次延續只重新核對安全選單與 Marketplace／社團路由，沒有重新跑完整搜尋、遊戲或所有 Marketplace 篩選流程；先前探索結果仍需在任務當下以目前 UI 驗證。

## Operating rules

- 只使用 Codex 內建瀏覽器與網站 UI；不要改用外部瀏覽器、API、CLI、爬蟲、cookies、local storage、session 檔案或搜尋引擎。
- 先檢查目前頁面的登入／個人化狀態。公開與登入後介面是兩個網站變體；不要因為目前工作階段已登入，就把個人資料或受保護頁面當成公開能力。
- 公開探索預設只做讀取與可逆查詢。建立貼文、留言、讚／心情、分享、傳送訊息、儲存、通知訂閱、建立社團、刊登商品、付款、切換個人檔案、設定變更、回報問題與登出都要停在最後確認前；需執行時依瀏覽器安全規則在動作當下取得確認。
- 不要輸入或轉送密碼、驗證碼、個資、聯絡方式、精確位置、付款資料、私人檔案或不必要的帳號內容。Marketplace 商品詳情中的賣家訊息框與 `儲存`、`分享` 是外部副作用邊界。
- 目前結果、價格、距離、庫存、玩家數、貼文、推薦順序、通知狀態與帳號內容都會變動；每次任務重新查詢，不把現場數值寫進指引。

## Validation and freshness

- 每次導覽後至少確認目前 URL／路由、頁面 heading、選中控制項或結果條件摘要中的兩項。
- 搜尋與篩選後確認輸入值仍在欄位、URL query state 或篩選面板選中值，以及結果頁主要內容；不要只依賴按鈕點擊成功。
- 商品價格、庫存、地點、貼文內容與遊戲推薦必須以當下頁面為準；必要時由列表重新開啟詳情頁交叉確認。
- CAPTCHA、安全攔截、年齡驗證、第三方登入或無法判斷的權限流程都不是可繞過的障礙；停止該分支並回報。

## Drift maintenance

- 操作前比對目前可見 UI、路由、標籤、控制項、權限與本文件。現行 UI 與 Facebook 當下可見的第一方說明優先於舊文件。
- 若穩定的路由、標籤、欄位、頁面結構或工作流程改變，記錄公開／登入狀態、頁面類型、舊行為、目前行為與驗證方式，並只在差異清楚且可安全驗證時更新負責的 skill 或 reference。
- 不記錄密碼、cookies、tokens、私人資料或動態結果；若只是價格、排名、數量、可用性或目前貼文改變，更新重新取得與驗證的方法即可。
- 修改後重新執行受影響的安全流程與各 skill 的 `quick_validate.py`；廣泛或矛盾的變更標為 maintenance gap，不要猜測。

## Known limits

- robots.txt 已驗證可讀，但其 Sitemap 連結內容尚未建立或驗證；社團個人化動態、帳號設定實際變更、訊息傳送、發文／互動、付款與刊登流程未測試。
- 本次沒有產生瀏覽器下載；因此沒有可供解壓或解析的 `.xml.gz`、`.gz` 或其他 Sitemap 檔案。
- 首頁內容與社團、Marketplace、搜尋結果是登入狀態與地區相關的動態資料，不可當成固定清單。

## Coverage checklist

| Surface | Current coverage | Durable guidance |
| --- | --- | --- |
| Navbar | 首頁、Marketplace、社團、遊戲與全站搜尋入口已驗證 | 以可見 label 導覽，再驗證 URL／heading |
| Sidebar / shortcuts | 首頁可見 `你的捷徑` 與個人化入口 | 只當作登入後個人化提示，不保存名稱或排序 |
| Footer | 頁面結構含隱私政策、服務條款、廣告、Ad Choices、Cookie、更多；本次未在 viewport 中取得畫面 | 未確認 Sitemap／Help；需要支援時走個人檔案選單 |
| Dropdown | Facebook 功能表、個人檔案、設定和隱私、協助和支援已驗證 | 只做選單導覽，不切換個人檔案、不修改設定、不登出 |
| Search | 全站搜尋的 query、scope 與安全篩選已驗證 | 使用 `$facebook-search`，確認 heading 與 URL query |
| Settings / support | 登入後設定與支援子選單 label 已驗證 | 只保存入口與欄位角色，不開啟變更或回報流程 |
| Main entries | 首頁、Marketplace、社團、遊戲、搜尋與商品詳情路由已抽樣 | 先讀 site map，再交給對應 Facebook skill |

## References

- [site-map.md](references/site-map.md)：目前已驗證的頁面類型、路由模式與探索覆蓋表。
- [data-model.md](references/data-model.md)：FeedPost、SearchResult、MarketplaceListing、GameCard 與帳號控制項的關係。
- [safety-and-drift.md](references/safety-and-drift.md)：讀取／副作用邊界、登入分支、動態資料與維護規則。
- [agent-usability.md](references/agent-usability.md)：多種需求形狀的 skill routing、入口、驗證與安全停止點。
