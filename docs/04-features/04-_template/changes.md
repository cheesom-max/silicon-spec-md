---
doc_type: reference
status: draft
owner: feature-authors
audience: feature-authors-reviewers
last_reviewed: 2026-03-18
canonical: false
supersedes: none
---

# Feature Changes Template

## Purpose
- Record a chronological change history for this feature package.

## Usage Order
- Update whenever feature-package documents change in a way others must track.
- Add one dated entry per meaningful package change; keep entries append-only.

## Intended Audience
- Contributors and reviewers needing a concise, dated history of feature-package updates.

## Out of Scope
- Canonical behavior ownership.
- ADR lifecycle policy.
- Runbook ownership.
- Repository-wide governance policy.

## Canonical Scope
- Date-stamped change entries scoped to this feature package.
- Links to authoritative docs where decisions and behavior are owned.
- Rollout chronology and evidence pointers for this feature package only.

## Canonical Links
- Canonical behavior and acceptance owner: `docs/04-features/<feature>/04-spec.md`.
- Governance workflow and evidence rules: `docs/08-document-operations.md`.
- ADR lifecycle and decision registry: `docs/06-adrs/06-ADR-INDEX.md`.
- Operational runbook registry: `docs/07-runbooks/07-INDEX.md`.

## Semantics and Ownership Boundaries
- `changes.md` is a chronology document for this feature package.
- Architecture decisions are owned by ADRs and must be linked, not redefined here.
- Operational procedures are owned by runbooks and must be linked, not duplicated here.
- If a change alters behavior expectations, update `04-spec.md` first and then append the chronology entry here.

## Change Log
- YYYY-MM-DD: change summary; affected docs; linked evidence path.

## Last Updated When
- When any meaningful feature-package update should be traceable in history.
