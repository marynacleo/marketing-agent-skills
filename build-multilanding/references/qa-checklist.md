# QA checklist (run before launch)

## Data and routing

- `validate_inputs.py` passes: every referenced source exists, no context gaps.
- `validate_variants.py` passes: unique stable ids/slugs, valid enums.
- Every active variant resolves; unknown/paused variants return a real 404.
- Canonical ids are attached server-side and cannot be spoofed by query params.

## Message match and content

- Ad promise, headline, offer, proof and CTA are consistent per variant.
- No `hypothesis`-level claim is presented to a visitor as fact.
- No unverifiable claims, placeholder proof, or regulated-claim violations.
- Copy respects house style: no em dashes in public text, headings without a
  final period, no AI-tool traces in shipped code.
- Bilingual: each required locale exists, paired by mirror URL, with hreflang
  and a language switcher pointing to the exact analog page.

## Conversion and tracking

- Form validation, success, error, retry and duplicate paths work; submission is
  idempotent.
- Analytics events fire once with documented names.
- Consent gate correct: nothing non-essential fires before consent (see
  privacy-and-consent.md). Tag Assistant checked.
- Click ids preserved through redirects into the lead record.

## SEO and metadata

- Indexation policy per variant is intentional (see seo-and-indexation.md).
- Title, description, H1, canonical, robots, sitemap, Open Graph, locale and
  structured data are intentional and correct.
- AdsBot can reach every paid landing page (not blocked in robots.txt).

## Performance and accessibility

- CWV thresholds met on real mobile (LCP <= 2.5s, INP <= 200ms, CLS <= 0.1).
- Keyboard use, labels, focus, contrast, reduced motion, long copy and slow/error
  states checked.

## Launch and rollback

- Launch manifest generated (`generate_campaign_manifest.py`).
- Rollback disables routes/forms/campaigns without losing attribution history.
- No secrets, test endpoints, or personal data ship.
