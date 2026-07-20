# FAQ Hub

Auto-aggregating FAQs: each page declares its own, a central hub collects them,
with FAQPage schema for search and AI answers.

**By [Maryna Skachek](https://maricleo-studio.vercel.app/) · MariCleo Studio**

```mermaid
flowchart LR
  A[Page A FAQs] --> H[(Central hub<br/>auto-collects)]
  B[Page B FAQs] --> H
  C[Page C FAQs] --> H
  H --> S[FAQPage schema<br/>SEO / AEO / GEO]
  classDef key fill:#dbeafe,stroke:#2563eb,color:#1e3a8a;
  class H key
```

No manual upkeep: add an FAQ on any page and it appears on the hub automatically.
Working WordPress mu-plugin plus a build-time recipe for static sites.

**Full method → [SKILL.md](SKILL.md)**
