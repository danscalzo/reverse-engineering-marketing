# Reconstruction: from inventory to mechanism

The inventory (the 12 questions) says WHAT they do. Reverse engineering starts here: rebuild the machine that produces what you saw, say why each part is there, and test the model with a prediction. Without this step the output is a competitor analysis, however detailed.

Depth: Quick = one key choice in one line (leading hypothesis + its rival). Standard = 3 key choices, blueprint, 2 predictions. Deep = 3-5 key choices, full blueprint, a prediction per key choice, rebuilt test log.

## 1. Pick the key choices
Not every fact needs a why. Pick the 3-5 choices that cost them money or effort, or that differ from what the rest of the market does (`compare.md` if competitors are in scope): the hook they repeat, the offer form, the destination, the channel mix, the geography, the proof they lead with.

## 2. Rival hypotheses (at least 2 per key choice)
One explanation is a story, not a reconstruction. For each key choice write 2-3 hypotheses that compete, then name the evidence that tells them apart.

Keep two questions separate, they have different answers:
- **Why they chose it**: works for them / constraint (budget, compliance, platform limit, stock, staff) / agency or tool default / habit or founder taste.
- **Why it works** (if it does): which fear it removes, which buyer it speaks to, which step of the funnel it feeds.

Typical rivals for the commonest signals:
| Signal | Rival hypotheses | Evidence that separates them |
|---|---|---|
| Ad running for months | winner kept on purpose / evergreen ad left on with small budget / brand or retargeting ad, not prospecting | new variations of it appearing (= they bet on it); same copy across new ads; landing still live and updated |
| Many near-identical ads | testing hooks / scaling a winner across placements / agency template output | launch dates (one batch or waves), what stopped first, whether the "losers" were all stopped together |
| No price on site | high-ticket, price kills the lead / price varies by case / hiding a weak price | competitors in the same market show price or not; quote form questions; reviews mentioning price |
| National geo with exclusions | logistics or service coverage / regulatory limit / past test showed bad lead quality there | the same exclusion across all ads and dates; service area page; job or office locations |

Mark the leading hypothesis INFERRED with its evidence IDs; the rivals stay listed, with what would kill them.

## 3. Predictions (the test of the model)
A reconstruction that predicts nothing cannot be wrong, so it cannot be right either. First resolve whatever a check can settle today (e.g. look at the partner's or agency's other clients). For each remaining leading hypothesis (Standard: the 2 strongest key choices; Deep: all) write one prediction that:
- is checkable from outside with the same filters (`monitoring.md`),
- has a date (default: next snapshot, 30 days),
- would come out differently if a rival hypothesis were true: write the expected outcome under each hypothesis, not only under the leading one.

Example: "H1, the monthly price hook is their engine: by <date> the NEW concepts (not just variations) also open on it, and the ads without it disappear first. H2, it is only the agency default: new concepts open with other hooks at the usual rate and nothing gets stopped in a pattern." Refuted = the hypothesis falls, the rival moves up, the ledger gets a line.

Two levels of validation, never confused:
- **Model check**: did the prediction hold? Answers "is my reconstruction right?"
- **Transfer test**: the experiment card on the user's own account (`reading-and-verdict.md`). Answers "does it work for us?". A win here does not prove their mechanism, a loss does not disprove it.

## 4. Rebuild their test log (when the library shows inactive ads)
Where "All ads" includes stopped ads (EU, UK, political or issue ads; elsewhere only active ads are public):
- Group ads by launch date: one batch = one test.
- Inside each batch: what stopped within ~7-14 days (lost, INFERRED), what survived (kept), what got new variations (scaled).
- Read the sequence: what they tried, dropped and doubled down on. This is the closest outside view of their real learning.
Only active ads visible (e.g. commercial ads outside the EU and UK): the past log is UNKNOWN; say so, and rebuild it forward from successive snapshots (an ad present in one and gone in the next = stopped, `monitoring.md`).

## 5. Blueprint: the machine, step by step
One row per step, from the first touch to the money event (`business-type.md`):
| Step | What they use | Its job | Evidence | Class | To rebuild it you need |
|---|---|---|---|---|---|
| Traffic | channel, campaign type, geo | | E.. | | budget, account, assets |
| Hook | concept, hook type | stop the right buyer | | | |
| Offer | what is promised, risk reversal | | | | |
| Handoff | landing, form, quiz, chat | | | | |
| Capture | form vendor, fields, tags | | | | |
| Follow-up | speed, channel, sequence | | | | |
| Money event | sale, booking, approval | | | | |
Close with "**The one idea that makes it run**" in one sentence, and the weakest link (where the machine would break if copied).

## 6. What cannot be rebuilt from outside
Write these as UNKNOWN in every outside-in reconstruction, each with what would resolve it:
- spend and budget split between campaigns,
- test history beyond what the library shows,
- unit economics: cost per sale, close rate, margin, lifetime value,
- audiences, exclusions and optimisation events beyond the visible tags,
- CRM, lead scoring and follow-up after the first reply.
A blueprint step that depends on one of these is marked "inferred, not rebuildable from outside".
