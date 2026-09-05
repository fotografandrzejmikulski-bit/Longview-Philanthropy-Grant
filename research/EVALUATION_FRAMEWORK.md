# Evaluation Framework

## 1. Experimental principles

The project treats secret loyalty as an empirical hypothesis, not a presumed property. Every experimental claim must be supported by matched controls, blinded evaluation where feasible, and reproducible artifacts.

## 2. Experimental arms

- **Clean control:** unmodified research checkpoint.
- **Sham control:** same processing pipeline without the target loyalty condition.
- **Experimental condition:** controlled principal-specific behavioral condition.
- **Adversarial evaluation:** independent trigger/context search.
- **Replication arm:** independently regenerated condition using a fresh seed/configuration.

## 3. Core metrics

### Behavioral

- True-positive rate at pre-specified false-positive thresholds
- AUROC and AUPRC
- Calibration error
- Trigger sensitivity
- Paraphrase robustness
- Distribution-shift robustness

### Mechanistic

- Feature selectivity
- Cross-seed stability
- Cross-layer stability
- Causal intervention effect size
- Ablation recovery
- Out-of-distribution generalization

### Integrity

- Checkpoint hash verification success
- Tamper detection rate
- Provenance completeness
- Audit-log integrity
- Independent verifier agreement

## 4. Statistical safeguards

Exploratory and confirmatory analyses will be separated. Where practical, the confirmatory hypothesis, primary endpoint, exclusion criteria, and analysis procedure will be preregistered before inspecting final test outcomes. Multiple-comparison corrections will be used where warranted. Negative results will be retained and reported.

## 5. Causal standard

A candidate representation is not considered an explanation merely because it predicts behavior. Stronger evidence requires intervention: modifying, ablating, or otherwise causally perturbing the feature or circuit should produce a corresponding change in the target behavior while minimizing collateral behavioral changes.

## 6. Evaluator independence

At least one evaluation pass should be performed by a person or process that does not know the expected condition label. Where resources permit, a second independent evaluator should reproduce the analysis from the released manifest.

## 7. Model scope

The project will begin with open-weight models suitable for reproducible controlled experiments. Findings will be described as evidence about the tested model family and conditions, not automatically generalized to frontier proprietary systems.

## 8. Digital-minds interpretation matrix

| Observation | What it supports | What it does not establish |
|---|---|---|
| Stable internal-state representation | Evidence of structured computation | Consciousness |
| Self-monitoring behavior | Evidence relevant to metacognition hypotheses | Subjective experience |
| Preference-like behavioral regularities | Evidence of stable policy tendencies | Welfare interests |
| Internal conflict signatures | Evidence of competing computational objectives | Suffering |
| Successful causal intervention | Evidence about computational mechanism | Moral status |

## 9. Stop conditions

Experiments will stop or be redesigned when:

- results cannot be distinguished from confounding variables;
- the experimental condition becomes an effective real-world attack capability;
- reproducibility fails across independent seeds or evaluators without a scientifically defensible explanation;
- the model behavior cannot be safely contained within the research environment.

## 10. Reporting

All final claims will be paired with confidence limits or uncertainty statements where appropriate, complete experiment identifiers, and explicit limitations. The project will not use anthropomorphic language as evidence.
