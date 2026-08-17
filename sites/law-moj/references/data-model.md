# Data model and relationships

本文件把網站 UI 中可辨識的欄位與關聯整理成 Agent 可用的概念模型。值域、數量、日期與搜尋結果都是動態的。

## 核心實體

| 實體 | 穩定欄位／識別 | 主要頁面與關聯 |
| --- | --- | --- |
| 最新訊息 | 日期、類別、摘要、`msgid` | `NewsList.aspx` → `NewsDetail.aspx?msgid=<ID>`；類別可為法律、法規命令、行政規則、地方法規、法規草案 |
| 法規 | `pcode`、法規名稱、位階／類別、制定／修正日期、現行／廢止狀態、可用英文版本 | `LawSearchLaw.aspx` → `LawAll.aspx?pcode=<PCODE>`；名稱連結可能先經 `Hot/AddHotLaw.ashx?PCode=<PCODE>` |
| 條文 | `pcode` + `flno`（條號） | `LawSingle.aspx?pcode=<PCODE>&flno=<N>`；全文頁列出所有條文 |
| 編章節 | `pcode` + `bp`（編章節節點） | `LawAllPara.aspx?pcode=<PCODE>` → `LawParaDeatil.aspx?pcode=<PCODE>&bp=<N>` |
| 條文搜尋結果 | `pcode`、條號或關鍵字、匹配條文 | 條號／條文表單 → `LawSearchContent.aspx`；結果中的高亮文字不是新的識別欄位 |
| 法規沿革 | 法規版本／事件日期、事件描述 | `LawHistory.aspx?pcode=<PCODE>`；沿革日期不要當成目前有效性唯一依據 |
| 司法資料 | `ty`、`JC`、`JNO`、`JYEAR`、`JCASE`、日期、案由、主文、相關法條 | `LawSearchJudge.aspx` → `LawClass/ExContent.aspx?...`；詳細資料也可能連到司法院外部網站 |
| 條約／協定 | `pcode`、名稱、區域、中文／英文版本、修正／資料日期 | `LawSearchAgree.aspx` → `LawAll.aspx?pcode=<PCODE>`；語言範圍以官方說明為準 |
| 兩岸協議 | `pcode`、名稱、日期、附件提示 | `LawSearchTwo.aspx` → `LawAll.aspx?PCODE=<PCODE>` |
| 綜合查詢結果 | 查詢類別、結果分頁（法規名稱／法條內容）、高亮關鍵字 | `LawSearchResult.aspx?ty=Z...`；結果筆數不可硬編碼 |
| 跨機關紀錄 | 機關、標題、命中片段、來源／庫存頁面、擷取語境 | `CrossGov_result.aspx?...`；內容由機關維護，網站週期性擷取 |
| 智慧查找節點 | `T` 主題、`O` 選項／子選項、說明、法規連結 | `SmartSearch/main.aspx` → `Theme.aspx?T=<T>&O=<O>`；不是法規正文的替代品 |
| 會員資料 | E 政府帳號、最愛法規、自訂資料夾 | `Mem/Login.aspx` 後的受保護分支；本輪未驗證 |

## 路由關係

```text
入口／分類清單
  ├─ 法規 → pcode → 全文／編章節／條文／條號查詢／條文查詢／沿革
  ├─ 司法資料 → 判決識別參數 → 單筆內容 → 相關法條／外部司法院頁面
  ├─ 最新訊息 → msgid → 異動詳情 → 可能連到正式公報或機關來源
  ├─ 跨機關 → 機關範圍 + 關鍵字 → 擷取結果 → 庫存頁面／原機關
  └─ 智慧查找 → T/O 路徑 → 情境說明 → 法規與工具連結
```

## Agent 使用原則

- 先從頁面取得實際 `pcode`、`msgid` 或司法識別參數，再導覽到詳細頁；不要猜測參數。
- 「相關法條」與智慧查找的法規連結是導航關係，不代表該頁已完成法律適用分析。
- 搜尋結果的排序、分頁、命中數與熱門主題會變動；只報告本次重新讀到的結果，並保留查詢條件。
- 跨機關結果包含「庫存頁面」與機關來源提示；對這類內容要同時記錄來源機關與資料可能是週期擷取。
