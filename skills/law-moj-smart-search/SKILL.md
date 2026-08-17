---
name: law-moj-smart-search
description: Use the Taiwan Laws & Regulations Database in the built-in browser to navigate its scenario-based Smart Search topics, follow T/O theme choices, and connect a user's everyday legal question to public law and service links without presenting the guide as legal advice.
---

# Law MOJ Smart Search

用生活情境逐層探索法律主題，將結果當作公開資源導覽，再回到正式法規或主管機關來源核對。

## Workflow

1. 開啟 `/SmartSearch/main.aspx`，先選主題分類，例如生活法律、婚姻與家庭、教育與校園、個資與網路、勞工權益、居住權益等；熱門案例與卡片內容是動態的。
2. 從頁面實際連結取得 `T` 主題參數與 `O` 選項參數，逐層進入 `/SmartSearch/Theme.aspx?T=<T>&O=<O>`；不要猜測子選項。
3. 閱讀主題說明、進一步選項與法規／服務連結；保留完整 T/O 路徑，避免只報告主題名稱。
4. 若使用者需要法律正文或裁判，從實際連結回到法規、司法或主管機關來源，重新確認頁面與日期。
5. 清楚說明智慧查找是情境索引，不是個案法律意見；复杂或高風險問題應建議使用者諮詢適格專業人士或官方法律扶助資源。

## References

路由與探索限制見 [site-map.md](../../sites/law-moj/references/site-map.md)，官方範圍與法律扶助邊界見 [first-party-guidance.md](../../sites/law-moj/references/first-party-guidance.md)。

## Boundaries

- 只做公開主題導覽，不登入、不收藏、不送出表單。
- 不把主題卡片、推薦法規或摘要視為完整、最新或適用於特定個案的法律結論。
- 主題與熱門案例會變動；每次重新讀取，不要硬編卡片數量或當前熱門項目。
- 若同一分頁截圖重試失敗但 DOM 可讀，回報此證據限制。
