# System Architecture Template

## Purpose
- Describe the stable technical structure of the system.

## Usage Order
- Step 2: Write this after `docs/01-product.md` is organized.
- Define it before starting feature-level design.

## Intended Audience
- Engineers and AI agents who need architectural context before writing or reviewing feature specs.

## Out of Scope
- Product strategy.
- Repository-wide coding rules.
- Step-by-step operational procedures.
- The full history of decisions.

## Canonical Scope
- System boundaries.
- Major components.
- Data and control flow.
- External dependencies.
- Stable technical constraints.

## Last Updated When
- When the stable system structure changes, a major dependency changes, or component boundaries change.

## Canonical Links
- For product intent, see `docs/01-product.md`.
- For repository-wide rules, see `docs/03-engineering-rules.md`.
- For decision records, see `docs/06-adrs/06-ADR-0000-template.md`.

## System Context
- What system are we building, and what is outside its boundary?

## Core Components
- Summarize the major components and the responsibility of each component.

## Boundaries and Interfaces
- Describe the important boundaries between layers, services, and modules.

## Data Flow
- Explain how data moves through the system.

## Control Flow
- Explain how requests, jobs, and events move through the system.

## External Dependencies
- List the third-party systems, platforms, and infrastructure the system depends on.

## Technical Constraints
- Record stable technical limits, invariants, and deployment assumptions.

## Current-State Decisions
- Summarize important current architectural decisions.
- Do not rewrite the full decision history; link to ADRs instead.

## Risk Areas and Hotspots
- Identify the architectural areas that future feature specs should treat with extra care.
