# Transaction and value-capture research methodology

Use this reference for payment networks, marketplaces, brokers, exchanges, auction houses, ad platforms, or any business that earns a small fee from a larger transaction flow. It records a reusable method, not current GMV, take rates, prices, or company recommendations.

## Research model

Analyze the chain as:

`participant → product/service flow → money flow → information flow → risk allocation → company fee`

Always distinguish:

- transaction value or GMV from reported revenue;
- the party that pays the fee from the party that receives the service;
- gross activity from net economic value captured;
- agency activity from principal, inventory, credit, guarantee, or settlement risk;
- price, volume, mix, frequency, penetration, and share as separate drivers.

## Sequence

### 1. Draw the transaction map

Name every participant, what each one supplies, when cash moves, and who bears fraud, credit, inventory, guarantee, settlement, or regulatory risk. Mark whether the company is an agent, principal, infrastructure provider, lender, or a combination.

### 2. Identify the value bottleneck

Ask which scarce capability makes the transaction possible: trust, acceptance, liquidity, authentication, routing, data, brand, distribution, or financing. Then test whether the company controls that bottleneck or merely benefits from temporary volume.

### 3. Build the revenue bridge

Use the most economically meaningful decomposition:

- `GMV × take rate = transaction-linked revenue`;
- `transactions × average fee = revenue`;
- `buyers × purchase frequency × average basket × take rate`;
- `auction sales × commission rate + ancillary fees`.

Reconcile the bridge to reported revenue and explain the residual. Do not call a residual “other revenue” without checking segment definitions, rebates, incentives, pass-through items, and principal accounting.

Add a gross-to-net bridge when incentives, rebates, guarantees, or pass-through payments are material. Record whether each item is contra-revenue, operating expense, balance-sheet exposure, or contingent risk. For payment networks, customer incentives can be the economic cost of maintaining participation even when accounting presents them as a revenue deduction; for auctions, distinguish auction guarantees, third-party guarantees, inventory, and ordinary agency commission.

### 4. Trace risk and capital

For every new service, record whether the company must fund receivables, inventory, guarantees, reserves, collateral, settlement liquidity, or customer incentives. A higher take rate may be unattractive if it requires disproportionate capital or risk.

## Role-specific metrics

| Business role | Primary metrics | Common false positive |
|---|---|---|
| Payment network | payment volume, cross-border mix, transactions, take rate, incentives, fraud/loss | revenue growth mistaken for transaction growth |
| Marketplace | GMV, buyers, sellers, conversion, repeat rate, take rate, liquidity | GMV growth without improving liquidity or contribution profit |
| Auction/broker | GMV, average lot value, buyer/seller fee, guarantees, private sales, inventory | record sale treated as recurring volume |
| Advertising intermediary | impressions, fill, price, advertiser spend, attribution, data revenue | ad revenue growth caused only by load or one customer |
| Principal/inventory business | inventory turns, gross margin, markdowns, working capital, guarantees | agency economics applied to principal risk |

## Invalidation triggers

Re-evaluate the thesis when:

- GMV grows but take rate, gross profit, or cash conversion falls;
- customers bypass the company through direct, private, open-source, or alternative rails;
- incentives grow faster than transaction value;
- guarantees, inventory, receivables, or fraud losses grow faster than revenue;
- the company raises price but loses supply, acceptance, liquidity, or repeat usage;
- accounting presentation changes make reported revenue incomparable.

## Output requirements

Produce a participant map, revenue and gross-to-net bridge, risk/capital table, role-specific KPI table, and a paragraph explaining who captures value and why that capture should persist. Label each input using [evidence-discipline.md](evidence-discipline.md); do not use “current metric” unless its date and current-state verification are explicit.

## Manny Pro case links

- [Visa series](../../../sites/manny-pro/references/series-guo-lu-cai-shen.md)
- [Sotheby's series](../../../sites/manny-pro/references/series-luo-chui-zhi-qian.md)
