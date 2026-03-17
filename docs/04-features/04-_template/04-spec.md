# Feature Spec Template

## Purpose
- Define the behavior, scope, acceptance criteria, and local design notes for a single feature.

## Usage Order
- Step 4: Write this before implementation of the feature starts.
- Copy this template for each new feature and use it as `docs/04-features/<feature>/04-spec.md`.

## Intended Audience
- People implementing, reviewing, testing, and approving a single feature.

## Out of Scope
- Global product strategy.
- Full-system architecture.
- Repository-wide rules.
- Long-lived architectural history.

## Canonical Scope
- Feature problem definition.
- Feature scope and non-goals.
- User-visible or API-visible behavior.
- Acceptance criteria.
- Affected areas and local risks.

## Last Updated When
- When feature scope, behavior, acceptance criteria, or implementation approach changes materially.

## Canonical Links
- For product intent, see `docs/01-product.md`.
- For architectural context, see `docs/02-system-architecture.md`.
- For repository-wide rules, see `docs/03-engineering-rules.md`.
- If this feature depends on a long-lived decision, refer to the related ADR.

## Problem
- What problem does this feature solve?
- Why is this feature needed now?

## Customer Narrative
- What real user flow does this feature belong to?
- At what moment does the user need this feature?
- What representative inconvenience or failure does the user experience without it?
- What change should the user feel when the feature works well?

## Scope
- What is included in this feature.

## Non-Goals
- What is explicitly not included in this feature.

## User or Caller
- Who uses this feature?
- What is the main flow?

## Behavior
- Describe the expected user-visible behavior or API-visible behavior.
- Include edge cases that materially affect correctness.

## Acceptance Criteria
- Write each criterion as a statement that can be judged pass/fail.
- Prefer observable outcomes over implementation details.

## Affected Areas
- Note the code paths, systems, data, or operational areas most likely to be affected.

## Local Design Notes
- Include only design details specific to this feature.
- Do not re-explain the global architecture; link to it.

## Execution Metadata
- What is the execution unit for this feature change? Example: document, code, data, operational configuration.
- What prerequisites must be checked before applying it?
- What logs, metrics, screens, or responses must be checked immediately after execution?
- If execution evidence must be left behind, what evidence should be recorded?

## Risks and Open Questions
- Risks, unknowns, and undecided points that are not yet resolved.

## Verification Plan
- Define how this feature will be verified: tests, manual QA, metrics, rollout checks, and so on.
