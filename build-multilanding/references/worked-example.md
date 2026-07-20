# Worked example: one offer, three intents

A complete miniature of the system. One tour operator, one offer, three search
intents, three landing experiences. Copy the shape, not the words. All names
and data are fictional; brand style: no em dashes, headings without a final
period, one primary CTA per page.

## The offer (from offers.yaml)

```yaml
- offer_id: offer-svaneti-sep
  name: Svaneti small-group trek, September
  what: 6-day guided trek in Svaneti, groups of 8, local guide, hotels booked
  price_model: fixed
  price_value: "1290 EUR"
  primary_conversion: deposit
  conversion_value: "300 EUR deposit, ~1290 EUR booking"
  proof_refs: [proof-reviews-49, proof-groups-140]
```

Same offer. Three different people are searching. Watch how everything else
changes while the offer stays identical.

## Intent 1: most-aware, the price checker

**Keyword cluster:** "svaneti tour september price", "svaneti trek cost 2026",
"mestia guided tour price"

This person has already chosen Svaneti and September. They are comparing
numbers. Do not sell them the dream; they bought the dream weeks ago. Sell
certainty.

**Landing contract:**

```yaml
intent_id: intent-svaneti-price
audience_id: aud-planner
awareness_stage: most-aware
message_id: msg-price-certainty
searcher_wants: a real price with real dates, no "from EUR..." tricks
ad_promise: fixed price, September dates, small group
landing_promise: the exact price, what it includes, and live availability
primary_cta: Reserve your spot
proof_required: [proof-reviews-49, proof-groups-140]
objections_to_resolve: [is the price final, what if the weather turns]
conversion_action: deposit
indexation_policy: noindex-paid
```

**Ad headline (test winner, mirrored on page):**
"Svaneti in September: 1290 EUR, all included, 8 people max"

**Page hero (mirrors the ad, near-verbatim):**

> H1: Svaneti in September: 1290 EUR, all included
> Sub: Six days, groups of eight, local guide, hotels booked. The price you
> see is the price you pay.
> CTA: Reserve your spot

Structure: hero with price → what is included (line by line, so nothing feels
hidden) → dates and availability → reviews → the two objections answered
plainly → CTA repeated. No problem section, no agitation. This page respects
that the visitor has done their homework.

## Intent 2: solution-aware, the comparer

**Keyword cluster:** "georgia hiking tours small group", "guided trek georgia
caucasus", "georgia trekking company"

This person knows they want a guided trek in Georgia but has not chosen where
or with whom. They are comparing operators. Sell the mechanism and the trust.

**Landing contract:**

```yaml
intent_id: intent-georgia-trek-compare
audience_id: aud-planner
awareness_stage: solution
message_id: msg-why-us-svaneti
searcher_wants: a trustworthy operator and a route worth the flight
ad_promise: small groups, local guides, one region done properly
landing_promise: why one deep route beats a highlights race, and who runs it
primary_cta: See the September trek
proof_required: [proof-reviews-49, proof-guide-bio]
objections_to_resolve: [why only Svaneti, is a small operator reliable]
conversion_action: deposit
indexation_policy: indexable-self
```

**Page hero:**

> H1: One region, done properly: six days deep in Svaneti
> Sub: Big tours race through five regions in a week. We spend six days where
> the towers are, with a guide who grew up under them.
> CTA: See the September trek

Structure: hero with differentiation → how the trek works day by day →
guide bio with a real face → reviews → comparison block (us vs typical
multi-region tour, honest, no strawmen) → objections → CTA. This page is
indexable: it answers a real query with real substance, so it earns organic
visits alongside paid ones.

## Intent 3: problem-aware, the dreamer

**Keyword cluster:** "where to go in georgia mountains", "georgia in september
worth it", "unusual hiking destinations europe"

This person has an itch, not a plan. Two weeks of vacation, a feeling that the
usual options are worn out, and a browser full of tabs. Name that feeling
before offering anything.

**Landing contract:**

```yaml
intent_id: intent-mountains-idea
audience_id: aud-dreamer
awareness_stage: problem
message_id: msg-stop-scrolling
searcher_wants: a destination that feels like a discovery, not a package
ad_promise: the mountain region most people miss
landing_promise: a concrete answer to "where", with an easy first step
primary_cta: Get the route and dates
proof_required: [proof-reviews-49]
objections_to_resolve: [is Georgia safe and easy, am I fit enough]
conversion_action: form (route guide + dates by email)
indexation_policy: noindex-paid
```

**Page hero (PAS is right at this stage):**

> H1: Still scrolling for a mountain trip that does not feel like a package
> Sub: There is a region in Georgia where 12th-century towers stand in
> villages higher than most ski resorts. Groups of eight go in September.
> CTA: Get the route and dates

Structure: hero naming the itch → the reveal (Svaneti, shown not described:
three strong photos, one map) → what six days there look like → "is this for
me" (fitness, safety, logistics answered honestly) → light CTA (email the
route guide, not a deposit) → reviews → CTA. The conversion here is softer on
purpose: this visitor needs a smaller first step, and the email feeds the
nurture flow.

## The three rows (variants.csv, abridged)

| id | intent | stage | headline promise | CTA | conversion | indexation |
| --- | --- | --- | --- | --- | --- | --- |
| var-sv-price | intent-svaneti-price | most-aware | exact price, all included | Reserve your spot | deposit | noindex-paid |
| var-ge-compare | intent-georgia-trek-compare | solution | one region done properly | See the September trek | deposit | indexable-self |
| var-mt-idea | intent-mountains-idea | problem | the region most people miss | Get the route and dates | form | noindex-paid |

One template renders all three. One offer sits behind all three. What changed:
the promise, the structure, the proof placement, the size of the first step.
That is the whole method.

## What the readout looks like

After two weeks: var-sv-price wins on cost per deposit, var-mt-idea fills the
email list cheaply but converts to deposits slowly, var-ge-compare converts
mid but also ranks organically and compounds. Decision: scale price and
compare, keep idea as list-builder, write the next hypothesis from what the
leads actually asked.
