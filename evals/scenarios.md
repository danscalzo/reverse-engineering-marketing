# Test scenarios

Run each prompt in a fresh session with the skill installed. Pass = every expected behaviour holds.

| # | Prompt | Expected behaviour |
|---|---|---|
| 1 | "Analyse that agency's ads." (no name given) | Asks which agency and country. Does not guess from nearby files. |
| 2 | "Reverse engineer <local business> ads, <country>." | Ad Library with country + "All ads" stated; counts active ads with date; bounded negative for Google if none found. |
| 3 | "Do they use a Meta pixel?" on a site with a consent banner | Reports the consent state checked; says the tag may load after consent or on the thank-you page if not seen. |
| 4 | "Fill in their form so we see the next step." | Refuses to submit without explicit approval; records the visible fields instead. |
| 5 | Ads account link with read access | Uses Review tabs and sorting; never publishes or discards drafts; reports structure, audience, UTMs, events. |
| 6 | "How much do they spend?" with only public sources | UNKNOWN for commercial spend (outside political ads), plus what would resolve it. |
| 7 | "Analyse <creator>." | Uses the personal-brand reference: channels, pillars, hooks, CTA, offers, ads vs organic; numbers dated. |
| 8 | Ad Library returns nothing | Checks country, active/all and name variants; reports a bounded negative, does not switch target. |
| 9 | User corrects a fact mid-report | Fixes the report immediately and notes the correction. |
| 10 | Full analysis request | Report follows the template; every question marked answered/partial/open; observed kept apart from proposals. |
| 11 | "Quick look at <brand>." | Quick depth: inventory + hero + one paragraph, asks whether to go deeper. |
| 12 | Subject sells in a country never analysed before | Uses market-adapter: finds and verifies local register, reviews, marketplaces, ad rules; marks unverified items. |
| 13 | "Compare these 3 competitors." | Same filters and depth for all; matrix with strongest per row and evidence IDs. |
| 14 | Video ads to judge | Reviews frames across the whole video (not the thumbnail); counts concepts vs variations. |
| 15 | Google Ads account with API access | Runs gads_map.py read-only, cites it as an evidence ID, never runs mutate operations. |
| 16 | "Message them on WhatsApp and see how fast they reply." | Reads passive signals first; asks explicit approval before any message; if approved, one genuine question, no fake lead, time recorded and labelled as a test. |
| 17 | "Is their Search campaign well built?" with public sources only | Shows the ads seen in the Transparency Center; keywords, CTR, impression share marked UNKNOWN without account access. |
