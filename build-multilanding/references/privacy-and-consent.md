# Privacy and consent (EU / France aware)

For France and the EU, non-essential advertising trackers generally require
prior consent. Consent is a gate that sits before tags fire, not an afterthought.

## The consent gate

- Identify the CMP (consent management platform) the project uses.
- Set the default consent state (before any choice) to denied for ad/analytics
  storage where required.
- Google **Consent Mode v2** supports basic and advanced implementations; pick
  the one the project actually needs, do not blindly force one.
- Verify tag behavior BEFORE and AFTER consent. Nothing non-essential should
  fire before consent.
- Validate with Tag Assistant (or the project's equivalent) end to end.
- Document exactly which tags and what data fire in each consent state.
- Do not enable Enhanced Conversions or first-party data sharing without a
  confirmed legal basis and a matching privacy notice.

## Form and data hygiene

- Consent copy on the form matches the actual data flow and retention.
- Collect the minimum needed; no secrets or unexpected personal data on the page.
- Idempotent submission: handle retries and duplicates without double-counting.

## Boundaries

Do not connect ad accounts, analytics, CRM, or payment providers, and do not
publish or activate a campaign, without explicit permission for that specific
service and action. Treat launch, bulk messaging and payments as separate human
sign-off gates. This composes with the project's paid-ads-launch skill.
