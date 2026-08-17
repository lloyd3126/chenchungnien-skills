# vocus Search Controls

## Entry and autocomplete

Open the visible header search icon and use the `搜尋` dialog textbox `在全站搜尋關鍵字`. After entering a non-sensitive query, wait for the suggestion panel before selecting a result. The observed groups are:

- `內容` — article/post results and `查看更多` to content search.
- `創作者` — creator/profile results.
- `沙龍` — public salon results.
- `關鍵字` — tag/keyword results.

## Result scopes

| Scope | Observed route | Verify |
| --- | --- | --- |
| Content | `/search/content?keyword=<q>` | query, `內容` tab, content card or empty state |
| Creator | `/search/user?keyword=<q>` | query, `創作者` tab, creator card |
| Salon | `/search/salon?keyword=<q>` | query, `沙龍` tab, salon card |
| Keyword | `/search/tag?keyword=<q>` | query, `關鍵字` tab, keyword list |

## Content filters

The content result page exposes two visible selects:

- Type: `全部內容`, `文章`, `貼文`.
- Sort: `發佈日期由新至舊`, `發佈日期由舊至新`, `愛心數由高至低`, `留言數由高至低`, `瀏覽數由高至低`.

One verified state was `type=article`; one verified like sort was `sort=likeCount&order=desc`. These query parameters are implementation details: confirm them from the live URL after applying a control.

## Evidence rules

After search, scope change, or filter change, verify at least two of query/URL, selected tab, selected control, first result card, page heading, or explicit empty state. Counts and order are dynamic. Do not save query terms, current counts, or personalized suggestions as facts.
