# Roadmap and implementation status

## Delivered in this repository

- Canonical portable `SKILL.md`, `AGENTS.md`, and instruction shims for Codex-compatible agents, Claude Code, Cursor, and GitHub Copilot.
- English README with workflow diagrams, usage prompts, an event example, safety rules, and honest compatibility claims.
- Taxonomy, architecture, threat model, coverage matrix, contribution guidance, event/finding schemas, localized message examples, and illustrative framework fixtures.
- Lightweight artifact validation. No target source is executed.

## Not implemented

- CLI, scanner, parsers, AST/data-flow engine, dependency/service discovery, cache, or repository report generator.
- Framework wiring/code generators, patch application, rollback engine, test runner, CI scanning integration, or automated RBAC enforcement.
- Native integration/installer for Gemini CLI, Roo Code, Aider, or every host version.

## Suggested milestones

1. Review skill use on fixture repositories and tighten finding/evidence guidance.
2. Add manually verified fixtures across Express, FastAPI, Laravel, and Dio.
3. If justified, design an optional offline scanner with explicit per-language confidence and resource limits.
4. Add protocol adapters and machine-readable reports only alongside meaningful tests and supported schemas.
5. Evaluate host-specific skill discovery and release validated shims.

Do not mark a milestone complete based on documentation alone when it requires executable behavior.
