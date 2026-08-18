# Tabelog Expert forward tests

Run these as read-only behavioral checks after a material workflow change. Use the live in-app browser when the site is available; do not save one-off results in the skill.

| Case | Input pattern | Required assertion |
|---|---|---|
| Default route | User asks for a ranked shortlist with area, food, storefront, and target month | The agent follows homepage → normalize → score-sorted inventory → early hard gates → current product → official website/SNS cross-check → date-sorted reviews → seasonal check → one score-first ranking. It does not ask the user to choose among methods. |
| Bounded search | The first result page has many candidates | The agent inspects the first 10 relevant cards, extends only to 20 or result exhaustion when fewer than three can qualify, and does not browse indefinitely. |
| Homepage recovery | A verified deep page becomes a connection/error page | The agent checks `https://tabelog.com/` first; if it loads, it rebuilds the search in the same in-app browser. |
| Error-page navigation | The current error page rejects navigation | The agent may create a fresh tab in the same in-app browser, but does not switch to Chrome or an external surface. |
| Homepage unavailable | Deep page and homepage both fail | The agent reports a connectivity gap and fabricates no shortlist. |
| Language normalization | User gives a Chinese or English food name | The agent records the Japanese keyword, synonyms, and exclusions before submitting. |
| False positive | Search returns an analog, wish-only review, or another branch | It is classified and excluded from the qualified ranking. |
| Review order | Keyword search and `訪問月順` are both available | The agent verifies visible order and URL/query state before interpreting dates. |
| Date distinction | Visit month and publication date differ or one is hidden | They are recorded separately; hidden publication date is `未取得`. |
| Current menu gap | Menu text omits an item but recent reviews mention it | Output says `目前未列出（未等於停售）` plus recent review evidence. |
| Future month | User asks for a future month at a facility-dependent venue | Opening status states the facility dependency and does not promise exact availability. |
| Fewer than three | Only one or two candidates pass all hard gates | Return fewer than three and list near-misses separately instead of filling the ranking. |
| Service optionality | User requires a storefront but says dine-in/reservation are optional | Storefront is gated; takeout, dine-in, and reservation remain separate fields. |
| Scenario map | User gives a short request without stating budget, transport, format, or prestige priorities | The agent declares the six core lenses at the start, exposes the three contextual lenses with an applicable/unconfirmed/not-found status, uses one shared evidence ledger, and does not ask the user to choose a method. |
| Scenario trade-off | Qualified candidates trade product format, price, station access, ease of purchase, seasonality, local exclusivity, or fame against score | Each lens uses its relevant evidence and states the trade-off; the same candidate may win multiple lenses, and a scenario advantage never repairs a failed hard gate. |
| Score boundary | A candidate just below Top 3 has a higher score than a specialist candidate, or two candidates tie | The agent audits the boundary/equal-score candidates, ranks only qualified candidates, and explains every higher-scoring exclusion. |
| Review cutoff | Matching reviews span many pages | The agent records newest-to-oldest visit months through the twelve-month cutoff, checks the same prior-year month when available, and stops rather than paging indefinitely. |
| Review extraction | A matching review contains a product, price, stock, seasonal, or wish-only cue | The evidence record keeps the review URL, visit month, exact wording, format, and freshness; a wish or failed purchase is not promoted to positive evidence. |
| Locator fallback | A visible sort or pagination locator fails once | The agent re-reads the current DOM, uses an observed visible equivalent/href, verifies the new page, and does not guess a URL or repeat the failed locator blindly. |
| Navigation misroute | Autocomplete or a failed navigation lands on another area/category or a nationwide result | The agent checks title/heading, area, keyword/category, and URL scope; when at least two checks fail, it returns to the Tabelog homepage and rebuilds instead of treating the wrong result as a fallback. |
| Future-weekday opening | The target month is future and the shop has weekly hours | The agent reports the likely weekdays/dates as `正常營業日推定`, keeps temporary-closure uncertainty, and does not promise every date. |
| Storefront vs access | A high-score restaurant mentions the item only as a course dessert while a lower-score shop sells it as a standalone item | The agent keeps both when format is open, labels product access prominently, and does not present the course dessert as takeaway. |
| Item-level takeaway | A store has a generic `テイクアウト` flag but the requested seasonal item appears only as dine-in or course evidence | The agent records `store takeout flag only` or the exact dine-in/course state, does not claim standalone takeaway, and applies the format caveat to ranking. |
| Future seasonal evidence | A future-month item has recent reviews but no current menu or same-month prior-year evidence | The agent marks it `條件式`, keeps it out of the main future-month ranking, and lists it as a near-miss instead of filling Top 3. |
| Seasonal recurrence | An official page shows a fixed season or prior-year target-month announcement but no current-year exact announcement | The agent records `固定季節／販售期` or `歷年同期模式（今年未公告）`, requires recent matching purchase evidence for `季節模式支持`, and never calls it current-year confirmed. |
| Official source cross-check | Tabelog links to a shop website or social account for a future, seasonal, local, or branch-limited request | The agent follows the Tabelog-linked source in the same in-app browser, records URL/type/observation date/item/period/branch/format/status, and keeps official current or planned information separate from historical Tabelog experience. |
| Official conflict | The official source lists the item for the target period, but recent Tabelog reviews report sell-outs, changed format, or inability to buy it | The output states both: official source supports the planned/current listing, while recent reviews support real-world stock or purchase friction; it marks the candidate `官方與 Tabelog 衝突` and lowers certainty as appropriate. |
| Official source unavailable | The Tabelog-linked official page or account is unavailable, silent, or cannot be verified as first-party | The agent records `官方未確認`, lowers confidence, does not invent a seasonal/current claim, and either qualifies on independent Tabelog evidence with the caveat or lists the candidate as a near-miss when an official announcement is required. |
| Collapsed review | The newest matching review exposes `もっと見る`/`続きを読む` and the visible snippet omits the item | The agent expands the card before judging product presence; if expansion fails, records `內容未展開` and lowers confidence. |
| Stale tab recovery | The controlled tab becomes stale or missing while the browser remains connected | The agent creates a fresh tab in the same browser, verifies the homepage, and rebuilds the visible search without switching surfaces. |
| Station scope | The requested station search returns shops near adjacent stations or inside facilities | The output records requested-station distance, nearest station, and facility/branch context rather than implying every result is inside the station. |
| Transport output | The user asks for a shortlist without providing an origin | The output reports the nearest station and an approximate walk time derived from the observed distance; it does not expose raw metres as the main access answer or invent a transit route. |
| Origin-based route | The user provides a start station, hotel, or landmark | The output uses a current in-app route source when available and reports total time, line(s), transfer count, and final walk; if the route cannot be verified it says `交通路線未確認` and preserves only the verified station walk estimate. |
| Raw versus qualified rank | The highest-score candidate fails item-level access or target-month evidence while a lower-score candidate passes | The output records the raw score leader as an explained near-miss and ranks the lower-score candidate only as the qualified winner. |
| Review date reconciliation | Review-card month, detail-page visit date, and publication date differ or one is hidden | The agent records each surface separately, keeps `未取得` when needed, and lowers confidence when the dates cannot be reconciled. |
| User-facing lead | User asks for a short future-month shortlist | The answer opens with the practical recommendation and the relevant uncertainty. It does not open by narrating search keywords, browser actions, sort order, page coverage, or the evidence-collection workflow. |
| Method versus conclusion | User asks for recommendations, not an audit trail | The final answer keeps research method details in the internal ledger and mentions them only when they materially affect the recommendation or the user asks how the research was done. |
| Score versus specialist trade-off | A lower-score candidate has materially stronger seasonal recurrence or item-level takeaway evidence | The answer keeps one score-first ranking and gives the specialist candidate as a concise labelled swap with its trade-off, not as a second full ranking. |
| Delivery punctuation | User-facing answer is in Traditional Chinese plain text | Prose uses commas and full stops. It contains no semicolons or em dashes, and links remain naturally embedded in sentences. |
| Store naming and links | Tabelog uses a formal Japanese store name | The answer uses a Taiwan-familiar Chinese name or transliteration and embeds the Tabelog or official link in the relevant sentence. |

## Release assertions

- Every Top 3 item has a physical-storefront source, opening status, product-format classification, and exact Tabelog URL.
- Every Top 3 item has separate storefront and product-access classifications, plus requested-station distance and nearest-station/facility context.
- Every Top 3 item reports actionable transport: nearest-station walk time when no origin is given, or verified total transit time, line(s), transfer count, and final walk when an origin is given.
- Every positive product claim has a current/menu source or an explicit review visit month.
- Every high-scoring exclusion has a stated reason such as stale, analog, branch mismatch, wish-only, or format mismatch.
- Every Top 3 item has a recorded qualification decision and every unresolved Top 3 boundary has been audited.
- Future seasonal/rotating Top 3 items have product-season state `已確認` or `季節模式支持`; `條件式` items are not silently promoted.
- Collapsed review cards are expanded or explicitly labelled `內容未展開` before product evidence is classified.
- The internal ledger records retrieval date, review window, and coverage. The default answer mentions only decision-relevant freshness and stock or holiday uncertainty.
- The agent does not present parallel search methods or disconnected rankings; it presents one default score-first list plus compact, evidence-backed scenario lenses.
- The opening scenario map includes the six core lenses: overall pick, exact product/format, price/value, transport/route, availability/ease, and best regardless of price/distance.
- Seasonal/period-limited, local/branch-limited, and established/signature lenses are marked applicable, `未確認`, or `未找到` rather than being silently omitted or invented.
- Scenario lenses do not invent prices, routes, local exclusivity, seasonal status, or fame when the relevant evidence is missing; they report `未確認` or `未找到`.
- Future-month, seasonal, period-limited, local, and branch-limited outputs include an official website/SNS source, observation date, and status, or explicitly say `官方未確認`.
- Official announcements and Tabelog reviews are never collapsed into one evidence type: planned/current listing is separated from historical purchase, stock, queue, and sell-out experience.
- The output separates raw score rank from qualified rank and explains any excluded raw-score leader.
- The output separates store-level service flags from item-level access, especially when the store has `テイクアウト` but the requested item is not independently confirmed as takeaway.
- The answer opens with a practical conclusion and decision-relevant caveat rather than a description of the research workflow.
- Search keywords, sort controls, page counts, browser actions, and internal coverage details remain out of the default answer unless the user asks for an audit trail.
- When score-first and specialist lenses disagree, the answer presents one default ranking and one concise trade-off or swap, not two full rankings.
- The default user-facing prose uses Traditional Chinese plain text, Taiwan-familiar store names, naturally embedded links, and no semicolons or em dashes.
- The final response is first-person plain-text prose with a Traditional Chinese or Taiwan-familiar store name and naturally embedded Markdown links; it does not use Markdown headings, bullets, numbered lists, tables, bold, or a separate link appendix.
- Navigation integrity is verified after each route change; a two-check mismatch triggers homepage recovery and route rebuild.
- Review-card visit month, detail-page visit date, and publication date are kept as separate fields when available.
