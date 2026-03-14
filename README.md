# silicon-spec-md

`silicon-spec-md`는 코드 구현보다 먼저 문서를 정리하는 docs-first 스펙 저장소입니다. 이 저장소의 핵심 목적은 제품 의도, 시스템 구조, 저장소 규칙, 기능 스펙, 테스트 전략, ADR, 런북을 번호 체계로 분리해 정본 문서를 명확히 유지하는 것입니다.

현재 저장소에는 실행 가능한 애플리케이션 코드나 빌드/테스트 도구가 없습니다. 대신 `docs/` 아래의 번호 문서들이 작업 시작점이며, 각 사실은 가장 권위 있는 문서 한 곳에만 두고 다른 문서에서는 링크로 연결하는 것을 기본 원칙으로 삼습니다.

## 저장소 구성

- `docs/00-README.md`: 전체 문서 지도와 읽기/작성 순서
- `docs/01-product.md`: 제품 의도 템플릿
- `docs/02-system-architecture.md`: 시스템 아키텍처 템플릿
- `docs/03-engineering-rules.md`: 저장소 전반의 엔지니어링 규칙 템플릿
- `docs/04-features/04-_template/04-spec.md`: 기능 스펙 템플릿
- `docs/05-test-strategy.md`: 프로젝트 수준 테스트 전략 템플릿
- `docs/06-adrs/06-ADR-0000-template.md`: ADR 템플릿
- `docs/07-runbooks/07-template.md`: 런북 템플릿
- `AGENTS.md`: AI 에이전트용 저장소 운영 규칙

## 읽기 순서

작업을 시작할 때는 아래 순서로 읽는 것을 기준으로 합니다.

1. `docs/00-README.md`
2. `docs/01-product.md`
3. `docs/02-system-architecture.md`
4. `docs/03-engineering-rules.md`
5. 관련 기능 스펙 (`docs/04-features/<feature>/04-spec.md`)
6. 필요 시 `docs/05-test-strategy.md`
7. 관련 ADR (`docs/06-adrs/`)
8. 관련 런북 (`docs/07-runbooks/`)

## 작성 흐름

문서를 새로 채우거나 프로젝트를 구체화할 때는 아래 순서를 권장합니다.

1. `docs/01-product.md`에서 제품 의도를 정리합니다.
2. `docs/02-system-architecture.md`에서 안정적인 시스템 구조를 정리합니다.
3. `docs/03-engineering-rules.md`에서 저장소 전반의 규칙을 정리합니다.
4. 기능을 시작할 때마다 `docs/04-features/<feature>/04-spec.md`를 작성합니다.
5. 프로젝트 공통 검증 원칙이 필요하면 `docs/05-test-strategy.md`를 작성합니다.
6. 오래 유지되는 기술 결정은 ADR로 기록합니다.
7. 반복 수행되는 운영 절차는 런북으로 기록합니다.

## 문서 운영 원칙

- 정본 사실은 가장 권위 있는 문서 한 곳에만 둡니다.
- 다른 문서에서 같은 내용을 반복하기보다 링크로 연결합니다.
- 기존 번호 체계와 파일 경로를 유지합니다.
- 기존 번호 문서는 한국어를 기본 언어로 유지합니다.
- `AGENTS.md`는 범용 에이전트를 위한 영어 문서입니다.
- 아직 없는 도구나 워크플로를 README에 가정해서 적지 않습니다.

## 현재 상태

- 애플리케이션 코드: 없음
- 패키지 매니저 설정: 없음
- 빌드 명령: `N/A`
- 린트 명령: `N/A`
- 테스트 명령: `N/A`

## 안전한 확인 명령

현재 저장소에서 안전하게 사용할 수 있는 기본 확인 명령은 아래와 같습니다.

- `pwd`
- `ls`
- `ls docs`

저장소 규칙과 문서 소유 경계의 최신 기준은 `AGENTS.md`와 `docs/00-README.md`를 함께 참고하면 됩니다.
