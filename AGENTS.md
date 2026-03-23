# AGENTS Guide

## Purpose
This repository is currently a docs-first specification workspace.
Agents working here should treat the numbered files under `docs/` as the primary source of truth for specification content.
For numbered-doc ownership and reading order, follow `docs/00-README.md`.
This file defines agent-specific operating rules and repository handling constraints.
Do not assume an application, package manager, CI pipeline, or test harness exists unless it is added later.

## Current Repository Shape
The repository currently contains only documentation templates and no executable source tree.
See `docs/00-README.md` for the canonical numbered-doc map, ownership boundaries, and reading order.

## Required Starting Point
When starting work:
1. Read `docs/00-README.md` first.
2. Follow the numbered-doc reading order defined there.
3. If a fact belongs clearly to one file, update that file and link from others instead of duplicating content.

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
- Existing numbered docs are written in English.
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
- `docs/00-README.md` owns numbered-doc ownership boundaries and reading order.
- `AGENTS.md` owns agent-specific operating rules, command constraints, and repository handling guidance.
- `README.md` is the public repository landing page and may summarize the repo, but it must not redefine numbered-doc ownership or reading order.
- If the same content can live in multiple places, pick the single most authoritative document and link to it.

## Editing Expectations for Agents
- Read `docs/00-README.md` before restructuring docs or changing document ownership/order.
- Preserve numeric ordering in filenames and folders.
- When renaming docs, update all internal path references in the docs set.
- Do not create extra framework-specific docs unless the repo actually gains that framework.
- Keep templates reusable; avoid filling them with project-specific implementation details unless asked.

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
