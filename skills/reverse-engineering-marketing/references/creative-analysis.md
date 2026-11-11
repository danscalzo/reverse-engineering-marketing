# Creative and credibility analysis

Goal: understand why the creative works, not just describe it. Same evidence rules: every creative gets an evidence ID (Ad Library ID, ad ID, post URL, frame file).

## 1. Inventory and concept count
- List every active creative (cap at ~50: sample by most recent and longest running).
- Group them into **concepts**: same idea, angle and visual approach = one concept, even if colours, text or the product change. Ten edits of one idea are one concept.
- Report: number of creatives, number of distinct concepts, concepts per format. Few concepts behind many ads = low creative diversity; on Meta's current delivery system similar creatives tend to be grouped and compete as one (INFERRED from platform guidance, not visible from outside).
- Longest-running ads (start date in the library) are the best public proxy for winners. Proxy, not proof.

## 2. Video: look across the whole video
- Never judge a video from its thumbnail or first second.
- Preferred, no download: open the ad or post in the browser, pause and screenshot at 0s, 1s, 3s, then every ~3-5s and the last frame.
- If the user provides the file or approves a download from an official source: `ffmpeg -i video.mp4 -vf fps=1 frames/f_%03d.jpg` (or `fps=1/3` for long videos), then review every frame.
- Record per video: hook (first 3s: what is seen and said), on-screen text, who appears (owner, staff, customer, actor, nobody), setting (real place or stock), proof shown, offer moment, CTA, length, captions yes/no, sound-off readability.

## 3. Static and carousel
- Real photos vs graphics vs AI; product alone vs in use; faces; text density; brand marks; consistency with landing and profile.
- Carousels: what card 1 does (hook) vs the last card (CTA); real sequence or just a gallery.

## 4. Hooks
Classify the first line or first 3 seconds of each concept:
| Type | Example shape |
|---|---|
| Offer / price | "From 29 a month, cancel anytime" |
| New arrival / scarcity | "Just arrived", "only one" |
| Avatar call-out | "For busy parents who hate meal prep" |
| Problem / pain | "Still waking up with back pain?" |
| Proof / result | "12,000 orders shipped this year" |
| Curiosity / contrarian | "Don't book a gym until..." |
| Story / testimonial | "Sarah tried everything before..." |
Count hooks by type: the mix shows what the advertiser believes works.

## 5. Credibility inventory (question 7, in depth)
For each proof element: what it is, where it appears (ad, landing, profile), and whether it is checkable.
- Third-party: review rating and count with source, accreditations, regulator numbers, awards, press, partner badges.
- Physical: real premises, staff, address, opening hours, photos of real stock or work.
- Social: comments under ads, customer content, before/after, case studies with names (only if public and published by the business).
- Numbers: precise and sourced vs vague ("100s of happy customers").
- Risk reversal: guarantees, no obligation, free check, returns.
Mark gaps: proof claimed but not shown, ratings without source, vague numbers.

## 5b. Winners with account access (inside mode)
- A winner has a **high CTR AND produces the money event** (purchases, qualified leads). High CTR alone is attention, not sales.
- Benchmarks change by sector and country: compare each creative with the account's own median and history, not with a fixed number from elsewhere. State the period.
- Variations of a winner are the next step: keep what was learned (hook, angle, proof) and change one element at a time.

## 6. Why it works (the reading)
Write, as INFERRED: which fear each creative removes, which buyer it speaks to, and how it hands off to the landing page (same words, same images, same offer?).
