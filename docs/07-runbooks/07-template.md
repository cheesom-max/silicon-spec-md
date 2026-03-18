# Runbook Template

## Purpose
- Provide a repeatable operational procedure that can be executed under normal conditions or incident pressure.

## Usage Order
- Step 9: add a runbook when repeatable execution steps are required.
- Keep runbooks procedural and operational, not tutorial-like.

## Intended Audience
- The people who actually carry out the procedure during normal operation or under pressure.

## Out of Scope
- Product planning.
- Architectural decision rationale.
- Repository-wide engineering policy.
- Long-form troubleshooting theory or conceptual onboarding.

## Canonical Scope
- Trigger conditions.
- Preconditions.
- Signals to watch.
- Execution steps.
- Verification, recovery, and escalation.

## Last Updated When
- When the operational procedure changes, a tool changes, or real execution exposes a gap.

## Canonical Links
- Runbook index: `docs/07-runbooks/07-INDEX.md`.
- ADR index: `docs/06-adrs/06-ADR-INDEX.md`.
- Feature package chronology: `docs/04-features/<feature>/changes.md`.

## Trigger
- What event or condition requires using this runbook?

## Preconditions
- What conditions must be satisfied before execution?

## Required Access and Tools
- List the required accounts, permissions, dashboards, and commands.

## Signals to Watch
- Which leading indicators confirm the procedure is on track?
- Which failure signals require rollback, recovery, or escalation?

## Execution Metadata
- What environment or scope does this procedure apply to?
- What baseline state must be recorded before execution?
- What evidence must be captured during and after execution?

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
- If follow-up changes are needed, which documents must also be updated? Example: feature spec, ADR, and `changes.md`.
