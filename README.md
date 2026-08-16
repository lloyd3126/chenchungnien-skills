# Chen Chung Nien Skills

[繁體中文](./README.zh-TW.md)

A curated collection of reusable agent skills designed by Chen Chung Nien.

This repository showcases the skills I design and publish to help AI agents work more reliably in specific domains.

## About

Each skill in this repository is designed to be practical, maintainable, and clearly scoped for real work instead of one-off prompting.

## Skills In This Repo

| Skill | Description |
| :--- | :--- |
| [`tw-gov-data`](skills/tw-gov-data) | Discover, inspect, compare, and summarize datasets from Taiwan's government open data platform, `data.gov.tw`. |
| [`tw-stock-data`](skills/tw-stock-data) | Fetch, validate, and analyze Taiwan stock, OTC, futures, options, and MOPS financial datasets using the `tw-stock` CLI. |
| [`website-skill-builder`](skills/website-skill-builder) | Systematically explore a website in Codex's built-in browser and turn its stable structure, workflows, and data model into reusable agent guidance. |
| [`tabelog-search`](skills/tabelog-search) | Search and filter public Tabelog listings in Codex's built-in browser, including autocomplete-based area selection and result verification. |
| [`tabelog-restaurant`](skills/tabelog-restaurant) | Inspect Tabelog restaurant pages and related menus, photos, reviews, ratings, maps, and availability through the built-in browser. |

## Website-specific Guidance

The [Tabelog site package](sites/tabelog/AGENTS.md) provides routing, session, freshness, and verification guidance for the Tabelog skills. Its [references](sites/tabelog/references) document the sitemap hierarchy, data model, and first-party explanations discovered during exploration.

## Usage

Use `website-skill-builder` when a website should become a reusable tool for future agents. It explores the current tab in Codex's built-in browser, starts with the site's sitemap when available, covers public functionality first, and asks before exploring protected functionality that requires login.

For Tabelog tasks, use `tabelog-search` for listings and filters, and `tabelog-restaurant` for restaurant details and subpages. Future agents should compare live UI and documentation with these files and update stable, verified differences when the workspace is writable.

## Installation

You can browse and install skills from this repository using the [Vercel skills CLI](https://skills.sh/docs/cli).

### Using Vercel skills CLI

```sh
# Interactively browse and install skills from this repo.
npx skills add lloyd3126/chenchungnien-skills --list

# Install a specific skill globally.
npx skills add lloyd3126/chenchungnien-skills --skill tw-gov-data --global
npx skills add lloyd3126/chenchungnien-skills --skill tw-stock-data --global
npx skills add lloyd3126/chenchungnien-skills --skill website-skill-builder --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-search --global
npx skills add lloyd3126/chenchungnien-skills --skill tabelog-restaurant --global
```
