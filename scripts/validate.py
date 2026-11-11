#!/usr/bin/env python3
"""Validate repository artifacts; never loads or executes target-project code."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    for directory in ("schemas", "templates/messages"):
        for path in sorted((ROOT / directory).glob("*.json")):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, OSError) as exc:
                errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    schema = json.loads((ROOT / "schemas/finding.schema.json").read_text(encoding="utf-8"))
    required = {"error_id", "category", "outcome", "severity", "audiences", "messages", "safe_to_retry", "idempotency_required", "confidence", "evidence", "status"}
    if not required <= set(schema["required"]):
        errors.append("Finding schema is missing required fields")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\nname: whatsmyerror\n"):
        errors.append("Canonical SKILL.md frontmatter is missing or invalid")
    for phrase in ("read-only", "explicit approval", "coverage", "contracts", "Retry-After", "untrusted"):
        if phrase.lower() not in skill.lower():
            errors.append(f"SKILL.md omits core concept: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for path in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]*)?\)", readme):
        if "://" not in path and not (ROOT / path).exists():
            errors.append(f"README link target does not exist: {path}")
    if (ROOT / "src").exists() or (ROOT / "pyproject.toml").exists():
        errors.append("Skill-only release must not ship the abandoned CLI prototype")
    if errors:
        print("\n".join(errors))
        return 1
    print("WhatsMyError artifacts are valid; no target code was executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
