with open(r"targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/infra/FlatBeefyZap.sol", encoding="utf-8") as f:
    zap_lines = f.read().splitlines()

print("=== FlatBeefyZap.sol L895-L998 ===")
for ln in range(895, len(zap_lines) + 1):
    print(f"{ln:4d}: {zap_lines[ln - 1]}")

with open(r"targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol", encoding="utf-8") as f:
    str_lines = f.read().splitlines()

print("\n=== StrategyMultiRewardsPolygonLP.sol L1-L225 ===")
for ln in range(1, min(226, len(str_lines) + 1)):
    print(f"{ln:4d}: {str_lines[ln - 1]}")
