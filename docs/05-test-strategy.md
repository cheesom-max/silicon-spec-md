# Test Strategy Template

## Purpose
- Define the project-level quality and verification approach.

## Usage Order
- Step 5: Write this after feature spec work has begun, when project-wide test principles need to be organized.
- Use it when common verification standards are needed across the repository.

## Intended Audience
- Engineers and AI agents who must decide how changes in this repository should be verified.

## Out of Scope
- Feature-specific test cases.
- Incident response procedures.
- Product priority decisions.
- Detailed architecture explanations.

## Canonical Scope
- Test levels.
- Quality risks.
- Required verification evidence.
- Exit criteria for changes.

## Last Updated When
- When the verification model, test tools, risk profile, or release gates change.

## Canonical Links
- For repository-wide contribution rules, see `docs/03-engineering-rules.md`.
- For feature-level verification plans, see the relevant feature spec.

## Scope
- Define which change types this strategy covers.

## Risk Areas
- Summarize the failure types that deserve the most testing effort.

## Test Levels
- Unit tests.
- Integration tests.
- End-to-end tests.
- Manual QA.

## Core Scenarios
- Scenarios that must stay reliable even as the system evolves.

## Environments and Fixtures
- Describe the environments, data, and fixtures required for trustworthy tests.

## Verification Evidence Expectations
- Define the evidence that must exist before a change is considered verified.

## Exit Criteria
- The minimum conditions that must be satisfied before deployment or merge.

## Operational Signals and Rollback Checks
- What operational signals must be checked for high-risk changes?
- What standard should be used to judge abnormal behavior?
- When problems happen, under what conditions should the team switch to rollback or follow-up corrective work?

## Gaps and Exceptions
- Define how known quality gaps and justified exceptions should be documented.
