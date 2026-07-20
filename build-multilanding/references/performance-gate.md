# Performance gate

Speed is both a conversion factor and part of landing page quality. Most paid
traffic is mobile, so the target is mobile-first.

## Acceptance thresholds (Core Web Vitals, 75th percentile of real mobile loads)

- LCP <= 2.5 s
- INP <= 200 ms
- CLS <= 0.1

Measure at the 75th percentile of real mobile field data where available, not a
single lab Lighthouse run on a fast desktop. A lab run is a smoke test, not proof.

## Functional performance checks

- Arbitrary query parameters (gclid and other click ids) work and are preserved.
- Redirects do not drop attribution parameters.
- Forms and conversion events work on mobile, including slow and error states.
- No 404/403 for AdsBot; unknown or disabled variants return a real 404.
- Images optimized (see the project web-images skill), sized to avoid layout
  shift; fonts loaded without blocking or causing CLS.

## Common regressions to watch

- Fonts in preload causing layout shift.
- Missing width/height on images (CLS).
- Third-party tags loading before consent and blocking render.
