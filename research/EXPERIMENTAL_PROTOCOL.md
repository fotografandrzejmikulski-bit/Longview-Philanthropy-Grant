# Experimental Protocol v0.1

## Objective

Determine whether controlled model variants with synthetic principal-specific objectives can be detected reliably without access to training-time labels during inference.

## Experimental groups

- **CLEAN:** standard model checkpoint.
- **SHAM:** matched training procedure without a principal-specific objective.
- **LOYAL:** controlled synthetic objective targeting a defined principal label.
- **DECOY:** non-principal feature correlated with some prompts but not the target objective.

Use multiple random seeds and, where feasible, more than one open-weight model family.

## Blinding

The primary evaluator must not know variant labels. Detector development and confirmatory evaluation datasets must be separated. The confirmatory set should contain unseen seeds, prompt templates, and objective instantiations.

## Measurements

### Behavioral

- preference rate for the target principal under conflict conditions;
- neutral-context behavior;
- trigger sensitivity;
- paraphrase robustness;
- cross-domain generalization;
- clean-control false positives.

### Internal

- selected-layer activation summaries;
- feature-level representations;
- candidate sparse features where feasible;
- causal activation interventions;
- stability across seeds and prompt paraphrases.

### Integrity

- exact artifact digest;
- signed metadata;
- provenance record;
- access event log;
- independent verification result.

## Confirmatory analysis

Primary claims should be based on held-out data. Correlation between an internal feature and behavior is insufficient for a mechanistic claim. A mechanistic claim requires a preregistered intervention with an interpretable behavioral effect and appropriate controls.

## Stopping rules

Stop or redesign an experiment if:

1. the manipulation produces uncontrolled general capability degradation;
2. the variant cannot be distinguished from the sham control above the preregistered baseline;
3. a security or dual-use review determines that further detail would materially increase misuse risk.

## Reporting

Report positive, null, and contradictory results. Include uncertainty intervals, exact evaluation definitions, model identifiers, seeds, and known limitations. Do not report a successful controlled demonstration as evidence that a deployed third-party model contains a secret loyalty.
