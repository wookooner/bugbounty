with open(r"targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyZapOneInch.sol", encoding="utf-8") as f:
    lines = f.read().splitlines()

for idx, line in enumerate(lines, start=1):
    print(f"{idx:4d}: {line}")
