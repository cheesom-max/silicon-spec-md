---
doc_type: governance
status: active
owner: docs-governance
audience: documentation-contributors-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Documentation Glossary

## Purpose
- Define a controlled vocabulary for documentation operations used by humans and AI agents.
- Reduce ambiguity in doc metadata, review gates, and ownership decisions.

## Usage Order
- Step 0: Read when authoring metadata, review outcomes, or governance workflow updates.

## Intended Audience
- Documentation contributors, reviewers, maintainers, and AI agents.

## Out of Scope
- Product behavior definitions.
- System architecture design details.
- Feature-specific acceptance criteria.

## Canonical Scope
- Controlled vocabulary for `doc_type`, `status`, and core governance terms.
- Allowed meanings used across numbered governance docs.

## Canonical Links
- `docs/00-README.md` for document map and ownership boundaries.
- `docs/08-document-operations.md` for the deterministic contributor workflow and review gates.

## Metadata Vocabulary
### `doc_type`
- `governance`: repository-wide policy, ownership, or process control documents.
- `feature-spec`: canonical feature behavior and acceptance criteria under `docs/04-features/<feature>/04-spec.md`.
- `adr`: architecture decision records under `docs/06-adrs/`.
- `runbook`: repeatable operational procedures under `docs/07-runbooks/`.
- `reference`: supporting explanation or reference material that does not own policy.

### `status`
- `draft`: active authoring or review is in progress; facts are not final.
- `active`: approved for current use and subject to freshness SLA.
- `deprecated`: still usable for transition but should not be used for new work.
- `archived`: retained for history; excluded from recurring freshness checks unless referenced by active docs.

## Core Governance Terms
- `canonical document`: the single source of truth for a durable fact.
- `canonical-doc impact`: explicit list of canonical docs affected by a change, including `none` when no canonical doc is affected.
- `subject-matter review`: factual and domain-correctness gate.
- `docs-structure review`: ownership-boundary and link-integrity gate.
- `freshness review`: recency gate for `last_reviewed` and `status` against SLA.
- `evidence file`: task-scoped artifact under `.sisyphus/evidence/` containing commands and exact outcomes.
- `cross-cutting change`: update that affects multiple canonical boundaries and may require an ADR.

## Authoring Rules for Vocabulary
- Use glossary terms exactly as defined in this file.
- Prefer explicit term reuse over synonyms in governance docs.
- Add new controlled terms only when existing terms cannot represent the concept.
- If a new term changes ownership boundaries or lifecycle behavior, update `docs/08-document-operations.md` in the same change.

## Last Updated When
- A new controlled term is added, removed, renamed, or its meaning changes.
