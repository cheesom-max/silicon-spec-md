# silicon-spec-md

Ship clarity before code.

`silicon-spec-md` is a docs-first specification workspace for teams that want product intent, system architecture, engineering rules, feature specs, test strategy, ADRs, and runbooks to stay aligned before implementation starts.

## Why this exists

- Ideas get expensive when intent, architecture, and execution drift apart.
- This repository gives each important fact a single canonical home instead of scattering it across tickets, chats, and half-written docs.
- It is designed for teams and AI-assisted workflows that want better decisions before the first production commit.

## What you get

- A structured document system for product intent, system shape, engineering rules, feature behavior, verification strategy, durable decisions, and operational runbooks.
- A layered docs model that keeps governance documents separate from feature delivery packages.
- Repo-local documentation validation scripts that help the docs stay consistent without requiring an application runtime or docs website.

## Docs model

- Layer 1: governance control plane in the numbered canonical docs.
- Layer 2: feature delivery packages under `docs/04-features/<feature>/` with `04-spec.md`, `concept.md`, `how-to.md`, `reference.md`, `examples.md`, `changes.md`, and `known-issues.md`.

## Who it is for

- Founders and product teams shaping a system before implementation hardens the wrong assumptions.
- Engineering leads who want architecture, trade-offs, and execution rules documented early.
- AI-assisted teams that need a stable spec workflow instead of prompt-by-prompt improvisation.

## Start here

- `docs/00-README.md` - canonical docs map, ownership boundaries, and reading order
- `AGENTS.md` - agent operating rules and repository constraints

## Current status

This repository currently contains documentation templates plus repo-local documentation validation scripts. There is no executable application code or application/runtime build pipeline. For the canonical docs map, start with `docs/00-README.md`. For exact docs validator commands, see `docs/05-test-strategy.md`.
