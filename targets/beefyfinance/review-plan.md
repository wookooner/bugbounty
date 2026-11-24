# Beefy Finance Review Plan

## Phase 1: Target Intake & Boundary Lock (Done)
- Lock official rules, payout conditions, and Polygon contract addresses in `scope.md`.

## Phase 2: Track A — Zap Contracts Audit (Start Here)
- **Targets**: `Zap Cometh` (`0x872c...E076`) & `Zap QuickSwap` (`0x540A...315C`) first, then diff against remaining 4 Zaps (`DYFN`, `ApeSwap`, `Wault`, `Sushi`).
- **Hypotheses to Test**:
  1. `H-ZAP-01`: Does `beefIn` / `beefInETH` enforce user-supplied slippage bounds on the internal single-sided swap, or is it vulnerable to sandwich/MEV extraction?
  2. `H-ZAP-02`: Are residual swap tokens (dust) properly refunded to `msg.sender`, or can a subsequent caller sweep leftover balances/approvals?
  3. `H-ZAP-03`: Can arbitrary external calls or unvalidated pair/router addresses drain approved user tokens?

## Phase 3: Track B — Vault & Strategy Accounting & Withdrawal Invariant
- **Targets**: `cometh-usdc-must` Vault (`0x8a19...0931`) & Strategy (`0xf6fD...821F`) as baseline, followed by `cometh-matic-must` and `cometh-eth-matic`.
- **Hypotheses to Test**:
  1. `H-VLT-01`: Can a first depositor or direct token donation inflate `getPricePerFullShare()` and cause share rounding theft?
  2. `H-STR-01`: Under `withdraw()` / `withdrawAll()` / `panic()`, can external farm reward claim reverts or fee rounding block user withdrawals (Permanent/Temporary Freezing)?
  3. `H-STR-02`: In `harvest()`, can flash-loan manipulation of spot AMM reserves extract unclaimed yield or principal?

## Phase 4: Local Fork Verification & Report Packaging
- Build Foundry/Hardhat local Polygon fork tests under `evidence/checks/` for any surviving hypothesis.
- Package report with runnable PoC + concrete code fix suggestion.