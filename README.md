<div align="center">

# Reverse Engineering Marketing

**See a competitor's marketing you like. Understand how it works, and why, from evidence.**

![version](https://img.shields.io/badge/version-1.5.0-blue) ![license](https://img.shields.io/badge/license-MIT-yellow) ![agent skill](https://img.shields.io/badge/agent%20skill-Claude%20Code-8A2BE2)

[Quick start](#quick-start) · [What you get](#what-you-get) · [What it does](#what-it-does) · [Ask it](#ask-it) · [Rules](#rules-it-follows) · [Layout](#layout) · [Feedback](#feedback)

</div>

See a competitor's ads, landing page or Instagram that you would like for your own business? Ask your agent to investigate it. It reads what is publicly visible (ad libraries, the site, the posts, the reviews), explains how the marketing is built and why, shows the evidence behind each claim, and tells you what is worth reusing.

It works on a company, an agency or a creator, in any country. If you can read the ads account (Google Ads, Meta), it also maps the account from the inside, read-only. Every claim is tied to a source and labelled OBSERVED, DERIVED, INFERRED or UNKNOWN, with the limits of each search stated.

It is an agent skill: plain instructions your agent follows (Claude Code, and any agent that reads `SKILL.md` skills). Nothing runs in the background and nothing is sent anywhere.

Inspired by the evidence-first method of [REA, Reverse Engineer Anything](https://github.com/morluto/rea), applied to marketing instead of software. Not affiliated with REA.

## Quick start

### 1. Install it
In Claude Code, run:
```bash
/plugin marketplace add danscalzo/reverse-engineering-marketing
/plugin install reverse-engineering-marketing
```
No plugin support in your agent? Copy the folder `skills/reverse-engineering-marketing/` into `~/.claude/skills/` (or wherever your agent reads skills).

What helps: a browser tool the agent can drive (to read ad libraries, landing pages and profiles) and web search. Optional: a Meta Ads MCP for ad library search, Google Ads API credentials for inside mode.

### 2. Launch it
Just ask, in your own words and in any language. Give it a URL, a brand name or a profile:
```text
Reverse engineer the marketing of https://example.com
```
Or call the skill by name with the target:
```text
/reverse-engineering-marketing https://example.com
```
(installed as a plugin, the command is `/reverse-engineering-marketing:reverse-engineering-marketing`).

### 3. Choose how deep
| Say | Time | You get |
|---|---|---|
| "quick" | ~15 min | Ad inventory, landing hero, offer, competitors in one line, a chat summary |
| nothing (standard) | ~1 h | The 12 questions, last 10 posts, site copy, competitors, a report file with evidence |
| "deep" | 2 h+ | Everything, every key video frame, landing section by section, a reusable playbook |

### 4. Read the result
The answer comes in chat; at standard and deep depth the agent also saves a report and an evidence folder in `./research/` (change the folder in `references/local.md`).

> [!IMPORTANT]
> Get this skill from [danscalzo/reverse-engineering-marketing](https://github.com/danscalzo/reverse-engineering-marketing). A similar repository name or a copied README does not make a download official.

## What you get
A report where every line can be checked.

**[Read the full sample report](examples/sample-report.md)** (fictional retailer, every name and number invented): the 12 questions, the last 10 posts, the site copy, the competitors, the verdict and the evidence ledger.

An extract from its ledger:

| ID | Claim | Class | Evidence | Search boundary |
|---|---|---|---|---|
| E01 | 38 active Meta ads, oldest running 74 days | OBSERVED | Ad Library screenshot, US, active, 2026-11-09 | One page name; other names not found |
| E02 | 5 concepts, 33 variations (same video, new first line) | DERIVED | Frames of all 38 ads | Active ads only |
| E04 | Ads that run longest probably convert | INFERRED | Run length in E01 | No spend data: hypothesis only |
| E06 | Meta Pixel, GA4, Google Ads tag, Klarna widget | OBSERVED | tag-scan output, consent accepted | 3 pages, one load |
| E08 | Spend | UNKNOWN | Not public for commercial ads | Needs account access |

How a run goes:
1. **Fix the target**: brand, domains, pages, country, business type.
2. **Sweep the evidence**: ad libraries, site and tags, last 10 posts, reviews, and the ads account if you can read it.
3. **Answer the 12 questions**, each with its evidence ID and its class.
4. **Deliver**: report with ledger, how they communicate and to whom, competitors by name, verdict, one experiment to run.

## What it does
- **Two modes**: outside-in on any competitor from public evidence, or inside an ads account you can read (Google Ads, Meta): structure, keywords, search terms, bidding, budgets, assets, conversions.
- **Fixes the target** (brand, domains, pages, country) and the **business type** (ecommerce, lead gen, local, finance...) before judging anything.
- **Any market**: adapts sources and ad rules to the subject's country and sector.
- **Three depths**: quick (15 min), standard (1 h), deep (full teardown).
- **Routes by input**: an ads account, a company name, a landing URL, creatives, a creator profile, an agency name, several competitors.
- **Creative teardown**: concepts vs variations, every key video frame, hook types, credibility inventory.
- **How they communicate**: the last 10 posts read one by one (recurring theme and what it is for, product or mood, AI-made images or not, who it is aimed at vs who buys) and the site copy.
- **Competitors always named**: 2-4 at top level in every analysis; the full comparison only if you ask.
- **Compare and monitor**: competitor matrix, monthly snapshots and diffs.
- **Evidence tools**: `tag-scan.js` (tags and form vendors on any page) and `gads_map.py` (read-only Google Ads account map).
- **Summary first, then drill down**: inventory of ads, pages and channels; deep dives only where a question is open.
- **Answers 12 questions**, each with the reason behind the choice: structure, budget, audience, visual creative, copy, angle and offer, credibility, funnel, tracking, organic communication, reputation, who runs it.
- **Bounded claims**: "no Google ads found for example.com, US, last 30 days", never "they don't do Google".
- **Delivers** a report with a findings ledger, a verdict and one experiment to run; at deep level also a section-by-section landing breakdown with screenshots.

## Personalise it
Add `skills/reverse-engineering-marketing/references/local.md` (git-ignored) with your language, output folder and private rules. The skill reads it first.

## Ask it
```text
Reverse engineer the Meta ads and landing page of <brand>, <country>.
What is <agency> doing for its clients, and what does it charge?
Break down <creator>'s content and how it turns into customers.
```

## Rules it follows
Public sources, official APIs or access you already hold. Read-only in other people's accounts. No fake leads, logins, CAPTCHA bypass or scraping where terms forbid it. Analyses businesses, not people. Rebuilds logic, never copies creatives. See [DISCLAIMER.md](DISCLAIMER.md).

## Layout
```
skills/reverse-engineering-marketing/
  SKILL.md                 core method (routing, 12 questions, evidence rules, guardrails)
  references/
    sources.md             verified public sources + 30-minute sweep
    market-adapter.md      adapt sources and rules to any country and sector
    business-type.md       what "well built" means per business type
    creative-analysis.md   concepts, video frames, hooks, credibility
    compare.md             several competitors side by side
    monitoring.md          snapshots and diffs over time
    google-ads-account.md  inside mode for Google Ads (map + read-only GAQL)
    account-access.md      inside mode for Meta (Ads Manager, Events Manager)
    landing-site-tracking.md
    organic.md
    personal-brand.md
    reading-and-verdict.md
    report-template.md
    example-case.md        fictional worked example
  scripts/
    tag-scan.js            read-only tag and form scan (browser)
    gads_map.py            read-only Google Ads map (GAQL)
examples/sample-report.md  full sample report (fictional)
evals/scenarios.md         test prompts and expected behaviour
```

## Feedback
Early version (beta). If something is missing or wrong, open an issue: what you asked, what it did, what you expected.

MIT licence.
