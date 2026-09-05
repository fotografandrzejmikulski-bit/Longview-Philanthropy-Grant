# 300-word project proposal — Extreme Power Concentration

Advanced AI systems may become embedded in government, markets, critical infrastructure, and corporate decision-making. A consequential security failure would occur if a model were compromised to systematically favor a hidden principal while appearing normal under routine evaluation. Longview's 2026 Extreme Power Concentration RFP explicitly identified “AI integrity and secret loyalties” as a priority area.

I propose a controlled research program to develop independently verifiable methods for detecting such hidden principal-specific behavior and for reducing the risk of model tampering or substitution. The research will use open-weight models in sandboxed environments and will create synthetic secret-loyalty variants alongside clean and sham controls. We will test them with blinded behavioral evaluations, distribution-shifted prompts, adversarial trigger searches, and evaluator randomization.

The central technical contribution will combine behavioral detection with model-internal analysis. Activation-level measurements, sparse autoencoders where appropriate, linear probes, activation patching, and causal ablations will be used to test whether candidate internal signatures are reproducible and causally relevant rather than merely correlational. Evaluation will emphasize held-out objectives, cross-seed replication, false-positive rates, calibration, and robustness to prompt perturbation.

A parallel engineering workstream will prototype an integrity architecture based on cryptographic model-artifact digests, signed provenance metadata, independent registries, access controls, audit logs, and reproducible verification scripts. Hashing will be treated as an identity and tamper-detection mechanism, not as a guarantee of benign behavior.

Outputs will include a research protocol, detection benchmark, replication materials, integrity-control specification, technical papers, and responsible-disclosure guidance. Potentially enabling attack details will be staged or withheld where publication would materially increase misuse risk.

The theory of impact is straightforward: convert a difficult but plausible concentration-of-power threat into measurable failure modes and practical verification controls that independent institutions can test and adopt. The project is designed for short feedback loops, replication, and rapid revision as the threat model evolves.
