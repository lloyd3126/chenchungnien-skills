---
name: tabelog-restaurant
description: Inspect a public Tabelog restaurant detail page and its menu, seats, photos, reviews, rating distribution, map, and current reservation-availability fields through the Codex in-app browser. Use when a restaurant is already known or has been selected from a Tabelog result.
---

# Tabelog Restaurant

## Purpose and entry point

Use this skill after a result card, area page, ranking, or user-provided Tabelog URL identifies a restaurant. Work only in the Codex in-app browser. Read [page-types.md](references/page-types.md) for the confirmed subpage map and [the data model](../../sites/tabelog/references/data-model.md) for entity semantics.

Start at the restaurant URL and re-read the current DOM. Do not rely on a cached restaurant name, price, rating, review count, photo count, opening hour, or availability.

## Procedure

1. Confirm the restaurant title and canonical visible breadcrumb. Capture the current restaurant URL and the page state.
2. Read the top-level identity fields: name, rating, review count, save count if shown, station/area, genres, dinner/lunch budget, and the `店舗情報（詳細）` link.
3. Read the detail table only for fields relevant to the user's request: reservation availability, address, transport, opening hours, budget, payment, invoice, service charge, seats, private room, charter, smoking, parking, space/equipment, children, languages, official links, and update/opening information.
4. Use the confirmed tabs as needed:
   - `トップ`: overview, notices, features, recent reviews and store details.
   - `座席`: seat types, photos/descriptions, and a possible seat reservation entry.
   - `メニュー・コース`: courses, dishes, drinks, lunch, and menu photos.
   - `写真`: official/user photos, category, sort, size, and pagination.
   - `口コミ`: review search, meal type, sort, reviewer, visit date, ratings, photos, and store replies.
   - `平均・分布`: simple user-rating averages/distributions and spend distributions; distinguish these from the restaurant score.
   - `地図`: address, transport, map, Google Maps region, and nearby restaurants.
5. For a current availability request, set only the requested date, party size, and time in the visible reservation widget, inspect the available state, and stop before `予約する` unless the user separately confirms that action. Availability is dynamic and may lead outside Tabelog.
6. Verify every reported value against the current page. For reviews and photos, include the page's date/ordering context and warn that historical content may not reflect the current restaurant.

## Page and field semantics

- The restaurant ID in the detail URL is the stable page key; names, ratings, counts, prices, and operating status are not stable identifiers.
- `店舗基本情報` is the primary structured source for contact, location, hours, budgets, payment, seats, and facilities.
- `口コミ` is user-submitted subjective experience, not a verified statement of fact or absolute restaurant quality. See [first-party-guidance.md](../../sites/tabelog/references/first-party-guidance.md).
- `平均・分布` may show simple averages of user-submitted dimensions while the headline restaurant score uses Tabelog's own algorithm; do not combine them without explaining the distinction.
- Menu item prices and descriptions are page snapshots and may be stale; confirm with the restaurant when material.
- `行った`, `保存`, `投稿`, photo posting, reviewer follow, and reservation submission can change state or require login. Observe the entry and stop at the login or confirmation boundary.

## Authentication boundary

Finish public detail and subpage exploration first. If a detail action leads to `/account/login/`, record the protected capability and continue with public tabs. After the public second-pass audit, ask whether the user wants protected functionality explored. Only after consent should the user manually sign in in this same in-app browser tab.

Treat authenticated Tabelog as a separate variant. Revisit the restaurant top, details table, every previously used tab, public review/photo/menu controls, and reservation form controls after login; compare navigation, fields, options, defaults, permissions, and result state before exploring protected lists or posting workflows.

## Safety and freshness

- Never submit a review, photo, save, mark-visited, booking, payment, or edit/delete action during exploration.
- Do not expose phone numbers, personal reviewer data, hidden form tokens, cookies, or login information unless the user's task explicitly requires a visible public field.
- Stop at CAPTCHA, safety interstitial, or an unclear external authentication/booking page.
- State the retrieval time and query parameters for dynamic availability, prices, rankings, ratings, and counts.

## Drift maintenance

Before using this procedure, compare the live restaurant page and subpage tabs with the documented routes and fields. If a stable page type, tab, field, route, permission, or verification rule differs, use the current UI safely, capture the public/authenticated state and evidence, and update this skill or its references in the authorized workspace. Do not write current menu prices, ratings, review counts, photo counts, opening status, or availability into the documentation. Re-run the affected safe inspection and `quick_validate.py` after a clear update; report ambiguous or broad changes instead of guessing.

## References

- [page-types.md](references/page-types.md) — detailed public subpage routing and fields.
- [data-model.md](../../sites/tabelog/references/data-model.md) — Restaurant, Review, Menu, Photo, Rating, and availability relationships.
- [first-party-guidance.md](../../sites/tabelog/references/first-party-guidance.md) — Tabelog's own review and rating definitions.
