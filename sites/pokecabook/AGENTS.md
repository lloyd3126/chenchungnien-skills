# PokecaBook 網站操作指引

## Scope

這份指引適用於透過 Codex 內建瀏覽器探索公開的 `https://pokecabook.com/`。網站以日文提供 Pokémon Card 的牌組、賽事結果、環境分析、卡片清單、專欄與規則解說。頁面內容、排名、日期、結果與搜尋排序會變動，未來任務必須重新讀取目前頁面。

## Global routing

- 關鍵字找文章、牌組、賽事、卡片或規則 → `$pokecabook-site-search`。
- 用日期、類別、名次、都道府縣、卡片名稱／張數篩選牌組或卡片採用率 → `$pokecabook-deck-analytics`。
- 閱讀分類、文章、牌組索引、賽事彙整、Tier、卡片清單或規則內容 → `$pokecabook-content-research`。
- 詳細路由與頁型見 [site-map.md](references/site-map.md)。

## Sitemap-assisted inventory

- 可見 HTML 網站地圖：`/sitemap`，包含固定頁面、投稿一覧與カテゴリー。
- `/sitemap_index.xml` 已在目前瀏覽器中確認為 PokecaBook `404 NOT FOUND`。
- `/robots.txt` 與 `/sitemap.xml` 在目前 in-app browser 連續導覽時回報 `net::ERR_BLOCKED_BY_CLIENT`；這是瀏覽器控制／客戶端阻擋證據，不代表檔案內容為空或不存在。
- 不要複製網站地圖的完整歷史文章清單；用它確認入口，再從分類、搜尋或代表性文章做有限度探索。

## Global routing and navigation

| 用途 | 路由 |
|---|---|
| 首頁 | `/` |
| 站內搜尋 | `/?s=<URL-encoded keyword>`；可見表單欄位為 `name="s"` |
| 網站地圖 | `/sitemap` |
| 投稿列表 | `/post` |
| 賽事總列表 | `/archives/category/tournament` |
| 賽事子分類 | `/archives/category/tournament/city-league`、`jim-battle`、`champions`、`extra` |
| 牌組、卡片、專欄、規則 | `/archives/category/deck-recipe`、`card-list`、`column`、`beginner` |
| 牌組篩選 | `/deckshow` |
| 卡片採用率 | `/card-adoption-rate` |
| 環境牌組索引 | `/archives/1417` |
| Tier／環境文章 | `/archives/26148` |
| 官方結果彙整 | `/archives/30272` |
| 聯絡、隱私、準備中 | `/inquiries`、`/privacy-policy`、`/preparation` |

共享選單的可見標籤包括 `大会結果まとめ`、`シティリーグ`、`ジムバトル`、`チャンピオンズリーグ`、`エクストラ【Expanded】`、`デッキレシピ`、`カードリスト`、`ポケカコラム`、`ルール【裁定解説】` 與 `検索`。

## Operating rules

- 只使用 Codex 內建瀏覽器目前的同一個分頁；不要建立臨時分頁、切換到外部瀏覽器、使用 web search、API、爬蟲、cookies、local storage 或 session 檔案。
- 以目前可見 UI、同源連結與頁面 DOM 為準。安全互動限於搜尋、分類分頁、目錄錨點、條件篩選、取消與讀取；不要送出留言、聯絡、社群分享、發布或帳戶資料變更。
- 文章中的 X、LINE、`pokemon-card.com` 牌組代碼、Google 等外部連結不屬於一般公開探索範圍；需要外部來源時先確認範圍。
- 搜尋與兩個分析頁的結果是動態的；保留查詢條件並重新驗證，不要把當前數值寫進 skills 或 references。
- 遇到 CAPTCHA、安全攔截、登入牆或無法判斷的第三方流程，記錄邊界並停止該分支，不嘗試繞過。

## Validation and freshness

導覽或篩選後至少確認兩項：頁面 title／主要 heading、目前 URL、選取條件、結果卡片／表格、分頁或明確空結果。`deckshow` 與 `card-adoption-rate` 會以 AJAX 顯示 `読み込み中...`，必須等載入結束後再判斷。

目前探索未看到登入／帳戶入口；`/inquiries` 要求透過網站 X 帳號 DM 聯絡，`/privacy-policy` 提及 Google reCAPTCHA。尚未探索任何登入後分支，不要假設其行為。

## Drift maintenance

每次使用前先對照目前頁面的標籤、路由、欄位、文章目錄與結果模型。穩定結構改變時，更新負責的 AGENTS、skill 或 reference，記錄日期、原行為、目前行為與證據來源，再重跑一條受影響的安全流程與 validator。單次排名、文章內容、日期、結果數量或卡片清單變動只需重新抓取，不要更新成固定值。

## References

- [site-map.md](references/site-map.md)：公開頁型、路由、實體關係與已知限制。
- [search-results.md](../../skills/pokecabook-site-search/references/search-results.md)：站內搜尋細節。
- [filter-controls.md](../../skills/pokecabook-deck-analytics/references/filter-controls.md)：牌組／卡片採用率條件欄位。
- [page-types.md](../../skills/pokecabook-content-research/references/page-types.md)：文章與分類頁 extraction model。
