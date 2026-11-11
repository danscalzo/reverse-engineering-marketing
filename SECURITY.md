# Security

## What this repository is
Markdown instructions for an agent, plus two read-only helper scripts:
- `scripts/tag-scan.js` reads the page it is run on and returns JSON. It sends nothing and changes nothing.
- `scripts/gads_map.py` runs read-only Google Ads queries with credentials you supply locally. It contains no mutate calls.

No credentials, tokens or account IDs belong in this repository. `references/local.md` is git-ignored for your private settings.

## Reporting a problem
If you find something that could leak data, change an account, or push an agent past the guardrails in `SKILL.md`, please report it privately through GitHub: Security tab, "Report a vulnerability". If that is not available, open an issue without the sensitive details and ask for a private channel.

Please include: the file, what happens, and how to reproduce it.

## Supported version
Only the latest version on `main`.
