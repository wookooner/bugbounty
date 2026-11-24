import json
import os
import re
import time
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright, Error as PlaywrightError

BASE_URL = "https://immunefi.com"
LIST_URL = "https://immunefi.com/bug-bounty/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_JSON_PATH = os.path.join(BASE_DIR, "immunefi_full_raw.json")
MASTER_INDEX_PATH = os.path.join(BASE_DIR, "immunefi_master_index.md")
AI_DIGEST_PATH = os.path.join(BASE_DIR, "immunefi_for_ai.txt")

RESERVED_SLUGS = {
    "explore", "boost", "search", "leaderboard", "vaults",
    "audit-competition", "bounties", "programs", "favicon",
    "static", "assets", "api", "login", "signup"
}

BOILERPLATE_CUTOFF_MARKERS = [
    "The following vulnerabilities are excluded from the rewards",
    "Responsible Publication",
    "Feasibility Limitation",
]


def is_cloudflare_blocked(page) -> bool:
    try:
        title = page.title().lower()
        if any(k in title for k in ["just a moment", "attention required", "checking your browser"]):
            return True
        body_head = page.locator("body").inner_text(timeout=3000)[:500].lower()
        if "verify you are human" in body_head or "enable javascript and cookies" in body_head:
            return True
    except PlaywrightError:
        return True
    return False


def wait_until_page_ready(page, timeout_sec: int = 45) -> str:
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        if is_cloudflare_blocked(page):
            page.wait_for_timeout(1500)
            continue
        try:
            text = page.locator("body").inner_text(timeout=3000)
            if "404" in page.title() or "this page could not be found" in text.lower():
                return "NOT_FOUND"
            if len(text.strip()) > 300:
                page.wait_for_timeout(1200)
                return "OK"
        except PlaywrightError:
            pass
        page.wait_for_timeout(1000)
    return "BLOCKED"


def safe_goto(page, url: str, retries: int = 3) -> str:
    for attempt in range(1, retries + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            status = wait_until_page_ready(page, timeout_sec=45)
            if status in ("OK", "NOT_FOUND"):
                return status
        except PlaywrightError as e:
            print(f"    [재시도 {attempt}/{retries}] 이동 오류 ({url}): {e}")
        time.sleep(2 * attempt)
    return "BLOCKED"


def is_valid_slug(slug: str) -> bool:
    s = slug.strip().lower()
    return (
        len(s) > 1
        and not s.startswith("_")
        and s not in RESERVED_SLUGS
    )


def discover_all_slugs(page) -> list[str]:
    """
    1) 백그라운드 네트워크 응답(JSON/RSC) 가로채기
    2) 페이지 초기 <script> 내장 데이터 파싱
    3) 마우스 휠 + 내부 스크롤 컨테이너 끝까지 내리기
    """
    slugs = set()

    def handle_response(response):
        try:
            if "immunefi.com" not in response.url:
                return
            ct = response.headers.get("content-type", "")
            if any(t in ct for t in ("json", "text/plain", "javascript")):
                body = response.text()
                for m in re.findall(r"/bug-bounty/([a-zA-Z0-9\-_]+)", body):
                    if is_valid_slug(m):
                        slugs.add(m.lower())
        except Exception:
            pass

    page.on("response", handle_response)

    status = safe_goto(page, LIST_URL)
    if status != "OK":
        raise RuntimeError("메인 목록 페이지 접근 실패 (Cloudflare 차단 지속)")

    # 1. 초기 HTML <script> 내부에 포함된 프로젝트 슬러그 추출
    embedded_slugs = page.evaluate("""
        () => {
            const found = new Set();
            const blob = Array.from(document.querySelectorAll('script'))
                              .map(s => s.textContent || '')
                              .join('\\n');
            for (const m of blob.matchAll(/\\/bug-bounty\\/([a-zA-Z0-9\\-_]+)/g)) {
                found.add(m[1].toLowerCase());
            }
            return Array.from(found);
        }
    """)
    for s in embedded_slugs:
        if is_valid_slug(s):
            slugs.add(s)

    # 2. 화면 중앙에 마우스를 두고 실제 휠 + 내부 스크롤 컨테이너 모두 내리기
    page.mouse.move(720, 500)
    no_new_rounds = 0

    for step in range(1, 250):
        prev_count = len(slugs)

        # Load more / Show more 버튼이 나타나면 클릭
        load_more = page.locator("button:has-text('Load more'), button:has-text('Show more')").first
        try:
            if load_more.count() > 0 and load_more.is_visible():
                load_more.click()
                page.wait_for_timeout(1500)
        except PlaywrightError:
            pass

        # 현재 화면에 렌더링된 <a> 링크 수집
        hrefs = page.evaluate("""
            () => Array.from(document.querySelectorAll("a[href*='/bug-bounty/']"))
                       .map(a => a.getAttribute('href'))
        """)
        for href in hrefs:
            if not href:
                continue
            parts = [p for p in urlparse(urljoin(BASE_URL, href)).path.split("/") if p]
            if len(parts) >= 2 and parts[0] == "bug-bounty" and is_valid_slug(parts[1]):
                slugs.add(parts[1].lower())

        # 마우스 휠 + 내부 스크롤 가능한 모든 요소(overflow-y) 강제 스크롤
        page.mouse.wheel(0, 2000)
        page.evaluate("""
            () => {
                window.scrollBy(0, 1500);
                document.querySelectorAll('*').forEach(el => {
                    if (el.scrollHeight > el.clientHeight + 50) {
                        el.scrollTop += 1500;
                    }
                });
            }
        """)
        page.wait_for_timeout(1200)

        if len(slugs) == prev_count:
            no_new_rounds += 1
            if no_new_rounds >= 12:
                break
        else:
            no_new_rounds = 0
            print(f"  ... 스크롤 진행 중: 현재 {len(slugs)}개 발견")

    page.remove_listener("response", handle_response)
    return sorted(slugs)


def strip_boilerplate(text: str) -> str:
    cleaned = text
    for marker in BOILERPLATE_CUTOFF_MARKERS:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[:idx]
    lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
    return "\n".join(lines)


def extract_max_bounty(info_text: str) -> str:
    m = re.search(r"Max(?:imum)?\s+Bounty\s*\n+\s*(\$[\d,]+(?:\.\d+)?)", info_text, re.IGNORECASE)
    if m:
        return m.group(1)

    rewards_idx = info_text.lower().find("rewards by threat level")
    if rewards_idx != -1:
        sub = info_text[rewards_idx:rewards_idx + 1500]
        m2 = re.search(r"(\$[\d,]+(?:\.\d+)?)", sub)
        if m2:
            return m2.group(1)

    return "Unknown"


def extract_meta_info(info_text: str) -> dict:
    max_bounty = extract_max_bounty(info_text)

    funds_m = re.search(r"Funds available\s*\n+\s*([^\n]+)", info_text, re.IGNORECASE)
    vault_funds = funds_m.group(1).strip() if funds_m else "None"

    updated_m = re.search(r"Last Updated\s*\n+\s*([^\n]+)", info_text, re.IGNORECASE)
    last_updated = updated_m.group(1).strip() if updated_m else ""

    if re.search(r"KYC\s+not\s+required", info_text, re.IGNORECASE):
        kyc = "No"
    elif re.search(r"KYC\s+required", info_text, re.IGNORECASE):
        kyc = "Yes"
    else:
        kyc = "Check"

    pay_to_submit = "Yes" if re.search(r"pay\s+to\s+submit|submission\s+fee", info_text, re.IGNORECASE) else "No"

    if re.search(r"Primacy of Impact", info_text, re.IGNORECASE):
        primacy = "Impact"
    elif re.search(r"Primacy of Rules", info_text, re.IGNORECASE):
        primacy = "Rules"
    else:
        primacy = "-"

    rewards_idx = info_text.lower().find("rewards by threat level")
    reward_slice = info_text[rewards_idx:rewards_idx + 2500] if rewards_idx != -1 else info_text[:3000]
    tokens = sorted(set(re.findall(r"\b(USDC|USDT|DAI|ETH|WETH|WBTC|ARB|OP|SOL|GRT|SSV|DEXE)\b", reward_slice)))

    return {
        "max_bounty": max_bounty,
        "vault_funds": vault_funds,
        "payout_tokens": ", ".join(tokens) if tokens else "Native/Other",
        "kyc": kyc,
        "pay_to_submit": pay_to_submit,
        "primacy": primacy,
        "last_updated": last_updated,
    }


def detect_tech_stack(info_text: str, scope_text: str, urls: list[str]) -> list[str]:
    blob = (info_text + "\n" + scope_text + "\n" + "\n".join(urls)).lower()
    rules = {
        "Solidity": r"solidity|\.sol\b|foundry|hardhat|etherscan|arbiscan|basescan|optimism|polygonscan|bscscan",
        "Rust/Solana": r"\brust\b|\.rs\b|solana|solscan|anchor|cosmwasm",
        "Vyper": r"vyper|\.vy\b",
        "Move": r"\bmove\b|aptos|sui",
        "Go/Cosmos": r"\.go\b|cosmos-sdk|cometbft|tendermint",
        "Clarity": r"clarity|\.clar\b|stacks",
        "Cairo": r"cairo|\.cairo\b|starknet",
        "Web/App": r"web\s*&\s*app|websites\s*and\s*applications|xss|csrf",
    }
    detected = [lang for lang, pat in rules.items() if re.search(pat, blob)]
    return detected if detected else ["Other"]


def extract_scope_links_and_text(page) -> tuple[str, dict]:
    data = page.evaluate("""
        () => {
            const main = document.querySelector('main') || document.body;
            const rawText = main.innerText || '';
            const anchors = Array.from(main.querySelectorAll('a[href]'));
            const links = anchors.map(a => ({
                text: (a.innerText || '').trim(),
                href: a.href
            }));
            return { rawText, links };
        }
    """)

    github_repos = []
    explorer_links = []
    other_assets = []

    explorer_domains = (
        "etherscan.io", "arbiscan.io", "basescan.org", "optimistic.etherscan.io",
        "polygonscan.com", "bscscan.com", "snowtrace.io", "solscan.io",
        "ftmscan.com", "gnosisscan.io", "lineascan.build", "scrollscan.com",
        "blastscan.io", "mantlescan.xyz", "explorer.hiro.so", "hashscan.io"
    )

    for item in data["links"]:
        href = item["href"]
        if not href or "immunefi.com" in href:
            continue

        if "github.com" in href:
            if href not in github_repos:
                github_repos.append(href)
        elif any(dom in href for dom in explorer_domains):
            if href not in explorer_links:
                explorer_links.append(href)
        elif href.startswith("http"):
            if href not in other_assets:
                other_assets.append(href)

    clean_scope = strip_boilerplate(data["rawText"])
    structured_links = {
        "github_repos": github_repos,
        "explorer_links": explorer_links,
        "other_assets": other_assets,
        "total_asset_links": len(github_repos) + len(explorer_links) + len(other_assets),
    }
    return clean_scope, structured_links


def scrape_single_project(page, slug: str) -> dict:
    info_url = f"{BASE_URL}/bug-bounty/{slug}/information/"
    scope_url = f"{BASE_URL}/bug-bounty/{slug}/scope/"

    status = safe_goto(page, info_url)
    if status == "NOT_FOUND":
        return {"slug": slug, "status": "NOT_FOUND"}
    if status != "OK":
        raise RuntimeError("Information 탭 로딩 실패 또는 차단됨")

    try:
        page.wait_for_selector("h1", timeout=10000)
    except PlaywrightError:
        pass

    h1 = page.locator("h1").first
    project_name = h1.inner_text().strip() if h1.count() > 0 else slug

    raw_info = page.evaluate("(document.querySelector('main') || document.body).innerText")

    if re.search(r"this bug bounty program has ended|program is closed|archived program", raw_info, re.IGNORECASE):
        return {"slug": slug, "project_name": project_name, "status": "CLOSED"}

    clean_info = strip_boilerplate(raw_info)
    meta = extract_meta_info(clean_info)

    scope_status = safe_goto(page, scope_url)
    if scope_status == "OK":
        clean_scope, links_data = extract_scope_links_and_text(page)
    else:
        clean_scope = ""
        links_data = {"github_repos": [], "explorer_links": [], "other_assets": [], "total_asset_links": 0}

    all_urls = links_data["github_repos"] + links_data["explorer_links"] + links_data["other_assets"]
    tech_stack = detect_tech_stack(clean_info, clean_scope, all_urls)

    return {
        "slug": slug,
        "status": "ACTIVE",
        "project_name": project_name,
        "info_url": info_url,
        "scope_url": scope_url,
        "meta": meta,
        "tech_stack": tech_stack,
        "links": links_data,
        "information_clean": clean_info,
        "scope_clean": clean_scope,
    }


def load_existing_data() -> dict[str, dict]:
    if not os.path.exists(RAW_JSON_PATH):
        return {}
    try:
        with open(RAW_JSON_PATH, "r", encoding="utf-8") as f:
            items = json.load(f)
        valid_map = {}
        for item in items:
            slug = item.get("slug")
            status = item.get("status")
            if slug and status in ("ACTIVE", "CLOSED", "NOT_FOUND"):
                if status == "ACTIVE" and len(item.get("information_clean", "")) < 200:
                    continue
                valid_map[slug] = item
        return valid_map
    except Exception:
        return {}


def atomic_write_text(filepath: str, content: str):
    tmp_path = filepath + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp_path, filepath)


def save_all_outputs(data_map: dict[str, dict]):
    all_items = list(data_map.values())
    active_items = [x for x in all_items if x.get("status") == "ACTIVE"]

    def bounty_sort_key(item):
        val_str = item.get("meta", {}).get("max_bounty", "0")
        nums = re.sub(r"[^\d.]", "", val_str)
        return float(nums) if nums else 0.0

    active_items.sort(key=bounty_sort_key, reverse=True)

    atomic_write_text(RAW_JSON_PATH, json.dumps(all_items, ensure_ascii=False, indent=2))

    md_lines = [
        f"# Immunefi Active Bug Bounties Master Index (Total: {len(active_items)})\n",
        "| # | Project | Max Bounty | Payout | KYC | Pay2Submit | Primacy | Tech Stack | GitHub Repos | Assets |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: | :---: |"
    ]
    for i, item in enumerate(active_items, 1):
        m = item.get("meta", {})
        links = item.get("links", {})
        stack_str = ", ".join(item.get("tech_stack", []))
        gh_count = len(links.get("github_repos", []))
        asset_count = links.get("total_asset_links", 0)
        name_link = f"[{item['project_name']}]({item['info_url']})"
        md_lines.append(
            f"| {i} | {name_link} | **{m.get('max_bounty')}** | {m.get('payout_tokens')} | "
            f"{m.get('kyc')} | {m.get('pay_to_submit')} | {m.get('primacy')} | {stack_str} | "
            f"{gh_count}개 | {asset_count}개 |"
        )
    atomic_write_text(MASTER_INDEX_PATH, "\n".join(md_lines) + "\n")

    txt_chunks = [
        f"=== IMMUNEFI ACTIVE BUG BOUNTIES CLEAN DUMP (Total: {len(active_items)} projects) ===\n"
    ]
    for i, item in enumerate(active_items, 1):
        m = item.get("meta", {})
        links = item.get("links", {})
        gh_list = "\n  - ".join(links.get("github_repos", [])) or "None"
        exp_list = "\n  - ".join(links.get("explorer_links", [])[:15]) or "None"

        block = (
            f"\n==================== [{i}] {item['project_name']} ({item['slug']}) ====================\n"
            f"URL: {item['info_url']}\n"
            f"Max Bounty: {m.get('max_bounty')} | Vault: {m.get('vault_funds')} | Tokens: {m.get('payout_tokens')}\n"
            f"KYC: {m.get('kyc')} | Pay-to-Submit: {m.get('pay_to_submit')} | Primacy: {m.get('primacy')} | Updated: {m.get('last_updated')}\n"
            f"Tech Stack: {', '.join(item.get('tech_stack', []))}\n"
            f"GitHub Repositories:\n  - {gh_list}\n"
            f"Contract Explorers (Top 15):\n  - {exp_list}\n"
            f"--- [INFORMATION & RULES] ---\n"
            f"{item.get('information_clean', '')}\n"
            f"--- [SCOPE & TARGETS] ---\n"
            f"{item.get('scope_clean', '')}\n"
        )
        txt_chunks.append(block)

    atomic_write_text(AI_DIGEST_PATH, "".join(txt_chunks))


def main(max_items: int | None = None):
    existing_map = load_existing_data()
    if existing_map:
        print(f"기존 정상 수집 데이터 {len(existing_map)}건을 불러왔습니다. (이어서 진행)")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        print("1. 전체 버그바운티 프로젝트 슬러그 스캔 중...")
        all_slugs = discover_all_slugs(page)
        print(f"총 {len(all_slugs)}개의 고유 프로젝트 슬러그를 확보했습니다!\n")

        target_slugs = all_slugs[:max_items] if max_items else all_slugs

        for idx, slug in enumerate(target_slugs, start=1):
            if slug in existing_map:
                print(f"[{idx}/{len(target_slugs)}] 건너뜀 (수집 완료): {slug}")
                continue

            print(f"[{idx}/{len(target_slugs)}] 수집 중: {slug}")
            try:
                record = scrape_single_project(page, slug)
                existing_map[slug] = record
                status_tag = record.get("status")
                if status_tag == "ACTIVE":
                    mb = record["meta"]["max_bounty"]
                    gh = len(record["links"]["github_repos"])
                    print(f"  -> 완료: {record['project_name']} | Max: {mb} | GitHub: {gh}개")
                else:
                    print(f"  -> 스킵 ({status_tag})")

                save_all_outputs(existing_map)
            except Exception as e:
                print(f"  -> 오류 ({slug}): {e} (다음 실행 시 자동 재시도됨)")

            time.sleep(1.5)

        browser.close()

    save_all_outputs(existing_map)
    print("\n모든 수집 및 파일 생성이 완료되었습니다!")
    print(f"1) 전체 원본 JSON : {RAW_JSON_PATH}")
    print(f"2) 1차 선별용 표  : {MASTER_INDEX_PATH}")
    print(f"3) 2차 분석용 TXT : {AI_DIGEST_PATH}")


if __name__ == "__main__":
    main(max_items=None)