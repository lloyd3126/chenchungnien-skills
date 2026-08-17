# AnnualReports.com data model

Keep the entity structure below separate from the live values shown on a page.

## Entities

### Company

The canonical public entity is a company profile at `/Company/<slug>`.

Observed fields and relationships:

- display name and logo/banner imagery;
- ticker symbol;
- exchange, with a `More` link to `/Companies?exch=<id>`;
- industry, with a `More` link to `/Companies?ind=<id>`;
- sector, with a `More` link to `/Companies?sect=<id>`;
- short description, employee-size label, and base location when supplied;
- optional `Visit website` external link;
- optional report usefulness rating summary;
- one current-report entry and zero or more archived-report entries;
- optional sustainability-report link to ResponsibilityReports.com;
- optional hardcopy request control.

The company list entity is a lighter projection: company name/slug plus industry and sector. Search, exchange, industry, sector, and alphabetical pages all return this projection.

### Taxonomy

Taxonomy is represented by visible labels and query parameters, not by a documented API schema:

- exchange: `exch`;
- industry: `ind`;
- sector: `sect`;
- alphabetical prefix: `a`.

Numeric IDs are opaque. Resolve them from visible links rather than guessing.

### Annual report

An annual report entry is linked to a company and has:

- report period/year label;
- report type label, such as Annual Report or Form 10-K;
- format, commonly PDF, HTML, Form 10-K HTML, DOCX, or legacy external HTML;
- current-report tracking/open target, commonly `/Click/<id>`;
- archive file path under `/HostedData/AnnualReportArchive/...`;
- optional `View Annual Report` target and/or `Download` link.

Current-report buttons in the observed profile used a `window.open` tracking target and also opened a rating modal in the current page. This is a UI behavior, not proof that the report target was successfully opened.

### Report rating

The company profile can show a live aggregate usefulness score and review count. The report viewer prompt exposes five radio ratings and a `Submit` action. Ratings are dynamic and submitting one is a representational side effect; do not write current values into skills or submit without explicit user direction and confirmation.

### Provider/contact forms

`AddCompany` and `sendreportsform` are outbound forms with company/contact/shipment fields. They are not part of read-only research. A visible button is not permission to transmit data.

## Entity routing

```text
keyword / exchange / industry / sector / alphabet
        ↓
company-list row (name + taxonomy)
        ↓
company profile (identity + report entries)
        ↓
current or archived annual-report link
```

When a profile exposes a sustainability report or official website, treat it as a separate external entity and preserve the boundary between AnnualReports.com evidence and third-party evidence.
