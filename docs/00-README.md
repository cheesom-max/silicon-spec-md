# 문서 지도

## 목적
- 유튜브 썸네일 자동 생성 앱의 정본 문서를 올바른 순서로 안내한다.
- 각 사실이 어느 문서의 소유인지 명확하게 정의한다.

## 사용 순서
- 0단계: 이 문서를 먼저 읽고 전체 문서 구조와 소유 경계를 파악한다.

## 대상 독자
- 이 저장소에서 스펙을 작성, 검토, 구현, 운영 준비하는 모든 사람.

## 범위 밖
- 제품 세부 요구사항의 본문.
- 시스템 구조의 상세 설명.
- 전역 코딩 규칙.
- 기능별 동작 상세.

## 정본으로 다루는 범위
- 이 저장소의 문서 지도.
- 문서 전반의 읽기 순서와 수정 순서.
- 문서별 소유 경계.

## 마지막 업데이트 시점
- 정본 문서가 추가, 삭제, 이름 변경되거나 소유 범위가 바뀔 때.

## 정본 링크
- 제품 의도는 `docs/01-product.md`를 참고한다.
- 시스템 구조는 `docs/02-system-architecture.md`를 참고한다.
- 전역 규칙은 `docs/03-engineering-rules.md`를 참고한다.

## 정본 문서
| 관심사 | 정본 파일 | 메모 |
|---|---|---|
| 제품 의도 | `docs/01-product.md` | 문제, 사용자, 목표, 비목표, 성공 지표, 제약 |
| 시스템 형태 | `docs/02-system-architecture.md` | 컴포넌트, 경계, 흐름, 외부 의존성 |
| 저장소 전반의 엔지니어링 규칙 | `docs/03-engineering-rules.md` | 필수 패턴, 금지 패턴, 네이밍, 검증 규칙 |
| 가입과 초기 크레딧 지급 | `docs/04-features/auth-and-onboarding/04-spec.md` | 인증, 무료 100 크레딧, 대시보드 진입 |
| 썸네일 생성 | `docs/04-features/thumbnail-generation/04-spec.md` | 30자 이상 입력, 생성 요청, 결과 저장 |
| 생성본 수정과 문구 오버레이 | `docs/04-features/thumbnail-revision-and-text-overlay/04-spec.md` | AI 수정, 수동 문구 추가, 다운로드 |
| 크레딧과 결제 | `docs/04-features/credits-and-billing/04-spec.md` | 10 크레딧 차감, Polar 결제, 부족 크레딧 처리 |
| 테스트 기대치 | `docs/05-test-strategy.md` | 프로젝트 수준의 품질 전략 |
| 크레딧 정책 ADR | `docs/06-adrs/06-ADR-0001-credit-ledger-and-deduction-policy.md` | 차감, 환불, 원장 방식 |
| 무문자 출력 ADR | `docs/06-adrs/06-ADR-0002-no-text-output-enforcement.md` | 텍스트 금지 강제 방식 |
| 공개 엔드포인트 보안 ADR | `docs/06-adrs/06-ADR-0003-public-endpoint-security-baseline.md` | 인증, abuse, DDoS, 격리 기준 |
| Polar 웹훅 장애 대응 | `docs/07-runbooks/07-polar-webhook-failure-recovery.md` | 결제 후 미반영 대응 |
| 크레딧 원장 정합성 점검 | `docs/07-runbooks/07-credit-ledger-reconciliation.md` | 잔액 불일치 대응 |
| 인증 또는 세션 침해 대응 | `docs/07-runbooks/07-auth-session-compromise-response.md` | 계정 탈취, 세션 오남용 대응 |
| abuse 또는 트래픽 급증 대응 | `docs/07-runbooks/07-abuse-and-traffic-spike-response.md` | signup/generation 남용, rate limit, DDoS 대응 |

## 기본 작성 순서
1. `docs/01-product.md`를 작성한다.
2. `docs/02-system-architecture.md`를 작성한다.
3. `docs/03-engineering-rules.md`를 작성한다.
4. 각 기능 스펙을 작성한다.
5. `docs/05-test-strategy.md`를 작성한다.
6. 오래 유지될 결정은 ADR로 기록한다.
7. 반복 운영 절차는 런북으로 기록한다.

## 읽는 순서
1. 제품 의도를 파악하려면 `docs/01-product.md`를 읽는다.
2. 기술 맥락을 파악하려면 `docs/02-system-architecture.md`를 읽는다.
3. 전역 규칙을 파악하려면 `docs/03-engineering-rules.md`를 읽는다.
4. 구현하려는 기능의 스펙을 읽는다.
5. 품질 기준이 필요하면 `docs/05-test-strategy.md`를 읽는다.
6. 지속되는 결정은 ADR에서 확인한다.
7. 운영 절차는 관련 런북을 읽는다.

## 수정 순서 원칙
1. 제품 방향이 바뀌면 `docs/01-product.md`부터 수정한다.
2. 시스템 구조가 바뀌면 `docs/02-system-architecture.md`를 수정한다.
3. 전역 규칙이 바뀌면 `docs/03-engineering-rules.md`를 수정한다.
4. 구현 전에 관련 기능 스펙을 갱신한다.
5. 지속되는 결정 변화는 ADR에 반영한다.
6. 운영 절차 변화는 런북에 반영한다.

## 작성 규칙
- 모든 문서는 `목적`, `대상 독자`, `범위 밖`, `정본으로 다루는 범위`, `마지막 업데이트 시점`으로 시작한다.
- 각 문서 상단에 `정본 링크`를 포함한다.
- 같은 사실은 한 문서에만 두고 다른 문서에서는 링크한다.
- 기능 스펙은 전역 설명을 다시 쓰지 않고 제품 문서와 아키텍처 문서로 연결한다.
- 실제로 존재하지 않는 명령, 도구, 워크플로를 사실처럼 적지 않는다.
