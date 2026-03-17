# Runbook Template

## Purpose
- Provide a repeatable operational procedure for a specific task or incident.

## Usage Order
- Step 7: Write this when a repeatable operational procedure is needed.
- Use it for work where real execution order matters, such as deploys, incident response, or recovery.

## Intended Audience
- The people who actually carry out the procedure during normal operation or under pressure.

## Out of Scope
- Product planning.
- Architectural decision rationale.
- Repository-wide engineering policy.
- Long-form troubleshooting theory.

## Canonical Scope
- Trigger conditions.
- Preconditions.
- Execution steps.
- Verification, recovery, and escalation.

## Last Updated When
- When the operational procedure changes, a tool changes, or real execution exposes a gap.

## Canonical Links
- Link the related ADR, feature spec, dashboard, and architecture docs.

## Trigger
- What event or condition requires using this runbook?

## Preconditions
- What conditions must be satisfied before execution?

## Required Access and Tools
- List the required accounts, permissions, dashboards, and commands.

## Execution Metadata
- What environment or scope does this procedure apply to?
- What baseline state must be recorded before execution?
- What signals must be checked during execution?

## Procedure
1. First step.
2. Second step.
3. Continue until the work is complete.

## Verification
- How do you confirm the procedure succeeded?

## Rollback or Recovery
- What should be done if the procedure fails or must be undone?

## Escalation
- When should it be escalated, to whom, and with what information?

## Operational Feedback Loop
- What observations must be recorded after running this runbook?
- What repeated failure patterns should trigger a document or procedure update?
- If follow-up changes are needed, which documents must also be updated? Example: feature spec, ADR, test strategy.
