---
name: reverse-engineering-marketing
description: Reverse engineer how a company, agency or personal brand does its marketing, from evidence you can legitimately access, in any country - ad libraries (Meta, Google, TikTok, LinkedIn), landing pages, website tracking, creatives and video frames, organic socials, reviews, company registers, and ads accounts you can read. Two modes - outside-in (public evidence on any competitor) and inside (a Google Ads or Meta account you can read: structure, keywords, search terms, bidding, budgets, assets, landing pages, conversions). Rebuilds what they do and why, keeps observed, derived, inferred and unknown apart, compares competitors and tracks changes over time. Use when asked to "reverse engineer", "analyse their ads/strategy/funnel/account", "how is this account built", "what is this competitor doing", "compare these competitors", "break down this landing page", "study this creator's content", or when given an Ad Library page, an ads account, a profile or a landing URL. Works in any language. Skip it for routine performance reporting and SEO-only audits.
license: MIT
metadata:
  version: "1.5.0"
---

# Reverse Engineering Marketing

Answers: **how is this subject's marketing built, why is it built this way, and what can be reapplied?**
Every claim carries its evidence: source, date, filters, limits.

## Before you start
- If `references/local.md` exists, read it first (language, output folder, tools, private rules). It overrides the defaults here.
- Default output folder: `./research/`. Reply in the user's language.
- Brief before research: run section 0 first. Once the brief is clear, no further ceremony: if browser, web or ads tools are available, start.

## When not to use
- Routine KPI reports: use a reporting skill. This one explains how and why something is built.
- Pure SEO or technical site audits.
- Anything needing logins you don't hold, fake profiles or bypassing controls: refuse (Guardrails).

## 0. Brief first: ask, then research
Do not open a single source before the brief is clear. A full sweep on a subject nobody scoped wastes time and tokens and buries the two things the user wanted under ten they did not.

Ask ONE round of questions (a multiple-choice question tool if you have one, otherwise a short numbered list), at most 4, each with a recommended default. Skip any question the request already answers. Skip the whole round only when the request already gives the market AND what the user wants to know, or the user says "everything" / "full analysis".

1. **Why this subject** (sets the lens of the verdict):
   - my brand or a client's: audit, what to fix
   - a competitor: where they are strong, where they can be beaten
   - a prospect: 3 opportunities to open a conversation
   - inspiration: what to copy, as a playbook
   If the answer is "my brand or a client's", ask at once: **is there an ads account I can read** (Google Ads, Meta), and how (API, MCP, browser already signed in)? Yes = inside mode: real keywords, search terms, spend, conversions, and the keep / cut / test table. No, or a competitor / prospect / inspiration = outside-in: public evidence only, and anything that lives inside the account stays UNKNOWN. Never assume access, never ask for a login: only access the user already holds.
2. **Market**: country (town or area for a local business). Never assumed.
3. **Paid, what matters** (multi-select): Meta ads (active or not, how many creatives, since when, formats, hooks) / Google Ads (active or not, Search, Shopping, Video) / other platforms (TikTok, LinkedIn) / not interested in paid.
4. **Beyond paid, what matters** (multi-select): organic social and how they communicate / products, prices, offers, bestsellers / site, landing, copy and tracking / business numbers, reputation, competitors, who runs it.

Then restate the brief in one line ("Example Cycles, US, competitor lens: Meta ads + bestsellers, chat answer") and start.

**Scope rules**
- Research ONLY the chosen modules. The others are written "not in scope", not UNKNOWN, and are not researched "just in case".
- Depth follows the scope: 1-2 modules = Quick, answer in chat. 3+ modules or "everything" = report file. Ask about depth only if still unclear.
- Cheapest check first: for a paid module answer the yes/no question first (ads active? how many? since when?, with country and filter) and report it before drilling into creatives.
- Sub-agents only for chosen modules, one per module, and only when there are 3 or more.
- Close by naming in ONE line the modules left out, so the user can ask for them. Do not run them unasked.

## 1. Fix target, market, mode, depth
- **Target**: brand and legal name, domain(s), social pages, advertiser names. Ambiguous = ask for the name AND the country. Never guess the target from nearby files or past research; never switch target silently.
- **Market**: country, language, sector, regulated or not. Sources and rules change by market: `references/market-adapter.md`.
- **Business type** decides what "well built" means: `references/business-type.md`.
- **Mode**: outside-in (public evidence) or inside (you can read the ads account: deeper, preferred). Decided in the brief (section 0, question 1), not guessed.
- **Depth** (follows the brief's scope, section 0; ask only if still unclear):

| Depth | Time | Covers | Deliverable |
|---|---|---|---|
| Quick | ~15 min | Ad library inventory, main landing hero, offer, one-paragraph read, competitors named in one line | Chat summary + "worth going deeper?" |
| Standard | ~1 h | 12 questions at summary level, 3 best / 3 worst, tags, last 10 posts read one by one, site copy, reputation, competitors at top level | Report file |
| Deep | 2 h+ | Everything, frames of every key video, landing section by section, inside-mode map, playbook | Report + landing folder + playbook |

## 2. Route by input
| You are given | First step |
|---|---|
| Google Ads account you can read | `references/google-ads-account.md` + `scripts/gads_map.py` |
| "Is their Search well built?" without access | `references/google-ads-account.md` section "Search: fast signs": ads from the Transparency Center only, the rest UNKNOWN |
| Meta ads account you can read | `references/account-access.md` |
| Company or page name | ad libraries for that market, then site |
| Domain or landing URL | `references/landing-site-tracking.md` + `scripts/tag-scan.js` |
| Ads, videos, creatives to judge | `references/creative-analysis.md` |
| Creator / person profile | `references/personal-brand.md` |
| Company social profile | `references/organic.md` |
| Agency name | `references/sources.md` section 7 |
| Several competitors / "who is best" | `references/compare.md` |
| "Keep an eye on them" | `references/monitoring.md` |

## 3. Plan
1. Turn the brief into questions, each paired with the evidence it needs: only those of the 12 below that fall inside the chosen modules, plus the user's own.
2. Reuse prior research in the output folder. Do not redo.
3. **Summary first**: inventory (active ads and since when, formats, pages, live channels). Drill only where a question is open: 1-3 examples per cluster.
4. Corroborate with the right evidence type ("website by X" does not prove X runs the ads).
5. Split big jobs into independent parts (sub-agents with a clear scope, returning sources, conclusions, gaps).
6. Keep the ledger with evidence IDs (step 5).
7. Close every question as answered / partial / open.

## 4. The 12 questions (always with the why)
Answer the ones inside the brief's scope. Map: Meta / Google / other paid = 1-5 on that platform; organic = 10; products and offers = 6; site, copy, tracking = 5, 8, 9; business, reputation, competitors, who runs it = 7, 11, 12 and the competitor table. The rest is "not in scope".
1. **Structure**: campaign types, campaigns, ad sets / ad groups, ads, naming; for search also keywords, match types, negatives, real search terms.
2. **Budget, bidding, results**: bid strategy, targets, budgets, spend, conversions, cost per result. No access = UNKNOWN.
3. **Audience**: areas, radius, age, exclusions, special ad category, real placements.
4. **Creative**: concepts vs variations, formats, video frames, faces, style, brand consistency (`creative-analysis.md`).
5. **Copy**: template, hooks by type, CTA, what varies. Ads AND site: when the site is in scope its copy is always read and reported (`landing-site-tracking.md`, "Copy reading").
6. **Angle and offer**: what they really sell, to whom, which fear they remove. Say who the communication is aimed at and who actually buys: when the two differ, that is a finding.
7. **Credibility**: proof inventory, checkable or not (`creative-analysis.md` section 5).
8. **Funnel**: ad -> page -> form (whose?) -> where the lead lands -> follow-up. Follow-up speed decides most lead businesses: read passive signals first (WhatsApp or chat button, "typically replies within" on the page, reviews about slow replies). An active test (one genuine question by message, time to reply recorded) only with the user's explicit approval, never a fake lead.
9. **Tracking**: tags, UTMs, conversion events, what the platforms optimise for.
10. **Organic**: the credibility layer people check after an ad (`organic.md`). When organic is in scope, read the last 10 posts one by one: what they show, the recurring theme and what it is used for, whether the images are AI-made.
11. **Reputation**: rating, count, recency, owner replies, themes.
12. **Who runs it and what it costs**: agency, tools, public pricing.

### Competitors at top level
When competitors are in scope (or the brief is "everything"), name the 2-4 main competitors: who they are, what they sell, how they communicate, whether they advertise (active ads, with country and filter). One short table, a few minutes each. The user then decides whether to go deeper (`compare.md`). Out of scope: at most one line naming them from what you already saw, no extra research.

## 5. Evidence rules
- **Quick depth**: a light ledger in chat (claim, source, date, filter) is enough; no files needed.
- **Evidence IDs**: every source gets an ID in the ledger (E01, E02...) pointing to a saved artifact: screenshot, script output, library ID, URL with date. Claims cite IDs. No ID, no claim.
- **Four classes, never mixed**: OBSERVED / DERIVED (computed from observed) / INFERRED (hypothesis) / UNKNOWN (plus what would resolve it).
- **Every number**: source, date, filters. Tool estimates = "estimate (tool)". The subject's own figures = "their claim, unverified".
- **Absence is bounded**: "no Google ads found for example.com, US, last 30 days". A tag not seen may be on another page, in GTM or after consent: state the consent state.
- **End of results is not full coverage** (other pages, countries, advertiser names).
- **Correlation is not cause. Layout and names are not proof. Interface warnings are not evidence**: verify at the source.
- **Time comparisons** only with identical filters (`monitoring.md`).
- **Never invent or rebuild a citation.** If a source is lost, say so.
- **Negative results are results.**

Ledger: | ID | Claim | Class | Evidence | Confidence | Search boundary | Unknowns |

## 6. Passive vs active
- Record separately what you observed and what you did (opened a quiz, clicked a step).
- Before walking a funnel declare: page, action, expected result, stop point.
- **Never submit a real form** of another business (fake lead, real cost to them). Record the fields instead. Only with explicit user approval, labelled as a test.

## 7. When a source fails
| Blocker | Do |
|---|---|
| Login wall, CAPTCHA, rate limit | Stop that source, report it, continue with others. Never bypass. |
| Library shows nothing | Check country, active/all, name variants; report a bounded negative. |
| Page needs JS or consent | Real browser; record the consent state. |
| Script or API error | Report the section as not available; keep the others. Do not repeat the same failing call. |
| Table will not scroll | Sort or filter instead (`account-access.md`). |

## 8. Guardrails
- Public sources, official APIs, or access the user already holds. Ads accounts: read-only, never publish, never discard drafts, never change budgets or keywords.
- No logins you don't own, fake profiles, CAPTCHA bypass, scraping where terms forbid it, tokens lifted from pages, downloads without approval.
- Analyse the business, not people: no lists of reviewers, staff or commenters.
- Replicate logic, never copy text or creatives verbatim.
- Market rules and compliance are flags for the user, not legal advice.
- If the user corrects a fact, fix the report at once and add a line to the ledger: what changed and why.

## 9. Verdict and deliverables
Read `references/reading-and-verdict.md` (one move on top, business lens, best and worst, verdict, experiment card, client-ready version). The answer and the report OPEN with three lines: constraint, one move, the number and date that prove it right or wrong. Inside mode on Google Ads: conversions are checked before any judgement, then the keep / cut / test table (`references/google-ads-account.md`). Deliver with `references/report-template.md`:
1. Report `<subject>-<topic>-<YYYY-MM-DD>.md` with ledger and evidence folder.
2. Landing folder: numbered desktop + mobile screenshots, section-by-section "what + why".
3. A reusable playbook if the strategy is replicable.
4. Chat answer: the user's questions one by one, then your view; observed apart from proposals; status of each question. Answer in the order of the brief. Include how they communicate and to whom, and the competitors by name, only when those modules were chosen. Last line: the modules not covered, on offer.

Worked example: `references/example-case.md`.
