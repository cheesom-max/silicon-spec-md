# Document Map

## Purpose
- Guide readers and AI agents to the correct numbered document.
- Define canonical ownership for the numbered docs set.
- Define the official reading, writing, and update order for the numbered docs set.

## Usage Order
- Step 0: Read this document first.
- Then follow the `Reading Order` section below.

## Intended Audience
- Anyone writing, reviewing, or implementing specs in this repository.

## Out of Scope
- GitHub landing-page copy in `README.md`.
- Agent-specific operating rules in `AGENTS.md`.
- Detailed product requirements.
- Architecture explanations.
- Coding rules.
- Feature-level decisions.

## Canonical Scope
- The document map for this repository.
- Ownership boundaries across the numbered docs set.
- The official reading, writing, and update order for the numbered docs set.

## Canonical Links
- For the public repository entry point, see `README.md`.
- For agent operating rules, see `AGENTS.md`.

## Canonical Numbered Documents
| Concern | Canonical File | Use this when | Do not put here |
|---|---|---|---|
| Document system and ownership map | `docs/00-README.md` | You need the official docs map, ownership boundaries, or document order | Product decisions, architecture detail, or agent-only workflow rules |
| Product intent | `docs/01-product.md` | You need the problem, users, goals, non-goals, themes, or success metrics | Feature-local behavior or implementation detail |
| System shape | `docs/02-system-architecture.md` | You need components, boundaries, flows, dependencies, or stable constraints | Product strategy or step-by-step operational procedures |
| Repository-wide engineering rules | `docs/03-engineering-rules.md` | You need required patterns, forbidden patterns, naming rules, or review expectations | Product intent or full architectural rationale |
| Feature behavior and acceptance criteria | `docs/04-features/<feature>/04-spec.md` | You need feature scope, behavior, local design notes, or verification plans | Global architecture or repo-wide policy |
| Test expectations | `docs/05-test-strategy.md` | You need project-level risk, verification evidence, or exit criteria | Feature-specific behavior or incident procedures |
| Architectural decisions | `docs/06-adrs/06-ADR-xxxx-title.md` | You need the context, decision, and consequences for one durable technical choice | Always-current architecture summaries |
| Operational response | `docs/07-runbooks/07-<name>.md` | You need a repeatable operational procedure with verification and recovery steps | Product planning or broad engineering policy |

## Default Writing Order
1. Write `docs/01-product.md`.
2. Write `docs/02-system-architecture.md`.
3. Write `docs/03-engineering-rules.md`.
4. Whenever a feature starts, write `docs/04-features/<feature>/04-spec.md`.
5. Write `docs/05-test-strategy.md` when project-wide verification principles are needed.
6. Add an ADR when a long-lived technical decision appears.
7. Add a runbook when a repeatable operational procedure is needed.

## Reading Order
1. Read `docs/00-README.md` to understand the document system and ownership boundaries.
2. Read `docs/01-product.md` to understand product intent.
3. Read `docs/02-system-architecture.md` to understand the technical context.
4. Read `docs/03-engineering-rules.md` to understand repository-wide rules.
5. Then read the relevant feature spec, test strategy, ADR, and runbook documents.

## Update Order Principles
1. If document ownership, reading order, or canonical paths change, update `docs/00-README.md` first.
2. After that, update only the short pointers in `README.md` and `AGENTS.md`; do not mirror full ownership tables, full reading-order lists, or full update-order guidance there.
3. If product intent changes, update `docs/01-product.md` first.
4. If the stable technical structure changes, update `docs/02-system-architecture.md`.
5. If repository-wide rules change, update `docs/03-engineering-rules.md`.
6. Before implementing a feature, create or update its feature spec.
7. Add an ADR when a lasting architectural decision appears.
8. Add or update a runbook when a repeatable operational procedure is needed.

## Writing Rules
- Every numbered document starts with `Purpose`, `Usage Order`, `Intended Audience`, `Out of Scope`, `Canonical Scope`, and `Last Updated When`.
- Include `Canonical Links` near the top of each numbered document.
- Keep facts with a clear single owner only in that owner document and link from others.
- Re-explain content only when local context is truly necessary; otherwise link first.
- `README.md` may summarize and link, but it is not the canonical owner of numbered-doc ownership or reading order.
- `AGENTS.md` may point here for document ownership and document order, but it must not mirror the full ownership table, full reading-order list, or full update-order guidance.
- If a section could be copied verbatim into another document, delete it and replace it with a link.

## Last Updated When
- When canonical numbered documents are added, removed, renamed, or their ownership boundaries change.
