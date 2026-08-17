# HDD research methodology

Use this reference for hard-disk-drive, nearline storage, HAMR, PMR, glass-substrate, HDD component, and HDD-versus-SSD reports. It records a reusable research method, not current report conclusions, prices, company recommendations, or dated forecasts.

## Research model

Analyze the chain as:

`workload and storage architecture → hot/warm/cold and nearline placement → bit demand versus drive-unit demand → capacity and recording technology → supply discipline and price per bit → original-maker margin and cash flow → media, head, suspension, motor, actuator, controller, and equipment impact`

Do not treat HDD demand as a simple count of drives. Always separate:

- data-center, enterprise, nearline, archival, consumer, and surveillance use;
- hot, warm, cold, backup, vector, checkpoint, and log data;
- bit shipment, drive-unit shipment, capacity per drive, and price per TB;
- PMR, HAMR, and any successor recording technology;
- drive upgrades that raise capacity without raising unit shipments;
- original makers, component suppliers, equipment suppliers, and materials suppliers.

## Demand and storage architecture

### 1. Start from the workload

Record whether demand comes from:

- AI training, inference, agentic workflows, RAG, vector indexes, KV-cache spillover, checkpoints, intermediate results, or audit logs;
- hyperscaler and enterprise cloud expansion;
- backup, archival, surveillance, and other capacity-oriented workloads;
- PC, consumer, or other markets where SSD substitution is stronger.

Map the workload to storage tier. High-IOPS and latency-sensitive data may stay in DRAM or SSD; large, lower-frequency, durable, or replicated data may use nearline HDD. Do not assume that a rise in total data automatically becomes HDD bit demand.

### 2. Test HDD versus SSD substitution

Compare:

- cost per TB and total cost of ownership;
- capacity per drive, rack density, power, cooling, and failure/rebuild behavior;
- latency, IOPS, bandwidth, endurance, and access pattern;
- NAND pricing, QLC/TLC mix, SSD availability, and HDD availability;
- the customer's actual storage architecture and qualification status.

Treat SSD substitution as workload-specific. A temporary NAND shortage can delay substitution, but a sustained fall in SSD cost or a change in application latency requirements can reverse the conclusion.

## Bit demand, capacity, and pricing

Track these separately:

1. data generated or retained;
2. required storage capacity and replication;
3. HDD bit shipment and drive-unit shipment;
4. capacity per drive and platter count;
5. price per drive and price per TB;
6. utilization, inventory, contract coverage, and customer visibility;
7. revenue, gross margin, free cash flow, and capex.

The core diagnostic is:

`bit demand growth ≠ drive-unit growth`

A capacity upgrade can allow original makers to ship more bits with flat units. Unit-correlated suppliers such as some motors, suspensions, brackets, or assemblies may therefore lag media, recording, or technology suppliers. Conversely, a supplier whose content per upgraded drive rises may benefit even without unit growth; verify actual content and qualification rather than assuming every component follows the drive market.

## Recording technology and process map

For PMR-to-HAMR or another recording transition, verify:

- recording medium and media material;
- platter or glass-substrate requirement;
- additional layers, sputtering, deposition, etch, lithography, or anneal steps;
- head, laser, suspension, actuator, spindle, and motor changes;
- drive qualification, yield, ramp, and customer acceptance;
- capacity per drive and bit-shipment contribution;
- the timing of pilot, qualification, volume production, and broad customer deployment.

Do not treat a roadmap, prototype, or qualification announcement as immediate supply. Separate technology availability from qualified volume and from recognized revenue.

## HDD supply-chain role matrix

| Role | What to verify | Common false positive |
|---|---|---|
| Original HDD maker | bit shipment, units, capacity per drive, ASP/price per TB, HAMR ramp, customer mix, inventory, margin, and capex | total data growth treated as immediate drive-unit growth |
| Media or platter supplier | substrate, magnetic layer, material content, capacity upgrade, qualification, yield, and customer concentration | material exposure assumed to equal volume production |
| Glass-substrate or material supplier | process capability, surface quality, capacity, qualification, and share of upgraded media | glass use assumed before the drive design is qualified |
| Head or laser supplier | head technology, laser integration, customer, yield, and recurring content | design reference treated as volume shipment |
| Suspension, actuator, spindle, motor, VCM, bracket, or assembly supplier | content per drive, unit sensitivity, capacity-upgrade content, utilization, and customer mix | all mechanical components assumed to grow with bit demand |
| Controller, preamp, or interface supplier | product design, customer, attach rate, qualification, and replacement cycle | controller shipment treated as HDD bit growth |
| Process-equipment supplier | sputter, PVD/CVD, IBD/IBE, etch, lithography, deposition, inspection, or service exposure | original-maker capex treated as immediate equipment revenue |
| Material or specialty-chemical supplier | material specification, qualification, volume, pricing, and substitution risk | a named material supplier assumed to have a locked share |

Mark every company as `explicit`, `inferred`, or `unverified`, and record the report section supporting the role. Keep original makers, component suppliers, and equipment suppliers in separate operating models.

## Timing and evidence ladder

Use this ladder:

1. workload, retention, and customer storage architecture;
2. hyperscaler or enterprise capex and procurement visibility;
3. HDD/SSD demand, inventory, contract coverage, and price per TB;
4. original-maker bit and unit outlook;
5. recording roadmap and customer qualification;
6. pilot line, yield, and volume ramp;
7. component/material/equipment order and installation;
8. supplier utilization, revenue, margin, cash flow, and repeat orders.

When a report says supply is disciplined, verify production cuts, customer contracts, utilization, inventory, capacity additions, and whether the duopoly can keep supply below demand. When it says pricing will rise, identify whether the mechanism is a shortage of bits, shortage of units, technology transition, contract repricing, or mix improvement.

## Forecast ledger and invalidation triggers

For every forecast, record the claim, workload, storage tier, technology, unit/bit assumption, customer, supply response, expected timing, evidence stage, company role, and status: `not_tested`, `supports`, `weakens`, `cannot_test`, or `unresolved`.

Re-evaluate the thesis when:

- AI-generated or retained data does not translate into customer HDD procurement or bit shipments;
- data shifts toward high-IOPS SSD, or SSD cost and availability improve enough to accelerate substitution;
- HDD units fall faster than capacity per drive and the thesis relied on unit growth;
- HAMR qualification, yield, laser integration, media, or customer acceptance is delayed;
- capacity upgrades raise bits but do not improve price per TB, utilization, or supplier content;
- supply discipline breaks through new entrants, excess inventory, customer concentration, or a demand shock;
- component or equipment suppliers do not show the expected order, utilization, revenue, margin, or cash-flow follow-through;
- a material, substrate, or process supplier fails qualification or can be substituted;
- original makers raise outlook without subsequent bookings, production, or recognized revenue.

## Output requirements

For every HDD report or company, produce:

1. workload and storage-tier scope;
2. HDD-versus-SSD substitution assumptions;
3. bit demand, unit demand, capacity per drive, price per TB, and inventory;
4. PMR/HAMR or other technology roadmap and qualification timing;
5. original-maker, component, materials, and equipment roles;
6. capacity, utilization, margin, cash-flow, capex, and customer-visibility checks;
7. catalysts, invalidation triggers, and time horizon;
8. historical report claims separated from current metrics and official disclosures.

Apply the common claim types and validation statuses from the research contract. Never treat a HDD concept-stock list as a recommendation.
