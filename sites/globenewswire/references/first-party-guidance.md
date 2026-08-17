# GlobeNewswire first-party guidance and interpretation limits

## What the site says about itself

The public `/about` page describes GlobeNewswire by Notified as a global news distribution platform for press releases, financial disclosures, and corporate communications. It says the service supports delivery to media, investors, analysts, and the public, with editorial review, regulatory expertise, secure workflows, and global distribution. The `/services` page groups offerings under PR and IR solutions, including press release distribution, regulatory filings, AI press release tools, media contacts, monitoring, and analytics.

These are first-party descriptions of the service. They are useful for routing and terminology, but they are not independent verification of distribution reach, regulatory status, performance, or any claim in a particular release.

## Site terminology and durable definitions

- `Press Release Distribution`: the site's public service description for targeted global news distribution.
- `Regulatory Filings`: the site's service category for EDGAR, SEDAR, XBRL, and European Transparency workflows.
- `CLEAR®`: the service page's identity-verification link for sharing news through GlobeNewswire.
- `SEO` / `AEO`: the About FAQ says GlobeNewswire formats releases with structured metadata, rich content formatting, and relevant keywords for search and answer-engine discovery. Treat this as a product claim, not a guarantee of ranking or citation.
- `RSS by Subject`, `RSS by Industry`, and `RSS by Location`: directory groupings for public feed links. The actual feed entries and available groups are live and must be inspected when requested.

## Content and disclosure limits

- A release's body, company profile, forward-looking statements, and quoted claims are attributed publisher content. Do not silently rewrite issuer claims as independently established facts.
- Financial, regulatory, medical, legal, investment, or market-sensitive conclusions require the relevant official filing, company source, regulator, or other authoritative source; the GlobeNewswire page alone is a distribution surface.
- Release time, language, source organization, tags, category, result order, and feed entries can change or be corrected. Record the observation time and re-open the page when freshness matters.
- The site may link to Notified, a company website, SEC, social networks, or other external destinations. Do not follow or transmit information to those destinations unless the user asks and the action is safe and authorized.

## Public versus protected boundaries

The public site exposes newsroom browsing and release reading. Top navigation `Sign In` leads to a Notified login page with a Username step and reCAPTCHA; `Sign into Reader Account` is a protected reader branch, and `Create Reader Account` leads to an external registration page. Do not enter credentials, solve CAPTCHA, or infer account permissions during public research.

## Verification pattern

For a material result, retain at least two signals: current URL or visible link, page heading, selected filter/chip, release title, source, publication time, or explicit error/empty state. A successful navigation API call, hidden DOM, or URL alone is not enough. If browser screenshot capture fails, report the limitation separately and rely only on current-tab DOM/interaction evidence that was actually obtained.
