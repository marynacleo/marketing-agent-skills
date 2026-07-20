---
name: build-multilanding
description: Design, build, audit, or scale a data-driven multi-segment landing-page system from one branded template, driven by search intent and a validated project marketing context. Use for paid-ad landing pages (Google/Meta/LinkedIn), personalized or programmatic landing pages, segment-specific campaign variants, message-match pages, lead attribution, campaign URL/UTM manifests, landing-page generators, or requests to create a few to thousands of variants while preserving one brand and one codebase. Reads .agents/product-marketing.md and the project marketing/ context first; never invents audiences, offers, or proof.
---

# Build Multilanding

A generic page is a promise to nobody. Paid traffic arrives with a specific
question, and the page either continues the conversation the ad started or
restarts it from zero at the visitor's expense. This skill builds the first
kind: one maintainable landing system where each URL keeps one promise to one
intent, and every variant is a testable hypothesis with its own paper trail
from ad click to revenue.

Build one system, not copied pages. Each row of the variant table is a
marketing hypothesis; each URL is a view of the same component system. The
payoff for paid traffic: kept promises raise relevance and trust, which lifts
conversion and drops the cost of each qualified lead. That is the entire
business case, and it is why the work starts with contracts, not copy.

The skill is the ENGINE (method, contracts, gates, scripts). The project is the
FUEL (its own audiences, offers, keywords, proof). The engine never stores or
invents a project's audiences or keywords. Read
[references/input-contract.md](references/input-contract.md) first. To see the
whole method in miniature, read
[references/worked-example.md](references/worked-example.md): one offer, three
intents, three different pages.

## Segment by intent, not by demographic

The unit is `distinct search intent + awareness stage + offer + message = one
landing experience`. Several audiences can share one page; one audience can need
several pages. Group keywords by meaning, not by minor string variants.
See [references/intent-and-message-match.md](references/intent-and-message-match.md).

## Start with the project context

1. Read `.agents/product-marketing.md` (strategic source of truth) via the
   project `marketing/source-map.yaml`. Fallback: `.claude/product-marketing-context.md`.
2. Read the campaign brief for the launch. Load only the linked intents,
   messages, offers and proof.
3. Classify every fact as confirmed / derived / hypothesis / unknown.
4. If a confirmed offer, conversion action, audience/intent hypothesis, or the
   required proof is missing, produce a context-gap report and stop. Run
   `scripts/validate_inputs.py`.

## Work in gates

### Gate 1: strategy and contracts
Build the intent matrix. For each variant write a landing contract before any
copy: what the searcher wants, what the ad promises, what the page promises, one
CTA, proof required, objections, conversion action and value, evidence.

### Gate 2: representative concepts
Build and review 3-5 deliberately different concepts, including the longest
realistic copy and one mobile-stress case. Do not generate at scale before this
passes review.

### Gate 3: compose and scale
Compose pages with the modular composer, not a fixed PAS template
([references/page-composer.md](references/page-composer.md)); choose structure by
awareness stage. Generate variants from validated fields
([references/variant-schema.md](references/variant-schema.md)). Reject duplicate
ids/slugs, empty required fields, invalid enums, unverifiable claims, and
mismatched campaign/creative mappings via `scripts/validate_variants.py`.

### Gate 4: conversion, tracking, privacy
Make forms accessible, concise, spam-resistant and idempotent. Wire attribution
to money, not form fills ([references/measurement-and-attribution.md](references/measurement-and-attribution.md)).
Gate all non-essential tags behind consent
([references/privacy-and-consent.md](references/privacy-and-consent.md)).

### Gate 5: QA
Run [references/qa-checklist.md](references/qa-checklist.md): schema, routes,
links, forms, analytics, consent, indexation, metadata, performance
([references/performance-gate.md](references/performance-gate.md)) and
accessibility. Set indexation intentionally per variant
([references/seo-and-indexation.md](references/seo-and-indexation.md)).

### Gate 6: launch and learning
Generate the campaign manifest (`scripts/generate_campaign_manifest.py`) and a
rollback plan. Launch the minimum viable set, usually 1-2 genuinely different
hypotheses per intent cluster, not all concepts. After traffic, compare qualified
conversion and downstream revenue, not clicks. Pause weak hypotheses; feed
verified lessons back into the matrix and `experiments/landing-experiments.csv`.

## Adjacent skills (invoke lazily, via contracts)

Do not load every skill for every task. Hand off only what the step needs, to the
project's own installed skills:

- audience pains and voice of customer -> the project's research/storytelling skill
- offer shaping -> the project's offers work
- campaign and measurement setup -> `paid-ads-launch`
- indexable-page SEO and schema -> `seo-optimization`
- image assets -> `web-images`
- FAQ blocks and objections -> `faq-hub`
- post-conversion nurture -> `brevo-automation`, as an OPTIONAL downstream
  adapter only; never a hard dependency, and never auto-connected.

## Safety and authority boundaries

- Never place API keys, CRM tokens, payment secrets, or `.env` contents in
  prompts, source data, pages, logs, or commits. Use placeholders; the user
  enters secrets in the trusted service UI.
- Do not connect CRM, analytics, auth, ad accounts, payment providers, or
  deploy/publish without explicit permission for that service and action.
- Treat production payments, public launch, campaign activation, and bulk
  messaging as separate human sign-off gates.
- Do not promise unsupported claims (fixed build time, cost, conversion lift, or
  unlimited scale). Respect the project's regulated-claim restrictions.
- Respect project house style: language and bilingual rules, no em dashes in
  public copy, headings without a final period, no AI-tool traces in shipped code.

## Deliverables

Return the smallest useful set: intent/variant matrix; landing contracts; schema
and validated data file; one reusable template and route resolver; representative
previews; campaign/URL manifest; form and attribution contract; consent map;
QA results; launch/rollback checklist; experiment readout plan. State what was
verified, what is assumed, and what still needs human approval.
