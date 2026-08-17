# 橘蘋學習平台（koding.school）網站操作指引

## Scope

這份指引只適用於透過 Codex 內建瀏覽器操作 `https://koding.school/`。網站是兒童、青少年與初學者的程式設計學習平台，包含課程、lesson、知識點、課程討論、作品、工作室、個人履歷與帳號入口。

本次探索於 2026-08-17 完成公開與登入後第二輪核對；目前文件只保留穩定導覽、頁型、控制項語意與安全邊界，不保留課程進度、專案名稱、訊息內容、作者資料、數量、時間或其他帳戶紀錄。

## Sitemap-assisted inventory

- 首頁未提供可見的 `Sitemap`／`Site map` 入口。
- 頁尾目前只看見 `關於我們`、聯絡方式與部分頁型的 `語言` 選單，未看見 HTML sitemap、Help、Documentation 或 FAQ 入口。
- 同源 `/robots.txt` 在 Codex 內建瀏覽器中回報 `ERR_BLOCKED_BY_CLIENT`，未取得任何 `User-agent`、`Allow`、`Disallow` 或 `Sitemap:` 內容；因此本次沒有 robots-derived route clue。
- 同源 `/sitemap.xml` 也回報 `ERR_BLOCKED_BY_CLIENT`，未取得 XML；沒有發生 `.gz` 下載，因此沒有 downloaded／locally parsed／UI-verified sitemap 狀態。不要用 CLI、API、web search 或外部瀏覽器補抓。
- 下列是由網站 UI 驗證的穩定路由模式，不是 sitemap 證據：`/courses/<family>/<slug>`、`/courses/<family>/<slug>/lessons/<unit>/<chapter>`、`/courses/<slug>/topics`、`/courses/<slug>/lessons/<lesson-id>/topics`、`/knowledges/<slug>`、`/my/courses`、`/my/projects`、`/my/studios`、`/studios/<studio-id>`、`/my/messages`、`/resume/<student-id>`、`/my/account`。
- 不要把私人、tokenized、動態或過量 URL 清單寫入 skills；需要目前資料時，回到可見 UI 重新取得。
- 詳細的 inventory 狀態、coverage checklist 與 workflow routing 見 [references/exploration-checklist.md](references/exploration-checklist.md) 與 [references/site-map.md](references/site-map.md)。

## Global routing

- 找課程、篩選已加入課程、查看課程詳情或 lesson／編輯器 → `$koding-school-learning`。
- 查看知識點、課程討論、lesson 主題、搜尋討論或閱讀回覆 → `$koding-school-community`。
- 瀏覽作品、工作室、個人履歷或帳號入口 → `$koding-school-projects`。
- 需要帳號設定、收信匣、訂閱或訂單的實際操作時，先閱讀對應 skill 的隱私與確認邊界；收信匣與財務頁本次沒有深入讀取。

## Navigation

- 首頁 `/`：登入後顯示 `繼續上課`、目前課程卡與進度摘要。`繼續上課` 目標會隨最近瀏覽 lesson 改變，不能當作完成度證據。
- 導覽列 `Toggle navigation`：展開後有 `創造`、`我有邀請碼`、`我的課程` 與帳號下拉選單。
- `創造`：開啟 Scratch3、JavaScript、Web、Micro:Bit、Ozobot、App Inventor、Python、Roblox 等作品類型選單，並提供專案名稱欄位；`新增作品` 是建立動作。
- `我有邀請碼`：開啟邀請碼與課程選擇表單；`送出` 會註冊／加入課程。
- 帳號下拉目前視覺確認到：`我的課程`、`我的作品`、`我的工作室`、`我的收信匣`、`我的履歷`、`帳號設定`、`登出`。訂閱／訂單入口本輪未在目前選單中看見，不要假設存在。
- 課程詳情：顯示課程特色、lesson outline、知識點連結與 `討論區`。
- lesson：以 breadcrumb、`返回課程`、`下一章`、`儲存`、課程列表、影片或嵌入式 JavaScript workspace 組成。
- 頁尾：`關於我們`、聯絡方式與 `語言`，語言選項為 `繁中`、`简中`、`English`、`日本語`。切換語言可能改變 session／頁面狀態，除非使用者要求不要主動切換。

## Operating rules

- 只使用 Codex 內建瀏覽器；不要改用 Chrome、外部瀏覽器、API、CLI、web search、cookies、local storage、session 檔案或頁面隱藏 token。
- 公開與登入後是兩個網站變體。每次登入後都要重新核對首頁、課程頁、知識點、討論搜尋與主要 lesson 控制項。
- 預設只做讀取與可逆安全互動：導覽、搜尋、篩選、展開選單、開啟／關閉空白表單、閱讀頁面。
- `送出`、`留言`、`新增主題`、`新增作品`、`新增工作室`、`儲存`、`Run`、`移除`、帳號更新、上傳、加入課程、登出與任何 POST／刪除動作都要停在確認邊界。
- 不要讀取或重述密碼、cookie、token、完整個人資料、私人訊息、財務紀錄或目前專案／進度資料，除非使用者提出精確且必要的請求。
- 搜尋表單的目前 query 會包含表單輔助參數（例如 `utf8`、`button`）；只把使用者輸入的 `q` 視為語意，並同時核對 URL 與結果。排序／類型篩選會保留既有 query，使用當下可見連結，不要猜參數。
- lesson 頁可能顯示帶編碼 `data` 的 `Subcourse button`；它是 tokenized 入口，不要保存、揭露或僅因看見它就跟隨。優先使用可見的課程列表、`返回課程` 或 `下一章`。
- 使用站上當前可見文字作為 source of truth；不要從頁面上看到的動態結果推導穩定規則。

## Validation and freshness

- 課程搜尋／篩選：同時核對主要 heading、目前 URL query 與可見卡片狀態。
- 討論搜尋：輸入安全代表詞後確認列表縮小；清除欄位後確認列表恢復。
- lesson：核對 URL、breadcrumb、lesson 標題、`下一章`、`返回課程`，需要時確認 video／editor iframe 與可見 tabs。
- 知識點：區分實際文章與 `尚無內容`，並重新讀取目前相關知識點與更新標記。
- 作品／工作室／帳號：只核對路由、heading、控制項與目前要求的欄位；不要把現在的卡片、名稱、訊息或數字寫入 reusable guidance。

## Known limits and gaps

- sitemap 與 robots metadata 在內建瀏覽器中 blocked，沒有 sitemap-based coverage。
- 知識點頁可能只有 `尚無內容`；本次未找到可依賴的完整方法論或 FAQ。
- 已確認 lesson 的 `【說明】`、`【講解】`、`【試玩】`、`【連結】` 型態；未執行編輯器 `Run`、`Format` 或 `儲存`。
- 已確認作品／工作室列表與一個代表性工作室頁；未進入專案編輯器、回收桶、工作室建立流程或移除流程。
- 已確認收信匣的列表與 `/my/messages/<message-id>` 路由結構，但未讀取私人訊息內容；已確認帳號設定欄位與 POST 邊界，但未修改帳號。訂閱／訂單頁本輪未在目前帳號選單中看見，未探索。
- 繁中履歷與帳號頁的 document title 出現 `translation missing: zh-TW...`，這是已觀察到的 UI 翻譯缺口，不代表路由失效。

## Drift maintenance

未來操作前先比對目前可見 UI、route、label、controls、權限與站上說明。若不同，先用目前 UI 完成安全任務，再記錄公開／登入變體、頁型、舊行為、目前行為、驗證證據與日期；當差異穩定且明確時，更新負責的 AGENTS、skill 或 reference。不要寫入密碼、cookie、token、私人資料、動態數值或一次性結果。更新後重新執行受影響的安全流程與 `quick_validate.py`；廣泛、矛盾或無法安全驗證的變更要標成 maintenance gap，不要猜測。

## References and skills

- [koding-school-learning](../../skills/koding-school-learning/SKILL.md) — 課程、已加入課程、lesson 與編輯器路由。
- [koding-school-community](../../skills/koding-school-community/SKILL.md) — 知識點、討論搜尋、主題與回覆閱讀。
- [koding-school-projects](../../skills/koding-school-projects/SKILL.md) — 作品、工作室、履歷、收信匣與帳號入口。
