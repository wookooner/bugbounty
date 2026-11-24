with open(r"targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol", encoding="utf-8") as f:
    s_lines = f.read().splitlines()

print("=== StrategyMultiRewardsPolygonLP.sol L310-L442 ===")
for ln in range(310, len(s_lines) + 1):
    print(f"{ln:4d}: {s_lines[ln - 1]}")

with open(r"targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV6.sol", encoding="utf-8") as f:
    v_lines = f.read().splitlines()

print("\n=== BeefyVaultV6.sol L80-L203 ===")
for ln in range(80, len(v_lines) + 1):
    print(f"{ln:4d}: {v_lines[ln - 1]}")
