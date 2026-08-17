# Chen Chung Nien Skills

[English](./README.md)

這是一套經過整理、可重複使用的 agent skills，涵蓋研究資料庫、市場工具、政府服務、社群平台與內容網站，目標是讓 Agent 能可靠且一致地完成實際工作。

每個 skill 都有明確且聚焦的責任；網站套件則集中管理共用的導覽、資料模型、新鮮度、登入狀態、證據與安全規則，讓同一網站下的 skills 維持一致行為。

## 從這裡開始

- 要執行既有任務：從下方領域找到需求，選擇範圍最精準的 skill。
- 要了解整個支援網站：點選套件名稱，開啟該網站共用的 `AGENTS.md` 指引。
- 要把新網站整理成可重用的指引與 skills：使用 `website-skill-builder`。
- 要比較已確認的覆蓋範圍與剩餘缺口：使用套件前先讀取[流程驗證狀態](#流程驗證狀態)。

瀏覽器型 skills 預設依目前可驗證的頁面狀態進行唯讀探索。帳密、session 資料、即時數量與單次搜尋結果不會寫入長期指引；發布、購買、送出、傳訊或變更帳號狀態等操作，都需要明確授權。

## 流程驗證狀態

這裡集中列出各網站套件已明確記錄的證據與缺口。`已驗證` 表示至少一條代表性唯讀路徑具有目前分頁的 UI 或 DOM／interaction 證據；不代表所有資料、權限變體或動態值都已測試。`未驗證` 或 `partial` 表示流程未能在當時可用的 Codex 內建瀏覽器 session 中完整走完；**不代表功能無法使用或不存在**。

所有套件中的狀態變更操作——登入／登出、帳號修改、儲存／追蹤、發布、留言、傳訊、表單送出、預約、購買、付款、上傳、建立憑證或 token、CAPTCHA 與第三方授權——均視為刻意未測；除非套件明確記錄已驗證，而且使用者已授權該次操作。

### 台灣公共資料、法律、教育與圖書館：驗證狀態

| 套件 | 已驗證流程 | 未驗證或僅部分驗證的流程 |
| :--- | :--- | :--- |
| [政府資料開放平臺](sites/data-gov-tw/references/site-map.md) | 資料集搜尋、進階篩選、排序與分頁；代表性資料集 metadata 與檔案／API 資源；消息列表與詳細頁。 | `專欄文章` 與統計資料只有路由層級紀錄；登入後留言／帳號功能、RSS payload、外部資源與下載流程未完整探索。 |
| [TDX 運輸資料流通服務](sites/tdx/AGENTS.md) | 公開服務探索、API／OAS 指引、資料標準、供應狀態、統計與資料市集頁；登入後 key、權限、用量、申請與訂閱介面唯讀檢視。 | 個人帳號詳細資料停在密碼驗證門檻；購買、刪除、申請與其他送出流程未執行。 |
| [司法院法學資料檢索](sites/judicial-lawsearch/references/first-party-guidance.md) | 入口分流、公開法規／判解函釋／裁判書搜尋，以及代表性結果與裁判詳細頁。 | 未探索受保護內容；裁判書系統說明頁逾時，因此完整收錄範圍與更新週期仍未驗證。 |
| [全國法規資料庫](sites/law-moj/references/site-map.md) | 中央法規搜尋與全文、司法資料、法規異動公告、智慧查找主題與跨機關搜尋結果頁。 | E 政府登入、最愛法規與自訂資料夾未驗證；部分司法單筆、跨機關、refresh、API 與智慧查找長頁只有 DOM 證據，未完成完整視覺驗證。 |
| [教育部因材網](sites/adl/references/coverage.md) | 公開首頁、消息、活動、操作手冊、FAQ 與網站導覽；初始登入教師 dashboard 及可見任務區域。 | 課程總覽、AI 學伴與完整受保護教師側欄仍需在登入狀態重驗；任務指派、班級／學生修改、匯入、上傳與帳號操作刻意未測。 |
| [國中小代理代課教師人才庫](sites/k12ea-ptst/AGENTS.md) | 公開職缺篩選與連動控制、結果與詳細頁；消息、縣市支援、求職指引、法規、FAQ、關於與網站導覽。 | 登入後履歷、收藏、完整聯絡資料、三招以上資訊、主動應徵、媒合與求才者／管理後台未探索。 |
| [國立公共資訊圖書館](sites/nlpi/AGENTS.md) | 全站搜尋、活動日曆與詳情、數位資源分流，以及會員中心主要 tabs 與服務卡唯讀檢視。 | `myispace`、`myactivity` 回傳網站錯誤，`myebook` 遭 client block；外部會員服務未深入探索，活動的單獨近 7 天／關鍵字篩選也不穩定。 |

### 市場、公司與監管研究：驗證狀態

| 套件 | 已驗證流程 | 未驗證或僅部分驗證的流程 |
| :--- | :--- | :--- |
| [Google 財經](sites/google-finance/AGENTS.md) | 金融實體搜尋與消歧、報價頁、圖表區間與比較；市場瀏覽、財報行事曆、公司收益、財務報表與持有資產揭露。 | 未登入變體仍未確認；研究問題送出、討論串／工作、深度搜尋、觀察清單分析、清單與投資組合建立均未執行。 |
| [Koyfin](sites/koyfin/references/coverage.md) | 證券與逐字稿搜尋；公司摘要、估計、財務、新聞與圖表；市場新聞、異動、指數與行事曆；watchlists、screens、portfolio 與 sample dashboard 唯讀檢視。 | Advisor Tools、其餘 Market Overview 子頁與個別新聞稿／逐字稿頁未驗證；My Graphs 只有 partial 證據。 |
| [財報狗](sites/statementdog/references/site-map.md) | 公司分析頁、自訂選股與排行榜、市場／產業／題材／新聞／報告，以及登入後動態、portfolio 與帳號欄位唯讀檢視。 | 網誌搜尋送出效果未確認，公司比較僅 partial；儲存選股、修改追蹤／帳號、付款與留言未執行。 |
| [Seeking Alpha](sites/seeking-alpha/references/site-map.md) | 公開股票／ETF 頁與研究 tabs、預設 screeners 與結果表、市場／新聞探索、站內搜尋與財報行事曆。 | Portfolio、訂閱、Investing Groups 與帳號相依內容未驗證；自訂 screener 欄位、操作符、排序、reset、儲存與比較未完整測試。 |
| [SEC.gov](sites/sec/AGENTS.md) | 公司／CIK 查詢、EDGAR 全文與最新 filings、filing details、API 指引，以及 Newsroom、rulemaking、活動與 public-comment 頁。 | 登入與 filer-management 分支未探索；filing、public comment、tip／complaint、訂閱、API token、上傳與帳號操作均未送出。 |
| [FRED](sites/fred/references/site-map.md) | 關鍵字／autocomplete 探索、代表性 series metadata 與 observations、圖表／匯出控制，以及 release catalog 與 calendar 日期／排序控制。 | Release／source／category 詳情、帳號功能、Add-in、行動 App、地圖與 ALFRED 未深入探索；Help 詳細面板停在載入 spinner。 |
| [AnnualReports.com](sites/annualreports/references/exploration-checklist.md) | 關鍵字與公司篩選、代表性公司頁、歷年報告展開與格式、Featured Reports、About／FAQ 與表單欄位檢視。 | Current report 目標未在新分頁驗證；分頁／排序、登入變體、外部合作網站、評分、紙本申請、Add Company 與寄送表單仍未驗證或刻意未測。 |

### 新聞、文章與研究資料庫：驗證狀態

| 套件 | 已驗證流程 | 未驗證或僅部分驗證的流程 |
| :--- | :--- | :--- |
| [Reuters](sites/reuters/AGENTS.md) | 站內搜尋、section／日期篩選與排序；Markets 區域 tabs 與行情表；文章 metadata、摘要、可見正文與來源脈絡。 | My News、儲存／追蹤後內容、帳號、註冊／登入、訂閱、付費內容與個人化資料未驗證。 |
| [GlobeNewswire](sites/globenewswire/references/site-map.md) | 首頁／Newsroom 與分類導覽、關鍵字與組織結果、分頁、新聞稿詳情、相關新聞稿與 RSS／ATOM 格式。 | RSS 的 Industry／Location tabs 與主要搜尋篩選的選項／結果仍為 partial；客戶／讀者帳號流程未探索。 |
| [PR Newswire](sites/pr-newswire/AGENTS.md) | 搜尋、新聞稿／分類／組織列表、單篇新聞稿與多媒體，以及公開產品、資源與 RSS 指引頁。 | 受保護的 Amplify workspace 尚未確認；客戶登入、建立帳號、發稿、Demo／Contact、行銷表單、社群分享與 CAPTCHA 刻意未完成。 |
| [曼報 Pro](sites/manny-pro/references/site-map.md) | 公開與登入後文章／集數列表、access tabs、tags、排序、詳細頁、載入更多、方案 FAQ 與 Account Profile 區塊唯讀檢視。 | Account Profile 僅 partial；會員管理、取消訂閱、退款、付款、更改付款資訊、登出與 Apple／Spotify 綁定未測試。 |
| [Paul Graham](sites/paul-graham/references/agent-usability.md) | Essays 列表與 index、文章詳細頁與 Prev／Next，以及公開 Books、Arc／Bel／Lisp／Spam、Responses、FAQ、Quotes、RSS、Bio 與聯絡參考頁。 | 外部 Y Combinator、Amazon、社群／論壇與 feed 目的地未探索；寄信、購買、申請與互動流程刻意未測。 |
| [Web of Science](sites/webofscience/references/exploration-checklist.md) | Smart／fielded／cited-reference search、結果 refinement／sorting／analysis 與 Full Records；研究者搜尋與 profiles；登入後 profile metrics、records 與主要 settings 唯讀檢視。 | Query Builder 的獨立行為、Research Assistant cards、匯出／alerts／marked lists、目前登入 profile 重驗、ORCID syncing、Account Settings、My Records 子頁與出版商／產品頁仍未確認。 |

### 社群、內容發布、學習與在地探索：驗證狀態

| 套件 | 已驗證流程 | 未驗證或僅部分驗證的流程 |
| :--- | :--- | :--- |
| [X](sites/x/references/site-map.md) | 首頁 feed 變體、公開 profiles 與 tabs、搜尋 scopes、貼文／對話詳情、引用內容、媒體與可用貼文 analytics 唯讀檢視。 | 通知、私訊、歷史記錄、帳號設定、Grok、Premium、Creator Studio、Articles、Spaces、廣告、第三方登入與付款未探索。 |
| [Threads](sites/threads/references/site-map.md) | 公開搜尋／topic／profile／post 與 reply sorting；登入後 activity filters、saved／following／ephemeral feeds、inbox／requests，以及 Insights dashboard／代表性 detail 唯讀檢視。 | 指定日期之前／自訂日期／指定 profile 搜尋篩選與 profile-to-author-search 路由未完整驗證；部分 Insights detail 與新訊息流程仍停在 loading skeleton。 |
| [Facebook](sites/facebook/AGENTS.md) | 首頁與導覽選單、全站搜尋 scopes／filters、Games／Groups 入口，以及 Marketplace 搜尋、篩選與商品詳細頁唯讀檢視。 | 社團個人化動態、帳號設定實際變更、訊息、發文／互動、付款與 Marketplace 刊登流程未測試。 |
| [vocus](sites/vocus/AGENTS.md) | 首頁／探索／搜尋／tag、文章／貼文／profile、公開沙龍與商品，以及 Studio 統計、內容、方案、會員、收益與設定唯讀檢視。 | 部分重型 feed／沙龍頁只有 DOM 或 partial 視覺證據；沙龍 room／商品詳情覆蓋為 partial，購買、會員變更、發布與 Studio 寫入操作刻意未執行。 |
| [koding.school](sites/koding-school/references/exploration-checklist.md) | 課程搜尋／篩選／詳情與 lesson 類型；知識點／討論搜尋與 threads；作品、代表性 studio、profile、inbox 列表與帳號入口唯讀檢視。 | 專案編輯器、回收桶、工作室建立／移除、帳號更新、私訊本文、付款、訂單與訂閱仍未驗證。 |
| [PokecaBook](sites/pokecabook/references/site-map.md) | 公開搜尋／分頁、賽事與內容分類、文章／詳細頁結構、牌組篩選、卡片採用率、Tier 與卡片清單頁。 | 未觀察到登入／帳戶分支；透過 X DM 詢問、reCAPTCHA、外部目的地與不可逆流程均未測試。 |
| [Tabelog](sites/tabelog/references/site-map.md) | 餐廳搜尋、地區 autocomplete 與篩選、排序／分頁，以及餐廳詳情、菜單、照片、評論、評分、地圖與空位頁。 | 第三方認證、登入後導覽、收藏／已去過清單、評論編輯器、個人化推薦、會員排名、預約帳戶、實際訂位與付款仍未驗證或刻意未測。 |

證據狀態改變時，應先更新負責的網站套件，再於同一變更中同步更新兩個狀態欄。代表性驗證不等於完整覆蓋；暫時性網站故障與瀏覽器控制錯誤也必須和真正的功能不存在分開記錄。

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
