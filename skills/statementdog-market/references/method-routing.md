# Statement Dog research-method routing

Always apply [research-contract.md](research-contract.md) first. Then select only the domain references needed for the claim or company role; a report can require more than one row.

| Trigger or research object | Add this reference | Distinguishing question |
|---|---|---|
| DRAM, HBM, DDR, memory module, memory packaging | [dram-research-methodology.md](dram-research-methodology.md) | Are bits, price, usable capacity, product generation, and company role being kept separate? |
| NAND, enterprise SSD, QLC/TLC/MLC/SLC, 3D NAND | [nand-research-methodology.md](nand-research-methodology.md) | Which workload and cell/layer transition creates bit demand and consumes usable wafer supply? |
| HDD, nearline, PMR/HAMR, HDD components | [hdd-research-methodology.md](hdd-research-methodology.md) | Does the candidate benefit from bits/capacity, drive units, content per drive, or equipment orders? |
| Glass carrier/core/interposer, TGV | [glass-substrate-research-methodology.md](glass-substrate-research-methodology.md) | Which glass application, process bottleneck, qualification stage, and revenue milestone apply? |
| PLP, FOPLP, panel RDL, CoPoS | [plp-research-methodology.md](plp-research-methodology.md) | Which package architecture and process route survives yield, throughput, and cost constraints? |
| Wire/flip-chip/TC/fluxless/hybrid bonder | [bonder-research-methodology.md](bonder-research-methodology.md) | Which bonding route, pitch, customer qualification, substitution path, and utilization matter? |
| Front-end equipment, WFE, fab facility | [frontend-equipment-research-methodology.md](frontend-equipment-research-methodology.md) | Which process step benefits, and when does capex become installed and productive equipment? |
| Foundry, node, 8-inch/12-inch, fab expansion | [foundry-research-methodology.md](foundry-research-methodology.md) | Which node, wafer size, end market, utilization, price, and depreciation profile apply? |
| Broad semiconductor outlook or cycle | [semiconductor-cycle-research-methodology.md](semiconductor-cycle-research-methodology.md) | Is the company a leading, coincident, or lagging sensor for the specified product and cycle? |
| PC, traditional server, AI server, server components | [pc-server-research-methodology.md](pc-server-research-methodology.md) | Are units, content, backlog, integration, acceptance, and pull-forward separated? |
| Automotive/industrial semiconductor, lead frame, machine tool | [auto-industrial-semiconductor-research-methodology.md](auto-industrial-semiconductor-research-methodology.md) | Is recovery sell-through, replenishment, price/mix, or tariff-driven pull-forward? |
| Quarterly company used as an industry sensor, especially equipment | [klic-quarterly-research-methodology.md](klic-quarterly-research-methodology.md) | After normalizing the quarter and segments, can one company legitimately support the broader inference? |

## Combination rules

- Use DRAM plus NAND when a memory-maker thesis mixes the two; never transfer one product's supply or price conclusion to the other.
- Use NAND plus HDD for storage substitution, but start with workload and storage tier before comparing cost or capacity.
- Use PLP plus glass only when permanent glass core/interposer or TGV is material; a temporary carrier alone does not prove a glass-substrate thesis.
- Use bonder plus the relevant end market when traditional and advanced packaging demand have different cycles.
- Use foundry plus front-end equipment only after preserving the lag from wafer demand to capex, orders, installation, and revenue.
- Use semiconductor-cycle as an overlay, not a substitute for the product-specific reference.

If no domain row fits, still use the evidence contract and [industry-report-methodology.md](industry-report-methodology.md); state the missing domain-specific indicators rather than borrowing an unrelated checklist.
