---
name: manny-pro-methodology
description: Extract, validate, compare, and apply reusable business research methods from 曼報 Pro / Manny Pro 商業解碼 series. Use when the user asks what an article teaches, wants article-to-method notes, compares methods across series, audits evidence, or needs a repeatable research framework derived from the member articles.
---

# Manny Pro Methodology

## Purpose

把商業解碼的個案文章轉成可重複使用、可追溯且可證偽的研究程序，而不是只做文章摘要。優先辨認交易流程、價值捕獲、競爭切入、工作流、單位經濟、成長品質、資本效率、制度與反向估值，再把每個方法連到證據、計算、時效限制與反證條件。

## Read the right references

- 必讀 [evidence-discipline.md](references/evidence-discipline.md)，先決定 source-bound 或 current-state 模式，再標示證據與時效。
- 讀 [research-methods.md](../../sites/manny-pro/references/research-methods.md) 取得抽取欄位與方法分類。
- 需要追蹤文章引用時，讀 [article-source-index.md](../../sites/manny-pro/references/article-source-index.md)，不要把文章提到的來源誤當成已直接核對。
- 用 [series-index.md](../../sites/manny-pro/references/series-index.md) 找到相關系列。
- 用 [method-index.md](references/method-index.md) 選擇一份主要方法 reference，再載入一至兩份支援方法。
- 只載入該案例的系列筆記，例如 [series-guo-lu-cai-shen.md](../../sites/manny-pro/references/series-guo-lu-cai-shen.md) 或 [series-luo-chui-zhi-qian.md](../../sites/manny-pro/references/series-luo-chui-zhi-qian.md)。
- 只有在 current-state 模式或使用者要求核對網站時，才使用 `manny-pro-content` 的唯讀瀏覽流程；遵守其登入、唯讀與不接觸帳號資料的界線。

## Source mode

- **Source-bound**：只使用本地原文、系列筆記與使用者指定檔案。使用者禁止上網時不得開啟瀏覽器；將價格、法規、公司現況等標成「截至本地資料日期」或「當期狀態未核實」。
- **Current-state**：保留文章時點的主張，再以有日期的第一方或權威資料核對現況。不得用新資料覆蓋舊主張而看不出變化。

## Method extraction workflow

1. **定義研究問題**：寫成可回答的問題，例如「收入成長是量、價格、mix、市佔還是金融滲透率？」
2. **畫交易與價值鏈**：標出客戶、供應商、平台、資金、資訊、風險與收費者；說明公司掌握哪個瓶頸。
3. **選擇經濟單位**：依案例選店舖、用戶、交易額、貸款、拍品、賭注、活躍畝數或會員點數。
4. **拆解驅動公式**：將營收、毛利、現金流或 ROIC 改寫成可驗證的因子，而非停留在敘事。
5. **建立 claim ledger**：依 [evidence-discipline.md](references/evidence-discipline.md) 分開來源類型與驗證狀態；記錄期間、日期、幣別、分母、公式、假設與 freshness need。
6. **設計反證**：為每個護城河或成長主張寫至少一個會推翻它的指標與觀察期間。
7. **產出可重用程序**：說清楚下次研究另一家公司時，要收集哪些資料、如何計算、多久更新、何時停止使用。

## Output format

用以下欄位整理每篇文章或每個方法：

- **文章/案例**與**研究問題**
- **核心假設**與**經濟單位**
- **交易流程與價值捕獲**
- **方法與公式**
- **證據台帳**（來源類型、驗證狀態、檔案/來源、日期、涵蓋期間）
- **應收集的證據**（財報、法說、產業、法規、外部資料）與**目前不能驗證的缺口**
- **可由 Statement Dog 承接的欄位**、**需要自建的計算**、**外部資料缺口**
- **反證與早期預警指標**
- **可複製到哪些產業**與**不適用的情況**

## Method selection guide

- 交易平台、支付、拍賣：讀 [transaction-value-capture.md](references/transaction-value-capture.md)，必要時加上 [platform-network-effects.md](references/platform-network-effects.md)。
- 替代技術、低價競爭、通路與入口威脅：讀 [competitive-entry-points.md](references/competitive-entry-points.md)。
- 餐飲、零售、硬體：讀 [unit-economics.md](references/unit-economics.md)，再用 [growth-quality.md](references/growth-quality.md) 分辨擴張品質。
- SaaS、評等、資料服務、硬體帶後端收入：讀 [workflow-productization.md](references/workflow-productization.md)，必要時加上 [governance-regulation.md](references/governance-regulation.md) 或 [capital-efficiency-roic.md](references/capital-efficiency-roic.md)。
- 收購型複利公司：讀 [acquisition-compounding.md](references/acquisition-compounding.md) 與 [capital-efficiency-roic.md](references/capital-efficiency-roic.md)。
- 金融或嵌入式金融：讀 [embedded-finance.md](references/embedded-finance.md)，再用 [capital-efficiency-roic.md](references/capital-efficiency-roic.md) 拆資本需求。
- 廣告、社群、博彩：讀 [unit-economics.md](references/unit-economics.md)、[platform-network-effects.md](references/platform-network-effects.md) 與 [governance-regulation.md](references/governance-regulation.md)。
- 高度稀缺或另類資產：讀 [alternative-assets.md](references/alternative-assets.md) 與 [scenario-reverse-valuation.md](references/scenario-reverse-valuation.md)。
- 任何需要判斷「好成長」或市場已定價多少的案例：加讀 [growth-quality.md](references/growth-quality.md) 與 [scenario-reverse-valuation.md](references/scenario-reverse-valuation.md)。

## Quality rules

- 不把文章中的歷史數字當成當前數字；current-state 模式重新查證，source-bound 模式明確保留資料時點並列待核實項目。
- 不把文章轉述的底層來源寫成已直接核對；來源類型與驗證狀態必須分開。
- 不把相關性寫成因果；說明哪些是文章觀點、哪些是本次推導。
- 不只列 KPI；說明 KPI 如何連到現金流、資本需求與估值。
- 不把「財報狗沒有欄位」誤寫成「產業沒有資料」；標示是平台覆蓋缺口、公司未揭露，或需要外部資料。
- 跨系列比較時先統一定義、期間、幣別與分母，再比較數值。
- 每個核心主張至少有一個可觀察反證；無法設計反證時，把它降級為敘事而非研究結論。
