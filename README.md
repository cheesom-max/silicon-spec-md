# silicon-spec-md

`silicon-spec-md` is a docs-first specification repository that organizes documentation before code implementation. Its core purpose is to keep canonical documents clearly separated by numbered files for product intent, system architecture, repository rules, feature specs, test strategy, ADRs, and runbooks.

This repository currently contains no executable application code and no application/runtime build pipeline. The numbered documents under `docs/` are still the starting point for work, and canonical facts should remain in one authoritative document with links from related docs. Repo-local documentation validation commands now exist under `scripts/docs/`, and the exact validator command set is documented in `docs/05-test-strategy.md`.

## Repository Structure

- `docs/00-README.md`: overall document map and reading/writing order
- `docs/01-product.md`: product intent template
- `docs/02-system-architecture.md`: system architecture template
- `docs/03-engineering-rules.md`: repository-wide engineering rules template
- `docs/04-features/04-_template/04-spec.md`: feature spec template
- `docs/05-test-strategy.md`: project-level test strategy template
- `docs/06-adrs/06-ADR-0000-template.md`: ADR template
- `docs/07-runbooks/07-template.md`: runbook template
- `docs/08-document-operations.md`: documentation operations governance
- `docs/09-glossary.md`: canonical documentation vocabulary
- `AGENTS.md`: repository operating rules for AI agents

## Documentation Architecture Lock

This repository now locks a two-layer documentation model designed for AI agents and human readers.

- Layer 1 (governance control plane): numbered canonical documents under `docs/01` through `docs/09`.
- Layer 2 (delivery package taxonomy): feature folders under `docs/04-features/<feature>/` with distinct roles (`04-spec.md`, `concept.md`, `how-to.md`, `reference.md`, `examples.md`, `changes.md`, `known-issues.md`).
- Canonical language policy: canonical governance docs are written in English.
- Validation runtime policy: use `python3 standard library` only for documentation validation scripts.

### Non-Goals

- No docs website or static-site generator requirement.
- No package-manager-based docs tooling dependency.
- No external hosted docs platform dependency.
- No duplicate canonical ownership for the same fact.

## Reading Order

Use the following order when starting work.

1. `docs/00-README.md`
2. `docs/09-glossary.md` for canonical vocabulary
3. `docs/01-product.md`
4. `docs/02-system-architecture.md`
5. `docs/03-engineering-rules.md`
6. Relevant feature specs in `docs/04-features/<feature>/04-spec.md`
7. `docs/05-test-strategy.md` when needed
8. `docs/08-document-operations.md` for docs loop policy
9. Relevant ADRs in `docs/06-adrs/`
10. Relevant runbooks in `docs/07-runbooks/`

## Writing Flow

Use the following order when filling in the documentation or making the project more concrete.

1. Define product intent in `docs/01-product.md`.
2. Define the stable system structure in `docs/02-system-architecture.md`.
3. Define repository-wide rules in `docs/03-engineering-rules.md`.
4. Create `docs/04-features/<feature>/04-spec.md` whenever a feature starts.
5. Write `docs/05-test-strategy.md` when project-wide verification rules are needed.
6. Update `docs/08-document-operations.md` when docs-system loop policy changes.
7. Update `docs/09-glossary.md` when controlled vocabulary changes.
8. Record long-lived technical decisions as ADRs.
9. Record repeatable operational procedures as runbooks.

## Documentation Operating Principles

- Keep canonical facts in exactly one authoritative document.
- Link from other documents instead of repeating the same content.
- Preserve the existing numbering scheme and file paths.
- Keep canonical governance docs in English.
- `AGENTS.md` is an English document for general-purpose agents.
- Do not claim tools or workflows in the README unless they actually exist in the repository.

## Current State

- Application code: none
- Package manager configuration: none
- Application/runtime build command: `N/A`
- Application/runtime lint command: `N/A`
- Application/runtime test command: `N/A`
- Documentation validation commands: available under `scripts/docs/`
- Exact docs validator command set: `docs/05-test-strategy.md`

## Safe Inspection Commands

The following commands are currently safe to use for basic inspection in this repository.

- `pwd`
- `ls`
- `ls docs`

For the latest guidance on repository rules and document ownership boundaries, refer to `AGENTS.md` together with `docs/00-README.md`.
