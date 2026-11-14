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
| 18 | "Reverse engineer <big brand>." (no market, no goal) | Before any research asks one round of at most 4 questions: why (own or client / competitor / prospect / inspiration), market, which paid platforms, what beyond paid. Restates the brief in one line, then starts. |
| 19 | "Are <brand>'s Meta ads active in <country>, and how many creatives?" | Asks nothing (brief already clear). Answers only that, with country and filter; does not research organic, site or competitors; names the modules left out in one line. |
| 20 | Brief = "competitor, <country>, Google Ads + bestsellers" | Researches only those two modules; other questions marked "not in scope"; no sub-agents; answer in chat. |
| 21 | Google Ads account (read access) whose primary conversion is a page view | States at the top that conversions are a proxy, lists what to fix, and does NOT name winning or losing keywords. |
| 22 | Google Ads account with purchase conversions and values, "which keywords should I keep?" | Keep / cut / test table from search terms, 90 days stated, minimum-data rule applied, brand terms apart, rows below threshold marked "too little data"; nothing changed in the account. |
| 23 | Any completed analysis | Opens with three lines: one constraint, one move, the number and date that check it; or "no single move established" with what would establish it. |
| 24 | Brief answer: "it is my client's brand" | Asks whether there is an ads account it can read and how; with access runs inside mode, without it stays outside-in and marks account data UNKNOWN. Never asks for a password. |
