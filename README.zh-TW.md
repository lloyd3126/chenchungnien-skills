# Chen Chung Nien Skills

[English](./README.md)

這是一套經過整理、可重複使用的 agent skills，涵蓋研究資料庫、市場工具、政府服務、社群平台與內容網站，目標是讓 Agent 能可靠且一致地完成實際工作。

每個 skill 都有明確且聚焦的責任；網站套件則集中管理共用的導覽、資料模型、新鮮度、登入狀態、證據與安全規則，讓同一網站下的 skills 維持一致行為。

## 從這裡開始

- 要執行既有任務：從下方領域找到需求，選擇範圍最精準的 skill。
- 要了解整個支援網站：點選套件名稱，開啟該網站共用的 `AGENTS.md` 指引。
- 要把新網站整理成可重用的指引與 skills：使用 `website-skill-builder`。

瀏覽器型 skills 預設依目前可驗證的頁面狀態進行唯讀探索。帳密、session 資料、即時數量與單次搜尋結果不會寫入長期指引；發布、購買、送出、傳訊或變更帳號狀態等操作，都需要明確授權。

## Skills 目錄

目錄先依任務領域分類，再依平台或網站套件分組，最後列出各套件內職責明確的 skills。

[台灣公共資料、法律、教育與圖書館](#台灣公共資料法律教育與圖書館) · [市場、公司與監管研究](#市場公司與監管研究) · [新聞、文章與研究資料庫](#新聞文章與研究資料庫) · [社群、內容發布、學習與在地探索](#社群內容發布學習與在地探索) · [建立網站 Skills](#建立網站-skills)

### 台灣公共資料、法律、教育與圖書館

- **[政府資料開放平臺](sites/data-gov-tw/AGENTS.md)** — 搜尋資料集、檢視 metadata 與資源，或追蹤平台最新消息。

  Skills: [`tw-gov-data`](skills/tw-gov-data) · [`tw-gov-data-search`](skills/tw-gov-data-search) · [`tw-gov-data-dataset`](skills/tw-gov-data-dataset) · [`tw-gov-data-news`](skills/tw-gov-data-news)

- **台灣市場資料** — 使用 `tw-stock` CLI 抓取與分析 TWSE、TPEX、TAIFEX 與 MOPS 資料。

  Skill: [`tw-stock-data`](skills/tw-stock-data)

- **[TDX 運輸資料流通服務](sites/tdx/AGENTS.md)** — 探索運輸 API，並安全檢視登入後的會員權限、用量與申請紀錄。

  Skills: [`tdx-api-discovery`](skills/tdx-api-discovery) · [`tdx-member-data-access`](skills/tdx-member-data-access)

- **[司法院法學資料檢索](sites/judicial-lawsearch/AGENTS.md)** — 在法規與裁判系統間正確分流，搜尋公開資料並驗證結果頁。

  Skills: [`judicial-lawsearch-routing`](skills/judicial-lawsearch-routing) · [`judicial-lawsearch-legal`](skills/judicial-lawsearch-legal) · [`judicial-lawsearch-judgments`](skills/judicial-lawsearch-judgments)

- **[全國法規資料庫](sites/law-moj/AGENTS.md)** — 搜尋法規、司法資料、法規異動、情境式指引與跨政府網站內容。

  Skills: [`law-moj-law-search`](skills/law-moj-law-search) · [`law-moj-judicial-search`](skills/law-moj-judicial-search) · [`law-moj-news`](skills/law-moj-news) · [`law-moj-smart-search`](skills/law-moj-smart-search) · [`law-moj-cross-government`](skills/law-moj-cross-government)

- **[教育部因材網](sites/adl/AGENTS.md)** — 閱讀公開資源，並安全檢視登入後的教師工作流程。

  Skills: [`adl-public-resources`](skills/adl-public-resources) · [`adl-teacher-workflows`](skills/adl-teacher-workflows)

- **[國中小代理代課教師人才庫](sites/k12ea-ptst/AGENTS.md)** — 查找目前職缺，並閱讀公開的招募指引與公告。

  Skills: [`k12ea-ptst-job-search`](skills/k12ea-ptst-job-search) · [`k12ea-ptst-public-resources`](skills/k12ea-ptst-public-resources)

- **[國立公共資訊圖書館](sites/nlpi/AGENTS.md)** — 搜尋網站與活動、查找數位資源，並唯讀檢視會員服務。

  Skills: [`nlpi-site-search`](skills/nlpi-site-search) · [`nlpi-activity-search`](skills/nlpi-activity-search) · [`nlpi-digital-resources`](skills/nlpi-digital-resources) · [`nlpi-member-center`](skills/nlpi-member-center)

### 市場、公司與監管研究

- **[Google 財經](sites/google-finance/AGENTS.md)** — 研究報價與比較、財報行事曆、財務報表與持有資產揭露。

  Skills: [`google-finance-market-research`](skills/google-finance-market-research) · [`google-finance-earnings`](skills/google-finance-earnings)

- **[Koyfin](sites/koyfin/AGENTS.md)** — 監測市場、辨識證券、研究公司，並唯讀檢視個人工作區。

  Skills: [`koyfin-market-monitoring`](skills/koyfin-market-monitoring) · [`koyfin-security-research`](skills/koyfin-security-research) · [`koyfin-advanced-search`](skills/koyfin-advanced-search) · [`koyfin-watchlists-and-screens`](skills/koyfin-watchlists-and-screens)

- **[財報狗](sites/statementdog/AGENTS.md)** — 分析公司、篩選股票、探索市場、檢視追蹤清單，並將報告轉為可重現研究。

  Skills: [`statementdog-stock-analysis`](skills/statementdog-stock-analysis) · [`statementdog-screening`](skills/statementdog-screening) · [`statementdog-market`](skills/statementdog-market) · [`statementdog-watchlist`](skills/statementdog-watchlist) · [`statementdog-stock-research`](skills/statementdog-stock-research)

- **[Seeking Alpha](sites/seeking-alpha/AGENTS.md)** — 研究單一證券、建立股票或 ETF 篩選，或調查整體市場新聞與行事曆。

  Skills: [`seeking-alpha-stock-analysis`](skills/seeking-alpha-stock-analysis) · [`seeking-alpha-screening`](skills/seeking-alpha-screening) · [`seeking-alpha-market-research`](skills/seeking-alpha-market-research)

- **[SEC.gov](sites/sec/AGENTS.md)** — 搜尋 EDGAR filings，並監測目前 SEC 新聞、規則制定、活動與公開意見案件。

  Skills: [`sec-filings-research`](skills/sec-filings-research) · [`sec-regulatory-monitoring`](skills/sec-regulatory-monitoring)

- **[FRED](sites/fred/AGENTS.md)** — 查找經濟數據序列與觀測值，或檢視資料發布時程與行事曆。

  Skills: [`fred-series-data`](skills/fred-series-data) · [`fred-release-calendar`](skills/fred-release-calendar)

- **[AnnualReports.com](sites/annualreports/AGENTS.md)** — 尋找公司，並驗證目前或歷年年報連結與格式。

  Skills: [`annualreports-search`](skills/annualreports-search) · [`annualreports-company`](skills/annualreports-company)

### 新聞、文章與研究資料庫

- **[Reuters](sites/reuters/AGENTS.md)** — 搜尋新聞、檢視市場資料，並連同來源與存取狀態閱讀文章詳情。

  Skills: [`reuters-news-search`](skills/reuters-news-search) · [`reuters-market-data`](skills/reuters-market-data) · [`reuters-article-research`](skills/reuters-article-research)

- **[GlobeNewswire](sites/globenewswire/AGENTS.md)** — 搜尋公開新聞稿、檢視新聞稿詳情，並查找 RSS 或 ATOM feeds。

  Skills: [`globenewswire-search`](skills/globenewswire-search) · [`globenewswire-release`](skills/globenewswire-release) · [`globenewswire-rss`](skills/globenewswire-rss)

- **[PR Newswire](sites/pr-newswire/AGENTS.md)** — 尋找並驗證新聞稿、組織、多媒體、產品、資源與 RSS 指引。

  Skills: [`pr-newswire-search`](skills/pr-newswire-search) · [`pr-newswire-news`](skills/pr-newswire-news) · [`pr-newswire-resources`](skills/pr-newswire-resources)

- **[曼報 Pro](sites/manny-pro/AGENTS.md)** — 閱讀網站內容、抽取可重用的商業方法、執行公司研究，並將方法對接財報狗證據。

  Skills: [`manny-pro-content`](skills/manny-pro-content) · [`manny-pro-methodology`](skills/manny-pro-methodology) · [`manny-pro-research`](skills/manny-pro-research) · [`manny-pro-statementdog-bridge`](skills/manny-pro-statementdog-bridge)

- **[Paul Graham](sites/paul-graham/AGENTS.md)** — 尋找與比較文章，或查閱書籍、程式語言專案、FAQ、feeds 等參考頁。

  Skills: [`paul-graham-essay-research`](skills/paul-graham-essay-research) · [`paul-graham-reference-research`](skills/paul-graham-reference-research)

- **[Web of Science](sites/webofscience/AGENTS.md)** — 搜尋文獻與引用參考資料、查找研究者，並檢視登入後的個人檔案與指標。

  Skills: [`wos-document-search`](skills/wos-document-search) · [`wos-researcher-search`](skills/wos-researcher-search) · [`wos-researcher-profile`](skills/wos-researcher-profile)

### 社群、內容發布、學習與在地探索

- **[X](sites/x/AGENTS.md)** — 閱讀首頁動態、個人頁、搜尋、貼文、對話、媒體與可用分析資料。

  Skills: [`x-home-feed`](skills/x-home-feed) · [`x-profile`](skills/x-profile) · [`x-search`](skills/x-search) · [`x-post`](skills/x-post)

- **[Threads](sites/threads/AGENTS.md)** — 搜尋公開內容、檢視個人頁與貼文，或唯讀查看登入後的動態、洞察報告與訊息介面。

  Skills: [`threads-search`](skills/threads-search) · [`threads-profile`](skills/threads-profile) · [`threads-post`](skills/threads-post) · [`threads-activity`](skills/threads-activity) · [`threads-insights`](skills/threads-insights) · [`threads-messages`](skills/threads-messages)

- **[Facebook](sites/facebook/AGENTS.md)** — 安全導覽 Facebook、搜尋各類公開結果，並在不互動的前提下檢視 Marketplace 商品。

  Skills: [`facebook-navigation`](skills/facebook-navigation) · [`facebook-search`](skills/facebook-search) · [`facebook-marketplace`](skills/facebook-marketplace)

- **[vocus](sites/vocus/AGENTS.md)** — 搜尋與閱讀內容、沙龍及商品，或唯讀檢視 Salon Studio。

  Skills: [`vocus-search`](skills/vocus-search) · [`vocus-content-reader`](skills/vocus-content-reader) · [`vocus-salon`](skills/vocus-salon) · [`vocus-product`](skills/vocus-product) · [`vocus-studio`](skills/vocus-studio)

- **[koding.school](sites/koding-school/AGENTS.md)** — 瀏覽課程與 lessons、閱讀社群討論，並安全檢視作品或工作室。

  Skills: [`koding-school-learning`](skills/koding-school-learning) · [`koding-school-community`](skills/koding-school-community) · [`koding-school-projects`](skills/koding-school-projects)

- **[PokecaBook](sites/pokecabook/AGENTS.md)** — 搜尋寶可夢集換式卡牌內容、研究文章與賽事，並比較牌組或卡牌採用率。

  Skills: [`pokecabook-site-search`](skills/pokecabook-site-search) · [`pokecabook-content-research`](skills/pokecabook-content-research) · [`pokecabook-deck-analytics`](skills/pokecabook-deck-analytics)

- **[Tabelog](sites/tabelog/AGENTS.md)** — 搜尋餐廳，並檢視餐廳詳情、菜單、照片、評論、地圖與空位。

  Skills: [`tabelog-search`](skills/tabelog-search) · [`tabelog-restaurant`](skills/tabelog-restaurant)

### 建立網站 Skills

- **Website skill builder** — 系統性探索網站、整理穩定行為與資料結構，並建立可維護的網站指引與聚焦 skills。

  Skill: [`website-skill-builder`](skills/website-skill-builder)

## Repository 結構

```text
skills/<skill-name>/SKILL.md          聚焦的任務指引
skills/<skill-name>/agents/           Agent metadata（若有提供）
sites/<site>/AGENTS.md                網站共用操作指引
sites/<site>/references/              穩定的路由、控制項與資料模型
```

即時頁面內容仍是動態資料。這個 repository 記錄的是可重複使用的操作知識，不是快取答案或私人 session 資料。

## 安裝

使用 [Vercel skills CLI](https://skills.sh/docs/cli) 瀏覽與安裝 skills：

```sh
# 瀏覽這個 repository 內所有可安裝的 skills。
npx skills add lloyd3126/chenchungnien-skills --list

# 全域安裝一個 skill；名稱可替換成上方任何已連結的 skill。
npx skills add lloyd3126/chenchungnien-skills --skill wos-document-search --global
```
