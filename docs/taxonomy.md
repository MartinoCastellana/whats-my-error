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

Audience views are projections of one event, not mutually exclusive categories. Every error must be mapped to an existing authorized technician/operator or administrator path; record evidence of where it is handled. If no such route is found, report a routing gap rather than pretending it exists. Preserve any additional levels actually implemented. User messages stay concise and safe; never send raw errors, technical codes, exception details, or diagnostic logs to the user. Support messages include stable codes and correlation references. Technical views contain authorized, redacted diagnostic context. Supervisors see impact/escalation state. Administrators receive operational details through a protected channel. The application enforces RBAC; a request parameter cannot grant a privileged view.

Every mapped user-visible outcome should have a plain message. Prefer concise success confirmation only when success is established (for example, “Sent successfully.”). For a failure, use a safe actionable message such as “Please check the highlighted information” or a neutral fallback such as “We couldn't complete this request. Please try again later.” If the existing software lacks one, draft it in the report in the application's locale and label it as proposed. Do not write it into source code under the read-only skill. If implementation guidance is requested, provide a separate snippet idiomatic to the discovered language/framework.

## User-facing code groups

When one function has many detailed codes, group them only when the same user message and action apply. Keep a complete mapping from each original code and source location to the user-facing group. For example, several field-level validation codes may map to `INPUT_INVALID`; expired and missing credentials may map to `SESSION_REQUIRED`; upstream timeout and outage codes may map to `SERVICE_TEMPORARY` if the user action is the same. Preserve distinct groups when actions differ. Grouping changes presentation only: it must not alter application functions or behavior, and it must not hide detailed codes from authorized technical/support views.

## Role index

Inspect actual role declarations and enforcement: role enums/constants, `isUser`/`isOperator`/`isAdmin`-style predicates, `hasRole` checks, middleware, decorators, route guards, policies, and protected UI/API paths. Produce a role-to-error index mapping each observed role to detailed codes and user-facing groups that can reach it, citing source locations and confidence. Keep role names and hierarchy as implemented. A symbol's name alone is not proof of authorization; when enforcement cannot be traced, mark visibility unknown for review. Do not assume an administrator can see every error or expose privileged details in a user view.

## Cross-file identity and centralized log

Trace the same failure across client, API, backend, and provider boundaries. Use one canonical `error_id` for the same underlying error, for example `WME-PAYMENT-UPSTREAM-TIMEOUT`, and map local codes (`DIO_CONNECTION_TIMEOUT`, `PAYMENT_API_504`, PHP exception class/code) as aliases. Do not replace the canonical ID at each layer. Preserve a validated correlation ID for the request and a valid trace ID when available; mark broken/missing propagation rather than guessing.

When authorized to write analysis artifacts, consolidate the map into structured records conforming to `schemas/error-log.schema.json`. Timestamp each observation with an ISO 8601 UTC `occurred_at`, and include service/layer, operation, source location, canonical ID, local alias, severity, audience/role, correlation/trace identifiers, evidence, and redaction status. These are analysis logs/reports, not runtime logs: do not edit application functions or add runtime logging code under this read-only skill. If file output is unavailable or not authorized, return the same records in the answer and explicitly say no log artifact was written.

## Retry rule

Retry only when the failure is transient **and** the operation is idempotent or protected by a valid idempotency key. Bound attempts, use exponential backoff with jitter, honor `Retry-After`, and account for cancellation/deadlines. A status code by itself is not sufficient evidence to retry.
