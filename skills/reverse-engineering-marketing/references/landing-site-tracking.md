# Landing page, website and tracking

## Capture
1. Open the landing from the ad's URL (keep its parameters: they show how tracking works).
2. Cookies: choose "essential only" and say so; if you need to see tags after consent, do a separate second reading.
3. Desktop screenshots section by section (`save_to_disk`), then mobile (window 400x860: most Meta traffic is mobile). Restore the window afterwards.
4. Full text with get_page_text; accordion FAQs: open them one by one via JS and read the answers.
5. Iframe host (`new URL(iframe.src).hostname`) = form vendor. Do not read iframe parameters.
6. Do NOT submit the form (a submission would be a fake lead with a real cost; only with the user's explicit approval for a genuine enquiry, labelled as a test). Note the first question, the visible number of steps, the fields.
7. Save screenshots to `<output folder>/<subject>-landing/`, numbered.

## Analysis sheet (for each section: what is there + why)
- Above the fold: headline (promises the outcome or the product?), subheadline, background (real photo or stock?), button, proof next to the button.
- Continuity with the ad: same phrase, same photos, same offer?
- Number of possible actions (menu, escape links) and how often the button repeats; sticky bar on mobile?
- Order in which fears are removed (time, cost, commitment, trust) and with which proof.
- Form: multi-step or long, first question, progress bar, when personal data is asked.
- Declared enemy (who or what they attack to position themselves).
- FAQs = objections of the real buyer.
- Legal and compliance text (disclaimers, licences, terms): where and how they place it.
- What is missing / missed opportunities.

## Copy reading (always report it, also for ecommerce)
A structure audit without the words is half an analysis. Report:
- **Main headline**: exact words, language (matches the visitor's?), promise of an outcome or a statement of identity.
- **What the copy says vs never says**: list the 3-5 things a buyer needs (how it works, who it is for, price logic, proof, next step) and tick which the home page covers. Proof hidden one click away (about page) counts as missing from the home.
- **Product or service descriptions**: length (median words), most frequent words (count them from the catalogue or page text), own jargon left unexplained, specs visible or tucked away.
- **Tone**: person addressed, concrete or abstract, numbers or adjectives, objections answered in the text or not.
- **Title tag and meta description** of the home.
- **Voice consistency**: same message on site, social and ads? Quote one line from each. Different voices = different audiences being addressed.
- **Translations**: errors in secondary languages.

## Common lead-killers (check every landing)
Each one found is OBSERVED; its impact on leads is INFERRED unless you have the numbers.
- **No tracking** (no pixel, no Google tag, no conversion event on submit or thank-you page): the platforms optimise blind.
- **No call to action above the fold**: the visitor has to scroll to find what to do.
- **Weak or missing hero image**: stock, blurry, or unrelated to the offer.
- **Weak final CTA**: the bottom of the page ends without a clear next step, or repeats a different action.
- **Form too long** for the value offered, or personal data asked before any commitment.
- **Too much text**: walls of copy, no headings, the offer lost in the middle.
- **Mobile not checked**: button below the fold, form fields too small, slow load.

## Tags (DevTools or JS) [STD]
- Meta: `fbq`, `connect.facebook.net/.../fbevents.js`, `facebook.com/tr?id=`.
- Google: `GTM-`, `G-` (GA4), `AW-` (Ads); Consent Mode = `gcs=` parameter.
- TikTok: `ttq`, `analytics.tiktok.com`.
- Absence: write the page checked + consent state; the tag may be on the thank-you page or inside GTM.
- Conversions API and server-side: invisible from outside -> UNKNOWN (unless Events Manager access).

## Website
- robots.txt, sitemap.xml, `site:` for hidden landings; Wayback for offer and price history (compare only declared dates).
- Pricing, about, case study pages: offer and positioning.
