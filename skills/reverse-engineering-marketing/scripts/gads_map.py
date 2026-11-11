"""Read-only Google Ads account map for inside-mode reverse engineering.

Runs only GAQL SELECT queries (GoogleAdsService.search). Never mutates.
Output: one markdown file to keep as evidence.

Usage:
  python3 gads_map.py --customer 1234567890 [--login-customer 1112223333]
                      [--config ~/google-ads.yaml] [--days 30] [--out map.md]
  --days: 7, 14, 30 or 90 (90 for structure and keywords, 30 for current behaviour).
"""

import argparse
import datetime as dt

QUERIES = {
    "1. Campaigns": (
        "SELECT campaign.name, campaign.status, campaign.advertising_channel_type, "
        "campaign.bidding_strategy_type, campaign_budget.amount_micros, "
        "campaign.network_settings.target_partner_search_network, "
        "campaign.network_settings.target_content_network, "
        "campaign.geo_target_type_setting.positive_geo_target_type, "
        "metrics.cost_micros, metrics.clicks, metrics.conversions, metrics.conversions_value "
        "FROM campaign WHERE campaign.status != 'REMOVED' AND segments.date {period} "
        "ORDER BY metrics.cost_micros DESC"
    ),
    "2. Keywords (top spend)": (
        "SELECT campaign.name, ad_group.name, ad_group_criterion.keyword.text, "
        "ad_group_criterion.keyword.match_type, ad_group_criterion.status, "
        "ad_group_criterion.quality_info.quality_score, metrics.cost_micros, metrics.clicks, metrics.conversions "
        "FROM keyword_view WHERE segments.date {period} "
        "ORDER BY metrics.cost_micros DESC LIMIT 100"
    ),
    "3. Search terms (top spend)": (
        "SELECT search_term_view.search_term, campaign.name, ad_group.name, "
        "metrics.cost_micros, metrics.clicks, metrics.conversions "
        "FROM search_term_view WHERE segments.date {period} "
        "ORDER BY metrics.cost_micros DESC LIMIT 150"
    ),
    "4. Negative keywords (campaign level)": (
        "SELECT campaign.name, campaign_criterion.keyword.text, campaign_criterion.keyword.match_type "
        "FROM campaign_criterion WHERE campaign_criterion.negative = TRUE "
        "AND campaign_criterion.type = 'KEYWORD' LIMIT 300"
    ),
    "5. Ads and final URLs": (
        "SELECT campaign.name, ad_group.name, ad_group_ad.ad.type, ad_group_ad.ad.final_urls, "
        "ad_group_ad.ad_strength, ad_group_ad.status, metrics.cost_micros, metrics.conversions "
        "FROM ad_group_ad WHERE ad_group_ad.status != 'REMOVED' AND segments.date {period} "
        "ORDER BY metrics.cost_micros DESC LIMIT 100"
    ),
    "6. Performance Max asset groups": (
        "SELECT campaign.name, asset_group.name, asset_group.status, asset_group.final_urls, "
        "metrics.cost_micros, metrics.conversions "
        "FROM asset_group WHERE segments.date {period}"
    ),
    "7. Locations and languages": (
        "SELECT campaign.name, campaign_criterion.type, campaign_criterion.location.geo_target_constant, "
        "campaign_criterion.proximity.radius, campaign_criterion.language.language_constant, "
        "campaign_criterion.negative FROM campaign_criterion "
        "WHERE campaign_criterion.type IN ('LOCATION','PROXIMITY','LANGUAGE')"
    ),
    "8. Conversion actions": (
        "SELECT conversion_action.name, conversion_action.status, conversion_action.category, "
        "conversion_action.type, conversion_action.primary_for_goal, conversion_action.counting_type "
        "FROM conversion_action WHERE conversion_action.status = 'ENABLED'"
    ),
    "9. Changes (last 28 days)": (
        "SELECT change_event.change_date_time, change_event.change_resource_type, "
        "change_event.resource_change_operation, campaign.name "
        "FROM change_event WHERE change_event.change_date_time >= '{since}' "
        "AND change_event.change_date_time <= '{until}' "
        "ORDER BY change_event.change_date_time DESC LIMIT 100"
    ),
}


def get_client(args):
    from google.ads.googleads.client import GoogleAdsClient
    client = GoogleAdsClient.load_from_storage(args.config)
    if args.login_customer:
        client.login_customer_id = args.login_customer.replace("-", "")
    return client


def flatten(row):
    """Turn a result row into {dotted.path: printable value}; *_micros shown in currency units."""
    from google.protobuf.json_format import MessageToDict
    raw = row._pb if hasattr(row, "_pb") else row
    out = {}

    def walk(d, prefix=""):
        for k, v in d.items():
            key = f"{prefix}{k}"
            if isinstance(v, dict):
                walk(v, key + ".")
            elif isinstance(v, list):
                out[key] = ", ".join(str(x) for x in v)
            elif k.endswith("_micros"):
                out[key] = f"{int(v) / 1e6:.2f}"
            else:
                out[key] = v

    walk(MessageToDict(raw, preserving_proto_field_name=True))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--customer", required=True)
    p.add_argument("--login-customer")
    p.add_argument("--config", default=None)
    p.add_argument("--days", type=int, default=30, choices=[7, 14, 30, 90])
    p.add_argument("--out", default=None)
    args = p.parse_args()
    cid = args.customer.replace("-", "")
    end = dt.date.today() - dt.timedelta(days=1)
    start = end - dt.timedelta(days=args.days - 1)
    period = f"BETWEEN '{start.isoformat()}' AND '{end.isoformat()}'"

    ga = get_client(args).get_service("GoogleAdsService")
    lines = [f"# Google Ads map · customer {cid} · period {period} · read {dt.date.today()}",
             "Read-only GAQL. Money in account currency. Evidence source for the findings ledger.", ""]
    for title, q in QUERIES.items():
        lines.append(f"## {title}")
        try:
            since = (dt.date.today() - dt.timedelta(days=28)).isoformat()
            until = (dt.date.today() + dt.timedelta(days=1)).isoformat()
            rows = [flatten(r) for r in ga.search(customer_id=cid, query=q.format(period=period, since=since, until=until))]
        except Exception as e:  # report the blocker, keep going with the other sections
            lines += [f"Not available: {type(e).__name__}: {str(e)[:200]}", ""]
            continue
        if not rows:
            lines += ["No rows (bounded to this query and period).", ""]
            continue
        cols = list(dict.fromkeys(k for r in rows for k in r))
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("|" + "---|" * len(cols))
        for r in rows:
            lines.append("| " + " | ".join(str(r.get(c, "")).replace("|", "/") for c in cols) + " |")
        lines.append("")
    text = "\n".join(lines)
    if args.out:
        open(args.out, "w").write(text)
        print(f"written {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
