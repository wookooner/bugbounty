files = [
    ("targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/strategies/degens/StrategyPolyzapLP.sol", 1, 218),
    ("targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/vaults/BeefyVaultV6Matic.sol", 90, 220),
    ("targets/beefyfinance/contracts/upstream-beefy/beefy-contracts/contracts/archive/zaps/BeefyZapKyber.sol", 50, 273),
]

for path, start_ln, end_ln in files:
    print(f"\n==================== {path} (L{start_ln}-L{end_ln}) ====================")
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    for ln in range(start_ln, min(len(lines), end_ln) + 1):
        print(f"{ln:4d}: {lines[ln - 1]}")
