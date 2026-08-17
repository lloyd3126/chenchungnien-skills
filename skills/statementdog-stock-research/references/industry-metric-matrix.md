# Industry-chain metric matrix

Use this reference after an industry report or thesis identifies companies across a supply chain. It selects indicators by business role without replacing the fixed company research order or the domain methodology.

## Role-exposure gate

Before selecting metrics, confirm:

1. exact product, process step, customer/end market, geography, and period;
2. `explicit`, `inferred`, or `unverified` source status;
3. whether the company benefits through units/bits, ASP, mix, utilization, content, equipment orders, service, or inventory timing;
4. exposure size, or `unknown` when segment contribution is not disclosed;
5. evidence stage from concept/order through qualification, productive volume, repeat demand, and financial contribution;
6. competitive-advantage hypothesis and its measurable failure condition.

If these cannot be established, keep the company as an unverified candidate. A supply-chain label is not a financial exposure.

## Evidence chain

For each candidate, connect:

`historical claim → normalized scope → company role → operating trace → financial trace → valuation expectation → invalidator`

Record historical report/capture date separately from current observation date. In offline mode, current evidence remains `current_not_checked`.

## Role matrix

| Role | Leading operating trace | Financial confirmation | Competitive-advantage evidence | Common false positive |
|---|---|---|---|---|
| End customer, cloud, or system buyer | capex, procurement, deployment, utilization, retained workload, customer acceptance | segment growth, capex intensity, cash generation | scale economics, ecosystem, utilization, switching cost | announced capex treated as immediate supplier demand |
| Brand, OEM, ODM, or system integrator | orders, backlog quality, configuration, component allocation, integration yield, shipment, acceptance | revenue/product mix, margin, inventory, receivables, CFO | customer access, design/integration ability, supply-chain execution | component shipment or backlog treated as recognized system revenue |
| IC designer, controller, or interface supplier | design win, platform, attach rate, qualification, unit/content, customer inventory | revenue mix, gross margin, R&D intensity, receivables, cash flow | IP, software/firmware, ecosystem, switching cost | design win or controller shipment treated as end-product volume |
| Foundry, IDM, or original manufacturer | units/bits/wafer starts, ASP, utilization, yield, inventory, product mix, qualification, capex | revenue, gross/operating margin, depreciation, CFO/FCF | process/yield, cost, scale, capacity, customer trust | price/mix growth treated as unit demand or announced capacity as usable supply |
| Mature-product manufacturer | spot/contract spread, substitution, utilization, inventory, customer redesign | revenue, margin, inventory days, CFO | cost position, installed customer base, disciplined supply | shortage assumed to persist after substitution or capacity response |
| Advanced-product supplier | sample, design validation, generation ramp, package/process capacity, yield, contract coverage | ASP/mix, margin, capex, cash conversion | performance, yield, qualification, scarce capacity | sample, roadmap, or one customer treated as mass production |
| OSAT, packaging, or test | package/test units, utilization, product mix, outsourcing, pricing, capacity | related revenue, margin, capex, CFO | process yield, customer qualification, package portfolio | chip-price increase treated as packaging-volume growth |
| Equipment OEM or specialist | customer capex, tool category, order, backlog, shipment, installation, acceptance, service attach | equipment/service mix, margin, inventory, receivables, CFO/FCF | process performance, approved-vendor position, installed base/service | customer capex or purchase order treated as productive tool revenue |
| Equipment part, module, or integration partner | content per tool, OEM/customer, qualification, capacity, yield, repeat order | product revenue, margin, working capital, cash collection | sole/primary source, precision capability, qualification | OEM relationship treated as direct end-customer share |
| Facility engineering or project contractor | cleanroom/utilities readiness, project scope, backlog, completion, collection | revenue recognition, margin, contract assets, receivables, CFO | execution, customer access, safety/quality record | fab announcement or backlog treated as recurring profitable revenue |
| Material, substrate, chemical, or consumable supplier | specification, qualification, recurring consumption, capacity, utilization, lead time, pass-through | product mix/margin, inventory, capex, CFO | material know-how, reliability, qualification, cost/pass-through | sample or supply-chain map treated as locked production share |
| Module, distributor, or channel company | shipment, selling price, inventory cost, inventory days, sell-through, channel/customer mix | gross margin, working capital, CFO/FCF | procurement, channel access, inventory discipline | low-cost inventory creates temporary margin mistaken for durable power |
| Mechanical or unit-linked component | content per device, unit shipment, platform, customer, utilization, qualification | revenue/margin, inventory, receivables, cash flow | content gain, precision/yield, qualified share | bit/capacity growth treated as device-unit growth |

## Competitive-advantage test

Do not describe an advantage only with adjectives. For each claimed moat, record its evidence and expiry risk:

- technology/process: measurable performance, defect rate, yield, throughput, or roadmap execution;
- qualification/customer access: approved-vendor position, design-in duration, repeat order, or switching cost;
- cost/scale: unit cost, utilization, purchasing, learning curve, or depreciation absorption;
- capacity/lead time: qualified usable capacity and customer commitment, not nominal announcements;
- service/installed base: service attach, recurring parts, uptime, and retention;
- balance sheet: ability to fund a downcycle or productive expansion without damaging dilution or leverage.

An advantage is supported only when the operating trace and financial economics both persist. Market growth alone does not prove company advantage.

## Required interpretation

For every metric, separate:

- `observed`: source, period, definition, and value/event;
- `interpretation`: what it suggests through the causal mechanism;
- `risk`: alternative explanation or invalidator;
- `unknown`: unavailable, protected, stale, ambiguous, or `current_not_checked`;
- `next_check`: exact monthly, quarterly, filing, qualification, installation, or customer event.

## Cross-checks

- Revenue up, units/bits/content flat: test ASP, mix, pull-forward, and inventory timing.
- Margin up, CFO flat: test receivables, inventory, payables, one-offs, and capitalization.
- Capex up, revenue flat: test cleanroom, tool installation, qualification, yield, ramp, and depreciation.
- Backlog up, shipments flat: test cancellations, components, integration, acceptance, and revenue timing.
- Orders up, service/utilization flat: test whether tools are installed and productive.
- Capacity announced, price still rising: test usable qualified supply rather than nameplate capacity.
- ROE up: decompose net margin, asset turnover, leverage, buybacks, one-offs, and dilution.
- Low PE/PB: test whether normalized earnings, margins, industry economics, or asset quality are deteriorating.
- Price up: treat expectations as context; seek operating and cash-flow confirmation.

This matrix creates a test plan, not an automatic pass/fail rule or recommendation.
