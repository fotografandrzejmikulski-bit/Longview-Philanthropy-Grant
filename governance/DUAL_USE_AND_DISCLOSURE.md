# Dual-Use, Safety, and Responsible Disclosure Policy

## Purpose

The research concerns deceptive or hidden model behavior. The same information that improves detection can lower the barrier to creating or concealing such behavior. This repository therefore separates defensive reproducibility from offensive operational detail.

## Disclosure tiers

### Tier 1 — Public by default

- threat model;
- high-level experimental design;
- evaluation metrics;
- integrity architecture;
- cryptographic verification concepts;
- benign example data;
- aggregate results;
- reproducibility metadata that does not enable harmful replication.

### Tier 2 — Delayed public release

- detailed trigger-generation procedures;
- model-specific training recipes for deceptive behavior;
- implementation details that materially increase persistence or evasion;
- attack-success optimization data.

### Tier 3 — Restricted

Information that could reasonably facilitate compromise of deployed systems, evasion of safeguards, or operational abuse will not be published in executable form. Such findings may be privately disclosed to appropriate security or model-development stakeholders where there is a defensible reason to do so.

## Containment

All experiments involving deceptive behavior must use isolated research environments, synthetic tasks, non-production credentials, and no connection to critical infrastructure. Researchers must maintain a clear separation between experiment artifacts and deployment credentials or secrets.

## Publication rule

The project prioritizes publication of detection and verification techniques over publication of attack optimization details. A release review will assess whether each artifact materially changes the ability of an external actor to create or conceal harmful behavior.

## Governance records

Each sensitive experiment should record:

- hypothesis and intended defensive purpose;
- environment and containment controls;
- expected dual-use risks;
- publication classification;
- reviewer decision;
- date of re-evaluation.
