# 表單與控制項

以下名稱來自已驗證的可見 DOM／ARIA 名稱。使用時先重新取得當前 DOM；不要把本文件的 selector 當成繞過 UI 的固定 API。

## 法規一欄式查詢

入口：`https://legal.judicial.gov.tw/FLAW/default.aspx`

- `textbox` accessible name：`檢索字詞`。
- placeholder：`可輸入法規名稱、舊法規名稱、法規簡稱、全文檢索字詞`。
- `button`：`送出查詢`。
- `link`：`檢索字詞說明`，連到 `../readme.aspx?ot=in#textHelp`。
- 進階連結：`更多條件查詢`，連到 `Default_AD.aspx`。

頁面說明的安全代表詞包含 `民訴法` 與含條號的格式；使用時仍要以當前結果頁驗證。

## 法規進階查詢

入口：`https://legal.judicial.gov.tw/FLAW/Default_AD.aspx`

- `textbox`：`檢索字詞`。
- `checkbox`：`法規名稱`、`條文內容`。
- `checkbox`：`現行有效`、`廢止`。
- 日期欄位：`開始日期的年度`、`開始日期的月份`、`開始日期的日`、`結束日期的年度`、`結束日期的月份`、`結束日期的日`。
- `button`：`送出查詢`、`清除重填`。
- 返回簡易查詢：`一欄式簡易查詢`。

日期與 checkbox 條件應只在使用者明確提出時設定；送出後確認結果 heading 和實際結果，不以按鈕無錯誤作為成功證據。

## 判解函釋一欄式查詢

入口：`https://legal.judicial.gov.tw/FINT/default.aspx`

- `textbox` accessible name：`檢索字詞`。
- placeholder：`可輸入法院名稱、裁判案號、案由、全文檢索字詞`。
- `button`：`送出查詢`。
- `link`：`檢索字詞說明`。
- 進階連結：`更多條件查詢`，連到 `Default_AD.aspx`。

站方提供的公開格式示例包括 `91台上1926` 與 `台東地院101訴225`；它們說明案號／法院名稱可作為簡易查詢輸入，但不代表任何固定結果筆數。

## 判解函釋進階查詢

入口：`https://legal.judicial.gov.tw/FINT/Default_AD.aspx`

可見控制包括：

- `textbox`：`檢索字詞`、`案由`、`年度`、`字`、`起始號`，以及開始／結束的 `年`、`月`、`日`。
- `checkbox`：資料態樣分群，包括憲法、司法解釋、民事、家事、刑事、行政、其他及其子項。
- `combobox`：`常用字別`。
- `button`：`送出查詢`、`清除重填`。
- `link`：`一欄式簡易查詢`。

資料態樣清單很長，應以當前 DOM 的 accessible name 為準；不要依固定順序或座標勾選。

## 裁判書一欄式查詢

入口：`https://judgment.judicial.gov.tw/FJUD/default.aspx`

- `textbox` accessible name：`檢索字詞`。
- placeholder：`可輸入法院名稱、裁判案號、案由、全文檢索字詞`。
- `button`：`送出查詢`。
- `link`：`檢索字詞說明`。
- 進階連結：`更多條件查詢`，連到 `Default_AD.aspx`。

站方提供的公開格式示例包括 `105訴123` 與 `台北地院105訴123`。一般裁判書查詢結果可按法院、案號年度、案件類別與裁判類別查看側欄分類。

## 裁判書進階查詢

入口：`https://judgment.judicial.gov.tw/FJUD/Default_AD.aspx`

可見控制包括：

- 法院 `listbox`，預設 `所有法院`，另有憲法法庭、最高法院、各級法院及其他法院選項。
- 案件類別 `checkbox`：`憲法`、`民事`、`刑事`、`行政`、`懲戒`；頁面說明未勾選預設為全選。
- 裁判字號：`年度`、常用字別 `combobox`、`字`、`第`、`號`。
- 裁判期間：開始／結束的 `年`、`月`、`日`。
- `textbox`：`裁判案由`、`裁判主文`、`全文內容`、`裁判大小`的下限與上限。
- `button`：`送出查詢`、`清除重填`。

頁面另提供複選法院方式說明、大法庭專區與行政裁判說明連結。只在使用者明確提供條件時設定進階欄位；法院與案件類別的互動規則不要靠猜測。

## 特殊程序表單

以下三頁的一欄式表單均可見 `檢索字詞`、`送出查詢`、檢索字詞說明與 `更多條件查詢`：

- `/FJUD/defaulte.aspx`：簡易案件；頁面明示查無簡易案件時可回到裁判書查詢單元。
- `/FJUD/defaultk.aspx?ty=E`：除權判決。
- `/FJUD/defaultk.aspx?ty=V`：公示催告裁定。

三者的 placeholder 以當前頁面為準，雖然相似，也不要把一個程序的結果 URL 套到另一個程序。

## 行動版選單

`/LAW_Mobile_SEARCH/default.aspx` 首頁的 `a[href="#nav-menu"]` 是 hamburger 控制項。點擊後應立即取得 DOM／截圖，確認選單已展開，再使用選單上實際可見的行動版 href；不要手動把桌面版大小寫參數改成行動版路由。
