import json
import os
import re

BASE_DIR = os.path.join("targets", "beefyfinance")
UPSTREAM_ROOT = os.path.join(BASE_DIR, "contracts", "upstream-beefy", "beefy-contracts")
LOGS_DIR = os.path.join(BASE_DIR, "research_logs")

SELECTIONS = {
    "contracts/archive/infra/FlatBeefyZap.sol": [
        "beefInETH", "beefIn", "beefOut", "beefOutAndSwap",
        "_removeLiqudity", "_getVaultPair", "_swapAndStake",
        "_returnAssets", "_getSwapAmount", "_approveTokenIfNeeded"
    ],
    "contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol": [
        "deposit", "withdraw", "harvest", "chargeFees",
        "addLiquidity", "balanceOf", "retireStrat", "panic"
    ],
    "contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol": [
        "deposit", "withdraw", "harvest", "chargeFees",
        "addLiquidity", "balanceOf", "retireStrat", "panic"
    ],
    "contracts/archive/vaults/BeefyVaultV6.sol": [
        "balance", "available", "getPricePerFullShare",
        "deposit", "earn", "withdraw", "proposeStrat", "upgradeStrat"
    ],
}


def extract_block(lines: list[str], start_line_1based: int) -> tuple[int, int, str]:
    idx = start_line_1based - 1
    n = len(lines)
    depth = 0
    found_open = False
    end_idx = min(n - 1, idx + 80)

    for i in range(idx, min(n, idx + 220)):
        line = lines[i]
        for ch in line:
            if ch == "{":
                depth += 1
                found_open = True
            elif ch == "}":
                depth -= 1
        if found_open and depth <= 0:
            end_idx = i
            break

    snippet = []
    for ln in range(idx + 1, end_idx + 2):
        snippet.append(f"{ln:4d}: {lines[ln - 1]}")
    return idx + 1, end_idx + 1, "\n".join(snippet)


def main():
    out_lines = [
        "# 2026-11-24 — Complete Function Bodies for Hypothesis Audit",
        "",
    ]

    for rel_path, target_names in SELECTIONS.items():
        full_path = os.path.join(UPSTREAM_ROOT, os.path.normpath(rel_path))
        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()

        out_lines.append(f"## `{rel_path}`")
        for fn_name in target_names:
            pat = re.compile(rf"^\s*function\s+{re.escape(fn_name)}\s*\(")
            matches = [i for i, l in enumerate(lines, start=1) if pat.match(l)]
            for start_ln in matches:
                s, e, body = extract_block(lines, start_ln)
                out_lines.append(f"\n### `{fn_name}` (L{s}–L{e})")
                out_lines.append("```solidity")
                out_lines.append(body)
                out_lines.append("```")
        out_lines.append("")

    out_path = os.path.join(LOGS_DIR, "2026-11-24-full-fn-bodies.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
