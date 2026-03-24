# silicon-spec-md

- [English](#english)
- [한국어](#한국어)

## English

Ship clarity before code.

`silicon-spec-md` is a docs-first specification workspace for teams that want product intent, system architecture, engineering rules, feature specs, test strategy, ADRs, and runbooks to stay aligned before implementation starts.

### Why this exists

- Ideas get expensive when intent, architecture, and execution drift apart.
- This repository gives each important fact a single canonical home instead of scattering it across tickets, chats, and half-written docs.
- It is designed for teams and AI-assisted workflows that want better decisions before the first production commit.

### What you get

- A structured document system for product intent, system shape, engineering rules, feature behavior, verification strategy, durable decisions, and operational runbooks.
- A layered docs model that keeps governance documents separate from feature delivery packages.
- Repo-local documentation validation scripts that help the docs stay consistent without requiring an application runtime or docs website.

### Docs model

- Layer 1: governance control plane in the numbered canonical docs.
- Layer 2: feature delivery packages under `docs/04-features/<feature>/` with `04-spec.md`, `concept.md`, `how-to.md`, `reference.md`, `examples.md`, `changes.md`, and `known-issues.md`.

### Who it is for

- Founders and product teams shaping a system before implementation hardens the wrong assumptions.
- Engineering leads who want architecture, trade-offs, and execution rules documented early.
- AI-assisted teams that need a stable spec workflow instead of prompt-by-prompt improvisation.

### Start here

- `docs/00-README.md` - canonical docs map, ownership boundaries, and reading order
- `AGENTS.md` - agent operating rules and repository constraints

### Starter prompts

Use these copy-paste prompts to kick off a new docs-first project. Keep `README.md` as a quick start only; for canonical ownership, reading order, and detailed document rules, go to `docs/00-README.md`.

#### 1. Product intent

```text
Read `docs/00-README.md` and `docs/01-product.md` first.

Draft `docs/01-product.md` for a new project.
Include:
- Problem
- Customer Narrative
- Users
- Goals
- Non-Goals
- Success Metrics
- Priority Themes
- Constraints
- Open Questions

Rules:
- This document owns product intent only.
- Do not include system architecture or implementation details.
- Write concise, reviewable statements.
```

#### 2. System architecture

```text
Read `docs/00-README.md` and `docs/02-system-architecture.md` first.

Draft `docs/02-system-architecture.md` based on the approved product intent.
Include:
- System Context
- Core Components
- Boundaries and Interfaces
- Data Flow
- Control Flow
- External Dependencies
- Technical Constraints
- Current-State Decisions
- Risk Areas and Hotspots

Rules:
- Keep this document focused on system shape and boundaries.
- Do not restate product goals or repository-wide rules.
```

#### 3. Engineering rules

```text
Read `docs/00-README.md` and `docs/03-engineering-rules.md` first.

Draft `docs/03-engineering-rules.md` for this project.
Include:
- Design Principles
- Required Patterns
- Forbidden Patterns
- Naming and Structure Rules
- Error Handling Rules
- Test Rules
- Review Rules
- Decision Heuristics
- Exceptions

Rules:
- Define repository-wide constraints only.
- Include canonical ownership, link-first writing, and validation expectations.
```

#### 4. First feature spec

```text
Read `docs/00-README.md` and `docs/04-features/04-_template/04-spec.md` first.

Create `docs/04-features/<feature-name>/04-spec.md` for the first feature.
Include:
- Problem
- Customer Narrative
- Scope
- Non-Goals
- User or Caller
- Behavior
- Acceptance Criteria
- Affected Areas
- Local Design Notes
- Execution Metadata
- Risks and Open Questions
- Verification Plan

Rules:
- This file is the canonical owner of feature behavior and acceptance criteria.
- Keep acceptance criteria pass/fail and observable.
- Use supporting docs only for context, not to redefine behavior.
```

#### 5. Supporting feature docs

```text
Read `docs/04-features/04-_template/` and decide which supporting docs are actually needed.

If needed, draft only the relevant files:
- `concept.md` for background and domain framing
- `how-to.md` for contributor procedure
- `reference.md` for stable lookup facts
- `examples.md` for worked scenarios
- `changes.md` for change chronology
- `known-issues.md` for unresolved constraints and workarounds

Rules:
- Do not duplicate feature behavior or acceptance criteria outside `04-spec.md`.
- Link back to the canonical spec instead of copying policy text.
```

#### 6. Test strategy

```text
Read `docs/05-test-strategy.md` first.

Draft `docs/05-test-strategy.md` for this project.
Include:
- Scope
- Risk Areas
- Test Levels
- Core Scenarios
- Environments and Fixtures
- Verification Evidence Expectations
- Exit Criteria
- Operational Signals and Rollback Checks
- Gaps and Exceptions

Rules:
- Keep this at project level.
- Do not invent a runtime, test runner, or CI system that does not exist.
- Define evidence expectations and validator command usage clearly.
```

#### 7. Documentation operations

```text
Read `docs/08-document-operations.md` first.

Draft `docs/08-document-operations.md` for this project.
Include:
- Docs-System Operating Model
- Loop Cadence and Workflow
- Contributor Workflow
- Evidence Update Rules
- Review Gates
- Review Roles
- Quality Bars
- WIP Limits
- Evidence Paths
- Freshness SLA
- Stop Conditions

Rules:
- Make the contributor workflow concrete and repeatable.
- Keep review gates separate for canonical impact, subject-matter, docs-structure, and freshness.
```

#### 8. Glossary

```text
Read `docs/09-glossary.md` first.

Draft `docs/09-glossary.md` for this project.
Define controlled vocabulary for:
- `doc_type`
- `status`
- canonical ownership terms
- review gate terms
- evidence terms

Rules:
- Add only reusable governance vocabulary.
- Do not use this document to restate product or feature behavior.
```

#### 9. Optional ADR or runbook

```text
If a long-lived architectural decision appears, use `docs/06-adrs/06-ADR-0000-template.md` to draft an ADR.
If a repeatable operational procedure is needed, use `docs/07-runbooks/07-template.md` to draft a runbook.

Rules:
- ADRs are for durable decisions, not temporary notes.
- Runbooks are for repeatable execution procedures, not product specs.
```

### Current status

This repository currently contains documentation templates plus repo-local documentation validation scripts. There is no executable application code or application/runtime build pipeline. For the canonical docs map, start with `docs/00-README.md`. For exact docs validator commands, see `docs/05-test-strategy.md`.

## 한국어

코드보다 먼저 명확함을 정리하세요.

`silicon-spec-md`는 제품 의도, 시스템 아키텍처, 엔지니어링 규칙, 기능 명세, 테스트 전략, ADR, 런북이 구현 전에 서로 어긋나지 않도록 정리하려는 팀을 위한 docs-first 명세 워크스페이스입니다.

### 이 저장소가 필요한 이유

- 의도, 아키텍처, 실행이 어긋나기 시작하면 아이디어의 비용이 빠르게 커집니다.
- 이 저장소는 중요한 사실마다 하나의 canonical home을 두어 티켓, 채팅, 반쯤 작성된 문서에 내용이 흩어지는 일을 줄입니다.
- 첫 프로덕션 커밋 전에 더 나은 결정을 내리고 싶은 팀과 AI 지원 워크플로우를 위해 설계되었습니다.

### 제공하는 것

- 제품 의도, 시스템 구조, 엔지니어링 규칙, 기능 동작, 검증 전략, 장기 결정, 운영 절차를 위한 구조화된 문서 시스템
- 거버넌스 문서와 기능 전달 패키지를 분리하는 계층형 docs 모델
- 애플리케이션 런타임이나 docs 사이트 없이도 문서 일관성을 검증할 수 있는 저장소 로컬 validation 스크립트

### 문서 모델

- Layer 1: 번호가 붙은 canonical docs로 구성된 거버넌스 컨트롤 플레인
- Layer 2: `docs/04-features/<feature>/` 아래의 기능 전달 패키지로, `04-spec.md`, `concept.md`, `how-to.md`, `reference.md`, `examples.md`, `changes.md`, `known-issues.md`를 포함합니다.

### 이런 팀에 적합합니다

- 구현 전에 시스템 방향을 제대로 잡고 싶은 창업자와 제품 팀
- 아키텍처, 트레이드오프, 실행 규칙을 일찍 문서화하고 싶은 엔지니어링 리드
- 즉흥적인 프롬프트 작업 대신 안정적인 명세 워크플로우가 필요한 AI 활용 팀

### 시작 위치

- `docs/00-README.md` - canonical docs map, ownership boundaries, reading order
- `AGENTS.md` - 에이전트 운영 규칙과 저장소 제약 사항

### 시작용 프롬프트

아래 프롬프트는 새 docs-first 프로젝트를 시작할 때 바로 복붙해서 사용할 수 있습니다. `README.md`는 빠른 시작 가이드만 담당하며, canonical ownership, reading order, 상세 문서 규칙은 `docs/00-README.md`를 기준으로 삼아야 합니다.

#### 1. 제품 의도

```text
먼저 `docs/00-README.md`와 `docs/01-product.md`를 읽어라.

새 프로젝트용 `docs/01-product.md` 초안을 작성하라.
포함 항목:
- Problem
- Customer Narrative
- Users
- Goals
- Non-Goals
- Success Metrics
- Priority Themes
- Constraints
- Open Questions

규칙:
- 이 문서는 제품 의도만 소유한다.
- 시스템 아키텍처나 구현 세부사항은 포함하지 않는다.
- 간결하고 검토 가능한 문장으로 작성한다.
```

#### 2. 시스템 아키텍처

```text
먼저 `docs/00-README.md`와 `docs/02-system-architecture.md`를 읽어라.

승인된 product intent를 기준으로 `docs/02-system-architecture.md` 초안을 작성하라.
포함 항목:
- System Context
- Core Components
- Boundaries and Interfaces
- Data Flow
- Control Flow
- External Dependencies
- Technical Constraints
- Current-State Decisions
- Risk Areas and Hotspots

규칙:
- 이 문서는 시스템 형태와 경계에만 집중한다.
- 제품 목표나 저장소 전역 규칙을 반복 설명하지 않는다.
```

#### 3. 엔지니어링 규칙

```text
먼저 `docs/00-README.md`와 `docs/03-engineering-rules.md`를 읽어라.

이 프로젝트용 `docs/03-engineering-rules.md` 초안을 작성하라.
포함 항목:
- Design Principles
- Required Patterns
- Forbidden Patterns
- Naming and Structure Rules
- Error Handling Rules
- Test Rules
- Review Rules
- Decision Heuristics
- Exceptions

규칙:
- 저장소 전반에 적용되는 제약만 정의한다.
- canonical ownership, link-first writing, validation expectations를 포함한다.
```

#### 4. 첫 기능 명세

```text
먼저 `docs/00-README.md`와 `docs/04-features/04-_template/04-spec.md`를 읽어라.

첫 번째 기능을 위해 `docs/04-features/<feature-name>/04-spec.md`를 작성하라.
포함 항목:
- Problem
- Customer Narrative
- Scope
- Non-Goals
- User or Caller
- Behavior
- Acceptance Criteria
- Affected Areas
- Local Design Notes
- Execution Metadata
- Risks and Open Questions
- Verification Plan

규칙:
- 이 파일은 feature behavior와 acceptance criteria의 canonical owner다.
- acceptance criteria는 pass/fail 가능하고 관찰 가능한 형태로 작성한다.
- supporting docs는 맥락 제공에만 사용하고, 동작 정의를 다시 쓰지 않는다.
```

#### 5. 기능 보조 문서

```text
`docs/04-features/04-_template/`를 읽고 어떤 supporting docs가 실제로 필요한지 판단하라.

필요한 경우에만 관련 파일을 작성하라:
- `concept.md` - 배경과 도메인 맥락
- `how-to.md` - 기여자 절차
- `reference.md` - 안정적인 lookup 정보
- `examples.md` - 예시 시나리오
- `changes.md` - 변경 이력
- `known-issues.md` - 미해결 제약과 우회 방법

규칙:
- `04-spec.md` 밖에서 feature behavior나 acceptance criteria를 중복 정의하지 않는다.
- 정책 문장을 복사하지 말고 canonical spec으로 링크한다.
```

#### 6. 테스트 전략

```text
먼저 `docs/05-test-strategy.md`를 읽어라.

이 프로젝트용 `docs/05-test-strategy.md` 초안을 작성하라.
포함 항목:
- Scope
- Risk Areas
- Test Levels
- Core Scenarios
- Environments and Fixtures
- Verification Evidence Expectations
- Exit Criteria
- Operational Signals and Rollback Checks
- Gaps and Exceptions

규칙:
- 프로젝트 수준 내용만 다룬다.
- 존재하지 않는 runtime, test runner, CI 시스템을 만들어내지 않는다.
- evidence expectations와 validator command usage를 명확히 적는다.
```

#### 7. 문서 운영 정책

```text
먼저 `docs/08-document-operations.md`를 읽어라.

이 프로젝트용 `docs/08-document-operations.md` 초안을 작성하라.
포함 항목:
- Docs-System Operating Model
- Loop Cadence and Workflow
- Contributor Workflow
- Evidence Update Rules
- Review Gates
- Review Roles
- Quality Bars
- WIP Limits
- Evidence Paths
- Freshness SLA
- Stop Conditions

규칙:
- contributor workflow는 구체적이고 반복 가능해야 한다.
- review gate는 canonical impact, subject-matter, docs-structure, freshness를 분리해서 작성한다.
```

#### 8. 용어집

```text
먼저 `docs/09-glossary.md`를 읽어라.

이 프로젝트용 `docs/09-glossary.md` 초안을 작성하라.
다음에 대한 controlled vocabulary를 정의하라:
- `doc_type`
- `status`
- canonical ownership 관련 용어
- review gate 관련 용어
- evidence 관련 용어

규칙:
- 재사용 가능한 거버넌스 용어만 추가한다.
- 이 문서에서 제품이나 기능 동작을 다시 설명하지 않는다.
```

#### 9. 선택 사항: ADR 또는 런북

```text
장기적인 아키텍처 결정이 생기면 `docs/06-adrs/06-ADR-0000-template.md`를 사용해 ADR을 작성하라.
반복 가능한 운영 절차가 필요하면 `docs/07-runbooks/07-template.md`를 사용해 runbook을 작성하라.

규칙:
- ADR은 오래 유지될 결정을 위한 문서이지 임시 메모가 아니다.
- Runbook은 반복 가능한 실행 절차를 위한 문서이지 제품 명세 문서가 아니다.
```

### 현재 상태

이 저장소는 현재 문서 템플릿과 저장소 로컬 validation 스크립트를 포함하고 있습니다. 실행 가능한 애플리케이션 코드나 애플리케이션/런타임 빌드 파이프라인은 아직 없습니다. canonical docs map은 `docs/00-README.md`부터 읽고, 정확한 docs validator 명령은 `docs/05-test-strategy.md`를 참고하세요.
