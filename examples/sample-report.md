# Example Cycles · marketing reverse engineering (sample report)

> [!IMPORTANT]
> **This report is fictional.** "Example Cycles", its competitors, and every number, date, ad, post and review below are invented to show what the skill delivers. No real business was analysed. Any resemblance to a real company is coincidental. Domains use `example.com`, which is reserved for examples.

Target: Example Cycles (fictional e-bike retailer), example.com, Instagram and TikTok @examplecycles
Market: United States, English, e-bikes, not regulated · Business type: ecommerce with a showroom · Mode: outside-in · Depth: standard
Sources used (all read 2026-11-09): Meta Ad Library (US, all ads, last 90 days), Google Ads Transparency Center (domain, US, last 30 days), site and product pages, tag scan on 3 pages, Instagram and TikTok profiles, Google and Trustpilot reviews, company register.
Not accessible: ads accounts, analytics, order data.

## In one paragraph
Example Cycles sells e-bikes at $1,400 to $3,200 and makes the price feel small: every ad opens with "from $39 a month". Meta creates the demand, Google catches people who search the brand afterwards, and the site offers two doors: pay in instalments now, or book a free test ride. The idea that makes it work is removing the "too expensive" fear before anything else is said.

## The 12 questions
| # | Question | Answer | Class | Status |
|---|---|---|---|---|
| 1 | Structure | Meta: 38 active ads from one page. Google: Shopping and Search ads present. Campaign structure not visible from outside. [E01, E05] | OBSERVED | partial |
| 2 | Budget, bidding, results | Not public for commercial ads. [E08] | UNKNOWN | open |
| 3 | Audience | US only; age and placements not shown outside the EU and UK. | UNKNOWN | open |
| 4 | Creative | 5 concepts behind 38 ads; 33 are the same rider video with a new first line. Real riders, real streets, no studio. [E02] | DERIVED | answered |
| 5 | Copy | Template: monthly price, one benefit, "book a free test ride". The first line is what changes. Site copy: see below. [E03, E11] | OBSERVED | answered |
| 6 | Angle and offer | They sell "a commute without the car", paid monthly. Fear removed: price. Aimed at city commuters aged about 30 to 50; the buyer is the same person. [E03, E10] | INFERRED | answered |
| 7 | Credibility | 4.6 on 900+ Google reviews, owner replies to negative ones, showroom address and photos. No named press or awards. [E09] | OBSERVED | answered |
| 8 | Funnel | Ad -> product page -> either checkout with instalments or test-ride form (hosted by a booking vendor) -> confirmation by email. Chat button says "typically replies in minutes". [E06, E07] | OBSERVED | answered |
| 9 | Tracking | Meta Pixel, GA4, Google Ads tag, instalment widget. Server-side events not visible. [E06] | OBSERVED | partial |
| 10 | Organic | Instagram 21,400 followers, about 3 posts a week. Polished product posts, no prices, no links. [E10] | OBSERVED | answered |
| 11 | Reputation | Recurring complaint: delivery delays. Recurring praise: the test ride. [E09] | OBSERVED | answered |
| 12 | Who runs it | No agency credit on the site or in the libraries. | UNKNOWN | open |

## How they communicate (last 10 posts)
Instagram, read one by one on 2026-11-09. Reels: cover and 4 frames each.

| # | Date | Format | What is shown | Caption / hook | Likes / comments | Product visible? | AI-made? |
|---|---|---|---|---|---|---|---|
| 1 | Nov 8 | Reel | Rider passing a traffic jam at sunrise | "8:10, already there." | 412 / 18 | Yes, in use | No sign |
| 2 | Nov 6 | Carousel | Three colours of the same model | "Pick your morning." | 268 / 9 | Yes | No sign |
| 3 | Nov 4 | Reel | Customer unboxing in a hallway | "Day one." | 731 / 44 | Yes, in use | No, customer content |
| 4 | Nov 1 | Photo | Bike locked outside a café | "Park anywhere." | 190 / 4 | Yes | No sign |
| 5 | Oct 30 | Reel | Mechanic adjusting brakes in the showroom | "Checked before it ships." | 355 / 12 | Yes | No sign |
| 6 | Oct 28 | Carousel | Commute map: car vs bike time | "22 minutes back, every day." | 540 / 31 | Partly | Graphic |
| 7 | Oct 25 | Reel | Rider in the rain with mudguards | "Yes, in the rain too." | 602 / 37 | Yes, in use | No sign |
| 8 | Oct 23 | Photo | Showroom front with staff | "Come try one, Saturday 10 to 4." | 221 / 15 | Yes | No sign |
| 9 | Oct 21 | Reel | Sunrise ride along a river | "Start slower. Arrive faster." | 480 / 16 | Yes, in use | No sign |
| 10 | Oct 18 | Carousel | Customer review screenshots | "What riders say." | 310 / 22 | No | No |

Reading:
- **Recurring theme: the morning commute.** 6 of 10 posts are about the trip between home and work (1, 2, 4, 6, 7, 9). The theme lends the brand routine and reliability: this is a tool for every day, not a weekend toy.
- **Product, not mood.** The bike is visible in 9 of 10 posts (one only partly) and in use in 4.
- **No AI imagery.** No platform label, real customers tagged, the same showroom and staff across posts.
- **One voice.** Short, concrete lines. The same "morning" idea appears in the ads and on the site.
- **Aimed at and bought by the same person**: the city commuter. No gap.
- **Response.** Median 384 likes on 21,400 followers (about 1.8%). Customer content gets the most (post 3), plain product photos the least (post 4).
- **Organic vs paid.** Post 3 and post 7 also run as ads (same videos in the Ad Library): they promote what already worked.

## Site copy
- **Main headline**: "Your commute, from $39 a month." An outcome and a price in one line, same words as the ads.
- **Says**: how the monthly plan works, range per charge, free test ride, 30-day return, delivery time.
- **Never says on the home page**: who builds the bikes, what happens when something breaks. Service is explained only in the FAQ.
- **Product descriptions**: median 85 words. Most frequent words: "range" (41), "commute" (37), "monthly" (29), "hills" (22). Specs in a table, visible without clicking.
- **Tone**: second person, numbers before adjectives. Each product page answers three objections in the text: rain, theft, battery life.
- **Voice consistency**: ad "from $39 a month", site "from $39 a month", profile bio "the commute, sorted". One message.

## Competitors (top level)
All fictional.

| Who | What they sell | How they communicate | Active Meta ads (US, 2026-11-09) |
|---|---|---|---|
| Acme Wheels | Cheaper e-bikes, online only | Discount first: "Save $400 this week" | 61 |
| Demo Rides | Premium e-bikes, 12 stores | Lifestyle films, no price in ads | 14 |
| Sample Motion | Subscription e-bikes | "Cancel anytime", monthly rental | 9 |

What they do that Example Cycles does not: Acme Wheels runs constant discounts; Sample Motion lets people rent instead of buy. What only Example Cycles does: the free test ride as a second door.
Counts come from page-level searches with identical filters. Deeper comparison on request.

## Why it is built this way
- **Few concepts, many variations**: they test hooks, not ideas (E02). Cheap to produce, but near-identical ads may be grouped by the platform and shown to the same people (hypothesis).
- **Monthly price in every hook**: removes "too expensive" first; the instalment widget on the page backs it up (E03, E06).
- **Two doors**: buy now, or book a test ride. The second catches people who are not ready to pay online (E07).
- **Organic shows real use**: the profile is where a doubtful buyer checks whether real people ride these bikes.

## Best and worst
- Longest running ad: rider video with "from $39 a month", 74 days (E01). Probably a winner: hypothesis, there is no spend data (E04).
- Shortest lived: two studio product shots, stopped after 6 days.
- Results per ad: UNKNOWN.

## Verdict
- **Works on**: a clear offer, one message everywhere, real proof. **Not known**: spend, cost per sale, test ride to purchase rate. Whether it makes money stays open.
- **Copy**: price reframed as a monthly cost; a second, lower-commitment door; promoting the organic posts that already worked.
- **Improve**: more concepts, not more first lines; say on the home page what happens when the bike needs service.
- **Do not copy**: their wording or videos. Reuse the logic, not the creative.
- **Experiment to run** (for your own business): one new concept with a monthly-price hook against your current best ad, same budget, two weeks, judged on cost per qualified lead.

## Findings ledger
| ID | Claim | Class | Evidence | Confidence | Search boundary | Unknowns |
|---|---|---|---|---|---|---|
| E01 | 38 active Meta ads, oldest running 74 days | OBSERVED | Ad Library screenshot | High | US, active, one page name, 2026-11-09 | Other page names |
| E02 | 5 concepts, 33 variations | DERIVED | Frames of all 38 ads | High | Active ads only | Stopped ads |
| E03 | Main hook is the monthly price | OBSERVED | E01 + frames | High | Same | |
| E04 | Longest-running ads probably convert | INFERRED | Run length in E01 | Low | No spend data | Results |
| E05 | Google Shopping and Search ads present | OBSERVED | Transparency Center screenshot | High | US, last 30 days | Keywords, spend |
| E06 | Meta Pixel, GA4, Google Ads tag, instalment widget | OBSERVED | tag-scan output | High | 3 pages, one load, consent accepted | Server-side events |
| E07 | Test-ride form hosted by a booking vendor | OBSERVED | iframe host in E06 | High | Product pages only | Follow-up speed |
| E08 | Spend | UNKNOWN | Not public | | | Needs account access |
| E09 | 4.6 on 900+ Google reviews; delivery delays recur | OBSERVED | Review page screenshots | High | Google and Trustpilot, 2026-11-09 | |
| E10 | Last 10 posts: commute theme, product visible in 9 | OBSERVED / INFERRED (reading) | 10 post screenshots | High | Instagram only | TikTok posts |
| E11 | Home headline matches the ad hook | OBSERVED | Home screenshot, desktop and mobile | High | Home page | |
| E12 | Competitor active ad counts | OBSERVED | Ad Library, same filters | Medium | US, active, page level | Spend |

## Open questions
- What do they spend and what does a sale cost? Needs account access.
- How many test rides become purchases? Needs their data or an interview.
- Who runs the ads? No public signal found.
