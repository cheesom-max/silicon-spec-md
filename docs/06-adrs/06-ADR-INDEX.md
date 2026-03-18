---
doc_type: reference
status: active
owner: architecture-and-docs-governance
audience: contributors-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# ADR Index

## Purpose
- Provide the canonical index for architecture decision records (ADRs).

## Usage Order
- Read before creating or updating an ADR.
- Update this index whenever an ADR is added, renamed, deprecated, or superseded.

## Intended Audience
- Contributors, reviewers, and AI agents navigating architecture decisions.

## Out of Scope
- Decision rationale details (owned by each ADR).
- Operational execution steps (owned by runbooks).

## Canonical Scope
- Canonical ADR list and lifecycle state tracking.
- File naming and status conventions for ADR records.

## Last Updated When
- Any ADR lifecycle state changes (`proposed`, `accepted`, `deprecated`, `superseded`).
- ADR files are added, renamed, or supersession relations change.

## Canonical Links
- ADR template: `docs/06-adrs/06-ADR-0000-template.md`.
- Runbook index: `docs/07-runbooks/07-INDEX.md`.
- Feature-package chronology template: `docs/04-features/04-_template/changes.md`.

## Naming and Status Rules
- ADR files use `docs/06-adrs/06-ADR-xxxx-title.md`.
- ADR statuses are restricted to `proposed`, `accepted`, `deprecated`, `superseded`.
- `superseded` ADRs must reference the replacing ADR in their `Supersession` section.

## Canonical Entries
| ADR | Title | Status | Canonical Path | Notes |
|---|---|---|---|---|
| ADR-0000 | ADR template | proposed | `docs/06-adrs/06-ADR-0000-template.md` | Template for new ADR authoring and lifecycle fields |
