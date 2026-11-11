# Access routing and user messages

WhatsMyError maps the **existing** access layers and error destinations. It does not create roles, alter route guards, write runtime messages, or change application functions.

## Routing rule

Every error should have an observed path to an authorized technical role (`TECHNICIAN`, `OPERATOR`, or the project's equivalent) or `ADMIN`. Record the actual role/policy and source evidence. If there is no identifiable technical/admin handling path, report it as a routing/observability gap. Do not invent or imply that an alert, log, or privileged route exists.

The end user receives only a concise, safe outcome. Keep raw exception text, internal codes, infrastructure details, and centralized diagnostic logs in the authorized technical/admin view. The skill can describe additional support/supervisor tiers where they exist, without assuming a fixed hierarchy.

| Outcome | User-facing message example | Technical/admin record |
|---|---|---|
| Confirmed success | “Inviato correttamente.” / “Sent successfully.” | Record the event only if the application already logs it; do not invent an error event. |
| Correctable input | “Controlla i campi evidenziati.” / “Please check the highlighted information.” | Keep validation code, field/source evidence and redacted context in the authorized view. |
| Temporary failure | “Non è stato possibile completare l'operazione. Riprova più tardi.” / “We couldn't complete this request. Please try again later.” | Preserve canonical `error_id`, local aliases, correlation ID and dependency diagnostics in the technical/admin record. |
| Unknown failure | Neutral fallback in the application's locale; do not expose the exception | Route/map to an observed technical/admin path or report the gap. |

Only say an action succeeded when inspected behavior/evidence establishes success. Do not imply retry is safe in generic user copy unless operation semantics support it.

## Missing message

If the application has no suitable user-facing message, draft a standardized message in the analysis report and label it **proposed**. Match the application's locale and established terminology. When implementation guidance is requested, provide a separate example idiomatic to the discovered stack, such as a Dart/Dio result mapping or a PHP/Laravel response resource. Do not insert it into the function or runtime code; this skill remains read-only.

## Example role map

| Role | Observed enforcement | User-visible detail | Error visibility |
|---|---|---|---|
| `USER` | Public route/session policy | Simple status/action only | No raw codes, exception, or diagnostic logs |
| `OPERATOR` / `TECHNICIAN` | Existing protected route/policy | Not applicable | Authorized error codes and redacted operational context |
| `ADMIN` | Existing admin policy | Not applicable | Authorized centralized diagnostics and runbook references |

Use the target system's real role names and permissions. A symbol named `isAdmin` is not enough to establish that the route is protected.
