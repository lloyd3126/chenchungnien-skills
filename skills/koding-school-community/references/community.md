# 知識點與討論 reference

## Verified routes

| Need | Route pattern | Page evidence | Safe operation |
| --- | --- | --- | --- |
| Read knowledge point | `/knowledges/<slug>` | Heading, main paragraph, related links, update marker | Read only; `尚無內容` means no article content was available. |
| Course discussion | `/courses/<course-slug>/topics` | Course heading and lesson-group links | Open a lesson board. Do not publish. |
| Lesson discussion | `/courses/<course-slug>/lessons/<lesson-id>/topics` | `Lesson N > 討論區`, topic list, `搜尋` | Search and clear safely. |
| Topic detail | Same lesson board with a visible topic selected | Heading, original post, replies, `返回主題列表` | Read; do not comment. |

## Search behavior

On a lesson board, the visible `搜尋` textbox filters the topic list immediately. A safe representative test with `文字` reduced the visible list to matching titles; selecting all and deleting restored the original list. Verify the active field and visible list after each change. Topic counts and relative update times are dynamic.

## Topic and reply semantics

A topic card contains a title, author label, reply count, and relative update marker. A topic detail contains the original post followed by replies and may include a `點我專案連結` to a project/editor. That link is not permission to edit or expose the project.

`新增主題` reveals a title textbox, a rich-text editor, formatting/link/image/list controls, `取消`, and a disabled `送出` until content is entered. A reply editor exposes similar controls and a disabled `留言` until content is entered. Entering text, uploading an image, submitting, or posting is outside the read-only workflow and requires action-time confirmation.

## Data model

- Knowledge point: a slug-addressed article-like page with related knowledge links and an update marker.
- Course board: groups lesson boards under a course.
- Lesson board: scopes topics to one lesson and supports client-side text filtering.
- Topic: original question/post plus zero or more replies.
- Reply: a community response within a topic.
- Project link: an optional relation from a topic to a project route; treat as user-specific.

Keep article text, topic text, author names, reply counts, timestamps, and project ids dynamic. They are current site data, not reusable site semantics.

## Verification checklist

1. Confirm the current heading and route.
2. For a knowledge point, distinguish content from `尚無內容` and note the current update marker.
3. For a board search, verify the list narrows and restores after clearing.
4. For a topic, verify the original post and reply sequence without entering the reply editor's submit path.
