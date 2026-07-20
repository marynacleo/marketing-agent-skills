# Marketing Agent Skills

A working toolkit of marketing skills for AI agents, built and battle-tested on
real client projects: websites, paid campaigns, local SEO, brand content and
short-form video. Each skill teaches an agent a complete method, not a prompt:
honest rules, checklists, data contracts and ready-to-use scripts.

Compatible with Claude Code, OpenAI Codex, and any tool that supports the
Agent Skills specification.

**By [Maryna Skachek](https://maricleo-studio.vercel.app/) · MariCleo Studio**

## The skills

| Skill | What it does |
|---|---|
| [build-multilanding](build-multilanding/) | Data-driven multi-segment landing system: one branded template, many pages, each keeping one promise to one search intent. Landing contracts, attribution to revenue, consent-aware tracking, validation scripts. Also available as a [standalone repo](https://github.com/marynacleo/build-multilanding). |
| [seo-optimization](seo-optimization/) | Organic SEO protocol: persona-first pages, topical clusters (mother/child, not a blog), structured data for Google AND LLM answers (GEO/AEO), real-reviews mechanics, NAP consistency, the monthly Search Console loop. |
| [faq-hub](faq-hub/) | Auto-aggregating FAQ system: each page declares its FAQs inline, a central hub collects them automatically, FAQPage JSON-LD included. Working WordPress mu-plugin + build-time recipe for static sites. |
| [brand-storytelling](brand-storytelling/) | The strategic process BEFORE any brand text: message-first architecture, pain-based personas (not demographic theatre), AI as interviewer and critic rather than writer. |
| [business-roi](business-roi/) | Evaluate an idea BEFORE building it: who pays, for what value, why now, full cost in hours, scalability, burnout risk, and the cheapest real-market test. |
| [emotional-brand-video](emotional-brand-video/) | Feel-First Framework: short documentary-style brand video that makes the viewer feel the story before seeing the product. 4-scene arc, storyboard templates, portable AI-video prompt library (Sora, Kling, Veo, and others). |

## What makes these different

- **Method over prompts.** Each skill encodes a repeatable process with gates
  and acceptance checks, so the output survives contact with a real project.
- **Honesty built in.** Claims are marked confirmed / derived / assumed;
  agents are told to report gaps instead of inventing facts.
- **Separation of engine and fuel.** The skills stay generic; your project's
  audiences, offers, keywords and proof live in your project. Nothing here
  hardcodes one client.
- **Production details included.** The unglamorous parts that make things work:
  consent gates, indexation policy, safe deploy paths, privacy blurs,
  bilingual-site rules, no-em-dash typography.

## Install

Copy any skill folder (or all of them) into your agent's skills directory:

```bash
# Claude Code
cp -r <skill-name> ~/.claude/skills/
# OpenAI Codex
cp -r <skill-name> ~/.codex/skills/
```

Start a new session and the agent picks the skill up automatically when the
task matches.

## Author

**Maryna Skachek** · marketing strategist and e-commerce project lead
(Chef de projet e-commerce, Bac+4; PhD recognized in France as Bac+8).
Studio: [MariCleo Studio](https://maricleo-studio.vercel.app/)

## License

MIT (see [LICENSE](LICENSE)). Use them, adapt them, ship them.
