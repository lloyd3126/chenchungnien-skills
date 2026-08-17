# 國資圖 Agent usability test

These are document-only simulations using the generated `AGENTS.md`, skills, and references. They do not replay the browser session and do not contain live results.

| Request | Expected routing | Safe sequence | Outcome |
| --- | --- | --- | --- |
| 找國資圖接下來幾天適合樂齡的講座 | `$nlpi-activity-search` → `/ActivityInfo/recap` | Open advanced filter; use current dates, `樂齡`, `講座`; apply; verify filter tags, count and cards; stop before registration | Pass: `activity-controls.md` supplies labels, reset/apply semantics and the known date-radio caveat. |
| 搜尋國資圖網站中「借閱」相關頁面 | `$nlpi-site-search` → `/Search` or `/AdvancedSearch` | Enter a non-sensitive keyword; submit once; verify retained input plus URL/hash and result state; report embedded-search errors | Pass: skill distinguishes a button click from a verified result and routes advanced syntax correctly. |
| 唯讀確認我的借閱與預約 | `$nlpi-member-center` → `/member` → `/Member/myipac` | Confirm visible authenticated state; inspect `我的借閱` / `我的預約`; report current list only; do not logout or renew | Pass: skill handles account scope, dynamic empty lists, cross-site cards and known record-route gaps. |
| 我有借閱證，想知道電子書和資料庫怎麼用 | `$nlpi-digital-resources` → `/StaticPage/resources-intro` | Read first-party categories and eligibility; distinguish `ers.nlpi.edu.tw` from `ebook.nlpi.edu.tw`; stop before external login | Pass: skill gives the three-step portal semantics while preserving the external-platform boundary. |

## Recheck rule

If a future agent cannot choose a skill, identify a confirmed route, or find a verification signal from these files, update the owning reference rather than adding a speculative URL or a current result value.
