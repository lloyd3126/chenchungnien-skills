# Chen Chung Nien Skills

[English](./README.md)

這是一個由 Chen Chung Nien 設計與整理的可重用 agent skills 集合。

這個 repository 主要用來展示我設計與發布的 skills，讓 AI agents 能在特定領域中更穩定地完成任務。

## About

這裡收錄的每個 skill 都以實用性、可維護性與明確邊界為目標，重點不是一次性的 prompt，而是能真正支援持續工作的能力模組。

## 目前收錄的 Skills

| Skill | 說明 |
| :--- | :--- |
| [`tw-gov-data`](skills/tw-gov-data) | 用來探索、檢視、比較與整理台灣政府開放資料平台 `data.gov.tw` 上的資料集。 |
| [`tw-stock-data`](skills/tw-stock-data) | 使用 `tw-stock` CLI 抓取、驗證與分析台灣上市櫃、期貨、選擇權與公開資訊觀測站財務資料。 |
| [`website-skill-builder`](skills/website-skill-builder) | 使用 Codex 內建瀏覽器系統性探索網站，將穩定的網站結構、工作流程與資料模型整理成可重用的 Agent 指引。 |
| [`tabelog-search`](skills/tabelog-search) | 在 Codex 內建瀏覽器中搜尋與篩選 Tabelog 公開餐廳資料，包含使用自動完成選取地區與驗證搜尋結果。 |
| [`tabelog-restaurant`](skills/tabelog-restaurant) | 透過內建瀏覽器查看 Tabelog 餐廳頁面，以及菜單、照片、評論、評分、地圖與空位等相關頁面。 |

## 網站專用指引

[Tabelog 網站套件](sites/tabelog/AGENTS.md)提供 Tabelog skills 共用的導覽、session、資料新鮮度與驗證原則；[references](sites/tabelog/references)則記錄探索過的 sitemap 階層、資料模型與網站第一方說明。

## 使用方式

當某個網站需要成為未來 Agent 可反覆使用的工具時，使用 `website-skill-builder`。它會從 Codex 內建瀏覽器目前開啟的分頁開始，若網站提供 sitemap 就優先使用，先完成不需登入的功能，再於需要登入時詢問是否繼續探索受保護功能。

處理 Tabelog 搜尋任務時使用 `tabelog-search`，查看餐廳詳細資料與子頁面時使用 `tabelog-restaurant`。未來 Agent 應將即時網站 UI 與說明文件和這些檔案比對，並在工作區可寫入時，自主更新已驗證的穩定差異。

## Installation

你可以使用 [Vercel skills CLI](https://skills.sh/docs/cli) 來瀏覽與安裝這個 repository 內的 skills。

### Using Vercel skills CLI

```sh
# 互動式瀏覽並安裝這個 repo 內的 skills。
npx skills add lloyd3126/chenchungnien-skills --list

# 全域安裝指定 skill。
npx skills add lloyd3126/chenchungnien-skills --skill tw-gov-data --global
npx skills add lloyd3126/chenchungnien-skills --skill tw-stock-data --global
npx skills add lloyd3126/chenchungnien-skills --skill website-skill-builder --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-search --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-restaurant --global
```
