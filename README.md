# Thumbnail Generator Spec Workspace

이 저장소는 유튜브 썸네일 자동 생성 웹 앱의 docs-first 스펙 저장소입니다. 제품 의도, 시스템 구조, 엔지니어링 규칙, 기능 스펙, 테스트 전략, ADR, 런북을 분리해 구현 전에 제품과 기술 결정을 먼저 고정하는 것을 목표로 합니다.

현재 저장소에는 실행 가능한 애플리케이션 코드나 빌드 도구가 없습니다. `docs/` 아래의 번호 문서가 정본이며, 각 사실은 가장 권위 있는 문서 한 곳에만 두고 다른 문서에서는 링크로 연결합니다.

## 저장소 구성

- `docs/00-README.md`: 전체 문서 지도와 읽기/수정 순서
- `docs/01-product.md`: 제품 의도와 비즈니스 범위
- `docs/02-system-architecture.md`: Next.js, Vercel, Supabase, Polar 중심의 시스템 구조
- `docs/03-engineering-rules.md`: 구현 시작 전 지켜야 할 전역 규칙
- `docs/04-features/auth-and-onboarding/04-spec.md`: 가입, 로그인, 무료 크레딧 지급
- `docs/04-features/thumbnail-generation/04-spec.md`: 썸네일 생성 요청과 결과 저장
- `docs/04-features/thumbnail-revision-and-text-overlay/04-spec.md`: 생성본 수정과 수동 문구 오버레이
- `docs/04-features/credits-and-billing/04-spec.md`: 크레딧 차감과 Polar 결제 흐름
- `docs/05-test-strategy.md`: 프로젝트 수준 검증 전략
- `docs/06-adrs/06-ADR-0001-credit-ledger-and-deduction-policy.md`: 크레딧 원장 정책
- `docs/06-adrs/06-ADR-0002-no-text-output-enforcement.md`: 무문자 출력 강제 정책
- `docs/06-adrs/06-ADR-0003-public-endpoint-security-baseline.md`: 인증, 인가, abuse, DDoS, 데이터 격리 기준
- `docs/07-runbooks/07-polar-webhook-failure-recovery.md`: Polar 웹훅 장애 대응
- `docs/07-runbooks/07-credit-ledger-reconciliation.md`: 크레딧 불일치 점검 및 복구
- `docs/07-runbooks/07-auth-session-compromise-response.md`: 인증 및 세션 침해 대응
- `docs/07-runbooks/07-abuse-and-traffic-spike-response.md`: abuse 및 트래픽 급증 대응
- `AGENTS.md`: AI 에이전트용 저장소 운영 규칙

## 읽기 순서

1. `docs/00-README.md`
2. `docs/01-product.md`
3. `docs/02-system-architecture.md`
4. `docs/03-engineering-rules.md`
5. 관련 기능 스펙 (`docs/04-features/<feature>/04-spec.md`)
6. `docs/05-test-strategy.md`
7. 관련 ADR (`docs/06-adrs/`)
8. 관련 런북 (`docs/07-runbooks/`)

## 작성 및 수정 원칙

1. 제품 방향이 바뀌면 `docs/01-product.md`부터 수정합니다.
2. 시스템 경계나 주요 의존성이 바뀌면 `docs/02-system-architecture.md`를 수정합니다.
3. 전역 규칙이 바뀌면 `docs/03-engineering-rules.md`를 수정합니다.
4. 기능 변경 전에는 해당 기능 스펙을 먼저 수정합니다.
5. 오래 유지될 결정은 ADR로 남깁니다.
6. 반복 운영 절차는 런북으로 남깁니다.

## 문서 운영 원칙

- 정본 사실은 한 문서에만 둡니다.
- 다른 문서에서는 반복 설명 대신 링크를 사용합니다.
- 기존 번호 체계와 파일 경로를 유지합니다.
- 번호 문서는 한국어를 기본 언어로 유지합니다.
- 아직 없는 도구나 워크플로를 문서에 사실처럼 적지 않습니다.

## 현재 상태

- 애플리케이션 코드: 없음
- 패키지 매니저 설정: 없음
- 빌드 명령: `N/A`
- 린트 명령: `N/A`
- 테스트 명령: `N/A`

저장소 규칙과 문서 소유 경계의 최신 기준은 `AGENTS.md`와 `docs/00-README.md`를 함께 참고합니다.
