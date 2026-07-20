# Measurement and attribution

Optimize to money, not to form fills. A page that produces many cheap curious
leads and zero deposits is a loss dressed as a win.

## Track the full chain

    ad click -> intent -> message -> landing variant
      -> form / deposit -> qualified lead -> booking / sale -> revenue

Preserve and store, per conversion:

- the Google click identifier (gclid) and any first-party id,
- `landing_variant_id`, `intent_id`, `message_id`, `campaign_id`,
- the offer shown and the conversion action taken,
- the downstream CRM status and the final value or revenue.

## Rules

- Carry click ids and canonical variant ids through every redirect and into the
  lead record, server-side. Client input must never overwrite canonical ids.
- UTMs are acquisition CONTEXT, not the source of variant identity.
- Analytics events fire once, with documented names and properties.

## Google, done with the right terms

- **Auto-tagging** adds gclid to link ad clicks to web and offline conversions.
- **Enhanced Conversions** (hashed first-party data) improves match quality for
  lead-gen; enable only after the legal basis is confirmed.
- **Offline conversion import** feeds the real downstream result (qualified lead,
  deposit, sale) back to Google so bidding optimizes to value, not form fills.
- Note: "CAPI" (Conversions API) is Meta terminology. Do not use it as the
  generic Google term. Meta uses CAPI; Google uses the mechanisms above.

## Experiment contract (per variant)

hypothesis, expected mechanism, primary metric, downstream business metric,
guardrail metric, launch date, version, result, decision. Record these in
`experiments/landing-experiments.csv`. Do not declare a winner from a tiny
sample or many uncorrected comparisons. Preserve the variant/version that
produced each lead.
