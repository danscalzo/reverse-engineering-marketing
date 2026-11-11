# Public sources (verified 2026-10-29)

Labels: [V] read on the official page on 2026-10-29; [3P] third-party sources only; [NV] not verified; [STD] standard practice.
Read only the section you need. Country details below are UK/EU examples; for any other market use `market-adapter.md` first.

## 1. Ad libraries
| Source | URL | What it shows | Limits | How |
|---|---|---|---|---|
| Meta Ad Library | facebook.com/ads/library | Worldwide: ACTIVE ads with creative, copy, lead-form details. Ads delivered in UK/EU: run dates, targeting (age, gender, locations incl./excl.), total reach and reach by location/age/gender, archived 1 year after last impression. EU only: advertiser and PAYER. [V] | No spend for commercial ads (political only). Outside UK/EU stopped ads disappear. [V] | The subject's country, "All ads", exact page; open "See ad details" for reach and targeting. Alternative: an Ad Library tool in a Meta Ads MCP, if connected: find the page ID first and filter by it (keyword search mixes in other advertisers); results may come newest first and counts are estimates, so page through or use the website for the oldest start date. |
| Meta Ad Library API | facebook.com/ads/library/api | Fields: dates, copy, platforms, age, gender, locations, reach by country/age/gender, `beneficiary_payers` (EU). Commercial UK/EU last year. [V] | Requires identity verification + developer app. [V] | `search_page_ids` + `ad_reached_countries=['<country code>']`, `ad_active_status=ALL`. |
| Google Ads Transparency Center | adstransparency.google.com | Search, YouTube, Shopping, Maps, Play ads from verified advertisers, 1 year; impression ranges with a 90-day delay. [V] | Landing pages can NO LONGER be opened (ads render as screenshots). Shows the advertiser, not the agency (payer if different). New ads after 48-72 h. [V] | Search by domain AND advertiser name, the subject's region, format, dates. Read the landing domain from the copy. |
| TikTok Commercial Content Library | library.tiktok.com | EU + CH + UK: advertiser, **"paid for by"** (e.g. agency), first/last shown, users reached, targeting. [V] | Free, no account. | Read "paid for by" to find the agency. |
| TikTok Creative Center | ads.tiktok.com/business/creativecenter | Top ads by industry/country. [3P] | Not per advertiser. | Creative style of a niche. |
| LinkedIn Ad Library | linkedin.com/ad-library | Since 2023-06-01: preview, format, advertiser, **payer**; EU also impressions and targeting. [V] | | Search by payer = agency. |
| Microsoft Ads Library | ads.microsoft.com | EU/EEA only. [3P] | | EU competitors only. |
| Pinterest / X / Snap | ad repositories | EU only (Pinterest without UK). [V] | Weak. | Low priority. |
Change: Meta ended political/social-issue ads in the EU from 2025-10-06 [3P].

## 2. Website and tracking
| Source | What | How |
|---|---|---|
| Source / DevTools [STD] | Meta pixel (`fbq`, `fbevents.js`, `facebook.com/tr?id=`), GTM (`GTM-`), GA4 (`G-`), Google Ads (`AW-`), TikTok (`ttq`). GTM from a first-party subdomain = likely server-side. | JS: `typeof fbq`, `typeof ttq`, `Object.keys(window.google_tag_manager||{})`, `dataLayer`. Iframe host = form vendor. Check BEFORE and AFTER cookie consent (choose "essential only" for the first reading and say so). |
| Wappalyzer | Stack (CMS, chat, CRM) | 50 lookups/month free. [V] |
| BuiltWith | Technologies and history | Free limits [NV]. |
| Wayback Machine | Past versions of offers and prices | `web.archive.org/web/*/domain/*`; list: `web.archive.org/cdx/search/cdx?url=domain/*` |
| robots.txt / sitemap.xml | Hidden funnel pages (/thank-you, /lp-) | [STD] |
| Google operators | Landing variants | `site:domain inurl:lp`, `"powered by" site:domain` |

## 3. Traffic and SEO (free, honest)
- Similarweb public page: estimated visits, channels, technologies, about 3 months. It is a model: write "estimate (Similarweb)". Small local sites often have no data [NV].
- Semrush free: 10 reports per day [V]. Ahrefs free tools: top 20 backlinks [V]. Google Trends and Keyword Planner for branded demand and seasonality.

## 4. Socials and content
- Public IG/FB/TikTok/LinkedIn/YouTube profiles: followers, cadence, visible likes/views, pinned offers, link in bio. Manual reading (Meta bans automated collection without written permission [V]). Method: `organic.md`.
- YouTube Data API: 10,000 units/day, search 100 units [V]. Social Blade: growth history [3P].
- Active "Paid partnership" content is in the Meta Ad Library [V].

## 5. Reputation
- Google Business Profile: rating, count, reviews, owner replies. Manual reading (paid API [V]).
- Trustpilot: rating, trend, invited vs organic reviews. Automated collection banned, including by AI agents [V]: manual reading only.
- Sector marketplaces often carry their own ratings (cars, trades, hotels, restaurants): find the ones for the subject's sector and country with `market-adapter.md` [NV].

## 6. Company facts
- Companies House (UK): officers, owners, accounts (often abridged). Free.
- Other countries: find the official register with `market-adapter.md` [NV].
- LinkedIn company page: headcount, growth, marketing hires. Job ads: tools used (e.g. HubSpot, Salesforce), in-house vs agency.

## 7. Who runs their ads (legitimate signals)
1. Payer fields: Meta (EU only), TikTok "paid for by", LinkedIn payer, Google payer if different.
2. Site footer and credits, HTML comments, author meta, form vendor.
3. Agency side: case studies, client logos, awards. Public pricing on the agency site.
4. Directories: Google Partners (partnersdirectory.withgoogle.com) [3P]; Meta Find a Partner [NV URL].
5. LinkedIn: people "Paid Social at agency X" mentioning the client.
6. Same GTM container or pixel across several sites = likely same operator (INFERRED, not proof).
7. If you have account access: Business Settings -> Partners.

### Judging the agency (not just naming it)
- **From outside**: number of clients (case studies, logos, LinkedIn), how concentrated they are in one sector (many clients in one niche = specialist with a repeatable playbook, INFERRED), how the offer is structured (packages, public prices, bundled tools), team size and roles.
- **What makes it good** (results, how accounts are built) is visible only with account access: from outside it stays UNKNOWN. Say so instead of guessing.

## 8. Legal limits
- Meta Automated Data Collection Terms (since 2024-10-07): no scraping without written permission [V]. Use the UI or the official API.
- Trustpilot bans automated collection [V].
- GDPR / UK GDPR: public personal data is still personal; no lists of people. Analyse the company.
- Never: other people's logins, fake profiles, CAPTCHA, fake leads, word-for-word copying.

## 30-minute minimum sweep
1. (3') Meta Ad Library: subject's country, all, exact page. Count active ads, oldest date, formats; open 3 ads for reach and targeting.
2. (3') Google Transparency: domain, subject's region, 30 days, formats; landing domains.
3. (2') TikTok and LinkedIn: advertiser + payer.
4. (4') Landing desktop + mobile: offer, proof, form vendor, thank-you page.
5. (3') Tags: pixel, GA4, AW-, GTM, TikTok; before and after consent.
6. (3') robots, sitemap, `site:`, Wayback for offer/price history.
7. (3') Similarweb, Ahrefs free, Google Trends for branded demand.
8. (3') Organic socials: cadence, top posts, link in bio, Social Blade.
9. (3') Reviews: Google, Trustpilot, sector platforms; rating, count, recency, replies.
10. (3') Company register (`market-adapter.md`), LinkedIn, job ads, agency signals. Every number with source and period.
