# AGENTS Guide

## Purpose
This repository is currently a docs-first specification workspace.
Agents working here should treat the numbered files under `docs/` as the primary source of truth for specification content.
For numbered-doc ownership and reading order, follow `docs/00-README.md`.
This file defines agent-specific operating rules and repository handling constraints.
Do not assume an application, package manager, CI pipeline, or test harness exists unless it is added later.

## Current Repository Shape
The repository is docs-first with no executable application source tree, plus a repo-local documentation validator layer under `scripts/docs/`.
- `docs/00-README.md`: documentation map and writing order
- `docs/01-product.md`: product intent template
- `docs/02-system-architecture.md`: system architecture template
- `docs/03-engineering-rules.md`: repository-wide engineering rules template
- `docs/04-features/04-_template/04-spec.md`: feature spec template
- `docs/05-test-strategy.md`: project-wide test strategy template
- `docs/06-adrs/06-ADR-0000-template.md`: ADR template
- `docs/07-runbooks/07-template.md`: runbook template
- `docs/08-document-operations.md`: documentation operations governance
- `docs/09-glossary.md`: canonical documentation vocabulary
- `scripts/docs/`: documentation validation scripts

## Required Starting Point
When starting work:
1. Read `docs/00-README.md` first.
2. Follow the numbered-doc reading order defined there.
3. If a fact belongs clearly to one file, update that file and link from others instead of duplicating content.

## Build, Lint, and Test Commands
Application/runtime build, lint, and test commands are not configured today.

Observed status:
- No `package.json`
- No `pyproject.toml`
- No `Cargo.toml`
- No `go.mod`
- No `Makefile`
- No `justfile`
- No ESLint, Prettier, Ruff, Biome, Jest, Vitest, or Pytest config

Because of that, agents must not invent application/runtime commands such as `npm test`, `pnpm lint`, `pytest`, `cargo test`, or `make test`.

Documentation validation runtime policy:
- Use `python3 standard library` only.
- Do not add Node, npm, pnpm, Poetry, or other package-manager tooling only for docs validation.

Use this guidance instead:
- Application/runtime build: `N/A` until a build tool is added
- Application/runtime lint: `N/A` until a linter or formatter is added
- Application/runtime full test suite: `N/A` until a test runner is added
- Application/runtime single test: unsupported until a test runner is added
- Documentation validation commands: present under `scripts/docs/`
- Exact docs validator command set: `docs/05-test-strategy.md`

If tooling is introduced later, update this file immediately with the exact commands.

## Single-Test Guidance
There is currently no supported way to run a single application/runtime test because there is no application/runtime test harness in the repository.
If future work adds a runner, document all of the following in this file:
- the full test command
- the single-test command
- one concrete example command
- any required environment setup

Until then, do not claim that an application/runtime single-test workflow exists.

## Safe Verification Commands
These commands are safe for repository inspection today:
- `pwd`
- `ls`
- `ls docs`

These are inspection commands only. They are not build, lint, or test commands.

## Code and Documentation Style
The only established conventions come from the current docs set.
Agents should preserve these conventions unless the repository intentionally changes direction.

### Language
- Canonical governance documents are written in English.
- This root `AGENTS.md` is in English because it is aimed at general-purpose coding agents.
- When editing existing docs, preserve the dominant language of the file.

### Naming Conventions
- Use numeric ordering prefixes for top-level docs that are part of the canonical reading flow.
- Use kebab-case for filenames and directory names.
- Keep feature specs under `docs/04-features/<feature>/04-spec.md`.
- Keep ADRs under `docs/06-adrs/06-ADR-xxxx-title.md`.
- Keep runbooks under `docs/07-runbooks/07-<name>.md`.

### Formatting
- Prefer simple Markdown with clear headings.
- Keep section names stable across related templates.
- Keep prose direct and operational rather than promotional.
- Prefer short lists over long narrative blocks when documenting procedures or rules.
- Do not add decorative formatting or unnecessary nesting.

### Imports and Modules
There is no source code yet, so there are no repository-proven import conventions.
Do not invent language-specific import rules in implementation work unless a real codebase and toolchain are added.
If source code is added later, update this file with observed import ordering and module boundary rules.

### Types
There is no typed language configuration in the repository yet.
Still, future agents should prefer explicit types and avoid type suppression once code exists.

### Error Handling
There is no runtime code yet, so there are no project-specific error patterns.
When code is introduced, prefer explicit failures, actionable messages, and no silent swallowing of errors.

### Documentation Ownership Boundaries
- `docs/00-README.md` owns numbered-doc ownership boundaries, layered taxonomy, and document order.
- `AGENTS.md` owns agent-specific operating rules, command constraints, and repository handling guidance.
- `README.md` is the public repository landing page and may summarize the repo, but it must not redefine numbered-doc ownership or reading order.
- If the same content can live in multiple places, pick the single most authoritative document and link to it.

## Editing Expectations for Agents
- Read `docs/00-README.md` before restructuring docs or changing document ownership/order.
- Preserve numeric ordering in filenames and folders.
- When renaming docs, update all internal path references in the docs set.
- Do not create extra framework-specific docs unless the repo actually gains that framework.
- Keep templates reusable; avoid filling them with project-specific implementation details unless asked.
- Keep the governance control plane in numbered docs and keep delivery taxonomy under feature folders.
- Do not introduce docs websites or external hosted docs dependencies unless explicitly added as project scope.

## Cursor and Copilot Rules
No Cursor rules were found.
- No `.cursor/rules/`
- No `.cursorrules`

No Copilot instruction file was found.
- No `.github/copilot-instructions.md`

Because no external assistant rule files exist, this `AGENTS.md` is the root instruction file for agentic work in this repository.

## How to Update This File
Update `AGENTS.md` whenever any of the following changes:
- a real build, lint, or test command is added
- a package manager or language toolchain is introduced
- Cursor or Copilot rules are added
- the docs numbering scheme changes
- the canonical doc paths change
- source code introduces real naming, import, typing, or error-handling conventions

When updating, prefer observed facts over guesses.
If a command is not defined in the repository, say so explicitly.
