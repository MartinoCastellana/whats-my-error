# Analysis coverage roadmap

Current analysis is performed by the selected coding agent. There are no bundled parsers or claims of language-level static-analysis coverage. Use this matrix when reporting what the host agent actually inspected.

| Area | Review guidance | Bundled parser/adapter | Status |
|---|---:|---:|---|
| JavaScript / TypeScript | Yes | No | Agent-assisted review |
| Python | Yes | No | Agent-assisted review |
| PHP | Yes | No | Agent-assisted review |
| Java / Kotlin | Yes | No | Agent-assisted review |
| C# | Yes | No | Agent-assisted review |
| Go | Yes | No | Agent-assisted review |
| Rust | Yes | No | Agent-assisted review |
| Dart / Flutter | Yes | No | Agent-assisted review |
| Other languages | Best effort if host can read them | No | Declare limitations |
| HTTP, GraphQL, gRPC | Yes | No | Contract-guided review |
| WebSocket, SSE, queues | Yes | No | Protocol-guided review |
| Database, filesystem, process | Yes | No | Boundary-guided review |

Never turn this intended scope into a claim that a particular repository was fully analyzed. A useful coverage report names directories/files reviewed, excluded/generated areas, languages and protocols found, analysis method, untraced paths, and the reason each gap remains.
