# Google Ads account, inside mode (read-only)

Goal: a map of how the account is built and why, deep enough to rebuild it elsewhere. Read-only: no changes, no budget or keyword edits, even on your own account (changes are a separate decision).

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
