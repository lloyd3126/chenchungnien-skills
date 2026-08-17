# Industry-report series methodology

Use this reference when the user asks to read multiple Statement Dog industry reports from newest to oldest, compare a report series, or整理 each report together with comments and author replies. It describes a repeatable research workflow; it does not store current report titles, prices, rankings, or company data.

Apply [research-contract.md](research-contract.md) before this workflow. It defines source modes, claim records, scope normalization, the two status dimensions, company handoff, and data-quality rules. Use [method-routing.md](method-routing.md) to add only the relevant product-specific methodology.

## Research unit and source hierarchy

Treat each report as one dated observation in a topic timeline. Keep these layers separate:

1. **Report body** — the author's thesis, evidence, assumptions, named companies, supply-chain roles, and stated risks.
2. **Reader comments** — questions, counterexamples, corrections, alternative interpretations, and practical site-use problems.
3. **Author/official replies** — clarifications, corrections, changed assumptions, links to site functions, and explicit non-answers.
4. **Current company evidence** — current Statement Dog metrics, price, news, filings, and official disclosures, gathered only after the historical report analysis.

The report is historical context. Current company data and official filings outrank a report's old numbers, screenshots, tax rules, valuation, or price examples.

## Current-site and local-snapshot modes

In `current_site` mode, enumerate the visible archive and record the observation time. In `local_snapshot` mode, do not open the site:

1. Use the local manifest to establish capture order and completeness when available.
2. Read each saved `article.html` and inspect its local images; use a text snapshot only as fallback.
3. Record report date, original URL, local file, capture time, visual state, and comment state.
4. Treat the archive as frozen historical evidence. Any current metric, price, news, UI, filing, or newly published report remains `current_not_checked`.
5. Do not silently fill a local gap with memory or outside sources.

## Article-by-article workflow

### 1. Establish the report inventory

- Open the current industry-report archive and enumerate the visible pages from newest to oldest.
- Record title, date, URL, author/team, page position, and any series or topic label.
- Detect a series when reports share an industry/topic, overlapping companies, a numbered or continuation title, or a common supply-chain map. Do not merge distinct reports merely because they mention the same company.
- Preserve the original order and identify missing pages, pagination gaps, duplicate cards, or reports that are inaccessible.
- In local mode, describe only the captured inventory; do not call it the current full archive.

### 2. Read the report itself

Read the full body, headings, tables, charts, diagrams, and linked company/topic cards. When a chart or supply-chain map carries meaning, visually inspect it rather than relying only on extracted text. Record:

- central thesis and the author's conclusion;
- demand drivers and end markets;
- supply, capacity, utilization, inventory, pricing, and margin assumptions;
- product generation or technology cycle and expected timing;
- competitive advantage, customer concentration, and supply-chain position;
- named companies, tickers, products, and explicit or implied roles;
- catalysts, risks, disconfirming evidence, and the time horizon;
- whether the claim is an observation, an assumption, a forecast, or a historical example.

Create the claim record defined in [research-contract.md](research-contract.md) for every material thesis, forecast, and candidate handoff. Record the scope and expected operating trace, not only a prose summary.

Do not turn a company inferred from a supply-chain description into a report-named candidate. Mark candidates as `explicit` or `inferred` and preserve the paragraph/section that supports the classification.

### 3. Read comments and replies

On the same report page, inspect the currently visible Disqus discussion after it loads:

- record the report-page response count separately from the currently visible comment count;
- read comment text and reply nesting, not just usernames or counts;
- classify comments as question, correction, counterexample, implementation issue, alternative thesis, praise, spam, or unrelated;
- identify author/official replies by the official account identity, not by a reader's confidence or tone;
- summarize what the official reply confirms, corrects, narrows, refuses to answer, or leaves unresolved;
- if there is no visible official reply, record `無官方回覆` rather than treating silence as agreement.

Reader comments are validation evidence and historical context, not automatically facts. A correction is only accepted as a correction when the page or official reply supports it; otherwise mark it as a disputed point.

Classify the comment-page state separately as visible, not_loaded, not_present, protected, or unknown. Never collapse not_loaded into no comments.

### 4. Compare the series across time

For each theme, build a timeline with one row per report. Compare:

- whether the supply/demand thesis strengthened, weakened, or changed;
- capacity additions, utilization, pricing, inventory, and product-cycle phase;
- whether the same companies remained beneficiaries and why;
- whether the author changed the preferred metric, valuation logic, or time horizon;
- which assumptions were confirmed by later reports and which failed;
- whether the same report sequence is being repeated for a new cycle;
- whether later comments or replies corrected an earlier claim or site definition.

Use the series-evolution labels `持續`, `更新`, `轉折`, `失效`, `未驗證`, and `資料不足`. Use the separate validation labels `not_tested`, `supports`, `weakens`, `cannot_test`, `unresolved`, and `not_applicable` only when judging evidence against a claim. Do not infer that a later article disproves an earlier one when the industry phase, product, geography, reporting scope, unit, or horizon changed.

## Forecast ledger and cycle split

Create a forecast ledger in addition to a prose timeline. Each row should contain:

- report date and URL;
- the thesis or forecast in paraphrase;
- horizon and product/geography scope;
- evidence type: report fact, author assumption, forecast, historical example, or inference;
- expected confirming or disconfirming indicators;
- series evolution: 持續, 更新, 轉折, 失效, 未驗證, or 資料不足;
- claim validation: not_tested, supports, weakens, cannot_test, unresolved, or not_applicable;
- the later report, current metric, official filing, or comment that supports the status.

Do not mark a forecast as confirmed merely because a later report repeats it. Repetition is continuity evidence; confirmation requires an observable metric, company disclosure, or clearly dated event.

For cyclical hardware industries, explicitly separate:

1. end-demand change;
2. unit or bit shipment change;
3. ASP, contract-price, or spot-price change;
4. inventory and utilization change;
5. capacity addition and qualification timing;
6. product substitution or generation change;
7. margin and cash-flow transmission to each company role.

Also record whether a product transition, customer mix change, contract structure, or capacity timing changed the meaning of the same indicator. This prevents an ASP-driven revenue increase from being mistaken for unit-demand growth and prevents a capacity announcement from being treated as immediately available supply.

## Candidate-to-company handoff

After the report timeline is complete, pass candidates to `$statementdog-stock-research`:

1. preserve the report URL or local file, report and capture dates, section, and explicit/inferred/unverified status;
2. summarize the normalized industry thesis and causal mechanism the company is supposed to express;
3. verify identity, product/process role, customer/end-market exposure, and whether the exposure is material or unknown;
4. state the competitive-advantage hypothesis and role-specific operating trace before looking at ratios;
5. check revenue growth, margins, EPS, ROE/ROA, CFO/NI, FCF, receivables, inventory, debt, dilution, valuation, price, and news in the fixed research order when current access is authorized;
6. apply the selected domain reference to qualification, capacity, substitution, utilization, pricing, and timing indicators;
7. state whether available evidence supports, weakens, cannot test, leaves unresolved, or does not apply to the historical claim. In local mode, current checks remain `current_not_checked` rather than being inferred.

Never treat “named in a report” or “passed a screen” as “buy”. A report candidate can fail current company verification, and a strong company can be absent because the historical report used a narrower universe.

## Output template

### Report record

- `order/date/title/url`
- `series/theme`
- `body thesis`
- `source mode/capture time/local file`
- `supply-demand/capacity/product-cycle assumptions`
- `named candidates` (`explicit` / `inferred`, with source section)
- `risks and disconfirming evidence`
- `report-page response count`
- `visible comment count`
- `comment themes`
- `author/official replies`
- `unresolved questions`

### Additional series fields

- forecast ledger status
- claim record IDs and normalized scope
- visual evidence state
- comment-page state
- claim-to-metric handoff for each named company role

### Series synthesis

- timeline of report conclusions;
- persistent assumptions;
- turning points and failed assumptions;
- repeated companies and changing roles;
- changes in the author's indicators or valuation rules;
- current evidence needed to verify the thesis.

### Evidence labels

Use `report_fact`, `author_assumption`, `forecast`, `historical_example`, `reader_question`, `official_clarification`, `current_metric`, `official_filing`, `inference`, or `unknown`. Include the observation or capture date and do not mix claim type with validation status.

## Safety and freshness

- Use the Codex in-app browser only in `current_site` or authorized `mixed` mode. In `local_snapshot` mode, remain offline and visually inspect the saved HTML and local images when layout matters.
- Do not use old report screenshots as proof of the current UI, current metric definition, or current price.
- Do not bypass login gates, paywalls, CAPTCHAs, query limits, or protected content.
- Do not post comments, subscribe, purchase, save reports, modify watchlists, or change account data during read-only research.
- If the archive count, Disqus count, report body, or reply list is incomplete, say exactly what was visible and what could not be verified.
