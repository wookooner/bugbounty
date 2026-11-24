# Bug Bounty Research

## Overview

Bug Bounty Research는 취약점 분석과 보안 연구 경험을 체계적으로 축적하기 위한 AI-assisted Security Research 프로젝트다.

개별 취약점 발견에 그치지 않고 연구 과정, 검증 결과, 실패 사례, 공개 보안 연구 자료 및 기술 지식을 지속적으로 관리하여 이후 연구에 재활용하는 것을 목표로 한다.

## Objectives

- 소스코드 기반 취약점 연구
- 바이너리 및 프로그램 동작 분석
- 버그바운티 취약점 발견 및 보고
- 연구 가설 및 검증 과정 관리
- 공개 취약점 사례 분석
- 기술 문서 및 보안 지식 축적
- 분석 실패 사례 관리
- AI 기반 연구 방법론 개선
- 장기적인 보안 연구 인프라 구축

## Research Domains

| Domain | Research Area |
|---|---|
| Web Security | 웹 애플리케이션, API, 인증, 인가 |
| Binary Security | 프로그램 구조, 메모리 안전성 |
| Kernel Security | 운영체제, 드라이버, 권한 경계 |
| Blockchain Security | EVM, 스마트 컨트랙트, DeFi |
| Application Security | 애플리케이션 내부 로직 및 보안 설계 |
| Protocol Security | 프로토콜 구현 및 상태 처리 |

연구 분야는 실제 프로젝트 진행에 따라 확장한다.

## Architecture

프로젝트는 다음 여섯 가지 계층으로 구성한다.

1. Target Management
2. Research Engine
3. Research Logging
4. Finding Management
5. Security Knowledge Base
6. Research Review

AI 에이전트는 연구 대상과 기존 지식을 기반으로 분석을 수행한다.

분석 과정과 결과는 저장소에 기록하며, 일반화 가능한 연구 지식은 별도의 지식베이스에 축적한다.

## Directory Structure

```text
BugBounty/
├── README.md
├── AGENTS.md
│
├── targets/
│   └── <project-name>/
│       ├── README.md
│       ├── official/
│       ├── scope.md
│       ├── overview.md
│       ├── status.md
│       ├── architecture.md
│       ├── attack_surface.md
│       ├── hypotheses/
│       ├── research_logs/
│       ├── evidence/
│       └── findings/
│
├── knowledge/
│   ├── vulnerability_patterns/
│   ├── case_studies/
│   ├── techniques/
│   ├── references/
│   └── methodology/
│
├── reproduction/
│   ├── public_cases/
│   ├── local_labs/
│   └── regression_tests/
│
├── reports/
│   ├── drafts/
│   ├── submitted/
│   └── resolved/
│
├── templates/
│   ├── target.md
│   ├── hypothesis.md
│   ├── research_log.md
│   ├── finding.md
│   └── knowledge.md
│
└── index/
    ├── targets.json
    ├── findings.json
    └── knowledge.json
```

## Directory Responsibilities

| Directory | Purpose |
|---|---|
| targets | 대상별 연구 자료 |
| hypotheses | 취약점 가설 |
| research_logs | 분석 과정 및 실패 기록 |
| evidence | 검증 증거 |
| findings | 확인된 취약점 |
| knowledge | 재사용 가능한 보안 지식 |
| reproduction | 공개 사례 및 허가된 재현 연구 |
| reports | 버그바운티 제출 보고서 |
| templates | 연구 문서 표준 양식 |
| index | 연구 및 지식 검색용 인덱스 |

## Research Lifecycle

```text
Target Registration
        |
        v
Scope Verification
        |
        v
Architecture Analysis
        |
        v
Attack Surface Mapping
        |
        v
Knowledge Retrieval
        |
        v
Hypothesis Generation
        |
        v
Validation
        |
        +---- Rejected / Blocked
        |           |
        |           v
        |      Research Log
        |
        v
Confirmed Finding
        |
        v
Reporting
        |
        v
Knowledge Extraction
        |
        v
Knowledge Base
```

분석 과정에서 추가 정보가 필요한 경우 이전 단계로 돌아갈 수 있다.

## Identifier Convention

| Type | Format | Example |
|---|---|---|
| Target | TGT-NNNN | TGT-0001 |
| Attack Surface | AS-NNNN | AS-0001 |
| Hypothesis | HYP-NNNN | HYP-0001 |
| Research Log | LOG-NNNN | LOG-0001 |
| Finding | FND-NNNN | FND-0001 |
| Knowledge | KB-NNNN | KB-0001 |
| Reference | REF-NNNN | REF-0001 |
| Reproduction | REP-NNNN | REP-0001 |

ID는 각 유형 내에서 전역적으로 고유해야 한다.

대상 간 관련 연구 및 지식은 ID를 이용해 연결한다.

## Research Data Relationships

```text
Target
  ├── Attack Surface
  │     └── Hypothesis
  │           ├── Research Log
  │           ├── Reference
  │           ├── Knowledge
  │           └── Finding
  │                 ├── Evidence
  │                 ├── Reproduction
  │                 └── Report
  │
  └── Research Status
```

모든 주요 연구 기록은 관련 데이터의 ID를 참조한다.

## Starting a New Research Target

1. 대상 ID를 생성한다.
2. `targets/<project-name>/`에 프로젝트 이름으로 폴더를 만들고 기존 대상 ID는 문서와 데이터에 유지한다.
3. 공식 Information, Scope, Resources, Source를 확인하고 출처와 확인일을 `official/`에 저장한다. 연구 범위는 프로젝트의 `scope.md`에 기록한다.
4. 시작 문서인 프로젝트 `README.md`에서 공식 자료와 상태를 연결하고, 버전과 소스 커밋을 고정한다.
5. 소스코드 또는 분석 가능한 자료를 확보한다.
6. architecture.md를 작성한다.
7. attack_surface.md를 작성한다.
8. 관련 지식 및 문서를 검색한다.
9. 취약점 가설을 생성한다.
10. 가설별 분석 및 검증을 수행한다.
11. 연구 결과를 기록한다.
12. 재사용 가능한 지식을 추출한다.

## Resuming Existing Research

기존 연구를 재개할 때 다음 순서로 확인한다.

1. AGENTS.md
2. 프로젝트 README.md에서 official/의 Information, Scope, Resources, Source
3. 프로젝트 scope.md와 status.md
4. 활성 가설과 최근 연구 기록
5. 관련 지식베이스와 필요한 코드 및 기술 문서

프로젝트 README.md를 시작점으로 사용한다. 여러 프로젝트에 재사용되는 원칙과 자료는 knowledge/에 두고, 프로젝트별 연구 자료와 증거는 해당 프로젝트 폴더에 둔다.

## Knowledge Management

지식베이스는 다음 두 종류의 정보를 관리한다.

### Source Knowledge

- 공식 기술 문서
- 공개 CVE
- 보안 연구 논문
- 공개 취약점 보고서
- 기술 블로그
- 공개 패치 분석 자료

### Processed Knowledge

- 취약점 발생 조건
- 근본 원인 패턴
- 분석 방법론
- 오탐 조건
- 보안 불변조건
- 검증 방법
- 실패 사례
- 적용 가능한 기술 및 버전

원본 출처와 가공된 지식 간의 연결 관계를 유지한다.

## Security and Confidentiality

본 프로젝트는 허가된 보안 연구를 목적으로 한다.

- 버그바운티 프로그램 정책 준수
- 허가된 범위 내에서 연구 수행
- 민감정보 및 인증정보 저장 제한
- 미공개 취약점의 무단 공개 금지
- 비공개 연구 자료 접근 권한 관리
- 대상 및 자료의 라이선스 준수

실제 비공개 대상 코드와 민감한 검증 자료는 필요한 경우 별도의 통제된 저장소에서 관리한다.

## Research Metrics

프로젝트의 발전을 평가하기 위해 다음 지표를 기록한다.

- 연구 대상 수
- 생성된 가설 수
- 검증된 가설 수
- 반증된 가설 수
- 중단된 가설 수
- 확인된 취약점 수
- 보고서 제출 및 채택 수
- 중복 및 오탐 비율
- 축적된 지식 수
- 기존 지식 재사용 횟수

## Development Roadmap

### Phase 1 — Research Foundation

- [ ] 연구 디렉터리 구축
- [ ] AI 운영 지침 작성
- [ ] 표준 기록 템플릿 구축
- [ ] 연구 ID 체계 구축
- [ ] 첫 번째 연구 대상 등록
- [ ] 실제 버그바운티 분석 수행

### Phase 2 — Knowledge Infrastructure

- [ ] 보안 지식베이스 구축
- [ ] 기술 문서 가공 및 색인
- [ ] 연구 기록 검색 기능
- [ ] 관련 취약점 및 지식 연결
- [ ] 지식 품질 검증 체계

### Phase 3 — Tool Integration

- [ ] 코드 검색 인터페이스
- [ ] 정적 분석 도구 연동
- [ ] 연구 데이터 자동 기록
- [ ] 테스트 결과 관리
- [ ] 보고서 생성 지원

### Phase 4 — Research Intelligence

- [ ] RAG 기반 지식 검색
- [ ] 관련 사례 자동 추천
- [ ] 다중 AI 에이전트 연동
- [ ] 연구 방법론 평가
- [ ] 연구 성과 기반 지식 개선

## Agent Compatibility

본 프로젝트는 특정 AI 모델에 종속되지 않는다.

ChatGPT, Codex, Claude Code 및 기타 AI 연구 도구는 AGENTS.md와 연구 상태 파일을 기반으로 동일한 연구 체계에 참여할 수 있다.

## Project Philosophy

취약점 발견뿐 아니라 취약점을 발견하거나 반증하는 과정에서 얻은 지식도 중요한 연구 성과다.

모든 연구는 이후 연구의 기반이 되어야 한다.

실패한 분석도 적절히 기록하고 검토한다면 재사용 가능한 연구 자산이 된다.