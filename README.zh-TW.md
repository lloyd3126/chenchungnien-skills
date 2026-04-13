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

## Installation

你可以使用 [Vercel skills CLI](https://skills.sh/docs/cli) 來瀏覽與安裝這個 repository 內的 skills。

### Using Vercel skills CLI

```sh
# 互動式瀏覽並安裝這個 repo 內的 skills。
npx skills add lloyd3126/chenchungnien-skills --list

# 全域安裝指定 skill。
npx skills add lloyd3126/chenchungnien-skills --skill tw-gov-data --global
```
