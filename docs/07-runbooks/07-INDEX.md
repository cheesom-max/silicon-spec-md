---
doc_type: reference
status: active
owner: operations-and-docs-governance
audience: operators-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Runbook Index

## Purpose
- Provide the canonical index for operational runbooks.

## Usage Order
- Read before creating or executing a runbook.
- Update this index whenever a runbook is added, renamed, or retired.

## Intended Audience
- Operators, responders, reviewers, and AI agents executing operational procedures.

## Out of Scope
- Architecture decision rationale (owned by ADRs).
- Feature behavior acceptance criteria (owned by feature specs).

## Canonical Scope
- Canonical runbook list and ownership metadata.
- Minimum section requirements for operational readiness.

## Last Updated When
- A canonical runbook entry is added, renamed, or retired.
- Runbook section requirements change.

## Canonical Links
- Runbook template: `docs/07-runbooks/07-template.md`.
- ADR index: `docs/06-adrs/06-ADR-INDEX.md`.
- Feature-package chronology template: `docs/04-features/04-_template/changes.md`.

## Required Sections for Every Runbook
- `Trigger`
- `Preconditions`
- `Required Access and Tools`
- `Signals to Watch`
- `Procedure`
- `Verification`
- `Rollback or Recovery`
- `Escalation`

## Canonical Entries
| Runbook | Purpose | Canonical Path | Notes |
|---|---|---|---|
| runbook-template | Operational procedure template | `docs/07-runbooks/07-template.md` | Includes required trigger, signals, rollback/recovery, and escalation sections |
