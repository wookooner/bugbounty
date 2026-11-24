# Beefy Finance Bug Bounty Scope

- **Program URL**: https://immunefi.com/bug-bounty/beefyfinance/information/
- **Last Updated**: 2026-11-20
- **Adjudication**: Primacy of Rules
- **Max Bounty**: $75,000 USD (Smart Contract Critical Flat: $75,000 / High: $15,000 / Medium: $2,000 / Low: $500)
- **Payout & KYC**: Paid in stablecoin, BTC, or ETH on Ethereum (USD-denominated) / KYC Not Required
- **Mandatory Submission Rules**:
  1. Runnable PoC required for ALL severities (Critical, High, Medium, Low).
  2. Suggestion on how to fix the vulnerability required for ALL reports.
  3. Testing MUST be performed ONLY on local forks of mainnet/testnet.

## Core System Invariant
- Users' funds are never locked in any Vault on Beefy Finance: users must always be able to withdraw at any moment in time.

## In-Scope Smart Contracts (Polygon)
### Zap Contracts (Track A - Priority 1)
- `Zap DYFN`: `0x1A53c6FCa349c23f573CEdd3F8AFE70c02CcEC39`
- `Zap ApeSwap`: `0xaAa3477c6b326e2E416Af7506A30F4519bC9960F`
- `Zap Wault`: `0x0EA7b115D96C4dF61B3e7d6757f0050F23492929`
- `Zap Sushi`: `0xf039fe26456901F863c873556f40fb207C6c9C18`
- `Zap Cometh`: `0x872c9DCE4B107042933AFD51E8A704631f7EE076`
- `Zap QuickSwap`: `0x540A9f99bB730631BF243a34B19fd00BA8CF315C`

### Vault & Strategy Pairs (Track B - Priority 2)
- `cometh-usdc-must` Vault: `0x8a198BCbF313A5565c64A7Ed61FaA413eB4E0931`
- `cometh-usdc-must` Strategy: `0xf6fD90FE8f057a63F0368B0B551D5e52C7Ae821F`
- `cometh-matic-must` Vault: `0x7f6fE34C51d5352A0CF375C0Fbe03bD19eCD8460`
- `cometh-matic-must` Strategy: `0xA338D34c5de06B88197609956a2dEAAfF7Af46c8`
- `cometh-eth-matic` Vault: `0xa5aaE3a55cA356C62b5425AA4bFC212542B17777`
- `cometh-eth-matic` Strategy: `0xb0F9c6FBcfE226EEAD3AE8b019ce4666cE223a78`

## Accepted Impacts & Boundaries
- **Critical**: Governance voting manipulation, direct theft of user funds (at-rest or in-motion), permanent freezing of funds, MEV exploitation, protocol insolvency.
- **High**: Theft or permanent freezing of unclaimed yield, temporary freezing of funds.
- **Medium**: Contract unable to operate due to lack of token funds, block stuffing for profit, griefing, theft of gas.
- **Included Vectors**: Oracle manipulation and flash loan attacks are explicitly NOT excluded.
- **Out of Scope**: Attacks requiring privileged access (governance/strategist) without privilege escalation, best practice critiques, 51%/Sybil/lack-of-liquidity/centralization risks, external stablecoin depeg not caused by code bug.