# Monitoring over time

A single reading is a photo; strategy shows in the changes. Use when the user wants to follow a competitor or after a full analysis worth watching.

## Snapshot (save every time)
File `<output folder>/<subject>-snapshots/<YYYY-MM-DD>.md` with:
- Filters used (country, active/all, platforms).
- Active ads: library IDs, start dates, format, concept, hook type.
- Landing URLs and the offer and price shown (screenshot of the hero).
- Organic: posts in last 30 days, top post, followers (with date).
- Reputation: rating and count per platform.
- Tag scan result (`scripts/tag-scan.js`) for the main landing.

## Diff (next run)
- Compare only snapshots taken with identical filters.
- Report: new ads, stopped ads, ads still running (= likely winners), new concepts, offer or price changes, new landing pages, tag changes, rating trend.
- First diff establishes normal churn. Call something a "strategy change" only if it persists in the next snapshot.

## Cadence
- Default monthly; weekly only during a launch or a promotion.
- A recurring run (scheduled task or routine) only with the user's explicit OK, and it only reads and writes snapshot files: it never contacts the subject.
