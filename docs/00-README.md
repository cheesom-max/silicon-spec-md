---
doc_type: governance
status: active
owner: docs-governance
audience: contributors-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Document Map

## Purpose
- Guide AI agents and human readers to the correct document.
- Define which file is canonical for each concern.
- Lock the layered documentation taxonomy and governance control plane.

## Usage Order
- Step 0: Read this document first to understand the overall document structure and writing order.

## Intended Audience
- Anyone writing, reviewing, or implementing specs in this repository.

## Out of Scope
- Detailed product requirements.
- Architecture explanations.
- Coding rules.
- Feature-level decisions.

## Canonical Scope
- The document map for this repository.
- The overall reading order and ownership boundaries across the docs set.

## Canonical Links
- This document points to the canonical documents listed below.

## Canonical Documents
| Concern | Canonical File | Notes |
|---|---|---|
| Product intent | `docs/01-product.md` | Problem, users, goals, non-goals, success metrics |
| System shape | `docs/02-system-architecture.md` | Components, boundaries, flows, constraints |
| Repository-wide engineering rules | `docs/03-engineering-rules.md` | Invariants, required patterns, forbidden patterns |
| Feature behavior and acceptance criteria | `docs/04-features/<feature>/04-spec.md` | Start from `docs/04-features/04-_template/04-spec.md` |
| Documentation operations model | `docs/08-document-operations.md` | Loop cadence, roles, quality bars, WIP limits, freshness SLA |
| Documentation controlled vocabulary | `docs/09-glossary.md` | Controlled terms for metadata, statuses, and governance language |
| Documentation migration map | `docs/migration-map.md` | Path-level record of created/moved/renamed/deleted items during IA overhaul |
| Architectural decisions | `docs/06-adrs/06-ADR-xxxx-title.md` | Copy `docs/06-adrs/06-ADR-0000-template.md` to start |
| Operational response | `docs/07-runbooks/07-<name>.md` | Copy `docs/07-runbooks/07-template.md` to start |
| Test expectations | `docs/05-test-strategy.md` | Project-level quality strategy |

## Layered Taxonomy Model
### Layer 1: Governance Control Plane
- Numbered canonical governance docs (`docs/01` to `docs/09`) own durable policy and decision boundaries.

### Layer 2: Delivery Package Taxonomy
- Each feature package under `docs/04-features/<feature>/` separates concept, procedure, reference, examples, change history, and known issues.
- `04-spec.md` remains canonical for feature behavior and acceptance criteria.
- Non-canonical sibling docs must link to canonical governance docs instead of duplicating policy.

## Default Writing Order
1. Write `docs/01-product.md`.
2. Write `docs/02-system-architecture.md`.
3. Write `docs/03-engineering-rules.md`.
4. Whenever a feature starts, write `docs/04-features/<feature>/04-spec.md`.
5. Write `docs/05-test-strategy.md` when project-wide verification principles are needed.
6. Write or update `docs/08-document-operations.md` when governance loop policy changes.
7. Write or update `docs/09-glossary.md` when controlled vocabulary changes.
8. Add an ADR when a long-lived technical decision appears.
9. Add a runbook when a repeatable operational procedure is needed.

## Reading Order
1. Read `docs/09-glossary.md` for canonical governance vocabulary.
2. Read `docs/01-product.md` to understand product intent.
3. Read `docs/02-system-architecture.md` to understand the technical context.
4. Read `docs/03-engineering-rules.md` to understand repository-wide rules.
5. Read `docs/05-test-strategy.md` and `docs/08-document-operations.md` for verification and loop policy.
6. Then read the relevant feature spec, ADR, and runbook documents.

## Update Order Principles
1. If product intent changes, update `docs/01-product.md` first.
2. If the stable technical structure changes, update `docs/02-system-architecture.md`.
3. If repository-wide rules change, update `docs/03-engineering-rules.md`.
4. Before implementing a feature, create or update its feature spec.
5. If loop cadence, review roles, WIP limits, or freshness policy changes, update `docs/08-document-operations.md`.
6. Add an ADR when a lasting architectural decision appears.
7. Add or update a runbook when a repeatable operational procedure is needed.

## Writing Rules
- Every document starts with `Purpose`, `Usage Order`, `Intended Audience`, `Out of Scope`, `Canonical Scope`, and `Last Updated When`.
- Include `Canonical Links` near the top of each document.
- Re-explain content only when local context is truly necessary; otherwise link first.
- Keep facts with a clear single owner only in that owner document and link from others.
- If a section could be copied verbatim into another document, delete it and replace it with a link.
- Canonical governance documents are written in English.

## Last Updated When
- When canonical documents are added, removed, renamed, or their ownership boundaries change.
