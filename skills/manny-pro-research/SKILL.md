---
name: manny-pro-research
description: Execute an evidence-traceable Manny Pro-style company or industry research workflow using value-chain mapping, workflow and competition analysis, unit economics, financial normalization, capital efficiency, scenarios, and reverse valuation. Use for deep business analysis or reports that must go beyond financial-statement summarization.
---

# Manny Pro Research

## Purpose

把個案方法組合成一份可驗證的公司研究。先理解公司如何交易與收費，再把營運因子接到財報、資本效率、競爭風險與估值；輸出必須區分文章觀察、直接證據、模型、推論與待查證假設。

## Load references

- 必讀 [evidence-discipline.md](../manny-pro-methodology/references/evidence-discipline.md)，並在開始時宣告 source-bound 或 current-state 模式。
- 讀 [series-index.md](../../sites/manny-pro/references/series-index.md) 選擇最相近的案例。
- 讀 [research-methods.md](../../sites/manny-pro/references/research-methods.md) 及一至兩份相關系列筆記。
- 讀 [article-source-index.md](../../sites/manny-pro/references/article-source-index.md) 追蹤系列文章的來源線索、資料期間與待核實原始文件。
- 依研究問題讀 [方法索引](../manny-pro-methodology/references/method-index.md) 中的一份主要方法與支援方法；不要一次載入全部 references。
- 若要整理 Statement Dog 對接，讀 [statementdog-bridge.md](../../sites/manny-pro/references/statementdog-bridge.md) 並搭配 `manny-pro-statementdog-bridge`。
- source-bound 模式只使用本地資料，不啟動網站或外部查找；current-state 模式需要最新數字、股價、法規或產業狀況時才重新查證，不沿用筆記中的舊數字。

## Research workflow

1. **界定來源與範圍**：記錄來源模式、最新本地資料日期、公司、業務、地區、期間、幣別、投資問題與不成立的條件。
2. **畫商業模式**：列出客戶、供應商、通路、平台、資金、資料、監管與風險承擔者；標出公司在哪個環節收費。
3. **建立收入橋**：依案例選用 `GMV × take rate`、價格 × 量 × mix、店舖數 × 同店銷售、使用者 × ARPU、貸款 × 利差或其他合理公式。
4. **建立單位經濟**：選一個最小可追蹤單位，計算收入、變動成本、固定成本、回收期、留存/重複率與增量資本需求。
5. **正常化財務**：拆核心與非核心、一次性項目、SBC、併購、商譽/無形資產、維持性與成長性資本支出；按業務風險計算分部 ROIC 或增量 ROIC。
6. **檢查競爭與制度**：用入口/替代路徑、工作流可替換層、市場歷史、客戶/供應商議價力、網路效應、法規與危機案例檢驗護城河。
7. **建情境模型**：至少建立基準、樂觀、悲觀三情境；每個情境明列成長、margin、再投資、資金成本與風險事件。
8. **做反向估值**：有明確估值日期與價格時，反推市場已經假設的收入、利潤、ROIC、終值與持續年限；缺少 dated price 時只提供可重算框架與所需輸入，不宣稱「目前估值」。
9. **列追蹤清單**：把最能改變結論的 3–7 個先行指標、更新頻率、觸發門檻與反證行動寫出來。

## Required output

### 1. Executive conclusion

用一段話回答：公司如何賺錢、主要價值驅動、資本效率與最大風險；只有具備 dated price/valuation 時才回答估值需要什麼條件才合理，否則列出估值待補輸入。

### 2. Claim ledger and model table

| 主張/輸入 | 來源類型 | 檔案/來源與日期 | 涵蓋期間 | 狀態 | 公式/假設 | Freshness need |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### 3. Driver tree and valuation

用表格列出驅動因子、觀察值及日期、基準假設、樂觀/悲觀值、影響的財務項目與反證來源。估值只在假設與 dated inputs 可追溯時呈現；不要用精確目標價掩蓋不確定性。

### 4. Falsifiers and monitoring

為每個核心主張指定：會推翻它的觀察、資料來源、更新頻率、門檻與下一步。

## Guardrails

- 把 Statement Dog 的欄位、手工重組、外部研究分開；不因資料缺口而補造數字。
- 最新市場、股價、監管、管理層與公司揭露只可在 current-state 模式下宣稱已核實；source-bound 模式一律標示資料時點與當期狀態未核實。
- 不把文章轉述、管理層說法、研究者計算與直接核對的第一方資料混成「已驗證事實」。
- 不把管理層指引視為事實；列出實現條件與過往達成紀錄。
- 對金融、博彩、藝術、平台等週期或監管敏感業務，至少做一次壓力情境。
- 若只有單一年度或單一案例支持結論，明確標示證據不足。
