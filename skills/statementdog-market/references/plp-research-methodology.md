# PLP and FOPLP research methodology

Use this reference for panel-level packaging, FOPLP, PLP, CoPoS, panel-based RDL, and related glass-carrier or glass-core reports. It records a reusable research method, not current report conclusions, prices, company recommendations, or dated forecasts.

## Research model

Analyze the chain as:

'package demand and architecture → carrier choice and panel size → process route → warpage, die-shift, uniformity, and yield bottleneck → material and equipment role → customer qualification → productive capacity → utilization and recurring revenue'

The first question is which problem PLP is solving. Usually the thesis combines larger-package geometry and panel utilization with a need for higher package throughput, lower cost, or a path to high-density RDL. Do not assume a theoretical panel-area advantage automatically becomes a cost advantage; yield, handling, cycle time, capital intensity, and qualification can reverse the result.

Always separate:

- temporary panel carrier, which leaves the package after processing;
- permanent glass core or glass interposer, which remains in the package;
- FOWLP, FOPLP, RDL-first, Die-first, and CoPoS, which are related but not interchangeable process or architecture labels.

## Architecture and process map

### 1. Define the target application

Record package size, die size, I/O density, target line width/spacing, number of RDL layers, thermal and warpage limits, and whether the target is a mature-node low-I/O device, a mobile or networking device, or an AI/HPC package.

Map the expected route:

'temporary carrier preparation → die placement or RDL formation → molding and cure → grinding or surface preparation → dielectric and photoresist formation → exposure and develop or laser opening → descum and seed layer → copper plating and etch → debonding → inspection and dicing'

If a permanent glass core or interposer is involved, extend the map with:

'glass forming → TGV modification and etch → seed layer and metallization → via fill → surface build-up → reliability and package integration'

For each step, record the objective, defect mode, material or tool, production owner, and the evidence stage.

### 2. Compare process routes

Compare Die-first face-down, Die-first face-up, and RDL-first on:

- line width/spacing and I/O density;
- die-shift and overlay tolerance;
- warpage and surface flatness;
- material and equipment complexity;
- throughput, yield, and cost;
- suitable customer and package class.

Do not compare routes only by nominal resolution. A finer route can lose its advantage if additional micro-bump, bonding, underfill, alignment, or inspection steps reduce usable yield.

### 3. Test the panel advantage

Check whether the proposed panel size actually improves:

- die-per-panel and edge utilization;
- handling and automation;
- cycle time and bottleneck throughput;
- material utilization;
- total package cost after yield loss and capital depreciation.

Large square panels create their own risks: corner stress, edge-thickness effects, temperature non-uniformity, liquid flow variation, metal current-density variation, panel handling, and crack propagation. These are operating variables to verify, not just background explanations.

## Bottleneck and supplier-role matrix

| Role | What to verify | Common false positive |
|---|---|---|
| OSAT or packaging integrator | package design, route, customer, line size, yield, utilization, recurring volume | announced line treated as qualified production |
| Panel manufacturer | large-panel handling, exposure, wet process, automation, idle capacity, customer access | idle display capacity treated as package capacity |
| Foundry or IDM | front-end and package co-design, high-density RDL, customer binding, qualification | advanced-node strength assumed to transfer to PLP automatically |
| Substrate or glass-core supplier | glass or carrier specification, TGV, adhesion, via fill, build-up, reliability | sample or pilot line treated as mass production |
| Die placement and bonding supplier | placement accuracy, throughput, panel size, die-shift control, bonding yield | machine shipment treated as customer volume |
| Coating, lamination, cure, and molding supplier | square-panel uniformity, dry-film or liquid route, temperature control, throughput | PCB or wafer capability assumed to transfer without qualification |
| Lithography supplier | stepper versus LDI fit, overlay, distortion correction, field size, throughput | resolution alone used as proof of suitability |
| Wet-process, plating, etch, and plasma supplier | chemistry, uniformity, current distribution, descum, via fill, repeatability | being a WLP supplier treated as PLP qualification |
| Laser, debond, drilling, grinding, and dicing supplier | glass or composite handling, crack rate, alignment, throughput, installed base | prototype demo treated as production readiness |
| Inspection and metrology supplier | warpage, overlay, die position, cracks, voids, thickness, electrical continuity, throughput | inspection capability treated as proof that yield is solved |
| Material and chemical supplier | dry-film or liquid fit, adhesion, CTE, purity, recurring consumption, qualification | supply-chain map treated as actual revenue |

Mark every company as `explicit`, `inferred`, or `unverified`, and record the report section that supports the role. A company may have different statuses for different process steps.

## Milestone and forecast ledger

Use this commercialization ladder:

1. concept, public explanation, or technology demonstration;
2. pilot process or laboratory equipment;
3. sample delivery;
4. customer reliability, design validation, or qualification;
5. small-volume shipment;
6. qualified production line and installed productive tools;
7. repeat orders, utilization, and usable panel output;
8. recurring revenue, margin, and operating-cash-flow contribution.

For each report forecast, record:

- the exact claim and report date;
- the expected product or process milestone;
- the expected timing;
- the companies and operating traces that should benefit;
- the current status: `not_tested`, `supports`, `weakens`, `cannot_test`, or `unresolved`;
- the evidence needed for the next review.

Separate a capacity announcement from tool installation, qualification, production ramp, customer volume, and supplier revenue. A downstream package line can be constrained by yield or customer qualification even when nominal panel capacity is available.

## Invalidation triggers

Re-evaluate the thesis when:

- panel utilization or theoretical cost advantage disappears after yield and depreciation;
- warpage, die-shift, overlay, thickness uniformity, corner stress, or crack defects remain unresolved;
- LDI or other flexible tools improve accuracy but throughput is too low for the target volume;
- dry-film, liquid, molding, plating, or adhesion changes do not produce stable panel-level uniformity;
- RDL resolution, bonding accuracy, or inspection capability cannot meet the package's I/O density;
- glass-core TGV, via fill, adhesion, delamination, or thermal-cycle reliability remains below qualification;
- a pilot line or sample does not progress to customer qualification, repeat orders, or productive volume;
- customer demand shifts to FOWLP, CoWoS, organic substrate, silicon interposer, or another route;
- a named supplier's related revenue, utilization, margin, or cash flow does not follow the claimed opportunity.

## Output requirements

For every PLP report or company, produce:

1. architecture and application scope;
2. process route and target line width/spacing;
3. panel-size and cost/yield thesis;
4. bottleneck and measurable operating indicator;
5. supplier role with explicit/inferred status;
6. qualification, capacity, utilization, and commercialization stage;
7. catalysts, invalidation triggers, and time horizon;
8. historical report claims separated from current metrics, news, and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat inclusion in a PLP concept-stock list as a recommendation.
