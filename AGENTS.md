# AGENTS Guide

## Purpose
This repository is currently a docs-first specification workspace.
Agents working here should treat the numbered files under `docs/` as the primary source of truth.
Do not assume an application, package manager, CI pipeline, or test harness exists unless it is added later.

## Current Repository Shape
The repository currently contains only documentation templates and no executable source tree.
- `docs/00-README.md`: documentation map and writing order
- `docs/01-product.md`: product intent template
- `docs/02-system-architecture.md`: system architecture template
- `docs/03-engineering-rules.md`: repository-wide engineering rules template
- `docs/04-features/04-_template/04-spec.md`: feature spec template
- `docs/05-test-strategy.md`: project-wide test strategy template
- `docs/06-adrs/06-ADR-0000-template.md`: ADR template
- `docs/07-runbooks/07-template.md`: runbook template

## Authoritative Reading Order
When starting work, read documents in this order:
1. `docs/00-README.md`
2. `docs/01-product.md`
3. `docs/02-system-architecture.md`
4. `docs/03-engineering-rules.md`
5. The relevant feature spec under `docs/04-features/`
6. `docs/05-test-strategy.md` when verification expectations matter
7. Relevant ADRs in `docs/06-adrs/`
8. Relevant runbooks in `docs/07-runbooks/`

## Stage Gates
Projects using these templates must distinguish `scaffolded`, `integration-ready`, and `production-ready` states.
For external auth, billing, webhook, or deploy-coupled work, implementation is not ready until all of the following exist in project-specific form:
- `docs/01-product.md`
- `docs/02-system-architecture.md`
- `docs/03-engineering-rules.md`
- the relevant feature spec under `docs/04-features/`
- `docs/05-test-strategy.md`
- a linked ADR for durable provider/platform decisions
- a runbook for provider onboarding or deployment-critical procedures

Hosted/provider verification evidence is required before calling such work complete.

If a fact belongs clearly to one file, update that file and link from others instead of duplicating content.

## Build, Lint, and Test Commands
No repository-level build, lint, or test commands are configured today.

Observed status:
- No `package.json`
- No `pyproject.toml`
- No `Cargo.toml`
- No `go.mod`
- No `Makefile`
- No `justfile`
- No ESLint, Prettier, Ruff, Biome, Jest, Vitest, or Pytest config

Because of that, agents must not invent commands such as `npm test`, `pnpm lint`, `pytest`, `cargo test`, or `make test`.

Use this guidance instead:
- Build: `N/A` until a build tool is added
- Lint: `N/A` until a linter or formatter is added
- Full test suite: `N/A` until a test runner is added
- Single test: unsupported until a test runner is added

If tooling is introduced later, update this file immediately with the exact commands.

## Single-Test Guidance
There is currently no supported way to run a single test because there is no test harness in the repository.
If future work adds a runner, document all of the following in this file:
- the full test command
- the single-test command
- one concrete example command
- any required environment setup

Until then, do not claim that a single-test workflow exists.

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
- Existing numbered docs are written in Korean.
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

### Source-of-Truth Rules
- `docs/01-product.md` owns product intent
- `docs/02-system-architecture.md` owns system shape
- `docs/03-engineering-rules.md` owns repository-wide rules
- `docs/04-features/<feature>/04-spec.md` owns feature behavior and acceptance
- `docs/05-test-strategy.md` owns project-wide verification expectations
- `docs/06-adrs/` owns durable decision records
- `docs/07-runbooks/` owns operational procedures

If the same content can live in multiple places, pick the single most authoritative document and link to it.

## Editing Expectations for Agents
- Read `docs/00-README.md` before restructuring docs.
- Preserve numeric ordering in filenames and folders.
- When renaming docs, update all internal path references in the docs set.
- Do not create extra framework-specific docs unless the repo actually gains that framework.
- Keep templates reusable; avoid filling them with project-specific implementation details unless asked.
- Strengthen reusable templates by adding ownership, readiness, and verification gates when repeated failure patterns reveal missing process.

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
