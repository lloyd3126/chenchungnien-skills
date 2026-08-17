# Chen Chung Nien Skills

[English](./README.md)

這是一個由 Chen Chung Nien 設計與整理的可重用 agent skills 集合。

這個 repository 主要用來展示我設計與發布的 skills，讓 AI agents 能在特定領域中更穩定地完成任務。

## About

這裡收錄的每個 skill 都以實用性、可維護性與明確邊界為目標，重點不是一次性的 prompt，而是能真正支援持續工作的能力模組。

## 目前收錄的 Skills

| Skill | 說明 |
| :--- | :--- |
| [`tw-gov-data`](skills/tw-gov-data) | 用來探索、檢視、比較與整理台灣政府開放資料平台 `data.gov.tw` 上的資料集。 |
| [`tw-stock-data`](skills/tw-stock-data) | 使用 `tw-stock` CLI 抓取、驗證與分析台灣上市櫃、期貨、選擇權與公開資訊觀測站財務資料。 |
| [`website-skill-builder`](skills/website-skill-builder) | 使用 Codex 內建瀏覽器系統性探索網站，將穩定的網站結構、工作流程與資料模型整理成可重用的 Agent 指引。 |
| [`reuters-news-search`](skills/reuters-news-search) | 透過內建瀏覽器搜尋與篩選 Reuters 最新新聞。 |
| [`reuters-market-data`](skills/reuters-market-data) | 檢視 Reuters Markets 分類、區域分頁、行情表格與延遲的 LSEG 資料。 |
| [`reuters-article-research`](skills/reuters-article-research) | 讀取 Reuters 文章詳情、可見來源脈絡、媒體與存取狀態。 |
| [`tabelog-search`](skills/tabelog-search) | 在 Codex 內建瀏覽器中搜尋與篩選 Tabelog 公開餐廳資料，包含使用自動完成選取地區與驗證搜尋結果。 |
| [`tabelog-restaurant`](skills/tabelog-restaurant) | 透過內建瀏覽器查看 Tabelog 餐廳頁面，以及菜單、照片、評論、評分、地圖與空位等相關頁面。 |
| [`koding-school-learning`](skills/koding-school-learning) | 透過內建瀏覽器瀏覽 koding.school 課程、已加入課程篩選、課程詳情與 lesson 頁型。 |
| [`koding-school-community`](skills/koding-school-community) | 閱讀 koding.school 知識點，並安全搜尋課程討論與回覆。 |
| [`koding-school-projects`](skills/koding-school-projects) | 唯讀瀏覽登入後的 koding.school 作品、工作室、履歷、收信匣與帳號入口。 |
| [`statementdog-stock-analysis`](skills/statementdog-stock-analysis) | 透過內建瀏覽器查看財報狗個股頁、健診、財務指標、估值、籌碼、產品、題材與相關新聞。 |
| [`statementdog-screening`](skills/statementdog-screening) | 建立與驗證財報狗自訂選股、策略清單、指標排行榜、排序、分頁與比較流程。 |
| [`statementdog-market`](skills/statementdog-market) | 探索財報狗大盤、產業、題材、新聞、網誌與產業報告頁面。 |
| [`statementdog-watchlist`](skills/statementdog-watchlist) | 唯讀檢視登入後的財報狗追蹤動態、追蹤股組合與帳號區域。 |
| [`x-home-feed`](skills/x-home-feed) | 在內建瀏覽器中唯讀檢視 X 首頁的推薦、正在跟隨與自訂時間軸。 |
| [`x-profile`](skills/x-profile) | 檢視 X 個人頁、貼文／回覆／轉發／媒體分頁與個人頁入口。 |
| [`x-search`](skills/x-search) | 使用 X 搜尋 autocomplete，並驗證熱門、最新、人物、媒體與列表結果。 |
| [`x-post`](skills/x-post) | 檢視 X 貼文、對話、引用內容、媒體與可用的貼文分析。 |

## 網站專用指引

[Tabelog 網站套件](sites/tabelog/AGENTS.md)提供 Tabelog skills 共用的導覽、session、資料新鮮度與驗證原則；[references](sites/tabelog/references)則記錄探索過的 sitemap 階層、資料模型與網站第一方說明。

[X 網站套件](sites/x/AGENTS.md)提供 X skills 共用的導覽、搜尋 autocomplete、貼文／個人頁資料模型、session 與安全邊界；[references](sites/x/references)記錄已驗證頁型與互動規則。

[財報狗網站套件](sites/statementdog/AGENTS.md)提供四個財報狗 skills 共用的導覽、登入、資料新鮮度與驗證原則；[references](sites/statementdog/references)則記錄網站地圖、資料模型、表單控制項與網站第一方說明。
[`Reuters 網站套件`](sites/reuters/AGENTS.md)提供 Reuters skills 共用的公開導覽、sitemap、搜尋、Markets、文章、資料新鮮度、來源與安全操作指引；[`references`](sites/reuters/references)記錄路由地圖、資料模型、控制項、第一方說明與 Agent 可用性情境。

[橘蘋學習平台網站套件](sites/koding-school/AGENTS.md)提供 koding.school skills 共用的導覽、公開／登入狀態、安全邊界與資料新鮮度規則；各 skill 的 references 記錄已驗證的課程、討論、作品與工作室頁型。

## 使用方式

當某個網站需要成為未來 Agent 可反覆使用的工具時，使用 `website-skill-builder`。它會從 Codex 內建瀏覽器目前開啟的分頁開始，若網站提供 sitemap 就優先使用，先完成不需登入的功能；若目前分頁已明確顯示登入狀態，就直接安全地探索登入後功能，否則才詢問是否要手動登入並繼續探索受保護功能。

處理 Tabelog 搜尋任務時使用 `tabelog-search`，查看餐廳詳細資料與子頁面時使用 `tabelog-restaurant`。未來 Agent 應將即時網站 UI 與說明文件和這些檔案比對，並在工作區可寫入時，自主更新已驗證的穩定差異。

處理 X 任務時，依意圖使用 `x-home-feed`、`x-profile`、`x-search` 或 `x-post`。未來 Agent 應將即時 X UI 與 `sites/x/AGENTS.md` 比對，並保留搜尋、貼文與帳戶資料的動態性。

處理 Reuters 任務時，站內搜尋與篩選使用 `reuters-news-search`，Markets、行情、表格與區域分頁使用 `reuters-market-data`，文章詳情與來源脈絡使用 `reuters-article-research`。目前標題、結果數量、文章內容、排名、價格、殖利率與帳戶資料都必須動態重新取得，並在 Save、Share、Subscribe、帳號或購買操作前停止。
處理財報狗任務時，依意圖使用 `statementdog-stock-analysis`、`statementdog-screening`、`statementdog-market` 或 `statementdog-watchlist`。未來 Agent 應將即時 UI 與 `sites/statementdog/AGENTS.md` 比對，並保留財務數值、排行榜、文章、市場資料與帳號資料的動態性。

處理 koding.school 任務時，課程與 lesson 使用 `koding-school-learning`，知識點與討論使用 `koding-school-community`，作品／工作室／帳號入口使用 `koding-school-projects`。目前進度、作品紀錄、訊息與其他帳戶資料都必須保留為動態且私人資訊。

## Installation

你可以使用 [Vercel skills CLI](https://skills.sh/docs/cli) 來瀏覽與安裝這個 repository 內的 skills。

### Using Vercel skills CLI

```sh
# 互動式瀏覽並安裝這個 repo 內的 skills。
npx skills add lloyd3126/chenchungnien-skills --list

# 全域安裝指定 skill。
npx skills add lloyd3126/chenchungnien-skills --skill tw-gov-data --global
npx skills add lloyd3126/chenchungnien-skills --skill tw-stock-data --global
npx skills add lloyd3126/chenchungnien-skills --skill website-skill-builder --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-search --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-restaurant --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-stock-analysis --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-screening --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-market --global
npx skills add lloyd3126/chenchungnien-skills --skill statementdog-watchlist --global
npx skills add lloyd3126/chenchungnien-skills --skill x-home-feed --global
npx skills add lloyd3126/chenchungnien-skills --skill x-profile --global
npx skills add lloyd3126/chenchungnien-skills --skill x-search --global
npx skills add lloyd3126/chenchungnien-skills --skill x-post --global
```
