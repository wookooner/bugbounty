import json
import os
import re
import urllib.request

TARGETS = [
    ("track-a-zap", "zap-cometh", "0x872c9DCE4B107042933AFD51E8A704631f7EE076"),
    ("track-a-zap", "zap-quickswap", "0x540A9f99bB730631BF243a34B19fd00BA8CF315C"),
    ("track-a-zap", "zap-dyfn", "0x1A53c6FCa349c23f573CEdd3F8AFE70c02CcEC39"),
    ("track-a-zap", "zap-apeswap", "0xaAa3477c6b326e2E416Af7506A30F4519bC9960F"),
    ("track-a-zap", "zap-wault", "0x0EA7b115D96C4dF61B3e7d6757f0050F23492929"),
    ("track-a-zap", "zap-sushi", "0xf039fe26456901F863c873556f40fb207C6c9C18"),
    ("track-b-vault", "cometh-usdc-must-vault", "0x8a198BCbF313A5565c64A7Ed61FaA413eB4E0931"),
    ("track-b-strategy", "cometh-usdc-must-strategy", "0xf6fD90FE8f057a63F0368B0B551D5e52C7Ae821F"),
    ("track-b-vault", "cometh-matic-must-vault", "0x7f6fE34C51d5352A0CF375C0Fbe03bD19eCD8460"),
    ("track-b-strategy", "cometh-matic-must-strategy", "0xA338D34c5de06B88197609956a2dEAAfF7Af46c8"),
    ("track-b-vault", "cometh-eth-matic-vault", "0xa5aaE3a55cA356C62b5425AA4bFC212542B17777"),
    ("track-b-strategy", "cometh-eth-matic-strategy", "0xb0F9c6FBcfE226EEAD3AE8b019ce4666cE223a78"),
]

BASE_DIR = os.path.join("targets", "beefyfinance")
CONTRACTS_DIR = os.path.join(BASE_DIR, "contracts")
LOGS_DIR = os.path.join(BASE_DIR, "research_logs")
API_KEY = os.environ.get("ETHERSCAN_API_KEY") or os.environ.get("POLYGONSCAN_API_KEY") or ""


def http_get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (AuditIntake/1.0)"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def safe_write(root: str, rel_name: str, content: str):
    clean = os.path.normpath(rel_name).lstrip("/\\")
    if clean.startswith(".."):
        clean = os.path.basename(clean)
    dest = os.path.join(root, clean)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)
    return dest


def fetch_from_sourcify(address: str, out_dir: str) -> list[str]:
    url = f"https://sourcify.dev/server/files/any/137/{address}"
    try:
        data = http_get_json(url)
    except Exception:
        return []
    files = data.get("files", [])
    saved = []
    for item in files:
        name = item.get("name", "")
        content = item.get("content", "")
        if name.endswith(".sol") and content:
            saved.append(safe_write(out_dir, name, content))
    return saved


def fetch_from_explorer(address: str, contract_name: str, out_dir: str) -> list[str]:
    if not API_KEY:
        return []
    url = (
        f"https://api.etherscan.io/v2/api?chainid=137"
        f"&module=contract&action=getsourcecode&address={address}&apikey={API_KEY}"
    )
    try:
        data = http_get_json(url)
    except Exception:
        return []
    result = data.get("result")
    if not isinstance(result, list) or not result:
        return []
    src = result[0].get("SourceCode", "")
    if not src:
        return []
    saved = []
    if src.startswith("{{") and src.endswith("}}"):
        try:
            parsed = json.loads(src[1:-1])
            sources = parsed.get("sources", {})
            for path, meta in sources.items():
                if path.endswith(".sol") and "content" in meta:
                    saved.append(safe_write(out_dir, path, meta["content"]))
            return saved
        except Exception:
            pass
    saved.append(safe_write(out_dir, f"{contract_name}.sol", src))
    return saved


def analyze_solidity_files(file_paths: list[str]) -> dict:
    contracts = []
    entry_points = []
    sinks = []
    sink_pattern = re.compile(
        r"\b(safeApprove|approve|safeTransfer|safeTransferFrom|swapExact\w+|addLiquidity\w*|removeLiquidity\w*|getReserves|delegatecall|\.call)\b"
    )
    func_pattern = re.compile(
        r"function\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)\s*([^{;]*)\{"
    )
    contract_pattern = re.compile(r"\b(contract|abstract\s+contract)\s+([A-Za-z0-9_]+)(?:\s+is\s+([^{]+))?\{")

    for fp in sorted(file_paths):
        rel_fp = os.path.relpath(fp, BASE_DIR)
        with open(fp, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        lines = text.splitlines()

        for m in contract_pattern.finditer(text):
            contracts.append({
                "name": m.group(2),
                "inherits": (m.group(3) or "").strip(),
                "file": rel_fp,
            })

        for m in func_pattern.finditer(text):
            fname = m.group(1)
            params = " ".join(m.group(2).split())
            quals = " ".join(m.group(3).split())
            if "external" in quals or "public" in quals:
                if "view" not in quals and "pure" not in quals:
                    line_no = text[: m.start()].count("\n") + 1
                    entry_points.append({
                        "function": fname,
                        "params": params,
                        "qualifiers": quals,
                        "file": rel_fp,
                        "line": line_no,
                    })

        for idx, line in enumerate(lines, start=1):
            stripped = line.strip()
            if stripped.startswith("//") or stripped.startswith("*"):
                continue
            found = sink_pattern.findall(stripped)
            if found:
                sinks.append({
                    "file": rel_fp,
                    "line": idx,
                    "ops": sorted(set(found)),
                    "code": stripped[:140],
                })

    return {
        "contracts": contracts,
        "state_mutating_entrypoints": entry_points,
        "external_sinks": sinks[:60],
    }


def main():
    summary = []
    for track, slug, addr in TARGETS:
        target_dir = os.path.join(CONTRACTS_DIR, slug)
        os.makedirs(target_dir, exist_ok=True)
        files = fetch_from_sourcify(addr, target_dir)
        source_origin = "sourcify"
        if not files:
            files = fetch_from_explorer(addr, slug, target_dir)
            source_origin = "etherscan_v2" if files else "pending_manual_fetch"

        analysis = analyze_solidity_files(files) if files else {
            "contracts": [],
            "state_mutating_entrypoints": [],
            "external_sinks": [],
        }
        entry = {
            "track": track,
            "slug": slug,
            "address": addr,
            "source_origin": source_origin,
            "file_count": len(files),
            "files": [os.path.relpath(p, BASE_DIR) for p in files],
            "analysis": analysis,
        }
        summary.append(entry)
        print(f"[{source_origin}] {slug} ({addr}) -> {len(files)} .sol files")

    json_path = os.path.join(LOGS_DIR, "2026-11-24-track-a-surface.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "id": "2026-11-24-track-a-surface",
                "date": "2026-11-24",
                "target": "beefyfinance",
                "phase": "source_and_surface_mapping",
                "results": summary,
            },
            f,
            indent=2,
        )

    md_lines = [
        "# 2026-11-24 — Track A & B Source Acquisition and Entry-Point Surface",
        "",
        "| Track | Target | Address | Source | .sol Files | State-Mutating Entry Points |",
        "| :--- | :--- | :--- | :--- | :---: | :--- |",
    ]
    for item in summary:
        eps = ", ".join(e["function"] for e in item["analysis"]["state_mutating_entrypoints"]) or "-"
        md_lines.append(
            f"| `{item['track']}` | `{item['slug']}` | `{item['address']}` | `{item['source_origin']}` | {item['file_count']} | {eps} |"
        )

    md_lines.append("\n## Track A — Zap Entry Points & Sink Details\n")
    for item in summary:
        if item["track"] != "track-a-zap":
            continue
        md_lines.append(f"### {item['slug']} (`{item['address']}`)")
        if not item["files"]:
            md_lines.append("- Source not fetched yet (set `ETHERSCAN_API_KEY` or save verified Solidity manually).\n")
            continue
        for ep in item["analysis"]["state_mutating_entrypoints"]:
            md_lines.append(f"- `{ep['function']}({ep['params']})` [{ep['qualifiers']}] — `{ep['file']}:{ep['line']}`")
        md_lines.append("")

    md_path = os.path.join(LOGS_DIR, "2026-11-24-track-a-surface.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")


if __name__ == "__main__":
    main()
