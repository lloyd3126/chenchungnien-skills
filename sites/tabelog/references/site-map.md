# Tabelog 公開 site map

探索基準：2026-08-16，透過 Codex 內建瀏覽器完成。頁面上的數量、排名、價格、空席與目前日期不寫死；以下只保留可重複使用的結構與路由。

## Coverage

| 區域 | 代表入口 | 狀態 | 可重用知識 |
|---|---|---|---|
| 首頁 | `/` | explored + second-pass checked | 搜尋表單、地區／料理／場景／條件入口、排名、百名店、說明與頁尾 |
| 公開搜尋 | `/rst/rstsearch/` → `/rstLst/` | explored | 地區／關鍵字搜尋，日期、時間、人數，結果列表與 pagination |
| 結果篩選 | `/rstLst/` | explored | 預算下限／上限、營業時段、場景、設備、支付等條件；絞り込む／詳細条件 |
| 都道府縣／區域索引 | `/tokyo/`、`/tokyo/A1316/` | representative explored | 層級式地區、區域排名與餐廳列表入口 |
| 全國排名 | `/rank/` | representative explored | 總合與料理ジャンル TOP20；數值須現場重查 |
| 餐廳詳情 | `/<area>/<restaurant-id>/` | explored | 基本資料、評分、預算、口コミ數、保存／行った／投稿入口、子頁 tabs |
| 座席 | `.../table/` | explored | 座位圖片／說明、座席預約入口、詳細店舖資訊 |
| 菜單／課程 | `.../dtlmenu/` | explored | 課程、料理、飲料、午餐、照片分頁與品項價格／描述 |
| 照片 | `.../dtlphotolst/...` | explored | 官方／使用者照片、分類、排序、尺寸切換、分頁 |
| 口コミ | `.../dtlrvwlst/` | explored | 口コミ搜尋、全部／夜／午餐、排序、顯示筆數、作者與評分 |
| 評分分布 | `.../dtlratings/` | explored | 各評分維度平均、分布、利用金額分布與方法論連結 |
| 地圖 | `.../dtlmap/` | explored | 地址、交通方式、Google 地圖區域、周邊店舖入口 |
| 官方說明 | `/help/beginner/`、`/help/r_about_review/`、`/help/review_guide/` | explored | 網站定位、口コミ定義、投稿規範與限制 |
| 登入 | `/account/login/` | public shell explored; protected branch pending | 顯示註冊／登入方式；未執行第三方登入 |

## Sitemap hierarchy

Tabelog's visible `サイトマップ` is a hierarchical public index rather than a flat XML inventory:

```text
/sitemap/
  → /sitemap/<prefecture>/
    → /sitemap/<prefecture>/<area-code>-<subarea-code>/
      → /sitemap/.../<kana>/
        → restaurant detail URL
```

The national index links prefectures; the Tokyo index links area names; a representative Ginza area index links Japanese gojūon branches; a gojūon branch contains restaurant detail URLs. Counts shown on these pages are dynamic and should not be copied into skills. Use the index to choose representative routes, not to open every restaurant.

## Homepage routing

- `エリアから探す`：都道府縣、主要城市、區域與車站層級。
- `料理ジャンルから探す`：料理類別列表，通往 genre list 或 ranking。
- `特集`、`利用シーンから探す`、`こだわり条件から探す`：以內容、場景或條件進入列表。
- `The Tabelog Award`、`百名店`、`ジャンル別ランキング`：策展／排名入口，內容與排名會更新。
- `ユーザーを探す`：使用者名稱查找入口；未深入操作帳號／個人資料分支。
- 頁尾提供預約確認、help、口コミ／排名政策、口コミガイドライン、sitemap、keywords、chain list 及語言入口。

## Verified public interactions

1. 首頁搜尋欄可輸入區域／車站與關鍵字；以 `銀座駅` + `焼肉` 建立公開結果列表。
2. 只輸入地區文字而不選 autocomplete 建議時，頁面顯示區域不存在並 fallback 到全國 genre list；選取 `銀座駅` 後，heading 與 URL 都限定到該車站／區域。
3. 結果頁的預算下限選單選為 `￥3,000` 後，heading 顯示夜間 ￥3,000 以上的條件摘要。
4. 結果頁的營業時段選單選為 `ランチ` 後，heading 顯示午餐條件摘要。
5. 結果頁可見分頁、排序／顯示切換與多個條件入口；實際操作只涵蓋安全的預算與營業時段篩選。
6. 餐廳詳情 tabs 可進入座席、菜單、照片、口コミ、評分分布與地圖；每頁都重新讀取目前 DOM。
7. 口コミ頁提供關鍵字搜尋、全部／夜／午餐分支、標準／訪問月順／いいね順與 20／50／100 筆顯示選項；未發佈或互動口コミ。

## Auth boundary

公開頁面普遍顯示 `保有Vポイント`、`行ったお店`、`保存リスト` 與 `無料会員登録/ログイン`。餐廳詳情的 `行った`、`保存`、`投稿` 和照片投稿也導向登入或可能需要登入。登入頁公開顯示註冊流程與 LINE、Google、Yahoo! JAPAN ID、X、Apple、価格.com ID、docomo ID、au ID、My SoftBank 認證入口。

尚未確認：任何第三方認證、登入後導覽、收藏／已去過清單、投稿編輯器、個人化推薦、會員專屬排名或預約帳戶功能。要探索時，先取得使用者同意，再請使用者在同一個內建瀏覽器分頁手動登入，並重新走過上表所有已探索公開區域。

## Intentionally untested

- 實際網路預約、送出預約、付款或外部 `yoyaku.tabelog.com` 流程。
- 發佈／編輯／刪除口コミ與照片。
- `行った`、`保存`、追蹤レビュアー與其他會改變帳戶資料的操作。
- CAPTCHA、安全攔截或第三方登入頁的繞過。
