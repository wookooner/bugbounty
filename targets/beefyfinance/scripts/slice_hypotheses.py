import json
import os

BASE_DIR = os.path.join("targets", "beefyfinance")
UPSTREAM_ROOT = os.path.join(BASE_DIR, "contracts", "upstream-beefy", "beefy-contracts")
LOGS_DIR = os.path.join(BASE_DIR, "research_logs")
SLICES_JSON = os.path.join(LOGS_DIR, "2026-11-24-deep-audit-slices.json")

TARGET_FUNCS = {
    "beefInETH", "beefIn", "beefOut", "beefOutAndSwap",
    "harvest", "withdraw", "deposit", "panic", "retireStrat",
    "earn", "withdrawAll", "proposeStrat", "upgradeStrat"
}


def main():
    with open(SLICES_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    out_lines = [
        "# 2026-11-24 — Hypothesis-Oriented Function & Sink Slices",
        "",
    ]

    for item in data:
        rel_path = item["file"]
        full_path = os.path.join(UPSTREAM_ROOT, os.path.normpath(rel_path))
        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()

        out_lines.append(f"## `{rel_path}`")
        all_fn_names = [f"`{fn['name']}`(L{fn['line']})" for fn in item.get("functions", [])]
        out_lines.append("- All functions/constructors: " + (", ".join(all_fn_names) if all_fn_names else "-"))

        matched = [fn for fn in item.get("functions", []) if fn["name"] in TARGET_FUNCS]
        for fn in matched:
            start = max(1, fn["line"] - 1)
            end = min(len(lines), fn["line"] + 45)
            out_lines.append(f"\n### `{fn['name']}` (starts L{fn['line']}, showing L{start}–L{end})")
            out_lines.append("```solidity")
            for ln in range(start, end + 1):
                out_lines.append(f"{ln:4d}: {lines[ln - 1]}")
            out_lines.append("```")
        out_lines.append("")

    out_md = os.path.join(LOGS_DIR, "2026-11-24-hypothesis-slices.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))

    print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()
