# Meta ads account, inside mode (read-only)

Any Meta account you can read: your own, a client's, or one you see as a partner. Read, never touch. If it is reachable through a Meta Ads MCP, prefer the MCP for numbers and use the UI only for settings it does not expose.

## Rules
- Never click Publish, "Discard draft", on/off toggles, budget edits. Open only the Review tabs. Leave with Close.
- URL filters and columns change only your view, not the account.
- If the account is also reachable through the Meta MCP (e.g. an account-listing tool), use the MCP: faster and no clicks.

## Useful URLs (replace act and business_id)
- Campaigns over a long period: `.../adsmanager/manage/campaigns?act=<ID>&business_id=<BM>&date=2024-01-01_<today>`
- Columns: `&columns=name,delivery,objective,results,cost_per_result,budget,spend,impressions,actions:link_click,ctr,cpm,adset_name`
- Sorting: `&sort=spend~0` (spend desc), `cost_per_result~0` (most expensive), `results~0`. The way to see best and worst without scrolling.
- Breakdowns: `&impression_breakdown=age,gender` or `device_platform,platform_position,publisher_platform`.
- The table is virtualised: the mouse wheel often does not scroll; drag the vertical scrollbar on the right, or sort.

## Reading the settings
- Ad set: hover the name -> Edit -> **Review** tab: locations and radius, age, gender, placements, objective, event, attribution, bid strategy, special ad category. No custom audience listed = none.
- Ad: same path. Shows page, Instagram, website URL (empty = uses an existing post), **URL parameters/UTM**, pixel, post type, full copy, comments.
- Special ad categories (housing, employment, credit and financial products, social issues): no lookalikes or fine exclusions, minimum radius, so the audience is broad by necessity.

## Events Manager
`business.facebook.com/events_manager2/list/dataset/<pixel>/overview?business_id=<BM>&act=<ID>`
- Events received and how many (e.g. PageView, Lead), integrations (Pixel, Conversions API), event match quality.
- If only Lead comes back and no qualified leads or sales: Meta optimises for form-fillers, not buyers.
- "Core setup" = restrictions for sensitive categories (no custom parameters).

## Who manages it
Business Settings -> Ad accounts -> Partners: shows the agency with access.

## Through a Meta Ads MCP (preferred for numbers)
1. `ads_get_ad_accounts`: confirm the account is queryable.
2. `ads_get_field_context` on the fields you plan to use (names differ between tools; never guess).
3. `ads_get_ad_entities`, level `campaign`, then `adset`, then `ad`, with `date_preset` stated (e.g. `last_90d`) and fields such as: name, effective_status, objective, start_time, daily_budget, amount_spent, results, cost_per_result, impressions, reach, frequency, link_click, ctr, cpm, lead.
4. Sort by spend to find where the money goes; filter `amount_spent > 0` to skip dead entities.
5. Daily series (`time_increment: "1"`, level account) to find launches, pauses and restarts.
6. Settings the MCP does not expose (UTM parameters, post type, special category details): Review tab in the UI.
Save each output as an evidence artifact with its ID.
