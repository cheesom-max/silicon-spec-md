---
doc_type: governance
status: active
owner: quality-and-docs-governance
audience: engineers-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Test Strategy

## Purpose
- Define the project-level quality and verification approach for documentation governance work.
- Specify deterministic evidence requirements for merge readiness.

## Usage Order
- Step 5: Read and update this document when defining or reviewing repository-wide verification requirements.
- Apply it to governance changes, feature-spec changes, and docs validation script updates.

## Intended Audience
- Engineers, maintainers, reviewers, and AI agents responsible for verification quality.

## Out of Scope
- Product intent and prioritization decisions (owned by `docs/01-product.md`).
- Architecture boundaries and component design (owned by `docs/02-system-architecture.md`).
- Repository-wide authoring rules and invariants (owned by `docs/03-engineering-rules.md`).
- Incident procedures and operational response runbooks (owned by `docs/07-runbooks/`).

## Canonical Scope
- Project-level verification model and required test levels.
- Quality-risk framing for documentation governance changes.
- Required command evidence and output contract for validators.
- Exit criteria that gate merge readiness.

## Last Updated When
- When validator command sets, evidence requirements, risk priorities, or exit criteria change.

## Canonical Links
- `docs/00-README.md` for canonical map and ownership boundaries.
- `docs/03-engineering-rules.md` for repository-wide required and forbidden patterns.
- `docs/08-document-operations.md` for review cadence and loop stop conditions.
- Relevant `docs/04-features/<feature>/04-spec.md` file for feature-level acceptance checks.

## Scope
- This strategy covers all numbered governance docs under `docs/` and docs-validation scripts under `scripts/docs/`.
- It defines minimum verification evidence for documentation governance changes.
- It applies to both human-authored and AI-authored documentation changes.

## Risk Areas
- Canonical ownership drift where a durable fact appears in multiple governance docs.
- Missing or malformed YAML metadata that breaks freshness and ownership checks.
- Broken canonical links that disconnect readers from source-of-truth documents.
- Validator regressions that produce non-deterministic output and block auditability.

## Test Levels
- Static docs validators (`python3`, standard library only).
- Cross-document ownership and link integrity checks.
- Manual review for policy clarity when validator failures indicate ambiguous ownership.
- Direct file review of changed governance docs when markdown LSP diagnostics are unavailable.

## Core Scenarios
- A governance doc update preserves all required sections and metadata keys.
- Ownership-sensitive changes fail when canonical boundaries are violated.
- Link-sensitive changes fail when canonical references are broken or missing.
- Validator contract remains stable: deterministic pass/fail lines and file-specific failures.

## Environments and Fixtures
- Local repository checkout with python3 available on `PATH`.
- No network dependency for validator execution.
- Test fixtures are the markdown docs under `docs/` and validator scripts under `scripts/docs/`.
- Evidence artifacts stored under `.sisyphus/evidence/`.

## Verification Evidence Expectations
- Save validation evidence under `.sisyphus/evidence/`.
- Use task-scoped files named `.sisyphus/evidence/task-<n>-<slug>.txt`.
- Evidence must include executed commands and exact terminal output.
- Docs validators must follow this exact terminal contract:
  - Pass output: `PASS: 0 failures`
  - Fail output first line: `FAIL: <n> failures`
  - Fail detail lines: one line per failure, prefixed with `- ` and including file path.
- Required docs validation command set:
  - `python3 scripts/docs/test_required_sections.py`
  - `python3 scripts/docs/test_canonical_ownership.py`
  - `python3 scripts/docs/test_links.py`
  - `python3 scripts/docs/test_taxonomy_coverage.py`
  - `python3 scripts/docs/test_metadata_freshness.py`
  - `python3 scripts/docs/test_orphans.py`
  - `python3 scripts/docs/test_migration_map.py`

## Exit Criteria
- All required docs validation commands pass and end with `PASS: 0 failures`.
- Evidence file exists in `.sisyphus/evidence/` for the change.
- No unresolved canonical ownership conflict remains in changed documents.
- Changed governance docs include required metadata keys and canonical links.

## Operational Signals and Rollback Checks
- Signal: validator output contract changes unexpectedly (missing pass/fail prefix).
- Signal: ownership or required-section checks fail on untouched files after a targeted change.
- Abnormal standard: any non-deterministic or non-path-specific failure messaging is treated as a verification defect.
- Rollback trigger: governance edits introduce cross-doc ownership conflicts that cannot be resolved within the current change scope.
- Follow-up trigger: known validator gaps discovered during review are logged and tracked before merge.

## Gaps and Exceptions
- Known gaps must be listed in evidence with owning reviewer and remediation target date.
- Exceptions to required validator execution are temporary and require explicit approval rationale.
- Exceptions do not waive canonical ownership rules; they only defer specific verification mechanics.
