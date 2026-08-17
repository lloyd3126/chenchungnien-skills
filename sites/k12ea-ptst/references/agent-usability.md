# Agent usability 測試

以下測試以新 Agent 只讀取 `sites/k12ea-ptst/AGENTS.md`、兩個 skills 及其 references 為前提；測試目標是確認它能選 skill、找入口、完成唯讀流程並停在正確邊界。測試使用抽象意圖，不把本輪 live 結果當答案。

| Scenario | Expected skill／entry | Required sequence | Verification and stop | Outcome |
| --- | --- | --- | --- | --- |
| 「找臺北市目前代理職缺」 | `$k12ea-ptst-job-search` → `職缺資訊` | Select current `臺北市`; re-read district options; optionally narrow type/level; click `查詢` | Verify selected county, query state and table; report current rows only; no favorite | Pass：route、dependent control、freshness rule 明確。 |
| 「看某筆職缺完整條件」 | `$k12ea-ptst-job-search` → current result row | Click the current row, not a guessed ID | Verify vacancy number, school, rounds, status and protected fields; stop before `我有意願` | Pass：detail entry and side-effect boundary 明確。 |
| 「這個網站怎麼申請代理老師」 | `$k12ea-ptst-public-resources` → `求職說明` + `FAQ` | Read first-party instruction; use FAQ for qualification wording | Separate instruction-page statement from public UI; do not provide legal conclusion | Pass：reference explains the observed public/instruction discrepancy。 |
| 「找臺北市教師攬才措施」 | `$k12ea-ptst-public-resources` → support index → current Taipei link | Open current county list and visible item detail | Verify county, date, title and body; no external share | Pass：county route and dynamic-content rule 明確。 |
| 「查資格或薪資 FAQ」 | `$k12ea-ptst-public-resources` → FAQ | Enter a non-sensitive keyword if useful; expand current question | Use current answer text; cross-check law only on request; no legal extrapolation | Pass：accordion/search behavior and interpretation limit 明確。 |
| 「把職缺加入我的最愛」 | `$k12ea-ptst-job-search` → current row star or `我的最愛` | Confirm current login state first | Stop before mutation; if unauthenticated report redirect to login and ask for manual sign-in if needed | Pass：protected boundary is explicit and no mutation is implied。 |

## Gaps found and addressed

- The row-to-detail transition is a table-row interaction rather than a visible anchor; job-search skill now calls out `tr[data-vacurl]` and requires current-row verification.
- FAQ keyword search can leave the URL unchanged; the public-resource skill uses visible question-set and expanded answer state as verification.
- `/robots.txt` and conventional Sitemap candidates do not provide usable inventory in this browser run; the site-map page is the authoritative first-party inventory captured here.
- RecruitSupport list/detail DOM was readable but screenshot control timed out; coverage records the limitation instead of calling those pages visually accessible.
