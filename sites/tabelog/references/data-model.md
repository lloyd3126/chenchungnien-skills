# Tabelog 公開資料模型

以下是從公開搜尋結果、餐廳詳情與子頁歸納的穩定結構。數值和可用性不固定，使用時必須重新取得。

## Entities

### Restaurant

核心識別是餐廳詳情 URL 中的 restaurant id。詳情頁可能包含：店名、料理ジャンル、最近車站／區域、地址、交通方式、電話、預約可否、營業時間、預算、付款方式、發票、服務費／チャージ、席數、個室、貸切、禁煙／喫煙、停車場、空間／設備、兒童、服務、官方網站與開店日。

入口：搜尋結果卡片、地區列表、排名、料理／場景／條件列表。主要查看頁：餐廳 top 與 `店舗情報（詳細）`。

### Listing result

搜尋結果是依地區、關鍵字、料理、日期、時間、人數與篩選條件產生的餐廳集合。卡片通常呈現店名、區域、料理、點數、口コミ數、保存數、預算、照片、口コミ片段與可能的網路預約可用性。列表有排序、篩選、顯示筆數／分頁。

### Review

口コミ連結到 reviewer、訪問日期／利用種別、總合分數，以及料理・味、サービス、雰囲気、CP、酒・ドリンク等分項。頁面也可能有照片、いいね、店家回覆與問題回報。口コミ是作者的主觀感想，不是店家的絕對評價；詳見 [first-party-guidance.md](first-party-guidance.md)。

### Menu item / course

`dtlmenu/` 把內容分成 `コース`、`料理`、`ドリンク`、`ランチ`、`写真` 等分頁。品項可能有分類、名稱、價格、描述、標籤與圖片。菜單內容、價格和更新日期需現場確認。

### Photo

照片頁可按全部、料理、飲料、內觀、外觀、其他或官方／使用者來源切換，並支援排序、尺寸與分頁。不要把照片數或圖片內容當成目前營業狀態的保證。

### Rating distribution

`dtlratings/` 顯示公開使用者評分的平均與分布，包含總合及各分項；也可能顯示人均利用金額分布。頁面明確區分使用者簡單平均與店舖顯示的獨自演算法分數，不應混為同一指標。

### Reservation availability

餐廳頁可能顯示指定日期、時間與人數的空席／可預約狀態，以及「予約する」入口。這是高度動態且可能進入外部或不可逆流程的資料；只讀取目前狀態，除非使用者明確要求並確認最後送出。

## Relationships

```text
Search query + filters
        ↓
Listing result ──→ Restaurant ──→ Menu / Seats / Photos / Reviews / Ratings / Map
        │                    └──→ Reservation availability
        └──→ Area / genre / ranking / scene landing pages

Restaurant ──→ Review ──→ Reviewer
Restaurant ──→ Photo
Restaurant ──→ Menu item / Course
Restaurant ──→ Area / Station / Genre
```

## Retrieval rule

先以使用者意圖選搜尋或餐廳 skill，再從目前頁面的可見連結進入下一層。不要依賴某次搜尋結果的店名、排名、價格或口コミ數；將這些視為當次查詢結果並回報查詢條件與時間。
