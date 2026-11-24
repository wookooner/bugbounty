# 2026-11-24 — Remaining Upstream Files Scan (Entry Points & High-Signal Sinks)

## `contracts/archive/interfaces/gmx/IBeefyVault.sol` (12 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/keepers/interfaces/IBeefyVault.sol` (26 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/strategies/Cake/StratManagerCake.sol` (82 lines)
- Entry points: setKeeper(L49), setUnirouter(L57), setVault(L65), setBeefyFeeRecipient(L73), beforeDeposit(L81)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol` (420 lines)
- Entry points: deposit(L147), withdraw(L163), harvest(L209), balanceOf(L297), balanceOfWant(L307), balanceOfPool(L317), retireStrat(L327), panic(L347), pause(L357), unpause(L369)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/strategies/Common/StratManager.sol` (96 lines)
- Entry points: setKeeper(L54), setStrategist(L62), setUnirouter(L71), setVault(L79), setBeefyFeeRecipient(L87), beforeDeposit(L95)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/strategies/Curve/ConicZap.sol` (132 lines)
- Entry points: estimateSwap(L28), beefInETH(L38), beefIn(L46), estimateSwapOut(L71), beefOutAndSwap(L86)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/strategies/degens/StrategyPolyzapLP.sol` (218 lines)
- Entry points: deposit(L71), withdraw(L86), harvest(L109), balanceOf(L156), balanceOfWant(L161), balanceOfPool(L166), retireStrat(L172), panic(L182), pause(L187), unpause(L193)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultBNB.sol` (250 lines)
- Entry points: balance(L70), available(L80), getPricePerFullShare(L88), depositAll(L95), deposit(L103), depositBNB(L126), earn(L150), withdrawAll(L159), withdrawAllBNB(L166), withdraw(L175), withdrawBNB(L197), proposeStrat(L222), upgradeStrat(L238)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultCapped.sol` (221 lines)
- Entry points: balance(L75), available(L85), getPricePerFullShare(L93), depositAll(L100), deposit(L108), earn(L131), withdrawAll(L140), withdraw(L149), proposeStrat(L171), upgradeStrat(L186), increaseDepositCap(L204), inCaseTokensGetStuck(L215)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultV2.sol` (193 lines)
- Entry points: balance(L71), available(L81), getPricePerFullShare(L89), depositAll(L96), deposit(L104), earn(L125), withdrawAll(L134), withdraw(L143), proposeStrat(L165), upgradeStrat(L181)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultV3.sol` (193 lines)
- Entry points: balance(L71), available(L81), getPricePerFullShare(L89), depositAll(L96), deposit(L104), earn(L125), withdrawAll(L134), withdraw(L143), proposeStrat(L165), upgradeStrat(L180)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultV4.sol` (193 lines)
- Entry points: balance(L71), available(L81), getPricePerFullShare(L89), depositAll(L96), deposit(L104), earn(L125), withdrawAll(L134), withdraw(L143), proposeStrat(L165), upgradeStrat(L180)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultV5.sol` (202 lines)
- Entry points: balance(L69), available(L79), getPricePerFullShare(L87), depositAll(L94), deposit(L102), earn(L123), withdrawAll(L132), withdraw(L141), proposeStrat(L163), upgradeStrat(L178), inCaseTokensGetStuck(L196)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultV6Matic.sol` (256 lines)
- Entry points: balance(L68), available(L78), getPricePerFullShare(L86), depositAll(L93), deposit(L101), depositBNB(L122), earn(L144), withdrawAll(L153), withdrawAllBNB(L160), withdraw(L169), withdrawBNB(L191), proposeStrat(L214), upgradeStrat(L230), inCaseTokensGetStuck(L248)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultV6Native.sol` (258 lines)
- Entry points: balance(L70), available(L80), getPricePerFullShare(L88), depositAll(L95), deposit(L103), depositBNB(L124), earn(L146), withdrawAll(L155), withdrawAllBNB(L162), withdraw(L171), withdrawBNB(L193), proposeStrat(L216), upgradeStrat(L232), inCaseTokensGetStuck(L250)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/vaults/BeefyVaultv6Moonpot.sol` (228 lines)
- Entry points: want(L71), balance(L80), available(L90), getPricePerFullShare(L98), depositAll(L105), deposit(L113), earn(L137), withdrawAll(L146), withdraw(L155), proposeStrat(L177), upgradeStrat(L193), setOnlyMoonpot(L207), setMoonpot(L211), inCaseTokensGetStuck(L222)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/BeefyPairFeeDataSource.sol` (47 lines)
- Entry points: setUpAFactory(L31), setUpASolidFactory(L41)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/BeefyUniV2ZapSolidly.sol` (953 lines)
- Entry points: beefInETH(L779), beefIn(L787), beefOut(L796), beefOutAndSwap(L815), estimateSwap(L927), checkWETH(L942)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/BeefyVelodromeV2Zap.sol` (221 lines)
- Entry points: beefInETH(L33), beefIn(L41), beefOut(L50), beefOutAndSwap(L69), estimateSwap(L201)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/BeefyZapKyber.sol` (273 lines)
- Entry points: beefInETH(L53), beefIn(L60), beefOut(L69), beefOutAndSwap(L87), beefOutAndReInvest(L112), quoteStableAddLiquidityRatio(L128), quoteRemoveLiquidity(L149)
- `delegatecall` / `selfdestruct` / `.call(`: L44:// Forward error message from call/delegatecall, L242:(bool success, bytes memory retData) = aggregationRouter.call(_callData);

## `contracts/archive/zaps/BeefyZapMdex.sol` (214 lines)
- Entry points: beefInETH(L58), beefIn(L66), beefOut(L75), beefOutAndSwap(L94), estimateSwap(L194)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/BeefyZapOneInch.sol` (325 lines)
- Entry points: beefInETH(L49), beefIn(L57), beefOut(L65), beefOutAndSwap(L70), quoteStableAddLiquidityRatio(L144)
- `delegatecall` / `selfdestruct` / `.call(`: L276:(bool success, bytes memory retData) = oneInchRouter.call(_callData);, L313:// Forward error message from call/delegatecall

## `contracts/archive/zaps/BeefyZapSolidlyDyst.sol` (237 lines)
- Entry points: beefInETH(L60), beefIn(L68), beefOut(L77), beefOutAndSwap(L96), estimateSwap(L208), checkWETH(L223)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/IBeefyDataSource.sol` (13 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/ZapBeFtmOneInch.sol` (95 lines)
- Entry points: depositNative(L40), inCaseTokensGetStuck(L83)
- `delegatecall` / `selfdestruct` / `.call(`: L61:(bool success, bytes memory retData) = router.call(_callData);, L73:// Forward error message from call/delegatecall

## `contracts/archive/zaps/ZapBeVelo.sol` (64 lines)
- Entry points: deposit(L38), inCaseTokensGetStuck(L54)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/libs/Babylonian.sol` (35 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/zapInterfaces/IBeefyVault.sol` (14 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/zapInterfaces/IERC20Extended.sol` (7 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/zapInterfaces/IStrategy.sol` (7 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/archive/zaps/zapInterfaces/IWETH.sol` (8 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/BIFI/interfaces/beefy/IBeefyVaultConcLiq.sol` (15 lines)
- Entry points: -
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/BIFI/vaults/BeefyVaultV7.sol` (404 lines)
- Entry points: want(L115), balance(L133), available(L153), getPricePerFullShare(L169), depositAll(L183), deposit(L199), earn(L241), withdrawAll(L259), withdraw(L277), proposeStrat(L321), upgradeStrat(L355), inCaseTokensGetStuck(L391)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/BIFI/vaults/BeefyVaultV7Factory.sol` (39 lines)
- Entry points: cloneVault(L29), cloneContract(L34)
- `delegatecall` / `selfdestruct` / `.call(`: -

## `contracts/BIFI/vaults/BeefyVaultV7Native.sol` (257 lines)
- Entry points: want(L59), balance(L68), available(L78), getPricePerFullShare(L86), depositAll(L93), deposit(L101), depositBNB(L122), earn(L144), withdrawAll(L153), withdrawAllBNB(L160), withdraw(L169), withdrawBNB(L191), proposeStrat(L214), upgradeStrat(L231), inCaseTokensGetStuck(L249)
- `delegatecall` / `selfdestruct` / `.call(`: -
