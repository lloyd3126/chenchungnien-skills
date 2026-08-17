# Seeking Alpha Agent Usability Checks

Use these request shapes to check that a future Agent can route the task without relying on current results.

| Request shape | Skill | Entry | Required verification | Safe stop |
| --- | --- | --- | --- | --- |
| 查某股票目前評等、財務與估值 | `$seeking-alpha-stock-analysis` | `/symbol/<ticker>` or global search | ticker/name heading, selected page tab, requested section fields and observation time | before interpreting as advice or executing a trade |
| 讀某股票最近分析與新聞 | `$seeking-alpha-stock-analysis` then `$seeking-alpha-market-research` | symbol hub → `Analysis`/`News` or linked article | symbol identity, selected content tab, article/news title, author/source and access state | before Follow, Like, Share, Comment or Save |
| 找今天或某日期的財報事件 | `$seeking-alpha-market-research` | `/earnings/earnings-calendar` | date/range, selected EPS/Revenue/revisions tab, table heading and rows | before treating estimates as actuals or a forecast |
| 看市場最新新聞或某主題 | `$seeking-alpha-market-research` | `/market-news` → visible topic/category | page heading, topic state, headline/source context and linked symbol | before copying, sharing or messaging |
| 按 Quant／股息／成長等條件找股票 | `$seeking-alpha-screening` | `/screeners` → visible preset or custom entry | screen name, criteria, sort/filter state, result table and freshness | before saving a screen, subscribing or purchasing Premium |
| 搜尋股票、作者或關鍵字 | `$seeking-alpha-market-research` | homepage search or `/basic-search` | retained query, visible result scope/heading, selected destination | before opening protected or account actions |

For every check, use the current UI and dynamic values at task time. Do not persist prices, result counts, rankings, article lists, user names or private records.
