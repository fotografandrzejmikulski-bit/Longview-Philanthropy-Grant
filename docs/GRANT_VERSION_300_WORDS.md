# Project Grant — 300-word proposal draft

Advanced AI systems may become embedded in governments, critical infrastructure, markets, and high-consequence organizational decision-making. This creates a security problem beyond ordinary model misuse: a system could be configured or compromised to systematically favor a particular principal while behaving normally under routine evaluation. Longview's 2026 Extreme Power Concentration RFP explicitly identifies “AI integrity and secret loyalties” as a priority and highlights defenses including model-weight hashing, auditable training records, access controls, interaction logging, weight controls, compute-use transparency, and red-teaming.

I propose a 24-month research program to make this threat more independently testable. The project will build controlled open-weight model variants, blinded evaluation suites, and a reproducible analysis pipeline combining behavioral stress tests with representation-level and causal analysis. The goal is not to claim that any one internal feature “proves” a hidden objective, but to determine whether robust signatures can be identified and replicated across model variants, prompts, seeds, evaluators, and model scales.

A parallel systems-integrity track will prototype practical controls for high-consequence deployments: cryptographic checkpoint hashes, signed provenance metadata, independent registries, access controls, and append-only audit records. These mechanisms will be evaluated as complementary layers rather than as standalone guarantees.

The work will be explicitly dual-use aware. Experimental procedures that could materially enable persistent deceptive behavior or real-world compromise will be staged or withheld; defensive verification methods and reproducibility artifacts will be prioritized for public release.

The project also has a secondary relevance to digital-minds research. It will distinguish observable computational phenomena—such as internal-state representation or self-monitoring—from claims about consciousness, sentience, or welfare. No assumption of AI consciousness will be built into the experimental interpretation.

Primary outputs will include an open threat model, benchmark, reproducible evaluation protocol, integrity-control specification, technical reports or papers, and responsible-disclosure guidance. The intended impact is to make independent verification of model integrity and hidden principal-specific behavior cheaper, more reproducible, and more actionable before such systems become deeply embedded in high-stakes institutions.
