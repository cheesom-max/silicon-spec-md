---
doc_type: governance
status: active
owner: docs-governance
audience: documentation-maintainers-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Documentation Operations

## Purpose
- Define the docs-system architecture and operating loop for this repository.
- Keep governance quality consistent for AI agents and human readers.

## Usage Order
- Step 0: Read after `docs/05-test-strategy.md` when planning or reviewing documentation changes.

## Intended Audience
- Documentation maintainers, spec authors, reviewers, and AI agents.

## Out of Scope
- Product requirements ownership (owned by `docs/01-product.md`).
- System architecture ownership (owned by `docs/02-system-architecture.md`).
- Repository-wide engineering rules ownership (owned by `docs/03-engineering-rules.md`).
- Feature behavior ownership (owned by `docs/04-features/<feature>/04-spec.md`).
- Building a docs website or external hosted docs platform.

## Canonical Scope
- Documentation operating model for the docs system.
- Documentation operating loop cadence, review roles, quality bars, WIP limits, evidence paths, freshness SLA, and stop conditions.

## Canonical Links
- `docs/00-README.md` for document map and ownership table.
- `docs/03-engineering-rules.md` for repository-wide constraints.
- `docs/05-test-strategy.md` for verification strategy expectations.

## Docs-System Operating Model
### Layer 1: Governance Control Plane
- Numbered governance documents in `docs/01` to `docs/09` define canonical policy and ownership boundaries.
- Canonical governance content is written in English.

### Layer 2: Delivery Package Taxonomy
- Feature packages under `docs/04-features/<feature>/` separate concept, procedure, reference, examples, change history, and known issues.
- `04-spec.md` remains the canonical owner of feature behavior and acceptance criteria.

## Validation Runtime and Non-Goals
- Validation runtime is `python3 standard library` only.
- No package-manager dependency is introduced only for docs validation.
- No static-site generator or docs website requirement is introduced by this governance layer.
- No external hosted docs dependency is required.

## Loop Cadence and Workflow
### Cadence
- Continuous updates happen per merged documentation change.
- Weekly review checks canonical ownership drift and link hygiene.
- Monthly freshness sweep checks stale-document risk against SLA thresholds.

### Contributor Workflow (Deterministic)
1. Intake issue or need with a one-line problem statement and expected document outcome.
2. Select the canonical target document first, then list impacted non-canonical docs.
3. Flag ADR requirement when change is cross-cutting, long-lived, or alters decision boundaries.
4. Implement updates in canonical docs first, then propagate links and local context updates.
5. Run required validators and capture exact command output in evidence.
6. Update changelog or runbook references when contributor-facing behavior or operating steps change.
7. Complete review gates in order: subject-matter review -> docs-structure review -> freshness review.
8. Close the cycle only after stop conditions are met and no freshness breach remains.

### Entry Criteria
- A concrete issue or need is documented.
- Proposed canonical doc owner is identified before editing.
- Impacted canonical docs are listed, even when the list is empty (`none`).

### Evidence Update Rules
- Evidence file path follows `.sisyphus/evidence/task-<n>-<slug>.txt`.
- Evidence must include validator commands, terminal output, and explicit pass/fail status.
- If a review gate rejects the change, append remediation notes and rerun evidence capture.
- Evidence is updated on every revision round; do not reuse stale outputs.

### Freshness Review Cadence
- Freshness review occurs during every merge cycle for touched active docs.
- Weekly sweep checks docs nearing SLA breach within 7 days.
- Monthly sweep reconciles overdue items and records correction actions.
- Release-triggered impact sweep checks docs touched by a release-facing change before the release is considered complete.

### Review Gates
1. Gate A - Canonical impact gate
   - Confirm canonical-doc impact identification is complete for changed scope.
   - Confirm selected canonical owner is not duplicated elsewhere.
2. Gate B - subject-matter review
   - Verify domain correctness and factual integrity.
   - Record explicit approval or required corrections.
3. Gate C - Docs-structure review
   - Verify ownership boundaries, link integrity, and index reachability.
   - Verify validators pass for the changed scope.
4. Gate D - Freshness review
   - Verify `last_reviewed` recency and status alignment with SLA.
   - Confirm no affected active doc remains past freshness policy.

## Review Roles
- Subject-matter review: verifies factual and domain correctness.
- Docs-structure review: verifies canonical ownership boundaries and link integrity.
- Freshness review: verifies review-date and status recency against SLA.

## Quality Bars
- Canonical ownership is singular for each durable fact.
- Reading order and writing order remain coherent with `docs/00-README.md`.
- Changes are reproducible from evidence artifacts, not informal approval text.
- Language policy remains English for canonical governance docs.

## WIP Limits
- Maximum open documentation changes per reviewer: 3.
- Maximum concurrent governance changes touching numbered canonical docs: 2.
- Enforce max WIP before starting additional documentation changes.
- New work is deferred when limits are exceeded until at least one item is closed.

## Evidence Paths
- Store cycle evidence under `.sisyphus/evidence/`.
- Use task-scoped files such as `.sisyphus/evidence/task-<n>-<slug>.txt`.
- Evidence must include executed commands and observed pass/fail outcomes.

## Freshness SLA
- `doc_type: governance`, `status: active`: review every 30 days.
- `doc_type: governance`, `status: draft`: review every 14 days.
- `doc_type: feature-spec`, `status: active`: review every 30 days.
- `doc_type: feature-spec`, `status: draft`: review every 14 days.
- `doc_type: adr`, `status: active`: review every 60 days.
- `doc_type: adr`, `status: draft`: review every 30 days.
- `doc_type: runbook`, `status: active`: review every 30 days.
- `doc_type: runbook`, `status: draft`: review every 14 days.
- `doc_type: reference`, `status: active`: review every 60 days.
- `doc_type: reference`, `status: draft`: review every 30 days.
- `status: deprecated`: review every 30 days regardless of `doc_type`.
- `status: archived`: exempt from recurring freshness review unless referenced by active docs.

## Stop Conditions
- Required validation commands for the cycle pass.
- No unresolved canonical ownership conflicts remain.
- Evidence file exists for the cycle and includes validation output.
- No freshness SLA breach remains for affected active documents.
- Documentation cycle must stop when green after all required gates pass.

## Last Updated When
- Loop policy, cadence, review roles, WIP limits, evidence path conventions, or freshness SLA changes.
