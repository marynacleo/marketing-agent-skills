# SEO and indexation policy

Paid-ad variants and organic pages need different indexation. Decide it per
variant, do not blanket-apply one rule.

## Policy table

| Page type | Policy |
|---|---|
| Paid-only variant, no standalone SEO value | `noindex`, crawlable, excluded from sitemap |
| True duplicate of an indexable page | `rel=canonical` to the preferred page |
| Genuinely useful page for a real intent | Indexable, self-canonical, in sitemap |
| Temporary A/B variant | Project test policy (usually canonical or noindex) |

Rules:

- Never block a Google Ads landing page from Google AdsBot in `robots.txt`.
  AdsBot must reach the page, or Ads may reject the destination. `noindex` only
  works if the crawler can open the page and read the tag.
- `canonical` and `noindex` solve different problems (consolidation vs exclusion).
  Do not stack them mechanically "just in case".
- For a bilingual site, every indexable page carries `hreflang` (self + pair +
  x-default) and links to its exact-analog page, not the other language's home.

## Doorway / thin-content boundary

Google penalizes large volumes of low-value pages built to manipulate search,
not automation itself. The crime is lack of unique value, not templating. Each
variant that competes in organic search must give real, segment-specific value.
This is why paid-only variants are usually kept out of the organic index: they
exist to serve a click, not to rank.

(Do not hardcode a specific dated algorithm update as law; cite a current
primary source if a date is needed.)

For structured data (FAQPage and similar) and deeper technical SEO, hand off to
the project's SEO/schema skill only for indexable pages.
