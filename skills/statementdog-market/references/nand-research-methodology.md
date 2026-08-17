# NAND Flash research methodology

Use this reference for NAND Flash, enterprise SSD, client/mobile NAND, QLC/TLC/MLC/SLC, 3D NAND layer scaling, NAND equipment, memory modules, and NAND/HDD substitution reports. It records a reusable research method, not current report conclusions, prices, company recommendations, or dated forecasts.

## Research model

Analyze the chain as:

'workload and storage architecture → NAND bit demand and product mix → layer, node, and cell-type transition → wafer output and supply discipline → enterprise/client pricing → original-maker margin and cash flow → equipment, module, controller, and HDD substitution impact'

Do not treat NAND as one market. Always split:

- enterprise SSD, client SSD, mobile NAND, removable/consumer NAND;
- cold, warm, compute, and high-IOPS storage;
- QLC, TLC, MLC, SLC and the associated capacity/latency/endurance trade-off;
- bit shipment from revenue, and price from volume;
- process upgrade bit growth from greenfield capacity growth.

## Demand map

### 1. Start from the workload

Record whether demand is driven by:

- AI training or inference;
- KV-cache offload;
- RAG vector databases and indexes;
- intermediate results, checkpoints, logs, and backups;
- enterprise storage and nearline HDD replacement;
- PC, smartphone, client, and other consumer devices.

Agentic AI can add repeated inference, longer-lived state, more retrieval, validation, intermediate data, and audit logs. Treat this as a hypothesis to verify with enterprise SSD bit demand and customer procurement, not as a substitute for shipment evidence.

### 2. Match workload to NAND product

Check capacity and cost efficiency, IOPS and latency, endurance and write amplification, interface bandwidth and queue depth, power and rack density, TLC/QLC/MLC/SLC mix, and controller, firmware, and qualification requirements.

A high-capacity QLC solution and a high-IOPS TLC/MLC/SLC solution consume different amounts of wafer capacity and may have different margins. A shift toward high-IOPS products can increase NAND bit demand even if total storage capacity growth is unchanged.

## Supply, process, and capacity model

Track three separate ways to increase bits:

1. higher wafer starts or greenfield fab capacity;
2. process shrink and layer-count increase;
3. product mix and cell-type change.

For 3D NAND, verify layer count, channel-hole aspect ratio, etch depth, deposition, wordline material, gap fill, bonding/alignment, yield, and ramp time. When layer count becomes very high, new etch, ALD, cryogenic, ALE, deposition, and inspection capabilities may be required.

For capacity timing, track cleanroom availability, DRAM versus NAND space allocation, existing-fab utilization, equipment order/installation/qualification/yield ramp, greenfield construction and first production, and export controls or service restrictions at China fabs.

Do not treat a process upgrade announcement as immediate bit supply. The same is true for a new-fab announcement that lacks cleanroom, tool, and qualification evidence.

## NAND role matrix

| Role | What to verify | Common false positive |
|---|---|---|
| NAND original maker | enterprise SSD mix, bit shipment, ASP, wafer starts, layer transition, margin, and capex | revenue growth treated as durable demand without mix evidence |
| Enterprise SSD supplier | customer qualification, controller/firmware, IOPS, latency, endurance, and recurring volume | sample or design win treated as hyperscaler volume |
| Controller supplier | controller design, TLC/QLC/SLC support, customer, attach rate, and inventory | controller shipment treated as NAND bit demand |
| Memory module maker | inventory cost, selling price, gross margin, turns, and cash conversion | rising spot price assumed to improve margin indefinitely |
| HDD supplier | HAMR transition, capacity per drive, bit shipment, production ramp, and substitution | SSD shortage assumed to remove HDD technology risk |
| Equipment supplier | etch/deposition/ALD/cryogenic/ALE tool, layer transition, customer qualification, and service | NAND capex assumed to benefit every equipment category equally |
| OSAT or test supplier | NAND product mix, outsourcing, package/test utilization, and customer | original-maker price increase assumed to pass through to tester |

Mark every company as `explicit`, `inferred`, or `unverified`, and record the report section supporting the role.

## Cycle and margin checks

For original makers, compare bit shipment growth, price and product mix, enterprise SSD share, wafer starts and utilization, inventory and capex, and gross margin, operating margin, and free cash flow.

For module companies, explicitly model the inventory cycle:

1. early price increase: low-cost inventory creates temporary margin expansion;
2. sustained increase: replenishment cost rises and margin growth slows;
3. flat or falling price: high-cost inventory can compress margin rapidly.

Do not transfer original-maker pricing power to module makers. Their revenue can rise while gross margin and cash conversion deteriorate.

## Forecast ledger and invalidation triggers

For every forecast, record the claim, workload, product, cell type, layer count, supply response, expected timing, company role, evidence stage, and status: `not_tested`, `supports`, `weakens`, `cannot_test`, or `unresolved`.

Re-evaluate the thesis when enterprise SSD demand is only inventory restocking or pre-buying; RAG/KV-cache adoption does not translate into qualified SSD volume; hyperscaler capex growth slows or shifts architecture; TLC/MLC/SLC or high-IOPS mix increases cost without pricing or margin support; layer scaling, etch, deposition, gap fill, yield, or cleanroom constraints delay bit supply; China restrictions block output; HDD HAMR capacity ramps faster and reduces SSD substitution; module prices rise but inventory cost, margin, and cash flow worsen; or original-maker/equipment revenue does not follow the claimed supply/demand improvement.

## Output requirements

For every NAND report or company, produce workload and storage-product scope; enterprise/client/mobile and cell-type mix; bit demand, price, wafer output, layer transition, and capacity timing; equipment, controller, module, OSAT, and HDD substitution roles; qualification, utilization, margin, inventory, and cash-flow evidence; catalysts, invalidation triggers, and time horizon; and historical report claims separated from current metrics and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat a NAND concept-stock list as a recommendation.
