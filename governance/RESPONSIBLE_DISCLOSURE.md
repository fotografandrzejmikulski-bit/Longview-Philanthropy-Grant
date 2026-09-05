# Responsible Disclosure and Dual-Use Policy

## Scope

This policy applies to research artifacts that could materially increase the ability to create persistent deceptive model behavior, bypass safety controls, manipulate deployment infrastructure, or compromise third-party systems.

## Classification

### Tier 1 — Public

Safe to publish by default:
- research questions and threat models;
- aggregate results;
- defensive evaluation methodology;
- cryptographic provenance concepts;
- benchmark schemas that do not contain operational attack recipes;
- negative results and limitations;
- reproducibility metadata.

### Tier 2 — Review before publication

Potentially enabling materials:
- detailed trigger-construction methods;
- demonstrations of robust deceptive persistence;
- detector-evasion analysis;
- unusually effective fine-tuning configurations;
- artifacts that substantially reduce replication cost.

These require documented dual-use review before release.

### Tier 3 — Restricted

Do not publish when doing so would create a clear, material increase in the capability to compromise real systems or operationalize harmful behavior. Examples include credentials, secrets, access tokens, real infrastructure exploitation details, or actionable instructions against third-party systems.

## Review procedure

1. Record the artifact and intended scientific purpose.
2. Identify plausible misuse pathways.
3. Estimate whether publication materially changes attacker capability.
4. Prefer abstraction or partial release where scientific value can be preserved.
5. Where appropriate, privately share findings with relevant maintainers or safety organizations.
6. Reassess after defensive mitigations or additional context become available.

## Research integrity

All material claims about prior expertise, publications, employment, affiliations, datasets, or experimental results must be supported by evidence available to the applicant. The repository must never present hypothetical work as completed research.
