# PokecaBook deck and card-adoption filters

Exploration basis: 2026-08-17, public state in the Codex in-app browser. Defaults, options, and returned data can change.

## Shared modal

Both `/deckshow` and `/card-adoption-rate` expose `条件検索` and a modal with:

- `開催期間`: two `input[type=date]` controls. The observed values represented a recent rolling window; do not hard-code them.
- `カテゴリ`: a select whose observed options included `Tier3`, `ドラパルトex系統`, `メガルカリオex`, `マリィのオーロンゲex`, `Nのゾロアークex`, `タケルライコex`, `オリーヴァex`, `オーガポンバレット`, `メガゲッコウガex`, and `メガユキノメex`. Re-read the live list before selecting.
- `順位`: a button that revealed options including `優勝`, `準優勝`, `TOP4`, `TOP8`, and `TOP16`.
- `都道府県`: a button that revealed location options; observed examples included `東京`, `京都`, `大阪`, and `沖縄`.
- `キャンセル` and `検索`.

## Route-specific fields

`/deckshow` additionally exposes `カード名` (`カードの名前を入力`) and two number inputs with placeholders `最小` and `最大` for card counts. Its page heading is `デッキ検索`, with a link to card adoption.

`/card-adoption-rate` exposes the card-adoption result view and a link back to deck search. Its page heading is `カード採用率`; it does not expose the deck-search card-name/count inputs.

## AJAX verification

Submitting the modal may leave the URL unchanged. The page can show `読み込み中...` and then either result cards/tables or an explicit empty message (`該当するデッキがありません。` or `該当するカードがありません。`). Wait for the loading text to settle and re-read the selected conditions before reporting.

## Safe interaction boundary

Opening the modal, selecting filters, expanding rank/prefecture choices, canceling, and submitting a read-only query were treated as safe. Do not click comments, social links, save/publish controls, or external Pokémon deck-code links during analytics.
