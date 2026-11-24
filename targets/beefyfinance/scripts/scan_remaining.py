import os
import re

UPSTREAM_ROOT = os.path.join("targets", "beefyfinance", "contracts", "upstream-beefy", "beefy-contracts")
LOGS_DIR = os.path.join("targets", "beefyfinance", "research_logs")

ALREADY_REVIEWED = {
    "contracts/archive/infra/FlatBeefyZap.sol",
    "contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol",
    "contracts/archive/vaults/BeefyVaultV6.sol",
}

ENTRY_RE = re.compile(r"^\s*function\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)\s*([^{;]*)\{")
SINK_RE = re.compile(r"\b(delegatecall|selfdestruct|suicide|safeApprove|approve|safeTransfer|safeTransferFrom|swapExact\w+|addLiquidity\w*|removeLiquidity\w*|\.call\b)")

out_lines = [
    "# 2026-11-24 — Remaining Upstream Files Scan (Entry Points & High-Signal Sinks)",
    "",
]

for root, _, files in os.walk(UPSTREAM_ROOT):
    for fn in sorted(files):
        if not fn.endswith(".sol"):
            continue
        full_path = os.path.join(root, fn)
        rel_path = os.path.relpath(full_path, UPSTREAM_ROOT).replace("\\", "/")
        if rel_path in ALREADY_REVIEWED:
            continue

        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()

        entries = []
        high_sinks = []
        for idx, line in enumerate(lines, start=1):
            m = ENTRY_RE.match(line)
            if m:
                quals = " ".join(m.group(3).split())
                if "external" in quals or "public" in quals:
                    entries.append(f"{m.group(1)}(L{idx})")
            if re.search(r"\b(delegatecall|selfdestruct|\.call\()", line):
                high_sinks.append(f"L{idx}:{line.strip()[:100]}")

        out_lines.append(f"## `{rel_path}` ({len(lines)} lines)")
        out_lines.append("- Entry points: " + (", ".join(entries) if entries else "-"))
        out_lines.append("- `delegatecall` / `selfdestruct` / `.call(`: " + (", ".join(high_sinks) if high_sinks else "-"))
        out_lines.append("")

out_path = os.path.join(LOGS_DIR, "2026-11-24-remaining-scan.md")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Wrote {out_path}")
for ln in out_lines:
    if ln.startswith("## `") or "delegatecall" in ln or "Entry points:" in ln:
        print(ln)
