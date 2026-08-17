# Bonder research methodology

Use this reference for wire bonder, flip-chip bonder, TC bonder, fluxless TC bonder, hybrid bonder, die attach, and related advanced-packaging bonding reports. It records a reusable research method, not current report conclusions, prices, company recommendations, or dated forecasts.

## Research model

Analyze the chain as:

'I/O density and package architecture → bonding route → pitch, height, warpage, alignment, and throughput constraint → equipment qualification → customer process adoption → installed capacity and utilization → recurring tool, service, and consumables revenue'

Start with the package requirement, not the equipment name. The same company may sell several bonding platforms into different markets, and the competitive position of a wire bonder does not prove a position in TC or hybrid bonding.

Always separate:

- wire bonding, which remains relevant for mature, memory, automotive, industrial, and other high-volume applications;
- flip-chip bonding, which uses bumps and serves a broad range of conventional and advanced packages;
- TC bonding, which applies controlled heat and compression to improve alignment and coplanarity at tighter pitch;
- fluxless TC bonding, which addresses contamination, pitch, and process-yield constraints without eliminating all TC-bonding trade-offs;
- hybrid bonding, which removes solder bumps and can support finer pitch and thinner stacks but usually requires higher process complexity, cost, and defect control;
- wafer-to-wafer and die-to-wafer hybrid bonding, which have different yield, flexibility, and throughput economics.

## Architecture and process comparison

### 1. Define the package requirement

Record I/O pitch, die size, stack height, package type, thermal budget, alignment tolerance, bump or bumpless interface, expected throughput, and whether the product is mature-node, HBM, 2.5D, 3D, CPO, backside-power, or another application.

### 2. Compare the bonding routes

| Route | Main advantage | Main constraint | Typical verification |
|---|---|---|---|
| Wire bonding | mature, low cost, high throughput, broad installed base | lower I/O density and longer interconnect path | customer utilization, unit volumes, mature-market cycle |
| Flip-chip bonding | higher I/O density than wire, established ecosystem | bump formation, warpage, alignment, and pitch limit | tool shipments, package volume, customer platform |
| TC bonding | controlled force and temperature, improved fine-pitch alignment | slower and more expensive than mass reflow; thermal and coplanarity control | installed tools, yield, bump pitch, customer qualification |
| Fluxless TC bonding | reduces flux-related contamination and can support tighter pitch | qualification, tool availability, cleaning, yield, and cost | customer trial, repeat orders, production ramp |
| Hybrid bonding | bumpless interface, finer pitch, lower stack height | surface cleanliness, planarity, alignment, defectivity, and cost | W2W/D2W qualification, yield, wafer/die throughput |

Do not treat finer nominal pitch as automatic substitution. The actual decision depends on stack height, thermal performance, yield, throughput, customer design, and total package cost.

### 3. Identify substitution and coexistence

Track whether TC and hybrid bonding are:

- direct substitutes in a target product;
- complementary routes used at different stack layers;
- sequential routes used in different generations;
- not comparable because the customers or package architectures differ.

When a standard or customer requirement changes, record the timing, the route affected, and whether the change creates demand for a new tool or merely upgrades an installed platform.

## Demand model and customer power

Separate the demand drivers:

1. traditional semiconductor cycles: consumer, automotive, industrial, memory, and general IC capacity;
2. indirect AI demand: power-management, networking, storage, and server components that still use traditional bonding;
3. advanced logic packaging: CoWoS, SoIC, CPO, backside power, and other high-density routes;
4. HBM: stack height, layer count, bump pitch, thermal requirements, and customer qualification;
5. OSAT expansion: outsourced advanced-packaging capacity and the timing of customer migration.

For advanced bonding, map the power of the end customer. A small number of foundries, HBM makers, IDMs, and OSATs can determine the tool specification, approved vendor list, and ramp timing. A supplier with technical leadership can still have weak pricing power if one customer dominates purchases or sponsors a competing in-house vendor.

## Supplier-role matrix

| Role | What to verify | Common false positive |
|---|---|---|
| Wire-bonder supplier | installed base, mature-market share, cycle exposure, service and replacement revenue | mature share mistaken for growth |
| Flip-chip supplier | package platform, pitch, customer, throughput, and installed tools | CoWoS shipment assumed to transfer to every package |
| TC-bonder supplier | bump pitch, fluxless capability, force/temperature control, yield, and customer certification | trial machine treated as mass-production share |
| Hybrid-bonder supplier | W2W/D2W route, overlay, cleanliness, defectivity, throughput, and reference customers | technology demo treated as revenue |
| Die-attach or placement supplier | placement accuracy, die-size range, throughput, and package use | generic die attach treated as hybrid bonding |
| Foundry, HBM maker, IDM, or OSAT | package roadmap, capacity, customer design, qualification, and capex | announced capex treated as immediate tool demand |
| Equipment service provider | installed base, service intensity, spare parts, and recurring revenue | tool revenue alone used to judge cycle health |

Mark each company as `explicit`, `inferred`, or `unverified`, and cite the process, customer, and evidence stage supporting the role.

## Commercialization and evidence ladder

Use this ladder for a new bonding route:

1. architecture or public demonstration;
2. laboratory tool or pilot line;
3. customer sample and process trial;
4. qualification, reliability, and design validation;
5. small-volume production;
6. repeat orders and installed productive capacity;
7. utilization, service, and recurring tool revenue;
8. gross-margin, operating-cash-flow, and free-cash-flow contribution.

Separate:

- order intake from revenue recognition;
- shipment from installation;
- installation from productive utilization;
- qualification from repeat production;
- a customer announcement from a supplier's recognized revenue.

## Forecast ledger and invalidation triggers

For each report forecast, record the claim, date, route, customer, expected timing, company role, evidence stage, and status: `not_tested`, `supports`, `weakens`, `cannot_test`, or `unresolved`.

Re-evaluate the thesis when:

- the claimed pitch or stack-height problem is solved by an existing TC, flip-chip, or packaging route;
- hybrid bonding remains too expensive, slow, defect-prone, or difficult to qualify;
- fluxless TC does not achieve the expected yield or customer adoption;
- HBM standards, stack height, or customer design changes postpone route substitution;
- the expected foundry, HBM, or OSAT capex does not become tool orders and productive capacity;
- an equipment supplier loses an approved-vendor position or a customer shifts to an in-house or sponsored competitor;
- tool shipments increase but utilization, service revenue, margin, or cash flow do not follow;
- mature-market recovery is attributed to AI without corroborating server, networking, power, or storage component demand.

## Output requirements

For every Bonder report or company, produce:

1. package/application and I/O-pitch scope;
2. bonding route and competing or complementary routes;
3. technical bottleneck and measurable indicator;
4. customer, approved-vendor, and concentration risk;
5. qualification, capacity, utilization, and revenue stage;
6. catalyst, substitution risk, invalidation trigger, and time horizon;
7. historical report claims separated from current metrics and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat a company in a concept-stock list as a recommendation.
