# SEC／EDGAR 操作資料模型

這是依 SEC.gov／EDGAR UI 與一方 API 說明整理的操作模型，不是 SEC API 的完整 schema。現場顯示的 filing、新聞、規則、數量與日期必須每次重新取得。

## Entities

| Entity | Identifier / important fields | Related pages |
| --- | --- | --- |
| Filer / Entity | CIK（10 位、含前導零）、current/former name、ticker、exchange、SIC、state/country、fiscal year end、mailing/business address；角色可為 Filer、Subject、Filed by 或 Reporting。 | Company Search、CIK Lookup、Latest Filings、Filing Detail、`data.sec.gov/submissions/CIK##########.json` 說明 |
| Filing | Form type、description、accession number、filing date、accepted timestamp、reporting-for date、Act、file number、film number、ownership role。 | Full Text Search、Latest Filings、Company filing list、Filing Detail |
| Filing Document | Sequence、description、document URL、document type、size；常見可見入口為 primary HTML/XML 與 complete submission text file。 | Filing Detail 的 `Document Format Files` table |
| Search Query | keyword／phrase、company name、ticker、CIK、individual name、filing category/form、date range、principal executive office location、entity/form/location filters、Show Columns。 | `/edgar/search/` |
| Latest Filings Query | Company、CIK、Form Type、ownership Include／Exclude／Only、entries count、start/page state、RSS feed。 | `getcurrent` |
| Rulemaking Item | title、rule identifier、status、division/office、year、detail anchor、related activity、proposal／final／concept document。 | Rulemaking Activity、rule detail |
| Public Comment Docket | docket / release identifier、proposal or request document、comment submission link、comments-received link、comment period state。 | Submit Public Comments、public-comments detail |
| News Item / Event | category、title、published／event date、body or document link、office/source、detail URL。 | Newsroom、Press Releases、Speeches & Statements、Meetings & Events |
| API Dataset | Submissions history、XBRL companyconcept、companyfacts、frames；bulk ZIP is a separate delivery surface with its own update schedule。 | EDGAR API page、Developer Resources |

## Relationships

```text
Filer / Entity
├── has many → Filing
├── identified by → CIK
├── may expose → ticker / exchange / SIC / fiscal year end
└── has current history → Submissions API JSON

Filing
├── has → accession number and accepted / filing dates
├── includes → Filing Document(s)
├── may identify → Filer / Subject / Filed by / Reporting entity
├── may link → SIC, file number, film number
└── may expose → primary document, XML, complete text

Rulemaking Item
├── belongs to → status / division / year filter
├── links to → notice, proposal, final or concept document
└── may link to → Public Comment Docket and related activity

News Item / Event
└── belongs to → newsroom category and source office
```

## Identity and interpretation rules

- CIK 是比名稱或 ticker 更穩定的 filer/entity identifier；查詢後仍核對名稱、ticker／exchange 與頁面 heading。
- Accession number 識別一個 filing submission；document URL 可能只是其中一個 component。若從 Archive component URL 進入，優先尋找相同 accession 的 `-index.htm` Filing Detail。
- `Filer`、`Subject`、`Filed by`、`Reporting` 是 filing 關係角色，不是同義詞；Latest Filings 的 Key to Descriptions 需一起讀。
- `Filing Date` 與 `Accepted` 不是同一欄位；報告時保留兩者及時區／頁面顯示方式。
- Rulemaking status、public comment period、news category、filing rows、XBRL facts 與 API JSON 都是時間敏感資料；模型只提供欄位語意，不提供現值。
