---
name: tabelog-expert
description: Compare public Tabelog food and restaurant candidates with a default score-first evidence route plus evidence-backed decision lenses. Use when the user wants the best shops for a dish, language-normalized product search, recent or seasonal review signals, a future-month opening check, official website or social-media cross-checking, actionable walking or transit guidance, or a defensible shortlist that separates storefront, item-level product access, current evidence, historical reviews, price/value, access, seasonal certainty, local, and established-shop trade-offs.
---

# Tabelog Expert

## Decision spine

Run one canonical decision path. Do not ask the user to choose a search method. Present one default recommendation plus a compact set of decision lenses derived from the same evidence ledger; do not create disconnected searches or unsupported rankings.

```text
request contract
→ scenario map
→ score-sorted inventory
→ hard-gate screen
→ evidence audit
→ official website/SNS cross-check
→ classify seasonal certainty and item-level access
→ qualified score-first ranking
→ scenario lenses
```

At each stage, keep a small ledger and apply a stop rule:

- **Request contract:** record area/station, normalized keyword, target month/date, requested result count `N`, storefront requirement, product-access preference if stated, service preferences, review window, and ignored controls.
- **Scenario map:** prepare six core lenses every time: `整體首選`, `品項對題／購買形式`, `價格／性價比`, `交通／動線`, `可得性／省事`, and `只求最好`. Also expose the contextual lenses `季節／期間限定`, `地方特色／分店限定`, and `名店／經典招牌`, marking each as `適用`, `未確認`, or `未找到`. Use one shared candidate ledger; do not run nine disconnected searches.
- **Inventory:** inspect the first 10 relevant score-sorted cards; expand only when the hard gates leave fewer than `N` serious candidates or when the Top N score boundary is unresolved. Use `N = 3` only when the user did not specify a count.
- **Hard gates:** require a physical storefront, plausible target-month opening, acceptable product identity and format, and at least one dated product signal. Reject or label the candidate immediately when a gate fails.
- **Evidence audit:** verify current/menu evidence, then audit matching reviews newest-to-oldest through the cutoff and the same month in the prior year when available.
- **Official cross-check:** for every serious candidate, inspect the Tabelog-linked official website and/or official social account when exposed; this is mandatory for future-month, seasonal, period-limited, local, or branch-limited requests. Separate what the shop currently announces from what reviewers actually experienced.
- **State classification:** classify official status, item-level access, and product-season state before ranking. A store-level `テイクアウト` flag does not prove that the requested seasonal item can be bought to-go.
- **Navigation integrity:** after every navigation, verify page title/heading, area, keyword or category, and URL scope. If two or more checks fail, return to the Tabelog homepage and rebuild the route; never continue from a stale or misrouted result.
- **Ranking:** keep raw score rank separate from qualified rank. Rank only qualified candidates by the default score-first order, preserve the user's requested Top N, and return fewer than N only when fewer than N qualify.

## State model

Use these finite states instead of compressing uncertainty into a vague “available” label:

- **Official status:** `官方目前列出` (current item/period is listed), `官方近期公告` (first-party announcement for the upcoming/current item), `固定季節／販售期` (official recurring window is stated but the current item may not yet be posted), `歷年同期模式（今年未公告）` (prior-year official evidence or recurring pattern, not current-year confirmation), `官方未確認`, or `官方與 Tabelog 衝突`.
- **Item-level access:** `standalone takeout`／單品可帶走, `single-item dine-in`／單品內用, `course dessert`／套餐甜點, `bar/lounge dessert`／酒吧或 lounge, `seasonal pop-up`／期間櫃位, `store takeout flag only`／只有店家層級外帶標記, or `unclear`／未確認. The last two cannot be treated as proof of standalone takeaway.
- **Takeout evidence:** `已確認可外帶` when a current menu, official source, or exact recent purchase confirms item-level takeaway; `近期外帶紀錄` when a recent review records an actual purchase but the current menu is silent; `僅店家標示外帶` when only the store-level service flag is visible; or `外帶未確認` when no item-level evidence is available. Only the first two are positive item-level evidence.
- **Product-season state:** `已確認` (current official target-period announcement, or current exact product plus exact target-month evidence), `季節模式支持` (official fixed season or prior-year same-month pattern plus recent matching Tabelog evidence, while this year's exact announcement is absent), `條件式` (recent exact evidence without current or recurring target-month support), or `歷史／排除` (old, analog, wish-only, or truncated evidence).

For a future-month request, put `已確認` and `季節模式支持` in the main qualified pool, with the latter visibly caveated; keep `條件式` in a separate conditional section. If the user requires a current-year official announcement, only `官方目前列出` or `官方近期公告` plus `已確認` passes.

## Default route

Use this route for every shortlist unless an exception below is triggered. Do not start by choosing among multiple methods.

```text
recover to the Tabelog homepage
→ normalize the food keyword and user constraints
→ declare the scenario map without asking the user to choose a lens
→ search and inspect the first 10 result cards by score
→ early-screen storefront, branch, format, and target-month opening
→ retain enough serious candidates to fill Top N plus the score-boundary candidates
→ extend to 20 cards only if fewer than N can qualify or the Top N boundary is unresolved
→ verify current menu/product evidence
→ cross-check the official website and official SNS linked from Tabelog
→ audit matching reviews with 訪問月順, newest-to-oldest, for 12 months
→ inspect the same month in the prior year for seasonality
→ rank one score-first qualified list
→ derive short scenario recommendations from the same qualified ledger
→ report the requested Top N, scenario lenses, near-misses, and exclusions
```

The governing rule is: a search hit or review mention is a lead, not proof that the shop currently sells the requested item. A candidate enters the main ranking only after storefront, opening, product identity, product format, evidence freshness, and the user's service constraints have been separated.

## Route steps

1. **Recover and normalize.** Start from `https://tabelog.com/` in the Codex in-app browser. If a deep page fails, follow the homepage recovery state machine in `sites/tabelog/AGENTS.md` before researching again. Record area/station, target food, retrieval date, intended month/date, storefront requirement, user origin if provided (otherwise `未指定`), transport-output mode, distance, budget, and service preference. Translate the target into the site's visible Japanese keyword, record the exact submitted keyword, and define synonyms and false positives. For example, distinguish `ミルクレープ` from `ミルフィーユ` and from a dessert merely described as “layered.”

   Treat a physical storefront as a hard gate when requested. Treat dine-in, takeout, and reservation as independent service dimensions; if the user says they are optional, do not filter on them. If no review period is specified, use the twelve months ending on the retrieval date. Do not set reservation date, time, or party-size controls when the user only asks whether a storefront is open or whether a product is sold. Vacancy chips and booking capability are not product or opening evidence. Record the requested item’s access separately from the store’s generic service flags.

   Build the scenario map immediately after the request contract. Always expose the six core lenses:

   - `整體首選` — balance score, evidence, price, access, and opening confidence;
   - `品項對題／購買形式` — exact product match and whether it is standalone, takeout, café, course, lounge, or another format;
   - `價格／性價比` — lowest credible product cost or strongest value, with price source, portion/context, and format stated;
   - `交通／動線` — actionable access: nearest-station walking time when no origin is given; total transit time, lines, transfer count, and final walk when an origin is given. Do not expose raw metres as the main answer;
   - `可得性／省事` — likely to be open and purchasable, with reservation, queue, stock, opening-hour, and sell-out friction stated;
   - `只求最好` — highest qualified score and product strength, even when expensive, course-only, or farther away.

   Add these contextual lenses to the opening map and show their status:

   - `季節／期間限定` — strongest target-month and prior-year seasonal fit, including sold-out risk; trigger for future months, seasonal wording, or rotating menus;
   - `地方特色／分店限定` — product, branch, facility, or area-specific fit when the evidence says it is location-limited;
   - `名店／經典招牌` — established reputation, awards, long-running signature, or unusually strong review depth, without treating fame as proof of current availability.

   Keep these as short recommendation cards, not nine full investigations. Reuse the same qualified ledger, and run an additional targeted pass only when a lens depends on a candidate outside the score-sorted boundary. If a lens has no qualified candidate, say so instead of filling it with a weaker near-miss.

2. **Search and bound the inventory.** From the homepage, select the exact visible `エリア・駅` autocomplete suggestion and submit the normalized keyword. Verify at least two of title/heading, condition summary, result count, URL scope, or selected sort. Use score sorting for discovery. Inspect the first 10 relevant result cards; if fewer than N candidates can pass the hard gates, paginate up to 20 relevant cards or until the result scope is exhausted. Record name, branch, live score, review count, detail URL, distance from the requested station, nearest station, facility/branch context, and product-format hint.

   Also record scenario evidence when exposed: exact product price and price basis, venue budget band, nearest station, observed station distance, estimated or route-verified walking time, direct/indoor/transfer access, opening, stock, queue, reservation friction, area or branch-exclusive wording, award or established-shop signal, and whether the item is seasonal or limited. Missing price, access, availability, local, fame, or route evidence is `未確認`, not an invitation to infer. A result-card `テイクアウト` label is store-level evidence only; verify the exact item’s format from its menu, product photo, official source, or full review.

   Translate transport into an action the user can take. If no origin is specified, report the nearest station and an approximate walk time derived from the observed station distance, rounded up and labelled approximate; keep the raw distance in the ledger. If an origin is specified, use a current in-app route source when available and record total time, transit lines, transfer count, station exit or final walk, route source, and observation date. Never invent a transit duration or transfer count. If a route cannot be verified, state `交通路線未確認` and provide only the verified nearest-station walk estimate.

   Always resolve the ranking boundary before stopping. In addition to the apparent Top N, keep any candidate immediately below the cutoff and any higher-scoring candidate whose qualification is uncertain. Audit an equal-score tie as well as the candidate above it. This prevents a stale high-score near-miss from silently displacing a better-supported lower-score candidate.

   Classify every inspected hit as `exact item`, `variant/seasonal item`, `analog or “like” item`, `wish-only/unavailable`, `branch mismatch`, `no physical storefront`, or `unclear`. Do not spend full review-audit time on an analog, wish-only, wrong branch, or no-storefront hit.

   Keep storefront and product access separate. A physical address can host a retail counter, a café with a single-item dessert, a restaurant-course dessert, a hotel/bar lounge, or a seasonal pop-up. Use `product access` labels such as `single-item takeout`, `single-item dine-in`, `course dessert`, `bar/lounge dessert`, `seasonal pop-up`, `wish-only`, or `unclear`. When the user only requires a storefront and does not constrain format, keep all plausible formats but show the label prominently; do not make a course dessert look like a takeaway cake.

3. **Early-screen the 3–5 serious candidates.** Open each candidate's current detail page and verify page title, branch, physical address, station distance, nearest station, regular hours, holidays, facility dependency, and service flags. After each open, verify the visible title/heading, requested area or branch, target keyword/category when present, and URL scope. If two checks disagree, stop using that page, return to the homepage, and rebuild the visible route. Remove candidates with no physical storefront, wrong branch, no plausible target-month opening, or a format that clearly violates the user's request. For a future month, record a likely schedule rather than promising an exact opening date.

   Check `メニュー・コース` and current menu/dish pages before the deeper review pass. Label product evidence as:

   - `頁面目前列出` — current text explicitly names the target item;
   - `目前菜單照片可見（文字未確認）` — a current menu photo may show it, but text evidence was not confirmed;
   - `目前未列出（未等於停售）` — the checked current menu text does not name it;
   - `未確認` — the menu surface could not establish current status.

   A missing menu entry is never a discontinuation claim. Keep a candidate for the review pass when an exact or variant product signal may still be recoverable from its reviews; mark the uncertainty rather than silently treating it as current.

   Do not collapse `storefront verified` into `product independently purchasable`. Record whether the target is a standalone retail/takeout item, a café order, or a dessert included only in a meal or course. If the user did not specify format, treat format as an output caveat and a ranking tie-breaker, not as an invisible exclusion. If only the store-level takeout flag is visible, use `store takeout flag only` until item-level evidence is found. For a strict takeaway request, do not qualify the candidate on this state alone.

4. **Cross-check official sources.** For every serious candidate, inspect the official website and official social account linked from the candidate's Tabelog page when exposed. This is mandatory for future-month, seasonal, period-limited, local, and branch-limited requests, and is the default corroboration pass for stable items. If no first-party link is exposed, record `官方未確認` rather than silently skipping the field. Stay in the same Codex in-app browser and read only. Do not follow reservation, ordering, payment, login, or third-party booking flows.

   Verify the account identity from Tabelog's own link or the shop's official detail page; do not treat an aggregator, map listing, influencer post, or unlinked account as official. Check the fields that can change the recommendation: exact item/variant, target-month or sale window, branch/location, takeout/dine-in/reservation format, stock/order/queue rules, hours, holidays, and temporary closure notices. Record the official URL, source type (`official_site` or `official_sns`), observation date, and the state from the official-status model. Distinguish a current-year announcement from `固定季節／販售期` and `歷年同期模式（今年未公告）`; the latter two support a seasonal pattern but never become current-year confirmation.

   Keep source roles separate. An official menu or post is evidence that the shop currently lists or announces an item and period; it is not proof of same-day stock. A Tabelog review is evidence of an actual historical purchase or visit; it is not proof that the item is still listed. When they disagree, use the official current source for the planned/current listing and scheduled period, use recent Tabelog reviews for real-world stock, queue, and purchase friction, and state the conflict explicitly. If the official source is unavailable or silent, record `官方未確認`, lower confidence, and never invent a current or seasonal status.

5. **Audit current and historical product evidence.** For each serious candidate, open `口コミ`, enter the target keyword in the visible review `キーワード` field, submit, then select visible `訪問月順`. If submitting resets the sort, select it again. Confirm the visible sort state and, when exposed, URL state such as `srt=visit&sby=D`; do not proceed on button success alone.

   Read full visible review cards, not only result snippets or titles. Expand the newest three matching cards and any card containing seasonal, sold-out, unavailable, branch, or contradictory cues. When a card exposes `もっと見る`, `続きを読む`, or an equivalent expansion control, activate the currently visible control and take a fresh snapshot before deciding that the exact product is absent. If the card cannot be expanded, record `內容未展開` and lower evidence confidence; do not convert a truncated snippet into negative evidence. Paginate until the twelve-month cutoff is covered, then stop; do not browse older pages unless the prior-year comparison or an exclusion reason requires it. Record separately:

   - `訪問月` — when the reviewer bought or ate the item;
   - `投稿日` — publication date, or `未取得` when not exposed;
   - exact item/variant, price, order or purchase context, stock cue, and negative qualifier;
   - product format: retail/takeout, café menu, restaurant-course dessert, hotel lounge, buffet, seasonal pop-up, or wish-only.

   When a review detail page exposes dates, preserve all three date surfaces: review-card `訪問月`, detail-page visit month/date, and `投稿日`. If they disagree, record both values, explain the mismatch, and lower confidence; never silently substitute publication date for visit date.

   Treat the review pass as an evidence extraction task. For every positive claim, retain the review URL, visit month, exact product wording, and freshness label. A recent review establishes recent appearance or purchase, not same-day stock. A review that only says the reviewer wanted, searched for, or failed to buy the item is negative or wish-only evidence, not a product match.

   For a future month, inspect the same month in the prior year when present. A newest matching visit outside the review window is `歷史曾出現` or `過期`, even if the live score is high. Review evidence can establish that the product appeared, but cannot by itself prove today's stock.

   For a future month, assign the product-season state from the state model. `季節模式支持` is usable in the main pool only when the official recurring/prior-year signal and recent matching purchase evidence agree; show that this year's exact announcement is absent. Keep `條件式` candidates as labelled near-misses; do not fill Top N with them merely to reach N results. For non-seasonal, stable items, a current menu or recent exact-product signal can satisfy the product-season check without a prior-year match.

6. **Apply the qualification gate.** A candidate qualifies for the main list only when all applicable gates pass:

   - physical storefront verified;
   - target-month status is `正常營業日推定`, `設施營業日依存`, or `指定日期已確認` (not `指定日期未確認` unless the uncertainty is explicitly acceptable);
   - product is exact or an explicitly acceptable variant, not analog-only or wish-only;
   - product access format matches the request, or is clearly labelled when the user left format open;
   - at least one current/menu, recent, or historical product signal is stated with its freshness and caveat.

   For a future seasonal or rotating item, also require product-season state `已確認` or `季節模式支持`. A physical restaurant with a recent course mention can pass the storefront gate while remaining `條件式` for the target-month product; keep it out of the main ranking until the stronger evidence is present. The official-source pass is mandatory for future-month, seasonal, period-limited, local, and branch-limited requests. If no official source can be verified, a candidate may remain qualified only when the independent Tabelog evidence passes, but it must be marked `官方未確認`, have reduced confidence, and never be described as officially announced. If the user explicitly requires an official current announcement, `官方目前列出` or `官方近期公告` plus `已確認` is a hard gate.

   Keep rejected high-score candidates as near-misses with one concrete exclusion reason. Do not fill Top N with stale, unclassified, branch-mismatched, analog-only, or wish-only candidates.

7. **Rank one default list, then apply scenario lenses.** Record both `raw score rank` (the score-sorted inventory position) and `qualified rank` (after all gates). Rank qualified candidates in this order: live score, product-match strength, evidence freshness, recent review quality, seasonal fit, opening confidence, then service fit. This is the default `整體首選`/score-first ranking. Then select one qualified candidate for each core lens using only the relevant evidence: exact product and format for `品項對題／購買形式`, product price/value for `價格／性價比`, actionable route for `交通／動線`, opening/stock/queue/reservation friction for `可得性／省事`, score and product strength for `只求最好`, and the full balance for `整體首選`. Apply the contextual lenses `季節／期間限定`, `地方特色／分店限定`, and `名店／經典招牌` when their evidence is relevant. For seasonal, future-month, local, or branch-limited claims, give official current/announcement evidence its own citation and do not substitute a review summary for it.

   Do not force every lens to produce a different store. The same candidate may win several lenses, and a lens may have no qualified winner. Do not let a scenario winner silently replace the default Top N; label it as a lens-specific recommendation and state the trade-off.

   Apply the order only after qualification. If a higher-scoring candidate fails a hard gate, do not promote it through a weaker caveat; show it as a near-miss and state the failed gate. If two qualified candidates tie, use product-match strength and evidence freshness as tie-breakers, then state the tie. A price, transport, seasonal, local, or fame advantage never repairs a failed storefront or product-evidence gate.

   If fewer than N candidates qualify, return fewer than N and show near-misses separately. Explain every higher-scoring exclusion. When the raw-score leader is excluded or conditional, name it explicitly as the `raw score leader` and state why it did not become the qualified winner.

   When score-first ranking and a specialist lens produce different winners, keep one default ranking and state the swap in one concise sentence. For example, identify the higher-scoring candidate as the score-first choice and the lower-scoring candidate as the seasonal or item-access choice. Do not create a second full ranking from the lens.

## Exception paths

Use only the matching exception; return to the default route afterward.

| Trigger | Action |
|---|---|
| Deep page or review page fails | Return to `https://tabelog.com/`; if a data-URL error blocks navigation, create a fresh tab in the same in-app browser; rebuild the search from visible UI. If the homepage also fails, report a connectivity gap and fabricate no shortlist. |
| Browser tab is stale, missing, or closed | Keep the same in-app browser binding, discard the stale tab handle, create a fresh tab, verify the homepage title/heading/search controls, and rebuild the search. Never switch browsers or retry the stale handle. |
| Locator or click fails | Do not repeat the same locator blindly. Re-read the fresh visible DOM, find the currently visible equivalent by text/role, and use only its observed href or node. After navigation, verify heading, URL, and selected sort. |
| Navigation integrity mismatch | If title/heading, area, keyword/category, or URL scope does not match the intended route and at least two checks fail, return to `https://tabelog.com/`, verify the homepage, and rebuild. Treat autocomplete misrouting or a nationwide/other-category result as a route failure, not a valid fallback. |
| Exact keyword returns no useful hits | Run one visible synonym or Japanese equivalent pass, record the change, and keep analog results labelled rather than silently broadening the target. |
| Review keyword or `訪問月順` is absent | Use the current visible equivalent only if the resulting order can be verified; otherwise label review order unverified and lower confidence. |
| Review card is collapsed | Expand the visible `もっと見る`/`続きを読む` equivalent for the newest three or relevant contradictory cards, then re-read the card. If expansion is unavailable, label the content unexpanded and do not treat absence from the snippet as negative evidence. |
| Current menu omits the item | Keep `目前未列出（未等於停售）`; use recent or historical reviews only as dated evidence, never as current-stock proof. |
| Future month depends on a facility | Use `設施營業日依存`; do not promise exact holiday opening, seasonal stock, or standalone purchase. |
| Target month has a recurring weekly schedule | Convert the schedule into the target month's likely weekdays/dates when calendar information is available, but label it `正常營業日推定` and preserve temporary-closure uncertainty. |
| Official source only shows prior-year recurrence | Label it `歷年同期模式（今年未公告）` and `季節模式支持` only when recent matching purchase evidence also exists; do not call it a current-year announcement. |
| Fewer than N pass | Stop the main ranking at the number that passes; list the nearest exclusions. |
| User asks for a different priority | Change only the final ranking order; keep the same evidence collection and hard gates, and state the changed priority. |
| User asks about transport without an origin | Report the nearest station and approximate walk time from the observed distance; do not invent a transit route. |
| User provides an origin | Verify a current in-app route when available and report total time, transit line(s), transfer count, and final walk; if unavailable, state `交通路線未確認`. |

## Output contract

Lead with the recommendation and its decision-relevant limitation. Do not open with the workflow, browser actions, search keywords, sort controls, page coverage, or a diary of how the evidence was collected. Avoid phrases such as `我先搜尋`, `我再切成訪問月順`, `我查看了幾頁`, or `我使用了以下方法`. If the user asks how the research was done, provide that audit separately after the recommendation.

For a future or seasonal request, state the practical conclusion in plain language, such as `今年十一月值得優先確認的店家如下` or `今年十一月目前尚未有官方限定公告`. Do not present `今年未公告` as a current-year confirmation. Show `已確認`, `季節模式支持`, `條件式`, or `官方未確認` only when the label helps the user choose. Do not expose the internal state model as a process explanation.

Preserve the user's requested result count. If the user asks for Top 5, return five qualified paragraphs when five pass the gates; do not silently collapse the answer to Top 3. For a short request, report only the requested ranking and the one or two caveats that change the decision. The full scenario map remains internal unless a lens materially changes the recommendation.

User-facing output must be first-person Traditional Chinese plain-text paragraphs. Apply [name-normalization.md](../../sites/tabelog/references/name-normalization.md) as a hard output gate. Use a Traditional Chinese or Taiwan-familiar transliteration as the primary shop and product name, and use `中文名稱（原文名稱）` only when the original helps identification. A raw Japanese name must never be the primary display label. Let the Tabelog link carry the formal Japanese name. Embed Tabelog, official-site, and SNS links naturally inside the relevant sentence. Do not use Markdown headings, bullets, numbered lists, tables, bold, or a separate link appendix. Use Chinese commas and full stops for prose. Do not use semicolons or em dashes in the user-facing answer.

Before returning, run the final language QA: every shop and product has `name_zh` or a Taiwan-familiar transliteration, no raw Japanese name appears outside parentheses, source links, or required search terms, and the surrounding prose is Traditional Chinese. If any candidate fails, normalize it before ranking or return. Do not use the source language as a reason to skip this gate.

Present the default score-first Top N as plain paragraphs beginning with labels such as `第一名是` or `我會先選`. If a specialist or more practical candidate would replace a score-first candidate, explain the trade-off in one short paragraph rather than creating a second ranking. Keep near-misses brief and give each one primary exclusion reason.

If the user did not provide an origin, write the nearest-station walk time. If an origin was provided, write the verified transit time, line(s), transfer count, station exit, and final walk. Keep raw metres and unverified route data out of the main prose unless they clarify a caveat. Keep retrieval date, normalized keyword, review window, inventory coverage, and ignored reservation controls in the internal ledger. Mention them in the answer only when they materially change the recommendation or the user explicitly asks for the audit trail.

Internal-only ledger templates; never render these tables in the user-facing answer.

| Lens | Recommendation | Why it wins | Trade-off / confidence |
|---|---|---|---|
| 整體首選 | one qualified candidate | score and evidence balance | state the main compromise |
| 品項對題／購買形式 | one qualified candidate or `未找到` | exact product and access format | course/takeout/café caveat |
| 價格／性價比 | one qualified candidate or `未找到` | exact product price/value evidence | price basis and format |
| 交通／動線 | one qualified candidate or `未找到` | nearest-station walk time, or verified origin-to-store route | adjacent station/facility or unverified-route caveat |
| 可得性／省事 | one qualified candidate or `未找到` | opening, stock, queue, reservation friction | same-day uncertainty |
| 只求最好 | one qualified candidate or `未找到` | highest qualified score/product strength | price and distance |
| 季節／期間限定 | 適用候選、`未確認`或`未找到` | current, recent, and prior-year month fit | stock/season caveat |
| 地方特色／分店限定 | 適用候選、`未確認`或`未找到` | explicit local/branch/facility evidence | wording may be historical |
| 名店／經典招牌 | 適用候選、`未確認`或`未找到` | reputation/award/signature evidence | fame is not availability |

Then use one main evidence matrix:

| Store | Raw score / qualified rank | Station scope / storefront / opening | Item-level access | Tabelog evidence | Official source / status | Product-season state | Visit month / 投稿日 | Service | Confidence | Caveat |
|---|---:|---|---|---|---|---|---|---|---|---|

Maintain one internal evidence matrix, but render the final answer as the plain-text paragraphs required above. Give exact Tabelog detail, relevant review/menu links, and the official website/SNS link or explicit `官方未確認` for every serious candidate. Distinguish `頁面目前列出`, `近一年曾買到`, `歷史曾出現`, `目前未列出（未等於停售）`, and `未確認`. For future-month, seasonal, period-limited, local, or branch-limited requests, show official observation date, official status, product-season state, and item-level access in the prose. If the source is silent or unavailable, say `官方未確認`. Include the raw-score leader when it is excluded, with one primary reason. End with the stock/holiday disclaimer: official announcements describe a planned/current listing but do not guarantee same-day stock, reviews are subjective and historical, menu pages can lag, and same-day confirmation is needed for limited items, sold-out risk, facility holidays, and future dates.

For each Top N recommendation, make the qualification decision auditable in prose: include raw score rank and qualified rank, nearest station and walk time, or origin-to-store transit time, line(s), transfer count, and final walk when an origin was provided; also include facility/branch context, storefront source, opening status, item-level access, takeout evidence, product-season state when applicable, strongest current/recent Tabelog evidence, official source/status and observation date (or `官方未確認`), `last_checked_at`, confidence when medium or low, both visit month and publication date when available, and one concrete caveat. For the scenario map, include the exact price source or `未確認`, the transport basis, and the evidence that supports seasonal, local, or fame claims; official claims and Tabelog experience must remain separate. If a specialist or more practical alternative is useful but ranks below the score-first list, show it as a labelled lens recommendation, not as an unlabelled second ranking. Put a short plain-text format warning before the recommendations when the list mixes takeaway, café, course, hotel, or bar desserts.

## Evidence and browser safety

- Use the fields in [audit schema](references/audit-schema.md). Every material claim must identify source surface and URL, observation date, evidence level, freshness, and uncertainty. Use `Strong/current`, `Recent`, `Historical`, or `Weak/non-qualifying`.
- Keep exploration read-only. Do not log in, save, mark `行った`, publish or edit reviews/photos, submit a reservation, pay, or follow an external booking flow.
- For future-month, seasonal, period-limited, local, and branch-limited requests, follow the official site/SNS linked from Tabelog and record the official URL, source type, observation date, status, and consistency with Tabelog. Never treat an unlinked aggregator or social account as official.
- After a locator click fails, inspect fresh visible DOM and use DOM-based CUA only for a currently visible node. After navigation, verify title/heading, area, keyword/category, URL scope, and selected sort. If two integrity checks fail, recover through the homepage before continuing.
- Treat one locator failure as a state change: refresh the visible DOM before retrying, prefer an observed visible href when the site exposes one, and never guess pagination or sort URLs.
- Treat a stale/missing tab as a tab-state failure, not a site failure: create a fresh tab in the same selected browser, confirm the homepage, and rebuild the visible route.
- When a review card is truncated, expand it through the visible page control before assigning positive or negative product evidence; preserve `內容未展開` when that control cannot be used.
- Stop on CAPTCHA, security interstitial, unclear third-party authentication/booking, or a homepage that also fails after recovery. Do not bypass it.
- Re-read dynamic scores, counts, hours, menu, prices, and availability on current pages. Never write live rankings, stock states, counts, or one-off restaurant results into this skill.
- If the UI changes, use the stable visible equivalent safely and update this skill only after the replacement is verified. Use [forward tests](references/forward-tests.md) after material workflow changes; `quick_validate.py` checks structure, not browser behavior.

## References

- [Tabelog site guidance](../../sites/tabelog/AGENTS.md) — canonical browser, homepage recovery, freshness, authentication, and safety rules.
- [Audit schema](references/audit-schema.md) — evidence ledger, labels, and output fields.
- [Forward tests](references/forward-tests.md) — behavioral cases and acceptance assertions.
- [Tabelog Search](../tabelog-search/SKILL.md) — area autocomplete, keyword search, filters, and result verification.
- [Tabelog Restaurant](../tabelog-restaurant/SKILL.md) — current detail, menu, review, photo, rating, map, and availability fields.
- [First-party guidance](../../sites/tabelog/references/first-party-guidance.md) — the meaning and limits of Tabelog reviews and scores.
- [Name normalization](../../sites/tabelog/references/name-normalization.md) — Chinese display names, original-name handling, and final language gate.
