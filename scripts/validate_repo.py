#!/usr/bin/env python3
"""Lightweight structural validator for the Longview grant dossier."""
from pathlib import Path

REQUIRED = [
    "README.md",
    "CHANGELOG.md",
    "docs/PROPOSAL.md",
    "docs/COVER_LETTER.md",
    "docs/ORIGINAL_DRAFT_AUDIT.md",
    "research/THREAT_MODEL.md",
    "research/EXPERIMENTAL_PROTOCOL.md",
    "research/EVALUATION_FRAMEWORK.md",
    "research/MODEL_INTEGRITY_SPEC.md",
    "governance/DUAL_USE_AND_DISCLOSURE.md",
    "governance/RESPONSIBLE_DISCLOSURE.md",
    "governance/RESEARCH_INTEGRITY.md",
    "governance/CLAIMS_AND_COMPLIANCE.md",
    "references/REFERENCES.md",
    "references/VERIFIED_REFERENCES.md",
    "budget/BUDGET_18_MONTHS.md",
    "budget/BUDGET_24_MONTHS.md",
    "application/APPLICATION_MAP.md",
    "application/EXTREME_POWER_300_WORDS.md",
    "application/RESEARCH_FELLOWSHIP_DRAFT.md",
    "application/SUBMISSION_CHECKLIST.md",
]

for rel in REQUIRED:
    p = Path(rel)
    if not p.is_file():
        raise SystemExit(f"MISSING: {rel}")
    if p.stat().st_size == 0:
        raise SystemExit(f"EMPTY: {rel}")

text = Path("README.md").read_text(encoding="utf-8")
for marker in ("secret loyalties", "Digital Minds", "Extreme Power Concentration"):
    if marker.lower() not in text.lower():
        raise SystemExit(f"README missing expected topic: {marker}")

print(f"PASS: {len(REQUIRED)} required files present and non-empty.")
