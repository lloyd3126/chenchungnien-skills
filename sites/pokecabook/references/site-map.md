# PokecaBook 公開 site map

探索基準：2026-08-17，使用 Codex 內建瀏覽器目前分頁完成。以下只保留可重複使用的公開結構；文章內容、日期、排名、卡片、結果與 pagination 數值必須現場重查。

## Coverage

| 區域 | 代表入口 | 狀態 | 可重用知識 |
|---|---|---|---|
| 首頁與共享選單 | `/` | explored + visual/DOM checked | 網站定位、搜尋、分類與頁尾入口 |
| HTML 網站地圖 | `/sitemap` | DOM/interaction checked | 固定頁面、投稿列表、分類入口；不做全量爬取 |
| 公開站內搜尋 | `/?s=<keyword>` | explored + visual/DOM checked | GET 關鍵字搜尋、結果卡片、分頁 |
| 賽事分類 | `/archives/category/tournament` | explored | 總賽事列表與分頁 |
| 賽事子分類 | `/archives/category/tournament/city-league`、`jim-battle`、`champions`、`extra` | representative explored | 城市聯賽、道館賽、冠軍聯賽、Expanded |
| 牌組／卡片／專欄／規則分類 | `/archives/category/deck-recipe`、`card-list`、`column`、`beginner` | explored | 分類文章卡片、日期、詳情路由、分頁 |
| 投稿列表 | `/post` | DOM checked | 按時間排列的公開文章與分頁 |
| 牌組篩選 | `/deckshow` | visual/DOM/interaction checked | 條件 modal、牌組篩選、AJAX 結果／空結果 |
| 卡片採用率 | `/card-adoption-rate` | visual/DOM/interaction checked | 條件 modal、採用率結果／空結果 |
| 環境牌組索引 | `/archives/1417` | representative explored | 牌組 archetype 連到文章詳情 |
| Tier／環境分析 | `/archives/26148` | visual/DOM checked | 動態更新日期、Tier headings、解說與牌組／採用率入口 |
| 卡片清單文章 | `/archives/323482` | DOM checked | 發售日、TOC、卡片名稱、效果／招式文字 |
| 官方結果彙整 | `/archives/30272` | DOM checked | 季度、環境、賽事文章與名次／牌組連結 |
| 公開輔助頁 | `/inquiries`、`/privacy-policy`、`/preparation` | DOM checked | 聯絡邊界、隱私聲明、準備中頁 |

## Page taxonomy

```text
category/list → article → TOC section → deck/event/card entity
ranking article → environment deck index → recipe/detail article
tournament roundup → season/environment → event result article → deck entry
card-list category → set article → card section
```

分類列表通常有文章卡片、類別標籤、日期與 `次のページ`／頁碼／`次へ`。文章詳情通常有 title、日期、X/LINE 分享連結、`#tocN` 目錄、section headings、圖像或文字內容、留言區與頁尾。外部 Pokémon 官方牌組代碼頁面是獨立來源，不等同於 PokecaBook 文章中的整理。

## Sitemap and evidence limits

- 可見 `/sitemap` 是 HTML 網站地圖；固定頁面可見 `HOME`、`お問合せ`、`デッキレシピ検索`、`プライバシーポリシー`、`投稿一覧`、`準備中` 與採用率頁。
- `/sitemap_index.xml` 在同一分頁實際顯示 PokecaBook `404 NOT FOUND`。
- `/robots.txt`、`/sitemap.xml` 在同一分頁導覽時回報 `net::ERR_BLOCKED_BY_CLIENT`；沒有讀到檔案內容，不可推論沒有 robots 或 XML sitemap。
- 首頁、搜尋、牌組 modal 與 Tier 文章有成功 current-tab visual 證據；網站地圖、分類、輔助頁與部分文章以 current-tab DOM/interaction 證據為主。多個截圖請求曾逾時，這些控制錯誤不視為頁面內容證據。
- 未看到登入／帳戶分支。`/inquiries` 指向 X DM；`/privacy-policy` 說明隱私、Analytics 與 reCAPTCHA。未測試任何登入後或不可逆功能。

## Freshness rule

本檔案只記結構。當使用者問目前環境、排名、賽事結果、發售日、卡片文字或採用率時，重新開啟相應頁面並記錄查詢日期、頁面 title、主要 heading 與證據來源；不依賴本檔案中的舊內容。
