# Report template

File: `<output folder>/<subject>-<topic>-<YYYY-MM-DD>.md`. Write in the user's language. Keep it short; the ledger carries the detail.

```markdown
# <Subject> · marketing reverse engineering (<date>)

Target: <brand / legal name>, <domains>, <pages>, <country>
Market: <country, language, sector, regulated?> · Business type: <...> · Mode: <outside-in / inside> · Depth: <quick / standard / deep>
Sources used: <list with dates and filters>
Not accessible: <blocked sources and why>

## In one paragraph
<What they sell, to whom, through which channel, and the one idea that makes it work.>

## The 12 questions
| # | Question | Answer | Class | Status |
|---|---|---|---|---|
| 1 | Structure | ... | OBSERVED | answered |
| ... | | | | |

## How they communicate (last 10 posts)
<Table, one row per post, then the reading: theme and its purpose, product or mood, AI-made or not, voice, aimed at whom vs who buys. See `organic.md`.>

## Site copy
<Headline, what it says and never says, description words, tone, voice consistency. See `landing-site-tracking.md`.>

## Competitors (top level)
<2-4 names: who, what they sell, how they communicate, active ads with filter. What they do that the subject does not.>

## Why it is built this way
<For each key choice: what they do -> why (hypothesis or evidence).>

## Best and worst
<3 + 3 with numbers and source, or UNKNOWN.>

## Verdict
- Works on: ... / Not known: ...
- Copy: ... / Improve: ... / Do not copy: ...
- Experiment to run: ...

## Findings ledger
| ID | Claim | Class | Evidence | Confidence | Search boundary | Unknowns |

Evidence artifacts saved in `<subject>-evidence/` named by ID (E01-library.png, E02-tag-scan.json, E03-gads-map.md...).

## Open questions
<What would resolve each.>
```

Landing breakdown file: `<subject>-landing/landing-structure.md`, one section per screenshot: image, what is there, why.
