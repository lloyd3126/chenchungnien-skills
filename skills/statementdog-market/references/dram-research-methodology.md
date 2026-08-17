# DRAM and memory-industry research methodology

Use this reference when reading a DRAM, HBM, NAND, memory-module, memory-packaging, substrate, or memory-server report. It records a reusable research method, not current report content, company recommendations, prices, or dated forecasts.

## Contents

- [Research model](#research-model)
- [Sequence](#sequence)
- [Role-specific metrics](#role-specific-metrics)
- [Product-cycle and substitution checks](#product-cycle-and-substitution-checks)
- [Invalidation triggers](#invalidation-triggers)
- [Output requirements](#output-requirements)

## Research model

Analyze the chain as:

'end demand → units/bits → supply and capacity → ASP/contract price → revenue → margins → cash flow and valuation'

Always separate these questions:

- Is demand increasing, or are customers only pulling orders forward?
- Are shipments increasing, or is revenue rising mainly because of price?
- Is supply constrained by wafer capacity, packaging, materials, qualification, or customer deployment?
- Is a new product adding demand, replacing an old product, or merely changing mix?
- Does the industry benefit reach the company through price, volume, utilization, mix, or inventory timing?

Do not use total memory revenue as a substitute for product-level supply/demand analysis.

## Sequence

### 1. Define the product boundary

Record the products and end markets separately:

- HBM and other AI accelerator memory;
- Server DRAM, including conventional high-performance memory;
- PC, mobile, consumer, industrial, and automotive DRAM;
- DDR generations and LPDDR generations;
- NAND, client SSD, and enterprise SSD;
- modules, packaging/test, substrates, materials, servers, and cloud demand.

Do not merge products merely because they share a memory manufacturer.

### 2. Map demand by buyer and use case

Separate hyperscaler/cloud capex, AI training, AI inference, general-purpose servers, PC, mobile, consumer electronics, industrial, automotive, and inventory replenishment. For each bucket record:

- buyer or channel;
- product required;
- shipment or deployment timing;
- whether demand is recurring, project-based, or pull-forward;
- evidence that can confirm or disconfirm the demand.

### 3. Measure supply in usable output

Track wafer starts or bit output, utilization, yield, product mix, inventory, packaging capacity, materials, and qualification status. Treat the following as separate milestones:

'capex announced → building/cleanroom → equipment installed → process ramp → customer qualification → usable volume shipment'

A new fab or equipment order is not current supply until the relevant product is qualified and shipping.

### 4. Analyze price and contracts

Keep spot price, contract price, blended ASP, and product-specific ASP separate. For contracts, record duration, volume commitment, price ceiling/floor, prepayment or collateral, take-or-pay terms, repricing triggers, and product-generation clauses. A long contract can reduce short-term price elasticity without removing a physical shortage.

### 5. Connect the product cycle

For every transition, record:

- old and new product;
- performance, power, capacity, or cost advantage;
- customer qualification and redesign time;
- relative price and total system cost;
- supplier readiness and yield;
- whether the transition expands total demand or substitutes existing demand.

### 6. Trace financial transmission

For each company role, explain whether the thesis should appear first in:

- shipments or utilization;
- ASP or product mix;
- revenue;
- gross margin;
- inventory valuation and days;
- operating cash flow and free cash flow;
- capex and depreciation;
- valuation or share-price expectations.

Revenue growth without shipment growth may be price-led. Margin growth without cash conversion may be inventory or accounting timing.

## Role-specific metrics

| Role | Primary checks | Common false positive |
|---|---|---|
| DRAM/NAND manufacturer | bit shipments, product ASP, mix, utilization, yield, inventory, capex, qualification, gross margin | revenue growth caused only by price or favorable mix |
| HBM or advanced-memory supplier | customer qualification, generation transition, stack/package capacity, yield, contract coverage, ASP, customer concentration | announced sampling treated as mass production |
| Mature-memory supplier | DDR/LPDDR product mix, spot/contract spread, utilization, inventory, substitution pace, pricing power | shortage assumed to persist after customers redesign to another generation |
| Memory module company | shipment volume, module ASP, inventory cost, inventory days, gross margin, working capital, customer/channel mix | low-cost inventory temporarily inflates margin |
| Packaging/test company | memory-related revenue, units, utilization, package mix, pricing, capex, customer concentration | chip price increase mistaken for packaging-volume growth |
| BT/substrate/material supplier | memory-related utilization, capacity, material cost, price pass-through, lead time, product mix, margin | demand improvement fully offset by material-cost inflation |
| Server/OEM/system company | AI/general-server orders, backlog, deployment timing, rack/system yield, memory content per system, inventory | chip shipment mistaken for completed system deployment |
| Hyperscaler/cloud demand | capex, data-center buildout, accelerator/server shipment, utilization, procurement commitments | capex guidance treated as immediate memory consumption |

Use the role matrix as a selection guide, not as an automatic screen. Record unavailable metrics rather than substituting a less relevant ratio.

## Product-cycle and substitution checks

When a product is being replaced, test all four:

1. Economic trigger — has the price or total-system-cost gap changed enough to motivate redesign?
2. Technical readiness — do processors, controllers, boards, packaging, and suppliers support the new product?
3. Time-to-convert — how many quarters are needed for design, certification, inventory depletion, and volume production?
4. Demand accounting — is the new product incremental demand or replacement demand?

When a product is supply constrained, test the reverse:

1. Can customers reduce memory content per system?
2. Can they delay deployment?
3. Can another product or supplier substitute?
4. Does a contract prevent short-term substitution?

## Invalidation triggers

Flag the thesis for re-evaluation when one or more occur:

- end-demand indicators weaken while inventories rise;
- unit/bit shipments fall after price increases;
- a new fab reaches qualified volume earlier than expected;
- packaging, materials, or customer qualification becomes the bottleneck instead of wafers;
- product substitution accelerates;
- a major supplier cuts price or increases mature-product supply;
- customer concentration or long-contract terms limit price upside;
- company gross margin rises but inventory, receivables, or cash conversion deteriorate;
- capex or backlog does not translate into actual deployment.

## Output requirements

For every DRAM-related report or company, produce:

1. product and end-market scope;
2. demand map and pull-forward assessment;
3. usable-supply and capacity-timing assessment;
4. ASP/contract-price and product-cycle assessment;
5. role-specific company indicators;
6. catalysts, invalidation triggers, and time horizon;
7. historical report claims separated from current metrics and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat a company being named in a report as a recommendation.
