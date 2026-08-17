---
name: facebook-marketplace
description: Search, filter, sort and inspect Facebook Marketplace listings through the Codex in-app browser. Use when the user wants current Marketplace products, prices, locations, conditions, availability or listing details, while avoiding messages, purchases, saves, notifications and other side effects.
---

# Facebook Marketplace

## Purpose and entry point

Use this skill for Marketplace discovery and current listing inspection. Start from the current Facebook tab and the visible `Marketplace` link. Read [the site map](../../sites/facebook/references/site-map.md) and [the data model](../../sites/facebook/references/data-model.md) when routing or fields are unclear.

## Search workflow

1. Open `Marketplace` through the visible navigation and wait for the Marketplace landmark to settle.
2. Use `搜尋 Marketplace` for a keyword. Submit only a read-only search and verify the resulting route shape `/marketplace/<area>/search/`, the retained query text and visible listing cards.
3. Verify the current location／distance control before interpreting proximity. Do not assume the displayed area, radius or language will be the same in another session.
4. Use `篩選條件` only for safe query changes. The observed panel exposes:
   - `排序依據`: `推薦`, `距離：從近到遠`, `刊登日期：由新到舊`, `價格：從低到高`, `價格：從高到低`;
   - `最低`／`最高` price textboxes;
   - `商品狀況`, `上架日期` and `存貨狀況` submenus;
   - `查看上架商品` to apply the panel.
5. After each meaningful change, verify at least two of: query text, selected radio/filter, URL query state, result ordering or changed listing cards. Do not report a filter as applied merely because the panel opened.
6. Open a representative listing card when details are needed. Confirm the detail heading and at least one of price, availability, condition or location. Re-fetch the detail page for current values instead of trusting an old result card.

## Listing fields

The detail view can expose title, price, availability, seller, condition, description, approximate location and a map/location control. It may also show a prefilled seller message textbox, `傳送`, `儲存`, `分享` and `更多商品選項`.

Treat all prices, inventory, condition, seller identity, location and listing text as live data. Use [the data model](../../sites/facebook/references/data-model.md) for field roles, not current values.

## Safety and limits

- Reading listings, changing search/filter/sort state and opening a detail view are read-only.
- Stop before typing or sending a seller message, saving a listing, sharing, subscribing via `通知我`, opening a purchase/payment flow, listing an item, accepting age/identity verification, or following an external advertiser link. These can transmit data or create external effects and require action-time confirmation.
- Marketplace may show a restricted-experience notice that adult verification is required in the Facebook app for messaging sellers, shopping and listing; treat that as a current page explanation, not a bypass instruction.
- Do not include current item IDs, prices, seller names, tracking URLs or private user data in durable skill guidance.

## Failure handling

- Wait through loading states before classifying the page. If a search or filter produces no results, preserve the query and report the empty state.
- If the location, age gate, login, CAPTCHA or permission state blocks a branch, record the blocked capability and stop rather than switching browsers or guessing.

## Drift maintenance

Compare the live Marketplace labels, route, filter options, result card structure and detail fields with this procedure before acting. If a stable difference is directly verified, update this skill or [the site map](../../sites/facebook/references/site-map.md) with the public/authenticated state, page type, old behavior, observed behavior, evidence and date. Update retrieval and verification rules rather than current values. Re-run the affected safe search and `quick_validate.py`; report broad or ambiguous changes instead of guessing.

## References

- [data-model.md](../../sites/facebook/references/data-model.md) — MarketplaceListing fields and relationships.
- [site-map.md](../../sites/facebook/references/site-map.md) — verified Marketplace routes and filters.
- [safety-and-drift.md](../../sites/facebook/references/safety-and-drift.md) — action boundaries, freshness and maintenance.
