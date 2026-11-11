# Runbook review checklist

The skill should locate and assess the target project's runbooks; this repository does not prescribe infrastructure-specific recovery actions.

For each high-impact error, check that an authorized operator can find:

- Stable error code, owning team, severity, and escalation thresholds.
- Affected dependency/service and safe health checks.
- User impact and approved public status message.
- Correlation/trace lookup steps and log redaction expectations.
- Recovery, rollback, and communication steps with role boundaries.
- Retry guidance, idempotency requirements, `Retry-After`, and stop conditions.
- Last review date and a test or exercise that validates the procedure.

Never invent production commands, URLs, or access requirements absent from project documentation.
