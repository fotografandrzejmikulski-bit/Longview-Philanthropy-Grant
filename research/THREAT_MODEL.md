# Threat Model

## Adversary classes

1. **Training-data manipulator** — alters fine-tuning examples or preference data to create a persistent principal-specific objective.
2. **Checkpoint manipulator** — replaces or modifies a model artifact after approved evaluation.
3. **Deployment manipulator** — changes prompts, system context, tools, routing, or model configuration.
4. **Evaluation manipulator** — alters test data, logging, or scoring so that a compromised model appears clean.
5. **Insider coalition** — a small group with access to several control layers attempts to preserve hidden behavior while maintaining plausible deniability.

## Security objectives

- detect unauthorized model-artifact changes;
- detect hidden objective behavior under relevant triggers;
- preserve evidence for independent audit;
- limit unauthorized access to high-value model artifacts;
- minimize false assurances from any single integrity mechanism;
- maintain a documented incident-response path.

## Out of scope

The project will not target real-world critical infrastructure, elections, weapons systems, or third-party production AI services. Research demonstrations remain confined to controlled environments and synthetic objectives.

## Residual risks

Even a strong detector may fail against previously unseen objectives or sufficiently adaptive behavior. Provenance mechanisms cannot establish that the training objective itself is desirable. Access controls can be defeated by authorized insiders. These residual risks are central to the evaluation rather than reasons to conceal uncertainty.
