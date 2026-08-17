# Semiconductor cycle and leading-indicator methodology

Use this reference for broad semiconductor outlooks that compare IC design, memory modules, foundry, original memory makers, consumer end markets, server demand, and front-end equipment. It records a reusable cycle-reading method, not current report conclusions, prices, company recommendations, or dated forecasts.

## Research model

Analyze the chain as:

`end-market demand → chip design orders → foundry/IDM production → utilization and inventory → equipment capex → supplier revenue and margin`

Track three dimensions separately:

- **leading, coincident, and lagging** position in the supply chain;
- **consumer, server, industrial, and automotive** demand sensitivity;
- **volume, price, inventory, capacity, and capex** as different signals.

The same company can be a leading indicator for one product and a lagging indicator for another. Record the product and end market before assigning its cycle role.

## Indicator hierarchy

### 1. Leading indicators

Start with demand-facing companies and observable customer behavior:

- IC design order, revenue, inventory, and customer shipment;
- memory-module sales, inventory, spot/contract pricing, and end-market mix;
- smartphone and PC unit forecasts, channel inventory, and pre-buying;
- customer guidance, cancellations, allocation, and purchase timing.

Use historical revenue-growth turning points as evidence of lead/lag, but verify the sample period, product mix, accounting basis, and whether the relationship survives the current cycle.

### 2. Coincident indicators

Then inspect:

- foundry/IDM wafer starts, utilization, wafer pricing, node mix, and inventory;
- memory bit shipment, ASP, product mix, inventory, and gross margin;
- server and hyperscaler procurement, capex, and accelerator deployment;
- package/test loading and production output.

Coincident does not mean contemporaneous in every quarter. Record the production and customer-qualification lag between an order and recognized revenue.

### 3. Lagging indicators

Finally inspect:

- front-end equipment orders, backlog, shipment, installation, and service revenue;
- fab construction, cleanroom completion, tool move-in, qualification, and ramp;
- facility, parts, and subsystem suppliers whose revenue follows customer capex;
- depreciation, utilization, and cash flow after capacity is installed.

Never infer equipment demand from a chip-demand headline alone. Trace the chain through capacity, capex approval, order, shipment, installation, qualification, and revenue.

## Demand sensitivity and pre-buying

Separate:

- real end-demand growth;
- tariff, subsidy, or policy-driven pre-buying;
- inventory replenishment;
- shortage allocation and price inflation;
- product transition, such as a new memory standard or node;
- structural AI/server demand.

Consumer electronics usually react faster to confidence, policy, and channel inventory than industrial or automotive demand. Server and infrastructure capex may be more durable but can be concentrated in a few customers and arrive later. A strong leading indicator can therefore weaken while a coincident or lagging group is still reporting growth.

## Time-lag checks

For each claim, map:

1. end-market order or sell-through;
2. design-company shipment and inventory;
3. wafer starts, foundry order, or memory production;
4. package/test output and customer qualification;
5. utilization, pricing, and product mix;
6. capex approval and equipment order;
7. tool shipment, installation, and production ramp;
8. supplier revenue, margin, free cash flow, and valuation.

Record the expected lag in quarters rather than treating a historical correlation as a fixed law. A supply shock, product transition, customer concentration, or policy event can shorten or lengthen the lag.

## Role matrix

| Role | What to verify | Common false positive |
|---|---|---|
| Consumer IC design | end-market units, customer inventory, order visibility, product mix, and revenue turning points | one customer or product cycle treated as the entire logic market |
| Memory module | spot/contract price, inventory cost, turns, end-market mix, and sell-through | module revenue growth treated as durable memory demand |
| Foundry/IDM | wafer starts, utilization, node/product mix, pricing, inventory, and customer concentration | fab revenue growth treated as new end demand without inventory evidence |
| Server/hyperscaler | capex, accelerator deployment, storage/network demand, procurement, and customer concentration | announced capex treated as immediate semiconductor revenue |
| Memory original maker | bit shipment, ASP, product mix, capacity allocation, inventory, margin, and capex | total data-center spending treated as immediate memory bits |
| Front-end equipment | customer capex, tool category, order/backlog, shipment, install, qualification, and service | equipment order assumed to repeat across all customers and tools |
| Parts/facility/subsystem supplier | installed base, customer fab, utilization, recurring service, and cash collection | customer fab announcement treated as supplier revenue |

Mark every company as `explicit`, `inferred`, or `unverified`, and record the report section supporting the role.

## Forecast ledger and invalidation triggers

For every forecast, record the claim, indicator class, end market, product, expected lead/lag, customer, inventory/capacity assumption, timing, evidence stage, company role, and status: `not_tested`, `supports`, `weakens`, `cannot_test`, or `unresolved`.

Re-evaluate the thesis when:

- pre-buying is mistaken for sell-through or recurring demand;
- channel inventory rises while company revenue still looks strong;
- leading indicators weaken but the assumed lag is no longer supported;
- AI/server demand is concentrated, delayed, or offset by consumer weakness;
- foundry utilization, wafer starts, pricing, or margin fail to follow design demand;
- equipment orders are cancelled, delayed, or not followed by installation and qualification;
- product transition or yield issues alter the expected capacity and pricing curve;
- a historical lead/lag relationship breaks because product mix or business model changed.

## Output requirements

For every broad semiconductor report or company, produce:

1. supply-chain position and indicator class;
2. end-market and product mix;
3. leading, coincident, and lagging evidence;
4. demand, inventory, price, capacity, utilization, and capex assumptions;
5. expected time lags and evidence stage;
6. company role, current operating checks, and cash-flow/valuation checks;
7. catalysts, invalidation triggers, and time horizon;
8. historical report claims separated from current metrics and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat a leading-indicator table or concept-stock list as a recommendation.
