import os
from datetime import datetime

BASE_DIR = os.path.join("targets", "beefyfinance")
LOGS_DIR = os.path.join(BASE_DIR, "research_logs")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
today_str = datetime.now().strftime("%Y-%m-%d")

inspection_log = f"""# {today_str} — Beefy Finance (`beefyfinance`) 검사 로그

- **작성 시각**: {now_str}
- **대상 타겟**: Beefy Finance (`beefyfinance`)
- **현황**: 1차~2차 코드 검사 및 잔여 파일/신규 가설(`H-NEW-01`~`H-NEW-03`) 분석 완료, 추가 인스코프 코드/가설 검증 진행 중

## 1. 점검 완료 파일 및 반증/판단 요약

### A. `FlatBeefyZap.sol` (L830–L905 및 관련 스왑·반환 경로)
- `beefIn` / `beefInETH` / `beefOut` / `beefOutAndSwap`: 호출자(`msg.sender`) 입력 또는 호출자 지분(`withdrawAmount`) 출금 기반으로 동작하며 타인 Vault 지분이나 전략 자산을 직접 탈취하는 경로는 확인되지 않음.
- `_swapAndStake` / `_returnAssets` / `addLiquidity(..., 1, 1, ...)`: 잔여 잔액 혼입이나 낮은 최소 수량(`1, 1`) 가능성은 있으나, 외부 직접 전송 dust나 일반 유동성/슬리피지 조건만으로는 직접 자금 탈취·동결 요건을 충족하기 어려움.

### B. `StrategyMultiRewardsPolygonLP.sol` (L310–L442)
- `balanceOf` / `balanceOfWant` / `balanceOfPool`: 실제 `want` 잔액과 `rewardPool.balanceOf(address(this))`를 조회하여 내부 장부 불일치 위험이 낮음.
- `retireStrat` (`only vault`), `panic` / `pause` / `unpause` (`onlyManager`): 권한 제어자 및 출금/승인 초기화 흐름이 일관됨.

### C. `BeefyVaultV6.sol` (L80–L203)
- `deposit` (`nonReentrant`): 예치 전후 `balance()` 차분(`_after.sub(_pool)`)으로 순증분을 계산하여 쉐어를 발행함.
- `withdraw`: 비례 출금액 `r` 계산 후 `_burn(msg.sender, _shares)`를 수행하고, 전략 인출 부족분(`_diff < _withdraw`)을 `r = b.add(_diff)`로 보정함.
- `proposeStrat` / `upgradeStrat` / `inCaseTokensGetStuck`: `onlyOwner` 보호가 적용되어 있음(특권 계정 관련 시나리오는 바운티 범위에서 제외).

### D. `BeefyZapOneInch.sol` (L1–L325)
- `_swapViaOneInch` (`oneInchRouter.call(_callData)`), `propagateError`, `_returnAssets`: 호출자 입력/출금 자산을 기반으로 스왑 및 잔여 토큰 반환을 수행하며, 타인 자산 직접 탈취로 이어지는 명확한 결함은 미확인.

### E. 잔여 업스트림 파일 스캔 (`2026-11-24-remaining-scan.md`)
- `delegatecall` / `selfdestruct` / `.call(` 흔적이 나타난 파일:
  - `contracts/archive/zaps/BeefyZapKyber.sol` (L242: `aggregationRouter.call(_callData)`)
  - `contracts/archive/zaps/BeefyZapOneInch.sol` (L276: `oneInchRouter.call(_callData)`)
  - `contracts/archive/zaps/ZapBeFtmOneInch.sol` (L61: `router.call(_callData)`)

### F. 신규 가설(`H-NEW-01` ~ `H-NEW-03`) 및 추가 파일 점검
- **`H-NEW-01` (`StrategyPolyzapLP.sol`, L1–L218)**:
  - 직접적인 임의 외부 호출(`delegatecall`/`.call`)이나 재진입 취약점은 미확인.
  - 관찰 포인트: `chargeFees()` 및 `addLiquidity()`에서 `swapExactTokensForTokens(..., amountOutMin=0, ..., now)` 및 `addLiquidity(..., 1, 1, ..., now)` 사용(수확 시 MEV/샌드위치 노출 가능성), `deposit()`이 `balanceOfPool() == 0`일 때만 `_deposit()` 수행, `withdraw()`의 `tx.origin == owner() || paused()` 수수료 면제 분기.
- **`H-NEW-02` (`BeefyVaultV6Matic.sol`, L90–L220)**:
  - `depositBNB`는 `msg.value`를 `wmatic.deposit{{value: _amount}}()`로 래핑 후 `earn()` 및 차분(`_after.sub(_pool)`)으로 쉐어를 발행하고, `withdrawBNB`는 쉐어 소각 후 `wmatic.withdraw(r)` 및 `msg.sender.transfer(r)`를 수행함. 명백한 잔액 탈취/동결 결함은 미확인.
- **`H-NEW-03` (`BeefyZapKyber.sol`, L50–L273)**:
  - `beefInETH`, `beefIn`, `beefOut`, `beefOutAndSwap`, `beefOutAndReInvest`, `_swapViaKyber` (`aggregationRouter.call(_callData)`), `_returnAssets` 점검 완료. 호출자 자금/지분 외 타인 자산을 직접 인출하는 경로는 미확인.

## 2. 미검증 / 후속 점검 대상
- **`H-NEW-04`**: `BeefyZapSolidlyDyst.sol` / `BeefyUniV2ZapSolidly.sol` (Solidly/Dystopia `stable` 및 수수료/비율 계산)
- **인스코프 자산 정합성 확인**: 프로그램 규칙(배포된 인스코프 컨트랙트 대상, 특권 접근·단순 슬리피지/MEV 한계, PoC 및 수정안 필수)에 부합하는 실제 배포 주소/자산 확인 필요
"""

report_md = f"""# Beefy Finance (`beefyfinance`) 중간 검사 보고서

- **생성 일시**: {now_str}
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
"""

status_md = f"""# Beefy Finance (`beefyfinance`) 상태 요약

- **최종 갱신**: {now_str}
- **상태**: 검사 진행 중 (1차~2차 코드 검사 완료, 신규 가설 `H-NEW-01`~`H-NEW-03` 분석 완료)
- **산출물**:
  - 검사 로그: `targets/beefyfinance/research_logs/{today_str}-beefy-inspection.md`
  - 중간 보고서: `targets/beefyfinance/reports/beefyfinance-inspection-report.md`
  - 잔여 파일 스캔 로그: `targets/beefyfinance/research_logs/{today_str}-remaining-scan.md`
- **다음 작업**: `H-NEW-04` (`BeefyZapSolidlyDyst.sol` / `BeefyUniV2ZapSolidly.sol`) 점검 및 인스코프 실배포 컨트랙트 대조
"""

with open(os.path.join(LOGS_DIR, f"{today_str}-beefy-inspection.md"), "w", encoding="utf-8") as f:
    f.write(inspection_log)

with open(os.path.join(REPORTS_DIR, "beefyfinance-inspection-report.md"), "w", encoding="utf-8") as f:
    f.write(report_md)

with open(os.path.join(BASE_DIR, "status.md"), "w", encoding="utf-8") as f:
    f.write(status_md)

print("Saved:")
print(" -", os.path.join(LOGS_DIR, f"{today_str}-beefy-inspection.md"))
print(" -", os.path.join(REPORTS_DIR, "beefyfinance-inspection-report.md"))
print(" -", os.path.join(BASE_DIR, "status.md"))
