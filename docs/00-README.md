# Document Map

## Purpose
- Guide readers and AI agents to the correct document.
- Define which file is canonical for each concern.

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
| Architectural decisions | `docs/06-adrs/06-ADR-xxxx-title.md` | Copy `docs/06-adrs/06-ADR-0000-template.md` to start |
| Operational response | `docs/07-runbooks/07-<name>.md` | Copy `docs/07-runbooks/07-template.md` to start |
| Test expectations | `docs/05-test-strategy.md` | Project-level quality strategy |

## Default Writing Order
1. Write `docs/01-product.md`.
2. Write `docs/02-system-architecture.md`.
3. Write `docs/03-engineering-rules.md`.
4. Whenever a feature starts, write `docs/04-features/<feature>/04-spec.md`.
5. Write `docs/05-test-strategy.md` when project-wide verification principles are needed.
6. Add an ADR when a long-lived technical decision appears.
7. Add a runbook when a repeatable operational procedure is needed.

## Reading Order
1. Read `docs/01-product.md` to understand product intent.
2. Read `docs/02-system-architecture.md` to understand the technical context.
3. Read `docs/03-engineering-rules.md` to understand repository-wide rules.
4. Then read the relevant feature spec, ADR, runbook, and test strategy documents.

## Update Order Principles
1. If product intent changes, update `docs/01-product.md` first.
2. If the stable technical structure changes, update `docs/02-system-architecture.md`.
3. If repository-wide rules change, update `docs/03-engineering-rules.md`.
4. Before implementing a feature, create or update its feature spec.
5. Add an ADR when a lasting architectural decision appears.
6. Add or update a runbook when a repeatable operational procedure is needed.

## Writing Rules
- Every document starts with `Purpose`, `Usage Order`, `Intended Audience`, `Out of Scope`, `Canonical Scope`, and `Last Updated When`.
- Include `Canonical Links` near the top of each document.
- Re-explain content only when local context is truly necessary; otherwise link first.
- Keep facts with a clear single owner only in that owner document and link from others.
- If a section could be copied verbatim into another document, delete it and replace it with a link.

## Last Updated When
- When canonical documents are added, removed, renamed, or their ownership boundaries change.
