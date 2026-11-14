# Google Ads account, inside mode (read-only)

Goal: a map of how the account is built and why, deep enough to rebuild it elsewhere. Read-only: no changes, no budget or keyword edits, even on your own account (changes are a separate decision).

## Step 0: can the conversions be trusted? (before any judgement)
Read the conversion actions FIRST (map point 9), then everything else. A verdict built on bad conversions is worse than no verdict.
- **Trusted**: the primary conversion is a real money event (purchase with value, qualified lead, booked call, offline sale imported) and it fires once per event.
- **Proxy**: the primary conversion is a click, page view, time on site, or a button with no submit behind it.
- **Broken or unclear**: no primary conversion, duplicates (same event from tag and GA4 import both primary), conversions that stop on a date, values all equal to 1.
If Proxy or Broken: say so at the top, list what must be fixed, and STOP the keep / cut / test table. Structure, search terms and settings can still be described; winners and losers cannot be named.

## How to read it (cheapest sufficient first)
1. **API** (GAQL, `search` / `searchStream`), if available: fastest and exact. Queries below.
2. **UI**: Campaigns, Keywords, Search terms, Assets, Change history, Conversions; Google Ads Editor export if offered.
3. Period: last 90 days for structure and keywords, last 30 for current behaviour; always state it.

## Map, in this order (summary first)
1. **Inventory**: campaigns by type (Search, Performance Max, Shopping, Display, Video, Demand Gen), status, budget, bid strategy, target (tCPA/tROAS), start date, spend and conversions in period.
2. **Naming logic**: what each part of the names encodes, and how labels are used.
3. **Search campaigns**: ad groups and their theme; keywords with match type, status, quality score, spend, conversions; negative keywords and shared lists; **search terms** that actually spend (the truth behind the keywords); broad + phrase duplicates and cannibalisation.
4. **Ads and assets**: RSA headlines/descriptions and pinning, ad strength, sitelinks, callouts, call, location, image and logo assets, business name; what repeats, what varies.
5. **Performance Max**: asset groups and their themes, audience signals, search themes, brand exclusions, listing groups / feed, final URL expansion on or off.
6. **Shopping / ecommerce**: Merchant Center link, feed quality (titles, prices, availability), product groups, tROAS, conversion values.
7. **Targeting and settings**: locations (presence vs interest), languages, ad schedule, devices and bid adjustments, network (Search partners, Display on Search campaigns), audiences in observation or targeting.
8. **Landing pages**: final URLs per ad group / asset group, tracking template, final URL suffix, UTMs or auto-tagging; then open the top pages (`landing-site-tracking.md`).
9. **Conversions**: conversion actions, primary vs secondary, source (tag, GA4 import, calls, offline import), counting, values, attribution model, enhanced conversions, consent mode. What the bidding is really optimising for.
10. **History**: change history for the last 30-90 days (what was touched and when), experiments.

## Read-only GAQL starters
```sql
-- campaigns
SELECT campaign.name, campaign.advertising_channel_type, campaign.status, campaign.bidding_strategy_type,
       campaign_budget.amount_micros, metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM campaign WHERE segments.date DURING LAST_30_DAYS
-- keywords
SELECT ad_group.name, ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type,
       ad_group_criterion.quality_info.quality_score, metrics.cost_micros, metrics.conversions
FROM keyword_view WHERE segments.date BETWEEN '<start>' AND '<end>'  -- 90 days: GAQL has no LAST_90_DAYS literal
-- search terms
SELECT search_term_view.search_term, campaign.name, metrics.cost_micros, metrics.conversions
FROM search_term_view WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC LIMIT 200
-- conversions
SELECT conversion_action.name, conversion_action.category, conversion_action.primary_for_goal,
       conversion_action.type, conversion_action.counting_type FROM conversion_action
```
Add `asset_group`, `asset_group_asset`, `campaign_criterion` (location, language, schedule), `change_event` as needed.

## Reading it (the why)
- Why this campaign type mix for this business type (`business-type.md`)?
- Is bidding optimising for something that means money (real conversion, value) or a proxy (page view, click)?
- Do the search terms match the intent the structure assumes?
- Is spend concentrated (top 10% keywords / asset groups) and is that deliberate?
- Where would the same structure break in another account (budget too thin for the number of campaigns, conversions too few for smart bidding)?

## Keep / cut / test (inside mode only, after Step 0 passes)
The step from "how it is built" to "what to do". Proposal only: nothing is changed in the account.
- **Source**: `search_term_view` first (what people really typed), then `keyword_view`. Period 90 days, stated. Check change history and seasonality: a campaign restructured three weeks ago does not have 90 comparable days.
- **Minimum data** (working default, a rule of thumb, not a statistic: say so and adjust to the account): a row is judged only with at least 30 clicks, or spend of at least 2x the account's average cost per conversion. Below that: "too little data, do not decide".
- **Target**: the account's own tCPA / tROAS if set; otherwise the account average cost per conversion (or ROAS) in the period. State which.

| Verdict | Rule | Example line |
|---|---|---|
| **Keep** | Above minimum data, conversions with cost per result at or better than target | "<term>: 14 purchases, cost per purchase 30% under average. Keep; check impression share lost to budget before adding money." |
| **Cut** | Above minimum data, spend with zero conversions, or cost per result far worse than target, and the term is not the brand | "<term>: spend = 3x average cost per purchase, 0 purchases. Negative keyword candidate." |
| **Test** | Below minimum data but with a signal (1-2 conversions, high intent wording) or a converting search term not yet a keyword | "<term>: 2 purchases on 11 clicks. Add as exact keyword and re-read in 30 days." |

- Report the top 10 rows per verdict, each with clicks, cost, conversions, value, period. Brand terms in a separate block (they convert because of the brand, not the keyword).
- Read the **Keep** list as market research too: the words buyers use are the words for ads, landing headline and organic content.
- Everything is DERIVED from OBSERVED numbers; the recommendation is a proposal. Budgets, bids and keywords are changed only by the account owner.

## Search: fast signs of good vs poor build
| Good | Poor |
|---|---|
| Keywords with buying intent ("price", "near me", "book", product + town) | Broad match with no negatives and no strong conversion signal: attracts the wrong people |
| Negative keyword lists, updated from search terms | Search terms full of irrelevant or informational queries |
| CTR healthy for the sector, impressions and clicks growing | Low CTR, few impressions: ads not relevant or bids too low |
| Good visibility: impression share and top-of-page rate on the core terms | Low impression share lost to rank (quality) or budget |
| A clear strategy: theme per ad group, ad copy that repeats the keyword | No visible logic: everything in one ad group, generic ads |
Outside-in you only see the ads (Transparency Center), not keywords or numbers: the table above needs inside mode; from outside, mark it UNKNOWN.

## Evidence rules apply
OBSERVED for settings and numbers read (with period), DERIVED for computed ratios, INFERRED for intentions, UNKNOWN for offline outcomes (sales, margin) unless imported.
