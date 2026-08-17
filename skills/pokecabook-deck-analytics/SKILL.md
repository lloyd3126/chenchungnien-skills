---
name: pokecabook-deck-analytics
description: Search and compare public PokecaBook deck recipes and card-adoption analysis through the Codex in-app browser. Use when the user asks for deck filters, tournament date/rank/prefecture conditions, deck categories, card-name counts, or live card adoption results.
---

# PokecaBook Deck Analytics

## Purpose and entry points

Use this skill for the two public query pages:

- `https://pokecabook.com/deckshow` — `デッキレシピ検索` / `デッキ検索`.
- `https://pokecabook.com/card-adoption-rate` — `カード採用率`.

Both open a `条件検索` modal and load results asynchronously. Read [filter-controls.md](references/filter-controls.md) for the observed fields and route-specific differences. Use `$pokecabook-content-research` for article pages that explain a deck or ranking rather than returning filtered data.

## Procedure

1. Inspect the current public tab and use one of the two entry routes above. Keep the same tab and do not inspect cookies, storage, or session data.
2. Click the visible `条件検索` button. Re-read the modal after it opens; do not assume the live default dates or option set.
3. Set only the conditions the user requested:
   - `開催期間`: two date inputs; use the current UI values or the user's explicit range.
   - `カテゴリ`: visible deck category select.
   - `カード名` and `カード枚数` (`最小`/`最大`): available on `deckshow` only.
   - `順位`: open `順位を選択`, then choose visible rank options such as `優勝`, `準優勝`, `TOP4`, `TOP8`, and `TOP16` when present.
   - `都道府県`: open `都道府県を選択` and choose visible locations when the user asks for a prefecture scope.
4. Submit the modal's `検索` button. This is a read-only query, but it may update the page through AJAX rather than navigation.
5. Wait for `読み込み中...` to settle. Verify the active conditions plus result cards/table or the explicit empty state (`該当するデッキがありません。` / `該当するカードがありません。`). Do not treat the loading state as a result.
6. Report the query conditions and live result state. Never carry observed dates, counts, adoption rates, rankings, or card lists into a future task without refetching.

## Safety and limits

- Use exact visible labels and verify duplicate controls; the shared site header also contains a search form.
- Do not submit comments, inquiries, social sharing, deck publication, save/favorite actions, or external Pokémon deck-code links as part of analytics.
- A no-result response may be caused by the selected date/category/rank combination; report the exact query rather than broadening it silently.
- Stop at CAPTCHA, login, safety interstitial, or an external confirmation page.

## Verification and drift maintenance

At minimum, confirm two of: modal heading/selected values, visible query conditions, URL/title, loading completion, result heading/cards, or explicit empty state. Before each task compare the live modal labels, fields, and options with [filter-controls.md](references/filter-controls.md). If stable behavior differs, use the current safe UI, record the mismatch with the date, update the owning artifact, rerun the affected query, and run the skill validator.

## References

- [filter-controls.md](references/filter-controls.md) — modal fields, shared options, route-specific semantics, and AJAX verification.
- [site-map.md](../../sites/pokecabook/references/site-map.md) — public site inventory and dynamic-data cautions.
