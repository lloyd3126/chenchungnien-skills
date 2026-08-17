# Semiconductor front-end equipment research methodology

Use this reference for wafer-fab equipment, WFE, lithography, etch, deposition, inspection, memory equipment, logic-process equipment, equipment suppliers, and fab-facility engineering reports. It records a reusable research method, not current report conclusions, prices, company recommendations, or dated forecasts.

## Research model

Analyze the chain as:

'end-demand and product mix → wafer-fab utilization and node transition → customer capex → cleanroom and facility readiness → tool order and delivery → installation and qualification → productive capacity and utilization → equipment revenue, service, margin, and cash flow'

Do not treat a customer's announced capex as immediate equipment revenue. A fab can be short of cleanroom space, utilities, qualified operators, or process demand even when the budget is approved.

Always separate:

- lithography exposure, including EUV and DUV;
- etch and selective etch;
- deposition and thin-film formation;
- inspection, metrology, and process control;
- memory-layering equipment;
- advanced-packaging equipment, which may have a different cycle from front-end WFE;
- facility engineering, cleanroom, gas, water, and utility work.

## Demand and equipment map

### 1. Start from end demand

Map the demand to product and node:

- AI training and inference: GPU, AI ASIC, CPU, HBM, DDR, networking, storage, and enterprise SSD;
- agentic AI: additional inference loops, state retention, RAG reads/writes, intermediate data, and longer task duration;
- logic: node migration, transistor architecture, GAA, backside power, and advanced packaging;
- DRAM: HBM, server DRAM, mature DRAM, and process migration;
- NAND: layer count, enterprise SSD, controller, and capacity demand;
- non-AI consumer, automotive, and industrial markets: cycle-sensitive demand that can offset or weaken AI growth.

### 2. Map each demand driver to tools

For each node or product, record which tool categories benefit:

- more EUV/DUV layers and overlay requirements → lithography;
- GAA, high aspect ratio structures, and 3D memory → etch and deposition;
- new materials, selective processes, and advanced packaging → deposition, etch, clean, and inspection;
- NAND layer increases → high-aspect-ratio etch, deposition, and metrology;
- HBM and 2.5D/3D packages → front-end-adjacent process control and advanced-packaging tools;
- new fabs → facility engineering, cleanroom, gas, water, and utility systems.

Do not assume every AI dollar benefits every tool category equally. A node transition can increase etch and deposition steps while adding fewer lithography layers, or create stronger inspection demand than exposure demand.

## Timing model and bottlenecks

Use a timing ladder:

1. end-demand or customer design signal;
2. customer capex announcement or budget;
3. equipment order and backlog;
4. cleanroom, power, water, gas, and facility readiness;
5. tool shipment and installation;
6. process qualification and acceptance;
7. productive wafer starts and utilization;
8. supplier revenue, service, spare parts, margin, and cash flow.

For every forecast, record the lag between order, delivery, installation, qualification, and production. A report may state that equipment takes multiple quarters from order to production; preserve that lag as part of the thesis rather than treating it as a footnote.

## Customer, geography, and policy matrix

| Dimension | What to verify | Common false positive |
|---|---|---|
| Customer capex | amount, mix, node, geography, and timing | headline capex treated as immediate tool order |
| Cleanroom and facility | completion, utilities, move-in, and tool-ready date | building construction treated as productive capacity |
| Tool category | exposure, etch, deposition, inspection, or service | total WFE growth applied equally to every vendor |
| Product mix | AI, memory, logic, consumer, automotive, industrial, SSD | AI label used without product or wafer-start evidence |
| China exposure | export rules, customer list, service, spare parts, and replacement demand | shipment restriction treated as the only exposure |
| Regional exposure | US, Taiwan, Korea, Japan, Europe, and China revenue/cost | geographic diversification assumed to remove policy risk |
| Supplier position | sole, primary, secondary, or unqualified vendor | industry share treated as the company's current approved position |
| Facility engineering | backlog, project completion, recurring service, and customer concentration | construction order treated as long-term recurring revenue |

## Supplier-role matrix

| Role | What to verify | Common false positive |
|---|---|---|
| Global equipment OEM | tool category, node, backlog, service, gross margin, and customer share | revenue growth attributed to AI without mix evidence |
| Taiwan equipment supplier/partner | exact component, integration, customer, and OEM dependency | OEM relationship assumed to be a direct end-customer position |
| Precision part or module supplier | content per tool, qualification, capacity, yield, and pricing | shipment increase without margin or cash-flow benefit |
| Facility engineering contractor | cleanroom, utilities, gas, water, project backlog, and completion | announced fab treated as recognized engineering revenue |
| Memory or logic manufacturer | node, product mix, utilization, capex, and fab schedule | capex plan treated as current output |
| Service and spare-parts provider | installed base, service attach, regional restriction, and recurring revenue | tool sales alone used as the cycle indicator |

Mark every company as `explicit`, `inferred`, or `unverified`, and record the process section and customer evidence supporting the role.

## Policy and cycle analysis

Separate three shocks:

- demand shock: consumer, auto, industrial, or AI spending changes;
- supply timing shock: cleanroom, utility, installation, qualification, or operator constraints;
- policy shock: export controls, tariff, local-content rules, service restrictions, and customer licensing.

For US equipment suppliers, check whether tariffs affect factory cost, imported components, pricing, or gross margin. For non-US suppliers, check whether policy changes affect tool shipment, US components, customer access, or service. For Taiwan partners, check whether OEM customers can pass through or share cost pressure.

## Forecast ledger and invalidation triggers

For each report forecast, record the claim, date, demand driver, tool category, customer, geography, expected timing, evidence stage, and status: `not_tested`, `supports`, `weakens`, `cannot_test`, or `unresolved`.

Re-evaluate the thesis when:

- customer capex is cut, delayed, or reallocated to a different node or product;
- cleanroom completion does not become tool move-in and productive capacity;
- equipment orders rise but backlog conversion, installation, utilization, or revenue does not follow;
- AI demand is offset by weakness in consumer, automotive, industrial, or China demand;
- export controls or tariffs affect customer access, component costs, service, or gross margin more than expected;
- etch/deposition/inspection advantages are assumed from a node transition that does not increase relevant process steps;
- facility contractors show backlog growth without project completion, cash collection, or margin support;
- a supplier's customer concentration, pricing, or OEM dependency causes revenue growth without durable economics.

## Output requirements

For every front-end equipment report or company, produce:

1. end-demand, product, and node scope;
2. equipment category and process-step exposure;
3. capex, cleanroom, installation, qualification, and production timing;
4. geographic, policy, and customer-concentration risk;
5. supplier role, approved position, and recurring service exposure;
6. revenue, gross margin, utilization, backlog, and cash-flow traces;
7. catalysts, invalidation triggers, and time horizon;
8. historical report claims separated from current metrics and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat a front-end equipment concept-stock list as a recommendation.
