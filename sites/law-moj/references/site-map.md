# Site map and route inventory

探索範圍：`https://law.moj.gov.tw/`。以下是供 Agent 導覽的路由索引，不是固定的網站內容快照。

## 主要路由

| 功能 | 路由／模式 | 用途 | 探索證據 |
| --- | --- | --- | --- |
| 首頁 | `/` | 全域查詢、最新訊息、功能入口 | 同分頁視覺 + DOM |
| 網站導覽 | `/SiteMap.aspx` | 功能區、快速入口與 access key | 同分頁視覺 + DOM |
| 最新訊息 | `/News/NewsList.aspx?type=all` | 最近一年法規異動 | 同分頁視覺 + DOM；分類與分頁安全測試 |
| 中央法規 | `/Law/LawSearchLaw.aspx` | 憲法、法律、法規命令與組織法規 | 同分頁視覺 + DOM；排序安全測試 |
| 法規全文 | `/LawClass/LawAll.aspx?pcode=<PCODE>` | 顯示法規 metadata 與所有條文 | 同分頁視覺 + DOM |
| 編章節 | `/LawClass/LawAllPara.aspx?pcode=<PCODE>` | 依編、章、節分組 | 同分頁視覺 + DOM |
| 單一條文 | `/LawClass/LawSingle.aspx?pcode=<PCODE>&flno=<N>` | 顯示一個條文與關聯裁判／解釋 | 同分頁視覺 + DOM |
| 條號檢索 | `/LawClass/LawSearchCNKey.aspx?BTNType=NO&pcode=<PCODE>` | 以條號或條號範圍找條文 | 同分頁視覺 + DOM；結果安全測試 |
| 條文檢索 | `/LawClass/LawSearchCNKey.aspx?BTNType=CON&pcode=<PCODE>` | 以含有／且含／或／不含搜尋全文 | 同分頁視覺 + DOM；結果安全測試 |
| 沿革 | `/LawClass/LawHistory.aspx?pcode=<PCODE>` | 顯示修正、制定等沿革 | 同分頁視覺 + DOM |
| 司法解釋 | `/Law/LawSearchJudge.aspx` | 憲法法庭、舊制解釋與最高法院判例 | 同分頁視覺 + DOM |
| 司法單筆 | `/LawClass/ExContent.aspx?...` | 顯示判決／解釋全文與相關法條 | DOM + 互動；截圖重試受客戶端錯誤影響 |
| 條約協定 | `/Law/LawSearchAgree.aspx` | 依地區與名稱／日期查找 | 同分頁視覺 + DOM |
| 兩岸協議 | `/Law/LawSearchTwo.aspx` | 查找兩岸協議 | 同分頁視覺 + DOM |
| 綜合查詢 | `/Law/LawSearchAll.aspx` | 跨類別、名稱／法條、日期或文號查詢 | 同分頁視覺 + DOM；結果安全測試 |
| 綜合結果 | `/Law/LawSearchResult.aspx?...` | 顯示法規名稱與法條內容結果分頁 | 同分頁視覺 + DOM |
| 跨機關 | `/CrossGov/CrossGov.aspx` | 依機關範圍查找擷取內容 | DOM + 互動；表單截圖重試受客戶端錯誤影響 |
| 跨機關結果 | `/CrossGov/CrossGov_result.aspx?...` | 顯示機關、來源與庫存頁面 | 同分頁視覺 + DOM；安全測試 |
| 智慧查找 | `/SmartSearch/main.aspx` | 生活情境分類與熱門案例 | 同分頁視覺 + DOM |
| 智慧查找主題 | `/SmartSearch/Theme.aspx?T=<T>&O=<O>` | 逐層選擇主題、問題與法律資源 | 主題同分頁視覺 + DOM；子選項 DOM，截圖重試受客戶端錯誤影響 |

## 入口與輔助頁

- English：`/Eng/index.aspx`；英文 sitemap、news、law、convention、searching 皆在 `/ENG/` 下。中文版本優先。
- 會員登入：`/Mem/Login.aspx`。本輪只確認入口與未登入畫面，未輸入憑證。
- 官方說明：`/Service/Intro.aspx`、`/Service/LawData.aspx`、`/Service/refresh.aspx`、`/Qanda.aspx`。
- 法律扶助：`/Service/LegalAid.aspx`；屬於外部／工具資源導覽，不是法規核心查詢。
- 相關網站：`/RelatedWebsite.aspx`；屬於外部網站目錄，本輪沒有遞迴探索外部站點。
- Open API 文件：`/api/swagger` 會導向 `/api/swagger/index.html`，並提供 `/api/swagger/docs/v1`；僅作為官方文件入口記錄，除非使用者明確授權，不以 API 取代瀏覽器操作。

## 探索限制與證據分級

- `robots.txt` 以同分頁導覽時得到 `net::ERR_BLOCKED_BY_CLIENT`，截圖重試仍停留前頁；這只能標記為客戶端阻擋，不能推論 robots 內容不存在。
- `/sitemap.xml`、`/sitemap_index.xml`、`/sitemap.xml.gz` 均嘗試過；未取得可供解析的正常 XML。前者在重試時受客戶端截圖／頁面處理影響，後兩者只顯示無法作為有效 sitemap 的編碼／單行內容；未確認任何下載檔。
- 個別長頁（司法單筆、跨機關表單、refresh、API 文件、智慧查找子題）DOM 與互動可確認，但同分頁截圖重試遇到 target closed 或 timeout。未將這些頁面描述成「已完整視覺檢查」。
- 其餘主要入口均以同一分頁的 URL、標題／heading、截圖與 DOM 驗證；安全測試均為公開、可重做的搜尋／篩選，沒有寫入資料。
