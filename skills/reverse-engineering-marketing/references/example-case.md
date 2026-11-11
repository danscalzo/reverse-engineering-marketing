# Worked example (fictional): an e-bike retailer

**This case is invented** to show the method. "Example Cycles" and every number below are made up; any resemblance to a real business is coincidental. Domain: example.com (reserved for examples).

**Input**: outside-in only. "Reverse engineer Example Cycles, US. Standard depth."

**Path**: Meta Ad Library (US, all ads, last 90 days) -> Google Ads Transparency Center (domain + advertiser name) -> landing pages from the ads, desktop and mobile -> `tag-scan.js` on home, product and checkout-start pages -> Instagram and TikTok profiles -> Google and Trustpilot reviews -> company register and the site footer.

**Ledger extract**

| ID | Claim | Class | Evidence | Search boundary |
|---|---|---|---|---|
| E01 | 38 active Meta ads, oldest running 74 days | OBSERVED | Ad Library screenshot, US, active, 2026-11-09 | One page name; other names not found |
| E02 | 5 concepts, 33 variations (same video, new first line) | DERIVED | Frames of all 38 ads | Active ads only |
| E03 | Main hook: monthly price ("from $39 a month") | OBSERVED | E01 + frames | Same |
| E04 | Ads that run longest probably convert | INFERRED | Run length in E01 | No spend data: hypothesis only |
| E05 | Google Shopping + Search ads present | OBSERVED | Transparency Center, US, 2026-11-09 | Last 30 days |
| E06 | Meta Pixel, GA4, Google Ads tag, Klarna widget | OBSERVED | tag-scan output, consent accepted | 3 pages, one load |
| E07 | Test-ride booking form hosted by a booking vendor | OBSERVED | iframe host in E06 | Product pages only |
| E08 | Spend | UNKNOWN | Not public for commercial ads | Needs account access |

**What was rebuilt (and why)**
- Few concepts, many variations: they test hooks, not ideas (E02). Why: cheap to produce, but the platform may group near-identical ads and show them to the same people.
- Price per month, not full price, in every hook (E03). Why: removes the "too expensive" fear; the Klarna widget on the page backs it up (E06).
- Two doors: buy now with instalments, or book a free test ride (E07). The second catches people who are not ready to pay online.
- Organic is a showroom, not a funnel: polished product posts, no prices, no links. Ads do the selling, the profile builds trust.
- Reviews: 4.6 on 900+, owners reply to negative ones within days; delivery delays are the recurring complaint.

**Mistakes made and corrected**
- Said "no TikTok ads" after checking only active ads; the "all ads" view showed a paused campaign. Lesson: state active vs all, and the period.
- Read "no pixel" from a browser extension before accepting cookies; after consent the pixel loaded. Lesson: record the consent state; interface hints are not evidence.

**Still unknown**: spend, cost per sale, test-ride to purchase rate. So "does it make money?" stays open (E08).

**Experiment to copy** (for the user's own business): one new concept with the monthly-price hook against the current best ad, same budget, two weeks, judged on cost per qualified lead.
