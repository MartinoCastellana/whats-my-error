# Error taxonomy

## Event fields

| Field | Meaning |
|---|---|
| `error_id` | Stable domain/code identifier independent of copy |
| `category` | `NETWORK`, `HTTP_CLIENT`, `HTTP_SERVER`, `AUTH`, `VALIDATION`, `RATE_LIMIT`, `TIMEOUT`, `DATABASE`, `FILESYSTEM`, `DEPENDENCY`, `QUEUE`, `RESOURCE`, `CONFIG`, `BUSINESS`, `SECURITY`, or `UNKNOWN` |
| `outcome` | `SUCCESS`, `EXPECTED_FAILURE`, `TRANSIENT_FAILURE`, `PERMANENT_FAILURE`, or `UNKNOWN` |
| `severity` | `INFO`, `WARNING`, `ERROR`, or `CRITICAL`, based on context and impact |
| `http_status` | Optional transport status; never use alone to infer business outcome or audience |
| `audiences` | Any combination of `USER`, `SUPPORT`, `TECHNICIAN`, `SUPERVISOR`, `ADMIN` |
| `messages` | Localizable and redacted audience-specific content |
| `safe_to_retry` | True only with evidence of transient failure and safe operation semantics |
| `idempotency_required` | Whether a key/other protection is required before retry |
| `retry_policy` | Bounded attempts/backoff/jitter and `Retry-After` handling, when justified |
| `correlation_id`, `trace_id` | Validated linkage identifiers; never secrets |
| `evidence`, `confidence`, `source_location` | Minimal reviewable evidence and uncertainty |
| `status` | `detected`, `proposed`, `fixed`, `verified`, or `needs_review` |

## Interpret status in context

| Signal | Starting hypothesis | Checks before conclusion |
|---|---|---|
| HTTP 2xx | Transport success | Does a documented payload contract encode an application failure? |
| 400 / 422 | Expected input failure | Is the response safe and actionable without sensitive detail? |
| 401 / 403 | Authentication/authorization | Are session handling, RBAC, and resource-existence privacy correct? |
| 404 / 409 | Expected absence/conflict | Does the response leak protected-resource existence? Does retry require refresh? |
| 408 / timeout | Possibly transient | Deadline, cancellation, idempotency, and end-to-end budget |
| 429 | Rate limit | Parse `Retry-After`, quota scope, retry budget, and repeated-impact escalation |
| 500 | Unknown server failure | Do not assume transient; inspect known cause and operation semantics |
| 502 / 503 / 504 | Often transient dependency issue | Verify provider behavior, idempotency, retry budget, jitter, circuit breaking |
| Database deadlock | Possibly transient | Transaction safety, limited retry, idempotency |
| Database constraint | Usually expected/permanent | Input validation, race/conflict, no raw SQL disclosure |

## Audience separation

Audience views are projections of one event, not mutually exclusive categories. User messages stay concise and safe. Support messages include stable codes and correlation references. Technical views contain only authorized, redacted diagnostic context. Supervisors see impact and escalation state. Administrators receive operational details through a protected channel. The application enforces RBAC; a request parameter cannot grant a privileged view.

## Retry rule

Retry only when the failure is transient **and** the operation is idempotent or protected by a valid idempotency key. Bound attempts, use exponential backoff with jitter, honor `Retry-After`, and account for cancellation/deadlines. A status code by itself is not sufficient evidence to retry.
