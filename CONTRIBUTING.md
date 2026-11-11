# Contributing

WhatsMyError is a portable agent skill. Keep `SKILL.md` as the canonical workflow and preserve the distinction between guidance and implemented automation.

## Changes

- Update the root `SKILL.md` first, then keep product shims aligned.
- Document actual host/product constraints and versions; avoid universal compatibility claims.
- Add fixture evidence for new detection guidance and include negative cases where a pattern is benign.
- Keep examples illustrative and free of real credentials, personal data, or production identifiers.
- Update `docs/roadmap.md` when implementation scope changes.

## Local checks

Python 3.12+ is needed for validation scripts; using the skill itself requires no install.

```bash
python3 scripts/sync_shims.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests/unit -v
```

Do not run scripts from a target repository unless the user approved the exact command.
