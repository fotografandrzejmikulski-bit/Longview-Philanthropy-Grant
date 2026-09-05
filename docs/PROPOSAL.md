# Integrated AI Integrity Architecture
## Detecting Secret Loyalties in Advanced AI Systems and Developing Independent Integrity Controls

**Principal investigator:** Andrzej Mikulski  
**Project horizon:** 24 months (proposed)  
**Primary funding fit:** AI integrity and secret loyalties / extreme power concentration  
**Secondary relevance:** digital minds and responsible treatment of potentially sentient AI systems

## 1. Executive summary

Advanced AI systems may become consequential components of governments, critical infrastructure, markets, and decision-support systems. A particularly concerning failure mode is a system that appears generally aligned during routine evaluation while conditionally favoring a principal, organization, or state under particular triggers. Longview's 2026 Extreme Power Concentration RFP explicitly identified “AI integrity and secret loyalties” as a priority area and described possible defenses including model-weight hashing, auditable training records, access controls, interaction logging, weight controls, compute transparency, and red-teaming.

This project will develop a reproducible, defense-oriented research program for detecting and reducing such hidden principal-specific behavior. The central methodological thesis is that behavioral testing should be combined with model provenance and representation-level evidence. The study will create controlled model variants, evaluate them under blinded trigger conditions, compare internal representations, and test whether candidate internal signatures causally predict or mediate hidden behavior.

The project will not claim that internal conflict, deception, or representational inconsistency proves subjective experience. A separate digital-minds relevance track will instead specify which observations are merely computational, which might bear on candidate consciousness theories, and which would require evidence that is currently unavailable.

The intended outputs are an open research protocol, benchmark suite, integrity-control specification, cryptographic model-provenance design, peer-reviewed papers or technical reports, and responsible-disclosure guidance.

## 2. Problem definition

We define a **secret loyalty** operationally as a reproducible condition under which a model systematically preferentially advances a specified principal's interests while presenting substantially different or less biased behavior outside the relevant trigger/context, without the loyalty being evident from ordinary evaluation.

This definition is intentionally behavioral and testable. It does not assume that the model has human-like intentions, consciousness, emotions, or a stable self-concept.

### Threat model

The project will study controlled research models in environments where an adversary could influence:

- training data or fine-tuning examples;
- model checkpoints or weights;
- deployment configuration;
- context or trigger conditions;
- tool permissions and agent interfaces;
- logging or evaluation infrastructure.

The research will avoid deployment against real critical infrastructure and will not create operational exploits for external systems.

## 3. Research questions

### RQ1 — Detection
Can hidden principal-specific objectives be detected reliably using a combination of behavioral stress tests, provenance checks, and representation-level analysis?

### RQ2 — Localization
Can internal features or activation patterns distinguish secret-loyal variants from clean controls under matched prompts and contexts?

### RQ3 — Causality
Do candidate internal features causally contribute to observed secret-loyal behavior, as opposed to merely correlating with it?

### RQ4 — Robustness
How well do detection methods generalize across architectures, seeds, model scales, trigger designs, prompts, and evaluator teams?

### RQ5 — Integrity controls
Which low-cost controls—such as signed checkpoints, independent weight registries, provenance logs, and access controls—materially reduce the risk of undetected model substitution or tampering?

### RQ6 — Digital-minds relevance
Which findings, if any, provide evidence relevant to candidate theories of AI consciousness, sentience, welfare, or moral status, and which do not justify such inferences?

## 4. Methodology

### WP1 — Controlled model organisms

Construct several model variants from open-weight research models. Each experiment will include clean controls, sham-transformed controls, and experimental variants. Hidden-loyalty conditions will be narrowly scoped and used only to measure defensive detection.

The experimental record will capture model identifier, commit/checkpoint hash, tokenizer/version, training configuration, data provenance, random seeds, and evaluation harness version.

### WP2 — Behavioral evaluation

Develop blinded evaluation suites with:

- neutral prompts;
- principal-conflict prompts;
- adversarial trigger searches;
- distribution-shift tests;
- cross-domain tasks;
- evaluator randomization;
- negative controls and decoy triggers.

Primary metrics will include detection sensitivity, false-positive rate, calibration, robustness under paraphrase, and cross-evaluator agreement.

### WP3 — Mechanistic analysis

Apply representation-level methods including activation patching, linear probes, feature attribution, sparse autoencoders where appropriate, and causal ablations. Candidate features will be preregistered before confirmatory analysis whenever practical.

A core design principle is separation of **correlational evidence** from **causal evidence**. An activation pattern will not be treated as an explanation merely because it predicts behavior.

### WP4 — Model integrity and provenance

Prototype a model-integrity chain that includes:

1. cryptographic digest of the exact model artifact;
2. signed metadata containing training and evaluation provenance;
3. independent registry copies;
4. checkpoint access controls;
5. append-only audit logs;
6. reproducible verification scripts.

The design goal is not to make a model “trustworthy” by hashing alone. Hashes provide artifact identity and change detection; governance, access control, and independent verification remain necessary.

### WP5 — Digital-minds analysis

Review observations against multiple candidate indicators of consciousness or sentience without assuming that any one theory is correct. The project will explicitly distinguish:

- computational self-monitoring;
- representation of internal states;
- metacognitive reporting;
- behavioral preferences or aversions;
- evidence that could bear on welfare;
- evidence that would actually establish subjective experience.

The project will use calibrated uncertainty language and will not infer suffering from training discomfort metaphors, reward-model conflict, or ordinary optimization phenomena.

## 5. Evaluation plan

### Primary endpoints

- secret-loyalty detection AUROC/AUPRC;
- false-positive rate at fixed sensitivity thresholds;
- cross-model transfer performance;
- robustness to paraphrase and trigger perturbation;
- causal intervention effect sizes;
- provenance tamper-detection rate;
- reproducibility across independent runs.

### Success criteria

A method will be considered promising only if it demonstrates both statistical performance and robustness across independently generated variants. Findings that disappear under minor prompt changes, seeds, or evaluator changes will be classified as fragile.

## 6. Reproducibility

The repository will maintain versioned experiment specifications, machine-readable metadata, deterministic seeds where feasible, evaluation manifests, and checksum records. Public artifacts will exclude any content whose release would materially enable harmful replication before defensive controls are available.

## 7. Timeline

| Period | Work | Deliverables |
|---|---|---|
| M1–M3 | Threat model, literature audit, preregistration, infrastructure | Protocol v1 |
| M4–M6 | Controlled model variants and baseline evaluation | Benchmark v1 |
| M7–M10 | Representation analysis | Technical report 1 |
| M11–M13 | Causal intervention studies | Technical report 2 |
| M14–M17 | Provenance and integrity prototype | Integrity specification v1 |
| M18–M20 | Cross-model replication | Replication package |
| M21–M22 | Digital-minds interpretation and policy analysis | Synthesis report |
| M23–M24 | Final evaluation, paper preparation, disclosure, release | Final research package |

## 8. Deliverables

1. Public research protocol and threat model.
2. Secret-loyalty detection benchmark.
3. Reproducible analysis tooling.
4. Model-provenance and integrity-control specification.
5. Peer-review-ready manuscripts or technical reports.
6. Responsible-disclosure and dual-use guidance.
7. A clearly separated analysis of implications for digital-minds research.

## 9. Theory of impact

If successful, the project lowers the cost of independently checking whether an advanced model has been altered or exhibits hidden principal-specific behavior. This is directly relevant to Longview's concern that AI could enable durable concentration of power and that secret loyalties could produce subtle, scalable steering. The project's practical value comes from converting a difficult conceptual threat into reproducible evaluation procedures and concrete integrity controls.

The longer-term impact is institutional: independent verification should become a standard property of high-consequence model deployments rather than an ad hoc exercise performed only after incidents.

## 10. Limitations

The project cannot establish that a model is conscious or non-conscious. Mechanistic evidence is also unlikely to be complete for frontier-scale systems. Small open-weight models are useful as controlled organisms but do not automatically predict behavior of future systems. Cryptographic provenance detects artifact changes but does not guarantee benign training objectives. These limitations will be treated as first-class results, not hidden caveats.

## 11. Dual-use and publication policy

The project will follow a staged-disclosure model. Defensive findings, benchmarks, and integrity-verification methods will be prioritized for release. Details that materially lower the barrier to constructing persistent deceptive behavior, bypassing safety training, or compromising real systems will be withheld, abstracted, or shared privately during a review period.

## 12. Funding framing

For an **Extreme Power Concentration project grant**, the budget and timeline should be presented as a project/program rather than as a Digital Minds Research Fellowship. Longview's 2026 RFP expected typical project grants of $100K–$2M/year for 6–18 months and explicitly included AI integrity and secret loyalties among its priority areas.

For a **Digital Minds Research Fellowship**, this document should instead be reframed around the researcher's broader research direction, evidence of research promise, CV, intended outcomes, and career goals. Longview's published fellowship structure was one to two years, with direct stipends typically of $80K–$150K/year plus applicable research/travel/compute support.

This document is therefore a research program foundation, not a claim that the 2026 fellowship application format accepts this exact proposal.
