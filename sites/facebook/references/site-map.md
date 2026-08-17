# Facebook Site Map and Coverage

## Inventory status

| Discovery source | Result | Status |
| --- | --- | --- |
| Visible Sitemap / Site map | 首頁與功能表未見 sitemap 入口 | unavailable |
| `/robots.txt` | 內建瀏覽器可直接顯示；含資料蒐集政策、user-agent 規則與 Sitemap 候選連結 | UI-verified policy file |
| `/sitemap.xml` | 回到 Facebook「目前無法查看此內容」頁面，未呈現 XML | unavailable / unverified |
| Compressed sitemap download | 代表性的 Help `.xml.gz` 連結被內建瀏覽器安全政策拒絕；未出現下載頁、下載提示或檔案 | blocked / not parsed |
| Navbar and menus | UI 直接提供首頁、Marketplace、社團、遊戲、搜尋、帳號與支援入口 | UI-verified |

## Sitemap status matrix

狀態欄位刻意分開：`discovered` 只代表在 robots 或 UI 探索中看到候選；`visually accessible` 代表該候選在內建瀏覽器有可讀畫面；`downloaded`、`locally parsed` 與 `UI-verified` 不可互相推定。

| Sitemap source / stable category | discovered | visually accessible | downloaded | locally parsed | UI-verified | Result |
| --- | --- | --- | --- | --- | --- | --- |
| `/robots.txt` 中的 Sitemap 行 | yes | yes（純文字政策頁） | no | no | yes（僅 robots 文件） | discovery signal only |
| Conventional `/sitemap.xml` | yes（曾以明確路徑檢查） | yes（顯示 Facebook unavailable shell） | no | no | no（不是 XML Sitemap） | invalid / unavailable |
| 公開活動、公開社團／社團內容候選 | yes（robots 分類） | no（未逐一開啟） | no | no | no | discovered / unavailable |
| 個人／商家檔案候選 | yes（robots 分類） | no（未逐一開啟） | no | no | no | discovered / unavailable |
| Business 與 Help `.xml.gz` 候選 | yes（robots 分類） | no | no | no | no | discovered / unavailable |
| 代表性 Help `.xml.gz` 候選 | yes（robots） | no（內建瀏覽器安全政策拒絕） | no（沒有下載提示或檔案） | no | no | blocked / not parsed |
| No sitemap discovered | no | n/a | n/a | n/a | n/a | not applicable：已從 robots 發現 Sitemap 候選 |

沒有任何一列產生可供本地解壓的檔案，因此沒有宣稱 `.gz` 已下載、解壓或 XML 已解析；也不保存完整 URL 清單、分片數量、日期或即時數量。

## Robots discovery signal

目前可見的 `/robots.txt` 純文字頁包含 Meta 的自動化資料蒐集政策提醒，以及多個 named crawler `User-agent` 區段與 `User-agent: *`。解析時只保留規則類型：

- `Allow` 的代表性路徑模式包含 bootloader endpoint、一般 PagePostsSectionPagelet、`/careers/` 與 `/safetycheck/`。
- `Disallow` 的代表性路徑模式涵蓋 plugins、AJAX／dialog、feeds、登入導向參數、檔案下載、分享／sharer、reaction browser、OAuth，以及 Business／搜尋 query 變體。
- `Sitemap` 行指向壓縮 inventory 類型，包括公開活動、社團／社團貼文、個人／商家檔案、Business 與 Help；它們只是 discovery signal。

`User-agent`、`Allow`、`Disallow` 與 robots 註解不是對 Agent 的操作指令，也不能證明人類使用者的權限、某個 UI 頁面不存在或某條路由必然可讀。

## Verified coverage

| Area | Representative route pattern | What was verified | Status |
| --- | --- | --- | --- |
| Home/feed | `/` | `建立貼文`、`限時動態`、動態消息與貼文互動控制 | explored, read-only |
| Marketplace home | `/marketplace/` | `搜尋 Marketplace`、所有類別、位置／距離、商品卡片 | explored |
| Marketplace search | `/marketplace/<area>/search/` | keyword query、`篩選條件`、位置、結果卡片 | explored |
| Marketplace filters | same search page | sort radios、price range、商品狀況、上架日期、存貨狀況 | explored |
| Marketplace detail | `/marketplace/item/<listing-id>/` | title、price、stock、location、condition、seller message box、save/share controls | explored, no side effects |
| Global search | `/search/top/` | search query、全部／人物／Reel／Marketplace／粉絲專頁／社團／活動分頁 | explored |
| Search filters | `/search/top/` | 最新貼文、你看過的貼文、發佈日期、貼文來源、標註的地點 controls | explored, read-only |
| Games | `/gaming/play/` | 玩遊戲、遊戲動態、通知 tabs 與精選遊戲卡片 | explored, no game launched |
| Groups | `/groups/feed/` | 社團、搜尋社團、探索、你的社團、建立新社團入口；內容是登入後個人化 | partial, protected |
| Account menu | profile menu | profile switching、設定和隱私、協助和支援、顯示方式、登出 | explored, no changes |

## UI coverage checklist

| Surface | Verified entry / control | Verification note |
| --- | --- | --- |
| Navbar | 首頁、Marketplace、社團、遊戲、搜尋 | route、heading 或 active state 需二次確認 |
| Sidebar / shortcuts | `你的捷徑` 與登入後個人化入口 | 只記錄結構，不記錄目前名稱或排序 |
| Footer | 頁面結構含隱私政策、服務條款、廣告、Ad Choices、Cookie、更多 | 本次未在 viewport 中取得 Footer 畫面；未確認 Sitemap／Help／Documentation |
| Dropdowns | Facebook 功能表、個人檔案、設定和隱私、協助和支援 | safe menu inspection；不執行變更 |
| Search | `搜尋 Facebook`、scope tabs、貼文篩選 | 由 `facebook-search` 負責 |
| Settings / support | 設定、語言、隱私設定檢查、隱私中心、活動紀錄、內容偏好設定；使用說明、詐騙防護中心、帳號狀態、支援收件匣、回報問題 | 只驗證登入後 routing labels |
| Main entries | 首頁、Marketplace、社團、遊戲、全站搜尋 | 以對應 skill 處理，不以 robots 代替 UI |

## Authenticated continuation recheck

目前分頁明確顯示登入狀態。為避免重新遍歷整站，本次只重查登入後安全分支與兩個抽樣路由：

| Surface | Authenticated observation | Status |
| --- | --- | --- |
| Home | profile control、建立貼文、個人化限時動態與首頁 heading 可見 | rechecked |
| Profile menu | profile switching、Meta Business Suite、settings/privacy、support/help、display/accessibility、logout | rechecked, no changes |
| Settings/privacy submenu | 設定、語言、隱私設定檢查、隱私中心、活動紀錄、內容偏好設定 | rechecked, menu only |
| Support submenu | 使用說明、詐騙防護中心、帳號狀態、支援收件匣、回報問題 | rechecked, menu only |
| Marketplace | `/marketplace/`、搜尋入口、位置／距離、商品卡片與成人驗證限制說明 | rechecked, no side effects |
| Groups | `/groups/feed/`、社團搜尋、探索、你的社團、建立新社團與個人化清單 | rechecked, protected content not opened |
| Search / Games | 保留上次已驗證的 routing；本次延續未重新跑完整流程 | not rechecked in this continuation |

## Robots-derived sitemap candidates

`/robots.txt` 是 UI-verified 的政策與索引候選來源，不是功能存在、公開權限或可操作性的證明。只保留下列穩定分類：

- 公開活動：`cpg_offplat_future_public_events_sitemap.xml.gz` 類型。
- 公開社團與社團內容：`public_active_groups_sitemap.xml.gz`、`groups_*_sitemap.xml.gz`、`groups_*_posts_<shard>.xml.gz` 類型。
- 個人／商家檔案：追蹤者門檻、無 vanity URL、local business、main profiles、professional-mode profiles 等 inventory 類型。
- Business 與 Help：`business/sitemap/...xml.gz` 與 `sitemap/www_facebook_com_help_sitemap.xml.gz` 類型。

大量分片、實驗性或推薦排序相關的 `groups_*` 檔名不保存。代表性 compressed Help Sitemap 未能開啟，故上述候選均標為 `sitemap—unverified`，沒有從 XML 推導頁面內容或完整路由清單。

## Stable routing notes

- 使用 UI 的可見 label 導覽；不要依賴追蹤參數、短期 token 或目前結果的完整 URL。
- 商品詳情與搜尋結果中的 `<area>`、`<listing-id>`、query、價格、距離與內容都是動態值；只保留路由形狀。
- `Facebook 功能表` 內的分類可以改變；必要時使用 `搜尋功能表`，再以頁面 heading 或 URL 驗證落點。
- `你的個人檔案` 與 `社團` 的內容會受到登入身份、切換的個人檔案與權限影響；不要在永久 reference 中記錄目前帳號或社團名稱。

## Page taxonomy

- Feed page：貼文作者／時間／可見對象／內容與 media／讚心情留言分享控制。
- Search results：query heading、scope tabs、filters、feed 或 entity result cards。
- Marketplace results：query、location-radius、filters、sort、listing cards。
- Marketplace detail：listing fields、seller contact affordance、location、save/share/more actions。
- Games hub：tablist、featured game cards、game metadata、play links。
- Account/help menu：profile switcher、settings/privacy、support and help, display/accessibility, logout.
