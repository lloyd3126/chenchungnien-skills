---
name: manny-pro-statementdog-bridge
description: Map 曼報 Pro business-research methods to Statement Dog facts, reproducible calculations, and evidence gaps. Use when the user asks whether Statement Dog covers a method, wants a combined workflow or coverage matrix, or needs to separate platform facts from custom industry analysis without overstating unavailable data.
---

# Manny Pro Statementdog Bridge

## Purpose

把「財報狗能直接提供什麼」與「曼報方法需要另外建模什麼」分開，建立可追溯的研究接點。輸出要能指出覆蓋範圍、公式、來源、缺口與不能由現有資料推出的結論。

## Read references

- 必讀 [evidence-discipline.md](../manny-pro-methodology/references/evidence-discipline.md)，先宣告 source-bound 或 current-state 模式。
- 讀 [statementdog-bridge.md](../../sites/manny-pro/references/statementdog-bridge.md)。
- 再讀 [research-methods.md](../../sites/manny-pro/references/research-methods.md) 與對應系列筆記。
- 需要區分文章引用與已核對資料時，讀 [article-source-index.md](../../sites/manny-pro/references/article-source-index.md)。
- 只有使用者允許且任務需要查詢時，才依既有 `statementdog-stock-research` 與 `statementdog-market` skills 的來源、期間、引用與登入規則操作；source-bound 模式只核對現有本地輸出與筆記。

## Three-layer mapping

將每個研究主張分到三層：

1. **財報狗事實**：本次直接讀取，或已保存在本地且能指出日期的財報、現金流、估值、同業、法說/產業資料與篩選結果；標示兩者差異並附期間、幣別與來源。
2. **自建模型**：由財報欄位重組的 GMV × take rate、單位經濟、正常化獲利、最低營運資金、分部/增量 ROIC 與反向估值。
3. **外部缺口**：平台未涵蓋或公司未揭露的營運 KPI、客戶行為、市佔、合約、法規、供應鏈與替代品資料。

「未在 Statement Dog 找到」不等於「產業沒有資料」。請再標示缺口屬於：平台欄位缺口、公司未揭露、需要外部來源、source-bound 模式未查，或尚未查找。

## Bridge workflow

1. **定義主張**：例如「平台 take rate 上升」「金融分部具備高 ROIC」「用戶成長能轉成 FCF」。
2. **列出證據需求**：指定欄位、期間、分母、幣別、分部、來源與更新頻率。
3. **核對 Statement Dog**：current-state 模式先取直接可得資料；source-bound 模式只核對既有輸出。兩者都記錄查不到/未查的項目，不用相近欄位代替而不註明。
4. **建立計算**：公開公式、調整項、正常化原則與敏感度；每個結果都能由輸入重算。
5. **處理外部缺口**：current-state 模式只補會改變投資判斷的缺口，標示來源日期、可信度與是否可重複取得；source-bound 模式只建立待核實清單，不進行外查。
6. **做一致性檢查**：核對公司揭露、財報三表、法說口徑、同業定義與期間。
7. **回到結論**：回答「Statement Dog 已覆蓋什麼、方法新增什麼、還缺什麼、哪些結論暫不能下」。

## Output template

| 研究主張 | 財報狗資料與日期 | 自建公式/模型 | 缺口類型 | 來源類型 | 證據狀態 |
|---|---|---|---|---|---|
|  |  |  |  |  | 直接核對 / 本地既有 / 計算 / 推論 / 待查證 |

接著提供：

- **覆蓋結論**：哪些可以直接回答，哪些只能形成初步假設。
- **公式與分母**：避免把營收、GMV、交易量、資產或投入資本混用。
- **資料缺口優先序**：按對估值/風險的敏感度排序。
- **下一輪核實清單**：指定未來要查的年報、法說、法規、產業報告或公司 KPI；source-bound 模式到此為止，不實際外查。

## Common mappings

- **平台/支付/拍賣**：Statement Dog 的收入、margin、FCF、負債與估值對應財務結果；GMV、take rate、供需密度、保證與網路效應通常要自建，或列入待核實的外部缺口。
- **店舖/硬體**：財報對應店舖、設備、存貨、capex 與現金流；同店、回收期、利用率、經銷商庫存與服務滲透通常需外部或手工整理。
- **金融分部**：財報對應貸款、利息、壞帳、負債與現金流；LTV、放貸條件、資產品質與跨周期壞帳需補資料。
- **平台廣告/博彩**：財報對應營收、SBC、FCF、現金與估值；DAU/MAU、ARPU、LTV/UAC、hold、法規狀態與內容/客戶風險需另建。

## Guardrails

- 不因 Statement Dog 沒有某個 KPI 就宣稱它「沒有涵蓋該產業」；精確描述覆蓋的是財務層、模型層還是營運層。
- 不把管理層口徑、文章觀點或單一年度數字當成已證實的產業規律。
- 最新財務、估值、法規、公司策略與市場數據只可在 current-state 模式下宣稱已重新查證；source-bound 模式標示最新本地日期與當期狀態未核實。
- 不把本地既有輸出冒充成本次即時查詢，也不把文章觀點冒充財報狗欄位。
- 對不可直接取得的資料明確標示估計、代理變數與不確定性。
