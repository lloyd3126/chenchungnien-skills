---
name: sec-regulatory-monitoring
description: Monitor and verify current SEC.gov newsroom items, press releases, speeches, meetings, rulemaking activity, public-comment dockets, and related SEC regulatory documents through the Codex in-app browser. Use for SEC news, proposed or final rules, comment periods, events, statements, or enforcement updates.
---

# SEC Regulatory Monitoring

## Purpose and entry points

Use the Codex in-app browser on the already-visible SEC tab for public, read-only monitoring. Read [sites/sec/AGENTS.md](../../sites/sec/AGENTS.md), [site-map.md](../../sites/sec/references/site-map.md), and [first-party-guidance.md](../../sites/sec/references/first-party-guidance.md) when route or terminology details matter.

- News, press releases, speeches, events, videos, social directory, or podcasts → `https://www.sec.gov/newsroom`
- Rulemaking status or activity → `https://www.sec.gov/rules-regulations/rulemaking-activity`
- Active proposals and public comments → `https://www.sec.gov/rules-regulations/submit-public-comments`
- SEC data/research update or API documentation → route through the site navigation and consult the first-party guidance; for filing/API field work use `$sec-filings-research`.

## Procedure

1. Inspect the current tab URL, title, heading, and visible page state. Actually open the target in the same tab and capture a screenshot before treating the page as available.
2. On `Newsroom`, select the visible category that matches the request: `Press Releases`, `What's New`, `Meetings & Events`, `Speeches & Statements`, `Videos`, `Social Media Directory`, or `Podcasts`. Open a specific item only from a visible current link.
3. For each news item or event, verify category, title, published or event date, detail URL, source office, and whether the body/document loaded. Report the retrieval time because the lists change.
4. On `Rulemaking Activity`, use the visible search field and filters. The observed status options are `Final`, `Interim Final`, `Proposed`, `Interpretive`, and `Concept`; the division/office and year lists are also available. After filtering, verify the selected values, activity title, rule identifier, status, and detail anchor. Use `View Related Activity` only when it is visible on the current result.
5. On `Submit Public Comments`, open the proposal or request that matches the user's topic. Read the official notice/PDF and use `View Comments Received` for public comments. A `Submit a Comment` link is only an entry point; never fill or submit it as part of exploration.
6. Distinguish a proposal/request, final rule, interpretive release, concept release, SRO notice, speech, enforcement release, and public comment docket. Do not treat a news headline as a legal conclusion or a current rule without opening the underlying first-party document.
7. Return the source URL, item title, document or rule identifier, date, current filter/query, and freshness caveat. Do not write live result lists, counts, rankings, or comment text into reusable guidance.

## Page and field semantics

- Rulemaking status and year are filters, not conclusions about a rule's current legal effect; read the detail page and official document.
- `View Comments Received` is a read-only public collection route. Comment availability and comment-period state are dynamic.
- `Submit a Comment`, `Submit a Tip or Complaint`, email alerts, and GovDelivery forms transmit user data or create an external effect.
- Newsroom category labels are routing hints; verify the item's detail page, date, and source office before summarizing.

## Safety and limits

- Default to read-only. Do not submit a public comment, complaint, email, subscription, filing, or form.
- Do not treat a proposal, press release, speech, enforcement allegation, or third-party comment as an independently verified legal or factual conclusion; describe the source and its status.
- If the user wants to submit a comment, stop immediately before the content is entered or sent and ask for action-time confirmation that identifies the SEC destination and data to transmit.
- Do not use external browsers, web search, CLI, direct APIs, cookies, local storage, or session files to bypass the in-app browser boundary.
- If a target is blocked, requires login, shows a CAPTCHA/security interstitial, or the active tab is unavailable, report the evidence and stop that branch.

## Drift maintenance

Compare current visible navigation, filters, labels, page sections, permissions, and SEC first-party explanations before acting. If a stable route or control changes, complete the smallest safe adaptation, record public/authenticated variant, old/new behavior, verification evidence, and date, then update the owning site reference or skill and rerun `quick_validate.py`. Never store passwords, cookies, tokens, private data, current headlines, dynamic counts, or speculative legal meaning. Mark broad or ambiguous changes as a maintenance gap.

## References

- [site-map.md](../../sites/sec/references/site-map.md) — newsroom, rulemaking, public-comment, and evidence coverage.
- [first-party-guidance.md](../../sites/sec/references/first-party-guidance.md) — SEC rulemaking/comment/API definitions and freshness limits.
- [agent-usability.md](../../sites/sec/references/agent-usability.md) — monitoring request shapes, verification, and safety stops.
