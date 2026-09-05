# Independent AI Integrity — Final 300-Word Project Proposal

Advanced AI systems may become embedded in governments, critical infrastructure, markets, and high-consequence decision-making. A consequential failure would occur if a model were configured or compromised to systematically favor a hidden principal while appearing normal under routine evaluation. Longview's Extreme Power Concentration RFP explicitly identifies **AI integrity and secret loyalties** as a priority area.

I propose a defense-oriented research program to make this threat independently testable. The project will construct controlled open-weight model variants, clean and sham controls, blinded evaluation suites, and a reproducible analysis pipeline combining behavioral stress tests with representation-level and causal analysis. The central question is whether robust signatures of hidden principal-specific behavior can be detected and replicated across model variants, prompts, random seeds, evaluators, and model scales.

A parallel integrity track will prototype practical controls for high-consequence deployments: cryptographic checkpoint hashes, signed provenance metadata, independent registries, access controls, and append-only audit records. These controls will be evaluated as complementary layers: hashing can establish artifact identity and detect changes, but cannot by itself establish benign training objectives.

The work will be explicitly dual-use aware. Experimental procedures that could materially lower the barrier to persistent deceptive behavior or real-world compromise will be staged, abstracted, or withheld where appropriate. Defensive verification methods, negative results, and reproducibility artifacts will receive publication priority.

Outputs will include an open threat model, benchmark, reproducible evaluation protocol, integrity-control specification, technical reports or papers, and responsible-disclosure guidance. The intended impact is practical: reduce the cost of independently checking whether an advanced model has been altered or exhibits hidden principal-specific behavior before such systems become deeply embedded in institutions where correction may be difficult.

The program is designed around short feedback loops, independent replication, and rapid revision as AI capabilities and the threat landscape evolve.