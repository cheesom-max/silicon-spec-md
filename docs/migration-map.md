---
doc_type: reference
status: active
owner: docs-governance
audience: documentation-maintainers-reviewers-ai-agents
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# Documentation Migration Map (T1-T7)

## Purpose
- Provide a factual path-level migration map for the documentation IA overhaul completed through T6 and integrated in T7.
- Record what was created and explicitly confirm where no move/rename/delete occurred.

## Usage Order
- Read after `docs/00-README.md` when validating path changes from the IA overhaul.
- Update this map before any future path rename, move, or removal.

## Intended Audience
- Documentation maintainers, reviewers, and AI agents verifying migration integrity.

## Out of Scope
- Defining future governance cadence updates (owned by `docs/08-document-operations.md`).
- Defining feature behavior or acceptance criteria (owned by `docs/04-features/<feature>/04-spec.md`).

## Canonical Scope
- Path-level migration facts for T1-T6 outputs.
- Replacement-path, rationale, status, and rollback notes for each migration category.

## Canonical Links
- Document map and ownership boundaries: `docs/00-README.md`.
- Documentation operations policy: `docs/08-document-operations.md`.
- Controlled vocabulary: `docs/09-glossary.md`.

## Migration Snapshot
- Scope baseline: pre-overhaul docs template set.
- Current snapshot: repository state after T1-T6 with T7 integration.
- Migration status: `active`.

## Category A: Created Paths
| Category | Source Path | Created Path | Replacement Path | Rationale | Status | Rollback Notes |
|---|---|---|---|---|---|---|
| governance | `none` | `docs/08-document-operations.md` | `N/A (new canonical file)` | Introduce canonical docs-operations loop ownership. | active | Remove links to this file, then delete file if governance lock is reverted. |
| governance | `none` | `docs/09-glossary.md` | `N/A (new canonical file)` | Add controlled vocabulary for metadata and governance terms. | active | Remove inbound links, then delete file if vocabulary control is reverted. |
| adr-index | `none` | `docs/06-adrs/06-ADR-INDEX.md` | `N/A (new canonical file)` | Centralize ADR discoverability and lifecycle indexing. | active | Restore direct ADR discovery without index, then remove file. |
| runbook-index | `none` | `docs/07-runbooks/07-INDEX.md` | `N/A (new canonical file)` | Centralize runbook discoverability and required-section governance. | active | Restore direct runbook discovery without index, then remove file. |
| feature-package | `none` | `docs/04-features/04-_template/concept.md` | `N/A (new support doc)` | Add domain framing sibling doc for feature package taxonomy. | active | Remove sibling link references and delete file. |
| feature-package | `none` | `docs/04-features/04-_template/how-to.md` | `N/A (new support doc)` | Add contributor procedure sibling doc for feature packages. | active | Remove sibling link references and delete file. |
| feature-package | `none` | `docs/04-features/04-_template/reference.md` | `N/A (new support doc)` | Add stable lookup sibling doc for feature packages. | active | Remove sibling link references and delete file. |
| feature-package | `none` | `docs/04-features/04-_template/examples.md` | `N/A (new support doc)` | Add worked examples sibling doc for feature packages. | active | Remove sibling link references and delete file. |
| feature-package | `none` | `docs/04-features/04-_template/changes.md` | `N/A (new support doc)` | Add chronology sibling doc for release-facing changes. | active | Remove sibling link references and delete file. |
| feature-package | `none` | `docs/04-features/04-_template/known-issues.md` | `N/A (new support doc)` | Add unresolved constraints sibling doc for feature packages. | active | Remove sibling link references and delete file. |
| validation | `none` | `scripts/docs/test_required_sections.py` | `N/A (new validator)` | Enforce required section contract for canonical docs. | active | Remove from validation workflow and delete file. |
| validation | `none` | `scripts/docs/test_canonical_ownership.py` | `N/A (new validator)` | Enforce canonical ownership and metadata constraints. | active | Remove from validation workflow and delete file. |
| validation | `none` | `scripts/docs/test_taxonomy_coverage.py` | `N/A (new validator)` | Enforce feature-package taxonomy coverage. | active | Remove from validation workflow and delete file. |
| validation | `none` | `scripts/docs/test_metadata_freshness.py` | `N/A (new validator)` | Enforce metadata recency policy checks. | active | Remove from validation workflow and delete file. |
| validation | `none` | `scripts/docs/test_migration_map.py` | `N/A (new validator)` | Verify migration lock terms in root and docs map. | active | Remove from validation workflow and delete file. |
| validation | `none` | `scripts/docs/test_links.py` | `N/A (new validator)` | Verify docs-path link integrity. | active | Remove from validation workflow and delete file. |
| validation | `none` | `scripts/docs/test_orphans.py` | `N/A (new validator)` | Verify inbound-link reachability for docs files. | active | Remove from validation workflow and delete file. |

## Category B: Moved Paths
- No path moves were introduced in T1-T6.
- Replacement path: `none`.
- Rationale: IA overhaul expanded structure using additive files and in-place edits only.
- Status: `verified-none`.
- Rollback notes: not applicable because no move occurred.

## Category C: Renamed Paths
- No file renames were introduced in T1-T6.
- Replacement path: `none`.
- Rationale: existing canonical filenames were retained to avoid link churn.
- Status: `verified-none`.
- Rollback notes: not applicable because no rename occurred.

## Category D: Deleted Paths
- No path deletions were introduced in T1-T6.
- Replacement path: `none`.
- Rationale: migration preserved prior templates while adding governance and taxonomy artifacts.
- Status: `verified-none`.
- Rollback notes: not applicable because no deletion occurred.

## In-Place Updates (No Path Change)
- The following files were updated in place and were not moved, renamed, or deleted: `README.md`, `AGENTS.md`, `docs/00-README.md`, `docs/01-product.md`, `docs/02-system-architecture.md`, `docs/03-engineering-rules.md`, `docs/04-features/04-_template/04-spec.md`, `docs/05-test-strategy.md`, `docs/06-adrs/06-ADR-0000-template.md`, and `docs/07-runbooks/07-template.md`.

## Verification Notes
- This map records repository-observed deltas only.
- If a future task introduces real moves/renames/deletes, update the corresponding category and replacement paths in the same change.

## Last Updated When
- Any docs IA path is created, moved, renamed, deleted, or reverted.
