# Reverse Engineering Marketing

**See a competitor's marketing you like. Understand how it works, and why, from evidence.**

An agent skill (Claude Code, and any agent that reads `SKILL.md` skills) that reverse engineers the marketing of a company, an agency or a creator: ads, audience, creative, copy, offer, landing page, funnel, tracking, organic socials, reputation, and who runs it. Every claim is tied to a source and labelled OBSERVED, DERIVED, INFERRED or UNKNOWN.

Inspired by the evidence-first method of [REA, Reverse Engineer Anything](https://github.com/morluto/rea), applied to marketing instead of software. Not affiliated with REA.

## What it does
- **Two modes**: outside-in on any competitor from public evidence, or inside an ads account you can read (Google Ads, Meta): structure, keywords, search terms, bidding, budgets, assets, conversions.
- **Fixes the target** (brand, domains, pages, country) and the **business type** (ecommerce, lead gen, local, finance...) before judging anything.
- **Any market**: adapts sources and ad rules to the subject's country and sector.
- **Three depths**: quick (15 min), standard (1 h), deep (full teardown).
- **Routes by input**: an ads account, a company name, a landing URL, creatives, a creator profile, an agency name, several competitors.
- **Creative teardown**: concepts vs variations, every key video frame, hook types, credibility inventory.
- **Compare and monitor**: competitor matrix, monthly snapshots and diffs.
- **Evidence tools**: `tag-scan.js` (tags and form vendors on any page) and `gads_map.py` (read-only Google Ads account map).
- **Summary first, then drill down**: inventory of ads, pages and channels; deep dives only where a question is open.
- **Answers 12 questions**, each with the reason behind the choice: structure, budget, audience, visual creative, copy, angle and offer, credibility, funnel, tracking, organic communication, reputation, who runs it.
- **Bounded claims**: "no Google ads found for example.com, US, last 30 days", never "they don't do Google".
- **Delivers** a report with a findings ledger, a verdict and one experiment to run; at deep level also a section-by-section landing breakdown with screenshots.

## Install (Claude Code)
```bash
/plugin marketplace add danscalzo/reverse-engineering-marketing
/plugin install reverse-engineering-marketing
```
Or copy `skills/reverse-engineering-marketing/` into `~/.claude/skills/`.

Works best with a real browser tool (to read ad libraries, landing pages and profiles) and web search. Optional: a Meta Ads MCP for ad library search.

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
evals/scenarios.md         test prompts and expected behaviour
```

## Feedback
Early version (beta). If something is missing or wrong, open an issue: what you asked, what it did, what you expected.

MIT licence.
