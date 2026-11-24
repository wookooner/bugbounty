import json
import os
import re

BASE_DIR = os.path.join("targets", "beefyfinance")
UPSTREAM_ROOT = os.path.join(BASE_DIR, "contracts", "upstream-beefy", "beefy-contracts")
LOGS_DIR = os.path.join(BASE_DIR, "research_logs")

FOCUS_FILES = [
    "contracts/archive/infra/FlatBeefyZap.sol",
    "contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol",
    "contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol",
    "contracts/archive/vaults/BeefyVaultV6.sol",
]

FUNC_DECL_RE = re.compile(r"^\s*(?:function\s+([A-Za-z0-9_]+)|constructor)\s*\(")
SINK_LINE_RE = re.compile(
    r"\b(safeApprove|approve|safeTransfer|safeTransferFrom|swapExact\w+|addLiquidity\w*|removeLiquidity\w*|getReserves|delegatecall|\.call\(|_swap|_addLiquidity|_removeLiquidity|balanceOf)\b"
)


def extract_function_signatures(lines: list[str]) -> list[dict]:
    funcs = []
    for idx, line in enumerate(lines, start=1):
        m = FUNC_DECL_RE.match(line)
        if m:
            name = m.group(1) or "constructor"
            header = " ".join(lines[idx - 1 : min(len(lines), idx + 4)]).strip()
            funcs.append({"line": idx, "name": name, "header": header})
    return funcs


def extract_sink_windows(lines: list[str], radius: int = 8) -> list[dict]:
    windows = []
    covered = set()
    for idx, line in enumerate(lines, start=1):
        if SINK_LINE_RE.search(line):
            start = max(1, idx - radius)
            end = min(len(lines), idx + radius)
            key = (start, end)
            if key in covered:
                continue
            covered.add(key)
            snippet = []
            for ln in range(start, end + 1):
                mark = ">>" if ln == idx else "  "
                snippet.append(f"{mark} {ln:4d}: {lines[ln - 1]}")
            windows.append({
                "sink_line": idx,
                "start": start,
                "end": end,
                "snippet": "\n".join(snippet),
            })
    return windows


def main():
    report_lines = [
        "# 2026-11-24 — Deep Audit Slices (Entry Points & Sink Windows)",
        "",
    ]
    json_out = []

    for rel_path in FOCUS_FILES:
        full_path = os.path.join(UPSTREAM_ROOT, os.path.normpath(rel_path))
        if not os.path.exists(full_path):
            report_lines.append(f"## `{rel_path}` (MISSING)")
            continue

        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()

        funcs = extract_function_signatures(lines)
        windows = extract_sink_windows(lines, radius=8)

        json_out.append({
            "file": rel_path,
            "total_lines": len(lines),
            "functions": funcs,
            "sink_windows": windows,
        })

        report_lines.append(f"## `{rel_path}` ({len(lines)} lines)")
        report_lines.append("### Functions / Constructors")
        for fn in funcs:
            report_lines.append(f"- L{fn['line']}: `{fn['name']}` — `{fn['header'][:160]}`")

        report_lines.append("\n### Sink Windows (±8 lines)")
        for w in windows:
            report_lines.append(f"#### Line {w['sink_line']} (L{w['start']}–L{w['end']})")
            report_lines.append("```solidity")
            report_lines.append(w["snippet"])
            report_lines.append("```\n")

    with open(os.path.join(LOGS_DIR, "2026-11-24-deep-audit-slices.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    with open(os.path.join(LOGS_DIR, "2026-11-24-deep-audit-slices.json"), "w", encoding="utf-8") as f:
        json.dump(json_out, f, indent=2)

    print(f"Generated deep audit slices for {len(json_out)} focus files.")


if __name__ == "__main__":
    main()
