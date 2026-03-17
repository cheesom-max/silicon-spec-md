# silicon-spec-md

`silicon-spec-md` is a docs-first specification repository that organizes documentation before code implementation. Its core purpose is to keep canonical documents clearly separated by numbered files for product intent, system architecture, repository rules, feature specs, test strategy, ADRs, and runbooks.

This repository currently contains no executable application code or build/test tooling. Instead, the numbered documents under `docs/` are the starting point for work, and the default principle is to keep each fact in exactly one authoritative document and connect other documents by links.

## Repository Structure

- `docs/00-README.md`: overall document map and reading/writing order
- `docs/01-product.md`: product intent template
- `docs/02-system-architecture.md`: system architecture template
- `docs/03-engineering-rules.md`: repository-wide engineering rules template
- `docs/04-features/04-_template/04-spec.md`: feature spec template
- `docs/05-test-strategy.md`: project-level test strategy template
- `docs/06-adrs/06-ADR-0000-template.md`: ADR template
- `docs/07-runbooks/07-template.md`: runbook template
- `AGENTS.md`: repository operating rules for AI agents

## Reading Order

Use the following order when starting work.

1. `docs/00-README.md`
2. `docs/01-product.md`
3. `docs/02-system-architecture.md`
4. `docs/03-engineering-rules.md`
5. Relevant feature specs in `docs/04-features/<feature>/04-spec.md`
6. `docs/05-test-strategy.md` when needed
7. Relevant ADRs in `docs/06-adrs/`
8. Relevant runbooks in `docs/07-runbooks/`

## Writing Flow

Use the following order when filling in the documentation or making the project more concrete.

1. Define product intent in `docs/01-product.md`.
2. Define the stable system structure in `docs/02-system-architecture.md`.
3. Define repository-wide rules in `docs/03-engineering-rules.md`.
4. Create `docs/04-features/<feature>/04-spec.md` whenever a feature starts.
5. Write `docs/05-test-strategy.md` when project-wide verification rules are needed.
6. Record long-lived technical decisions as ADRs.
7. Record repeatable operational procedures as runbooks.

## Documentation Operating Principles

- Keep canonical facts in exactly one authoritative document.
- Link from other documents instead of repeating the same content.
- Preserve the existing numbering scheme and file paths.
- Keep the numbered docs primarily in English going forward.
- `AGENTS.md` is an English document for general-purpose agents.
- Do not claim tools or workflows in the README unless they actually exist in the repository.

## Current State

- Application code: none
- Package manager configuration: none
- Build command: `N/A`
- Lint command: `N/A`
- Test command: `N/A`

## Safe Inspection Commands

The following commands are currently safe to use for basic inspection in this repository.

- `pwd`
- `ls`
- `ls docs`

For the latest guidance on repository rules and document ownership boundaries, refer to `AGENTS.md` together with `docs/00-README.md`.
