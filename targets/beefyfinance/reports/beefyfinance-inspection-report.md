# Beefy Finance (`beefyfinance`) 중간 검사 보고서

- **생성 일시**: 2026-11-24 20:51
- **분석 상태**: 진행 중 (1차~2차 코드 검사 및 신규 가설 3건 분석 완료, 후속 가설 및 인스코프 실배포 자산 대조 필요)

---

## 1. 프로그램 및 검증 기준 요약
- **보상 체계**: Smart Contract Critical `$75,000` / High `$15,000` / Medium `$2,000` / Low `$500` (정액, PoC 및 수정 제안 필수)[cite: 5].
- **주요 제외 원칙**: 관리자/특권 역할 필요 공격, 단순 best practice 지적, 제3자 오라클 단순 오류 등 프로그램 제외 조항 준수 필요[cite: 5].
- **검증 원칙**: 코드 정적 분석만으로 성립 여부를 단정하지 않고, 실제 상태 변화·자금 흐름·반증(무력화 조건)을 함께 확인.

---

## 2. 파일별 검사 결과 요약

| 대상 파일 | 점검 범위 | 주요 확인 사항 및 판정 |
| :--- | :--- | :--- |
| `FlatBeefyZap.sol` | L830–L905 및 스왑·반환 경로 | 호출자 입력/출금 기반 처리; 직접 자금 탈취/동결 결함 미확인 |
| `StrategyMultiRewardsPolygonLP.sol` | L310–L442 | `balanceOf()` 직접 잔액 합산, `only vault`/`onlyManager` 제어 확인 |
| `BeefyVaultV6.sol` | L80–L203 | 예치 차분(`_after.sub(_pool)`) 민팅 및 출금 부족분 보정 확인 |
| `BeefyZapOneInch.sol` | L1–L325 | `oneInchRouter.call(_callData)` 및 `_returnAssets` 점검; 직접 탈취 경로 미확인 |
| `StrategyPolyzapLP.sol` | L1–L218 (`H-NEW-01`) | 직접 외부 호출/재진입 결함 미확인; `amountOutMin=0`/`1,1` 및 `deposit()` `balanceOfPool()==0` 조건 기록 |
| `BeefyVaultV6Matic.sol` | L90–L220 (`H-NEW-02`) | `depositBNB` / `withdrawBNB` 래핑·언래핑 및 쉐어 정산 확인 |
| `BeefyZapKyber.sol` | L50–L273 (`H-NEW-03`) | `beefOutAndReInvest`, `_swapViaKyber`, `_returnAssets` 점검; 직접 탈취 경로 미확인 |

---

## 3. 오탐/반증 필터링 인사이트
1. **외부 호출(`call(_callData)`) 존재만으로 취약점 단정 금지**: `BeefyZapOneInch.sol`과 `BeefyZapKyber.sol` 모두 외부 라우터 호출이 존재하지만, 호출자가 맡긴 입력 토큰 또는 출금 LP 범위 내 정산이 주를 이루므로 **누구의 자산이 어느 경로로 빠져나가는지**를 추적해야 합니다.
2. **슬리피지/최소 수량(`0`, `1, 1`)과 바운티 인정 기준 분리**: 수확(`harvest`)이나 유동성 추가(`addLiquidity`) 시 `amountOutMin=0` 또는 `1, 1`은 이론적 MEV/비율 불리 요인이 될 수 있으나, 바운티 제출 전에는 **실제 인스코프 배포 컨트랙트 여부와 실질적 영향**을 엄격히 따져야 합니다.

---

## 4. 다음 단계 계획
1. `H-NEW-04` (`BeefyZapSolidlyDyst.sol`, `BeefyUniV2ZapSolidly.sol`) 및 `ZapBeFtmOneInch.sol` 점검.
2. 노트북/저장소 내 `beefyfinance` 인스코프 배포 컨트랙트 주소와 현재 저장소 파일의 일치 여부 확인.
3. 유효 가설 도출 시 로컬 포크 환경에서 재현 가능한 PoC 및 수정안 작성.
