---
doc_type: governance
status: active
owner: architecture-and-docs-governance
audience: engineers-architects-reviewers
last_reviewed: 2026-03-18
canonical: true
supersedes: none
---

# System Architecture

## Purpose
- Describe the stable technical structure of this documentation system.
- Define architecture boundaries so policy, behavior, and verification concerns remain separated.

## Usage Order
- Step 2: Read and update this document after product intent is clarified in `docs/01-product.md`.
- Use this as architectural context before changing repository-wide rules or feature specs.

## Intended Audience
- Engineers, maintainers, and AI agents who need system-shape context before editing specs.

## Out of Scope
- Product intent, goals, and user outcomes (owned by `docs/01-product.md`).
- Repository-wide rules and constraints (owned by `docs/03-engineering-rules.md`).
- Verification gates and test evidence policy (owned by `docs/05-test-strategy.md`).
- Operational cadence and loop governance (owned by `docs/08-document-operations.md`).

## Canonical Scope
- System boundary for docs authoring, governance, and validation runtime.
- Major architectural components and interfaces across governance and delivery layers.
- Data and control flow from authoring input to validated documentation output.
- External dependency boundaries and non-negotiable technical constraints.

## Last Updated When
- When component boundaries, runtime assumptions, or interface contracts change.

## Canonical Links
- `docs/00-README.md` for canonical document map and taxonomy.
- `docs/01-product.md` for product intent and outcomes.
- `docs/03-engineering-rules.md` for repository-wide engineering policy.
- `docs/05-test-strategy.md` for verification expectations.
- `docs/08-document-operations.md` for operating cadence and review loop policy.
- `docs/06-adrs/06-ADR-0000-template.md` for durable decision records.

## System Context
- The system is a docs-first specification workspace that produces authoritative governance and feature documents.
- In-bound scope: numbered governance docs, feature-package specs, and python3-based validation scripts.
- Out-of-bound scope: application runtime services, production infrastructure, and user-facing software deployment.

## Core Components
- Governance control plane (`docs/00` to `docs/09`): durable policy and ownership boundaries.
- Delivery package taxonomy (`docs/04-features/<feature>/`): feature behavior and supporting artifacts.
- Validation layer (`scripts/docs/`): deterministic policy checks for structure, ownership, and metadata.
- Evidence layer (`.sisyphus/evidence/`): command output traces used for review and audit.

## Boundaries and Interfaces
- Product intent interface: `docs/01-product.md` provides goals and constraints consumed by architecture and feature specs.
- Architecture interface: this document defines stable system shape consumed by engineering rules and feature specs.
- Rules interface: `docs/03-engineering-rules.md` defines required/forbidden patterns enforced across docs.
- Verification interface: `docs/05-test-strategy.md` defines what must be validated and evidenced for changes.
- Operations interface: `docs/08-document-operations.md` defines loop cadence and review role workflow.

## Data Flow
- Input: change request or authoring task defines intended documentation update.
- Transformation: contributor edits canonical owner docs first, then updates non-canonical links.
- Validation: python3 scripts parse markdown structure and metadata to detect policy violations.
- Output: passing validator output and evidence artifacts feed review and merge decisions.

## Control Flow
- Trigger: a governance or feature change request enters authoring workflow.
- Control gate 1: canonical owner is selected before edits proceed.
- Control gate 2: required validators run and produce deterministic pass/fail output.
- Control gate 3: review roles assess content, structure, and freshness before closure.

## External Dependencies
- Python 3 standard library runtime for docs validation scripts.
- Git repository history for traceability and reviewability.
- Local CLI tooling for executing validation commands.
- No package-manager dependency is required for governance validation.

## Technical Constraints
- Canonical governance docs are plain Markdown files with stable numbered paths.
- Substantive governance docs must include required YAML metadata keys.
- Validators must run without network dependency and without third-party Python packages.
- Ownership rules require one canonical source per durable fact.

## Current-State Decisions
- Decision: maintain a two-layer docs system (governance control plane and feature delivery taxonomy).
- Decision: keep docs validation in python3 standard library for portability.
- Decision: enforce canonical ownership via numbered governance docs and link-first referencing.
- Decision: keep operational loop policy in `docs/08-document-operations.md` instead of duplicating it here.

## Risk Areas and Hotspots
- Boundary drift between architecture content and repository-wide rules.
- Duplication of operating-loop policy between this document and `docs/08-document-operations.md`.
- Metadata inconsistency that can break ownership and freshness validation scripts.
- Feature-package documents accidentally absorbing governance-level decisions.
