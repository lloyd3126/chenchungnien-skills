# PokecaBook public search

Exploration basis: 2026-08-17, using the Codex in-app browser on the public site. Query values and result contents are dynamic.

## Observed form

- Entry: `https://pokecabook.com/`.
- Visible label and placeholder: `サイト内を検索`.
- Observed input: `name="s"`, text input.
- Observed form action: site root, using a GET query.
- A safe derived result route is `https://pokecabook.com/?s=<URL-encoded keyword>`.

The first semantic fill-and-Enter attempt did not navigate, and a visible submit click was offscreen in one state. That is a browser-control limitation, not evidence that search is unavailable. Direct same-origin navigation derived from the observed form opened a result page successfully.

## Result semantics

For the observed keyword `リザードン`, the result page title was `“リザードン” の検索結果 | PokecaBook`, the main heading was `"リザードン"`, and result cards carried PokecaBook category labels such as `ポケカコラム`, `デッキレシピ`, `ジムバトル`, and `Tournament results`. Detail links use `/archives/<numeric-id>`.

Pagination was visible as `次のページ`, page numbers, and `次へ`. Observed forms included `/page/2?s=...` and `?s=...&paged=2`; preserve the live link rather than constructing a page URL from memory.

## Verification contract

After search, verify the keyword in the title/heading or URL, at least one result card or the explicit empty state, and pagination when present. Record the exact query and page route. Do not write result counts, dates, or rankings into reusable artifacts.
