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

**Reconstruction of one key choice: the monthly-price hook**
| Rival hypothesis | Evidence that separates them | Status |
|---|---|---|
| H1 it is their engine: it sells | new variations keep it; ads without it stop first | leading, INFERRED (E02, E03) |
| H2 it is the finance partner's template | same wording on the partner's other retailers | open: check the partner's Ad Library |
| H3 forced by margin: full price would not convert | full price hidden on the product page too | weak: full price is shown (E06) |
Why they chose it (H1 vs H2) is still open; why it works (removes the price fear, backed by the Klarna widget) is supported.
Check today: H2 is settled by the partner's Ad Library, no prediction needed. Prediction for what is left: "H1: by 2026-12-09 the new concepts (not just variations) also open on the monthly price, and the 2 active ads without it disappear before the others. If it were only habit or a default, new concepts would open with other hooks and nothing would stop in a pattern." Checked at the next snapshot, same filters (in the US stopped ads are not shown, so 'stopped' = present on 11-09, gone on 12-09).

**Blueprint (short)**: Meta video hook on monthly price -> product page with instalment widget -> buy now, or book a test ride through a booking vendor -> (follow-up UNKNOWN) -> sale. The one idea: make a big ticket feel like a subscription. Weakest link if copied: it needs a finance partner and stock to deliver fast (delivery delays are already the top complaint).

**Mistakes made and corrected**
- Said "no YouTube ads" after the Transparency Center's default last-30-days view; widening the date range showed a paused video campaign. Lesson: state the period and the filter.
- Read "no pixel" from a browser extension before accepting cookies; after consent the pixel loaded. Lesson: record the consent state; interface hints are not evidence.

**Still unknown**: spend, cost per sale, test-ride to purchase rate. So "does it make money?" stays open (E08).

**Experiment to copy** (for the user's own business): one new concept with the monthly-price hook against the current best ad, same budget, two weeks, judged on cost per qualified lead.
