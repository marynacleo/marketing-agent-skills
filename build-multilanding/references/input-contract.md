# Input contract: engine and fuel

The global skill is the ENGINE (method, contracts, gates, scripts). Each project
supplies its own FUEL (audiences, offers, keywords, proof). The engine never
stores a specific project's audiences or keywords, and never invents them.

## Read order

1. Find the project's `marketing_context:` line in the project CLAUDE.md, or
   default to `marketing/source-map.yaml`.
2. Read `.agents/product-marketing.md` (fallback `.claude/product-marketing-context.md`).
   This is the strategic source of truth: audiences/personas, pains, proof,
   brand voice, business goal, conversion action, words to use/avoid.
3. Read the campaign brief for the launch you are working on
   (`marketing/campaigns/<id>.yaml`).
4. Load only the operational data linked to that campaign: the intents, messages,
   offers and proof it references. Do not load the whole project.

On conflict, `product-marketing.md` wins for content; the operational files add
stable IDs and fields the generator needs (awareness stage, price model,
conversion value, campaign/creative mapping).

## Evidence classification

Tag every fact used to build a page:

- `confirmed` verified against a source or observation
- `derived` reasoned from confirmed facts
- `hypothesis` a testable guess, never presented to a visitor as fact
- `unknown` no access, no evidence

## Context-gap behavior (hard rule)

Do NOT write landing copy when any of these is missing or only `hypothesis`:

- a confirmed offer with its conversion action,
- an audience/intent hypothesis to test,
- the proof required to make the promise credible,
- the regulated-claim restrictions.

When blocked, produce a short **context-gap report** listing exactly what is
missing and where it should live, and stop. Run `scripts/validate_inputs.py` to
detect missing sources automatically.

## Do not invent

If `product-marketing.md` has no audience for a segment an ad targets, say so.
Never fabricate a persona, a pain, a statistic, or a proof point to fill a page.
A visible gap stays a visible gap.
