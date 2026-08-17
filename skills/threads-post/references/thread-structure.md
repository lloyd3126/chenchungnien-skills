# Threads Post and Reply Structure

## Root post detail

Observed public post detail pages contain:

- a `返回` control and `串文` heading
- a view indicator when available
- author profile link, topic links, and time link
- root text and optional multi-image, video, music, or external-link preview
- like, reply, repost, and share controls
- a reply section with sorting and activity controls

## Reply controls

The observed reply area included:

- `排序 熱門` — current reply ordering label; re-read any menu before choosing another option
- `查看動態` — visible activity entry point, not explored in this pass
- a reply textbox labeled `文字欄位空白。請輸入內容以撰寫新貼文。`
- `附加影音內容`、`新增 GIF`, and `展開撰寫工具`

The composer must be treated as a transmission boundary. Read its presence if needed, but never fill or submit it during a read-only task.

## Reply item fields

Read fields in this order when requested:

1. reply author and public profile link
2. time link and post ID if visible
3. parent context or author marker
4. reply text, media, translation label, or external preview
5. current engagement labels

Do not equate a reply's dynamic counts with its importance or truthfulness.

## Media handling

Use media links exposed by the current DOM. Multi-image content may expose `1 / N`, alt text, and separate media links. Video can expose a `Video player` group and muted state. Music can expose a play control and track metadata. These are presentation details; verify the current page rather than relying on this sample.
