import json
import os
import re
import urllib.request

BASE_DIR = os.path.join("targets", "beefyfinance")
CONTRACTS_DIR = os.path.join(BASE_DIR, "contracts")
UPSTREAM_DIR = os.path.join(CONTRACTS_DIR, "upstream-beefy")
LOGS_DIR = os.path.join(BASE_DIR, "research_logs")

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

# Beefy 공식 GitHub 저장소에서 Zap, Vault, Cometh Strategy 관련 파일 경로 탐색 및 다운로드
UPSTREAM_REPOS = [
    ("beefyfinance/beefy-contracts", "master"),
    ("beefyfinance/beefy-zap", "main"),
    ("beefyfinance/beefy-zap", "master"),
]

KEYWORDS = ("zap", "vaultv6", "beefyvault", "cometh", "stratmanager", "feeutil")


def http_get_text(url: str, headers: dict | None = None) -> str:
    hdrs = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_upstream_github() -> list[str]:
    saved = []
    for repo, branch in UPSTREAM_REPOS:
        tree_url = f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1"
        try:
            raw = http_get_text(tree_url, {"Accept": "application/vnd.github+json"})
            tree = json.loads(raw).get("tree", [])
        except Exception as e:
            print(f"[GitHub Tree Skip] {repo}@{branch}: {e}")
            continue

        for node in tree:
            path = node.get("path", "")
            if not path.endswith(".sol"):
                continue
            low = path.lower()
            if any(k in low for k in KEYWORDS):
                raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"
                try:
                    code = http_get_text(raw_url)
                    repo_slug = repo.split("/")[1]
                    dest = os.path.join(UPSTREAM_DIR, repo_slug, os.path.normpath(path))
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    with open(dest, "w", encoding="utf-8") as f:
                        f.write(code)
                    saved.append(dest)
                    print(f"[GitHub] {repo_slug}/{path}")
                except Exception as e:
                    print(f"[GitHub File Err] {path}: {e}")
    return saved


def fetch_polygon_rpc_code_size(address: str) -> int:
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "eth_getCode",
        "params": [address, "latest"],
        "id": 1,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://polygon-rpc.com",
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            code = data.get("result", "0x")
            return max(0, (len(code) - 2) // 2)
    except Exception:
        return -1


def analyze_solidity_files(file_paths: list[str]) -> list[dict]:
    results = []
    func_pattern = re.compile(r"function\s+([A-Za-z0-9_]+)\s*\(([^)]*)\)\s*([^{;]*)\{")
    sink_pattern = re.compile(
        r"\b(safeApprove|approve|safeTransfer|safeTransferFrom|swapExact\w+|addLiquidity\w*|removeLiquidity\w*|getReserves|delegatecall|\.call)\b"
    )
    for fp in sorted(file_paths):
        rel = os.path.relpath(fp, BASE_DIR).replace("\\", "/")
        with open(fp, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        eps = []
        for m in func_pattern.finditer(text):
            quals = " ".join(m.group(3).split())
            if ("external" in quals or "public" in quals) and "view" not in quals and "pure" not in quals:
                eps.append({
                    "function": m.group(1),
                    "params": " ".join(m.group(2).split()),
                    "qualifiers": quals,
                    "line": text[: m.start()].count("\n") + 1,
                })
        sinks = sorted(set(sink_pattern.findall(text)))
        results.append({
            "file": rel,
            "lines": len(text.splitlines()),
            "entrypoints": eps,
            "sinks": sinks,
        })
    return results


def main():
    saved_files = fetch_upstream_github()
    analyzed = analyze_solidity_files(saved_files)

    onchain_status = []
    for track, slug, addr in TARGETS:
        byte_len = fetch_polygon_rpc_code_size(addr)
        onchain_status.append({
            "track": track,
            "slug": slug,
            "address": addr,
            "polygon_runtime_bytes": byte_len,
        })
        print(f"[RPC] {slug} ({addr}) -> {byte_len} bytes")

    out_json = os.path.join(LOGS_DIR, "2026-11-24-upstream-surface.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(
            {
                "id": "2026-11-24-upstream-surface",
                "date": "2026-11-24",
                "target": "beefyfinance",
                "onchain_targets": onchain_status,
                "upstream_files_count": len(analyzed),
                "upstream_analysis": analyzed,
            },
            f,
            indent=2,
        )

    md = [
        "# 2026-11-24 — Upstream Beefy Contracts & On-Chain Bytecode Verification",
        "",
        "## 1. Polygon In-Scope On-Chain Status",
        "| Track | Slug | Address | Runtime Bytecode (bytes) |",
        "| :--- | :--- | :--- | :---: |",
    ]
    for item in onchain_status:
        md.append(f"| `{item['track']}` | `{item['slug']}` | `{item['address']}` | {item['polygon_runtime_bytes']} |")

    md.append("\n## 2. Fetched Upstream Solidity Files & Entry Points")
    if not analyzed:
        md.append("- No files fetched.")
    for f_info in analyzed:
        ep_names = ", ".join(e["function"] for e in f_info["entrypoints"]) or "-"
        sink_names = ", ".join(f_info["sinks"]) or "-"
        md.append(f"- **`{f_info['file']}`** ({f_info['lines']} lines)")
        md.append(f"  - Entry Points: `{ep_names}`")
        md.append(f"  - Sinks: `{sink_names}`")

    out_md = os.path.join(LOGS_DIR, "2026-11-24-upstream-surface.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")


if __name__ == "__main__":
    main()
