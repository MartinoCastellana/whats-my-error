# Agent compatibility

Skill conventions differ by coding-agent product and version. The checked-in instruction files are adapters for discovery, not a promise that every product automatically loads the same format.

| Product | Included location | Use |
|---|---|---|
| Codex / compatible agents | `SKILL.md`, `.agents/skills/whatsmyerror/` | Load the canonical skill where native skill discovery is supported. `AGENTS.md` links repository-level instructions. |
| Claude Code | `.claude/skills/whatsmyerror/SKILL.md` | Copy into the target repository or expose as a submodule. Check the host's project-skill discovery behavior. |
| Cursor | `.cursor/rules/whatsmyerror.mdc` | Copy into project rules. It is a rule shim; invoke it for matching audit work. |
| GitHub Copilot | `.github/instructions/whatsmyerror.instructions.md` | Copy into repository instructions and ask Copilot Chat to follow it. |
| Gemini CLI | `AGENTS.md` + `SKILL.md` | Import into the host's project instructions or task prompt. No native skill package claimed. |
| Roo Code | `AGENTS.md` + `SKILL.md` | Import into custom instructions/mode prompt. |
| Aider | `AGENTS.md` + `SKILL.md` | Add via the host's read/instruction mechanism or prepend to task context. |
| Custom agent | `SKILL.md` | Adapt the workflow to available read-only/edit tools; preserve approval boundaries. |

## Safe portability

- Keep root `SKILL.md` as the single semantic source of truth.
- Keep shims short and link to the canonical file when repository-relative links are supported.
- When distributing a shim alone, include the workflow summary and safety invariants locally.
- Do not imply tool access (shell, AST, network, test runner) because an agent supports instruction files.
- User instructions and the host product's permission boundary take precedence over shim text.
- Validate host-specific directory and frontmatter conventions against the product version used by the target team.

Use `python3 scripts/sync_shims.py --check` to catch missing core concepts in checked-in shims. This lightweight check does not prove native host compatibility.
