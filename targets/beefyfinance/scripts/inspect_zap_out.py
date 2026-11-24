with open(r"targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/infra/FlatBeefyZap.sol", encoding="utf-8") as f:
    lines = f.read().splitlines()

print("=== FlatBeefyZap.sol L830-L905 ===")
for ln in range(830, 906):
    print(f"{ln:4d}: {lines[ln - 1]}")
