# Intent-first segmentation and message match

## Segment by intent, not by demographic

The unit is not "one audience = one page". It is:

> distinct search intent + awareness stage + offer + message promise = one landing experience.

Several audiences can share one intent and one page. One audience can need
several pages for different intents or stages. The same person may search
"куда поехать в Грузии" today and "Svaneti tour September price" next week:
same audience, different intent, different page.

Identity chain carried through the whole system:

    audience_id -> intent_id -> awareness_stage -> offer_id -> message_id
      -> campaign_id / ad_group_id / creative_id -> landing_variant_id
      -> conversion_action -> qualified lead / deposit / sale / revenue

Group keywords by MEANING (intent), not by minor string variants. A keyword
cluster does not become a page until it has an intent, an offer, a message and
a landing contract.

## Message match: semantic, not word-for-word

The query intent, ad promise, landing headline, offer, proof and CTA must be
consistent. Match the PROMISE, not the exact keyword string. Google asks you to
align query, ad and landing page and deliver what was promised; it does not
require copying the search phrase verbatim into the H1.

Write the **landing contract** before any copy:

- what the searcher wants
- what the ad promises
- what the landing page promises (must honor the ad)
- primary CTA (one)
- proof required
- objections to resolve
- conversion action and its value
- source references (evidence)

Skeleton before the dress: no copy until the contract is filled.

## Intent ladder: which pages to build, and how hot each is

Order intents by how ready the searcher is to act. Each tier needs a different
page treatment:

1. **Brand** (searches your name): shortest page, offer and proof up top, no warm-up.
2. **High-intent category** (direct solution searches): product page, price/dates,
   strong CTA, minimal problem framing.
3. **Problem-aware** (searches the pain, not the solution): lead with the problem,
   PAS is appropriate, build the case before the offer.
4. **Awareness / competitor** (broad, educational): most context, comparison and
   education, softer CTA.

Build hot tiers first (brand, high-intent): they convert cheapest. Expand
downward only when the top tiers reach their volume ceiling.

## Headline mirroring

The strongest form of message match: take the ad headline that actually won on
click-through and downstream conversion, and put it on the H1 and subheadline.
When a variant maps to a tested winning ad, mirror that headline closely
(near-verbatim is fine here). When generating a fresh page before any test,
match the promise semantically. Either way, the visitor must see the promise
they clicked. Mismatched headlines bounce even strong pages.

## Why message match lowers cost (the economic reason)

Google officially frames Quality Score as a diagnostic, not a KPI or a direct
auction input; it does not publish exact weights or guaranteed discounts. In
practice, practitioners consistently report that landing page experience is a
major component and that better ad-to-page consistency lowers cost per click and
raises conversion. Reported industry figures (treat as indicative, not law):

- Landing page experience is often cited around a third of Quality Score weight.
- Low quality scores can cost multiples more per click than high ones.
- Strong quality scores are associated with meaningful CPC discounts.

The mechanism the client cares about: a dedicated page that keeps the ad's
promise raises relevance and trust, which lifts conversion and tends to lower the
cost of each qualified lead. That is the whole reason we build variants instead
of sending paid traffic to a generic page.

Sources (indicative, verify before quoting to a client):
- https://leadpages.com/blog/landing-page-message-match
- https://foundrycro.com/blog/google-ads-landing-page-best-practices-2026/
- https://growleads.io/blog/fix-your-google-ads-quality-score/
