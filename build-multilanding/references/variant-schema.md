# Variant data contract (intent-first)

One row per landing hypothesis in `marketing/generated/variants.csv`. Validate
with `scripts/validate_variants.py`. IDs are stable and never recycled.

## Required fields

| Field | Purpose |
|---|---|
| `id` | Landing variant id (stable, internal) |
| `slug` | Unique lowercase URL slug |
| `status` | `draft`, `active`, or `paused` |
| `locale` | BCP 47 language/region tag |
| `audience_id` | Who this is for (from product-marketing.md) |
| `intent_id` | What they are trying to solve now (from keyword-intents.csv) |
| `awareness_stage` | `problem`, `solution`, `product`, or `most-aware` |
| `offer_id` | Canonical offer (from offers.yaml) |
| `message_id` | The promise shown (from message-map.yaml) |
| `campaign_id` | Canonical campaign mapping |
| `ad_group_id` | Canonical ad group mapping |
| `creative_id` | Canonical ad/creative mapping |
| `headline` | Segment promise that honors the ad |
| `subheadline` | Clarification and fit |
| `problem` | Concrete pain/context (may be light for hot intents) |
| `solution` | Mechanism, not vague benefit |
| `proof` | Verified proof or approved proof id |
| `objection` | Primary objection addressed |
| `cta_label` | Visible action label (one primary CTA) |
| `form_id` | Approved form configuration reference |
| `conversion_action` | What counts as conversion (from offers.yaml) |
| `indexation_policy` | `noindex-paid`, `canonical-to`, `indexable-self`, or `test` |
| `canonical_url` | Required when `indexation_policy=canonical-to` |
| `evidence_status` | `confirmed`, `derived`, or `hypothesis` |

Optional: `benefits` (structured list), and governance fields `owner`,
`created_at`, `updated_at`, `approved_by`, `experiment_id`, `start_at`,
`end_at`, `notes`.

## Rules

- Never store secrets, CRM credentials, personal lead data, or executable
  HTML/JavaScript in the table. Render text as text.
- `evidence_status=hypothesis` content is never shown to a visitor as fact.
- The identity chain (audience -> intent -> offer -> message -> campaign/creative
  -> variant -> conversion) must be internally consistent: every referenced id
  exists in its source file.
- UTMs are not stored here as identity; they are generated in the campaign
  manifest from the canonical ids.
