# PR Newswire interaction guide

## Search

1. From any public page, click the visible `Search` button.
2. Use the visible textbox with placeholder `Search News Releases, Organizations, Resources, and Products`.
3. Enter the exact user keyword and wait for the overlay state. An overlay may show `Searching for your content...` or `No results found`; this is not the final result page.
4. Press Enter to submit. Verify the result URL, a heading such as `All Search Results` or `News Search Results`, the displayed keyword, and at least one result or an explicit empty state.
5. Use the visible result-type tab: `All`, `News`, `Organizations`, `Products`, or `Resources`. Preserve the query; do not silently broaden it.

Search result lists may expose `Select number of items per page` with 25/50/75/100 options. In the observed News search, 75 and 100 were disabled while 25 was selected; re-check the current page before relying on those limits.

## News lists

Category and organization list pages expose:

- `Jump to News Releases:` date input with `MM/dd/yyyy` placeholder
- an hour selector from `00:00` through `23:00`
- `Go` button
- `Select number of items per page` (observed options 25, 50, 75, 100)
- `Latest` release cards with timestamp, title, summary, and optional image

For a time slice, enter/select only a non-sensitive representative date/time, click `Go`, then verify the selected date/time and the first release timestamp. The route may encode `month`, `day`, `year`, and `hour` query parameters. Counts, order, and rows are dynamic.

## News menus and detail pages

Expand a visible news-menu button and select a child link that is actually shown. On a detail page, verify the release title, `News provided by` organization, ET timestamp, bullets/body, and any `Also from this source` or `Explore` links. Do not click Facebook/Twitter/LinkedIn/WhatsApp/email/Pinterest sharing controls; they can transmit or publish content.

## Resources

The Resources overview exposes section tabs and a list with page-size and category controls. Use visible tabs such as `Articles`, `White Papers`, or `Webinars` when the user's intent is a resource type. Resource detail pages are read-only article/guide pages; verify the title, body, and first-party links before summarizing.

The category `<select>` may update asynchronously and can be unreliable under browser control. If it does not complete, use the visible resource-section route instead of retrying blindly. Verify the resulting heading and resource type.

## Public forms and protected branches

`Request a Demo`, `Contact Us`, and `Send a Release` forms contain personal/contact fields, organization data, terms or marketing language, and reCAPTCHA. Inspecting fields is allowed; do not fill, check contractual consent, solve CAPTCHA, or submit without explicit action-time confirmation. `Client Login` opens a Cision username screen; never enter credentials or OTPs. Protected workspace behavior remains unconfirmed.

## Evidence and drift

After every navigation or meaningful interaction, collect at least two signals: current URL, heading, selected option, result title, or explicit state. Keep current-tab visual, current-tab DOM/interaction, and automation/control errors distinct. Before use, compare the live UI with this file; patch stable, verified drift in the owning skill and run `quick_validate.py`.
