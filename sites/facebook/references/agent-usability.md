# Facebook Agent Usability Checks

Use these stable request shapes to check that an Agent can route to the right skill without relying on current results or personal data.

| Request shape | Skill | Entry | Required verification | Safe stop |
| --- | --- | --- | --- | --- |
| 找 Facebook 上與某主題相關的社團或貼文 | `$facebook-search` | `搜尋 Facebook` | query retained、`<query>的搜尋結果` heading、scope tab and query route | before reacting, commenting, messaging, sharing or saving |
| 找 Marketplace 上某類商品，按價格或距離排序 | `$facebook-marketplace` | `Marketplace` → `搜尋 Marketplace` | query text、selected filter/sort、URL state or changed cards、detail heading and a listing field | before messaging seller, saving, buying, verifying age or listing |
| 找遊戲、設定或支援入口 | `$facebook-navigation` | top nav `遊戲` or profile menu | route、heading/tab or visible submenu label | before launching a game, changing settings, reporting or logging out |
| 判斷 Facebook Sitemap 能否提供路由 | `$facebook-navigation` + `references/site-map.md` | visible UI, then `/robots.txt` only as discovery | independent Sitemap status fields and robots boundary | before treating Disallow as permission or using a blocked `.xml.gz` workaround |

For each check, use the current UI and dynamic values at task time. Do not persist query results, prices, counts, ranking, account names, shard lists or tracking parameters.
