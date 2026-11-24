# 2026-11-24 — Upstream Beefy Contracts & On-Chain Bytecode Verification

## 1. Polygon In-Scope On-Chain Status
| Track | Slug | Address | Runtime Bytecode (bytes) |
| :--- | :--- | :--- | :---: |
| `track-a-zap` | `zap-cometh` | `0x872c9DCE4B107042933AFD51E8A704631f7EE076` | -1 |
| `track-a-zap` | `zap-quickswap` | `0x540A9f99bB730631BF243a34B19fd00BA8CF315C` | -1 |
| `track-a-zap` | `zap-dyfn` | `0x1A53c6FCa349c23f573CEdd3F8AFE70c02CcEC39` | -1 |
| `track-a-zap` | `zap-apeswap` | `0xaAa3477c6b326e2E416Af7506A30F4519bC9960F` | -1 |
| `track-a-zap` | `zap-wault` | `0x0EA7b115D96C4dF61B3e7d6757f0050F23492929` | -1 |
| `track-a-zap` | `zap-sushi` | `0xf039fe26456901F863c873556f40fb207C6c9C18` | -1 |
| `track-b-vault` | `cometh-usdc-must-vault` | `0x8a198BCbF313A5565c64A7Ed61FaA413eB4E0931` | -1 |
| `track-b-strategy` | `cometh-usdc-must-strategy` | `0xf6fD90FE8f057a63F0368B0B551D5e52C7Ae821F` | -1 |
| `track-b-vault` | `cometh-matic-must-vault` | `0x7f6fE34C51d5352A0CF375C0Fbe03bD19eCD8460` | -1 |
| `track-b-strategy` | `cometh-matic-must-strategy` | `0xA338D34c5de06B88197609956a2dEAAfF7Af46c8` | -1 |
| `track-b-vault` | `cometh-eth-matic-vault` | `0xa5aaE3a55cA356C62b5425AA4bFC212542B17777` | -1 |
| `track-b-strategy` | `cometh-eth-matic-strategy` | `0xb0F9c6FBcfE226EEAD3AE8b019ce4666cE223a78` | -1 |

## 2. Fetched Upstream Solidity Files & Entry Points
- **`contracts/upstream-beefy/beefy-contracts/contracts/BIFI/interfaces/beefy/IBeefyVaultConcLiq.sol`** (15 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/BIFI/vaults/BeefyVaultV7.sol`** (404 lines)
  - Entry Points: `initialize, depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/BIFI/vaults/BeefyVaultV7Factory.sol`** (39 lines)
  - Entry Points: `cloneVault, cloneContract`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/BIFI/vaults/BeefyVaultV7Native.sol`** (257 lines)
  - Entry Points: `initialize, depositAll, deposit, depositBNB, earn, withdrawAll, withdrawAllBNB, withdraw, withdrawBNB, proposeStrat, upgradeStrat, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/infra/FlatBeefyZap.sol`** (998 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap`
  - Sinks: `.call, addLiquidity, addLiquidityETH, approve, getReserves, removeLiquidity, removeLiquidityETH, removeLiquidityETHSupportingFeeOnTransferTokens, removeLiquidityETHWithPermit, removeLiquidityETHWithPermitSupportingFeeOnTransferTokens, removeLiquidityWithPermit, safeApprove, safeTransfer, safeTransferFrom, swapExactETHForTokens, swapExactETHForTokensSupportingFeeOnTransferTokens, swapExactTokensForETH, swapExactTokensForETHSupportingFeeOnTransferTokens, swapExactTokensForTokens, swapExactTokensForTokensSupportingFeeOnTransferTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/interfaces/gmx/IBeefyVault.sol`** (12 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/keepers/interfaces/IBeefyVault.sol`** (26 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Cake/StratManagerCake.sol`** (82 lines)
  - Entry Points: `setKeeper, setUnirouter, setVault, setBeefyFeeRecipient, beforeDeposit`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol`** (442 lines)
  - Entry Points: `deposit, withdraw, harvest, retireStrat, panic, pause, unpause`
  - Sinks: `addLiquidity, safeApprove, safeTransfer, swapExactTokensForTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol`** (420 lines)
  - Entry Points: `deposit, withdraw, harvest, retireStrat, panic, pause, unpause`
  - Sinks: `addLiquidity, safeApprove, safeTransfer, swapExactTokensForTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Common/StratManager.sol`** (96 lines)
  - Entry Points: `setKeeper, setStrategist, setUnirouter, setVault, setBeefyFeeRecipient, beforeDeposit`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Curve/ConicZap.sol`** (132 lines)
  - Entry Points: `beefInETH, beefIn, beefOutAndSwap`
  - Sinks: `.call, safeApprove, safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/degens/StrategyPolyzapLP.sol`** (218 lines)
  - Entry Points: `deposit, withdraw, harvest, retireStrat, panic, pause, unpause`
  - Sinks: `addLiquidity, safeApprove, safeTransfer, swapExactTokensForTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultBNB.sol`** (250 lines)
  - Entry Points: `depositAll, deposit, depositBNB, earn, withdrawAll, withdrawAllBNB, withdraw, withdrawBNB, proposeStrat, upgradeStrat`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultCapped.sol`** (221 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat, increaseDepositCap, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV2.sol`** (193 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV3.sol`** (193 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV4.sol`** (193 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV5.sol`** (202 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV6.sol`** (203 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV6Matic.sol`** (256 lines)
  - Entry Points: `depositAll, deposit, depositBNB, earn, withdrawAll, withdrawAllBNB, withdraw, withdrawBNB, proposeStrat, upgradeStrat, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV6Native.sol`** (258 lines)
  - Entry Points: `depositAll, deposit, depositBNB, earn, withdrawAll, withdrawAllBNB, withdraw, withdrawBNB, proposeStrat, upgradeStrat, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultv6Moonpot.sol`** (228 lines)
  - Entry Points: `depositAll, deposit, earn, withdrawAll, withdraw, proposeStrat, upgradeStrat, setOnlyMoonpot, setMoonpot, inCaseTokensGetStuck`
  - Sinks: `safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyPairFeeDataSource.sol`** (47 lines)
  - Entry Points: `setUpAFactory, setUpASolidFactory`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyUniV2ZapSolidly.sol`** (953 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap`
  - Sinks: `.call, addLiquidity, addLiquidityETH, approve, getReserves, removeLiquidity, removeLiquidityETH, safeApprove, safeTransfer, safeTransferFrom, swapExactTokensForTokensSimple`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyVelodromeV2Zap.sol`** (221 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap`
  - Sinks: `.call, addLiquidity, getReserves, safeApprove, safeTransfer, safeTransferFrom, swapExactTokensForTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyZapKyber.sol`** (273 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap, beefOutAndReInvest`
  - Sinks: `.call, addLiquidity, delegatecall, safeApprove, safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyZapMdex.sol`** (214 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap`
  - Sinks: `.call, addLiquidity, getReserves, safeApprove, safeTransfer, safeTransferFrom, swapExactTokensForTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyZapOneInch.sol`** (325 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap, beefOutAndReInvest`
  - Sinks: `.call, addLiquidity, delegatecall, safeApprove, safeTransfer, safeTransferFrom`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyZapSolidlyDyst.sol`** (237 lines)
  - Entry Points: `beefInETH, beefIn, beefOut, beefOutAndSwap`
  - Sinks: `.call, addLiquidity, getReserves, safeApprove, safeTransfer, safeTransferFrom, swapExactTokensForTokensSimple`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/IBeefyDataSource.sol`** (13 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/ZapBeFtmOneInch.sol`** (95 lines)
  - Entry Points: `depositNative, inCaseTokensGetStuck`
  - Sinks: `.call, delegatecall, safeApprove, safeTransfer`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/ZapBeVelo.sol`** (64 lines)
  - Entry Points: `deposit, inCaseTokensGetStuck`
  - Sinks: `.call, safeApprove, safeTransfer, safeTransferFrom, swapExactTokensForTokens`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/libs/Babylonian.sol`** (35 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/zapInterfaces/IBeefyVault.sol`** (14 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/zapInterfaces/IERC20Extended.sol`** (7 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/zapInterfaces/IStrategy.sol`** (7 lines)
  - Entry Points: `-`
  - Sinks: `-`
- **`contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/zapInterfaces/IWETH.sol`** (8 lines)
  - Entry Points: `-`
  - Sinks: `-`
