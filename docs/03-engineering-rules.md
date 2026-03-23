---
doc_type: governance
status: active
owner: engineering-governance
audience: engineers-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Engineering Rules

## Purpose
- Define repository-wide engineering invariants and conventions for docs-first work.
- Provide enforceable rules that keep canonical ownership stable across contributors.

## Usage Order
- Step 3: Read and update this document after product and architecture docs are stable.
- Apply these rules to all governance, feature-spec, and validator changes.

## Intended Audience
- Engineers, documentation maintainers, reviewers, and AI agents editing repository content.

## Out of Scope
- Product goals, users, and success outcomes (owned by `docs/01-product.md`).
- System architecture and component boundaries (owned by `docs/02-system-architecture.md`).
- Project-level verification strategy and risk model (owned by `docs/05-test-strategy.md`).
- Loop cadence and review-role operations policy (owned by `docs/08-document-operations.md`).

## Canonical Scope
- Required and forbidden repository-wide authoring patterns.
- Naming, path, and structural rules for canonical docs.
- Enforcement rules for metadata, ownership, and deterministic validation behavior.
- Exception-handling policy for rule deviations.

## Last Updated When
- When repository-wide conventions, invariants, or enforcement requirements change.

## Canonical Links
- `docs/00-README.md` for canonical map and ownership table.
- `docs/02-system-architecture.md` for architecture boundaries.
- `docs/05-test-strategy.md` for verification strategy and exit criteria.
- `docs/08-document-operations.md` for operational loop policy and review workflow.

## Design Principles
- Keep one canonical owner for every durable fact.
- Keep governance documents in English.
- Keep docs validation deterministic and runnable with `python3` standard library only.

## Required Patterns
- Substantive docs (non-template documents that define active policy, behavior, or operations) must start with YAML front matter.
- Required YAML keys for substantive docs:
  - `doc_type`
  - `status`
  - `owner`
  - `audience`
  - `last_reviewed`
  - `canonical`
  - `supersedes`
- `last_reviewed` format must be `YYYY-MM-DD`.
- `canonical` must be `true` for canonical owner docs and `false` for supporting docs.
- `supersedes` must be `none` or a repository path to replaced canonical content.
- Substantive docs must include these sections exactly once:
  - `## Purpose`
  - `## Usage Order`
  - `## Intended Audience`
  - `## Out of Scope`
  - `## Canonical Scope`
  - `## Last Updated When`
  - `## Canonical Links`

## Forbidden Patterns
- Duplicating durable facts across multiple canonical docs.
- Claiming docs validation requires a package manager, external service, or third-party Python package.
- Omitting required metadata keys on substantive docs.
- Storing unresolved policy placeholders such as `TBD`, `TODO`, or question-only section bodies in active governance docs.

## Naming and Structure Rules
- Preserve numbered canonical file paths under `docs/`.
- Keep feature specs under `docs/04-features/<feature>/04-spec.md`.
- Keep ADRs under `docs/06-adrs/06-ADR-xxxx-title.md`.
- Keep runbooks under `docs/07-runbooks/07-<name>.md`.
- Keep durable policy in numbered governance docs and use links from feature-package supporting files.

## Error Handling Rules
- Validation scripts fail fast with explicit, file-path-specific messages.
- Failures must identify the violated rule so remediation is deterministic.
- Review comments must reference canonical owner documents when reporting ownership drift.
- Silent failure handling is not allowed in governance validation scripts.

## Test Rules
- For docs validation, each script must print one deterministic terminal line:
  - pass: `PASS: 0 failures`
  - fail: `FAIL: <n> failures` followed by path-specific failure lines
- Validation scripts must resolve paths from repository root and produce file-path-specific failures.
- Project-level risk strategy and exit criteria belong in `docs/05-test-strategy.md`.
- Rule-only changes and content-only changes both require the same validator command set.

## Review Rules
- Required validators for docs governance changes must pass before review approval.
- Evidence must be captured at the path conventions defined in `docs/05-test-strategy.md` and `docs/08-document-operations.md`.
- Reviewers must reject changes that move canonical ownership without explicit boundary updates in the owning doc.

## Decision Heuristics
- If a statement can be true in only one governance domain, place it in that domain's canonical doc and link from others.
- If a rule affects all contributors regardless of feature, place it in this document.
- If a requirement can be machine-checked, encode it in a validator before adding manual review burden.
- If two docs appear to own the same fact, keep the stricter owner and replace the other with a link.

## Exceptions
- Exceptions must be explicit, time-bounded, and recorded in review evidence with rationale.
- Exception requests must include owning reviewer, expiration date, and rollback condition.
- Expired exceptions are treated as policy violations until renewed or removed.
