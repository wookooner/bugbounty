# 2026-11-24 — Beefy Finance (`beefyfinance`) 검사 로그

- **작성 시각**: 2026-11-24 20:51
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
  - `depositBNB`는 `msg.value`를 `wmatic.deposit{value: _amount}()`로 래핑 후 `earn()` 및 차분(`_after.sub(_pool)`)으로 쉐어를 발행하고, `withdrawBNB`는 쉐어 소각 후 `wmatic.withdraw(r)` 및 `msg.sender.transfer(r)`를 수행함. 명백한 잔액 탈취/동결 결함은 미확인.
- **`H-NEW-03` (`BeefyZapKyber.sol`, L50–L273)**:
  - `beefInETH`, `beefIn`, `beefOut`, `beefOutAndSwap`, `beefOutAndReInvest`, `_swapViaKyber` (`aggregationRouter.call(_callData)`), `_returnAssets` 점검 완료. 호출자 자금/지분 외 타인 자산을 직접 인출하는 경로는 미확인.

## 2. 미검증 / 후속 점검 대상
- **`H-NEW-04`**: `BeefyZapSolidlyDyst.sol` / `BeefyUniV2ZapSolidly.sol` (Solidly/Dystopia `stable` 및 수수료/비율 계산)
- **인스코프 자산 정합성 확인**: 프로그램 규칙(배포된 인스코프 컨트랙트 대상, 특권 접근·단순 슬리피지/MEV 한계, PoC 및 수정안 필수)에 부합하는 실제 배포 주소/자산 확인 필요
