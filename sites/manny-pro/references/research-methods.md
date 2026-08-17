# 曼報 Pro 研究方法整理

## Purpose

這份文件記錄從已登入、可讀取的曼報 Pro 會員文章中，逐篇萃取的研究問題、論證方法、證據類型、可驗證指標，以及與財報狗研究流程的對接方式。

本文件不是投資建議，也不把文章中的單一公司結論直接套用到其他公司。每一篇文章的動態數字、估值與事件背景都應在重新研究時回到原文及第一方資料核對；若使用者限制為本地資料，則保留文章時點並標示「當期狀態未核實」，不得暗示已完成現況核對。

## Evidence mode

- **Source-bound**：只用本地原文、系列筆記與使用者指定檔案；記錄最新本地資料日期，動態主張只作文章/檔案時點結論。
- **Current-state**：保留文章時點，再對會變動的數字、法規、估值與公司狀態做有日期的第一方核對。

來源類型與驗證狀態分開記錄。文章寫過、文章引用過某份報告、已直接打開底層文件、研究者自行計算與研究者推論是五種不同的證據，不得統稱「已驗證」。共同規則見 [evidence-discipline.md](../../../skills/manny-pro-methodology/references/evidence-discipline.md)。

## Article extraction schema

每篇文章固定記錄：

1. 研究問題：作者試圖解釋什麼商業現象？
2. 核心假說：公司為什麼能創造或捕捉價值？
3. 研究單位：公司、產業鏈、交易流程、利益關係人或制度。
4. 方法：流程拆解、價值鏈、競爭、單位經濟、歷史、情境、估值等。
5. 證據：年報、法說、產業資料、訴訟文件、學術研究、專訪或業界訪談。
6. 量化驗證：收入來源、take rate、滲透率、成長率、利潤率、ROIC、現金流、估值等。
7. 反證與風險：哪些條件成立時，原本的商業假說會失效？
8. 財報狗對接：可用的個股、產業、財務、估值、法說與同業比較欄位。
9. 可重複流程：下一家公司可如何照做。

## Reusable method taxonomy

- Transaction/process mapping：先把一筆交易或服務的參與者、流程、責任和費用拆開。
- Value-chain and value-capture analysis：辨識每個參與者創造了什麼價值、收取什麼費用，以及誰承擔成本與風險。
- Business-model asymmetry：比較收入、資本需求、信用風險、營運成本和責任是否落在不同參與者身上。
- Multi-sided network analysis：分析消費者、商家、供應商、平台、金融機構或監管者之間的互相依賴。
- Competitive entry-point analysis：依新競爭者從消費者端、商家端或雙邊市場切入的位置分類威脅。
- Workflow productization analysis：拆開資料、研究/洞察、決策軟體、工作流、入口硬體、後端耗材與人工服務，檢驗收入是否真正產品化並形成可量化的使用與切換成本。
- Unit economics：用每筆交易、每位客戶、每美元金流或每項服務的收入與成本檢查規模效應。
- Growth-quality analysis：把成長拆成量、價、滲透、跨界延伸與併購，檢查每種成長的邊際報酬是否相同。
- Historical and institutional analysis：重建規則、制度、責任分配與公司策略如何長期累積成護城河。
- Capital-allocation and reinvestment analysis：區分核心營運報酬與管理層再投入資本的報酬。
- Scenario and falsification analysis：建立基準、壓力和替代情境，並明確列出能推翻主張的觀察訊號。
- Reverse valuation：由目前市值反推市場隱含的成長率、利潤率、抽成率或終值假設。

這 12 類方法的可執行版本與案例路由見 [method-index.md](../../../skills/manny-pro-methodology/references/method-index.md)。

逐篇文章的來源線索、主張對應、保存狀態與待核實清單見 [article-source-index.md](article-source-index.md)。

## Statement Dog bridge

曼報 Pro 的質化假說可先轉成以下財報狗問題：

- 商業模式是否帶來持續的營收成長與毛利／營業利益率？
- 成長是否轉化成營業現金流與自由現金流？
- 核心業務與併購、投資、商譽、無形資產是否應分開看？
- ROIC、資產週轉、負債與資本配置是否支持護城河假說？
- 法說會的管理層說法，是否與財報數字及同業比較一致？
- 現在估值隱含的成長和利潤率，是否高於可合理支持的情境？

若公司或產業不在財報狗的可用資料範圍，應標記 coverage gap，改以年報、法說原文、監管文件、產業報告或其他第一方資料補足，不應用相近公司數字代替原公司。
