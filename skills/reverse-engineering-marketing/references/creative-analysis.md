# Creative and credibility analysis

Goal: understand why the creative works, not just describe it. Same evidence rules: every creative gets an evidence ID (Ad Library ID, ad ID, post URL, frame file).

## 1. Inventory and concept count
- List every active creative (cap at ~50: sample by most recent and longest running).
- Group them into **concepts**: same idea, angle and visual approach = one concept, even if colours, text or the product change. Ten edits of one idea are one concept.
- Report: number of creatives, number of distinct concepts, concepts per format. Few concepts behind many ads = low creative diversity; on Meta's current delivery system similar creatives tend to be grouped and compete as one (INFERRED from platform guidance, not visible from outside).
- Longest-running ads (start date in the library) are the best public proxy for winners. Proxy, not proof: an evergreen ad left on with a small budget, or a brand / retargeting ad, also runs for months. Separate them with the rivals table in `reconstruction.md`.

## 2. Video: look across the whole video
- Never judge a video from its thumbnail or first second.
- Preferred, no download: open the ad or post in the browser, pause and screenshot at 0s, 1s, 3s, then every ~3-5s and the last frame.
- If the user provides the file or approves a download from an official source: `ffmpeg -i video.mp4 -vf fps=1 frames/f_%03d.jpg` (or `fps=1/3` for long videos), then review every frame.
- Record per video: hook (first 3s: what is seen and said), on-screen text, who appears (owner, staff, customer, actor, nobody), setting (real place or stock), proof shown, offer moment, CTA, length, captions yes/no, sound-off readability.

## 3. Static and carousel
- Real photos vs graphics vs AI; product alone vs in use; faces; text density; brand marks; consistency with landing and profile.
- AI check: platform label ("AI info", "AI content") = OBSERVED; otherwise INFERRED from signs (same face in unrelated scenes, nobody credited, rendered skin or hands). Applies to ads and organic posts alike.
- Theme: what the subjects have in common (sport, travel, family...) and what that theme is meant to lend the brand. Method and table: `organic.md`, "Last 10 posts".
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
- Next steps from a winner: iterations change one element at a time to learn what carries it; new concepts stack proven variables into a fresh idea (section 7d).

## 6. Why it works (the reading)
Write, as INFERRED: which fear each creative removes, which buyer it speaks to, and how it hands off to the landing page (same words, same images, same offer?). This is "why it works"; "why they chose it" is a separate question (`reconstruction.md` section 2).

## 7. From breakdown to next tests
Turns a breakdown into reusable variables and tests. Scope by depth:
- **Quick**: skip, or at most the 7a variable list in chat. No library file, no test cards.
- **Standard**: 7a, plus 1-3 tests from 7d as proposals.
- **Deep**, or when the user asks for tests, a swipe breakdown or a playbook: all of 7a-7f.
Tests are always proposals: the skill never creates, launches or budgets them (Guardrails).

### 7a. Split each creative into variables
Every creative is a stack of elements that can win or lose on their own. One row per variable, each citing an evidence ID:
| Group | Variables |
|---|---|
| Messenger | casting role only (owner, staff, customer, creator, nobody); fits the target buyer yes/no (INFERRED) |
| Setting | place, background, props, light, real or staged (INFERRED) |
| Look | clothing colours, framing, camera style (selfie, tripod, screen recording), edit pace, caption style |
| Message | hook type and idea, angle, offer, proof, CTA |
| Format | length, ratio, static / video / carousel, sound on or off |
No age, appearance or identity claims about the people on camera (Guardrails).

Status of each variable (rule of thumb, not statistical proof: state spend and sample behind each result):
- **Candidate**: seen in one ad or swipe. Anything seen from outside stays here: one external ad is one data point, and a long run date is a proxy, not proof.
- **Supported**: won one test on the user's own account against their control.
- **Winner**: won two or more tests, or held across different concepts.

### 7b. Tier (inside mode only)
S / A / B / C / D / F, DERIVED from the account's own spend and target cost per result (cite the export's evidence ID, state the period): S scales well above usual spend inside target, A profitable at usual spend, B profitable only small, C break-even, D below target, F no delivery or clearly losing. Outside-in the tier is UNKNOWN; run time is a proxy, labelled INFERRED.

### 7c. Variables library
Create or update `<brand>-variables-library.md` in the output folder only if the user asked for it or already has one; say so in one line. If none exists, ask once in the brief whether to start one.
| Variable | Value | Status | Evidence ID | Test and result | Date | Notes |
|---|---|---|---|---|---|---|
No evidence ID, no row. Losing variables stay with their result. An untested idea is never written as a winner.

### 7d. Next tests
- **New concept**: stack Supported or Winner variables from the user's own library into a fresh idea, against the current control. This is where big jumps come from. Never clone a competitor's full stack.
- **Iteration**: change one variable of a winner to learn what carries it. Good for learning, rarely beats the original by much, so not most of the test budget.
- Each test uses the experiment card (`reading-and-verdict.md`) plus: variables kept, variables changed, evidence IDs behind the choice, and the minimum spend or impressions before reading it.
- Read attention first (3-second view rate against the account's own median, never a fixed threshold from elsewhere), then the money event.
- Every test that runs closes with a written conclusion, win or lose, recorded in the library if there is one.

### 7e. Repurpose for the user's brand
Translate the chosen variables into the user's product, buyer, real customer language and differentiator. Missing inputs = list the gaps, never invent drafts. Rebuild the logic; never copy the swipe's script, visuals or people.

### 7f. Reverse mode: an ad that underperformed
Put the loser next to the control or the closest winner, list the variables that differ, rank them by likely impact (INFERRED), and turn the top one or two into proposed tests. Check both the creative variables and the landing handoff (6) before concluding; do not blame product or market first.
