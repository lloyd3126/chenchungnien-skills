# Statement Dog research evidence contract

Use this contract for every industry-report series and every report-to-company handoff. It defines the common method shared by the domain references; those references add product-specific indicators and invalidation conditions.

## Choose the evidence mode first

Record one of these modes before reading:

- `current_site`: inspect the live Statement Dog page in the Codex in-app browser and record the observation time and visible update state.
- `local_snapshot`: use only the files supplied by the user or already saved locally. Record the capture time when available and do not browse unless the user later authorizes it.
- `mixed`: historical claims come from local files and current evidence comes from a separately authorized live check. Keep the two observation dates separate.

In `local_snapshot` mode:

1. Start from the archive manifest when one exists, but treat it as an inventory rather than article evidence.
2. Read each saved HTML article and visually inspect its local images. Use a text fallback only when the HTML or image cannot be rendered.
3. Preserve the saved order, source URL, report date, capture time, image count, and comment-state metadata.
4. Treat `not_present_at_read_time` as a capture state, not proof that comments never existed.
5. Never infer a current price, ratio, filing, news item, UI label, or current report inventory from the snapshot. Mark these `current_not_checked`.

## Normalize scope before comparing claims

For every claim, identify:

- product, technology, or process route;
- end market and customer type;
- geography and policy regime;
- period and forecast horizon;
- unit of analysis, such as units, bits, capacity, ASP, price per TB, wafer starts, tool orders, installed tools, or recognized revenue;
- company role and the share of business actually exposed to the thesis.

Two statements are not contradictory until these dimensions are comparable. A later report may be an update caused by a different product, customer, geography, time horizon, or cycle phase.

## Build a claim record

Give every material claim a stable ID and record:

| Field | Required content |
|---|---|
| source | report/file, date, section or visual, and capture/observation time |
| claim | concise paraphrase without strengthening the original wording |
| claim type | `report_fact`, `author_assumption`, `forecast`, `historical_example`, `reader_question`, `official_clarification`, or `inference` |
| scope | product, end market, geography, period, unit, and company role |
| causal mechanism | why the author expects the claim to affect supply, demand, price, capacity, or a company |
| confirming trace | the operating or financial indicator expected if the claim is right |
| disconfirming trace | the event or indicator that would weaken or invalidate it |
| evidence stage | concept, order, shipment, installation, qualification, productive volume, repeat order, or financial contribution when applicable |
| status | the validation and series labels defined below |

When a chart or diagram is the evidence, describe what the visual actually shows and what it cannot establish. An illustration is context, not quantitative proof.

## Reconstruct the causal chain

Use the smallest chain that explains the thesis:

`end demand → units/bits/content → inventory and usable supply → price/mix → company role → revenue → margin → cash flow → valuation expectations`

For equipment or commercialization stories, insert the required timing ladder:

`plan/capex → order → shipment → installation → qualification → productive utilization → repeat order/service → revenue and cash flow`

For each step, ask whether it is observed, assumed, forecast, or still unknown. Do not jump from industry demand to company revenue without proving role exposure, customer access, qualification, timing, and economic significance.

Classify the thesis driver when useful:

- `structural`: a durable change in workload, architecture, regulation, or customer behavior;
- `cyclical`: inventory, utilization, price, replacement, or capex normalization;
- `product_transition`: substitution, generation change, redesign, or qualification;
- `policy_or_pull_forward`: tariffs, subsidies, controls, pre-buying, or demand timing shifts.

One claim may contain more than one driver; keep their evidence and failure conditions separate.

## Use two status dimensions

Do not mix a report-series narrative change with the strength of external evidence.

### Series evolution

- `持續`: the later report preserves the same mechanism and comparable scope.
- `更新`: the mechanism remains but scope, timing, or indicator changes.
- `轉折`: the direction or dominant mechanism changes.
- `失效`: a stated assumption or forecast is contradicted within comparable scope.
- `未驗證`: the expected evidence date or event has not arrived.
- `資料不足`: the available source cannot support a judgment.

### Claim validation

- `not_tested`: no independent validating evidence has been reviewed yet.
- `supports`: independent dated evidence matches the expected trace.
- `weakens`: independent dated evidence moves against the expected trace.
- `cannot_test`: the needed metric is unavailable, protected, stale, or outside the source mode.
- `unresolved`: evidence is mixed or the horizon has not closed.
- `not_applicable`: the metric does not fit the company role or claim.

A later report repeating an earlier claim proves continuity only. It is not `supports` unless an observable operating metric, official disclosure, or clearly dated event also confirms the mechanism.

## Company handoff gate

Before opening ratios or assigning a candidate status, establish:

1. verified company identity and ticker;
2. `explicit`, `inferred`, or `unverified` appearance in the report;
3. exact product, process, customer, and supply-chain role;
4. exposure size or `unknown` when segment contribution is not disclosed;
5. competitive-advantage hypothesis, such as cost, yield, technology, qualification, switching cost, customer access, scale, capacity, service base, or balance-sheet endurance;
6. expected operating trace and then the expected revenue, margin, working-capital, capex, and cash-flow trace;
7. the earliest event that would invalidate the handoff.

Only after this gate should the company enter the fixed financial and valuation workflow. Being named, passing a screen, receiving an order, or appearing in a supply-chain diagram is not a recommendation and is not proof of material revenue.

## Data-quality checks

Before comparing values, confirm:

- consolidated versus standalone statements;
- single-quarter, cumulative, trailing-twelve-month, or annual periods;
- average versus ending balance in turnover and return ratios;
- units versus value, bits versus devices, and capacity versus productive output;
- currency, scale, restatement, and fiscal versus calendar quarter;
- one-time gains/losses, tax effects, impairments, and asset sales;
- share-count changes, convertibles, treasury stock, and dilution;
- backlog versus cancellable orders versus recognized revenue;
- announced capacity versus installed, qualified, and usable capacity.

Financial companies and other structurally different business models require role-specific definitions and should not inherit ordinary operating-company thresholds silently.

## Minimum output

Every completed research record should state:

- source mode, scope, and completeness;
- claim records and series timeline;
- causal chain and key assumptions;
- candidates with source section and role status;
- role-specific operating and financial traces;
- series-evolution and claim-validation statuses, including `not_tested` when validation has not begun;
- risks, unknowns, next check, and observation date;
- a clear boundary between historical evidence and current evidence.
